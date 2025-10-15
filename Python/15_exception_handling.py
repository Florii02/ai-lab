# ============================================================================
# 15. EXCEPTION HANDLING - TRY, EXCEPT, FINALLY
# ============================================================================
# WHAT: Handle errors gracefully without crashing program
# WHY: Prevent crashes, provide user-friendly error messages, cleanup resources
# WHEN: File operations, user input, network requests, any error-prone code

# ============================================================================
# BASIC TRY-EXCEPT
# ============================================================================

print("="*60)
print("BASIC TRY-EXCEPT")
print("="*60)

# WHAT: Try code that might fail, handle errors in except block
# WHY: Program continues running even if error occurs

print("Example 1: Handling undefined variable")
try:
    print(undefined_variable)  # This will cause NameError
except:
    print("An error occurred!")

print("Program continues...\n")

# ============================================================================
# SPECIFIC EXCEPTION TYPES
# ============================================================================

print("="*60)
print("SPECIFIC EXCEPTION TYPES")
print("="*60)

# WHY: Handle different errors differently

print("Example: Division by zero")
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

print("\nExample: Invalid type conversion")
try:
    number = int("hello")
except ValueError:
    print("Cannot convert 'hello' to integer!")

print("\nExample: Accessing non-existent key")
try:
    person = {"name": "Alice"}
    print(person["age"])
except KeyError:
    print("Key 'age' not found in dictionary!")

# ============================================================================
# MULTIPLE EXCEPT BLOCKS
# ============================================================================

print("\n" + "="*60)
print("MULTIPLE EXCEPT BLOCKS")
print("="*60)

# WHY: Handle different errors with specific responses

def process_number(text):
    try:
        number = int(text)
        result = 100 / number
        return result
    except ValueError:
        return "Error: Not a valid number"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"

print(f"process_number('20'): {process_number('20')}")
print(f"process_number('hello'): {process_number('hello')}")
print(f"process_number('0'): {process_number('0')}")

# ============================================================================
# CATCHING MULTIPLE EXCEPTIONS
# ============================================================================

print("\n" + "="*60)
print("CATCHING MULTIPLE EXCEPTIONS")
print("="*60)

# WHY: Handle multiple exception types with same code

try:
    # This could raise either ValueError or ZeroDivisionError
    x = int(input("Enter a number (or just press Enter): ") or "abc")
    result = 10 / x
except (ValueError, ZeroDivisionError) as e:
    print(f"Input error: {e}")

# ============================================================================
# TRY-EXCEPT-ELSE
# ============================================================================

print("\n" + "="*60)
print("TRY-EXCEPT-ELSE")
print("="*60)

# WHAT: Else block runs if NO exception occurs
# WHY: Code that should only run when try succeeds

try:
    print("Trying to process...")
    result = 10 / 2
except ZeroDivisionError:
    print("Error occurred!")
else:
    print(f"Success! Result: {result}")
    print("No errors occurred")

# ============================================================================
# TRY-EXCEPT-FINALLY
# ============================================================================

print("\n" + "="*60)
print("TRY-EXCEPT-FINALLY")
print("="*60)

# WHAT: Finally block ALWAYS runs (error or not)
# WHY: Cleanup code (close files, connections) that must run

try:
    print("Opening resource...")
    result = 10 / 0  # This will error
    print("Processing...")
except ZeroDivisionError:
    print("Error: Division by zero")
finally:
    print("Cleanup: This always runs")
    print("Resource closed")

# ============================================================================
# RAISING EXCEPTIONS
# ============================================================================

print("\n" + "="*60)
print("RAISING EXCEPTIONS")
print("="*60)

# WHAT: Manually trigger exceptions
# WHY: Validate input, enforce rules

def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age cannot exceed 150")
    return f"Age {age} is valid"

try:
    print(check_age(25))
    print(check_age(-5))
except ValueError as e:
    print(f"Validation error: {e}")

# ============================================================================
# RAISING SPECIFIC EXCEPTION TYPES
# ============================================================================

print("\n" + "="*60)
print("SPECIFIC EXCEPTION TYPES")
print("="*60)

def withdraw(balance, amount):
    if not isinstance(amount, (int, float)):
        raise TypeError("Amount must be a number")
    if amount < 0:
        raise ValueError("Amount cannot be negative")
    if amount > balance:
        raise Exception("Insufficient funds")
    return balance - amount

try:
    balance = 100
    print(f"Balance: ${balance}")
    new_balance = withdraw(balance, 150)
    print(f"New balance: ${new_balance}")
except Exception as e:
    print(f"Transaction failed: {e}")

# ============================================================================
# ACCESSING EXCEPTION DETAILS
# ============================================================================

print("\n" + "="*60)
print("ACCESSING EXCEPTION DETAILS")
print("="*60)

try:
    numbers = [1, 2, 3]
    print(numbers[10])
except IndexError as e:
    print(f"Exception type: {type(e).__name__}")
    print(f"Exception message: {e}")
    print(f"Exception args: {e.args}")

# ============================================================================
# PRACTICAL EXAMPLES
# ============================================================================

print("\n" + "="*60)
print("PRACTICAL EXAMPLES")
print("="*60)

# Example 1: Safe file reading
print("\nExample 1: File operations")
try:
    with open("nonexistent.txt", "r") as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("File not found - creating default file")
    with open("default.txt", "w") as f:
        f.write("Default content")
    print("Default file created")
except PermissionError:
    print("Permission denied to access file")
finally:
    print("File operation complete")

# Example 2: Safe user input
print("\nExample 2: User input validation")
def get_positive_number():
    try:
        value = int(input("Enter a positive number (or press Enter for demo): ") or "-5")
        if value <= 0:
            raise ValueError("Number must be positive")
        return value
    except ValueError as e:
        print(f"Invalid input: {e}")
        return None

result = get_positive_number()
if result:
    print(f"You entered: {result}")

# Example 3: API call with error handling
print("\nExample 3: API call simulation")
def fetch_data(url):
    try:
        # Simulate API call
        if "invalid" in url:
            raise ValueError("Invalid URL")
        if "timeout" in url:
            raise TimeoutError("Connection timeout")
        return {"data": "Success"}
    except ValueError as e:
        return {"error": f"Bad request: {e}"}
    except TimeoutError as e:
        return {"error": f"Network error: {e}"}
    except Exception as e:
        return {"error": f"Unknown error: {e}"}

print(fetch_data("https://api.example.com/data"))
print(fetch_data("https://invalid.com/data"))

# Example 4: Division calculator
print("\nExample 4: Safe calculator")
def safe_divide(a, b):
    try:
        result = a / b
        return f"{a} / {b} = {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    except TypeError:
        return "Error: Both arguments must be numbers"

print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide(10, "2"))

# ============================================================================
# COMMON EXCEPTION TYPES
# ============================================================================

print("\n" + "="*60)
print("COMMON EXCEPTION TYPES")
print("="*60)

print("""
Common Python Exceptions:

ValueError:      Invalid value (e.g., int('hello'))
TypeError:       Wrong type (e.g., 'text' + 5)
KeyError:        Missing dictionary key
IndexError:      Invalid list/tuple index
FileNotFoundError: File doesn't exist
ZeroDivisionError: Division by zero
AttributeError:  Attribute doesn't exist
ImportError:     Module import failed
NameError:       Variable not defined
IOError:         Input/output error
""")
