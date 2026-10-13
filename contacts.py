from datetime import datetime

contacts = [
    ("Alice", "123-456-7890", datetime.now().strftime("%Y-%m-%d %H:%M:%S"), ["Some City", "Some State", "Some Country"]),
    ("Bob", "987-654-3210", datetime.now().strftime("%Y-%m-%d %H:%M:%S"), ["Another City", "Another State", "Another Country"]),
    ("Charlie", "555-555-5555", datetime.now().strftime("%Y-%m-%d %H:%M:%S"), ["Yet Another City", "Yet Another State", "Yet Another Country"])
]

def add_contact():
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    address = input("Enter address (City, State, Country): ").strip().split(", ")
    contacts.append((name, phone, timestamp, address))
    print(f"✅ Contact '{name}' added successfully.")
def view_contacts():
    if not contacts:
        print("📭 No contacts found.")
        return
    print("\n📇 Contacts List:")
    for idx, (name, phone, timestamp, address) in enumerate(contacts, start=1):
        print(f"{idx}. Name: {name}, Phone: {phone}, Added: {timestamp}, Address: {', '.join(address)}")


def search_contact(query):
    results = [c for c in contacts if query.lower() in c[0].lower() or query in c[1]]
    if not results:
        print(f"🔍 No contacts found for '{query}'.")
        return
    print(f"\n🔍 Search Results for '{query}':")
    for idx, (name, phone, timestamp, address) in enumerate(results, start=1):
        print(f"{idx}. Name: {name}, Phone: {phone}, Added: {timestamp}, Address: {', '.join(address)}")
def edit_contact():
    view_contacts()
    id_str = input("Enter ID to edit: ").strip()
    try:
        idx = int(id_str) - 1
        if idx < 0 or idx >= len(contacts):
            print("❌ Invalid ID.")
            return
        name, phone, timestamp, address = contacts[idx]
        new_name = input(f"Enter new name (or press Enter to keep '{name}'): ").strip() or name
        new_phone = input(f"Enter new phone (or press Enter to keep '{phone}'): ").strip() or phone
        new_address = input(f"Enter new address (or press Enter to keep '{', '.join(address)}'): ").strip().split(", ") or address
        contacts[idx] = (new_name, new_phone, timestamp, new_address)
        print(f"✅ Contact ID {id_str} updated successfully.")
    except ValueError:
        print("❌ Invalid input. Please enter a valid number.")
def delete_contact(id_str):
    try:
        idx = int(id_str) - 1
        if idx < 0 or idx >= len(contacts):
            print("❌ Invalid ID.")
            return
        deleted_contact = contacts.pop(idx)
        print(f"🗑️ Contact '{deleted_contact[0]}' deleted successfully.")
    except ValueError:
        print("❌ Invalid input. Please enter a valid number.")
      
      
menu_items = [
    "Add Contact",  
    "View Contacts",
    "Search Contact",
    "Edit Contact",
    "Delete Contact",
    "Exit"
]  
choice = input(f"Enter your choice (1-{len(menu_items)}): ").strip()
match choice:
    case "1": add_contact()
    case "2": view_contacts()
    case "3":
        query = input("Enter term for search: ").strip()
        search_contact(query)
    case "4": edit_contact()
    case "5":
        view_contacts() # Show contacts before asking for ID
        id_str = input("Enter ID to delete: ").strip()
        delete_contact(id_str)
    case "6":
        print("👋 Thank you for using Phone Book CLI. Goodbye!")
    case _: print("❌ Invalid choice. Please try again.")