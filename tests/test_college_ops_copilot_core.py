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

    def test_whitespace_only_required_field_asks(self):
        result = Ticket("1", "exam", {"student_id": "S", "course_code": "   "}).assess()
        self.assertEqual(result["outcome"], "ASK")
        self.assertEqual(result["missing"], ["course_code"])

    def test_empty_ticket_id_is_rejected(self):
        with self.assertRaises(ValueError):
            Ticket(" ", "exam", {"student_id": "S", "course_code": "ML"}).assess()

    def test_unknown_category_asks_for_clarification(self):
        result = Ticket("1", "other", {}).assess()
        self.assertEqual(result["outcome"], "ASK")
        self.assertIsNone(result["office"])


if __name__ == "__main__":
    unittest.main()
