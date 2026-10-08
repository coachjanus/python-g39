var1 = "My String"
print(type(var1))
var1 = 100
print(type(var1))
print(var1 + 50)
print(type(int))
print(type(str))
print(type(True))
print(int(True))
# 00000001
# 00000000
# 00000010
# 00000011
print(int(False))

print(type(10)) # <class 'int'>
print(type(0o10)) # <class 'int'>
print(type(0x10)) # <class 'int'>
print( isinstance(1, int) ) # 

a = 10_000_000_000
print(a)

x = 12.77
print(int(x))

print(7**4300)

x = 0.1 + 0.2
print(x) # 0.30000000000000004

x = 0.1 + 0.1
print(x) # 0.2

# Import the Decimal class from the decimal module
from decimal import Decimal, getcontext
# Create Decimal objects and perform addition
x = Decimal("0.1") + Decimal("0.2")
# Print the result
print(x) # 0.3

# Set precision
getcontext().prec = 4
# Define price and quantity as Decimal objects
price = Decimal("19.99")
qty = Decimal("3")
# Calculate total and print it
total = price * qty
# Print the total
print(total) # 59.97

hello = "Hello"
world = "World"
print(hello + " " + world) # Hello World

print(hello[0]*100) # H
print(hello[0]) # H
print(hello[1]) # e
print(hello[2]) # l
print(hello[3]) # l
print(hello[4]) # o
test = "Hello World"
print("_"*100) # 

print(test[0:5]) # Hello

print(test[:8]) # llo

sentence = "Flat is better than nested"
words = sentence.split() # ['Flat', 'is', 'better', 'than', 'nested']

print(words) # ['Flat', 'is', 'better', 'than', 'nested']
name, age = "John", 30
print("Мене звати %s, мені %d років." % (name, age))

n = 20
m = 25
prod = n * m
print(f'The product of {n} and {m} is {prod}')

ord('a') # 97
ord('#') # 35
ord('€') # 8364
ord('∑') # 8721
chr(97) # 'a'
chr(35) # '#'
chr(8364) # '€'
chr(8721) # '∑'

num1 = 100
num2 = 0
# op == '/'

try:
    print(f"{num1} / {num2} = {num1 / num2}") # Raises ZeroDivisionError
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")