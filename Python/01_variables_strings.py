# 1. Variables & Strings + Data Types + String Methods

# ============================================================================
# VARIABLE NAMING RULES IN PYTHON
# ============================================================================
# - Must start with a letter or underscore (_)
# - Cannot start with a number
# - Case sensitive (myVar and myvar are different)
# - Can contain letters, numbers, and underscores
# - Cannot use Python keywords (if, else, for, etc.)

# ============================================================================
# BASIC VARIABLE ASSIGNMENT
# ============================================================================
a = 5                                    # Integer
b = "Hello World"                        # String
c = 3.14                                 # Float
x, y, z = "Orange", "Banana", "Cherry"   # Multiple assignment in one line

n = 1j                                   # Complex number (real + imaginary)
print(type(n))                           # Output: <class 'complex'>

# ============================================================================
# STRING CREATION
# ============================================================================
# Strings can be created using single quotes, double quotes, or triple quotes

a = "Hello World"           # Double quotes
b = 'Good Morning'          # Single quotes (functionally identical)

# Triple quotes allow multi-line strings (preserves line breaks)
c = """This is a multi-line string
that spans multiple lines."""

# ============================================================================
# STRING INDEXING & SLICING
# ============================================================================
# Strings are arrays of characters - you can access individual characters
# Python uses 0-based indexing (first character is at position 0)

text = "Hello, World!"
print(text[0])          # 'H' - First character (index 0)
print(text[7])          # 'W' - Character at index 7
print(text[-1])         # '!' - Last character (negative indexing from end)
print(text[-2])         # 'd' - Second from last

# Slicing: Extract substring using [start:end] (end is NOT included)
print(text[0:5])        # "Hello" - Characters from index 0 to 4
print(text[7:12])       # "World" - Characters from index 7 to 11
print(text[2:5])        # "llo" - Slice from index 2 to 4

# Negative slicing (count from end)
print(text[-5:-2])      # "orl" - From 5th-last to 3rd-last character

# ============================================================================
# STRING LENGTH
# ============================================================================
print(len(text))        # 13 - Returns number of characters in string

# ============================================================================
# STRING ITERATION
# ============================================================================
# You can loop through characters in a string
for char in b:
    print(char, end=' ')  # Prints each character separated by space
print()                   # New line after loop

# ============================================================================
# STRING CONCATENATION
# ============================================================================
# Combine strings using the + operator
greeting = "Hello"
name = "Alice"
message = greeting + " " + name  # "Hello Alice"
print(message)

# NOTE: You CANNOT concatenate strings and numbers directly
# age = 25
# print("I am " + age)  # TypeError! Must convert number to string first
# print("I am " + str(age))  # Correct way using str()

# ============================================================================
# CHECKING STRING MEMBERSHIP
# ============================================================================
# Use 'in' and 'not in' to check if substring exists
txt = "The rain in Spain"
print("rain" in txt)      # True - "rain" is present
print("sun" not in txt)   # True - "sun" is NOT present

# ============================================================================
# ESSENTIAL STRING METHODS
# ============================================================================
# All string methods return NEW strings - they don't modify the original

sample = "  Hello, World!  "

# Changing case
print(sample.lower())          # "  hello, world!  " - All lowercase
print(sample.upper())          # "  HELLO, WORLD!  " - All uppercase
print(sample.capitalize())     # "  hello, world!  " - First char uppercase
print(sample.title())          # "  Hello, World!  " - Each word capitalized
print(sample.swapcase())       # "  hELLO, wORLD!  " - Swap upper/lower

# Removing whitespace
print(sample.strip())          # "Hello, World!" - Remove leading/trailing spaces
print(sample.lstrip())         # "Hello, World!  " - Remove left spaces only
print(sample.rstrip())         # "  Hello, World!" - Remove right spaces only

# Replacing substrings
print(sample.replace("Hello", "Hi"))      # "  Hi, World!  "
print(sample.replace("World", "Python"))  # "  Hello, Python!  "

# Splitting and joining
sentence = "apple,banana,cherry"
fruits = sentence.split(",")   # ['apple', 'banana', 'cherry'] - Returns list
print(fruits)
print(type(fruits))            # <class 'list'>

joined = "-".join(fruits)      # "apple-banana-cherry" - Join list into string
print(joined)

# Finding substrings
print(sample.find("World"))    # 9 - Index where "World" starts (-1 if not found)
print(sample.index("World"))   # 9 - Same as find(), but raises error if not found
print(sample.count("o"))       # 2 - Count occurrences of "o"

# Checking string content
print("hello".startswith("he"))   # True - String starts with "he"
print("hello".endswith("lo"))     # True - String ends with "lo"
print("hello123".isalnum())       # True - All chars are alphanumeric
print("hello".isalpha())          # True - All chars are alphabetic
print("123".isdigit())            # True - All chars are digits
print("123".isnumeric())          # True - All chars are numeric
print("hello".islower())          # True - All chars are lowercase
print("HELLO".isupper())          # True - All chars are uppercase
print("   ".isspace())            # True - All chars are whitespace
print("Hello World".istitle())    # True - String follows title case rules

# Alignment methods
print("test".center(10))       # "   test   " - Center in 10-char string
print("test".ljust(10))        # "test      " - Left justify
print("test".rjust(10))        # "      test" - Right justify
print("42".zfill(5))           # "00042" - Pad with zeros to width 5

# Partitioning
print("Hello-World".partition("-"))  # ('Hello', '-', 'World') - Split at first occurrence
print("Hello-World".rpartition("-")) # ('Hello', '-', 'World') - Split at last occurrence

# ============================================================================
# STRING FORMATTING WITH .format()
# ============================================================================
# Modern way to insert variables into strings (better than concatenation)

# Basic placeholder usage
age = 25
name = "Alice"
message = "My name is {} and I am {} years old".format(name, age)
print(message)  # "My name is Alice and I am 25 years old"

# Using index numbers {0}, {1} to specify order
txt = "I want {0} pieces of item {1} for {2} dollars".format(3, 567, 49.95)
print(txt)  # "I want 3 pieces of item 567 for 49.95 dollars"

# Reusing values with index numbers
person = "His name is {1}. {1} is {0} years old.".format(36, "John")
print(person)  # "His name is John. John is 36 years old."

# Using named placeholders (more readable)
order = "I have a {car}, it is a {model}.".format(car="Ford", model="Mustang")
print(order)  # "I have a Ford, it is a Mustang."

# Format specifications (control number formatting)
price = 49.12345
print("The price is {:.2f} dollars".format(price))  # "The price is 49.12 dollars" (2 decimals)
print("The price is {:10.2f}".format(price))        # "     49.12" (width 10, 2 decimals)

# ============================================================================
# F-STRINGS (Python 3.6+) - MODERN & RECOMMENDED
# ============================================================================
# F-strings provide a cleaner, faster way to format strings
name = "Bob"
age = 30
print(f"My name is {name} and I am {age} years old")  # Direct variable insertion
print(f"Next year I'll be {age + 1}")                 # Can include expressions

# ============================================================================
# COMPREHENSIVE STRING METHOD REFERENCE
# ============================================================================
x = "this Is A String"

# All methods demonstrated (uncomment to test individually):
# print(x.capitalize())     # First character uppercase, rest lowercase
# print(x.casefold())       # Aggressive lowercase (better for comparisons)
# print(x.center(20))       # Center string in field of width 20
# print(x.count("i"))       # Count occurrences of substring
# print(x.encode())         # Encode to bytes using UTF-8
# print(x.expandtabs(20))   # Set tab size
# print(x.partition("A"))   # Split into 3-part tuple at first occurrence
# print(x.split("A"))       # Split into list at separator
# print(x.splitlines())     # Split at line breaks
