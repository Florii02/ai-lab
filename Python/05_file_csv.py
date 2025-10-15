# ============================================================================
# 5. FILE HANDLING - CSV (Comma-Separated Values)
# ============================================================================
# WHAT: Read and write CSV files using Python's csv module
# WHY: CSV is a common format for tabular data, Excel compatibility
# WHEN: Working with spreadsheet data, data import/export

import csv

# ============================================================================
# WRITING CSV FILES
# ============================================================================
# WHAT: Create CSV file with rows of data
# WHY: Export data for Excel, databases, or other programs
# NOTE: newline="" prevents extra blank lines on Windows

print("Writing CSV file...")
with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])     # Header row
    writer.writerow(["Alice", 30, "Berlin"])
    writer.writerow(["Bob", 25, "Munich"])
    writer.writerow(["Carol", 35, "Hamburg"])
print("CSV file created: data.csv")

# ============================================================================
# READING CSV FILES
# ============================================================================
# WHAT: Read CSV file row by row
# WHY: Process data from CSV files

print("\nReading CSV file:")
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print("CSV row:", row)

# ============================================================================
# USING CSV DICTREADER (MORE READABLE)
# ============================================================================
# WHAT: Read CSV with first row as keys (column names)
# WHY: Access columns by name instead of index - more readable

print("\nReading with DictReader:")
with open("data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"Name: {row['Name']}, Age: {row['Age']}, City: {row['City']}")

# ============================================================================
# CSV FOR BI & DATA PIPELINES
# ============================================================================

print("\n" + "="*60)
print("CSV → BI INTEGRATION")
print("="*60)

print("""
💡 CSV as ETL Bridge Format:

1. Extract Data → CSV
   - Export from databases (SQL → CSV)
   - Download from web portals
   - API response → CSV conversion

2. Transform in Python
   - Clean data (remove nulls, duplicates)
   - Aggregate (sum, average, group by)
   - Enrich (add calculated columns)

3. Load to BI Tools
   - Power BI: Import CSV directly
   - Tableau: Connect to CSV
   - Excel: Open and format
   - Google Sheets: Upload via API

💡 Automation Workflow:
   1. Python script fetches data (API/DB)
   2. Process & clean with pandas
   3. Export to CSV
   4. Power BI refreshes from CSV (scheduled)
   5. Email report to stakeholders
""")

print("\nExample: CSV → Power BI Pipeline")
print("""
# Step 1: Extract and Transform
import csv
import requests

response = requests.get("https://api.example.com/sales")
data = response.json()

# Step 2: Write to CSV
with open("sales_data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Date", "Revenue", "Items"])
    for record in data:
        writer.writerow([record["date"], record["revenue"], record["items"]])

# Step 3: Power BI Auto-Refresh
# - Power BI Desktop: Import from CSV
# - Set refresh schedule (hourly/daily)
# - Publish to Power BI Service
""")

print("\n🔗 Make.com / n8n Integration:")
print("- Trigger: Scheduled (daily 9am)")
print("- Action 1: Run Python script (generate CSV)")
print("- Action 2: Upload CSV to Google Drive/OneDrive")
print("- Action 3: Notify team via Slack/Email")
print("- Power BI reads from cloud CSV")

# Cleanup
import os
if os.path.exists("data.csv"):
    os.remove("data.csv")
    print("\nCleaned up: data.csv")
