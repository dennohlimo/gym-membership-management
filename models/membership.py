
from datetime import date, timedelta


class Membership:
    """A membership plan assigned to a gym member."""

    _memberships = {}
    _next_id = 0

    def __init__(
        self,
        membership_id,
        member_id,
        plan_id,
        start_date,
        expiry_date
    ):
        self.membership_id = membership_id
        self.member_id = member_id
        self.plan_id = plan_id
        self.start_date = date.fromisoformat(start_date)
        self.expiry_date = date.fromisoformat(expiry_date)

    @classmethod
    def assign(cls, member, plan, start_date=None):
        for existing in cls.for_member(member.member_id):
            if not existing.is_expired:
                raise ValueError(
                    f"Member already has an active membership with this plan: {existing.membership_id}"
                )
        
        """Assign a plan to a member and calculate its expiry date."""
        start = (
            date.fromisoformat(start_date)
            if start_date
            else date.today()
        )

        expiry = start + timedelta(days=plan.duration_days)
        new_id = cls._next_id + 1

        membership = cls(
            f"MS{new_id}",
            member.member_id,
            plan.plan_id,
            start.isoformat(),
            expiry.isoformat()
        )

        cls._next_id = new_id
        cls._memberships[membership.membership_id] = membership

        from utils.storage import save_data
        save_data()

        return membership

    @classmethod
    def all(cls):
        return list(cls._memberships.values())

    @classmethod
    def for_member(cls, member_id):
        return [
            membership
            for membership in cls._memberships.values()
            if membership.member_id == member_id
        ]

    @property
    def is_expired(self):
        return date.today() >= self.expiry_date

    def to_dict(self):
        return {
            "membership_id": self.membership_id,
            "member_id": self.member_id,
            "plan_id": self.plan_id,
            "start_date": self.start_date.isoformat(),
            "expiry_date": self.expiry_date.isoformat()
        }

    @classmethod
    def from_dict(cls, data):
        membership = cls(
            data["membership_id"],
            data["member_id"],
            data["plan_id"],
            data["start_date"],
            data["expiry_date"]
        )

        cls._memberships[membership.membership_id] = membership
        number = int(membership.membership_id.replace("MS", ""))
        cls._next_id = max(cls._next_id, number)

        return membership
