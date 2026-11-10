import sys

def my_decor(fn):
    def wrapper():
        func = fn()
        make_upper_case = func.upper()
        return make_upper_case
    return wrapper

def hi():
    return f"hello there"

decorate = my_decor(hi)

# print(decorate())

def command_decor(fn):
    def wrapper(arg=None):
        if arg == None:
            print(f"""You get an error, You are missing Name.
                  Usage: app.py [OPTIONS] NAME""")
            raise sys.exit("Missing argument Name")
        func = fn(arg)
        make_upper_case = func.upper()
        return make_upper_case
    return wrapper

@command_decor
def hi_name(name):
    return f"hello there {name}"

# print(hi_name())

# print(hi_name("Developer"))
        
def split_sentence(func):
    def wrapper():
        func_ret = func()
        output = func_ret.split()
        return output
    return wrapper

# # Застосуємо декоратори my_decorator та split_sentence до функції:
@split_sentence
@my_decor
def hello_function():
    return 'helllo there, how are you?'
# print(hello_function())

def my_decorator(func):
    def my_wrapper(argument1, argument2):
        print("The arguments are: {0}, {1}".format(argument1, argument2))
        func(argument1, argument2)
    return my_wrapper

@my_decorator
def names(firstName, secondName):
    print("Your first and second names are {0} and {1} respectively".format(firstName, secondName))
    
# print(names("Nicholas", "Samuel"))


def add(*args):
    sum = 0
    for arg in args:
        sum += arg
    print(f"The sum is: {sum}")
    
# add(1,2,3,4,5,6,7,8,9)
# add(10,2,32,45,67,8,9)

def names(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
        
# names(Fname="John",Lname="Doe",work="Doctor")


def my_deco(func):
    def my_wrapper(*args, **kwargs):
        print('Positional arguments:', args)
        print('Keyword arguments:', kwargs)
        func(*args)
    return my_wrapper

@my_deco
def function_without_arguments():
    print("No arguments")
    
# function_without_arguments()


# # Щоб передати значення позиційним аргументам:
@my_deco
def function_with_arguments(x, y, z):
    print(x, y, z)
# function_with_arguments(5, 15, 25)

# # Щоб передати ключові аргументи, потрібно використовувати ключові слова у виклику функції:
@my_deco
def passing_keyword_arguments():
    print("Passing keyword arguments")
    
# passing_keyword_arguments(firstName="Nicholas", secondName="Samuel")


# def decor_input(fn):
#     def wrapper(arg):
#         func = fn(arg)
#         output = func.strip().upper()
#         return output
#     return wrapper

# @decor_input
# def make_upper(string):
#     return string