# ============================================================================
# 21. CLIPBOARD AUTOMATION - COPY/PASTE PROGRAMMATICALLY
# ============================================================================
# WHAT: Automate clipboard operations (copy/paste) using Python
# WHY: Quick data transfer, automate repetitive copy-paste tasks
# WHEN: Form filling, data transfer between apps, quick text manipulation
# NOTE: Requires pyperclip - install with: pip install pyperclip

print("="*60)
print("CLIPBOARD AUTOMATION WITH PYPERCLIP")
print("="*60)

try:
    import pyperclip

    print("""
    💡 What is Pyperclip?
    - Cross-platform clipboard access (Windows, Mac, Linux)
    - Copy text to clipboard programmatically
    - Paste (read) text from clipboard
    - Perfect for automation workflows
    """)

    # ============================================================================
    # BASIC OPERATIONS
    # ============================================================================

    print("\n" + "="*60)
    print("BASIC CLIPBOARD OPERATIONS")
    print("="*60)

    # Copy to clipboard
    pyperclip.copy("Hello from Python!")
    print("✓ Copied: 'Hello from Python!' to clipboard")

    # Paste from clipboard
    text = pyperclip.paste()
    print(f"✓ Pasted from clipboard: '{text}'")

    # ============================================================================
    # PRACTICAL USE CASES
    # ============================================================================

    print("\n" + "="*60)
    print("PRACTICAL USE CASES")
    print("="*60)

    # Use Case 1: Quick Email Template
    print("\n1. Email Template Generator:")
    def create_email_template(name, product):
        template = f"""
    Dear {name},

    Thank you for your interest in {product}.
    We'll get back to you within 24 hours.

    Best regards,
    The Team
    """
        pyperclip.copy(template)
        print(f"✓ Email template copied to clipboard!")
        print(f"  Recipient: {name}")
        print(f"  Product: {product}")

    create_email_template("Alice", "Premium Plan")

    # Use Case 2: Password Generator
    print("\n2. Password Generator:")
    import random
    import string

    def generate_password(length=12):
        chars = string.ascii_letters + string.digits + "!@#$%"
        password = ''.join(random.choice(chars) for _ in range(length))
        pyperclip.copy(password)
        return password

    pwd = generate_password(16)
    print(f"✓ Generated password copied to clipboard: {pwd[:4]}...{pwd[-4:]}")

    # Use Case 3: Text Formatting
    print("\n3. Text Formatter (Uppercase):")
    def format_to_uppercase():
        text = pyperclip.paste()
        formatted = text.upper()
        pyperclip.copy(formatted)
        print(f"✓ Converted to uppercase: '{formatted}'")

    pyperclip.copy("convert this to uppercase")
    format_to_uppercase()

    # Use Case 4: Add Bullet Points
    print("\n4. Add Bullet Points to List:")
    def add_bullets(items):
        bulleted = '\n'.join(f"• {item}" for item in items)
        pyperclip.copy(bulleted)
        print("✓ Bulleted list copied to clipboard:")
        print(bulleted)

    add_bullets(["Python", "JavaScript", "SQL"])

    # ============================================================================
    # AUTOMATION WORKFLOWS
    # ============================================================================

    print("\n" + "="*60)
    print("AUTOMATION WORKFLOWS (FROM ATBS)")
    print("="*60)

    print("""
    💡 Clipboard Automation Ideas:

    1. Multi-Clipboard Manager
       - Store multiple clipboard items
       - Recall previous copies with keyboard shortcut
       - Clipboard history

    2. Data Transfer Between Apps
       - Copy from Excel → Format → Paste to Email
       - Extract data from PDF → Process → Copy result

    3. Form Auto-Fill
       - Read clipboard → Validate → Fill form fields
       - Pre-fill repetitive form data

    4. Text Processing Pipeline
       - Copy text → Clean/Format → Paste back
       - Remove extra spaces, fix capitalization
       - Convert formats (Markdown → HTML, etc.)

    5. Code Snippet Manager
       - Quick access to code templates
       - Copy boilerplate code
       - Insert frequently used snippets

    6. Integration with Make.com/n8n
       - Webhook receives data → Copy to clipboard
       - User pastes into target application
       - Manual step in automation workflow
    """)

    # ============================================================================
    # ADVANCED EXAMPLE: MULTI-CLIPBOARD
    # ============================================================================

    print("\n" + "="*60)
    print("ADVANCED: MULTI-CLIPBOARD STORAGE")
    print("="*60)

    print("""
    Example: Store multiple clipboard items
    Usage: python script.py save <label>
           python script.py load <label>
    """)

    # Simple multi-clipboard implementation
    import json
    from pathlib import Path

    def save_clipboard(label):
        clipboard_data = {}
        storage_file = Path("clipboard_storage.json")

        # Load existing data
        if storage_file.exists():
            with open(storage_file, "r") as f:
                clipboard_data = json.load(f)

        # Save current clipboard
        clipboard_data[label] = pyperclip.paste()

        # Write back
        with open(storage_file, "w") as f:
            json.dump(clipboard_data, f, indent=4)

        print(f"✓ Saved clipboard as '{label}'")

    def load_clipboard(label):
        storage_file = Path("clipboard_storage.json")

        if not storage_file.exists():
            print("✗ No saved clipboards found")
            return

        with open(storage_file, "r") as f:
            clipboard_data = json.load(f)

        if label in clipboard_data:
            pyperclip.copy(clipboard_data[label])
            print(f"✓ Loaded '{label}' to clipboard")
        else:
            print(f"✗ Label '{label}' not found")

    # Demo
    pyperclip.copy("Important email template")
    save_clipboard("email_template")

    pyperclip.copy("SQL query for reports")
    save_clipboard("sql_query")

    load_clipboard("email_template")
    print(f"  Clipboard now contains: '{pyperclip.paste()}'")

    # Cleanup
    if Path("clipboard_storage.json").exists():
        Path("clipboard_storage.json").unlink()
        print("\nCleaned up: clipboard_storage.json")

    # ============================================================================
    # INTEGRATION TIPS
    # ============================================================================

    print("\n" + "="*60)
    print("INTEGRATION WITH YOUR WORKFLOW")
    print("="*60)

    print("""
    🔗 Combine with:

    1. Keyboard Shortcuts (PyAutoGUI)
       - Trigger clipboard operations with hotkeys
       - Auto-paste after copying

    2. Web Scraping
       - Scrape data → Copy to clipboard → Paste to Excel

    3. File Processing
       - Read file → Process → Copy result to clipboard

    4. API Integration
       - API response → Format → Copy to clipboard

    5. Scheduled Tasks
       - Daily summary → Copy to clipboard at 9am
       - Reminder with pre-filled text

    ⚠️ Security Note:
    - Don't copy sensitive data (passwords) unnecessarily
    - Clear clipboard after sensitive operations
    - Be aware clipboard is accessible by other apps
    """)

except ImportError:
    print("✗ pyperclip not installed")
    print("Install with: pip install pyperclip")
    print("""
    Alternative clipboard libraries:
    - xerox (cross-platform)
    - clipboard (simpler API)
    - tkinter (built-in, GUI-based)
    """)
