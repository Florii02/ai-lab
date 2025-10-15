# ============================================================================
# 7. AUTOMATION - BATCH FILE RENAMING
# ============================================================================
# WHAT: Automatically rename multiple files based on pattern
# WHY: Rename hundreds of files in seconds, maintain naming conventions
# WHEN: Organizing photos, cleaning up downloads, standardizing file names

import os

print("Batch File Renaming Example")
print("="*50)

# Example: Rename all .txt files to file_0.txt, file_1.txt, etc.
# CAUTION: This modifies actual files - use carefully!

# enumerate() gives us both index and value
for count, filename in enumerate(os.listdir(".")):
    # Check if file matches criteria
    if filename.endswith(".txt") and not filename.startswith("file_"):
        new_name = f"file_{count}.txt"
        # os.rename(filename, new_name)  # Commented out for safety
        print(f"Would rename: {filename} -> {new_name}")

print("\n# WHY USE THIS:")
print("# - Rename hundreds of files instantly")
print("# - Add prefixes, suffixes, or dates to file names")
print("# - Clean up messy download folders")
print("# - Standardize naming conventions across projects")
