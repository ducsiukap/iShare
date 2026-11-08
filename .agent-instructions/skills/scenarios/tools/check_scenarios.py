#!/usr/bin/env python3
"""Lint scenario Markdown. Checks structure and graph properties, not business truth."""

from __future__ import annotations

import argparse
from collections import deque
from pathlib import Path
import re
import sys

REQ = re.compile(r"\b(?:FR|BR)-M\d{2}-\d+(?:\.\d+)?\b")
SC = re.compile(r"<!-- sc:scenario (SC-M\d{2}-\d{3}) -->")
MARK = re.compile(r"<!-- ((?:sc|uc):[^\n>]+?) -->")
TERMINALS = {"SUCCESS", "REJECTED", "CANCELLED", "HANDED_OFF"}
STEP_COLUMNS = {"step", "subject", "action", "data", "next", "sources"}


def cells(line: str) -> list[str]:
    """Split a Markdown row while preserving escaped pipe characters."""
    return [c.strip().replace(r"\|", "|") for c in re.split(r"(?<!\\)\|", line.strip()[1:-1])]


def tables(text: str, errors: list[str]) -> dict[str, list[dict[str, str]]]:
    """Read tables immediately after named markers; reject ambiguous tables."""
    result = {}
    for match in MARK.finditer(text):
        name = match[1].strip()
        lines = text[match.end():].lstrip().splitlines()
        if not lines or not lines[0].startswith("|"):
            continue
        if name in result:
            errors.append(f"Duplicate table marker: {name}")
            continue
        header = cells(lines[0])
        if len(header) != len(set(header)):
            errors.append(f"Duplicate column: {name}")
        rows = []
        for line in lines[1:]:
            if not line.startswith("|"):
                break
            values = cells(line)
            if all(re.fullmatch(r":?-+:?", v) for v in values):
                continue
            if len(values) != len(header):
                errors.append(f"Column count mismatch: {name}: {line}")
                continue
            rows.append(dict(zip(header, values)))
        result[name] = rows
    return result


def keyed(rows: list[dict[str, str]], key: str, context: str, errors: list[str]) -> dict:
    result = {}
    for row in rows:
        value = row.get(key, "")
        if not value or value in result:
            errors.append(f"Missing/duplicate {key}: {context}: {value!r}")
        result[value] = row
    return result


def ids(value: str, prefix: str) -> set[str]:
    return set(re.findall(rf"\b{prefix}-M\d{{2}}-\d{{3}}\b", value))


def reachable(roots: set[str], graph: dict[str, set[str]]) -> set[str]:
    seen, queue = set(roots), deque(roots)
    while queue:
        for target in graph.get(queue.popleft(), set()):
            if target not in seen:
                seen.add(target)
                queue.append(target)
    return seen


def check_graph(sid: str, block: str, data: dict, actors: set[str], errors: list[str]) -> int:
    """Check replacement branches, re-entry alternation, reachability and termination."""
    headings = list(re.finditer(r"^#### ([1-6])\. (.+)$", block, re.M))
    if [h[1] for h in headings] != list("123456"):
        errors.append(f"{sid}: expected six ordered sections 1..6")
    for i, heading in enumerate(headings):
        end = headings[i + 1].start() if i + 1 < len(headings) else len(block)
        content = re.sub(r"<!--.*?-->", "", block[heading.end():end], flags=re.S).strip()
        if not content:
            errors.append(f"{sid}: section {heading[1]} is empty")
    required = [f"sc:{name} {sid}" for name in ("post", "main", "exceptions")]
    for marker in required:
        if marker not in data:
            errors.append(f"{sid}: missing table {marker}")
    post = keyed(data.get(required[0], []), "result", sid, errors)
    for result, row in post.items():
        if result not in TERMINALS or not row.get("condition", "").strip(" -"):
            errors.append(f"{sid}: invalid/empty postcondition {result}")
    main = data.get(required[1], [])
    subjects = {row.get("subject") for row in main}
    if "SYSTEM" not in subjects or not subjects.intersection(actors):
        errors.append(f"{sid}: main path requires both actor and SYSTEM interaction")
    if main and (main[-1].get("subject") != "SYSTEM" or main[-1].get("next") != "END:SUCCESS"):
        errors.append(f"{sid}: main path must finish with SYSTEM returning END:SUCCESS for the actor goal")
    exceptions = keyed(data.get(required[2], []), "id", sid, errors)
    groups = {"main": main}
    for key, rows in data.items():
        if key.startswith(f"sc:branch {sid} "):
            groups[key.split()[-1]] = rows
    for eid in set(groups) - {"main"} - set(exceptions):
        errors.append(f"{sid}: orphan branch {eid}")
    nodes = {}
    for group, rows in groups.items():
        if not rows:
            errors.append(f"{sid}: empty step list {group}")
        for i, row in enumerate(rows):
            step = row.get("step", "")
            pattern = r"M[1-9]\d*" if group == "main" else re.escape(group) + r"\.[1-9]\d*"
            if not re.fullmatch(pattern, step) or step in nodes:
                errors.append(f"{sid}: invalid/duplicate step {step}")
            if STEP_COLUMNS - row.keys() or any(not row.get(c, "").strip(" -") for c in STEP_COLUMNS):
                errors.append(f"{sid}/{step}: missing step content/columns")
            if row.get("subject") not in actors | {"SYSTEM"}:
                errors.append(f"{sid}/{step}: invalid subject {row.get('subject')}")
            if i + 1 < len(rows) and row.get("next") != rows[i + 1].get("step"):
                errors.append(f"{sid}/{step}: next must follow the displayed step order")
            nodes[step] = row
    if not main:
        return len(exceptions)
    graph = {step: set() for step in nodes}
    terminal_nodes = set()
    for step, row in nodes.items():
        target = row.get("next", "")
        if target.startswith("END:"):
            result = target[4:]
            if result not in post or result not in TERMINALS:
                errors.append(f"{sid}/{step}: terminal without postcondition {target}")
            terminal_nodes.add(step)
        elif target not in nodes:
            errors.append(f"{sid}/{step}: unknown next step {target}")
        else:
            graph[step].add(target)
            if row.get("subject") == nodes[target].get("subject"):
                errors.append(f"{sid}: same subject on edge {step} -> {target}")
    # The main path must end, not hide an undeclared loop at its last step.
    if not main[-1].get("next", "").startswith("END:"):
        errors.append(f"{sid}: main path must end with an explicit outcome")
    main_ids = {row.get("step") for row in main}
    roots = {main[0].get("step", "")}
    for eid, branch in exceptions.items():
        at, entry = branch.get("at", ""), branch.get("entry", "")
        if not re.fullmatch(r"E[1-9]\d*", eid):
            errors.append(f"{sid}: invalid exception ID {eid}")
        if branch.get("kind") not in {"system", "user-choice"} or not branch.get("condition", "").strip(" -"):
            errors.append(f"{sid}/{eid}: missing kind/condition")
        steps = groups.get(eid, [])
        if at not in main_ids or not steps or entry != steps[0].get("step"):
            errors.append(f"{sid}/{eid}: invalid replacement point or branch entry")
            continue
        if nodes[at].get("subject") != nodes[entry].get("subject"):
            errors.append(f"{sid}/{eid}: first subject must match the replaced step")
        if at == main[0].get("step"):
            roots.add(entry)
        # Include retry edges that re-enter a step with exceptions.
        for step, row in nodes.items():
            if row.get("next") == at:
                graph[step].add(entry)
    unreachable = set(nodes) - reachable(roots, graph)
    if unreachable:
        errors.append(f"{sid}: unreachable steps {sorted(unreachable)}")
    reverse = {step: set() for step in nodes}
    for source, targets in graph.items():
        for target in targets:
            reverse[target].add(source)
    stranded = set(nodes) - reachable(terminal_nodes, reverse)
    if stranded:
        errors.append(f"{sid}: no path to an outcome from {sorted(stranded)}")
    return len(exceptions)


def validate(text: str, fr_texts: list[str], us_text: str, final: bool = False) -> tuple[list[str], dict]:
    """Validate an authored document against supplied FR and US snapshots."""
    errors = []
    data = tables(text, errors)
    upstream = tables(us_text, errors)
    meta = {r.get("key"): r.get("value", "") for r in data.get("sc:document", [])}
    if not re.fullmatch(r"M\d{2}", meta.get("module", "")):
        errors.append("Missing/invalid module metadata")
    catalog = keyed(data.get("sc:ucs", []), "id", "UC inventory", errors)
    actors = keyed(data.get("sc:actors", []), "id", "actors", errors)
    source_ucs = {r.get("id") for r in upstream.get("uc:catalog", [])}
    source_actors = {r.get("id") for r in upstream.get("uc:actors", [])}
    if not source_ucs:
        errors.append("US has no uc:catalog; inventory cannot be verified")
    if set(actors) - source_actors:
        errors.append(f"Actors absent from US: {sorted(set(actors) - source_actors)}")
    scope = meta.get("scope", "")
    expected = source_ucs if scope == "ALL" else ids(scope, "UC")
    if not expected or expected - source_ucs:
        errors.append("Scope is empty or references UC IDs absent from US")
    if expected - set(catalog) or set(catalog) - source_ucs:
        errors.append(f"UC inventory mismatch: missing={sorted(expected - set(catalog))}, unknown={sorted(set(catalog) - source_ucs)}")
    source_pairs = {(r.get("core"), r.get("sub")) for r in upstream.get("uc:decomposition", [])}
    pairs = {(r.get("core"), r.get("sub")) for r in data.get("sc:decomposition", [])}
    expected_pairs = {p for p in source_pairs if scope == "ALL" or p[1] in expected}
    if expected_pairs - pairs or pairs - source_pairs:
        errors.append("Core/sub mapping differs from the in-scope US decomposition")
    matches = list(SC.finditer(text))
    scenario_ids = [m[1] for m in matches]
    if (not matches and any(r.get("treatment") == "scenario" for r in catalog.values())) or len(set(scenario_ids)) != len(scenario_ids):
        errors.append("Missing scenarios or duplicate scenario IDs")
    flows = keyed(data.get("sc:flows", []), "id", "business flows", errors)
    claimed = []
    for fid, flow in flows.items():
        sid, uc = flow.get("scenario", ""), flow.get("uc", "")
        if not re.fullmatch(r"BF-" + re.escape(meta.get("module", "")) + r"-\d{3}", fid):
            errors.append(f"Invalid flow ID: {fid}")
        if sid not in scenario_ids or uc not in catalog or catalog.get(uc, {}).get("treatment") != "scenario":
            errors.append(f"{fid}: missing scenario or non-executable/unknown UC owner")
        if sid not in ids(catalog.get(uc, {}).get("scenarios", ""), "SC"):
            errors.append(f"{fid}: owner UC does not list scenario {sid}")
        for field in ("trigger", "goal", "completion", "rationale"):
            if not flow.get(field, "").strip(" -"):
                errors.append(f"{fid}: missing actor-journey field {field}")
        primary = flow.get("primary", "")
        steps = data.get(f"sc:main {sid}", [])
        if primary not in actors or primary == "SYSTEM":
            errors.append(f"{fid}: missing/invalid primary actor")
        elif not steps or steps[0].get("subject") != primary:
            errors.append(f"{fid}: main path must start with the primary actor")
        covered = ids(flow.get("covered_ucs", ""), "UC")
        if uc not in covered or covered - set(catalog):
            errors.append(f"{fid}: covered_ucs must include owner and only known UC IDs")
        for covered_uc in covered:
            if sid not in ids(catalog.get(covered_uc, {}).get("scenarios", ""), "SC"):
                errors.append(f"{fid}: covered UC {covered_uc} does not list scenario {sid}")
        claimed.append(sid)
    if set(claimed) != set(scenario_ids) or len(claimed) != len(set(claimed)):
        errors.append("Each business flow needs its own six-part scenario; unmapped or reused scenario")
    for uc, row in catalog.items():
        treatment = row.get("treatment")
        refs = ids(row.get("scenarios", ""), "SC")
        if treatment not in {"scenario", "embedded", "aggregate", "abstract", "background", "gap"}:
            errors.append(f"{uc}: invalid treatment")
        if treatment not in {"gap", "background"} and (not refs or refs - set(scenario_ids)):
            errors.append(f"{uc}: missing/unknown scenario coverage")
        if treatment != "scenario" and not row.get("rationale", "").strip(" -"):
            errors.append(f"{uc}: missing disposition rationale")
        participating = {r.get("scenario") for r in flows.values() if uc in ids(r.get("covered_ucs", ""), "UC")}
        if treatment in {"scenario", "embedded"} and refs != participating:
            errors.append(f"{uc}: scenario coverage does not match participating flows")
        if treatment == "scenario" and not any(r.get("uc") == uc for r in flows.values()):
            errors.append(f"{uc}: scenario treatment requires an owned actor goal")
        if treatment == "embedded":
            locations = re.findall(r"\b(SC-M\d{2}-\d{3})/((?:M[1-9]\d*|E[1-9]\d*\.[1-9]\d*))\b", row.get("coverage", ""))
            if not locations or {sid for sid, _ in locations} != refs:
                errors.append(f"{uc}: embedded coverage needs SC/step locations for every scenario")
            for sid, step in locations:
                marker = f"sc:main {sid}" if step.startswith("M") else f"sc:branch {sid} {step.split('.')[0]}"
                if not any(r.get("step") == step for r in data.get(marker, [])):
                    errors.append(f"{uc}: unknown embedded coverage step {sid}/{step}")
        if treatment == "background" and (refs or not row.get("coverage", "").strip(" -")):
            errors.append(f"{uc}: background needs a rule reference and must not own scenarios")
        if final and treatment == "gap":
            errors.append(f"{uc}: unresolved gap in final scope")
    defined = set()
    for source in fr_texts:
        defined.update(re.findall(r"(?m)^\|\s*((?:FR|BR)-M\d{2}-\d+(?:\.\d+)?)\s*\|", source))
    if not defined:
        errors.append("No FR/BR definitions found in supplied sources")
    for name, rows in data.items():
        for row in rows:
            if "sources" not in row:
                continue
            refs = set(REQ.findall(row["sources"]))
            if not refs or refs - defined:
                errors.append(f"{name}: missing/unknown FR/BR sources {sorted(refs - defined)}")
    branch_count = 0
    for i, match in enumerate(matches):
        sid = match[1]
        if not sid.startswith(f"SC-{meta.get('module')}-"):
            errors.append(f"Scenario outside module: {sid}")
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        block = text[match.end():end]
        if f"<!-- sc:end {sid} -->" not in block:
            errors.append(f"{sid}: missing end marker")
        block = block.split(f"<!-- sc:end {sid} -->")[0]
        branch_count += check_graph(sid, block, data, set(actors), errors)
    if re.search(r"\{\{[^}]+\}\}", text):
        errors.append("Unfilled template placeholders")
    if meta.get("status") == "Đã duyệt" and not meta.get("approval_evidence", "").strip(" -"):
        errors.append("Approved status lacks approval evidence")
    counts = {"use_cases": len(catalog), "flows": len(flows), "scenarios": len(matches), "exceptions": branch_count}
    return errors, counts


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("document", type=Path)
    parser.add_argument("--fr", type=Path, action="append", required=True, help="Repeat for related FR documents")
    parser.add_argument("--us", type=Path, required=True)
    parser.add_argument("--final", action="store_true", help="Also reject UC inventory entries marked gap")
    args = parser.parse_args(argv)
    try:
        read = lambda path: path.read_text(encoding="utf-8-sig")
        errors, counts = validate(read(args.document), [read(p) for p in args.fr], read(args.us), args.final)
    except (OSError, UnicodeError) as exc:
        print(f"ERROR: Cannot read input: {exc}", file=sys.stderr)
        return 2
    for error in errors:
        print(f"ERROR: {error}")
    print(f"{'FAIL' if errors else 'PASS'}: {counts}; structural checks only; business review still required.")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
