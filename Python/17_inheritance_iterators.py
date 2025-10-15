# ============================================================================
# 17. INHERITANCE AND ITERATORS
# ============================================================================
# Part 1: Inheritance - Create new classes based on existing ones
# Part 2: Iterators - Objects that can be iterated over

# ============================================================================
# PART 1: INHERITANCE
# ============================================================================

print("="*60)
print("INHERITANCE - BASICS")
print("="*60)

# WHAT: Child class inherits properties and methods from parent class
# WHY: Code reuse, create specialized versions, organize hierarchies
# WHEN: "is-a" relationship (Dog is-a Animal)

# Parent class (Base class)
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return f"{self.name} makes a sound"

    def info(self):
        return f"{self.name} is {self.age} years old"

# Child class inherits from Animal
class Dog(Animal):
    pass  # Inherits everything from Animal

# Create dog object
dog = Dog("Buddy", 5)
print(dog.info())      # Inherited method
print(dog.speak())     # Inherited method

# ============================================================================
# ADDING CHILD CLASS METHODS
# ============================================================================

print("\n" + "="*60)
print("EXTENDING CHILD CLASSES")
print("="*60)

# Child class with additional methods
class Cat(Animal):
    def speak(self):
        # Override parent method
        return f"{self.name} says Meow!"

    def purr(self):
        # New method specific to Cat
        return f"{self.name} is purring"

cat = Cat("Whiskers", 3)
print(cat.info())      # Inherited from Animal
print(cat.speak())     # Overridden in Cat
print(cat.purr())      # Specific to Cat

# ============================================================================
# THE __init__() METHOD IN CHILD CLASSES
# ============================================================================

print("\n" + "="*60)
print("CHILD CLASS __init__() METHOD")
print("="*60)

# WHAT: Child class can have its own __init__()
# WHY: Add additional properties specific to child

class Bird(Animal):
    def __init__(self, name, age, wingspan):
        # Call parent __init__() to initialize inherited attributes
        Animal.__init__(self, name, age)
        # Add new attribute specific to Bird
        self.wingspan = wingspan

    def fly(self):
        return f"{self.name} is flying with {self.wingspan}cm wingspan"

bird = Bird("Eagle", 7, 200)
print(bird.info())     # Inherited
print(bird.fly())      # Specific to Bird

# ============================================================================
# USING super() FUNCTION
# ============================================================================

print("\n" + "="*60)
print("USING super() FUNCTION")
print("="*60)

# WHAT: super() references parent class without naming it
# WHY: More flexible, works with multiple inheritance

class Fish(Animal):
    def __init__(self, name, age, water_type):
        super().__init__(name, age)  # Call parent __init__()
        self.water_type = water_type

    def swim(self):
        return f"{self.name} swims in {self.water_type} water"

fish = Fish("Nemo", 2, "salt")
print(fish.info())
print(fish.swim())

# ============================================================================
# ADDING PROPERTIES TO CHILD CLASS
# ============================================================================

print("\n" + "="*60)
print("CHILD CLASS WITH ADDITIONAL PROPERTIES")
print("="*60)

class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

class GraduateStudent(Student):
    def __init__(self, first_name, last_name, graduation_year):
        super().__init__(first_name, last_name)
        self.graduation_year = graduation_year

    def info(self):
        return f"{self.full_name()} graduates in {self.graduation_year}"

grad = GraduateStudent("Alice", "Smith", 2024)
print(grad.full_name())  # Inherited
print(grad.info())       # New method

# ============================================================================
# METHOD OVERRIDING
# ============================================================================

print("\n" + "="*60)
print("METHOD OVERRIDING")
print("="*60)

# WHAT: Child class replaces parent method with own version
# WHY: Customize behavior for specific child class

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        return f"{self.brand} {self.model} is starting"

class ElectricCar(Vehicle):
    def start(self):
        # Override parent method completely
        return f"{self.brand} {self.model} (Electric) is starting silently"

gas_car = Vehicle("Toyota", "Camry")
electric_car = ElectricCar("Tesla", "Model 3")

print(gas_car.start())
print(electric_car.start())

# ============================================================================
# PART 2: ITERATORS
# ============================================================================

print("\n" + "="*60)
print("ITERATORS - BASICS")
print("="*60)

# WHAT: Object that can be iterated (looped) over
# WHY: Implement custom iteration logic
# HOW: Implement __iter__() and __next__() methods

# Built-in iterables
my_list = [1, 2, 3]
my_iter = iter(my_list)

print("Using iter() and next():")
print(next(my_iter))  # 1
print(next(my_iter))  # 2
print(next(my_iter))  # 3
# print(next(my_iter))  # Would raise StopIteration

# ============================================================================
# STRING ITERATOR
# ============================================================================

print("\n" + "="*60)
print("STRING ITERATOR")
print("="*60)

text = "Python"
text_iter = iter(text)

print("Iterating through string:")
for char in text_iter:
    print(char, end=" ")
print()

# ============================================================================
# CREATING CUSTOM ITERATOR
# ============================================================================

print("\n" + "="*60)
print("CUSTOM ITERATOR CLASS")
print("="*60)

# WHAT: Class that implements __iter__() and __next__()
# WHY: Create custom iteration behavior

class Counter:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        # Return iterator object (self)
        return self

    def __next__(self):
        # Return next value or raise StopIteration
        if self.current <= self.end:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration

# Use custom iterator
counter = Counter(1, 5)
print("Custom counter:")
for num in counter:
    print(num, end=" ")
print()

# ============================================================================
# ITERATOR WITH STOPITERATION
# ============================================================================

print("\n" + "="*60)
print("ITERATOR WITH STOPITERATION")
print("="*60)

class Fibonacci:
    def __init__(self, max_count):
        self.max_count = max_count
        self.count = 0
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.max_count:
            value = self.a
            self.a, self.b = self.b, self.a + self.b
            self.count += 1
            return value
        else:
            raise StopIteration

fib = Fibonacci(10)
print("First 10 Fibonacci numbers:")
for num in fib:
    print(num, end=" ")
print()

# ============================================================================
# PRACTICAL EXAMPLES
# ============================================================================

print("\n" + "="*60)
print("PRACTICAL EXAMPLES")
print("="*60)

# Example 1: Employee hierarchy
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_info(self):
        return f"{self.name}: ${self.salary}/year"

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def get_info(self):
        return f"Manager {self.name}: ${self.salary}/year, Team: {self.team_size}"

emp = Employee("John", 50000)
mgr = Manager("Alice", 80000, 5)

print(emp.get_info())
print(mgr.get_info())

# Example 2: Custom range-like iterator
class CustomRange:
    def __init__(self, start, end, step=1):
        self.start = start
        self.end = end
        self.step = step
        self.current = start

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if self.current < self.end:
            value = self.current
            self.current += self.step
            return value
        else:
            raise StopIteration

print("\nCustom range (0 to 10, step 2):")
for i in CustomRange(0, 10, 2):
    print(i, end=" ")
print()

# Example 3: Shape hierarchy
class Shape:
    def __init__(self, color):
        self.color = color

    def area(self):
        pass

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

class Square(Shape):
    def __init__(self, color, side):
        super().__init__(color)
        self.side = side

    def area(self):
        return self.side ** 2

circle = Circle("red", 5)
square = Square("blue", 4)

print(f"\n{circle.color} circle area: {circle.area():.2f}")
print(f"{square.color} square area: {square.area()}")
