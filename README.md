# GymPulse Management System

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Local Setup](#local-setup)
- [Usage Guide](#usage-guide)
- [Known Issues](#known-issues)
- [Potential Improvements](#potential-improvements)
- [License](#license)

## Overview
**GymPulse Management System** is a beginner-friendly Python command-line program that helps gym staff manage members, membership plans and memberships. A numbered menu lets the gym administrator add and remove members, create membership plans, assign a plan to a member and see when each membership expires. Gym members can use the same program to view the available plans and their own membership details. Everything is saved to a JSON file so the data is still there the next time the program runs.

### Purpose
- Practice object-oriented programming in Python: classes, inheritance, properties with validation, and class methods
- Show how objects that belong together (members, plans and the memberships that link them) can be connected by ID
- Show how to save and load program data with JSON
- Practice working as a team by splitting a program into separate files that depend on each other

## Features

### Core Features
- **Add, View and Remove Members** — each member has a name and a validated Kenyan phone number, and gets an ID such as `MEM1001`
- **Create and View Membership Plans** — each plan has a name, a price in KSh, a duration in days and an optional description, and gets an ID such as `PLN1`
- **Assign Memberships** — give a member a plan, starting today or on a date the administrator enters. The expiry date is worked out automatically from the plan's duration, and the ID looks like `MS1`
- **Track Expiry Dates** — every membership shows its start date, its expiry date and whether it is `Active` or `Expired`
- **Member View** — a member can see the available plans, their own memberships and their own details
- **Saved Data** — members, plans and memberships are written to `data/data.json` after every change and loaded again at start-up

### User Experience Features
- **Menu-Driven Interface** — numbered menus for each role that repeat until the user chooses to go back or exit
- **Input Validation** — empty names, invalid phone numbers, bad prices or durations and wrongly formatted dates show a friendly message instead of crashing
- **Clear Messages** — the program says when a member, plan or membership cannot be found, and when a member already has an active membership
- **Forgiving IDs** — member and plan IDs can be typed in lower case, for example `mem1001`

## Technologies Used

### Language
- **Python 3** — the whole program is written in Python

### Standard Library
- **`json`** — saving and loading the data file
- **`pathlib`** — building the path to the data file and creating the `data/` folder
- **`re`** — checking that a phone number has a valid format
- **`datetime`** — working out expiry dates and checking whether a membership has expired
- **`unittest`** — running the automated tests

### Third-Party Packages
- None. The program needs nothing beyond Python itself.

## Project Structure

```
gym-membership-management/
├── main.py                 # the menus and the functions the menus call
├── models/
│   ├── person.py           # Person base class
│   ├── member.py           # Member class (inherits from Person)
│   ├── plan.py             # MembershipPlan class
│   └── membership.py       # Membership class
├── utils/
│   └── storage.py          # save_data() and load_data()
├── tests/
│   └── test_plan.py        # unit tests for MembershipPlan
├── data/
│   └── data.json           # saved data (created automatically)
└── README.md
```

The program is built from four classes:

| Class | Main attributes | Main methods |
|---|---|---|
| `Person` | `name` (must be non-empty text) | — |
| `Member` (inherits `Person`) | `member_id`, `phone` (validated) | `create`, `all`, `find`, `remove`, `to_dict`, `from_dict` |
| `MembershipPlan` | `plan_id`, `name`, `price`, `duration_days`, `description` | `create`, `all`, `find`, `remove`, `clear`, `to_dict`, `from_dict` |
| `Membership` | `membership_id`, `member_id`, `plan_id`, `start_date`, `expiry_date` | `assign`, `all`, `for_member`, `is_expired`, `to_dict`, `from_dict` |

- Each class keeps its own collection of objects and its own ID counter, so IDs are generated automatically (`MEM1001`, `MEM1002`, ...)
- A `Membership` links one member to one plan by storing their IDs, and its expiry date is the start date plus the plan's duration
- `to_dict()` and `from_dict()` turn objects into plain dictionaries and back, which is how they are written to and read from JSON
- `save_data()` and `load_data()` in `utils/storage.py` handle the file
- `main.py` shows the menus in `while` loops and calls the right function for the chosen option

## Local Setup

### Requirements
- Python 3.8 or higher
- A terminal or command prompt

### Installation
1. Clone the repository:
   ```
   git clone <your-repo-url>
   ```
2. Navigate into the project directory:
   ```
   cd gym-membership-management
   ```
3. There are no packages to install.
4. Run the program from inside the project folder:
   ```
   python3 main.py
   ```
   On Windows, use `python main.py` instead.

Run the program from the project folder every time. The data file is found using a path relative to where you start the program. The `data/` folder and `data.json` are created automatically the first time something is saved.

### Running the Tests
From the project folder:
```
python3 -m unittest discover tests
```
The tests check that a plan can be created, found and removed, and that an invalid price or duration is rejected.

## Usage Guide

When the program starts, it asks for a role:

```
SELECT YOUR ROLE
1. Gym Administrator
2. Gym Member
0. Exit
```

There is no login. Choosing the administrator role opens the main menu directly, and a member types their member ID when they ask to see their own information.

The administrator's main menu:

```
MAIN MENU
1. Manage Gym Members
2. Manage Membership Plans
3. Assign Memberships
4. Record Attendance
5. View Available Membership Plans
0. Log Out
```

The member menu:

```
GYM MEMBER MENU
1. View Available Membership Plans
2. View My Membership
3. View My Attendance
4. View My Details
0. Log Out
```

Type a number and press Enter. After each action the menu appears again. Options 4 (Record Attendance) and 3 on the member menu (View My Attendance) are not built yet. See [Known Issues](#known-issues).

### Creating a Membership Plan
1. Choose role **1**, then **2. Manage Membership Plans**, then **1. Create Membership Plan**
2. Enter the plan name, the price in KSh, the duration in days and an optional description
3. The program shows the new plan and its ID, for example `PLN1`

### Viewing Plans
1. As the administrator, choose **2. Manage Membership Plans**, then **2. View Membership Plans**, or choose **5** on the main menu
2. As a member, choose **1** on the member menu

### Adding a Member
1. Choose **1. Manage Gym Members**, then **1. Add Member**
2. Enter the member's name and phone number. The phone number must be `0` followed by 9 digits, starting `07` or `01`
3. The program shows the new member and their ID, for example `MEM1001`

### Viewing Members
1. Choose **1. Manage Gym Members**, then **2. View Members**

### Removing a Member
1. Choose **1. Manage Gym Members**, then **3. Remove Member**
2. Enter the member's ID

### Assigning a Membership
1. Choose **3. Assign Memberships**, then **1. Assign Plan to Member**
2. Enter the member ID and the plan ID exactly as shown in the lists
3. Enter a start date as `YYYY-MM-DD`, or press Enter to start today
4. The program shows the membership, its expiry date and its status. A member who already has an active membership cannot be given another one

### Viewing a Member's Memberships
1. As the administrator, choose **3. Assign Memberships**, then **2. View Member Memberships**, and enter the member ID
2. As a member, choose **2. View My Membership** and enter your own member ID

### Viewing My Details
1. On the member menu, choose **4. View My Details** and enter your member ID

### Exiting
1. Choose **0** on the main menu to log out, then **0** on the role menu to close the program. Data is saved after every change, so nothing extra is needed before exiting

### Example Session
The lists of menu options are left out below to keep it short.
```
No saved data found. Starting with empty records.
       GymPulse Management System
Choose your role: 1
MAIN MENU
Choose an option: 2
MEMBERSHIP PLANS
Choose an option: 1
CREATE MEMBERSHIP PLAN
Enter plan name: Monthly
Enter plan price (KSh): 1500
Enter duration in days: 30
Enter description (optional): Monthly gym membership
Data saved successfully.
Plan created successfully!
PLN1 | Monthly | KSh 1,500.00 | 30 days
    Monthly gym membership
MEMBERSHIP PLANS
Choose an option: 0
MAIN MENU
Choose an option: 1
GYM MEMBERS
Choose an option: 1
ADD GYM MEMBER
Enter member name: Jane Wanjiru
Enter phone number (0...): 12345
Error: Invalid phone number. Use 0 followed by 9 digits.
Please try again.
Enter member name: Jane Wanjiru
Enter phone number (0...): 0712345678
Data saved successfully.
Member added successfully!
Member ID: MEM1001
Name: Jane Wanjiru
Phone Number: 0712345678
GYM MEMBERS
Choose an option: 0
MAIN MENU
Choose an option: 3
ASSIGN MEMBERSHIPS
Choose an option: 1
ASSIGN PLAN TO MEMBER
REGISTERED GYM MEMBERS
-------------------------
Member ID: MEM1001
Name: Jane Wanjiru
Phone Number: 0712345678
Enter member ID: MEM1001
AVAILABLE MEMBERSHIP PLANS
-------------------------
PLN1 | Monthly | KSh 1,500.00 | 30 days
    Monthly gym membership
Enter plan ID: PLN1
Enter start date (YYYY-MM-DD), or press Enter for today:
Data saved successfully.
Membership assigned successfully!
Membership ID: MS1
Member: Jane Wanjiru
Plan: Monthly
Start date: 2026-10-22
Expiry date: 2026-11-21
Status: Active
ASSIGN MEMBERSHIPS
Choose an option: 0
MAIN MENU
Choose an option: 0
       GymPulse Management System
Choose your role: 2
GYM MEMBER MENU
Choose an option: 2
Enter member ID: MEM1001
MEMBERSHIPS FOR Jane Wanjiru
-------------------------
Membership ID: MS1
Plan ID: PLN1
Plan: Monthly
Start date: 2026-10-22
Expiry date: 2026-11-21
Status: Active
GYM MEMBER MENU
Choose an option: 0
Logging out...
       GymPulse Management System
Choose your role: 0
Thank you for using GymPulse. Goodbye!
```
Run the program again and the same plan, member and membership are loaded from `data/data.json`.

## Known Issues
- **Attendance is not implemented yet.** "Record Attendance" and "View My Attendance" only show a "not implemented yet" message, and the `attendance` section of the data file is always empty
- **Removing a member leaves their memberships behind, and their ID can be reused.** If the member with the highest ID is removed and the program is restarted, the next new member gets that same ID and appears to own the removed member's old membership
- **A member can only have one active membership at a time**, so a membership cannot be renewed early. The error message also says "with this plan", but the rule applies to any plan
- **A damaged `data/data.json` is replaced.** The program starts with empty records and overwrites the file the next time something is saved
- **Plans cannot be edited or deleted from the menu**, only created and viewed
- **No login.** Anyone who starts the program can choose the administrator role, and a member can view any member's details by typing that member's ID
- **Duplicates are allowed.** Two members can have the same phone number, and two plans can have the same name
- **Past start dates are accepted.** Only the date format is checked, so a membership that starts far in the past can be expired as soon as it is assigned
- **Only phone numbers starting with `07` or `01` are accepted**, so numbers written as `+254...` are rejected
- **Tests cover plans only.** There are no automated tests yet for members or memberships

## Potential Improvements
- **Record Attendance** — check members in, show today's visits and show each member's attendance history, refusing check-ins for members with no active membership
- **Remove Memberships With Members** — delete or block the removal of a member's memberships, and never reuse an ID
- **Edit and Delete Plans** — change a plan's details or remove it, but only if no membership uses it
- **Renewals** — let an administrator queue a new membership to start when the current one ends
- **Expiring Soon Alerts** — list members whose memberships end within the next few days
- **Duplicate Checks** — refuse a phone number that is already registered
- **Login** — add a simple administrator password so members cannot open the administrator menu
- **Automated Tests** — add unit tests for `Member`, `Membership` and the storage functions

## License

MIT License

Copyright © 2026 Dennis Sambu, Josphat Kipsoi and Sharon Wanjiru

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
