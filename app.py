"""_summary_

    Returns:
        _type_: _description_
"""
# comments

# This is a sample Python script that demonstrates basic functionality.

foo = "Hello, World!"
print(foo)

print(3 - 10000)  # This will print a negative number
print(10000 - 3)  # This will print a positive number


def add_numbers(a, b):
    """This function takes two numbers and returns their sum."""
    return a + b

result = add_numbers(5, 3)
print(result)  # This will print 8

print("=== Simple Command-Line Calculator ===\n")
a = b = 2
print("a: ", a)
print("b: ", b)
print("a + b = ", a + b)
print("a - b = ", a - b)
print("a * b = ", a * b)   

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
print("a + b = ", a + b)
operation = input("Enter an operation (+, -, *, /): ")
if operation == "+":
    print("Result: ", a + b)
elif operation == "-":
    print("Result: ", a - b)
elif operation == "*":
    print("Result: ", a * b)
elif operation == "/":
    if b != 0:
        print("Result: ", a / b)
    else:
        print("Error: Division by zero is not allowed.") 
        
else:
    print("Invalid operation. Please enter one of +, -, *, or /.")

