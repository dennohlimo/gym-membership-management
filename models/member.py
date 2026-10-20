
import re
from models.person import Person
from utils.storage import save_data


class Member(Person):
    _members = {}
    _next_id = 1000

    def __init__(self, member_id, name, phone):
        super().__init__(name)
        self.member_id = member_id
        self.phone = phone

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, new_phone):
        """Validate a Kenyan phone number in 0XXXXXXXXX format."""
        if not isinstance(new_phone, str):
            raise ValueError("Phone number must be text.")

        new_phone = new_phone.strip().replace(" ", "")

        if not re.fullmatch(r"0[17]\d{8}", new_phone):
            raise ValueError(
                "Invalid phone number. Use 0 followed by 9 digits."
            )

        self._phone = new_phone

    @classmethod
    def create(cls, name, phone):
        """Create and store a member with an automatically generated ID."""
        new_id = cls._next_id + 1
        member = cls(f"MEM{new_id}", name, phone)

        cls._next_id = new_id
        cls._members[member.member_id] = member
        save_data(cls._members)

        return member

    @classmethod
    def all(cls):
        """Return all registered members."""
        return list(cls._members.values())

    @classmethod
    def find(cls, member_id):
        """Find a member by ID or raise ValueError."""
        member = cls._members.get(member_id)

        if member is None:
            raise ValueError("Member not found.")

        return member

    @classmethod
    def remove(cls, member_id):
        """Remove a member and save the updated records."""
        if member_id not in cls._members:
            raise ValueError("Member not found.")

        del cls._members[member_id]
        save_data(cls._members)

    def to_dict(self):
        """Convert a member to a dictionary for JSON storage."""
        return {
            "member_id": self.member_id,
            "name": self.name,
            "phone": self.phone,
        }

    @classmethod
    def from_dict(cls, data):
        """Rebuild a member from a dictionary."""
        member = cls(
            data["member_id"],
            data["name"],
            data["phone"],
        )

        cls._members[member.member_id] = member

        number = int(member.member_id.replace("MEM", ""))
        if number > cls._next_id:
            cls._next_id = number

        return member
