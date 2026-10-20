from models.member import Member


print("===================================")
print("       GymPulse Management System")
print("===================================")

#admin function
def add_member():
    print("\nADD GYM MEMBER")
    while True:
        name = input("Enter member name: ").strip()
        phone = input("Enter phone number (+254...): ").strip()
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

#admin function
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

#admin function
def remove_member():
    print("\nREMOVE GYM MEMBER")

    member_id = input("Enter member ID: ").strip().upper()

    try:
        Member.remove(member_id)
        print("Member removed successfully!")

    except ValueError as error:
        print(error)





while True:
    print("\nSELECT YOUR ROLE")
    print("1. Gym Administrator")
    print("2. Gym Member")
    print("0. Exit")

    role_choice = input("Choose your role: ")

    if role_choice == "1":
        while True:
            print("\nMAIN MENU")
            print("1. Manage Gym Members")
            print("2. Manage Membership Plans")
            print("3. Assign Memberships")
            print("4. Record Attendance")
            print("5. View Available Membership Plans")
            print("0. Log Out")

            choice = input("Choose an option: ")

            if choice == "1":
                while True:
                    print("\nGYM MEMBERS")
                    print("1. Add Member")
                    print("2. View Members")
                    print("3. Remove Member")
                    print("0. Back to Main Menu")

                    member_choice = input("Choose an option: ")

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
                    print("0. Back to main menu")

                    plan_choice = input("Choose an option: ")

                    if plan_choice == "1":
                        print("Create Membership Plan selected.")
                    elif plan_choice == "2":
                        print("View Membership Plans selected.")
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

                    membership_choice = input("Choose an option: ")

                    if membership_choice == "1":
                        print("Assign Plan to Member selected.")

                    elif membership_choice == "2":
                        print("View Member Memberships selected.")

                    elif membership_choice == "0":
                        break

                    else:
                        print("Invalid choice. Please try again.")

            elif choice == "4":
                while True:
                    print("\nRECORD ATTENDANCE")
                    print("1. Record Member Attendance")
                    print("2. View Attendance Records")
                    print("0. Back to Main Menu")

                    attendance_choice = input("Choose an option: ")

                    if attendance_choice == "1":
                        print("Record Member Attendance selected.")

                    elif attendance_choice == "2":
                        print("View Attendance Records selected.")

                    elif attendance_choice == "0":
                        break

                    else:
                        print("Invalid choice. Please try again.")

            elif choice == "5":
                print("View Available Membership Plans selected.")

            elif choice == "0":
                break

            else:
                print("Invalid choice. Please try again.")
    elif role_choice == "2":
        while True:
            print("\nGYM MEMBER MENU")
            print("1. View Available Membership Plans")
            print("2. View My Membership")
            print("3. View My Attendance")
            print("4. View My Detais")
            print("0. Log Out")

            member_menu_choice = input("Choose an option: ")

            if member_menu_choice == "1":
                print("View Available Membership Plans Selected.")
            elif member_menu_choice == "2":
                print("View My Membership selected.")
            elif member_menu_choice == "3":
                print("View My Attendance selected.")
            elif member_menu_choice == "0":
                print("Logging out...")
                break

            else:
                print("Invalid choice. Please try again.")

    elif role_choice == "0":
        print("Thank you for using GymPulse. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")






