#!/usr/bin/env python3
"""Check iShare US structure and source references; does not prove UML semantics."""
from __future__ import annotations

import argparse
import re
from collections import Counter
from pathlib import Path

REQ = re.compile(r"\b(?:FR-M\d{2}-\d{2}(?:\.\d{2})?|BR-M\d{2}-\d{2})\b")
MODULE = re.compile(r"M\d{2}")
ROOT = Path(__file__).resolve().parents[4]
REQUIRED_SPEC = (
    "goal", "subject", "level", "primary", "supporting", "trigger",
    "preconditions", "success", "failure", "abstract", "common_contract",
)


def clean(value: str) -> str:
    """Remove presentation markup, preserving the value being validated."""
    value = value.strip().replace("\x60", "").replace("**", "")
    return "" if value in ("-", "—") else value


def items(value: str) -> list[str]:
    return [clean(x) for x in value.split(",") if clean(x)]


def table(text: str, marker: str) -> list[dict[str, str]]:
    """Read one marked Markdown table; an empty body is a valid empty table."""
    found = re.findall(r"<!--\s*uc:" + re.escape(marker) + r"\s*-->", text)
    if len(found) != 1:
        raise ValueError(f"Expected one uc:{marker} marker, got {len(found)}")
    tail = re.split(r"<!--\s*uc:" + re.escape(marker) + r"\s*-->", text, maxsplit=1)[1]
    lines = tail.lstrip().splitlines()
    rows = []
    for line in lines:
        if not line.strip().startswith("|"):
            break
        rows.append([clean(x.replace(r"\|", "|"))
                     for x in re.split(r"(?<!\\)\|", line.strip())[1:-1]])
    if len(rows) < 2:
        raise ValueError(f"Missing table after uc:{marker}")
    headers = rows[0]
    schemas = {
        "document": ("key", "value"),
        "sources": ("path", "version", "role"),
        "actors": ("id", "name", "kind", "parent", "boundary_reason", "sources"),
        "catalog": ("id", "name", "level", "primary", "supporting", "owner", "anchor", "sources"),
        "extension-points": ("id", "base", "at", "description"),
        "relations": ("type", "source", "target", "at", "condition", "return_to", "rationale", "sources"),
        "trace": ("requirement", "target", "coverage", "note"),
        "diagrams": ("id", "format", "renderer", "result", "artifact"),
    }
    expected_columns = ("key", "value") if marker.startswith("spec ") else schemas.get(marker, ())
    if not set(expected_columns).issubset(headers):
        raise ValueError(f"Missing columns in uc:{marker}")
    if len(headers) != len(set(headers)):
        raise ValueError(f"Duplicate columns in uc:{marker}")
    result = []
    for row in rows[2:]:
        if len(row) != len(headers):
            raise ValueError(f"Wrong column count in uc:{marker}: {row}")
        result.append(dict(zip(headers, row)))
    return result


def fields(rows: list[dict[str, str]]) -> dict[str, str]:
    keys = [row.get("key", "") for row in rows]
    if len(keys) != len(set(keys)):
        raise ValueError("Duplicate key in key/value table")
    return {row.get("key", ""): row.get("value", "") for row in rows}


def cycle(edges: list[tuple[str, str]]) -> bool:
    """Detect a directed cycle without recursing into an unbounded call stack."""
    graph: dict[str, list[str]] = {}
    indegree: Counter[str] = Counter()
    for start, end in edges:
        graph.setdefault(start, []).append(end)
        indegree.setdefault(start, 0)
        indegree[end] += 1
    ready = [node for node, degree in indegree.items() if degree == 0]
    seen = 0
    while ready:
        node = ready.pop()
        seen += 1
        for end in graph.get(node, []):
            indegree[end] -= 1
            if indegree[end] == 0:
                ready.append(end)
    return seen != len(indegree)


def source_index(path: Path) -> tuple[dict[str, str], str, str]:
    """Read active requirements only, excluding history and trace appendices."""
    text = path.read_text(encoding="utf-8-sig")
    body = re.split(r"(?m)^##\s+6\.", text, maxsplit=1)[0]
    index = {}
    for line in body.splitlines():
        match = re.match(r"^\|\s*((?:FR|BR)-M\d{2}-\d{2}(?:\.\d{2})?)\s*\|(.*)", line)
        if match and not re.search(r"\(\s*Đã bỏ\b", match[2], re.I):
            index[match[1]] = match[2]
    version = re.search(r"(?m)^phien_ban:\s*(.+)$", text)
    status = re.search(r"(?m)^trang_thai:\s*(.+)$", text)
    return index, version[1].strip() if version else "", status[1].strip() if status else ""


def validate(path: Path, repo: Path = ROOT, final: bool = False,
             scope: list[str] | None = None) -> tuple[list[str], list[str], str]:
    errors: list[str] = []
    warnings: list[str] = []
    text = path.read_text(encoding="utf-8-sig")
    meta = fields(table(text, "document"))
    mode = meta.get("mode", "")
    modules = items(meta.get("modules", ""))
    scope = scope or []
    label = f"{mode or 'unknown'}; modules={','.join(modules)}"
    if mode not in ("module", "overview", "partial"):
        errors.append("mode must be module, overview or partial")
    if not modules or any(not MODULE.fullmatch(m) for m in modules):
        errors.append("modules must contain IDs such as M01")
        return errors, warnings, label
    if mode == "module" and len(modules) != 1:
        errors.append("module mode requires exactly one owner module")
    for key in ("document_id", "skill_version", "source_baseline", "author", "date"):
        if not meta.get(key):
            errors.append(f"Missing document field: {key}")
    declared = items(meta.get("scope", ""))
    if scope:
        label += "; PARTIAL scope=" + ",".join(scope)
        if mode != "partial" or set(scope) != set(declared):
            errors.append("--scope must match scope metadata and mode=partial")
    elif mode == "partial" or declared != ["ALL"]:
        errors.append("Use mode=partial and matching --scope for a restricted scope")
    if re.search(r"\{\{[^{}\n]+\}\}", text):
        errors.append("Unfilled template placeholders")
    if "file:///" in text.lower():
        warnings.append("Machine-specific file URI; use relative document links")

    cache = {}
    def index(module: str):
        if module not in cache:
            source = repo / "docs/specs/fr" / f"FR-{module}.md"
            cache[module] = source_index(source) if source.exists() else ({}, "", "")
        return cache[module]

    def refs(value: str, context: str, required: bool = True):
        codes = REQ.findall(value)
        if required and not codes:
            errors.append(f"{context}: missing FR/BR evidence")
        for code in codes:
            module = code.split("-")[1]
            if code not in index(module)[0]:
                errors.append(f"{context}: unknown or retired requirement {code}")

    expected = set()
    for module in modules:
        active, _, status = index(module)
        if not active:
            errors.append(f"Missing/empty FR-{module}.md")
        if status != "Đã chốt":
            errors.append(f"FR-{module} is not approved (Đã chốt)")
        expected.update(active)
    if scope:
        for root in scope:
            if root not in expected:
                errors.append(f"Unknown scope root: {root}")
        expected = {code for code in expected
                    if any(code == root or code.startswith(root + ".") for root in scope)}
    elif mode == "overview":
        expected = {code for code in expected
                    if re.fullmatch(r"FR-M\d{2}-\d{2}", code)}
        warnings.append("OVERVIEW: group inventory only; no claim of detailed behavior coverage")

    sources = table(text, "sources")
    baseline = {}
    for row in sources:
        source_path = row.get("path", "").replace("\\", "/")
        match = re.fullmatch(r"docs/specs/fr/FR-(M\d{2})\.md", source_path)
        if not match:
            errors.append(f"Invalid FR source path: {source_path}")
            continue
        module = match[1]
        baseline[module] = row.get("version", "")
        if baseline[module] != index(module)[1]:
            errors.append(f"Stale baseline for {module}: {baseline[module]} != {index(module)[1]}")
    for module in modules:
        if module not in baseline:
            errors.append(f"Missing source baseline: {module}")

    anchor_list = re.findall(r'<a\s+id="([^"]+)"\s*></a>', text)
    anchors = set(anchor_list)
    for anchor, count in Counter(anchor_list).items():
        if count > 1:
            errors.append(f"Duplicate anchor: {anchor}")
    def anchor(value: str, context: str, owner: str = ""):
        if not value.startswith("#") or value[1:] not in anchors:
            errors.append(f"{context}: missing local anchor {value!r}")
        elif owner and not value[1:].startswith(owner.lower() + "-"):
            errors.append(f"{context}: anchor does not belong to {owner}")

    actors = table(text, "actors")
    actor_ids = [row.get("id", "") for row in actors]
    for value, count in Counter(actor_ids).items():
        if not value or count > 1:
            errors.append(f"Empty or duplicate actor ID: {value!r}")
    actor_edges = []
    for row in actors:
        if row.get("kind") not in ("human", "external-system"):
            errors.append(f"{row.get('id')}: actor kind must be external")
        if not row.get("boundary_reason"):
            errors.append(f"{row.get('id')}: missing boundary rationale")
        parent = row.get("parent", "")
        if parent:
            if parent not in actor_ids:
                errors.append(f"Unknown actor parent: {parent}")
            actor_edges.append((row.get("id", ""), parent))
        refs(row.get("sources", ""), row.get("id", "actor"))
    if cycle(actor_edges):
        errors.append("Actor generalization cycle")

    catalog = table(text, "catalog")
    uc_ids = [row.get("id", "") for row in catalog]
    if not catalog:
        errors.append("Empty UC catalog")
    for value, count in Counter(uc_ids).items():
        if not value or count > 1:
            errors.append(f"Empty or duplicate UC ID: {value!r}")
    for row in catalog:
        uid = row.get("id", "")
        if row.get("level") not in ("Summary", "User goal", "Subfunction"):
            errors.append(f"{uid}: invalid goal level")
        if row.get("owner") not in modules:
            warnings.append(f"{uid}: related UC owner outside selected modules")
        anchor(row.get("anchor", ""), uid)
        refs(row.get("sources", ""), uid)
        for actor in items(row.get("primary", "")) + items(row.get("supporting", "")):
            if actor not in actor_ids:
                errors.append(f"{uid}: unknown actor {actor}")
        if row.get("level") == "User goal" and not row.get("primary"):
            errors.append(f"{uid}: User goal needs a primary actor")
        if mode != "overview" and row.get("owner") in modules and row.get("level") != "Summary":
            try:
                spec = fields(table(text, f"spec {uid}"))
            except ValueError as exc:
                errors.append(f"{uid}: {exc}")
                continue
            for field in REQUIRED_SPEC:
                if field not in spec or (field != "supporting" and not spec.get(field)):
                    errors.append(f"{uid}: missing contract field {field}")
            for field in ("primary", "supporting", "level"):
                if clean(spec.get(field, "")) != row.get(field, ""):
                    errors.append(f"{uid}: catalog/spec mismatch for {field}")

    points = table(text, "extension-points")
    point_ids = [row.get("id", "") for row in points]
    for pid, count in Counter(point_ids).items():
        if not pid or count > 1:
            errors.append(f"Empty or duplicate extension point: {pid!r}")
    point_map = {row.get("id", ""): row for row in points}
    for row in points:
        base = row.get("base", "")
        if base not in uc_ids:
            errors.append(f"Extension point has unknown base: {base}")
        anchor(row.get("at", ""), row.get("id", "extension point"), base)

    generalizations, includes = [], []
    for row in table(text, "relations"):
        kind, start, end = (row.get(k, "") for k in ("type", "source", "target"))
        context = f"{kind} {start}->{end}"
        if start not in uc_ids or end not in uc_ids or start == end:
            errors.append(f"{context}: invalid endpoints")
        if kind not in ("include", "extend", "generalization"):
            errors.append(f"{context}: unknown relation type")
        if not row.get("rationale"):
            errors.append(f"{context}: missing rationale")
        refs(row.get("sources", ""), context)
        if kind == "extend":
            point = point_map.get(row.get("at", ""))
            if not point or point.get("base") != end:
                errors.append(f"{context}: extension point must belong to base")
            if not row.get("condition"):
                errors.append(f"{context}: missing condition")
            result = row.get("return_to", "")
            if not result.startswith("END:"):
                anchor(result, context + " return", end)
            elif not result[4:].strip():
                errors.append(f"{context}: missing END outcome")
        else:
            anchor(row.get("at", ""), context, start if kind == "include" else end)
            if kind == "include":
                includes.append((start, end))
                result = row.get("return_to", "")
                if not result.startswith("END:"):
                    anchor(result, context + " return", start)
                elif not result[4:].strip():
                    errors.append(f"{context}: missing END outcome")
            elif kind == "generalization":
                generalizations.append((start, end))
    if cycle(generalizations):
        errors.append("UC generalization cycle")
    if cycle(includes):
        warnings.append("Include cycle: review recursion and termination manually")

    trace = table(text, "trace")
    trace_codes = [row.get("requirement", "") for row in trace]
    for code, count in Counter(trace_codes).items():
        if count > 1:
            errors.append(f"Duplicate trace row: {code}")
    full = set()
    for row in trace:
        code = row.get("requirement", "")
        if not REQ.fullmatch(code):
            errors.append(f"Invalid trace requirement: {code}")
        refs(code, "trace")
        coverage = row.get("coverage", "")
        if coverage not in ("Đủ", "Một phần", "Chưa"):
            errors.append(f"{code}: invalid coverage")
        targets = items(row.get("target", ""))
        if coverage == "Đủ" and not targets:
            errors.append(f"{code}: full coverage needs a target")
        for target in targets:
            anchor(target, code)
        if coverage == "Đủ" and targets:
            full.add(code)
        elif not row.get("note"):
            errors.append(f"{code}: incomplete coverage needs explanation")
    missing = sorted(expected - full)
    if missing:
        message = "Not fully mapped: " + ", ".join(missing)
        (errors if final else warnings).append(message)
    for module in cache:
        if module not in baseline:
            errors.append(f"Referenced FR lacks source baseline: {module}")

    approved = items(meta.get("approved_steps", ""))
    completed = items(meta.get("completed_steps", ""))
    if any(x not in [str(i) for i in range(1, 8)] for x in approved + completed):
        errors.append("Invalid completed_steps/approved_steps")
    if not set(approved).issubset(completed):
        errors.append("Approved step is not completed")
    if meta.get("status") not in ("Đang soạn", "Chờ duyệt", "Đã duyệt"):
        errors.append("Invalid approval status")
    if meta.get("status") == "Đã duyệt":
        if "7" not in approved or not meta.get("approval_evidence"):
            errors.append("Approved document needs step 7 approval evidence")
    if final:
        if set(completed) != {str(i) for i in range(1, 8)}:
            errors.append("Final review requires all steps completed")
        if meta.get("semantic_review") != "pass":
            errors.append("Final review needs recorded semantic review")
        diagram_rows = table(text, "diagrams")
        has_diagrams = bool(re.search(r"(?m)^\x60{3}(plantuml|mermaid)\s*$", text))
        if (mode in ("module", "overview") or has_diagrams) and (
            meta.get("diagram_check") != "pass" or not diagram_rows
        ):
            errors.append("Final review needs diagram/render evidence")
        elif meta.get("diagram_check") not in ("pass", "not-applicable"):
            errors.append("Diagram check not completed")
        for row in diagram_rows:
            if row.get("result") != "pass" or not row.get("renderer") or not row.get("artifact"):
                errors.append(f"Diagram {row.get('id')}: incomplete render evidence")
            if row.get("format") == "illustrative":
                errors.append(f"Diagram {row.get('id')}: illustrative view is not formal UML")
    warnings.append("Manual checks remain: source meaning, goal quality, relation semantics, diagrams")
    return errors, warnings, label


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("document", type=Path)
    parser.add_argument("--repo", type=Path, default=ROOT)
    parser.add_argument("--scope", nargs="+", help="Explicit partial scope; must match metadata")
    parser.add_argument("--final", action="store_true")
    args = parser.parse_args()
    try:
        errors, warnings, label = validate(
            args.document, args.repo, args.final, args.scope
        )
    except (OSError, ValueError) as exc:
        print(f"ERROR: {exc}")
        return 1
    print(f"SCOPE: {label}")
    for error in errors:
        print(f"ERROR: {error}")
    for warning in warnings:
        print(f"WARN: {warning}")
    print(f"STRUCTURAL RESULT: errors={len(errors)} warnings={len(warnings)}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
