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
            raise ValueError("ticket_id must be non-empty")
        if not isinstance(self.category, str) or not self.category.strip():
            raise ValueError("category must be non-empty")
        if not isinstance(self.fields, dict) or any(
            not isinstance(k, str) or not isinstance(v, str) for k, v in self.fields.items()
        ):
            raise ValueError("fields must map strings to strings")
        if not isinstance(self.events, list) or any(not isinstance(event, str) for event in self.events):
            raise ValueError("events must be a list of strings")
        # Keep caller-owned containers from mutating ticket state behind its
        # validation and idempotent event-recording logic.
        self.fields = dict(self.fields)
        self.events = list(self.events)

    def assess(self) -> dict:
        if self.category not in OFFICE_RULES:
            return {"outcome": Outcome.ASK.value, "missing": ["recognized category"],
                    "office": None, "sla_hours": None}
        office, required, sla = OFFICE_RULES[self.category]
        missing = sorted(key for key in required
                         if not isinstance(self.fields.get(key), str) or not self.fields[key].strip())
        event = ("missing:" + ",".join(missing)) if missing else ("routed:" + office)
        if not self.events or self.events[-1] != event:
            self.events.append(event)
        return {"outcome": Outcome.ASK.value if missing else Outcome.ROUTE.value,
                "missing": missing, "office": office, "sla_hours": sla}

if __name__ == "__main__":
    ticket = Ticket("T1", "exam", {"student_id": "S1", "course_code": "DSA"})
    print(ticket.assess())
