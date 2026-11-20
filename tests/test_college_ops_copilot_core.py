import unittest
from college_ops_copilot_core import Ticket

class CollegeOpsTests(unittest.TestCase):
    def test_complete_ticket_routes(self):
        result = Ticket("1", "exam", {"student_id": "S", "course_code": "ML"}).assess()
        self.assertEqual(result["office"], "examinations")
        self.assertEqual(result["outcome"], "ROUTE")
    def test_missing_field_asks(self):
        result = Ticket("1", "fees", {"student_id": "S"}).assess()
        self.assertEqual(result["outcome"], "ASK")
        self.assertIn("payment_reference", result["missing"])
    def test_unknown_category_asks(self):
        result = Ticket("1", "other", {}).assess()
        self.assertEqual(result["outcome"], "ASK")
        self.assertIsNone(result["office"])
    def test_whitespace_required_field_is_missing(self):
        result = Ticket("1", "exam", {"student_id": "S", "course_code": "  "}).assess()
        self.assertIn("course_code", result["missing"])
    def test_assessment_event_is_idempotent(self):
        ticket = Ticket("1", "exam", {"student_id": "S", "course_code": "ML"})
        ticket.assess()
        ticket.assess()
        self.assertEqual(ticket.events, ["routed:examinations"])
    def test_invalid_event_container_rejected(self):
        with self.assertRaises(ValueError):
            Ticket("1", "exam", {}, events="not-a-list")
        with self.assertRaises(ValueError):
            Ticket("1", "exam", {}, events=["ok", 7])

    def test_caller_container_mutation_does_not_mutate_ticket(self):
        fields = {"student_id": "S", "course_code": "ML"}
        events = ["created"]
        ticket = Ticket("1", "exam", fields, events)
        fields["course_code"] = " "
        events.append("tampered")
        self.assertEqual(ticket.fields["course_code"], "ML")
        self.assertEqual(ticket.events, ["created"])

    def test_invalid_ticket_identity_rejected(self):
        with self.assertRaises(ValueError): Ticket("", "exam", {})
if __name__ == "__main__": unittest.main()
