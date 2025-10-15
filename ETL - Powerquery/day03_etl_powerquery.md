# ETL Basics with Pandas + Power Query (EU-First Framework)

## Overview
This guide teaches ETL (Extract, Transform, Load) concepts using EU-hosted tools and services, respecting data sovereignty and GDPR compliance.

---

## 1. What is ETL?

**ETL** stands for:
- **Extract**: Pull data from various sources (databases, APIs, files)
- **Transform**: Clean, reshape, and enrich the data
- **Load**: Store the processed data in a destination system

### Real-World Example
Imagine collecting customer orders from multiple EU stores → cleaning/standardizing the data → loading into a central EU database for analytics.

---

## 2. EU-First Considerations

When working with data in the EU context:
-  **Data Residency**: Use EU-based cloud services (AWS Frankfurt, Azure West Europe, Google Belgium)
-  **GDPR Compliance**: Ensure personal data handling follows GDPR rules
-  **Data Sovereignty**: Keep sensitive data within EU borders
-  **EU Cloud Providers**: Consider OVHcloud (France), Hetzner (Germany), or Scaleway (France)

### Recommended EU Platforms
- **Databases**: PostgreSQL on EU servers, MySQL on Hetzner
- **Data Lakes**: MinIO on EU infrastructure, AWS S3 EU regions
- **Processing**: Python/pandas on EU-hosted VMs or containers

---

## 3. ETL with Pandas (Python)

**Pandas** is a powerful Python library for data manipulation, perfect for ETL workflows.

### Installation
```bash
pip install pandas openpyxl sqlalchemy psycopg2-binary
```

### Example: Basic ETL Pipeline

#### Extract
```python
import pandas as pd

# Extract from CSV
df_csv = pd.read_csv('eu_customers.csv')

# Extract from Excel
df_excel = pd.read_excel('orders.xlsx', sheet_name='Q1_2025')

# Extract from PostgreSQL (EU server)
from sqlalchemy import create_engine
engine = create_engine('postgresql://user:pass@eu-server.example.com:5432/dbname')
df_db = pd.read_sql('SELECT * FROM transactions WHERE country IN (\'DE\', \'FR\', \'IT\')', engine)
```

#### Transform
```python
# Data cleaning
df = df_csv.copy()

# Remove duplicates
df = df.drop_duplicates()

# Handle missing values
df['email'] = df['email'].fillna('no-email@example.com')

# Standardize column names
df.columns = df.columns.str.lower().str.replace(' ', '_')

# Filter EU countries only
eu_countries = ['DE', 'FR', 'IT', 'ES', 'NL', 'BE', 'AT', 'PL', 'SE', 'DK']
df = df[df['country'].isin(eu_countries)]

# Add calculated columns
df['total_with_vat'] = df['amount'] * 1.19  # German VAT example

# Data type conversions
df['order_date'] = pd.to_datetime(df['order_date'])
df['amount'] = pd.to_numeric(df['amount'], errors='coerce')
```

#### Load
```python
# Load to CSV
df.to_csv('cleaned_eu_data.csv', index=False)

# Load to PostgreSQL (EU server)
df.to_sql('clean_transactions', engine, if_exists='replace', index=False)

# Load to Excel
with pd.ExcelWriter('output.xlsx', engine='openpyxl') as writer:
    df.to_excel(writer, sheet_name='Cleaned_Data', index=False)
```

### Complete ETL Script Example
```python
import pandas as pd
from sqlalchemy import create_engine

def etl_pipeline():
    # EXTRACT
    print("Extracting data...")
    df = pd.read_csv('raw_data.csv')

    # TRANSFORM
    print("Transforming data...")
    df = df.drop_duplicates()
    df = df.dropna(subset=['customer_id', 'amount'])
    df['country'] = df['country'].str.upper()
    df = df[df['country'].isin(['DE', 'FR', 'IT', 'ES', 'NL'])]
    df['processed_date'] = pd.Timestamp.now()

    # LOAD
    print("Loading data...")
    engine = create_engine('postgresql://user:pass@eu-db.example.com/warehouse')
    df.to_sql('processed_orders', engine, if_exists='append', index=False)

    print(f" Loaded {len(df)} records to EU database")

if __name__ == "__main__":
    etl_pipeline()
```

---

## 4. Power Query (Microsoft Power BI / Excel)

**Power Query** is a visual ETL tool integrated into Excel and Power BI, great for business users.

### EU-First Setup for Power Query
- Use **Power BI Premium in EU regions** (West Europe, North Europe)
- Configure **data residency** in Power BI admin settings
- Use **on-premises data gateway** for sensitive EU data

### Power Query Basics

#### Accessing Power Query
- **Excel**: Data tab → Get Data → From File/From Database
- **Power BI Desktop**: Home → Get Data

#### Common Transformations

**1. Extract from CSV/Excel**
```
Home → Get Data → From File → From Text/CSV
or From Excel Workbook
```

**2. Transform Steps (UI)**
- **Remove Duplicates**: Home → Remove Rows → Remove Duplicates
- **Filter Rows**: Click column dropdown → Filter by values
- **Change Data Types**: Right-click column → Change Type
- **Replace Values**: Right-click column → Replace Values
- **Add Columns**: Add Column → Custom Column
- **Merge Queries**: Home → Merge Queries (like SQL JOIN)
- **Append Queries**: Home → Append Queries (like UNION)

**3. M Language (Power Query Formula Language)**

Example custom column:
```m
= Table.AddColumn(#"Previous Step", "VAT_Amount",
    each [Amount] * 0.19)
```

Filter EU countries:
```m
= Table.SelectRows(#"Changed Type",
    each List.Contains({"DE", "FR", "IT", "ES", "NL"}, [Country]))
```

**4. Load Data**
- **Excel**: Home → Close & Load → Close & Load To...
- **Power BI**: Home → Close & Apply

### Example Power Query ETL Workflow

**Scenario**: Consolidate sales data from multiple EU Excel files

1. **Extract**
   - Get Data → From Folder
   - Select folder with multiple Excel files
   - Combine & Transform Data

2. **Transform**
   - Remove columns: Remove unnecessary columns
   - Filter: Keep only `Country = "DE" or "FR" or "IT"`
   - Add Custom Column: `= [Quantity] * [UnitPrice]`
   - Change Types: Ensure dates and numbers are correct
   - Group By: Aggregate sales by country

3. **Load**
   - Close & Load to Excel table or Power BI model

### M Language Script Example
```m
let
    // Extract
    Source = Csv.Document(File.Contents("C:\Data\eu_sales.csv"), [Delimiter=",", Encoding=1252]),
    PromotedHeaders = Table.PromoteHeaders(Source),

    // Transform
    ChangedType = Table.TransformColumnTypes(PromotedHeaders, {
        {"OrderDate", type date},
        {"Amount", type number},
        {"Country", type text}
    }),
    FilteredEU = Table.SelectRows(ChangedType,
        each List.Contains({"DE", "FR", "IT", "ES", "NL", "BE"}, [Country])),
    AddedVAT = Table.AddColumn(FilteredEU, "AmountWithVAT",
        each [Amount] * 1.19, type number),
    RemovedDuplicates = Table.Distinct(AddedVAT, {"OrderID"})
in
    RemovedDuplicates
```

---

## 5. Comparing Pandas vs Power Query

| Feature | Pandas | Power Query |
|---------|--------|-------------|
| **User Level** | Developers/Data Scientists | Business Analysts/Excel Users |
| **Language** | Python | M Language (or UI) |
| **Flexibility** | Very high (any Python library) | Moderate (within M capabilities) |
| **Performance** | Excellent for large datasets | Good for medium datasets |
| **EU Hosting** | Run anywhere (EU VMs/containers) | Power BI EU regions or Excel desktop |
| **Version Control** | Easy (Python scripts in Git) | Harder (binary files) |
| **Automation** | Excellent (cron, Airflow) | Good (Power BI scheduled refresh) |
| **Learning Curve** | Steeper (requires Python) | Gentle (visual interface) |

---

## 6. EU-Hosted ETL Architecture Example

```text
┌─────────────────────────────────────────────────────────┐
│                  EU Data Sources                        │
│  (PostgreSQL Frankfurt, CSV on EU S3, Excel on-prem)   │
└────────────────┬────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────┐
│           ETL Processing Layer (EU Region)              │
│                                                           │
│  Option A: Python/Pandas on Hetzner VM (Germany)        │
│  Option B: Power BI Gateway in EU                        │
│  Option C: Apache Airflow on OVHcloud (France)          │
└────────────────┬────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────┐
│           Data Warehouse (EU Region)                    │
│  PostgreSQL on AWS Frankfurt or Azure West Europe       │
└─────────────────────────────────────────────────────────┘
```

---

## 7. Hands-On Exercise

### Exercise: Build an EU Sales ETL Pipeline

**Objective**: Extract customer orders, transform for EU compliance, load to database.

**Steps**:

1. **Create sample data** (`eu_orders.csv`):
```csv
OrderID,CustomerName,Email,Country,Amount,OrderDate
1001,Hans Müller,hans@example.de,DE,150.00,2025-01-15
1002,Marie Dubois,marie@example.fr,FR,200.00,2025-01-16
1003,John Doe,john@example.us,US,300.00,2025-01-17
1004,Luigi Rossi,luigi@example.it,IT,175.50,2025-01-18
1005,Emma Schmidt,,DE,220.00,2025-01-19
```

2. **Pandas Solution**:
```python
import pandas as pd

# Extract
df = pd.read_csv('eu_orders.csv')

# Transform
df = df[df['Country'].isin(['DE', 'FR', 'IT', 'ES', 'NL'])]  # EU only
df['Email'] = df['Email'].fillna('noemail@example.com')
df['AmountWithVAT'] = df['Amount'] * 1.19
df['ProcessedDate'] = pd.Timestamp.now()

# Load
df.to_csv('eu_orders_clean.csv', index=False)
print(f" Processed {len(df)} EU orders")
```

3. **Power Query Solution**:
   - Get Data → From Text/CSV → Select `eu_orders.csv`
   - Transform → Filter `Country` column → Keep DE, FR, IT, ES, NL
   - Replace null values in `Email` with "noemail@example.com"
   - Add Column → Custom Column: `[Amount] * 1.19` (name it `AmountWithVAT`)
   - Close & Load

---

## 8. Best Practices for EU ETL

1. **Data Minimization**: Only extract data you need (GDPR principle)
2. **Encryption**: Use TLS/SSL for data in transit, encryption at rest
3. **Audit Logging**: Log all ETL operations for compliance
4. **Anonymization**: Pseudonymize personal data when possible
5. **EU Hosting**: Ensure all processing happens within EU
6. **Documentation**: Maintain data lineage and transformation logic
7. **Testing**: Validate data quality at each stage
8. **Incremental Loads**: Use timestamps to process only new/changed data

---

## 9. Next Steps

- **Practice**: Run the hands-on exercise with your own data
- **Explore**: Try combining pandas and Power Query in hybrid workflows
- **Scale**: Look into Apache Airflow (EU-hosted) for production pipelines
- **Learn More**:
  - Pandas documentation: https://pandas.pydata.org
  - Power Query M reference: https://learn.microsoft.com/power-query
  - EU cloud providers: OVHcloud, Hetzner, Scaleway

---

## 10. Resources

- **EU Cloud Providers**:
  - [OVHcloud](https://www.ovhcloud.com) - France
  - [Hetzner](https://www.hetzner.com) - Germany
  - [Scaleway](https://www.scaleway.com) - France

- **Tools**:
  - Pandas: `pip install pandas`
  - Power BI Desktop: Download from Microsoft
  - DBeaver: EU database management tool

- **GDPR Resources**:
  - Official GDPR text: https://gdpr-info.eu
  - Data protection impact assessments (DPIA) guidelines

---

**📓 Document: *"ETL basics with pandas + PowerQuery"* - Completed**
