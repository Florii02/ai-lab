# ============================================================================
# 2. LISTS & LOOPS - COMPREHENSIVE REFERENCE
# ============================================================================
# WHAT: Lists are ordered, mutable (changeable) collections that allow duplicates
# WHY: Perfect for storing sequences of data that need to be modified
# WHEN: Use for dynamic collections, processing sequences, managing ordered data

# ============================================================================
# BASIC LIST CREATION AND ACCESS
# ============================================================================

# Creating a list - use square brackets
fruits = ["apple", "banana", "cherry"]
print("Basic list:", fruits)
print("Type:", type(fruits))

# Accessing items by index (zero-based)
print("\nFirst item:", fruits[0])      # apple
print("Second item:", fruits[1])       # banana

# Negative indexing - count from the end
# WHY: Convenient way to access items from the end without knowing list length
print("Last item:", fruits[-1])        # cherry
print("Second to last:", fruits[-2])   # banana

# ============================================================================
# LIST SLICING
# ============================================================================
# WHAT: Extract a portion of a list using [start:end] syntax
# WHY: Efficiently work with subsets of data without loops
# NOTE: End index is NOT included in the result

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("\nOriginal list:", numbers)
print("Items [2:5]:", numbers[2:5])      # [2, 3, 4] - items at index 2, 3, 4
print("Items [:4]:", numbers[:4])        # [0, 1, 2, 3] - from start to index 3
print("Items [5:]:", numbers[5:])        # [5, 6, 7, 8, 9] - from index 5 to end
print("Items [-3:]:", numbers[-3:])      # [7, 8, 9] - last 3 items

# ============================================================================
# LIST METHODS - ADDING ITEMS
# ============================================================================

# .append() - Add single item to end
# WHY: Most common way to build lists dynamically
my_list = ["a", "b", "c"]
my_list.append("d")
print("\nAfter append:", my_list)       # ["a", "b", "c", "d"]

# .insert() - Add item at specific position
# WHY: Insert data at exact location without replacing existing items
my_list.insert(1, "inserted")
print("After insert at index 1:", my_list)  # ["a", "inserted", "b", "c", "d"]

# .extend() - Add multiple items from another iterable
# WHY: Merge lists or add multiple items efficiently
my_list.extend(["e", "f"])
print("After extend:", my_list)

# ============================================================================
# LIST METHODS - REMOVING ITEMS
# ============================================================================

sample = ["apple", "banana", "cherry", "banana"]

# .remove() - Remove first occurrence of specific value
# WHY: Remove item when you know the value but not the index
sample_copy = sample.copy()
sample_copy.remove("banana")
print("\nAfter remove('banana'):", sample_copy)  # Removes first "banana"

# .pop() - Remove and return item at index (or last item if no index given)
# WHY: Remove item AND use its value in one operation
sample_copy = sample.copy()
removed_item = sample_copy.pop()
print("Popped item:", removed_item)
print("After pop():", sample_copy)

sample_copy = sample.copy()
removed_item = sample_copy.pop(1)
print("Popped item at index 1:", removed_item)
print("After pop(1):", sample_copy)

# .clear() - Remove all items
# WHY: Empty list while keeping the variable reference
sample_copy = sample.copy()
sample_copy.clear()
print("After clear():", sample_copy)        # []

# ============================================================================
# LIST METHODS - ORGANIZING & SEARCHING
# ============================================================================

numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print("\nOriginal numbers:", numbers)

# .sort() - Sort list in place (modifies original)
# WHY: Organize data for easier processing or display
numbers_copy = numbers.copy()
numbers_copy.sort()
print("After sort():", numbers_copy)

numbers_copy.sort(reverse=True)
print("After sort(reverse=True):", numbers_copy)

# .reverse() - Reverse list order in place
# WHY: Reverse sequence without sorting
numbers_copy = numbers.copy()
numbers_copy.reverse()
print("After reverse():", numbers_copy)

# .count() - Count occurrences of a value
# WHY: Find how many times an item appears
print("Count of 1:", numbers.count(1))      # 2

# .index() - Find first index of a value
# WHY: Locate position of specific item
print("Index of 5:", numbers.index(5))      # 4

# ============================================================================
# LIST METHODS - COPYING
# ============================================================================

# .copy() - Create shallow copy
# WHY: Modify copy without affecting original
original = ["apple", "banana", "cherry"]
copied = original.copy()
copied.append("date")
print("\nOriginal:", original)
print("Copied:", copied)

# Alternative: use list() constructor
another_copy = list(original)
print("Copy via list():", another_copy)

# ============================================================================
# CHECKING MEMBERSHIP
# ============================================================================

fruits = ["apple", "banana", "cherry"]
print("\n'apple' in fruits:", "apple" in fruits)      # True
print("'orange' in fruits:", "orange" in fruits)      # False

# ============================================================================
# FOR LOOPS - ITERATING OVER SEQUENCES
# ============================================================================
# WHAT: Execute code for each item in a sequence
# WHY: Process every element without manual index management

print("\n" + "="*50)
print("FOR LOOPS")
print("="*50)

# Basic for loop
for fruit in fruits:
    print(f"I like {fruit}")

# Looping through string (strings are iterable)
for char in "Python":
    print(char, end=" ")
print()

# ============================================================================
# RANGE() FUNCTION
# ============================================================================
# WHAT: Generate sequence of numbers
# WHY: Create numeric loops without manually creating lists
# SYNTAX: range(start, stop, step)

print("\nrange(5):", end=" ")
for i in range(5):
    print(i, end=" ")       # 0 1 2 3 4
print()

print("range(2, 6):", end=" ")
for i in range(2, 6):
    print(i, end=" ")       # 2 3 4 5
print()

print("range(0, 10, 2):", end=" ")
for i in range(0, 10, 2):
    print(i, end=" ")       # 0 2 4 6 8
print()

# ============================================================================
# LOOP CONTROL - BREAK
# ============================================================================
# WHAT: Exit loop immediately
# WHY: Stop processing when condition is met

print("\nLoop with break:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    if fruit == "banana":
        break               # Exit loop when banana is found
    print(fruit)            # Only prints "apple"

# ============================================================================
# LOOP CONTROL - CONTINUE
# ============================================================================
# WHAT: Skip rest of current iteration, move to next
# WHY: Skip processing for specific items

print("\nLoop with continue:")
for fruit in fruits:
    if fruit == "banana":
        continue            # Skip banana, continue with next item
    print(fruit)            # Prints "apple" and "cherry"

# ============================================================================
# LOOP CONTROL - ELSE CLAUSE
# ============================================================================
# WHAT: Execute code when loop completes normally (not via break)
# WHY: Distinguish between completed and interrupted loops

print("\nLoop with else (no break):")
for x in range(3):
    print(x)
else:
    print("Loop completed normally!")

print("\nLoop with else (with break):")
for x in range(5):
    if x == 2:
        break
    print(x)
else:
    print("This won't print because loop was broken")

# ============================================================================
# NESTED LOOPS
# ============================================================================
# WHAT: Loop inside another loop
# WHY: Work with multi-dimensional data or create combinations

print("\nNested loops:")
adjectives = ["red", "big"]
fruits = ["apple", "banana"]

for adj in adjectives:
    for fruit in fruits:
        print(f"{adj} {fruit}")

# ============================================================================
# WHILE LOOPS
# ============================================================================
# WHAT: Repeat while condition is true
# WHY: Loop when you don't know how many iterations needed

print("\n" + "="*50)
print("WHILE LOOPS")
print("="*50)

count = 0
while count < 3:
    print(f"Count is {count}")
    count += 1

# While with break
print("\nWhile with break:")
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# While with continue
print("\nWhile with continue:")
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue            # Skip printing 3
    print(i)

# While with else
print("\nWhile with else:")
i = 1
while i < 4:
    print(i)
    i += 1
else:
    print("While loop completed!")

# ============================================================================
# PRACTICAL EXAMPLES
# ============================================================================

print("\n" + "="*50)
print("PRACTICAL EXAMPLES")
print("="*50)

# Build a list dynamically
squares = []
for i in range(1, 6):
    squares.append(i ** 2)
print("Squares:", squares)

# Filter items from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = []
for num in numbers:
    if num % 2 == 0:
        evens.append(num)
print("Even numbers:", evens)

# Find item in list
shopping = ["milk", "eggs", "bread"]
search = "eggs"
found = False
for item in shopping:
    if item == search:
        found = True
        break
if found:
    print(f"{search} is in shopping list")
