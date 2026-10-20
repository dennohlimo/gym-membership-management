import unittest
from models.plan import MembershipPlan

class TestMembershipPlan(unittest.TestCase):

    def setUp(self):
        MembershipPlan.clear()

    def test_create_plan(self):
        plan = MembershipPlan.create("Monthly", 1500, 30)

        self.assertEqual(plan.name, "Monthly")
        self.assertEqual(plan.price, 1500)
        self.assertEqual(plan.duration_days, 30)

    def test_invalid_price(self):
        with self.assertRaises(ValueError):
            MembershipPlan.create("Monthly", -100, 30)

    def test_invalid_duration(self):
        with self.assertRaises(ValueError):
            MembershipPlan.create("Monthly", 1500, 0)

    def test_find_plan(self):
        plan = MembershipPlan.create("Weekly", 500, 7)

        found = MembershipPlan.find(plan.plan_id)

        self.assertEqual(found.name, "Weekly")

    def test_remove_plan(self):
        plan = MembershipPlan.create("Weekly", 500, 7)

        MembershipPlan.remove(plan.plan_id)

        with self.assertRaises(ValueError):
            MembershipPlan.find(plan.plan_id)


if __name__ == "__main__":
    unittest.main()
