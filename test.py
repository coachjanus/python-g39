from datetime import datetime

def test_datetime():
    # Get the current date and time
    now = datetime.now()
    
    # Print the current date and time
    print("Current date and time:", now)
    
    # Format the date and time
    formatted_now = now.strftime("%d-%m-%Y %H:%M:%S")
    print("Formatted date and time:", formatted_now)
    
    # Check if the year is a leap year
    year = now.year
    is_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    print(f"Is {year} a leap year? {'Yes' if is_leap_year else 'No'}")
    
# test_datetime()

# contacts = [
#     ["Alice", "123-456-7890", datetime.now().strftime("%Y-%m-%d %H:%M:%S"), [Some City, Some State, Some Country]],
#     ["Bob", "987-654-3210", datetime.now().strftime("%Y-%m-%d %H:%M:%S"), [Another City, Another State, Another Country]],
#     ["Charlie", "555-555-5555", datetime.now().strftime("%Y-%m-%d %H:%M:%S"), [Yet Another City, Yet Another State, Yet Another Country]]
# ]

# print("name of the first contact in Contacts List:", contacts[0][0])  # Print name of the first contact
# print("phone number of the first contact in Contacts List:", contacts[0][1])  # Print phone number of the first contact
# print("timestamp of the first contact in Contacts List:", contacts[0][2])  # Print timestamp of the first contact
# print("address of the first contact in Contacts List:", contacts[0][3])  # Print address of the first contact
# print("City of the first contact in Contacts List:", contacts[0][3][0])  # Print city of the first contact
# print("State of the first contact in Contacts List:", contacts[0][3][1])  # Print state of the first contact
# print("Country of the first contact in Contacts List:", contacts[0][3][2])  # Print country of the first contact

contacts = [
    ("Alice", "123-456-7890", datetime.now().strftime("%Y-%m-%d %H:%M:%S"), ["Some City", "Some State", "Some Country"]),
    ("Bob", "987-654-3210", datetime.now().strftime("%Y-%m-%d %H:%M:%S"), ["Another City", "Another State", "Another Country"]),
    ("Charlie", "555-555-5555", datetime.now().strftime("%Y-%m-%d %H:%M:%S"), ["Yet Another City", "Yet Another State", "Yet Another Country"])
]

print("name of the first tuples item in Contacts List:", contacts[0][0])  # Print name of the first tuple element
print("phone number of the first contact in Contacts List:", contacts[0][1])  # Print phone number of the first contact
print("timestamp of the first contact in Contacts List:", contacts[0][2])  # Print timestamp of the first contact
print("address of the first contact in Contacts List:", contacts[0][3])  # Print address of the first contact
print("City of the first contact in Contacts List:", contacts[0][3][0])  # Print city of the first contact
print("State of the first contact in Contacts List:", contacts[0][3][1])  # Print state of the first contact
print("Country of the first contact in Contacts List:", contacts[0][3][2])  # Print country of the first contact


x = range(5)
print(x) # range(0, 5)
# range() повертає об’єкт діапазону класу, а не список чи кортеж значень.
print(type(x)) # <class 'range'>
print(list(range(5))) # [0, 1, 2, 3, 4]
print(list(range(1, 7))) # [1, 2, 3, 4, 5, 6]
print(list(range(1, 20, 2))) # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
numbers = list(range(1, 20, 2))
print(numbers) # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(list(range(2, 20, 2))) # [2, 4, 6, 8, 10, 12, 14, 16, 18]

print(numbers.index(11)) # 5