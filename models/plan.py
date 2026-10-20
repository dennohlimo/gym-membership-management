class MembershipPlan:
    """A membership plan the gym sells (e.g. Monthly, 30 days, KSh 3000)."""

    _plans = {}
    _next_id = 0

    def __init__(self, plan_id, name, price, duration_days, description=""):
        self._plan_id = plan_id
        self.name = name
        self.price = price
        self.duration_days = duration_days
        self.description = description

    @property
    def plan_id(self):
        """Read-only ID, e.g. PLN1."""
        return self._plan_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str) or not new_name.strip():
            raise ValueError("Plan name must be a non-empty string.")
        self._name = new_name.strip()

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        """Price must be a number greater than 0."""
        try:
            value = float(new_price)
        except (TypeError, ValueError):
            raise ValueError("Price must be a number.")
        if value <= 0:
            raise ValueError("Price must be greater than 0.")
        self._price = value

    @property
    def duration_days(self):
        return self._duration_days

    @duration_days.setter
    def duration_days(self, new_duration):
        """Duration must be a whole number of days greater than 0."""
        try:
            value = int(new_duration)
        except (TypeError, ValueError):
            raise ValueError("Duration must be a whole number of days.")
        if value <= 0:
            raise ValueError("Duration must be at least 1 day.")
        self._duration_days = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, new_description):
        if not isinstance(new_description, str):
            raise ValueError("Description must be text.")
        self._description = new_description.strip()

    @classmethod
    def create(cls, name, price, duration_days, description=""):
        """Create a new plan with an auto-generated ID and store it."""
        new_id = cls._next_id + 1
        plan = cls(f"PLN{new_id}", name, price, duration_days, description)
        cls._next_id = new_id  # only consumed if validation passed
        cls._plans[plan.plan_id] = plan
        return plan

    @classmethod
    def all(cls):
        """Return a list of all plans."""
        return list(cls._plans.values())

    @classmethod
    def find(cls, plan_id):
        """Return one plan by ID, or raise ValueError if not found."""
        plan = cls._plans.get(plan_id)
        if plan is None:
            raise ValueError("Plan not found.")
        return plan

    @classmethod
    def remove(cls, plan_id):
        """Remove a plan by ID, or raise ValueError if not found."""
        if plan_id in cls._plans:
            del cls._plans[plan_id]
        else:
            raise ValueError("Plan not found.")

    @classmethod
    def clear(cls):
        """Remove all plans from memory and reset the ID counter."""
        cls._plans = {}
        cls._next_id = 0

    def to_dict(self):
        """Return the plan as a dictionary (for JSON saving)."""
        return {
            "plan_id": self.plan_id,
            "name": self.name,
            "price": self.price,
            "duration_days": self.duration_days,
            "description": self.description,
        }

    @classmethod
    def from_dict(cls, data):
        """Rebuild a plan from a dictionary (for JSON loading)."""
        plan = cls(
            data["plan_id"],
            data["name"],
            data["price"],
            data["duration_days"],
            data.get("description", ""),
        )
        cls._plans[plan.plan_id] = plan
        cls._next_id = max(cls._next_id, int(plan.plan_id[3:]))
        return plan

    def __str__(self):
        text = (f"{self.plan_id} | {self.name} | KSh {self.price:,.2f} | "
                f"{self.duration_days} days")
        if self.description:
            text += f"\n    {self.description}"
        return text

    def __repr__(self):
        return (f"MembershipPlan({self.plan_id!r}, {self.name!r}, "
                f"{self.price}, {self.duration_days})")