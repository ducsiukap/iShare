"""Behavioral checks for source coverage, graph integrity and approval boundaries.

Fixtures are synthetic and render records are stubs, not UML or render evidence.
"""
import tempfile
import unittest
from pathlib import Path

from check_us import cycle, fields, table, validate


def marked(name, headers, rows=()):
    return f"<!-- uc:{name} -->\n| " + " | ".join(headers) + " |\n|" + "|".join(
        "---" for _ in headers
    ) + "|\n" + "".join("| " + " | ".join(row) + " |\n" for row in rows) + "\n"


def document():
    metadata = {
        "document_id": "US-M01", "skill_version": "2.2", "mode": "module",
        "modules": "M01", "scope": "ALL", "status": "Chờ duyệt",
        "current_step": "7", "completed_steps": "1, 2, 3, 4, 5, 6, 7",
        "approved_steps": "1, 2, 3, 4, 5, 6", "source_baseline": "M01 1.0",
        "author": "Synthetic fixture", "date": "2026-10-28",
        "approval_evidence": "-", "semantic_review": "pass", "diagram_check": "pass",
    }
    result = marked("document", ["key", "value"], metadata.items())
    result += marked("sources", ["path", "version", "role"], [
        ["docs/specs/fr/FR-M01.md", "1.0", "owner"]
    ])
    result += marked("actors", ["id", "name", "kind", "parent", "boundary_reason", "sources"], [
        ["ACT-001", "External user", "human", "-", "Outside subject", "FR-M01-01"]
    ])
    catalog = [["UC-M01-000", "Core capability", "core", "Summary", "ACT-001", "-",
                "M01", "#uc-m01-000", "FR-M01-01"]]
    for number in (1, 2):
        uid = f"UC-M01-00{number}"
        catalog.append([uid, f"Goal {number}", "sub", "User goal", "ACT-001", "-", "M01",
                        f"#{uid.lower()}", "FR-M01-01.01"])
    result += marked("catalog", ["id", "name", "tier", "level", "primary", "supporting", "owner",
                                 "anchor", "sources"], catalog)
    result += marked("decomposition", ["core", "sub", "rationale", "sources"], [
        ["UC-M01-000", f"UC-M01-00{number}", "Contributes to core goal", "FR-M01-01.01"]
        for number in (1, 2)
    ])
    result += marked("module-models", ["module", "path", "baseline"])
    result += '<a id="uc-m01-000"></a>\n<a id="uc-m01-000-main-1"></a>\n<a id="uc-m01-000-main-2"></a>\n'
    for number in (1, 2):
        uid = f"UC-M01-00{number}"
        result += f'<a id="{uid.lower()}"></a>\n'
        spec = {key: "Fixture value" for key in [
            "goal", "subject", "trigger", "preconditions", "success", "failure", "common_contract"
        ]}
        spec.update(level="User goal", primary="ACT-001", supporting="-", abstract="false")
        result += marked(f"spec {uid}", ["key", "value"], spec.items())
        for suffix in ("main-1", "main-2", "contract"):
            result += f'<a id="{uid.lower()}-{suffix}"></a>\n'
    result += marked("extension-points", ["id", "base", "at", "description"])
    result += marked("relations", ["type", "source", "target", "at", "condition",
                                  "return_to", "rationale", "sources"])
    result += marked("trace", ["requirement", "target", "coverage", "note"], [
        [code, "#uc-m01-001-main-1", "Đủ", "Synthetic mapping"]
        for code in ["FR-M01-01", "FR-M01-01.01", "FR-M01-01.02", "BR-M01-01"]
    ])
    result += marked("diagrams", ["id", "view", "focus", "members", "format", "renderer", "result", "artifact"], [
        ["D1", "core", "-", "UC-M01-000", "plantuml", "RENDER-STUB", "pass", "STUB-core.svg"],
        ["D2", "detail", "UC-M01-000", "UC-M01-000, UC-M01-001, UC-M01-002", "plantuml", "RENDER-STUB", "pass", "STUB-detail.svg"]
    ])
    return result


class USChecks(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.repo = Path(self.tmp.name)
        self.fr = self.repo / "docs/specs/fr/FR-M01.md"
        self.fr.parent.mkdir(parents=True)
        self.fr.write_text(
            "---\nphien_ban: 1.0\ntrang_thai: Đã chốt\n---\n"
            "## 4. Functions\n| FR-M01-01 | Goal |\n"
            "## 5. Requirements\n| FR-M01-01.01 | Action |\n"
            "| FR-M01-01.02 | Keep other data |\n"
            "| BR-M01-01 | Policy |\n"
            "| FR-M01-02 | (Đã bỏ ở phiên bản 1.0) |\n"
            "## 6. History\n| FR-M01-99 | Historical reference |\n",
            encoding="utf-8",
        )
        self.path = self.repo / "US-M01.md"

    def check(self, text=None, final=True, scope=None):
        self.path.write_text(document() if text is None else text, encoding="utf-8")
        return validate(self.path, self.repo, final, scope)

    def test_complete_module_passes_structure(self):
        errors, warnings, _ = self.check()
        self.assertEqual(errors, [])
        self.assertTrue(any("Manual checks" in warning for warning in warnings))

    def test_missing_detail_fails_final_even_with_group_mapped(self):
        text = document().replace("| FR-M01-01.02 | #uc-m01-001-main-1 | Đủ | Synthetic mapping |\n", "")
        errors, _, _ = self.check(text)
        self.assertTrue(any("FR-M01-01.02" in error for error in errors))
        errors, warnings, _ = self.check(text, final=False)
        self.assertEqual(errors, [])
        self.assertTrue(any("Not fully mapped" in warning for warning in warnings))

    def test_explicit_partial_scope_does_not_claim_module_completion(self):
        text = document().replace("| mode | module |", "| mode | partial |")
        text = text.replace("| scope | ALL |", "| scope | FR-M01-01.01 |")
        text = text.replace("| FR-M01-01.02 | #uc-m01-001-main-1 | Đủ | Synthetic mapping |\n", "")
        errors, _, label = self.check(text, scope=["FR-M01-01.01"])
        self.assertEqual(errors, [])
        self.assertIn("PARTIAL", label)
        self.assertTrue(self.check(text)[0])
        self.assertTrue(self.check(text, scope=["FR-M01-77"])[0])

    def test_overview_only_checks_groups(self):
        text = self.overview()
        text = text.replace("| FR-M01-01.02 | #uc-m01-000 | Đủ | Synthetic mapping |\n", "")
        errors, warnings, _ = self.check(text)
        self.assertEqual(errors, [])
        self.assertTrue(any("OVERVIEW" in value for value in warnings))

    def overview(self):
        module_path = self.repo / "docs/specs/us/US-M01.md"
        module_path.parent.mkdir(parents=True, exist_ok=True)
        module_path.write_text(document(), encoding="utf-8")
        text = document().replace("| mode | module |", "| mode | overview |")
        text = "\n".join(line for line in text.splitlines()
                         if not line.startswith(("| UC-M01-001 | Goal", "| UC-M01-002 | Goal",
                                                 "| UC-M01-000 | UC-M01-00"))) + "\n"
        text = text.replace("#uc-m01-001-main-1 | Đủ", "#uc-m01-000 | Đủ")
        text = text.replace("| D1 | core |", "| D1 | system |")
        text = "\n".join(line for line in text.splitlines() if not line.startswith("| D2 | detail |")) + "\n"
        text = text.replace('\n\n<a id="uc-m01-000">',
                            '\n| M01 | docs/specs/us/US-M01.md | M01 1.0 |\n\n<a id="uc-m01-000">')
        return text

    def test_module_requires_both_tiers_and_full_mapping(self):
        text = document().replace("| core | Summary |", "| unknown | Summary |")
        errors = self.check(text)[0]
        self.assertTrue(any("missing core UC tier" in e for e in errors))
        self.assertTrue(any("declared core" in e for e in errors))
        text = "\n".join(line for line in document().splitlines()
                         if not line.startswith("| UC-M01-000 | UC-M01-00"))
        errors = self.check(text)[0]
        self.assertTrue(any("core has no sub" in e for e in errors))
        self.assertTrue(any("orphan sub" in e for e in errors))

    def test_shared_sub_uses_one_id_without_uml_inheritance(self):
        text = document().replace(
            '<a id="uc-m01-000"></a>',
            '<a id="uc-m01-000"></a>\n<a id="uc-m01-009"></a>'
        )
        text = text.replace("\n\n<!-- uc:decomposition -->",
                            "\n| UC-M01-009 | Other capability | core | Summary | ACT-001 | - | M01 | #uc-m01-009 | FR-M01-01 |\n\n<!-- uc:decomposition -->")
        text = text.replace("\n\n<!-- uc:module-models -->",
                            "\n| UC-M01-009 | UC-M01-001 | Shared contribution | FR-M01-01.01 |\n\n<!-- uc:module-models -->")
        text = text.rstrip() + "\n| D3 | detail | UC-M01-009 | UC-M01-009, UC-M01-001 | plantuml | RENDER-STUB | pass | STUB-other.svg |\n"
        self.assertEqual(self.check(text)[0], [])

    def test_each_core_detail_must_show_core_and_all_subs(self):
        text = document().replace("UC-M01-000, UC-M01-001, UC-M01-002 | plantuml",
                                  "UC-M01-001 | plantuml")
        errors = self.check(text)[0]
        for uid in ("UC-M01-000", "UC-M01-002"):
            self.assertTrue(any("missing detail UC member " + uid in e for e in errors))
        text = document().replace("| D2 | detail | UC-M01-000 |", "| D2 | detail | UC-M01-001 |")
        errors = self.check(text)[0]
        self.assertTrue(any("focus must be a core" in e for e in errors))
        self.assertTrue(any("missing per-core detail" in e for e in errors))

    def test_relations_allow_core_sub_and_sub_sub_in_same_detail(self):
        text = self.relation("include", start="UC-M01-000", end="UC-M01-001",
                             at="#uc-m01-000-main-1", return_to="#uc-m01-000-main-2")
        text = text.replace("\n\n<!-- uc:trace -->",
                            "\n| extend | UC-M01-002 | UC-M01-001 | EP1 | guard | #uc-m01-001-main-2 | Sub extends sub | FR-M01-01.01 |\n\n<!-- uc:trace -->")
        self.assertEqual(self.check(text)[0], [])

    def test_overview_rejects_subs_and_core_drift(self):
        text = self.overview().replace("| Core capability |", "| Changed core |")
        self.assertTrue(any("overview name differs" in e for e in self.check(text)[0]))
        text = self.overview().replace("| core | Summary |", "| sub | Summary |")
        self.assertTrue(any("only module core" in e for e in self.check(text)[0]))
        text = self.overview().replace("docs/specs/us/US-M01.md | M01 1.0",
                                       "docs/specs/us/US-M01.md | old")
        self.assertTrue(any("stale module-models" in e for e in self.check(text)[0]))

    def test_complete_module_needs_core_and_detail_views(self):
        text = document().replace("| D2 | detail |", "| D2 | core |")
        self.assertTrue(any("missing detail diagram" in e for e in self.check(text)[0]))
        text = self.overview().replace("| D1 | system |", "| D1 | core |")
        self.assertTrue(any("missing system diagram" in e for e in self.check(text)[0]))

    def test_retired_unknown_and_stale_sources(self):
        text = document().replace("FR-M01-01.01", "FR-M01-02").replace(
            "docs/specs/fr/FR-M01.md | 1.0", "docs/specs/fr/FR-M01.md | 0.9"
        )
        errors, _, _ = self.check(text)
        self.assertTrue(any("retired" in value for value in errors))
        self.assertTrue(any("Stale baseline" in value for value in errors))
        self.assertFalse(any("FR-M01-99" in value for value in errors))

    def test_duplicate_ids_anchors_and_unknown_actor(self):
        text = document().replace("UC-M01-002", "UC-M01-001")
        text += '<a id="uc-m01-001"></a>\n'
        text = text.replace("| ACT-001 | - | M01 |", "| ACT-099 | - | M01 |")
        errors, _, _ = self.check(text)
        for phrase in ("duplicate UC ID", "Duplicate anchor", "unknown actor"):
            self.assertTrue(any(phrase in value for value in errors), errors)

    def test_actor_boundary_and_hierarchy(self):
        text = document().replace("| human | - | Outside subject |",
                                  "| internal | ACT-001 | - |")
        errors, _, _ = self.check(text)
        self.assertTrue(any("kind must be external" in value for value in errors))
        self.assertTrue(any("boundary rationale" in value for value in errors))
        self.assertTrue(any("Actor generalization cycle" in value for value in errors))

    def test_contract_and_catalog_must_agree(self):
        text = document().replace("| trigger | Fixture value |\n", "")
        text = text.replace("| primary | ACT-001 |", "| primary | ACT-099 |")
        errors, _, _ = self.check(text)
        self.assertTrue(any("missing contract field trigger" in value for value in errors))
        self.assertTrue(any("catalog/spec mismatch" in value for value in errors))

    def relation(self, kind, start="UC-M01-002", end="UC-M01-001", at="EP1",
                 condition="guard", return_to="#uc-m01-001-main-2"):
        text = document()
        point = "| EP1 | UC-M01-001 | #uc-m01-001-main-1 | Decision |\n\n"
        text = text.replace("\n\n<!-- uc:relations -->", "\n" + point + "<!-- uc:relations -->")
        row = f"| {kind} | {start} | {end} | {at} | {condition} | {return_to} | Reason | FR-M01-01.01 |\n\n"
        return text.replace("\n\n<!-- uc:trace -->", "\n" + row + "<!-- uc:trace -->")

    def test_extension_point_guard_and_return(self):
        self.assertEqual(self.check(self.relation("extend"))[0], [])
        errors, _, _ = self.check(self.relation("extend", at="UNKNOWN", condition="-",
                                               return_to="#uc-m01-002-main-2"))
        for phrase in ("extension point", "missing condition", "does not belong"):
            self.assertTrue(any(phrase in value for value in errors), errors)
        self.assertEqual(self.check(self.relation("extend", return_to="END: stopped"))[0], [])
        self.assertTrue(self.check(self.relation("extend", return_to="END:"))[0])

    def test_include_and_generalization_edges(self):
        for kind, at in [("include", "#uc-m01-002-main-1"),
                         ("generalization", "#uc-m01-001-contract")]:
            target = "#uc-m01-002-main-2" if kind == "include" else "-"
            self.assertEqual(self.check(self.relation(kind, at=at, return_to=target))[0], [])
        text = self.relation("generalization", at="#uc-m01-001-contract")
        text = text.replace("\n\n<!-- uc:trace -->",
                            "\n| generalization | UC-M01-001 | UC-M01-002 | #uc-m01-002-contract | - | - | Common | FR-M01-01 |\n\n<!-- uc:trace -->")
        self.assertTrue(any("UC generalization cycle" in value for value in self.check(text)[0]))
        text = self.relation("include", at="#uc-m01-002-main-1", return_to="#uc-m01-002-main-2")
        text = text.replace("\n\n<!-- uc:trace -->",
                            "\n| include | UC-M01-001 | UC-M01-002 | #uc-m01-001-main-1 | - | END: done | Common | FR-M01-01 |\n\n<!-- uc:trace -->")
        self.assertTrue(any("Include cycle" in value for value in self.check(text)[1]))

    def test_bad_relation_and_missing_target(self):
        text = self.relation("unknown", start="UC-M01-099", at="#missing")
        errors, _, _ = self.check(text)
        self.assertTrue(any("invalid endpoints" in value for value in errors))
        self.assertTrue(any("unknown relation type" in value for value in errors))
        errors, _, _ = self.check(document().replace("#uc-m01-001-main-1 | Đủ", "#missing | Đủ"))
        self.assertTrue(any("missing local anchor" in value for value in errors))

    def test_coverage_and_approval_claims(self):
        text = document().replace("| Đủ | Synthetic mapping |", "| Chưa | - |")
        text = text.replace("| status | Chờ duyệt |", "| status | Đã duyệt |")
        text = text.replace("| completed_steps | 1, 2, 3, 4, 5, 6, 7 |",
                            "| completed_steps | 1, 2 |")
        errors, _, _ = self.check(text)
        for phrase in ("incomplete coverage", "Approved step", "approval evidence",
                       "all steps completed"):
            self.assertTrue(any(phrase in value for value in errors), errors)

    def test_render_and_semantic_review_not_assumed(self):
        text = document().replace("| semantic_review | pass |", "| semantic_review | pending |")
        text = text.replace("| diagram_check | pass |", "| diagram_check | pending |")
        text = text.replace("| plantuml | RENDER-STUB | pass |", "| illustrative | - | pending |")
        errors, _, _ = self.check(text)
        for phrase in ("semantic review", "render evidence", "incomplete render", "not formal UML"):
            self.assertTrue(any(phrase in value for value in errors), errors)

    def test_table_and_key_failures_are_reported(self):
        with self.assertRaises(ValueError):
            table("no markers", "trace")
        with self.assertRaises(ValueError):
            table("<!-- uc:trace -->\n| a | b |\n|---|---|\n| value |\n", "trace")
        with self.assertRaises(ValueError):
            fields([{"key": "x", "value": "a"}, {"key": "x", "value": "b"}])
        self.assertTrue(cycle([("a", "b"), ("b", "a")]))
        self.assertFalse(cycle([("a", "b")]))

    def test_missing_and_unapproved_fr(self):
        self.fr.write_text(self.fr.read_text(encoding="utf-8").replace("Đã chốt", "Nháp"),
                           encoding="utf-8")
        self.assertTrue(any("not approved" in value for value in self.check()[0]))
        self.fr.unlink()
        self.assertTrue(any("Missing/empty" in value for value in self.check()[0]))


if __name__ == "__main__":
    unittest.main()
