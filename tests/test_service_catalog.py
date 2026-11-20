import unittest
from service_catalog import ServiceCatalog, ServiceDefinition, default_catalog

class ServiceCatalogTests(unittest.TestCase):
    def test_default_catalog_routes_complete_exam_request(self):
        result = default_catalog().assess("exam", {"student_id": "S1", "course_code": "ML"})
        self.assertEqual(result["outcome"], "ROUTE")
        self.assertEqual(result["office"], "examinations")
    def test_custom_service_can_be_added(self):
        catalog = ServiceCatalog([ServiceDefinition("library", "library", frozenset({"student_id"}), 12)])
        self.assertEqual(catalog.assess("library", {"student_id": "S1"})["office"], "library")
    def test_duplicate_categories_rejected(self):
        service = ServiceDefinition("library", "library", frozenset(), 12)
        with self.assertRaises(ValueError): ServiceCatalog([service, service])
    def test_invalid_sla_rejected(self):
        with self.assertRaises(ValueError):
            ServiceCatalog([ServiceDefinition("library", "library", frozenset(), 0)])
    def test_whitespace_required_field_missing(self):
        result = default_catalog().assess("exam", {"student_id": "S1", "course_code": " "})
        self.assertEqual(result["outcome"], "ASK")
if __name__ == "__main__": unittest.main()
