from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class Outcome(str, Enum):
    ASK = "ASK"
    ROUTE = "ROUTE"


OFFICE_RULES = {
    "fees": ("accounts", {"student_id", "payment_reference"}, 24),
    "exam": ("examinations", {"student_id", "course_code"}, 24),
    "certificate": ("academic_office", {"student_id", "certificate_type"}, 72),
    "hostel": ("hostel_office", {"student_id"}, 48),
}


@dataclass
class Ticket:
    ticket_id: str
    category: str
    fields: dict[str, str]
    events: list[str] = field(default_factory=list)

    def __post_init__(self):
        if not isinstance(self.ticket_id, str) or not self.ticket_id.strip():
            raise ValueError("ticket_id is required")
        if not isinstance(self.category, str) or not self.category.strip():
            raise ValueError("category is required")
        if not isinstance(self.fields, dict) or any(
            not isinstance(key, str) or not key.strip() or not isinstance(value, str)
            for key, value in self.fields.items()
        ):
            raise ValueError("ticket fields must map non-empty keys to string values")

    def assess(self) -> dict:
        if self.category not in OFFICE_RULES:
            return {
                "outcome": Outcome.ASK.value,
                "missing": ["recognized category"],
                "office": None,
                "sla_hours": None,
            }

        office, required, sla = OFFICE_RULES[self.category]
        missing = sorted(key for key in required if not self.fields.get(key, "").strip())
        if missing:
            self.events.append("missing:" + ",".join(missing))
            return {
                "outcome": Outcome.ASK.value,
                "missing": missing,
                "office": office,
                "sla_hours": sla,
            }

        self.events.append("routed:" + office)
        return {
            "outcome": Outcome.ROUTE.value,
            "missing": [],
            "office": office,
            "sla_hours": sla,
        }


if __name__ == "__main__":
    t = Ticket("T1", "exam", {"student_id": "S1", "course_code": "DSA"})
    print(t.assess())
