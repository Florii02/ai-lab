# ============================================================================
# 22. PDF PROCESSING - READ & EXTRACT DATA
# ============================================================================
# WHAT: Extract text and data from PDF files using Python
# WHY: PDFs are common for reports, invoices, documents - automate extraction
# WHEN: Process invoices, extract reports, read documentation, data mining
# NOTE: Requires pypdf or PyPDF2 - install with: pip install pypdf

print("="*60)
print("PDF PROCESSING WITH PYTHON")
print("="*60)

print("""
💡 Why Process PDFs?
- Extract text from reports, invoices, contracts
- Automate data entry from PDF forms
- Convert PDF tables to CSV/Excel
- Search through multiple PDFs
- Extract metadata (author, date, etc.)
""")

# ============================================================================
# BASIC PDF READING
# ============================================================================

print("\n" + "="*60)
print("BASIC PDF READING")
print("="*60)

try:
    # Try pypdf first (newer), fallback to PyPDF2
    try:
        from pypdf import PdfReader
        print("Using pypdf library")
    except ImportError:
        from PyPDF2 import PdfReader
        print("Using PyPDF2 library")

    print("""
    Installation:
    pip install pypdf         # Recommended (newer)
    pip install PyPDF2        # Alternative (older)
    """)

    # Example code for reading PDFs
    print("\nExample: Reading PDF Files")
    print("""
    from pypdf import PdfReader

    # Open PDF file
    reader = PdfReader("document.pdf")

    # Get number of pages
    num_pages = len(reader.pages)
    print(f"PDF has {num_pages} pages")

    # Extract text from first page
    page = reader.pages[0]
    text = page.extract_text()
    print(text)

    # Loop through all pages
    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        print(f"--- Page {i+1} ---")
        print(text)
    """)

    # ============================================================================
    # PDF METADATA
    # ============================================================================

    print("\n" + "="*60)
    print("EXTRACTING PDF METADATA")
    print("="*60)

    print("""
    # Get PDF information
    reader = PdfReader("document.pdf")
    meta = reader.metadata

    print(f"Author: {meta.author}")
    print(f"Creator: {meta.creator}")
    print(f"Producer: {meta.producer}")
    print(f"Subject: {meta.subject}")
    print(f"Title: {meta.title}")
    print(f"Creation Date: {meta.creation_date}")
    """)

    # ============================================================================
    # PRACTICAL USE CASES
    # ============================================================================

    print("\n" + "="*60)
    print("PRACTICAL USE CASES (FROM ATBS)")
    print("="*60)

    print("""
    💡 Automation Ideas:

    1. Invoice Processing
       - Extract invoice number, date, total
       - Save to CSV for accounting
       - Validate amounts automatically

    2. Resume Parsing
       - Extract contact info, skills
       - Filter candidates by keywords
       - Batch process applications

    3. Report Data Extraction
       - Pull key metrics from monthly reports
       - Compare data across multiple PDFs
       - Generate summary dashboard

    4. Legal Document Search
       - Search for specific clauses
       - Find all occurrences of terms
       - Extract dates and parties

    5. PDF to Text Conversion
       - Bulk convert PDFs to .txt files
       - Make searchable archives
       - Feed to AI/LLM for analysis

    6. Table Extraction
       - Extract tables from PDFs
       - Convert to CSV/Excel
       - Use tabula-py or camelot libraries
    """)

    # ============================================================================
    # EXAMPLE SCRIPTS
    # ============================================================================

    print("\n" + "="*60)
    print("EXAMPLE: SEARCH THROUGH PDFs")
    print("="*60)

    print("""
    # Find PDFs containing specific text
    from pathlib import Path
    from pypdf import PdfReader

    def search_pdfs(folder, search_term):
        results = []
        for pdf_file in Path(folder).glob("*.pdf"):
            reader = PdfReader(pdf_file)
            for i, page in enumerate(reader.pages):
                text = page.extract_text()
                if search_term.lower() in text.lower():
                    results.append({
                        "file": pdf_file.name,
                        "page": i + 1,
                        "context": text[:200]
                    })
        return results

    # Usage
    matches = search_pdfs("./documents", "invoice")
    for match in matches:
        print(f"{match['file']} - Page {match['page']}")
    """)

    print("\n" + "="*60)
    print("EXAMPLE: EXTRACT TEXT FROM ALL PAGES")
    print("="*60)

    print("""
    def extract_all_text(pdf_path):
        reader = PdfReader(pdf_path)
        full_text = []

        for page in reader.pages:
            full_text.append(page.extract_text())

        return '\\n'.join(full_text)

    # Save to text file
    text = extract_all_text("report.pdf")
    with open("report.txt", "w", encoding="utf-8") as f:
        f.write(text)

    print("✓ Extracted text saved to report.txt")
    """)

    print("\n" + "="*60)
    print("EXAMPLE: BATCH PROCESS INVOICES")
    print("="*60)

    print("""
    import re
    import csv
    from pathlib import Path
    from pypdf import PdfReader

    def extract_invoice_data(pdf_path):
        reader = PdfReader(pdf_path)
        text = reader.pages[0].extract_text()

        # Extract invoice number (example pattern)
        invoice_match = re.search(r'Invoice #(\d+)', text)
        invoice_num = invoice_match.group(1) if invoice_match else "N/A"

        # Extract total (example pattern)
        total_match = re.search(r'Total: \$([0-9,.]+)', text)
        total = total_match.group(1) if total_match else "N/A"

        return {
            "file": pdf_path.name,
            "invoice_num": invoice_num,
            "total": total
        }

    # Process all invoices in folder
    invoices = []
    for pdf in Path("invoices").glob("*.pdf"):
        data = extract_invoice_data(pdf)
        invoices.append(data)

    # Save to CSV
    with open("invoice_summary.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["file", "invoice_num", "total"])
        writer.writeheader()
        writer.writerows(invoices)

    print("✓ Invoice data extracted to CSV")
    """)

    # ============================================================================
    # ADVANCED: TABLE EXTRACTION
    # ============================================================================

    print("\n" + "="*60)
    print("ADVANCED: TABLE EXTRACTION")
    print("="*60)

    print("""
    For extracting tables from PDFs, use specialized libraries:

    1. tabula-py (Java-based, accurate)
       pip install tabula-py

       import tabula
       tables = tabula.read_pdf("document.pdf", pages="all")
       tables[0].to_csv("table_data.csv")

    2. camelot-py (Python-based)
       pip install camelot-py[cv]

       import camelot
       tables = camelot.read_pdf("document.pdf")
       tables[0].to_csv("table_data.csv")

    3. pdfplumber (text + tables)
       pip install pdfplumber

       import pdfplumber
       with pdfplumber.open("document.pdf") as pdf:
           page = pdf.pages[0]
           table = page.extract_table()
           print(table)
    """)

    # ============================================================================
    # INTEGRATION WITH WORKFLOWS
    # ============================================================================

    print("\n" + "="*60)
    print("INTEGRATION WITH BI/AI WORKFLOWS")
    print("="*60)

    print("""
    🔗 PDF → Data Pipeline:

    1. Extract → Transform → Load (ETL)
       - Extract: PDF → Text/Tables
       - Transform: Clean & structure data
       - Load: → CSV → Power BI / Excel

    2. AI/LLM Integration
       - Extract PDF text
       - Send to LLM for summarization
       - Generate insights from documents

    3. Make.com / n8n Automation
       - Trigger: New PDF in folder
       - Action: Extract data with Python
       - Store: Save to database/spreadsheet
       - Notify: Email summary to team

    4. Document Management
       - Auto-categorize PDFs by content
       - Extract metadata for indexing
       - Create searchable archive

    💡 Use Cases for Your Stack:
    - Process supplier invoices → Power BI dashboard
    - Extract report data → Feed to AI for analysis
    - Search contracts → Context for LLM queries
    - Batch convert PDFs → Structured data for ML
    """)

    # ============================================================================
    # LIMITATIONS & TIPS
    # ============================================================================

    print("\n" + "="*60)
    print("LIMITATIONS & TIPS")
    print("="*60)

    print("""
    ⚠️ PDF Extraction Limitations:

    1. Scanned PDFs (Images)
       - Text extraction won't work
       - Need OCR (Optical Character Recognition)
       - Use: pytesseract + pdf2image

    2. Complex Layouts
       - Tables may not extract perfectly
       - Multi-column text can be mixed up
       - Test with your specific PDFs

    3. Protected PDFs
       - Password-protected PDFs need decryption
       - Some PDFs have copy restrictions

    💡 Tips for Better Results:
    - Test extraction on sample PDFs first
    - Use regex for pattern matching (invoice #, dates)
    - Validate extracted data
    - Handle exceptions (corrupted PDFs)
    - Combine multiple libraries for best results
    """)

    print("\n✓ PDF processing concepts covered!")

except ImportError as e:
    print(f"\n✗ Required library not installed: {e}")
    print("""
    Install PDF processing libraries:

    # Option 1: pypdf (recommended, newer)
    pip install pypdf

    # Option 2: PyPDF2 (older, but widely used)
    pip install PyPDF2

    # For table extraction:
    pip install tabula-py      # Requires Java
    pip install camelot-py[cv] # Requires system dependencies
    pip install pdfplumber     # Good balance

    # For OCR (scanned PDFs):
    pip install pytesseract pdf2image
    """)
