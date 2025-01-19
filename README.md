# Follow-Up Reminder Tool

A simple Python script to track leads and remind business development teams of follow-ups.

## Features

- Add leads with contact details.
- Automatically calculate follow-up due dates.
- Export data to CSV for reporting.

## Code

```python
import csv
from datetime import datetime, timedelta

# Initialize lead list
leads = []

# Add a lead
def add_lead(name, email, company, contact_date):
    lead = {
        "Name": name,
        "Email": email,
        "Company": company,
        "Contact Date": contact_date,
        "Follow-Up Due": (datetime.strptime(contact_date, "%Y-%m-%d") + timedelta(days=7)).strftime("%Y-%m-%d")
    }
    leads.append(lead)
    print("Lead added successfully!")

# View leads that need follow-ups
def view_follow_ups():
    print("\n--- Follow-Up Reminders ---")
    today = datetime.today().strftime("%Y-%m-%d")
    for lead in leads:
        if lead["Follow-Up Due"] <= today:
            print(f"Name: {lead['Name']}, Email: {lead['Email']}, Follow-Up Due: {lead['Follow-Up Due']}")

# Export leads to CSV
def export_to_csv(filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["Name", "Email", "Company", "Contact Date", "Follow-Up Due"])
        writer.writeheader()
        writer.writerows(leads)
    print(f"Leads exported to {filename} successfully!")

# Menu
while True:
    print("\n--- Follow-Up Reminder Tool ---")
    print("1. Add Lead")
    print("2. View Follow-Ups")
    print("3. Export to CSV")
    print("4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter Lead Name: ")
        email = input("Enter Email: ")
        company = input("Enter Company Name: ")
        contact_date = input("Enter Contact Date (YYYY-MM-DD): ")
        add_lead(name, email, company, contact_date)
    elif choice == "2":
        view_follow_ups()
    elif choice == "3":
        filename = input("Enter filename (e.g., leads.csv): ")
        export_to_csv(filename)
    elif choice == "4":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")
```
## Output

### 1. Adding a Lead
When you run the script and choose option 1 to add a lead, the output will look like this:

```--- Follow-Up Reminder Tool ---
1. Add Lead
2. View Follow-Ups
3. Export to CSV
4. Exit
Choose an option: 1
Enter Lead Name: John Doe
Enter Email: johndoe@example.com
Enter Company Name: ABC Corp
Enter Contact Date (YYYY-MM-DD): 2025-01-01
Lead added successfully!
```
### 2. Viewing Follow-Ups
When you choose option 2 to view follow-ups (assuming it's time for follow-up), the output will look like this:
```--- Follow-Up Reminders ---
Name: John Doe, Email: johndoe@example.com, Follow-Up Due: 2025-01-08
```
### 3. Exporting to CSV
When you choose option 3 to export to CSV, the output will look like this:
```
Leads exported to leads.csv successfully!
```
The generated leads.csv file will look like this:
```
Name,Email,Company,Contact Date,Follow-Up Due
John Doe,johndoe@example.com,ABC Corp,2025-01-01,2025-01-08
```
## How to Run
### 1. Install Python
### 2. Run the script in your terminal using:
```
python follow_up_reminder.py
```
## Conclusion
This tool helps business development teams manage leads and track follow-ups efficiently, ensuring no lead is forgotten.




