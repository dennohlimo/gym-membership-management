import attendance

from datetime import date

from models.member import Member
from models.plan import MembershipPlan
from models.membership import Membership
from utils.storage import load_data


def add_member():
    print("\nADD GYM MEMBER")

    while True:
        name = input("Enter member name: ").strip()
        phone = input("Enter phone number (0...): ").strip()

        try:
            member = Member.create(name, phone)
            print("\nMember added successfully!")
            print("Member ID:", member.member_id)
            print("Name:", member.name)
            print("Phone Number:", member.phone)
            break
        except ValueError as error:
            print("Error:", error)
            print("Please try again.")


def view_members():
    members = Member.all()

    if not members:
        print("\nNo members have been registered yet.")
        return

    print("\nREGISTERED GYM MEMBERS")
    for member in members:
        print("-------------------------")
        print("Member ID:", member.member_id)
        print("Name:", member.name)
        print("Phone Number:", member.phone)


def remove_member():
    print("\nREMOVE GYM MEMBER")
    member_id = input("Enter member ID: ").strip().upper()

    try:
        Member.remove(member_id)
        print("Member removed successfully!")
    except ValueError as error:
        print(error)


def view_my_details():
    member_id = input("Enter your member ID: ").strip().upper()

    try:
        member = Member.find(member_id)
        print("\nMY DETAILS")
        print("Member ID:", member.member_id)
        print("Name:", member.name)
        print("Phone Number:", member.phone)
    except ValueError as error:
        print(error)


def create_plan():
    print("\nCREATE MEMBERSHIP PLAN")

    try:
        name = input("Enter plan name: ").strip()
        price = float(input("Enter plan price (KSh): "))
        duration = int(input("Enter duration in days: "))
        description = input("Enter description (optional): ").strip()

        plan = MembershipPlan.create(
            name, price, duration, description
        )

        from utils.storage import save_data
        save_data()

        print("\nPlan created successfully!")
        print(plan)

    except ValueError as error:
        print("Error:", error)


def view_plans():
    plans = MembershipPlan.all()

    if not plans:
        print("\nNo membership plans available.")
        return

    print("\nAVAILABLE MEMBERSHIP PLANS")
    for plan in plans:
        print("-------------------------")
        print(plan)


def assign_membership():
    print("\nASSIGN PLAN TO MEMBER")

    if not Member.all():
        print("Please register a member first.")
        return

    if not MembershipPlan.all():
        print("Please create a membership plan first.")
        return

    view_members()
    member_id = input("\nEnter member ID: ").strip().upper()

    try:
        member = Member.find(member_id)
    except ValueError as error:
        print(error)
        return

    view_plans()
    plan_id = input("\nEnter plan ID: ").strip().upper()

    try:
        plan = MembershipPlan.find(plan_id)
    except ValueError as error:
        print(error)
        return

    start_date = input(
        "Enter start date (YYYY-MM-DD), or press Enter for today: "
    ).strip()

    try:
        if start_date:
            date.fromisoformat(start_date)
        else:
            start_date = date.today().isoformat()

        membership = Membership.assign(member, plan, start_date)

        print("\nMembership assigned successfully!")
        print("Membership ID:", membership.membership_id)
        print("Member:", member.name)
        print("Plan:", plan.name)
        print("Start date:", membership.start_date)
        print("Expiry date:", membership.expiry_date)
        print("Status:", "Expired" if membership.is_expired else "Active")

    except ValueError as error:
        print("Could not assign membership:", error)


def view_member_memberships():
    member_id = input("Enter member ID: ").strip().upper()

    try:
        member = Member.find(member_id)
    except ValueError as error:
        print(error)
        return

    memberships = Membership.for_member(member.member_id)

    if not memberships:
        print("You have no assigned memberships.")
        return

    print(f"\nMEMBERSHIPS FOR {member.name}")

    for membership in memberships:
        try:
            plan = MembershipPlan.find(membership.plan_id)
            plan_name = plan.name
        except ValueError:
            plan_name = "Plan no longer available"

        print("-------------------------")
        print("Membership ID:", membership.membership_id)
        print("Plan ID:", membership.plan_id)
        print("Plan:", plan_name)
        print("Start date:", membership.start_date)
        print("Expiry date:", membership.expiry_date)
        print(
            "Status:",
            "Expired" if membership.is_expired else "Active"
        )


def main():
    load_data()

    while True:
        print("\n===================================")
        print("       GymPulse Management System")
        print("===================================")
        print("\nSELECT YOUR ROLE")
        print("1. Gym Administrator")
        print("2. Gym Member")
        print("0. Exit")

        role_choice = input("Choose your role: ").strip()

        if role_choice == "1":
            while True:
                print("\nMAIN MENU")
                print("1. Manage Gym Members")
                print("2. Manage Membership Plans")
                print("3. Assign Memberships")
                print("4. Record Attendance")
                print("5. View Available Membership Plans")
                print("0. Log Out")

                choice = input("Choose an option: ").strip()

                if choice == "1":
                    while True:
                        print("\nGYM MEMBERS")
                        print("1. Add Member")
                        print("2. View Members")
                        print("3. Remove Member")
                        print("0. Back to Main Menu")

                        member_choice = input("Choose an option: ").strip()

                        if member_choice == "1":
                            add_member()
                        elif member_choice == "2":
                            view_members()
                        elif member_choice == "3":
                            remove_member()
                        elif member_choice == "0":
                            break
                        else:
                            print("Invalid choice. Please try again.")

                elif choice == "2":
                    while True:
                        print("\nMEMBERSHIP PLANS")
                        print("1. Create Membership Plan")
                        print("2. View Membership Plans")
                        print("0. Back to Main Menu")

                        plan_choice = input("Choose an option: ").strip()

                        if plan_choice == "1":
                            create_plan()
                        elif plan_choice == "2":
                            view_plans()
                        elif plan_choice == "0":
                            break
                        else:
                            print("Invalid choice. Please try again.")

                elif choice == "3":
                    while True:
                        print("\nASSIGN MEMBERSHIPS")
                        print("1. Assign Plan to Member")
                        print("2. View Member Memberships")
                        print("0. Back to Main Menu")

                        membership_choice = input("Choose an option: ").strip()

                        if membership_choice == "1":
                            assign_membership()
                        elif membership_choice == "2":
                            view_member_memberships()
                        elif membership_choice == "0":
                            break
                        else:
                            print("Invalid choice. Please try again.")

                elif choice == "4":
                    # Linked to your new admin portal feature
                    attendance.admin_menu()

                elif choice == "5":
                    view_plans()

                elif choice == "0":
                    break
                else:
                    print("Invalid choice. Please try again.")

        elif role_choice == "2":
            while True:
                print("\nGYM MEMBER MENU")
                print("1. View My Profile & Live Attendance Status")
                print("2. View My Assigned Membership History")
                print("0. Log Out")

                member_menu_choice = input("Choose an option: ").strip()

                if member_menu_choice == "1":
                    # Linked to your new member login profile feature
                    attendance.member_menu()
                elif member_menu_choice == "2":
                    view_member_memberships()
                elif member_menu_choice == "0":
                    break
                else:
                    print("Invalid choice. Please try again.")

        elif role_choice == "0":
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid role selected. Please choose 1, 2, or 0.")


if __name__ == "__main__":
    main()
