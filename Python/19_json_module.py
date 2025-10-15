# ============================================================================
# 19. JSON MODULE - WORKING WITH JSON DATA
# ============================================================================
# WHAT: JSON (JavaScript Object Notation) - text format for data exchange
# WHY: APIs use JSON, configuration files, data storage, universal format
# WHEN: Web APIs, config files, data serialization, cross-language data

import json

# ============================================================================
# JSON BASICS
# ============================================================================

print("="*60)
print("JSON BASICS")
print("="*60)

print("""
JSON (JavaScript Object Notation):
- Lightweight data-interchange format
- Human-readable text format
- Language-independent (used everywhere)
- Similar to Python dictionaries

Common uses:
- Web APIs (most APIs return JSON)
- Configuration files
- Data storage
- Data exchange between systems
""")

# ============================================================================
# PYTHON TO JSON (json.dumps)
# ============================================================================

print("="*60)
print("PYTHON TO JSON - json.dumps()")
print("="*60)

# WHAT: Convert Python object to JSON string
# WHY: Send data to API, save to file, transmit over network

# Dictionary to JSON
person = {
    "name": "Alice",
    "age": 30,
    "city": "Berlin",
    "is_student": False
}

json_string = json.dumps(person)
print("Python dict:", person)
print("JSON string:", json_string)
print("Type:", type(json_string))

# ============================================================================
# DATA TYPE CONVERSION
# ============================================================================

print("\n" + "="*60)
print("PYTHON TO JSON TYPE CONVERSION")
print("="*60)

# Python types that can be converted to JSON
python_types = {
    "dictionary": {"key": "value"},
    "list": [1, 2, 3],
    "tuple": (1, 2, 3),
    "string": "hello",
    "integer": 42,
    "float": 3.14,
    "boolean_true": True,
    "boolean_false": False,
    "none": None
}

for name, value in python_types.items():
    json_value = json.dumps(value)
    print(f"{name:20s} {str(value):20s} -> {json_value}")

print("""
\nPython -> JSON Conversion:
dict     -> Object
list     -> Array
tuple    -> Array
str      -> String
int      -> Number
float    -> Number
True     -> true
False    -> false
None     -> null
""")

# ============================================================================
# JSON FORMATTING
# ============================================================================

print("="*60)
print("JSON FORMATTING")
print("="*60)

data = {
    "name": "John",
    "age": 30,
    "married": True,
    "children": ["Ann", "Billy"],
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

# Without formatting (compact)
compact = json.dumps(data)
print("Compact JSON:")
print(compact[:80] + "...")

# With indentation (readable)
print("\nFormatted JSON (indent=4):")
formatted = json.dumps(data, indent=4)
print(formatted)

# Custom separators
print("\nCustom separators:")
custom = json.dumps(data, indent=4, separators=(". ", " = "))
print(custom[:100] + "...")

# Sorted keys
print("\nSorted keys (sort_keys=True):")
sorted_json = json.dumps(data, indent=4, sort_keys=True)
print(sorted_json)

# ============================================================================
# JSON TO PYTHON (json.loads)
# ============================================================================

print("\n" + "="*60)
print("JSON TO PYTHON - json.loads()")
print("="*60)

# WHAT: Convert JSON string to Python object
# WHY: Parse API responses, read JSON data

json_string = '{"name": "Bob", "age": 25, "city": "Munich"}'
print("JSON string:", json_string)

# Parse JSON string
python_dict = json.loads(json_string)
print("Python dict:", python_dict)
print("Type:", type(python_dict))
print("Access value:", python_dict["name"])

# ============================================================================
# READING JSON FROM FILE
# ============================================================================

print("\n" + "="*60)
print("READING JSON FROM FILE - json.load()")
print("="*60)

# Create JSON file
data = {
    "users": [
        {"id": 1, "name": "Alice", "email": "alice@example.com"},
        {"id": 2, "name": "Bob", "email": "bob@example.com"}
    ],
    "total": 2
}

# Write JSON to file
with open("users.json", "w") as file:
    json.dump(data, file, indent=4)
print("Created 'users.json'")

# Read JSON from file
with open("users.json", "r") as file:
    loaded_data = json.load(file)

print("\nData loaded from file:")
print(f"Total users: {loaded_data['total']}")
for user in loaded_data['users']:
    print(f"  {user['name']}: {user['email']}")

# ============================================================================
# WRITING JSON TO FILE
# ============================================================================

print("\n" + "="*60)
print("WRITING JSON TO FILE - json.dump()")
print("="*60)

# WHAT: Write Python object directly to file as JSON
# WHY: Save configuration, cache data, export data

config = {
    "app_name": "MyApp",
    "version": "1.0.0",
    "settings": {
        "theme": "dark",
        "language": "en",
        "notifications": True
    },
    "database": {
        "host": "localhost",
        "port": 5432,
        "name": "myapp_db"
    }
}

with open("config.json", "w") as file:
    json.dump(config, file, indent=4)

print("Configuration saved to 'config.json'")
print("\nFile contents:")
with open("config.json", "r") as file:
    print(file.read())

# ============================================================================
# HANDLING NESTED JSON
# ============================================================================

print("="*60)
print("HANDLING NESTED JSON")
print("="*60)

json_data = '''
{
    "company": "TechCorp",
    "employees": [
        {
            "name": "Alice",
            "position": "Developer",
            "skills": ["Python", "JavaScript", "SQL"]
        },
        {
            "name": "Bob",
            "position": "Designer",
            "skills": ["Photoshop", "Illustrator"]
        }
    ],
    "location": {
        "city": "Berlin",
        "country": "Germany"
    }
}
'''

data = json.loads(json_data)

print(f"Company: {data['company']}")
print(f"Location: {data['location']['city']}, {data['location']['country']}")
print("\nEmployees:")
for emp in data['employees']:
    print(f"  {emp['name']} - {emp['position']}")
    print(f"    Skills: {', '.join(emp['skills'])}")

# ============================================================================
# ERROR HANDLING
# ============================================================================

print("\n" + "="*60)
print("ERROR HANDLING")
print("="*60)

# Invalid JSON
invalid_json = '{"name": "Alice", "age": 30,}'  # Trailing comma

try:
    data = json.loads(invalid_json)
except json.JSONDecodeError as e:
    print(f"JSON Error: {e}")
    print(f"Error at line {e.lineno}, column {e.colno}")

# ============================================================================
# PRACTICAL EXAMPLES
# ============================================================================

print("\n" + "="*60)
print("PRACTICAL EXAMPLES")
print("="*60)

# Example 1: API Response Simulation
print("\n1. Parse API response:")
api_response = '''
{
    "status": "success",
    "data": {
        "temperature": 22.5,
        "humidity": 65,
        "condition": "sunny"
    }
}
'''

weather = json.loads(api_response)
if weather["status"] == "success":
    temp = weather["data"]["temperature"]
    condition = weather["data"]["condition"]
    print(f"Weather: {temp}°C, {condition}")

# Example 2: Save/Load User Preferences
print("\n2. Save and load user preferences:")

def save_preferences(prefs):
    with open("prefs.json", "w") as f:
        json.dump(prefs, f, indent=4)
    print("Preferences saved")

def load_preferences():
    try:
        with open("prefs.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Save preferences
user_prefs = {
    "username": "alice",
    "theme": "dark",
    "notifications": True,
    "language": "en"
}
save_preferences(user_prefs)

# Load preferences
loaded_prefs = load_preferences()
print(f"Loaded preferences: {loaded_prefs}")

# Example 3: JSON Data Manipulation
print("\n3. Add user to JSON file:")

# Read existing data
with open("users.json", "r") as f:
    users_data = json.load(f)

# Add new user
new_user = {"id": 3, "name": "Charlie", "email": "charlie@example.com"}
users_data["users"].append(new_user)
users_data["total"] = len(users_data["users"])

# Write back to file
with open("users.json", "w") as f:
    json.dump(users_data, f, indent=4)

print("User added to 'users.json'")

# Example 4: Pretty Print JSON
print("\n4. Pretty print JSON:")

def pretty_print_json(json_string):
    data = json.loads(json_string)
    print(json.dumps(data, indent=4, sort_keys=True))

json_str = '{"name":"Alice","age":30,"city":"Berlin"}'
pretty_print_json(json_str)

# ============================================================================
# JSON FOR BI & DATA PIPELINES
# ============================================================================

print("\n" + "="*60)
print("JSON FOR BI & DATA PIPELINES")
print("="*60)

print("""
💡 Why JSON is Critical for BI/AI/Automation:

1. API Communication
   - REST APIs send/receive JSON
   - Connect to external data sources
   - Push data to visualization tools

2. ETL Pipeline Format
   - Extract: API → JSON
   - Transform: Process JSON data
   - Load: JSON → Database/Excel/Power BI

3. Configuration Files
   - Make.com/n8n workflows use JSON
   - Store API credentials (encrypted)
   - Define data transformations

4. LLM/AI Integration
   - Send prompts with JSON context
   - Receive structured AI responses
   - Chain multiple AI calls with JSON

5. Data Exchange
   - Cross-platform format (Python ↔ JavaScript ↔ Power BI)
   - Version control friendly (git-trackable)
   - Human-readable for debugging
""")

# Example: ETL Pipeline with JSON
print("\nExample: ETL Pipeline Flow")
print("""
Step 1: Extract (API → JSON)
------
import requests
response = requests.get("https://api.example.com/data")
raw_data = response.json()  # Parse JSON response

Step 2: Transform (Process JSON)
------
transformed = {
    "date": raw_data["timestamp"][:10],
    "revenue": sum(item["price"] for item in raw_data["sales"]),
    "items_sold": len(raw_data["sales"])
}

Step 3: Load (JSON → Excel/Power BI)
------
import pandas as pd
df = pd.json_normalize(transformed)  # Convert to DataFrame
df.to_excel("report.xlsx")  # Or push to Power BI API
""")

print("\n📊 JSON → Power BI Integration:")
print("1. Python script fetches API data (JSON)")
print("2. Transform & clean in Python")
print("3. Save to CSV or push via Power BI REST API")
print("4. Power BI reads JSON directly or via gateway")
print("5. Automate with schedule (daily refresh)")

print("\n🔗 Make.com / n8n Automation:")
print("- Trigger: Webhook receives JSON")
print("- Process: Parse & validate JSON data")
print("- Action: Send to Google Sheets, Slack, email")
print("- Store: Save to database as JSON")

# Cleanup
import os
print("\n\nCleaning up demo files...")
for f in ["users.json", "config.json", "prefs.json"]:
    if os.path.exists(f):
        os.remove(f)
        print(f"Deleted {f}")
