from __future__ import annotations
from dataclasses import dataclass

@dataclass(frozen=True)
class ServiceDefinition:
    category: str
    office: str
    required_fields: frozenset[str]
    sla_hours: int

class ServiceCatalog:
    def __init__(self, services: list[ServiceDefinition]):
        if not isinstance(services, list):
            raise ValueError("services must be a list")
        self.services = {}
        for service in services:
            if not isinstance(service, ServiceDefinition):
                raise ValueError("each service must be a ServiceDefinition")
            if not isinstance(service.category, str) or not service.category.strip():
                raise ValueError("service category must be non-empty")
            if not isinstance(service.office, str) or not service.office.strip():
                raise ValueError("service office must be non-empty")
            if not isinstance(service.required_fields, frozenset) or any(
                not isinstance(field, str) or not field.strip() for field in service.required_fields
            ):
                raise ValueError("required_fields must be a frozenset of non-empty strings")
            if isinstance(service.sla_hours, bool) or not isinstance(service.sla_hours, int) or service.sla_hours < 1:
                raise ValueError("sla_hours must be a positive integer")
            if service.category in self.services:
                raise ValueError(f"duplicate service category: {service.category}")
            self.services[service.category] = service

    def assess(self, category: str, fields: dict[str, str]) -> dict:
        if not isinstance(category, str) or not category.strip():
            return {"outcome": "ASK", "office": None, "missing": ["recognized category"], "sla_hours": None}
        if not isinstance(fields, dict):
            raise ValueError("fields must be a dictionary")
        service = self.services.get(category)
        if service is None:
            return {"outcome": "ASK", "office": None, "missing": ["recognized category"], "sla_hours": None}
        missing = sorted(field for field in service.required_fields
                         if not isinstance(fields.get(field), str) or not fields[field].strip())
        return {"outcome": "ASK" if missing else "ROUTE", "office": service.office,
                "missing": missing, "sla_hours": service.sla_hours}

def default_catalog() -> ServiceCatalog:
    return ServiceCatalog([
        ServiceDefinition("fees", "accounts", frozenset({"student_id", "payment_reference"}), 24),
        ServiceDefinition("exam", "examinations", frozenset({"student_id", "course_code"}), 24),
        ServiceDefinition("certificate", "academic_office", frozenset({"student_id", "certificate_type"}), 72),
        ServiceDefinition("hostel", "hostel_office", frozenset({"student_id"}), 48),
    ])
