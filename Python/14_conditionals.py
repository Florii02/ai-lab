# ============================================================================
# 14. CONDITIONALS - IF, ELIF, ELSE
# ============================================================================
# WHAT: Control flow based on conditions (True/False)
# WHY: Make decisions, execute code selectively, handle different scenarios
# WHEN: Need different behavior based on conditions

# ============================================================================
# BASIC IF STATEMENT
# ============================================================================

print("="*60)
print("BASIC IF STATEMENT")
print("="*60)

# WHAT: Execute code only if condition is True
# SYNTAX: if condition:

age = 20

if age >= 18:
    print(f"Age {age}: You are an adult")
    print("You can vote")

print("Program continues...")

# ============================================================================
# IF-ELSE STATEMENT
# ============================================================================

print("\n" + "="*60)
print("IF-ELSE STATEMENT")
print("="*60)

# WHAT: Execute one block if True, another if False
# WHY: Handle both outcomes

temperature = 15

if temperature > 20:
    print(f"{temperature}°C: It's warm outside")
else:
    print(f"{temperature}°C: It's cold outside")

# ============================================================================
# IF-ELIF-ELSE STATEMENT
# ============================================================================

print("\n" + "="*60)
print("IF-ELIF-ELSE STATEMENT")
print("="*60)

# WHAT: Check multiple conditions in sequence
# WHY: Handle multiple different scenarios
# NOTE: Only FIRST true condition executes

score = 75

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score {score} = Grade {grade}")

# ============================================================================
# COMPARISON OPERATORS IN CONDITIONS
# ============================================================================

print("\n" + "="*60)
print("COMPARISON OPERATORS")
print("="*60)

x, y = 10, 20

print(f"x = {x}, y = {y}\n")

if x == y:
    print("x equals y")

if x != y:
    print("x does not equal y")

if x < y:
    print("x is less than y")

if x > y:
    print("x is greater than y")
else:
    print("x is not greater than y")

# ============================================================================
# LOGICAL OPERATORS - AND, OR, NOT
# ============================================================================

print("\n" + "="*60)
print("LOGICAL OPERATORS")
print("="*60)

age = 25
has_license = True

# AND - Both conditions must be True
if age >= 18 and has_license:
    print("Can drive a car")

# OR - At least one condition must be True
is_weekend = False
is_holiday = True

if is_weekend or is_holiday:
    print("No work today!")

# NOT - Reverse the condition
is_raining = False

if not is_raining:
    print("Can go for a walk")

# ============================================================================
# NESTED IF STATEMENTS
# ============================================================================

print("\n" + "="*60)
print("NESTED IF STATEMENTS")
print("="*60)

# WHAT: If statements inside other if statements
# WHY: Check conditions that depend on other conditions

age = 16
has_id = True

if age >= 13:
    print("Age check passed")
    if age >= 18:
        print("  Access level: Adult")
    else:
        if has_id:
            print("  Access level: Teen with ID")
        else:
            print("  Access level: Teen (no ID)")

# ============================================================================
# SHORT HAND IF (TERNARY OPERATOR)
# ============================================================================

print("\n" + "="*60)
print("SHORT HAND IF (TERNARY OPERATOR)")
print("="*60)

# WHAT: Compact one-line if-else
# SYNTAX: value_if_true if condition else value_if_false
# WHY: Concise for simple conditions

age = 22
status = "Adult" if age >= 18 else "Minor"
print(f"Age {age}: {status}")

# Can use in expressions
price = 100
discount = 0.2 if price > 50 else 0
final_price = price * (1 - discount)
print(f"\nPrice: ${price}, Discount: {discount*100}%, Final: ${final_price}")

# ============================================================================
# SHORT HAND IF WITHOUT ELSE
# ============================================================================

print("\n" + "="*60)
print("SHORT HAND IF (SINGLE LINE)")
print("="*60)

# WHAT: One-line if statement (no else clause)
# NOTE: Less common, can reduce readability

x = 5
if x > 0: print("Positive")  # Everything on one line

# ============================================================================
# MULTIPLE CONDITIONS ON ONE LINE
# ============================================================================

print("\n" + "="*60)
print("CHAINED TERNARY OPERATORS")
print("="*60)

# WHAT: Multiple conditions in one line
# WHY: Very compact (but can reduce readability)

score = 85
grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "F"
print(f"Score {score} = Grade {grade}")

# ============================================================================
# PASS STATEMENT
# ============================================================================

print("\n" + "="*60)
print("PASS STATEMENT")
print("="*60)

# WHAT: Placeholder for empty code block
# WHY: Python requires code in if blocks, use pass when planning structure

age = 25

if age < 18:
    pass  # TODO: Implement minor handling later
elif age >= 65:
    pass  # TODO: Implement senior handling later
else:
    print("Adult handling complete")

# ============================================================================
# MEMBERSHIP OPERATORS IN CONDITIONS
# ============================================================================

print("\n" + "="*60)
print("MEMBERSHIP OPERATORS")
print("="*60)

# Check if value exists in sequence
fruits = ["apple", "banana", "cherry"]

if "apple" in fruits:
    print("We have apples!")

if "grape" not in fruits:
    print("We need to buy grapes")

# Check substring in string
text = "Hello World"
if "World" in text:
    print("Found 'World' in text")

# ============================================================================
# IDENTITY OPERATORS IN CONDITIONS
# ============================================================================

print("\n" + "="*60)
print("IDENTITY OPERATORS")
print("="*60)

# Check if variables reference same object
x = None

if x is None:
    print("x is None")

if x is not None:
    print("x has a value")
else:
    print("x has no value")

# ============================================================================
# PRACTICAL EXAMPLES
# ============================================================================

print("\n" + "="*60)
print("PRACTICAL EXAMPLES")
print("="*60)

# Example 1: Login validation
username = "admin"
password = "secret"

if len(username) >= 3 and len(password) >= 6:
    print("Valid credentials format")
else:
    print("Invalid credentials format")

# Example 2: Grade calculator
score = 88

if score >= 90:
    print(f"Score {score}: Excellent!")
elif score >= 70:
    print(f"Score {score}: Good job!")
elif score >= 50:
    print(f"Score {score}: Need improvement")
else:
    print(f"Score {score}: Failed")

# Example 3: Even or odd
number = 17
if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")

# Example 4: Age category
age = 35
if age < 13:
    category = "Child"
elif age < 20:
    category = "Teenager"
elif age < 65:
    category = "Adult"
else:
    category = "Senior"
print(f"Age {age}: {category}")

# Example 5: Discount eligibility
total = 150
is_member = True

if total > 100 and is_member:
    discount = 0.2
elif total > 100:
    discount = 0.1
elif is_member:
    discount = 0.05
else:
    discount = 0

print(f"\nTotal: ${total}, Member: {is_member}, Discount: {discount*100}%")
print(f"Final price: ${total * (1 - discount)}")

# Example 6: Range checking
temperature = 22
if 18 <= temperature <= 25:
    print(f"\n{temperature}°C: Comfortable temperature")
else:
    print(f"\n{temperature}°C: Uncomfortable temperature")
