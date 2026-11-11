"""Behavioral checks using the worked example and malformed control-flow variants."""

from contextlib import redirect_stdout, redirect_stderr
import io
from pathlib import Path
import unittest

from check_scenarios import cells, check_graph, main, tables, validate

ROOT = Path(__file__).resolve().parents[1]
EXAMPLE = ROOT / "references/worked-example.md"
SOURCE = ROOT / "references/example-inputs.md"


class ScenarioValidationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.example = EXAMPLE.read_text(encoding="utf-8")
        cls.source = SOURCE.read_text(encoding="utf-8")

    def errors(self, text, source=None, final=False):
        return validate(text, [self.source], source or self.source, final)[0]

    def rejects(self, text, fragment, **kwargs):
        errors = self.errors(text, **kwargs)
        self.assertTrue(any(fragment in error for error in errors), errors)

    def test_complete_recovery_cancel_and_rejection_paths(self):
        errors, counts = validate(self.example, [self.source], self.source)
        self.assertEqual([], errors)
        self.assertEqual({"use_cases": 3, "flows": 2, "scenarios": 2, "exceptions": 4}, counts)

    def test_one_sided_paths_rejected_and_distinct_actors_still_allowed(self):
        # Both sides are required; real exchanges between distinct actors remain possible.
        sid = "SC-M90-001"
        block = "\n".join(f"#### {n}. Section\nContent.\n" for n in range(1, 7))
        for subjects, valid in ((["SYSTEM"], False), (["ACT-901"], False),
                                (["ACT-901", "ACT-902"], False),
                                (["ACT-901", "ACT-902", "SYSTEM"], True)):
            rows = []
            for i, subject in enumerate(subjects, 1):
                rows.append({"step": f"M{i}", "subject": subject, "action": "Action",
                             "data": "Business data", "sources": "FR-M90-01.01",
                             "next": f"M{i+1}" if i < len(subjects) else "END:SUCCESS"})
            data = {f"sc:main {sid}": rows, f"sc:exceptions {sid}": [],
                    f"sc:post {sid}": [{"result": "SUCCESS", "condition": "Completed"}]}
            errors = []
            check_graph(sid, block, data, {"ACT-901", "ACT-902"}, errors)
            if valid:
                self.assertEqual([], errors)
            else:
                self.assertTrue(any("both actor and SYSTEM" in error for error in errors), errors)

    def test_primary_actor_must_initiate_journey(self):
        self.rejects(self.example.replace("| UC-M90-001 | ACT-901 | Biên tập viên yêu cầu", "| UC-M90-001 | SYSTEM | Biên tập viên yêu cầu"), "primary actor")
        # Preserve alternating steps but swap actor/system: the goal owner no longer starts.
        text = self.example.replace("| M1 | ACT-901 |", "| M1 | SYSTEM |")
        self.rejects(text, "start with the primary actor")

    def test_refusal_or_handoff_is_not_a_main_business_goal(self):
        for result in ("REJECTED", "CANCELLED", "HANDED_OFF"):
            self.rejects(self.example.replace("END:SUCCESS", f"END:{result}"), "SYSTEM returning END:SUCCESS")

    def test_complete_goal_metadata_required(self):
        for field in ("primary", "completion", "rationale"):
            text = self.example.replace(f"| {field} |", f"| removed_{field} |")
            self.rejects(text, "primary actor" if field == "primary" else f"field {field}")

    def test_embedded_uc_needs_real_step_in_each_containing_scenario(self):
        self.rejects(self.example.replace("SC-M90-001/M4", "SC-M90-001/M99"), "unknown embedded coverage step")
        self.rejects(self.example.replace("SC-M90-002/M2", "missing"), "SC/step locations")
        self.rejects(self.example.replace("| embedded |", "| scenario |"), "requires an owned actor goal")

    def test_flow_cannot_hide_or_invent_participating_uc(self):
        self.rejects(self.example.replace("| UC-M90-001, UC-M90-002 |", "| UC-M90-001 |"), "participating flows")
        self.rejects(self.example.replace("| UC-M90-001, UC-M90-002 |", "| UC-M90-999 |"), "covered_ucs")

    def test_background_is_traced_without_scenario(self):
        # Synthetic source variant exercises disposition without adding a product rule.
        source = self.source
        anchor = "| UC-M90-010 | Quản lý nhãn"
        source = source.replace(anchor, "| UC-M90-099 | Tác vụ nền minh họa | sub | Subfunction | - | BR-M90-01 |\n" + anchor)
        line = "| UC-M90-099 | background | - | Ghi chú nền: trigger và hiệu ứng giả lập | Không có mục tiêu actor trong scope | BR-M90-01 |\n"
        text = self.example.replace("| scope | UC-M90-001, UC-M90-002 |", "| scope | ALL |")
        text = text.replace("| UC-M90-010 | aggregate |", line + "| UC-M90-010 | aggregate |")
        self.assertEqual([], self.errors(text, source=source))
        self.rejects(text.replace("| background | - |", "| background | SC-M90-001 |"), "background needs", source=source)

    def test_same_subject_in_main_is_rejected(self):
        self.rejects(self.example.replace("| M2 | SYSTEM |", "| M2 | ACT-901 |", 1), "same subject")

    def test_same_subject_at_reentry_is_rejected(self):
        self.rejects(self.example.replace("| E1.2 | ACT-901 |", "| E1.2 | SYSTEM |", 1), "E1.2 -> M4")

    def test_controller_cannot_be_subject(self):
        self.rejects(self.example.replace("| M2 | SYSTEM |", "| M2 | Controller |", 1), "invalid subject")

    def test_unknown_reentry_is_rejected(self):
        self.rejects(self.example.replace("| M4 | FR-M90-01.03 |", "| M99 | FR-M90-01.03 |"), "unknown next")

    def test_closed_retry_cycle_is_rejected(self):
        self.rejects(self.example.replace("| M4 | FR-M90-01.03 |", "| E1.1 | FR-M90-01.03 |"), "no path to an outcome")

    def test_exception_must_replace_existing_step(self):
        self.rejects(self.example.replace("| E2 | user-choice | M3 |", "| E2 | user-choice | M99 |"), "invalid replacement")

    def test_replacement_subject_must_match(self):
        self.rejects(self.example.replace("| E2.1 | ACT-901 |", "| E2.1 | SYSTEM |"), "first subject")

    def test_replacement_journey_accepts_another_registered_actor(self):
        sid = "SC-M90-001"
        block = "\n".join(f"#### {n}. Section\nContent.\n" for n in range(1, 7))

        def step(identifier, subject, target):
            return {"step": identifier, "subject": subject, "action": "Request or response",
                    "data": "Synthetic business data", "sources": "FR-M90-01.01", "next": target}

        data = {
            f"sc:main {sid}": [step("M1", "ACT-901", "M2"), step("M2", "SYSTEM", "END:SUCCESS")],
            f"sc:post {sid}": [{"result": "SUCCESS", "condition": "Actor receives completed result"},
                                {"result": "REJECTED", "condition": "Actor receives refusal"}],
            f"sc:exceptions {sid}": [{"id": "E1", "kind": "system", "at": "M1",
                                      "condition": "ACT-902 has another role", "entry": "E1.1",
                                      "sources": "FR-M90-01.01"}],
            f"sc:branch {sid} E1": [step("E1.1", "ACT-902", "E1.2"),
                                      step("E1.2", "SYSTEM", "END:REJECTED")],
        }
        errors = []
        check_graph(sid, block, data, {"ACT-901", "ACT-902"}, errors)
        self.assertEqual([], errors)
        data[f"sc:branch {sid} E1"][0]["subject"] = "SYSTEM"
        errors = []
        check_graph(sid, block, data, {"ACT-901", "ACT-902"}, errors)
        self.assertTrue(any("must start with a known actor" in error for error in errors), errors)
        data[f"sc:branch {sid} E1"][0]["subject"] = "ACT-999"
        errors = []
        check_graph(sid, block, data, {"ACT-901", "ACT-902"}, errors)
        self.assertTrue(any("invalid subject" in error for error in errors), errors)
        data[f"sc:branch {sid} E1"][0]["subject"] = "ACT-902"
        del data[f"sc:exceptions {sid}"][0]["sources"]
        errors = []
        check_graph(sid, block, data, {"ACT-901", "ACT-902"}, errors)
        self.assertTrue(any("missing exception content" in error for error in errors), errors)

    def test_nonstandard_alternative_marker_is_rejected(self):
        for name in ("role-path", "variant", "path", "unregistered"):
            self.rejects(self.example + f"\n<!-- sc:{name} SC-M90-001 V1 -->\n", "Unsupported scenario marker")

    def test_terminal_requires_a_system_response(self):
        self.rejects(self.example.replace("| E2.2 | SYSTEM |", "| E2.2 | ACT-902 |"), "outcome must be returned by SYSTEM")

    def test_orphan_branch_is_not_ignored(self):
        line = next(line for line in self.example.splitlines() if line.startswith("| E2 | user-choice |"))
        self.rejects(self.example.replace(line, ""), "orphan branch")

    def test_result_needs_postcondition(self):
        self.rejects(self.example.replace("END:CANCELLED", "END:HANDED_OFF"), "terminal without postcondition")

    def test_business_flow_needs_distinct_scenario(self):
        self.rejects(self.example.replace("| SC-M90-002 | FR-M90-02.01 |", "| SC-M90-001 | FR-M90-02.01 |"), "own six-part scenario")

    def test_scope_cannot_silently_omit_uc(self):
        source = self.source.replace("| UC-M90-010 | Quản lý", "| UC-M90-099 | Xem nhãn | sub | User goal | ACT-901 | FR-M90-02.01 |\n| UC-M90-010 | Quản lý")
        self.rejects(self.example.replace("| scope | UC-M90-001, UC-M90-002 |", "| scope | ALL |"), "inventory mismatch", source=source)

    def test_unknown_actor_and_requirement(self):
        self.rejects(self.example.replace("ACT-901", "ACT-999"), "Actors absent")
        self.rejects(self.example.replace("FR-M90-01.03", "FR-M90-99.99"), "unknown FR/BR")

    def test_missing_section_and_data(self):
        self.rejects(self.example.replace("#### 3. Tiền điều kiện", "#### 7. Tiền điều kiện", 1), "six ordered sections")
        self.rejects(self.example.replace("D1: tên = Đại số", "-"), "missing step content")

    def test_bad_disposition_and_approval(self):
        self.rejects(self.example.replace("| aggregate |", "| ignored |"), "invalid treatment")
        self.rejects(self.example.replace("| status | Đang soạn |", "| status | Đã duyệt |"), "approval evidence")
        self.rejects(self.example.replace("| aggregate |", "| gap |"), "unresolved gap", final=True)

    def test_missing_end_marker_and_placeholder(self):
        self.rejects(self.example.replace("<!-- sc:end SC-M90-001 -->", ""), "missing end marker")
        self.rejects(self.example + "\n{{UNFILLED}}", "Unfilled template")

    def test_duplicate_and_malformed_tables(self):
        self.assertEqual(["a|b", "c"], cells(r"| a\|b | c |"))
        errors = []
        text = "<!-- sc:actors -->\n| id | id |\n|---|---|\n| A |\n\n<!-- sc:actors -->\n| id |\n|---|\n"
        tables(text, errors)
        self.assertTrue(any("Duplicate column" in e for e in errors))
        self.assertTrue(any("Column count" in e for e in errors))
        self.assertTrue(any("Duplicate table" in e for e in errors))

    def test_cli_reports_pass_and_missing_file(self):
        with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
            self.assertEqual(0, main([str(EXAMPLE), "--fr", str(SOURCE), "--us", str(SOURCE)]))
            self.assertEqual(2, main([str(ROOT / "missing.md"), "--fr", str(SOURCE), "--us", str(SOURCE)]))


if __name__ == "__main__":
    unittest.main()
