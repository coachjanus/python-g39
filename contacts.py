from datetime import datetime

# contacts = [
#     ("Alice", "123-456-7890", datetime.now().strftime("%Y-%m-%d %H:%M:%S"), ["Some City", "Some State", "Some Country"]),
#     ("Bob", "987-654-3210", datetime.now().strftime("%Y-%m-%d %H:%M:%S"), ["Another City", "Another State", "Another Country"]),
#     ("Charlie", "555-555-5555", datetime.now().strftime("%Y-%m-%d %H:%M:%S"), ["Yet Another City", "Yet Another State", "Yet Another Country"])
# ]

def add_contact_old():
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
        
# def delete_contact(id_str):
#     try:
#         idx = int(id_str) - 1
#         if idx < 0 or idx >= len(contacts):
#             print("❌ Invalid ID.")
#             return
#         deleted_contact = contacts.pop(idx)
#         print(f"🗑️ Contact '{deleted_contact[0]}' deleted successfully.")
#     except ValueError:
#         print("❌ Invalid input. Please enter a valid number.")
      
def delete_contact(contact_id):
    """Delete a contact by ID"""
    if not contacts:
        print(f"{chr(10060)} No contacts to delete.")
        return
    try:
        contact_id = int(contact_id)
        if contact_id < 1 or contact_id > len(contacts):
            print(f"{chr(10060)} Invalid contact ID.")
            return
    except ValueError:
        print(f"{chr(10060)} Please enter a valid number.")
        return
    deleted_contact = contacts.pop(contact_id - 1)
    print(f"🗑 Contact '{deleted_contact['name']}' deleted successfully!")
      
menu_items = [
    "Add Contact",  
    "View Contacts",
    "Search Contact",
    "Edit Contact",
    "Delete Contact",
    "Exit"
]  
# choice = input(f"Enter your choice (1-{len(menu_items)}): ").strip()
# match choice:
#     case "1": add_contact()
#     case "2": view_contacts()
#     case "3":
#         query = input("Enter term for search: ").strip()
#         search_contact(query)
#     case "4": edit_contact()
#     case "5":
#         view_contacts() # Show contacts before asking for ID
#         id_str = input("Enter ID to delete: ").strip()
#         delete_contact(id_str)
#     case "6":
#         print("👋 Thank you for using Phone Book CLI. Goodbye!")
#     case _: print("❌ Invalid choice. Please try again.")

keys = ["name", "phone", "email", "address", "notes", "added"]

# contact.from_keys = lambda d: (d.get("name"), d.get("phone"), d.get("email"), d.get("address"), d.get("notes"), d.get("added"))
contact = dict.fromkeys(keys, "")
# {'name': "", 'phone': "", 'email': "", 'address': "", 'notes': "", 'added': ""}
print("📞 Welcome to Phone Book CLI")
print("Please choose an option:")
for idx, item in enumerate(menu_items, start=1):
    print(f"{idx}. {item}")
    
# print(contact)  # Print the contact dictionary to verify its structure

print(hash(contact['name']))  # Print the hash of the contact's name

i = 1  # Example index for demonstration
contact['name'] = "John Doe"
contact['phone'] = "123-456-7890"
contact['email'] = "john.doe@example.com"
contact['address'] = "123 Main St, Anytown, USA"
contact['notes'] = "Friend from college" 
added = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"{i:<2} {contact['name']:<8} {contact['phone']:<10} {contact['email']:<15} {contact['address']:<20} {contact['notes']:<20} {added}")  
# Print formatted contact information

contacts = []  # Initialize an empty list to store contacts
values = ['Alice', '456730', 'test@my.com', 'My city', 'My note', datetime.now().isoformat() ]

def save_contact(keys, values):
    """Add a new contact to memory and disk"""
    contact = {}
    for k, v in zip(keys, values):
        contact[k] = v
    contacts.append(contact)
    print(f"✅ Contact '{contact['name'].title()}' added successfully!")
    print(f"📇 Total contacts: {len(contacts)}")
    # print(f"📝 Contact details: {contacts[0]}")

save_contact(keys, values)  # Call the function to save the contact

def get_field(field):
    """Gets valid field from user with validation."""
    
    while True:
        result = input(f"Enter {field}: ").strip()
        if result:
            return result
        print(f"{chr(10060)} {field.title()} cannot be empty.")

def get_optional_field(field):
    """Gets optional field from user."""
    return input(f"Enter {field} (optional): ").strip() or None

# name = get_field("name")
# phone = get_field("phone")
# address = get_optional_field("address")

# def add_contact():
#     name = input("Enter name: ").strip()
#     phone = input("Enter phone number: ").strip()
#     timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     address = input("Enter address (City, State, Country): ").strip().split(", ")
#     contacts.append((name, phone, timestamp, address))
#     print(f"✅ Contact '{name}' added successfully.")

def add_contact():
    """Handle adding a contact with validation"""
    print("\n➕ ADD NEW CONTACT")
    name = get_field('name')
    phone = get_field('phone number')
    email = get_field('email')
    address = get_optional_field('address') # input("Enter address (optional): ").strip() or None
    notes = get_optional_field('notes') # input("Enter notes (optional): ").strip() or None
    save_contact(keys, [name, phone, email, address, notes, datetime.now().isoformat()])
    
# add_contact()


def data_table(contacts, title):
    """Display contacts in a formatted table"""
    print("\n" + "="*80)
    print(f"📱 {title.upper()}")
    print("="*80)
    print(f"{'No.':<3} {'Name':<20} {'Phone':<15} {'Email':<20} {'Added':<10}")
    print("-"*80)
    for i, contact in enumerate(contacts, 1):
        email = contact.get('email', 'N/A')
        address = contact.get('address', 'N/A')
        added = contact.get('added', 'N/A')
        print(f"{i:<3} {contact['name']:<20} {contact['phone']:<15} {email:<20} {added[:10]}")

# for idx, contact in enumerate(contacts, start=1):
#     print(f"{idx:<2} {contact['name']:<8} {contact['phone']:<10} {contact['email']:<15} {contact['address'] or 'N/A':<20} {contact['notes'] or 'N/A':<20} {contact['added']}")  

def view_contacts():
    """Display all contacts"""
    if not contacts:
        print("📭 No contacts found.")
        return
    data_table(contacts, 'contact list')
    
while True:
    print("\nPlease choose an option:")
    for idx, item in enumerate(menu_items, start=1):
        print(f"{idx}. {item}")
    
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
            break
        case _: print("❌ Invalid choice. Please try again.")
    
