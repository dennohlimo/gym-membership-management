# GymPulse Management System 🏋️‍♂️

GymPulse is a command-line interface (CLI) application written in Python designed to manage gym operations seamlessly. It features object-oriented models, robust validation for Kenyan phone formatting, live subscription expiration checking, and specific operation portals split by user roles.

---

## 🚀 Key Features

### 👔 Gym Administrator Portal

* **Manage Gym Members:** Seamlessly add new gym members, view registration rosters, or remove members from active systems.
* **Manage Membership Plans:** Design and create multi-day subscription rate tiers with customizable pricing and timelines.
* **Assign Memberships:** Dynamically bind active subscription packages to specific members with automated system validation constraints.
* **Live Attendance Dashboard:** View an overview table of all gym members, displaying their names, phone contacts, raw plan codes, and live color/status markers (`✅ ACTIVE` or `❌ EXPIRED`).

### 🏋️ Gym Member Portal

* **Live Attendance & Profile View:** Quick lookups using a Member ID (e.g., `MEM1003`) to print a personal account card displaying active profile data, validity ranges, and active status updates.
* **Membership History:** Inspect historical and present membership packages assigned to your account.

---

## 📁 System Architecture & Directory Layout

The project follows a modular Object-Oriented design structure:

```text
gym-membership-management/
│
├── main.py                  # Primary landing module and interface entry loop
├── attendance.py            # Attendance dashboards and member profile panels
├── LICENSE                  # Open-source licensing agreement file
│
├── models/                  # Data layer object structures (Blueprints)
│   ├── person.py            # Base validation object for foundational profiles
│   ├── member.py            # Member subclass enforcing unique IDs and phone limits
│   ├── plan.py              # Subscription structure rules and validation frameworks
│   └── membership.py        # Framework computing active dates and validation rules
│
├── utils/
│   └── storage.py           # Core read/write engine for system stability
│
└── data/
    └── data.json            # Central flat-file database storage matrix
```

---

## 🛠️ Requirements & Installation

### Prerequisites

Make sure you have **Python 3** installed on your operating system (Ubuntu/Debian via WSL, macOS, or Windows).

### Getting Started

1. **Clone the repository to your local computer machine:**

   ```bash
   git clone https://github.com
   cd gym-membership-management
   ```

2. **Verify you are on the feature branch (if testing unmerged details):**

   ```bash
   git checkout adding-attendance.py
   ```

---

## 💻 Running the Application

Launch the central interface menu engine by running the following command from the project root directory:

```bash
python3 main.py
```

### Quick Test Identities (Seeded in `data.json`)

You can log in to test features using these sample records:

* **Administrator Portal:** Select Role `1`.
* **Member Portal (Role `2`) Profiles:**
  * `MEM1001` — Denn (Active)
  * `MEM1002` — Limo (Active)
  * `MEM1003` — Josphat (Active)

---

## 👥 Group Project Contributors

* **Josphat kipsoi** — Developed the core `attendance.py` module, updated integrated view actions inside `main.py`, and handled data layer testing and configuration.
* **Dennis Sambu & Sharon Wanjiru** — Designed and implemented the core Object-Oriented system architecture, including member management schemas, data validation models, and membership plan structures.

---

## 📄 License

This project is licensed under the MIT License - see the details below:

```text
MIT License

Copyright (c) 2026 Josphat and Group Members

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
