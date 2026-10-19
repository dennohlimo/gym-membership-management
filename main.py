
print("===================================")
print("       GymPulse Management System")
print("===================================")

while True:
    print("\nMAIN MENU")
    print("1. Manage Gym Members")
    print("2. Manage Membership Plans")
    print("3. Assign Memberships")
    print("4. Record Attendance")
    print("5. View Available Membership Plans")
    print("0. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        while True:
            print("\nGYM MEMBERS")
            print("1. Add Member")
            print("2. View Members")
            print("0. Back to Main Menu")

            member_choice = input("Choose an option: ")

            if member_choice == "1":
                print("Add Member selected.")

            elif member_choice == "2":
                print("View Members selected.")
            elif member_choice == "0":
                break

            else:
                print("Invalid choice. Please try again.")


    elif choice == "2":
        while True:
            print("\nMEMBERSHIP PLANS")
            print("1. Create Membership Plan")
            print("2. View Membership Plans")
            print("0 Back to main menu")

            plan_choice = input("Choose an option: ")

            if plan_choice == "1":
                print("Create Membership Plan selected.")
            elif plan_choice == "2":
                print("View Membership Plans selected.")
            elif plan_choice == "0":
                break

            else:
                print("invalid choice. Please try again.")
        

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
        print("Thank you for using GymPulse. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
