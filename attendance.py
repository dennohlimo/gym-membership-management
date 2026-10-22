import sys
from models.member import Member
from models.membership import Membership

def admin_menu():
    while True:
        print("\n=====================================================================")
        print("                         ADMIN PORTAL MENU                           ")
        print("=====================================================================")
        print("1. View All Gym Members & Status")
        print("2. Back to Main Menu")
        print("=====================================================================")
        
        choice = input("Select an option: ").strip()
        
        if choice == "1":
            print("\n" + "=" * 72)
            print(f"{'ID':<9} | {'Full Name':<20} | {'Phone':<12} | {'Plan Code':<10} | {'Status':<10}")
            print("=" * 72)
            
            members = Member.all()
            if not members:
                print("No members found in the system.")
            else:
                for member in members:
                    # Pull historical memberships from membership.py
                    memberships = Membership.for_member(member.member_id)
                    
                    plan_code = "None"
                    status_str = "No Plan"
                    
                    if memberships:
                        latest = memberships[-1]
                        plan_code = latest.plan_id  # Directly using raw IDs like PLN1
                        status_str = "❌ EXPIRED" if latest.is_expired else "✅ ACTIVE"
                    
                    print(f"{member.member_id:<9} | {member.name:<20} | {member.phone:<12} | {plan_code:<10} | {status_str:<10}")
            print("=" * 72)
            input("\nPress Enter to continue...")
            
        elif choice == "2":
            break
        else:
            print("❌ Invalid option. Please choose 1 or 2.")

def member_menu():
    print("\n=====================================")
    print("         MEMBER LOGIN PORTAL         ")
    print("=====================================")
    member_id = input("Enter your Member ID (e.g., MEM1001): ").strip().upper()
    
    try:
        # Validate identity using member.py
        target_member = Member.find(member_id)
        
        print("\n=====================================")
        print("            YOUR PROFILE             ")
        print("=====================================")
        print(f"  Member ID    : {target_member.member_id}")
        print(f"  Full Name    : {target_member.name}")
        print(f"  Phone Number : {target_member.phone}")
        print("-------------------------------------")
        print("          MEMBERSHIP STATUS          ")
        print("-------------------------------------")
        
        # Pull profile plan details from membership.py
        memberships = Membership.for_member(target_member.member_id)
        if not memberships:
            print("  ⚠️ Status     : No membership packages assigned yet.")
        else:
            latest = memberships[-1]
            status_text = "❌ EXPIRED" if latest.is_expired else "✅ ACTIVE"
            
            print(f"  Current Plan : {latest.plan_id}")  # Directly outputs PLN1, PLN2 etc.
            print(f"  Start Date   : {latest.start_date}")
            print(f"  Expiry Date  : {latest.expiry_date}")
            print(f"  Status       : {status_text}")
        print("=====================================")
        
    except ValueError:
        print(f"❌ Error: Member with ID '{member_id}' not found.")
        
    input("\nPress Enter to return to the main menu...")

def main():
    while True:
        print("\n=====================================")
        print("    GYM ATTENDANCE & MEMBER PORTAL    ")
        print("=====================================")
        print("1. Admin Portal")
        print("2. Member Profile View")
        print("3. Exit Portal")
        print("=====================================")
        
        choice = input("Please select user type (1-3): ").strip()
        
        if choice == "1":
            admin_menu()
        elif choice == "2":
            member_menu()
        elif choice == "3":
            print("Exiting Portal. Goodbye!")
            sys.exit()
        else:
            print("❌ Invalid selection. Please type 1, 2, or 3.")

if __name__ == "__main__":
    main()
