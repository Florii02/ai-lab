# ============================================================================
# 4. FUNCTIONS - COMPREHENSIVE REFERENCE
# ============================================================================
# WHAT: Reusable blocks of code that perform specific tasks
# WHY: Organize code, reduce repetition, make code more maintainable
# WHEN: Task is used multiple times, logical grouping, complex operations

# ============================================================================
# BASIC FUNCTION DEFINITION AND CALLING
# ============================================================================

# Simple function with no parameters
def greet():
    print("Hello!")

greet()  # Call the function

# Function with parameter
def greet_name(name):
    return f"Hello, {name}!"

result = greet_name("Alice")
print(result)

# ============================================================================
# FUNCTION PARAMETERS
# ============================================================================

# Multiple parameters
def add_numbers(a, b):
    return a + b

print("\n5 + 3 =", add_numbers(5, 3))

# ============================================================================
# DEFAULT PARAMETERS
# ============================================================================
# WHAT: Parameters with default values
# WHY: Make parameters optional, provide sensible defaults
# NOTE: Default parameters must come AFTER required parameters

def greet_with_default(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print("\nWith default:", greet_with_default("Bob"))
print("With custom:", greet_with_default("Bob", "Hi"))

# Multiple default parameters
def create_profile(name, age=None, city="Unknown"):
    profile = f"Name: {name}"
    if age:
        profile += f", Age: {age}"
    profile += f", City: {city}"
    return profile

print("\nProfile 1:", create_profile("Alice"))
print("Profile 2:", create_profile("Bob", 30))
print("Profile 3:", create_profile("Carol", 25, "NYC"))

# ============================================================================
# KEYWORD ARGUMENTS
# ============================================================================
# WHAT: Pass arguments by parameter name
# WHY: Order doesn't matter, improves readability, skip optional params
# NOTE: Keyword arguments must come AFTER positional arguments

def describe_pet(animal_type, pet_name, age):
    print(f"I have a {age}-year-old {animal_type} named {pet_name}")

# Positional arguments (order matters)
print("\nUsing positional arguments:")
describe_pet("dog", "Max", 3)

# Keyword arguments (order doesn't matter)
print("Using keyword arguments:")
describe_pet(pet_name="Whiskers", age=2, animal_type="cat")

# Mixed positional and keyword arguments
print("Mixed arguments:")
describe_pet("hamster", age=1, pet_name="Fluffy")

# ============================================================================
# *ARGS - ARBITRARY POSITIONAL ARGUMENTS
# ============================================================================
# WHAT: Accept any number of positional arguments as a tuple
# WHY: Handle variable number of arguments without knowing count in advance
# USAGE: Perfect for sum, max, concatenation, etc.

def sum_all(*numbers):
    """Sum any number of arguments"""
    total = 0
    for num in numbers:
        total += num
    return total

print("\n*args examples:")
print("sum_all(1, 2, 3):", sum_all(1, 2, 3))
print("sum_all(10, 20, 30, 40, 50):", sum_all(10, 20, 30, 40, 50))

def make_pizza(size, *toppings):
    """Make pizza with any number of toppings"""
    print(f"\nMaking a {size}-inch pizza with:")
    for topping in toppings:
        print(f"  - {topping}")

make_pizza(12, "pepperoni", "mushrooms", "olives")
make_pizza(16, "extra cheese")

# ============================================================================
# **KWARGS - ARBITRARY KEYWORD ARGUMENTS
# ============================================================================
# WHAT: Accept any number of keyword arguments as a dictionary
# WHY: Handle flexible key-value pairs, configuration options
# USAGE: Perfect for configuration, flexible API design

def build_profile(first, last, **user_info):
    """Build profile with required info and any additional info"""
    profile = {
        "first_name": first,
        "last_name": last
    }
    # Add additional key-value pairs from **kwargs
    for key, value in user_info.items():
        profile[key] = value
    return profile

print("\n**kwargs examples:")
user1 = build_profile("Albert", "Einstein",
                      location="Princeton",
                      field="Physics",
                      age=76)
print("User profile:", user1)

# Function accepting both *args and **kwargs
def flexible_function(*args, **kwargs):
    print("\nPositional arguments (*args):", args)
    print("Keyword arguments (**kwargs):", kwargs)

flexible_function(1, 2, 3, name="Alice", age=30, city="NYC")

# ============================================================================
# LAMBDA FUNCTIONS
# ============================================================================
# WHAT: Anonymous (unnamed) functions defined in single line
# WHY: Quick, simple functions for short operations
# WHEN: Used as arguments to other functions, one-time use
# SYNTAX: lambda parameters: expression

# Basic lambda
square = lambda x: x ** 2
print("\nLambda square(5):", square(5))

# Lambda with multiple parameters
multiply = lambda a, b: a * b
print("Lambda multiply(4, 5):", multiply(4, 5))

# Lambda with conditional
max_of_two = lambda a, b: a if a > b else b
print("Lambda max_of_two(10, 20):", max_of_two(10, 20))

# Lambda in practical use - with sorted()
pairs = [(1, 'one'), (3, 'three'), (2, 'two')]
# Sort by second element of tuple
sorted_pairs = sorted(pairs, key=lambda pair: pair[1])
print("Sorted pairs:", sorted_pairs)

# Lambda with map() - apply function to all items
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print("Squared numbers:", squared)

# Lambda with filter() - filter items based on condition
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", evens)

# Lambda function that returns a function
def multiplier(n):
    """Returns a function that multiplies by n"""
    return lambda x: x * n

doubler = multiplier(2)
tripler = multiplier(3)
print("\nDoubler(5):", doubler(5))      # 10
print("Tripler(5):", tripler(5))        # 15

# ============================================================================
# RECURSION
# ============================================================================
# WHAT: Function that calls itself
# WHY: Solve problems that can be broken into smaller similar problems
# WHEN: Tree traversal, mathematical sequences, divide-and-conquer
# WARNING: Must have base case to avoid infinite recursion

# Factorial example: 5! = 5 * 4 * 3 * 2 * 1
def factorial(n):
    """Calculate factorial using recursion"""
    if n == 0 or n == 1:        # Base case
        return 1
    else:
        return n * factorial(n - 1)  # Recursive case

print("\nRecursion examples:")
print("factorial(5):", factorial(5))    # 120
print("factorial(0):", factorial(0))    # 1

# Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, ...
def fibonacci(n):
    """Return nth Fibonacci number"""
    if n <= 1:                  # Base cases
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)  # Recursive case

print("fibonacci(7):", fibonacci(7))    # 13

# Countdown example
def countdown(n):
    """Count down from n to 1"""
    if n <= 0:                  # Base case
        print("Blast off!")
    else:
        print(n)
        countdown(n - 1)        # Recursive case

print("\nCountdown from 5:")
countdown(5)

# Sum of list using recursion
def sum_list(numbers):
    """Sum list elements using recursion"""
    if len(numbers) == 0:       # Base case
        return 0
    else:
        return numbers[0] + sum_list(numbers[1:])  # Recursive case

print("\nsum_list([1,2,3,4,5]):", sum_list([1, 2, 3, 4, 5]))

# ============================================================================
# VARIABLE SCOPE
# ============================================================================
# WHAT: Visibility and lifetime of variables
# WHY: Understand where variables can be accessed
# TYPES: Local, Global, Nonlocal

print("\n" + "="*50)
print("VARIABLE SCOPE")
print("="*50)

# Global variable
x = "awesome"  # Global variable

def show_global():
    # Can read global variable
    print("Inside function, x is:", x)

show_global()
print("Outside function, x is:", x)

# Local variable
def show_local():
    y = "fantastic"  # Local variable (only exists in function)
    print("Inside function, y is:", y)

show_local()
# print(y)  # Would cause error - y doesn't exist outside function

# Modifying global variable from function
count = 0  # Global

def increment():
    global count  # Declare we're using global variable
    count += 1
    print(f"Count inside function: {count}")

increment()
increment()
print(f"Count outside function: {count}")

# ============================================================================
# DOCSTRINGS
# ============================================================================
# WHAT: Documentation strings for functions
# WHY: Explain what function does, parameters, return value
# ACCESS: Using function.__doc__ or help(function)

def calculate_area(length, width):
    """
    Calculate area of rectangle.

    Args:
        length (float): Length of rectangle
        width (float): Width of rectangle

    Returns:
        float: Area of rectangle
    """
    return length * width

print("\n" + "="*50)
print("DOCSTRINGS")
print("="*50)
print(calculate_area.__doc__)

# ============================================================================
# PRACTICAL EXAMPLES
# ============================================================================

print("\n" + "="*50)
print("PRACTICAL EXAMPLES")
print("="*50)

# Function with input validation
def divide(a, b):
    """Safe division with error handling"""
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

print("\n10 / 2 =", divide(10, 2))
print("10 / 0 =", divide(10, 0))

# Function returning multiple values
def get_user_info():
    """Return multiple values as tuple"""
    name = "Alice"
    age = 30
    city = "Berlin"
    return name, age, city  # Returns tuple

name, age, city = get_user_info()  # Unpack tuple
print(f"\nUser: {name}, {age}, {city}")

# Function with list parameter
def process_scores(scores):
    """Calculate statistics from list of scores"""
    if not scores:
        return None
    return {
        "min": min(scores),
        "max": max(scores),
        "avg": sum(scores) / len(scores)
    }

test_scores = [85, 92, 78, 90, 88]
stats = process_scores(test_scores)
print("\nScore statistics:", stats)
