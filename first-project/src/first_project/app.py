from datetime import datetime
import pickle
# import sys
from .helpers import get_field, get_optional_field, get_updated_field, normalize
from pathlib import Path

contacts = {}
keys = ["name", "phone", "email", "address", "notes", "added"]

menu_items = (
    "Add Contact",
    "View All Contacts",
    "Search Contact",
    "Edit Contact",
    "Delete Contact",
    "Exit"
)
contact =  dict.fromkeys(keys)

def save_contacts(contacts, db_name='db.pkl'):
    with open(db_name, "wb") as f:
        pickle.dump(contacts, f)

def load_contacts(db_name: str):
    """Load contacts from file."""
    try:
        with open(db_name, "rb") as f:
            return pickle.load(f)
    except (FileNotFoundError, EOFError, pickle.UnpicklingError):
        return {}

def add_contact(contacts, db_name):
    new_contact = {}  # Local dict!
    for key in keys:
        if key in ["name", "phone", "email"]:
            new_contact[key] = get_field(key)
        elif key == "added":
            new_contact[key] = datetime.now().strftime("%Y-%m-%d")
        else:
            new_contact[key] = get_optional_field(key)
    
    if new_contact["name"] and new_contact["phone"]:
        contacts[len(contacts) + 1] = new_contact  
        save_contacts(contacts, db_name)
        print(f"✅ Contact '{new_contact['name']}' added successfully.")

def data_table(contacts_dict, title):
    print("\n" + "="*80)
    print(f"📱 {title.upper()}")
    print("="*80)
    print(f"{'No.':<3} {'Name':<20} {'Phone':<15} {'Email':<20} {'Added':<10}")
    print("-"*80)
    
    for i, contact in enumerate(contacts_dict.values(), 1):
        print(f"{i:<3} {contact['name']:<20} {contact['phone']:<15} "
              f"{contact['email']:<20} {contact['added'][:10]:<10}")

def view_contacts(contacts):
    """Display all contacts"""
    if not contacts:
        print("📭 No contacts found.")
        return
    data_table(contacts, 'contact list')
    
def search_contact(contacts):
    """Search for contacts by name, phone, or email"""
    search_term = normalize(input("Enter name, phone, or email to search: "))
    search_results = {
        id: contact for id, contact in contacts.items()
        if any(search_term in normalize(contact[k]) for k in ["name", "phone", "email"])
    }
    if not search_results:
        print("🔍 No contacts found matching your search.")
        return
    data_table(search_results, 'SEARCH RESULTS')

def display_menu():
    """Displays the menu options."""
    
    print("\n" + "="*60)
    print("📱 Simple Command-Line Contact Manager")
    print("="*60)
    
    for idx, item in enumerate(menu_items, 1):
        print(f"{idx}. {item}")
        
    return input(f"Enter your choice (1-{len(menu_items)}): ").strip()

def edit_contact(contacts, db_name):
    """Edit an existing contact."""
    id_str = input("Enter the contact ID to edit: ").strip()
    if not id_str.isdigit() or int(id_str) not in contacts:
        print("❌ Invalid contact ID.")
        return
    
    contact_id = int(id_str)
    contact = contacts[contact_id]
    
    print(f"Editing contact '{contact['name']}' (ID: {contact_id})")
    
    for key in keys:
        if key in ["name", "phone", "email"]:
            contact[key] = get_updated_field(key, contact[key])
        elif key == "added":
            contact[key] = datetime.now().strftime("%Y-%m-%d")
        else:
            contact[key] = get_updated_field(key, contact[key], optional=True)
            
    print(f"✅ Contact '{contact['name']}' updated successfully.")
    save_contacts(contacts, db_name)

def delete_contact(contacts, db_name):
    """Delete contact by id."""
    if not contacts:
        print("❌ No contacts to delete.")
        return
    
    view_contacts()
    id_str = input("\nEnter contact ID to delete: ").strip()
    
    if not id_str.isdigit() or int(id_str) not in contacts:
        print("❌ Invalid contact ID.")
        return
    
    name = contacts[int(id_str)]["name"]
    valid_answers = {"yes", "Yes", "y", "Y", "no", "No", "n", "N"}
    
    while (confirm := input(f"Delete '{name}'? (y/n): ").strip().lower()) not in valid_answers:
        print(f"Please answer one of {', '.join(valid_answers)}")
        
    confirm = normalize(confirm)[0]

    if confirm == 'y':
        del contacts[int(id_str)]
        save_contacts(contacts, db_name)
        print(f"🗑️ '{name}' deleted!")
    else:
        print("Cancelled.")

def ui(contacts, db_name):
    while True:
        match display_menu():
            case "1":
                add_contact(contacts, db_name)
            case "2":
                view_contacts(contacts)
            case "3":
                search_contact(contacts)
            case "4":
                edit_contact(contacts, db_name)
            case "5":
                delete_contact(contacts, db_name)
            case '6':
                print("👋 Thank you for using Phone Book CLI. Goodbye!")
                break
            case _:
                print("❌ Invalid choice. Please enter a number between 1 and 6.")
def app(db_name):
    # print("Hello from first-project!")
    contacts = load_contacts(db_name)
    ui(contacts, db_name)
    
