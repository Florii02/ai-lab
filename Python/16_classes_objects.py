# ============================================================================
# 16. CLASSES AND OBJECTS - OBJECT-ORIENTED PROGRAMMING
# ============================================================================
# WHAT: Blueprint (class) for creating objects with properties and methods
# WHY: Organize code, model real-world entities, reuse code, encapsulation
# WHEN: Complex programs, multiple similar entities, data with behavior

# ============================================================================
# BASIC CLASS DEFINITION
# ============================================================================

print("="*60)
print("BASIC CLASS AND OBJECT")
print("="*60)

# WHAT: Class is a template, object is an instance of class
# WHY: Create multiple objects from same template

class Dog:
    species = "Canis familiaris"  # Class attribute (shared by all instances)

# Creating objects (instances)
dog1 = Dog()
dog2 = Dog()

print(f"dog1 species: {dog1.species}")
print(f"dog2 species: {dog2.species}")
print(f"dog1 and dog2 are different objects: {dog1 is not dog2}")

# ============================================================================
# THE __init__() METHOD (CONSTRUCTOR)
# ============================================================================

print("\n" + "="*60)
print("THE __init__() METHOD")
print("="*60)

# WHAT: Special method called when object is created
# WHY: Initialize object attributes (properties)
# NOTE: self represents the instance itself

class Person:
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute

# Create persons with different attributes
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

print(f"Person 1: {person1.name}, Age: {person1.age}")
print(f"Person 2: {person2.name}, Age: {person2.age}")

# ============================================================================
# INSTANCE METHODS
# ============================================================================

print("\n" + "="*60)
print("INSTANCE METHODS")
print("="*60)

# WHAT: Functions defined inside class that operate on instance
# WHY: Add behavior to objects
# NOTE: First parameter must be self

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.odometer = 0

    def get_description(self):
        """Return formatted description"""
        return f"{self.year} {self.brand} {self.model}"

    def drive(self, miles):
        """Add miles to odometer"""
        self.odometer += miles
        print(f"Driven {miles} miles. Total: {self.odometer} miles")

    def honk(self):
        """Make car sound"""
        print("Beep beep!")

# Create and use car object
my_car = Car("Toyota", "Corolla", 2020)
print(my_car.get_description())
my_car.drive(50)
my_car.drive(30)
my_car.honk()

# ============================================================================
# MODIFYING OBJECT PROPERTIES
# ============================================================================

print("\n" + "="*60)
print("MODIFYING OBJECT PROPERTIES")
print("="*60)

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

student = Student("Charlie", "B")
print(f"Initial grade: {student.grade}")

# Modify property directly
student.grade = "A"
print(f"Updated grade: {student.grade}")

# Add new property
student.school = "Central High"
print(f"School: {student.school}")

# ============================================================================
# THE self PARAMETER
# ============================================================================

print("\n" + "="*60)
print("THE self PARAMETER")
print("="*60)

# WHAT: Reference to current instance of class
# WHY: Access instance attributes and methods
# NOTE: Can use any name, but 'self' is convention

class Calculator:
    def __init__(self, value=0):
        self.value = value

    def add(self, x):
        self.value += x
        return self.value

    def subtract(self, x):
        self.value -= x
        return self.value

    def get_value(self):
        return self.value

calc = Calculator(10)
print(f"Initial value: {calc.get_value()}")
print(f"After add(5): {calc.add(5)}")
print(f"After subtract(3): {calc.subtract(3)}")

# Alternative self names (not recommended)
class Example:
    def __init__(myself, data):
        myself.data = data

    def show(myself):
        print(f"Data: {myself.data}")

ex = Example("test")
ex.show()

# ============================================================================
# DELETE OBJECT PROPERTIES AND OBJECTS
# ============================================================================

print("\n" + "="*60)
print("DELETE PROPERTIES AND OBJECTS")
print("="*60)

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

product = Product("Laptop", 999)
print(f"Product: {product.name}, Price: ${product.price}")

# Delete property
del product.price
# print(product.price)  # Would cause AttributeError

# Delete object
del product
# print(product)  # Would cause NameError

print("Property and object deleted")

# ============================================================================
# PASS STATEMENT
# ============================================================================

print("\n" + "="*60)
print("PASS STATEMENT IN CLASSES")
print("="*60)

# WHAT: Placeholder for empty class
# WHY: Define class structure before implementation

class EmptyClass:
    pass  # Will implement later

obj = EmptyClass()
print(f"Empty object created: {obj}")

# ============================================================================
# __str__() METHOD
# ============================================================================

print("\n" + "="*60)
print("__str__() METHOD")
print("="*60)

# WHAT: Define string representation of object
# WHY: Readable output when printing object

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.pages} pages)"

book = Book("1984", "George Orwell", 328)
print(book)  # Uses __str__() method

# Without __str__() method
class BookNoStr:
    def __init__(self, title, author):
        self.title = title
        self.author = author

book2 = BookNoStr("Animal Farm", "George Orwell")
print(book2)  # Prints memory address

# ============================================================================
# CLASS ATTRIBUTES VS INSTANCE ATTRIBUTES
# ============================================================================

print("\n" + "="*60)
print("CLASS VS INSTANCE ATTRIBUTES")
print("="*60)

class Employee:
    company = "TechCorp"  # Class attribute (shared)
    employee_count = 0    # Class attribute

    def __init__(self, name, salary):
        self.name = name        # Instance attribute (unique)
        self.salary = salary    # Instance attribute (unique)
        Employee.employee_count += 1

emp1 = Employee("Alice", 75000)
emp2 = Employee("Bob", 80000)

print(f"emp1: {emp1.name}, Company: {emp1.company}")
print(f"emp2: {emp2.name}, Company: {emp2.company}")
print(f"Total employees: {Employee.employee_count}")

# Modifying class attribute affects all instances
Employee.company = "NewTech"
print(f"\nAfter changing class attribute:")
print(f"emp1 company: {emp1.company}")
print(f"emp2 company: {emp2.company}")

# ============================================================================
# PRACTICAL EXAMPLES
# ============================================================================

print("\n" + "="*60)
print("PRACTICAL EXAMPLES")
print("="*60)

# Example 1: Bank Account
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        return "Invalid amount"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        if amount > 0:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        return "Invalid amount"

    def get_balance(self):
        return f"{self.owner}'s balance: ${self.balance}"

account = BankAccount("Alice", 1000)
print(account.get_balance())
print(account.deposit(500))
print(account.withdraw(300))
print(account.get_balance())

# Example 2: Rectangle
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return f"Rectangle({self.width}x{self.height})"

rect = Rectangle(5, 3)
print(f"\n{rect}")
print(f"Area: {rect.area()}")
print(f"Perimeter: {rect.perimeter()}")

# Example 3: Shopping Cart
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item, price):
        self.items.append({"item": item, "price": price})
        print(f"Added {item} (${price})")

    def remove_item(self, item):
        for cart_item in self.items:
            if cart_item["item"] == item:
                self.items.remove(cart_item)
                print(f"Removed {item}")
                return
        print(f"{item} not in cart")

    def total(self):
        return sum(item["price"] for item in self.items)

    def show_cart(self):
        print("\nShopping Cart:")
        for item in self.items:
            print(f"  {item['item']}: ${item['price']}")
        print(f"  Total: ${self.total()}")

cart = ShoppingCart()
cart.add_item("Apple", 1.50)
cart.add_item("Banana", 0.75)
cart.add_item("Milk", 3.00)
cart.show_cart()
cart.remove_item("Banana")
cart.show_cart()
