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
        if not isinstance(new_phone, str):
            raise ValueError("Phone number must be text.")
        if not re.fullmatch(r"0[17]\d{8}", new_phone):
            raise ValueError("Invalid phone number. Use +254 followed by 9 digits.")
        self._phone = new_phone

    @classmethod
    def create(cls, name,phone):
        member_id = f"MEM{cls._next_id+1}"
        member = cls(member_id, name, phone)
        cls._next_id +=1
        cls._members[member_id] = member

        save_data(cls._members)

        return member
    @classmethod
    def all(cls):
        return list(cls._members.values())

    @classmethod
    def remove(cls, member_id):
        if member_id in cls._members:
            del cls._members[member_id]
            save_data(cls._members)
        else:
            raise ValueError("Member not found.")
    
    def to_dict(self):
        return{
            "member_id": self.member_id,
            "name": self.name,
            "phone": self.phone
        }
    @classmethod
    def from_dict(cls, data):
        member = cls(
            data["member_id"],
            data["name"],
            data["phone"]
        )

        cls._members[member.member_id] = member

        number = int(member.member_id.replace("MEM", ""))

        if number > cls._next_id:
            cls._next_id = number

        return member

    