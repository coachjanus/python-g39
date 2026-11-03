def inner():
    print("I am function inner()!")
def outer(function):
    function()
outer(inner)

animals = ["ferret", "vole", "dog", "gecko"]
#['dog', 'ferret', 'gecko', 'vole']
sorted_list = sorted(animals, key=len) # ['dog', 'vole', 'gecko', 'ferret']

print(sorted_list)

def reverse_len(s):
    return -len(s)

sorted_list = sorted(animals, key=reverse_len) # ['ferret', 'gecko', 'vole', 'dog']

print(sorted_list)

a = [10,3,4,1,9]
a.sort() # [1, 3, 4, 9, 10]
print(a)

def outer(): # outer() визначає локальну функцію inner().
    def inner():
        print("I am function inner()!")
    return inner # Function outer() returns function inner()

function = outer() # значення, що повертається з outer(), призначається змінній.
print(function) # <function outer.<locals>.inner at 0x7f18bc85faf0>
# Після цього можна викликати inner()
function() # I am function inner()!
# Можна навіть не застосовувати проміжного function
outer()() # I am function inner()!

numbers = [-2, -1, 0, 1, 2]
# Виклик filter() відфільтровує від’ємні числа та 0.
positive_numbers = filter(lambda n: n > 0, numbers)
print(positive_numbers) # <filter object at 0x7f3632683610>
print(list(positive_numbers)) # [1, 2]
# Визначення функції is_positive(), яка отримує число як аргумент і повертає True, якщо число більше
# за 0, в іншому випадку повертає False.
def is_positive(n):
    return n > 0

# Виклик filter() застосовує is_positive() до кожного значення в списку,відфільтровуючи від’ємні числа.
# Оскільки filter() повертає ітератор, потрібно викликати list(), щоб створити остаточний список.
print(list(filter(is_positive, numbers))) # [1, 2]

import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
        return True
    

# виклик filter() повертає всі прості числа в діапазоні від 1 до 50.
print(list(filter(is_prime, range(1, 201)))) # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]


list(map(lambda s: s[::-1], ["cat", "dog", 3.14159, "gecko"]))