# ============================================================================
# 20. REGULAR EXPRESSIONS (REGEX) - PATTERN MATCHING
# ============================================================================
# WHAT: Powerful text pattern matching and manipulation
# WHY: Search, validate, extract, and replace text patterns
# WHEN: Email validation, parsing logs, data extraction, text processing

import re

# ============================================================================
# REGEX BASICS
# ============================================================================

print("="*60)
print("REGEX BASICS")
print("="*60)

print("""
Regular Expressions (Regex):
- Pattern matching for strings
- Search, validate, extract, replace text
- Powerful but can be complex

Common uses:
- Email/phone validation
- Extract data from text
- Find/replace patterns
- Parse log files
- Web scraping
""")

# ============================================================================
# BASIC REGEX FUNCTIONS
# ============================================================================

print("="*60)
print("BASIC REGEX FUNCTIONS")
print("="*60)

text = "The rain in Spain falls mainly in the plain"

# re.search() - Find first match
match = re.search("Spain", text)
if match:
    print(f"✓ Found 'Spain' at position {match.start()}-{match.end()}")

# re.findall() - Find all matches
matches = re.findall("ain", text)
print(f"\n'ain' appears {len(matches)} times: {matches}")

# re.split() - Split string by pattern
parts = re.split(r"\s", text)  # Split on whitespace
print(f"\nSplit into {len(parts)} words")

# re.sub() - Replace pattern
new_text = re.sub("Spain", "Denmark", text)
print(f"\nReplaced: {new_text}")

# ============================================================================
# METACHARACTERS
# ============================================================================

print("\n" + "="*60)
print("METACHARACTERS")
print("="*60)

# . - Any character (except newline)
print("Pattern '.ain':")
matches = re.findall(r".ain", text)
print(f"  Matches: {matches}")

# ^ - Start of string
print("\nPattern '^The':")
if re.search(r"^The", text):
    print("  ✓ String starts with 'The'")

# $ - End of string
print("\nPattern 'plain$':")
if re.search(r"plain$", text):
    print("  ✓ String ends with 'plain'")

# * - Zero or more occurrences
print("\nPattern 'ai*n':")
matches = re.findall(r"ai*n", "an ain aiin")
print(f"  Matches: {matches}")

# + - One or more occurrences
print("\nPattern 'ai+n':")
matches = re.findall(r"ai+n", "an ain aiin")
print(f"  Matches: {matches}")

# ? - Zero or one occurrence
print("\nPattern 'colou?r':")
matches = re.findall(r"colou?r", "color colour")
print(f"  Matches: {matches}")

# {} - Exactly specified number
print("\nPattern 'a{2}':")
matches = re.findall(r"a{2}", "aa aaa aaaa")
print(f"  Matches: {matches}")

# | - Either/or
print("\nPattern 'cat|dog':")
matches = re.findall(r"cat|dog", "I have a cat and a dog")
print(f"  Matches: {matches}")

# ============================================================================
# CHARACTER CLASSES
# ============================================================================

print("\n" + "="*60)
print("CHARACTER CLASSES")
print("="*60)

# [abc] - Any character in brackets
print("Pattern '[aeiou]':")
vowels = re.findall(r"[aeiou]", "hello world")
print(f"  Vowels found: {len(vowels)} - {vowels}")

# [a-z] - Range of characters
print("\nPattern '[a-z]':")
lowercase = re.findall(r"[a-z]", "Hello World 123")
print(f"  Lowercase: {lowercase}")

# [^abc] - NOT in brackets
print("\nPattern '[^aeiou]':")
consonants = re.findall(r"[^aeiou\s]", "hello world")
print(f"  Consonants: {consonants}")

# [0-9] - Digits
print("\nPattern '[0-9]':")
digits = re.findall(r"[0-9]", "Room 123 is on floor 4")
print(f"  Digits: {digits}")

# ============================================================================
# SPECIAL SEQUENCES
# ============================================================================

print("\n" + "="*60)
print("SPECIAL SEQUENCES")
print("="*60)

test_str = "The price is $49.99 and code is ABC123"

# \d - Digit (0-9)
print("Pattern '\\d+' (one or more digits):")
numbers = re.findall(r"\d+", test_str)
print(f"  Numbers: {numbers}")

# \D - Non-digit
print("\nPattern '\\D+' (one or more non-digits):")
non_digits = re.findall(r"\D+", test_str)
print(f"  Non-digits: {non_digits[:3]}")

# \w - Word character (a-z, A-Z, 0-9, _)
print("\nPattern '\\w+' (words):")
words = re.findall(r"\w+", test_str)
print(f"  Words: {words}")

# \W - Non-word character
print("\nPattern '\\W' (non-word chars):")
special = re.findall(r"\W", test_str)
print(f"  Special chars: {special}")

# \s - Whitespace
print("\nPattern '\\s' (whitespace):")
spaces = re.findall(r"\s", test_str)
print(f"  Spaces found: {len(spaces)}")

# \S - Non-whitespace
print("\nPattern '\\S+' (non-whitespace):")
non_spaces = re.findall(r"\S+", test_str)
print(f"  Tokens: {non_spaces}")

# ============================================================================
# SETS
# ============================================================================

print("\n" + "="*60)
print("SETS IN REGEX")
print("="*60)

# [arn] - Any of a, r, or n
print("Pattern '[arn]':")
matches = re.findall(r"[arn]", "banana")
print(f"  Matches: {matches}")

# [a-n] - Range from a to n
print("\nPattern '[a-n]':")
matches = re.findall(r"[a-n]", "hello world")
print(f"  Matches: {matches}")

# [^arn] - NOT a, r, or n
print("\nPattern '[^arn]':")
matches = re.findall(r"[^arn]", "banana")
print(f"  Matches: {matches}")

# [0-5][0-9] - Two-digit number 00-59
print("\nPattern '[0-5][0-9]':")
matches = re.findall(r"[0-5][0-9]", "Times: 12, 45, 67, 89")
print(f"  Valid times (00-59): {matches}")

# ============================================================================
# MATCH OBJECT
# ============================================================================

print("\n" + "="*60)
print("MATCH OBJECT")
print("="*60)

text = "The rain in Spain"
match = re.search(r"\bS\w+", text)  # Word starting with S

if match:
    print(f"Match found: '{match.group()}'")
    print(f"Position: {match.span()}")
    print(f"Start: {match.start()}, End: {match.end()}")
    print(f"Original string: '{match.string}'")

# ============================================================================
# PRACTICAL EXAMPLES
# ============================================================================

print("\n" + "="*60)
print("PRACTICAL EXAMPLES")
print("="*60)

# Example 1: Email Validation
print("\n1. Email Validation:")
def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))

emails = ["user@example.com", "invalid.email", "test@test.co.uk"]
for email in emails:
    valid = "✓" if is_valid_email(email) else "✗"
    print(f"  {valid} {email}")

# Example 2: Phone Number Extraction
print("\n2. Extract Phone Numbers:")
text = "Call me at 123-456-7890 or 555.123.4567"
pattern = r"\d{3}[-.]?\d{3}[-.]?\d{4}"
phones = re.findall(pattern, text)
print(f"  Found: {phones}")

# Example 3: Extract URLs
print("\n3. Extract URLs:")
text = "Visit https://www.example.com or http://test.org for info"
pattern = r"https?://[\w.-]+"
urls = re.findall(pattern, text)
print(f"  Found: {urls}")

# Example 4: Password Validation
print("\n4. Password Validation:")
def is_strong_password(password):
    """
    Must have:
    - At least 8 characters
    - At least one uppercase
    - At least one lowercase
    - At least one digit
    """
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"\d", password):
        return False
    return True

passwords = ["weak", "Strong1", "VerySecure123"]
for pwd in passwords:
    valid = "✓" if is_strong_password(pwd) else "✗"
    print(f"  {valid} '{pwd}'")

# Example 5: Extract Dates
print("\n5. Extract Dates (DD/MM/YYYY or DD-MM-YYYY):")
text = "Events: 25/12/2023, 01-01-2024, and 15/08/2024"
pattern = r"\d{2}[/-]\d{2}[/-]\d{4}"
dates = re.findall(pattern, text)
print(f"  Found: {dates}")

# Example 6: Find Hashtags
print("\n6. Extract Hashtags:")
text = "Follow #python and #coding for updates! #programming"
pattern = r"#\w+"
hashtags = re.findall(pattern, text)
print(f"  Found: {hashtags}")

# Example 7: Remove HTML Tags
print("\n7. Remove HTML Tags:")
html = "<p>This is <b>bold</b> and <i>italic</i> text.</p>"
clean = re.sub(r"<[^>]+>", "", html)
print(f"  Original: {html}")
print(f"  Cleaned: {clean}")

# Example 8: Extract Numbers from Text
print("\n8. Extract Numbers:")
text = "Price: $49.99, Quantity: 10, Total: $499.90"
integers = re.findall(r"\d+", text)
floats = re.findall(r"\d+\.\d+", text)
print(f"  Integers: {integers}")
print(f"  Floats: {floats}")

# Example 9: Split on Multiple Delimiters
print("\n9. Split on Multiple Delimiters:")
text = "apple,banana;orange|grape:melon"
fruits = re.split(r"[,;|:]", text)
print(f"  Fruits: {fruits}")

# Example 10: Replace Multiple Spaces with Single Space
print("\n10. Normalize Whitespace:")
text = "This   has    irregular     spacing"
normalized = re.sub(r"\s+", " ", text)
print(f"  Original: '{text}'")
print(f"  Normalized: '{normalized}'")

# ============================================================================
# REGEX FLAGS
# ============================================================================

print("\n" + "="*60)
print("REGEX FLAGS")
print("="*60)

print("""
Common flags:
re.IGNORECASE (re.I) - Case-insensitive matching
re.MULTILINE (re.M)  - ^ and $ match line start/end
re.DOTALL (re.S)     - . matches newline too
re.VERBOSE (re.X)    - Allow comments in pattern
""")

# Case-insensitive search
text = "Python is AWESOME"
matches = re.findall(r"python", text, re.IGNORECASE)
print(f"Case-insensitive: {matches}")

# ============================================================================
# COMMON PATTERNS CHEAT SHEET
# ============================================================================

print("\n" + "="*60)
print("COMMON PATTERNS CHEAT SHEET")
print("="*60)

print("""
Email:      ^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$
URL:        https?://[\\w.-]+
Phone:      \\d{3}[-.]?\\d{3}[-.]?\\d{4}
Date:       \\d{2}/\\d{2}/\\d{4}
Time:       \\d{2}:\\d{2}(:\\d{2})?
Hashtag:    #\\w+
Mention:    @\\w+
IP Address: \\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}
Hex Color:  #[0-9A-Fa-f]{6}
""")

# ============================================================================
# AUTOMATION USE CASES (FROM ATBS)
# ============================================================================

print("\n" + "="*60)
print("AUTOMATION USE CASES")
print("="*60)

print("""
💡 Real-world automation with regex:

1. Email/Contact Validation
   - Validate form inputs
   - Clean mailing lists
   - Extract contacts from documents

2. Log File Analysis
   - Parse server logs
   - Extract error codes
   - Find IP addresses

3. Data Extraction from Text
   - Pull phone numbers from PDFs
   - Extract prices from web pages
   - Find dates in documents

4. Text Preprocessing for AI/ML
   - Clean datasets
   - Remove special characters
   - Standardize formats

5. Web Scraping Enhancement
   - Extract structured data
   - Parse HTML patterns
   - Clean scraped text
""")

# Example: Extract all contacts from mixed text
print("\nExample: Extract all contact info from text")
contact_text = """
For support, email help@company.com or call 555-123-4567.
Sales: sales@company.com (555-987-6543)
Website: https://www.company.com
"""

emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", contact_text)
phones = re.findall(r"\d{3}[-.]?\d{3}[-.]?\d{4}", contact_text)
urls = re.findall(r"https?://[\w.-]+", contact_text)

print(f"Emails found: {emails}")
print(f"Phones found: {phones}")
print(f"URLs found: {urls}")
