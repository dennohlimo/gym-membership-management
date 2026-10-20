
import json


def save_data(members):
    data = {
        "members": {
            member_id: member.to_dict()
            for member_id, member in members.items()
        },
        "plans": {},
        "memberships": {},
        "attendance": {}
    }

    with open("data/data.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    print("Data saved successfully.")

def load_data():
    from models.member import Member
    try:
        with open("data/data.json", "r", encoding="utf-8") as file:
            data = json.load(file)

    except FileNotFoundError:
        print("No saved data found. Starting with empty records.")
        return

    except json.JSONDecodeError:
        print("Saved data is damaged. Starting with empty records.")
        return

    for member_data in data.get("members", {}).values():
        Member.from_dict(member_data)

    print("Data loaded successfully.")
