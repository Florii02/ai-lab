# ============================================================================
# 12. PYTHON DATA TYPES - COMPREHENSIVE REFERENCE
# ============================================================================
# WHAT: Classification of data determining what operations can be performed
# WHY: Choose right data type for efficiency, accuracy, and functionality
# WHEN: Every variable has a type - understanding types is fundamental

print("="*60)
print("PYTHON DATA TYPES OVERVIEW")
print("="*60)

# ============================================================================
# DATA TYPE CATEGORIES
# ============================================================================
# Text Type:      str
# Numeric Types:  int, float, complex
# Sequence Types: list, tuple, range
# Mapping Type:   dict
# Set Types:      set, frozenset
# Boolean Type:   bool
# Binary Types:   bytes, bytearray, memoryview

# ============================================================================
# NUMERIC TYPES
# ============================================================================

print("\n" + "="*60)
print("NUMERIC TYPES")
print("="*60)

# INT - Integers (whole numbers)
# WHAT: Whole numbers, positive or negative, unlimited length
# WHY: Counting, indexing, exact calculations
x = 42
y = -100
z = 9999999999999999999999
print(f"Integer examples: {x}, {y}, {z}")
print(f"Type: {type(x)}")

# FLOAT - Floating point numbers
# WHAT: Numbers with decimal points
# WHY: Measurements, scientific calculations, percentages
a = 3.14
b = -0.001
c = 2.5e2  # Scientific notation: 2.5 * 10^2 = 250.0
print(f"\nFloat examples: {a}, {b}, {c}")
print(f"Type: {type(a)}")

# COMPLEX - Complex numbers
# WHAT: Numbers with real and imaginary parts (j = sqrt(-1))
# WHY: Scientific computing, signal processing, engineering
comp = 3 + 5j
print(f"\nComplex example: {comp}")
print(f"Real part: {comp.real}, Imaginary part: {comp.imag}")
print(f"Type: {type(comp)}")

# ============================================================================
# TYPE CONVERSION (CASTING)
# ============================================================================

print("\n" + "="*60)
print("TYPE CONVERSION (CASTING)")
print("="*60)

# int() - Convert to integer
print("int('42'):", int('42'))            # String to int
print("int(3.9):", int(3.9))              # Float to int (truncates)
print("int(True):", int(True))            # Bool to int (True=1, False=0)

# float() - Convert to float
print("\nfloat(42):", float(42))          # Int to float
print("float('3.14'):", float('3.14'))    # String to float
print("float(True):", float(True))        # Bool to float

# str() - Convert to string
print("\nstr(42):", str(42))              # Int to string
print("str(3.14):", str(3.14))            # Float to string
print("str(True):", str(True))            # Bool to string

# complex() - Convert to complex
print("\ncomplex(2, 3):", complex(2, 3))  # Create complex number

# NOTE: Cannot convert complex to other number types

# ============================================================================
# BOOLEAN TYPE
# ============================================================================

print("\n" + "="*60)
print("BOOLEAN TYPE")
print("="*60)

# WHAT: True or False values
# WHY: Logic, conditions, decision making

print("Boolean values: True, False")
print("Type:", type(True))

# Evaluating to Boolean
print("\nEvaluating expressions:")
print("10 > 5:", 10 > 5)                  # True
print("10 == 5:", 10 == 5)                # False

# bool() function - Convert to boolean
print("\nUsing bool():")
print("bool(1):", bool(1))                # True (non-zero)
print("bool(0):", bool(0))                # False (zero)
print("bool('text'):", bool('text'))      # True (non-empty)
print("bool(''):", bool(''))              # False (empty)
print("bool([1,2,3]):", bool([1,2,3]))    # True (non-empty)
print("bool([]):", bool([]))              # False (empty)

# Values that evaluate to False
print("\nFalsy values (evaluate to False):")
falsy_values = [False, None, 0, 0.0, 0j, '', [], (), {}, set()]
for val in falsy_values:
    print(f"  bool({repr(val)}) = {bool(val)}")

# ============================================================================
# STRING TYPE
# ============================================================================

print("\n" + "="*60)
print("STRING TYPE")
print("="*60)

# WHAT: Sequence of characters
# WHY: Text data, user input, display output
text = "Hello, World!"
print(f"String: {text}")
print(f"Type: {type(text)}")

# String methods
print("\nCommon string methods:")
print(f"Upper: {text.upper()}")
print(f"Lower: {text.lower()}")
print(f"Replace: {text.replace('World', 'Python')}")
print(f"Split: {text.split(', ')}")
print(f"Length: {len(text)}")

# ============================================================================
# SEQUENCE TYPES - LIST, TUPLE, RANGE
# ============================================================================

print("\n" + "="*60)
print("SEQUENCE TYPES")
print("="*60)

# LIST - Ordered, mutable (changeable)
# WHY: Dynamic collections, can modify after creation
my_list = [1, 2, 3, "four", 5.0]
print(f"List: {my_list}, Type: {type(my_list)}")
my_list.append(6)
print(f"After append: {my_list}")

# TUPLE - Ordered, immutable (cannot change)
# WHY: Fixed collections, faster than lists, can use as dict keys
my_tuple = (1, 2, 3, "four", 5.0)
print(f"\nTuple: {my_tuple}, Type: {type(my_tuple)}")
# my_tuple[0] = 99  # Would cause error - tuples are immutable

# RANGE - Sequence of numbers
# WHY: Memory efficient for loops, don't store all numbers
my_range = range(5)
print(f"\nRange: {my_range}, Type: {type(my_range)}")
print(f"Range as list: {list(my_range)}")

# ============================================================================
# MAPPING TYPE - DICTIONARY
# ============================================================================

print("\n" + "="*60)
print("MAPPING TYPE - DICTIONARY")
print("="*60)

# DICT - Key-value pairs
# WHY: Fast lookups, store related data, represent objects
person = {"name": "Alice", "age": 30, "city": "Berlin"}
print(f"Dictionary: {person}")
print(f"Type: {type(person)}")
print(f"Access by key: person['name'] = {person['name']}")

# ============================================================================
# SET TYPES
# ============================================================================

print("\n" + "="*60)
print("SET TYPES")
print("="*60)

# SET - Unordered, no duplicates, mutable
# WHY: Remove duplicates, fast membership testing, set operations
my_set = {1, 2, 3, 3, 4, 5}
print(f"Set: {my_set}, Type: {type(my_set)}")  # Duplicates removed
print(f"'3 in my_set': {3 in my_set}")

# FROZENSET - Unordered, no duplicates, immutable
# WHY: Immutable version of set, can use as dict key
my_frozenset = frozenset([1, 2, 3])
print(f"\nFrozenset: {my_frozenset}, Type: {type(my_frozenset)}")

# ============================================================================
# CHECKING DATA TYPES
# ============================================================================

print("\n" + "="*60)
print("CHECKING DATA TYPES")
print("="*60)

# type() - Get type of object
x = 42
print(f"type(42): {type(x)}")

# isinstance() - Check if object is instance of type
print(f"\nisinstance(42, int): {isinstance(42, int)}")
print(f"isinstance(42, (int, float)): {isinstance(42, (int, float))}")
print(f"isinstance('hello', int): {isinstance('hello', int)}")

# ============================================================================
# PRACTICAL EXAMPLES
# ============================================================================

print("\n" + "="*60)
print("PRACTICAL EXAMPLES")
print("="*60)

# Calculate percentage (using float)
score = 85
total = 100
percentage = (score / total) * 100
print(f"Score: {score}/{total} = {percentage}%")

# Remove duplicates from list (using set)
numbers = [1, 2, 2, 3, 4, 4, 5]
unique = list(set(numbers))
print(f"\nOriginal: {numbers}")
print(f"Unique: {unique}")

# Check if value is numeric type
value = 42
if isinstance(value, (int, float, complex)):
    print(f"\n{value} is a numeric type")

# Convert user input to integer
user_input = "25"
age = int(user_input)
print(f"\nConverted '{user_input}' to integer: {age}")
