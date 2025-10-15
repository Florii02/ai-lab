# ============================================================================
# 11. PYTHON OPERATORS - COMPREHENSIVE REFERENCE
# ============================================================================
# WHAT: Symbols that perform operations on variables and values
# WHY: Build expressions, compare values, perform logic, manipulate data
# WHEN: Every program uses operators for calculations and logic

# ============================================================================
# ARITHMETIC OPERATORS
# ============================================================================
# WHAT: Perform mathematical operations
# WHY: Calculate values, process numbers

print("="*60)
print("ARITHMETIC OPERATORS")
print("="*60)

x, y = 10, 3

print(f"x = {x}, y = {y}\n")
print(f"Addition (x + y):        {x + y}")        # 13
print(f"Subtraction (x - y):     {x - y}")        # 7
print(f"Multiplication (x * y):  {x * y}")        # 30
print(f"Division (x / y):        {x / y}")        # 3.333... (always float)
print(f"Floor Division (x // y): {x // y}")       # 3 (rounds down)
print(f"Modulus (x % y):         {x % y}")        # 1 (remainder)
print(f"Exponentiation (x ** y): {x ** y}")       # 1000 (10^3)

# ============================================================================
# ASSIGNMENT OPERATORS
# ============================================================================
# WHAT: Assign values to variables (often combined with arithmetic)
# WHY: Update variables efficiently

print("\n" + "="*60)
print("ASSIGNMENT OPERATORS")
print("="*60)

x = 10
print(f"Initial x = {x}")

x += 5      # Same as: x = x + 5
print(f"After x += 5:  x = {x}")

x -= 3      # Same as: x = x - 3
print(f"After x -= 3:  x = {x}")

x *= 2      # Same as: x = x * 2
print(f"After x *= 2:  x = {x}")

x /= 4      # Same as: x = x / 4
print(f"After x /= 4:  x = {x}")

x //= 2     # Same as: x = x // 2
print(f"After x //= 2: x = {x}")

x %= 2      # Same as: x = x % 2
print(f"After x %= 2:  x = {x}")

x = 5
x **= 2     # Same as: x = x ** 2
print(f"After x **= 2: x = {x}")

# ============================================================================
# COMPARISON OPERATORS
# ============================================================================
# WHAT: Compare two values, return True or False
# WHY: Make decisions, control flow, filtering

print("\n" + "="*60)
print("COMPARISON OPERATORS")
print("="*60)

a, b = 10, 20

print(f"a = {a}, b = {b}\n")
print(f"a == b (equal):              {a == b}")            # False
print(f"a != b (not equal):          {a != b}")            # True
print(f"a > b (greater than):        {a > b}")             # False
print(f"a < b (less than):           {a < b}")             # True
print(f"a >= b (greater or equal):   {a >= b}")            # False
print(f"a <= b (less or equal):      {a <= b}")            # True

# ============================================================================
# LOGICAL OPERATORS
# ============================================================================
# WHAT: Combine conditional statements
# WHY: Complex conditions, multiple criteria

print("\n" + "="*60)
print("LOGICAL OPERATORS")
print("="*60)

x, y = 5, 10

print(f"x = {x}, y = {y}\n")

# AND - Both conditions must be True
print(f"(x < 10 and y > 5):  {x < 10 and y > 5}")        # True (both true)
print(f"(x < 3 and y > 5):   {x < 3 and y > 5}")         # False (first false)

# OR - At least one condition must be True
print(f"(x < 10 or y < 5):   {x < 10 or y < 5}")         # True (first true)
print(f"(x < 3 or y < 5):    {x < 3 or y < 5}")          # False (both false)

# NOT - Reverse the result
print(f"not(x < 10):         {not(x < 10)}")             # False (reverses True)
print(f"not(x > 10):         {not(x > 10)}")             # True (reverses False)

# ============================================================================
# IDENTITY OPERATORS
# ============================================================================
# WHAT: Compare object identity (same object in memory)
# WHY: Check if two variables reference the same object
# NOTE: Different from equality (==) which checks values

print("\n" + "="*60)
print("IDENTITY OPERATORS")
print("="*60)

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x  # z points to same object as x

print(f"x = {x}")
print(f"y = {y}")
print(f"z = {z}\n")

print(f"x == y (same values):      {x == y}")        # True (same values)
print(f"x is y (same object):      {x is y}")        # False (different objects)
print(f"x is z (same object):      {x is z}")        # True (same object)
print(f"x is not y:                {x is not y}")    # True

# ============================================================================
# MEMBERSHIP OPERATORS
# ============================================================================
# WHAT: Test if value is present in a sequence
# WHY: Check if item exists in list, tuple, set, string, dict

print("\n" + "="*60)
print("MEMBERSHIP OPERATORS")
print("="*60)

fruits = ["apple", "banana", "cherry"]
text = "Hello World"

print(f"fruits = {fruits}")
print(f"text = '{text}'\n")

print(f"'apple' in fruits:         {'apple' in fruits}")           # True
print(f"'grape' in fruits:         {'grape' in fruits}")           # False
print(f"'grape' not in fruits:     {'grape' not in fruits}")       # True
print(f"'Hello' in text:           {'Hello' in text}")             # True
print(f"'hello' in text:           {'hello' in text}")             # False (case sensitive)

# ============================================================================
# BITWISE OPERATORS
# ============================================================================
# WHAT: Operate on binary representations of integers
# WHY: Low-level operations, flags, permissions, optimization
# WHEN: Systems programming, embedded systems, performance critical code

print("\n" + "="*60)
print("BITWISE OPERATORS")
print("="*60)

a, b = 5, 3  # Binary: 101, 011

print(f"a = {a} (binary: {bin(a)})")
print(f"b = {b} (binary: {bin(b)})\n")

print(f"a & b (AND):               {a & b} (binary: {bin(a & b)})")
print(f"a | b (OR):                {a | b} (binary: {bin(a | b)})")
print(f"a ^ b (XOR):               {a ^ b} (binary: {bin(a ^ b)})")
print(f"~a (NOT):                  {~a}")
print(f"a << 1 (left shift):       {a << 1} (binary: {bin(a << 1)})")
print(f"a >> 1 (right shift):      {a >> 1} (binary: {bin(a >> 1)})")

# ============================================================================
# OPERATOR PRECEDENCE
# ============================================================================
# WHAT: Order in which operations are performed
# WHY: Understand expression evaluation, avoid bugs
# ORDER (high to low): () -> ** -> *, /, //, % -> +, - -> comparisons -> logical

print("\n" + "="*60)
print("OPERATOR PRECEDENCE")
print("="*60)

result1 = 2 + 3 * 4            # Multiplication first: 2 + 12 = 14
result2 = (2 + 3) * 4          # Parentheses first: 5 * 4 = 20
result3 = 10 - 3 + 2           # Left to right: 7 + 2 = 9
result4 = 2 ** 3 ** 2          # Right to left: 2 ** 9 = 512

print(f"2 + 3 * 4 = {result1}")
print(f"(2 + 3) * 4 = {result2}")
print(f"10 - 3 + 2 = {result3}")
print(f"2 ** 3 ** 2 = {result4}")

# ============================================================================
# PRACTICAL EXAMPLES
# ============================================================================

print("\n" + "="*60)
print("PRACTICAL EXAMPLES")
print("="*60)

# Check if number is even or odd
num = 15
if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")

# Check age range
age = 25
if age >= 18 and age < 65:
    print(f"Age {age}: Working age adult")

# Multiple membership checks
shopping_cart = ["milk", "eggs", "bread"]
if "milk" in shopping_cart and "eggs" in shopping_cart:
    print("Can make scrambled eggs!")

# Using logical operators for validation
username = "alice"
password = "secret123"
if len(username) >= 3 and len(password) >= 8:
    print("Valid credentials")
else:
    print("Invalid credentials")
