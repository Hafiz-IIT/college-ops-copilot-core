import unittest

from service_catalog import ServiceCatalog, ServiceDefinition, default_catalog


class ServiceCatalogTests(unittest.TestCase):
    def test_default_catalog_routes_complete_exam_request(self):
        result = default_catalog().assess(
            "exam",
            {"student_id": "S1", "course_code": "ML"},
        )
        self.assertEqual(result["outcome"], "ROUTE")
        self.assertEqual(result["office"], "examinations")

    def test_custom_service_can_be_added_without_code_change(self):
        catalog = ServiceCatalog([
            ServiceDefinition("library", "library", frozenset({"student_id"}), 12)
        ])
        result = catalog.assess("library", {"student_id": "S1"})
        self.assertEqual(result["office"], "library")


if __name__ == "__main__":
    unittest.main()
