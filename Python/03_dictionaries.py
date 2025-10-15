# ============================================================================
# 3. DICTIONARIES - COMPREHENSIVE REFERENCE
# ============================================================================
# WHAT: Unordered collection of key-value pairs (ordered in Python 3.7+)
# WHY: Fast lookup, store related data together, represent structured objects
# WHEN: Need to map keys to values, store configuration, work with JSON-like data

# ============================================================================
# BASIC DICTIONARY CREATION AND ACCESS
# ============================================================================

# Creating a dictionary - use curly braces with key:value pairs
person = {"name": "Alice", "age": 30, "city": "Berlin"}
print("Dictionary:", person)
print("Type:", type(person))

# Accessing values by key - use square brackets
print("\nAccessing with []:")
print("Name:", person["name"])
print("Age:", person["age"])

# .get() method - safer way to access (returns None if key doesn't exist)
# WHY: Prevents KeyError when key might not exist
print("\nAccessing with .get():")
print("City:", person.get("city"))
print("Country:", person.get("country"))              # Returns None
print("Country:", person.get("country", "Unknown"))   # Returns default value

# ============================================================================
# ADDING AND MODIFYING ITEMS
# ============================================================================

# Add new key-value pair
person["job"] = "Engineer"
print("\nAfter adding job:", person)

# Modify existing value
person["age"] = 31
print("After updating age:", person)

# .update() - Update with multiple key-value pairs
# WHY: Update multiple items at once or merge dictionaries
person.update({"salary": 75000, "department": "IT"})
print("After update():", person)

# ============================================================================
# DICTIONARY METHODS - REMOVING ITEMS
# ============================================================================

car = {"brand": "Ford", "model": "Mustang", "year": 1964, "color": "red"}
print("\nOriginal car dict:", car)

# .pop() - Remove and return value for specific key
# WHY: Remove item and use its value in one operation
removed_color = car.pop("color")
print(f"Popped color: {removed_color}")
print("After pop('color'):", car)

# .popitem() - Remove and return last inserted key-value pair
# WHY: Remove most recent addition (useful for LIFO operations)
car_copy = {"brand": "Ford", "model": "Mustang", "year": 1964, "color": "red"}
last_item = car_copy.popitem()
print(f"\nPopped last item: {last_item}")
print("After popitem():", car_copy)

# .clear() - Remove all items
# WHY: Empty dictionary while keeping variable reference
car_copy = {"brand": "Ford", "model": "Mustang"}
car_copy.clear()
print("After clear():", car_copy)              # {}

# ============================================================================
# DICTIONARY METHODS - ACCESSING KEYS, VALUES, ITEMS
# ============================================================================

product = {"name": "Laptop", "price": 999, "stock": 15}

# .keys() - Get all keys
# WHY: Iterate over or check available keys
print("\nKeys:", product.keys())
print("Keys as list:", list(product.keys()))

# .values() - Get all values
# WHY: Work with values without needing keys
print("Values:", product.values())
print("Values as list:", list(product.values()))

# .items() - Get all key-value pairs as tuples
# WHY: Iterate over both keys and values simultaneously
print("Items:", product.items())
print("Items as list:", list(product.items()))

# ============================================================================
# LOOPING THROUGH DICTIONARIES
# ============================================================================

student = {"name": "Bob", "age": 22, "major": "Computer Science"}

# Loop through keys (default behavior)
print("\nLooping through keys:")
for key in student:
    print(f"{key}: {student[key]}")

# Loop through keys explicitly
print("\nUsing .keys():")
for key in student.keys():
    print(key)

# Loop through values
print("\nUsing .values():")
for value in student.values():
    print(value)

# Loop through key-value pairs (most common)
# WHY: Access both key and value directly
print("\nUsing .items():")
for key, value in student.items():
    print(f"{key} = {value}")

# ============================================================================
# DICTIONARY COPYING
# ============================================================================

# .copy() - Create shallow copy
# WHY: Modify copy without affecting original
original = {"a": 1, "b": 2, "c": 3}
copied = original.copy()
copied["d"] = 4
print("\nOriginal:", original)
print("Copied:", copied)

# Alternative: use dict() constructor
another_copy = dict(original)
print("Copy via dict():", another_copy)

# ============================================================================
# NESTED DICTIONARIES
# ============================================================================
# WHAT: Dictionaries containing other dictionaries
# WHY: Represent hierarchical or complex data structures

# Method 1: Create nested dict directly
family = {
    "child1": {
        "name": "Emma",
        "age": 10
    },
    "child2": {
        "name": "Liam",
        "age": 8
    }
}
print("\nNested dictionary:", family)
print("Child1 name:", family["child1"]["name"])

# Method 2: Combine existing dictionaries
person1 = {"name": "Alice", "age": 30}
person2 = {"name": "Bob", "age": 25}
team = {
    "member1": person1,
    "member2": person2
}
print("\nTeam dict:", team)
print("Member2 age:", team["member2"]["age"])

# ============================================================================
# DICT() CONSTRUCTOR
# ============================================================================
# WHAT: Create dictionary using constructor
# WHY: Alternative syntax, useful for simple string keys

# Note: Keys are not string literals, no quotes needed
config = dict(host="localhost", port=8080, debug=True)
print("\nDict via constructor:", config)

# ============================================================================
# CHECKING MEMBERSHIP
# ============================================================================

inventory = {"apples": 50, "bananas": 30, "oranges": 25}
print("\n'apples' in inventory:", "apples" in inventory)      # True
print("'grapes' in inventory:", "grapes" in inventory)        # False

# Check if key NOT in dict
if "grapes" not in inventory:
    print("Need to order grapes!")

# ============================================================================
# DICTIONARY LENGTH
# ============================================================================

print("\nNumber of items:", len(inventory))

# ============================================================================
# OTHER USEFUL METHODS
# ============================================================================

# .setdefault() - Get value or set default if key doesn't exist
# WHY: Safely initialize values without checking if key exists
settings = {"theme": "dark"}
theme = settings.setdefault("theme", "light")      # Returns "dark"
lang = settings.setdefault("language", "en")       # Sets and returns "en"
print("\nSettings after setdefault:", settings)

# .fromkeys() - Create dict from sequence of keys with same value
# WHY: Initialize multiple keys with default value
keys = ["a", "b", "c"]
new_dict = dict.fromkeys(keys, 0)
print("Dict from keys:", new_dict)

# ============================================================================
# PRACTICAL EXAMPLES
# ============================================================================

print("\n" + "="*50)
print("PRACTICAL EXAMPLES")
print("="*50)

# Count occurrences of items
fruits = ["apple", "banana", "apple", "cherry", "banana", "apple"]
fruit_count = {}
for fruit in fruits:
    fruit_count[fruit] = fruit_count.get(fruit, 0) + 1
print("\nFruit count:", fruit_count)

# Store user data
users = {
    "user001": {"name": "Alice", "email": "alice@example.com"},
    "user002": {"name": "Bob", "email": "bob@example.com"}
}
print("\nUsers database:", users)

# Configuration settings
app_config = {
    "database": {
        "host": "localhost",
        "port": 5432,
        "name": "myapp_db"
    },
    "cache": {
        "enabled": True,
        "ttl": 3600
    }
}
print("\nApp config:", app_config)
print("Database host:", app_config["database"]["host"])
