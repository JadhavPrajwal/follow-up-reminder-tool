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
