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
        self.services = {service.category: service for service in services}

    def assess(self, category: str, fields: dict[str, str]) -> dict:
        service = self.services.get(category)
        if service is None:
            return {
                "outcome": "ASK",
                "office": None,
                "missing": ["recognized category"],
                "sla_hours": None,
            }

        missing = sorted(
            field
            for field in service.required_fields
            if not fields.get(field)
        )
        return {
            "outcome": "ASK" if missing else "ROUTE",
            "office": service.office,
            "missing": missing,
            "sla_hours": service.sla_hours,
        }


def default_catalog() -> ServiceCatalog:
    return ServiceCatalog([
        ServiceDefinition("fees", "accounts", frozenset({"student_id", "payment_reference"}), 24),
        ServiceDefinition("exam", "examinations", frozenset({"student_id", "course_code"}), 24),
        ServiceDefinition("certificate", "academic_office", frozenset({"student_id", "certificate_type"}), 72),
        ServiceDefinition("hostel", "hostel_office", frozenset({"student_id"}), 48),
    ])
