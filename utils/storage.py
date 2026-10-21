
import json
from pathlib import Path

DATA_FILE = Path("data/data.json")


def save_data(members=None):
    from models.member import Member
    from models.plan import MembershipPlan
    from models.membership import Membership

    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

    data = {
        "members": {
            item.member_id: item.to_dict()
            for item in Member.all()
        },
        "plans": {
            item.plan_id: item.to_dict()
            for item in MembershipPlan.all()
        },
        "memberships": {
            item.membership_id: item.to_dict()
            for item in Membership.all()
        },
        "attendance": {}
    }

    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    print("Data saved successfully.")



def load_data():
    from models.member import Member
    from models.plan import MembershipPlan
    from models.membership import Membership

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("No saved data found. Starting with empty records.")
        return
    except json.JSONDecodeError:
        print("Saved data is damaged. Starting with empty records.")
        return

    for item in data.get("members", {}).values():
        Member.from_dict(item)

    for item in data.get("plans", {}).values():
        MembershipPlan.from_dict(item)

    for item in data.get("memberships", {}).values():
        Membership.from_dict(item)

    print("Data loaded successfully.")
