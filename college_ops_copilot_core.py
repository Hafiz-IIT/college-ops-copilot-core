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

    def assess(self) -> dict:
        if self.category not in OFFICE_RULES:
            return {
                "outcome": Outcome.ASK.value,
                "missing": ["recognized category"],
                "office": None,
                "sla_hours": None,
            }

        office, required, sla = OFFICE_RULES[self.category]
        missing = sorted(key for key in required if not self.fields.get(key))
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
