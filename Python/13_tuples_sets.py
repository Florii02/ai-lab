# ============================================================================
# 13. TUPLES AND SETS - COMPREHENSIVE REFERENCE
# ============================================================================
# WHAT: Tuples (immutable sequences) and Sets (unordered unique collections)
# WHY: Tuples for fixed data, Sets for uniqueness and fast lookups
# WHEN: Tuples for coordinates/records, Sets for deduplication/membership

# ============================================================================
# TUPLES - IMMUTABLE SEQUENCES
# ============================================================================

print("="*60)
print("TUPLES - IMMUTABLE SEQUENCES")
print("="*60)

# Creating tuples - use parentheses
fruits = ("apple", "banana", "cherry")
print(f"Tuple: {fruits}")
print(f"Type: {type(fruits)}")

# Single item tuple - MUST have trailing comma
single = ("apple",)  # Tuple
not_tuple = ("apple")  # String!
print(f"\nSingle item tuple: {single}, Type: {type(single)}")
print(f"Without comma: {not_tuple}, Type: {type(not_tuple)}")

# ============================================================================
# ACCESSING TUPLE ITEMS
# ============================================================================

print("\n" + "="*60)
print("ACCESSING TUPLE ITEMS")
print("="*60)

colors = ("red", "green", "blue", "yellow", "purple")

# Positive indexing
print(f"First item [0]: {colors[0]}")
print(f"Third item [2]: {colors[2]}")

# Negative indexing (from end)
print(f"\nLast item [-1]: {colors[-1]}")
print(f"Second to last [-2]: {colors[-2]}")

# Slicing
print(f"\nItems [1:3]: {colors[1:3]}")
print(f"Items [:3]: {colors[:3]}")
print(f"Items [2:]: {colors[2:]}")
print(f"Last 2 items [-2:]: {colors[-2:]}")

# ============================================================================
# WHY TUPLES ARE IMMUTABLE
# ============================================================================

print("\n" + "="*60)
print("IMMUTABILITY - CANNOT MODIFY")
print("="*60)

point = (10, 20)
print(f"Point: {point}")

# Cannot modify tuple items
# point[0] = 99  # Would raise TypeError

# Workaround: Convert to list, modify, convert back
temp_list = list(point)
temp_list[0] = 99
point = tuple(temp_list)
print(f"After workaround: {point}")

# ============================================================================
# TUPLE OPERATIONS
# ============================================================================

print("\n" + "="*60)
print("TUPLE OPERATIONS")
print("="*60)

# Length
coords = (100, 200, 300)
print(f"Length of {coords}: {len(coords)}")

# Concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined = tuple1 + tuple2
print(f"\n{tuple1} + {tuple2} = {combined}")

# Repetition
print(f"(1, 2) * 3 = {(1, 2) * 3}")

# Membership
print(f"\n200 in {coords}: {200 in coords}")
print(f"500 in {coords}: {500 in coords}")

# ============================================================================
# TUPLE METHODS
# ============================================================================

print("\n" + "="*60)
print("TUPLE METHODS")
print("="*60)

numbers = (1, 2, 3, 2, 4, 2, 5)
print(f"Tuple: {numbers}")

# .count() - Count occurrences
print(f"\nCount of 2: {numbers.count(2)}")
print(f"Count of 7: {numbers.count(7)}")

# .index() - Find first index
print(f"\nIndex of 3: {numbers.index(3)}")
print(f"Index of first 2: {numbers.index(2)}")

# ============================================================================
# LOOPING THROUGH TUPLES
# ============================================================================

print("\n" + "="*60)
print("LOOPING THROUGH TUPLES")
print("="*60)

days = ("Mon", "Tue", "Wed", "Thu", "Fri")

print("Days of work week:")
for day in days:
    print(f"  {day}")

# With index
print("\nWith index:")
for i, day in enumerate(days):
    print(f"  Day {i+1}: {day}")

# ============================================================================
# TUPLE UNPACKING
# ============================================================================

print("\n" + "="*60)
print("TUPLE UNPACKING")
print("="*60)

# Assign tuple items to multiple variables
person = ("Alice", 30, "Berlin")
name, age, city = person
print(f"Name: {name}, Age: {age}, City: {city}")

# Swap variables using tuple unpacking
x, y = 10, 20
print(f"\nBefore swap: x={x}, y={y}")
x, y = y, x
print(f"After swap: x={x}, y={y}")

# Function returning multiple values (returns tuple)
def get_coordinates():
    return 100, 200, 300  # Returns tuple

x, y, z = get_coordinates()
print(f"\nCoordinates: x={x}, y={y}, z={z}")

# ============================================================================
# TUPLE() CONSTRUCTOR
# ============================================================================

print("\n" + "="*60)
print("TUPLE() CONSTRUCTOR")
print("="*60)

# Create tuple from other iterables
from_list = tuple([1, 2, 3])
from_string = tuple("hello")
from_range = tuple(range(5))

print(f"From list: {from_list}")
print(f"From string: {from_string}")
print(f"From range: {from_range}")

# ============================================================================
# WHEN TO USE TUPLES
# ============================================================================

print("\n" + "="*60)
print("WHEN TO USE TUPLES")
print("="*60)

print("""
# Use tuples when:
1. Data should not change (coordinates, RGB colors, database records)
2. Need hashable type (can use as dict keys)
3. Want to ensure data integrity
4. Slightly faster than lists
5. Returning multiple values from functions
""")

# Example: RGB colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
print(f"Colors: RED={RED}, GREEN={GREEN}, BLUE={BLUE}")

# ============================================================================
# ============================================================================
# SETS - UNORDERED UNIQUE COLLECTIONS
# ============================================================================
# ============================================================================

print("\n" + "="*60)
print("SETS - UNORDERED UNIQUE COLLECTIONS")
print("="*60)

# Creating sets - use curly braces (but not empty {})
fruits = {"apple", "banana", "cherry"}
print(f"Set: {fruits}")
print(f"Type: {type(fruits)}")

# Duplicates are automatically removed
numbers = {1, 2, 3, 3, 4, 5, 5}
print(f"\nWith duplicates {[1,2,3,3,4,5,5]}: {numbers}")

# Create empty set - must use set()
empty = set()  # NOT {} which creates empty dict
print(f"\nEmpty set: {empty}, Type: {type(empty)}")

# ============================================================================
# SET OPERATIONS
# ============================================================================

print("\n" + "="*60)
print("SET OPERATIONS")
print("="*60)

colors = {"red", "green", "blue"}

# Add item
colors.add("yellow")
print(f"After add: {colors}")

# Add multiple items
colors.update(["orange", "purple"])
print(f"After update: {colors}")

# Remove item (raises error if not found)
colors.remove("orange")
print(f"After remove: {colors}")

# Discard item (no error if not found)
colors.discard("purple")
colors.discard("pink")  # No error even though not in set
print(f"After discard: {colors}")

# Pop random item
colors_copy = colors.copy()
popped = colors_copy.pop()
print(f"\nPopped: {popped}, Remaining: {colors_copy}")

# Clear all items
colors_copy.clear()
print(f"After clear: {colors_copy}")

# ============================================================================
# SET MEMBERSHIP AND LENGTH
# ============================================================================

print("\n" + "="*60)
print("SET MEMBERSHIP AND LENGTH")
print("="*60)

inventory = {"apple", "banana", "cherry"}

print(f"'apple' in inventory: {'apple' in inventory}")
print(f"'grape' in inventory: {'grape' in inventory}")
print(f"Length: {len(inventory)}")

# ============================================================================
# MATHEMATICAL SET OPERATIONS
# ============================================================================

print("\n" + "="*60)
print("MATHEMATICAL SET OPERATIONS")
print("="*60)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(f"Set 1: {set1}")
print(f"Set 2: {set2}")

# Union - All items from both sets
print(f"\nUnion (set1 | set2): {set1 | set2}")
print(f"Union (set1.union(set2)): {set1.union(set2)}")

# Intersection - Items in both sets
print(f"\nIntersection (set1 & set2): {set1 & set2}")
print(f"Intersection (set1.intersection(set2)): {set1.intersection(set2)}")

# Difference - Items in first set but not second
print(f"\nDifference (set1 - set2): {set1 - set2}")
print(f"Difference (set1.difference(set2)): {set1.difference(set2)}")

# Symmetric Difference - Items in either set but not both
print(f"\nSymmetric Diff (set1 ^ set2): {set1 ^ set2}")
print(f"Symmetric Diff (set1.symmetric_difference(set2)): {set1.symmetric_difference(set2)}")

# ============================================================================
# SET COMPARISONS
# ============================================================================

print("\n" + "="*60)
print("SET COMPARISONS")
print("="*60)

a = {1, 2, 3}
b = {1, 2, 3, 4, 5}
c = {1, 2}

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

# Subset - All items of one set are in another
print(f"\na.issubset(b): {a.issubset(b)}")      # True
print(f"c.issubset(a): {c.issubset(a)}")        # True

# Superset - Contains all items of another set
print(f"\nb.issuperset(a): {b.issuperset(a)}")  # True
print(f"a.issuperset(c): {a.issuperset(c)}")    # True

# Disjoint - No common elements
print(f"\na.isdisjoint({10,20}): {a.isdisjoint({10, 20})}")  # True
print(f"a.isdisjoint(b): {a.isdisjoint(b)}")                 # False

# ============================================================================
# FROZENSET - IMMUTABLE SET
# ============================================================================

print("\n" + "="*60)
print("FROZENSET - IMMUTABLE SET")
print("="*60)

# WHY: Can use as dict key, hashable, guaranteed not to change
frozen = frozenset([1, 2, 3])
print(f"Frozenset: {frozen}")
print(f"Type: {type(frozen)}")

# Cannot add or remove items
# frozen.add(4)  # Would raise AttributeError

# ============================================================================
# PRACTICAL EXAMPLES
# ============================================================================

print("\n" + "="*60)
print("PRACTICAL EXAMPLES")
print("="*60)

# Remove duplicates from list
numbers_list = [1, 2, 2, 3, 4, 4, 5, 1]
unique_numbers = list(set(numbers_list))
print(f"Remove duplicates: {numbers_list} -> {unique_numbers}")

# Find common items in lists
list1 = ["apple", "banana", "cherry"]
list2 = ["banana", "cherry", "date"]
common = set(list1) & set(list2)
print(f"\nCommon items: {common}")

# Check if lists have no common items
list3 = ["x", "y", "z"]
have_common = not set(list1).isdisjoint(list3)
print(f"\nlist1 and list3 have common items: {have_common}")

# Fast membership testing
large_set = set(range(1000000))
print(f"\n999999 in large set: {999999 in large_set}")  # Very fast!
