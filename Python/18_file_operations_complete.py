# ============================================================================
# 18. FILE OPERATIONS - COMPREHENSIVE REFERENCE
# ============================================================================
# WHAT: Read, write, and manage files using Python
# WHY: Store data, read configuration, log information, process files
# WHEN: Need persistent storage, data processing, configuration management

import os

# ============================================================================
# FILE MODES
# ============================================================================

print("="*60)
print("FILE MODES OVERVIEW")
print("="*60)

print("""
File Opening Modes:

'r'  - Read (default) - Error if file doesn't exist
'w'  - Write - Creates file or overwrites existing
'a'  - Append - Creates file or appends to existing
'x'  - Create - Error if file exists
'r+' - Read and Write
'w+' - Write and Read (overwrites)
'a+' - Append and Read

Additional modes:
't'  - Text mode (default)
'b'  - Binary mode (for images, etc.)

Examples: 'rb', 'wt', 'ab'
""")

# ============================================================================
# CREATING AND WRITING FILES
# ============================================================================

print("="*60)
print("CREATING AND WRITING FILES")
print("="*60)

# Write mode - creates file or overwrites existing
print("\n1. Write mode ('w'):")
with open("demo.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a test file.\n")
print("File 'demo.txt' created and written")

# Append mode - adds to end of file
print("\n2. Append mode ('a'):")
with open("demo.txt", "a") as file:
    file.write("This line was appended.\n")
print("Content appended to 'demo.txt'")

# Create mode - error if file exists
print("\n3. Create mode ('x'):")
try:
    with open("newfile.txt", "x") as file:
        file.write("This is a new file.\n")
    print("File 'newfile.txt' created")
except FileExistsError:
    print("File 'newfile.txt' already exists")

# Writing multiple lines
print("\n4. Writing multiple lines:")
lines = [
    "Line 1\n",
    "Line 2\n",
    "Line 3\n"
]
with open("multiline.txt", "w") as file:
    file.writelines(lines)
print("Multiple lines written to 'multiline.txt'")

# ============================================================================
# READING FILES
# ============================================================================

print("\n" + "="*60)
print("READING FILES")
print("="*60)

# Read entire file
print("\n1. Read entire file:")
with open("demo.txt", "r") as file:
    content = file.read()
    print(content)

# Read specific number of characters
print("2. Read first 10 characters:")
with open("demo.txt", "r") as file:
    content = file.read(10)
    print(f"'{content}'")

# Read one line
print("\n3. Read one line:")
with open("demo.txt", "r") as file:
    line = file.readline()
    print(f"First line: {line}", end="")

# Read all lines as list
print("\n4. Read all lines as list:")
with open("demo.txt", "r") as file:
    lines = file.readlines()
    print(f"Total lines: {len(lines)}")
    for i, line in enumerate(lines, 1):
        print(f"  Line {i}: {line}", end="")

# Loop through file line by line (memory efficient)
print("\n5. Loop through file:")
with open("demo.txt", "r") as file:
    for i, line in enumerate(file, 1):
        print(f"  {i}: {line}", end="")

# ============================================================================
# THE with STATEMENT
# ============================================================================

print("\n" + "="*60)
print("THE 'with' STATEMENT")
print("="*60)

print("""
# WHY USE 'with':
- Automatically closes file (even if error occurs)
- Cleaner code
- Prevents resource leaks

# Without 'with':
file = open("file.txt", "r")
content = file.read()
file.close()  # Must remember to close

# With 'with':
with open("file.txt", "r") as file:
    content = file.read()
# File automatically closed here
""")

# ============================================================================
# FILE EXISTENCE AND PROPERTIES
# ============================================================================

print("="*60)
print("FILE EXISTENCE AND PROPERTIES")
print("="*60)

# Check if file exists
filename = "demo.txt"
if os.path.exists(filename):
    print(f"✓ File '{filename}' exists")

    # Check if it's a file (not directory)
    if os.path.isfile(filename):
        print(f"  ✓ It's a file")

    # Get file size
    size = os.path.getsize(filename)
    print(f"  Size: {size} bytes")

else:
    print(f"✗ File '{filename}' does not exist")

# ============================================================================
# DELETING FILES
# ============================================================================

print("\n" + "="*60)
print("DELETING FILES")
print("="*60)

# Safe file deletion with existence check
def safe_delete(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print(f"✓ Deleted: {filename}")
    else:
        print(f"✗ File not found: {filename}")

# Create and delete test file
with open("temp.txt", "w") as f:
    f.write("Temporary file")

safe_delete("temp.txt")
safe_delete("nonexistent.txt")

# ============================================================================
# DIRECTORY OPERATIONS
# ============================================================================

print("\n" + "="*60)
print("DIRECTORY OPERATIONS")
print("="*60)

# Create directory
test_dir = "test_directory"
if not os.path.exists(test_dir):
    os.mkdir(test_dir)
    print(f"✓ Created directory: {test_dir}")

# Check if path is directory
if os.path.isdir(test_dir):
    print(f"  ✓ '{test_dir}' is a directory")

# List files in directory
print(f"\nFiles in current directory:")
files = os.listdir(".")
for f in files[:5]:  # Show first 5
    print(f"  - {f}")

# Delete directory (must be empty)
try:
    os.rmdir(test_dir)
    print(f"\n✓ Deleted directory: {test_dir}")
except OSError as e:
    print(f"\n✗ Cannot delete directory: {e}")

# ============================================================================
# WORKING WITH FILE PATHS
# ============================================================================

print("\n" + "="*60)
print("WORKING WITH FILE PATHS")
print("="*60)

# Get current working directory
cwd = os.getcwd()
print(f"Current directory: {cwd}")

# Join paths (OS-independent)
file_path = os.path.join("folder", "subfolder", "file.txt")
print(f"Joined path: {file_path}")

# Get absolute path
abs_path = os.path.abspath("demo.txt")
print(f"Absolute path: {abs_path}")

# Split path into directory and filename
directory, filename = os.path.split(abs_path)
print(f"Directory: {directory}")
print(f"Filename: {filename}")

# Get filename without extension
name, ext = os.path.splitext(filename)
print(f"Name: {name}, Extension: {ext}")

# ============================================================================
# BINARY FILES
# ============================================================================

print("\n" + "="*60)
print("BINARY FILES")
print("="*60)

# Writing binary data
print("Writing binary file:")
data = bytes([65, 66, 67, 68, 69])  # ASCII: ABCDE
with open("binary.dat", "wb") as file:
    file.write(data)
print("Binary file created")

# Reading binary data
print("\nReading binary file:")
with open("binary.dat", "rb") as file:
    binary_content = file.read()
    print(f"Binary data: {binary_content}")
    print(f"As string: {binary_content.decode('ascii')}")

# Clean up
safe_delete("binary.dat")

# ============================================================================
# PRACTICAL EXAMPLES
# ============================================================================

print("\n" + "="*60)
print("PRACTICAL EXAMPLES")
print("="*60)

# Example 1: Read and count words in file
print("\n1. Word counter:")
with open("demo.txt", "w") as f:
    f.write("Python is awesome. Python is powerful. Python is easy.")

with open("demo.txt", "r") as file:
    content = file.read()
    word_count = len(content.split())
    print(f"Total words: {word_count}")

# Example 2: Copy file
print("\n2. Copy file:")
def copy_file(source, destination):
    with open(source, "r") as src:
        content = src.read()
    with open(destination, "w") as dst:
        dst.write(content)
    print(f"Copied '{source}' to '{destination}'")

copy_file("demo.txt", "demo_copy.txt")

# Example 3: Log file
print("\n3. Log file:")
import datetime

def log_message(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("app.log", "a") as log:
        log.write(f"[{timestamp}] {message}\n")

log_message("Application started")
log_message("User logged in")
log_message("Data processed")

print("Log entries written to 'app.log'")
with open("app.log", "r") as log:
    print("Log contents:")
    print(log.read())

# Example 4: Configuration file
print("\n4. Configuration file:")
config = {
    "server": "localhost",
    "port": 8080,
    "debug": True
}

# Write config
with open("config.txt", "w") as f:
    for key, value in config.items():
        f.write(f"{key}={value}\n")

# Read config
with open("config.txt", "r") as f:
    print("Configuration:")
    for line in f:
        print(f"  {line}", end="")

# ============================================================================
# ADVANCED FILE/FOLDER MANAGEMENT (FROM ATBS)
# ============================================================================

print("\n" + "="*60)
print("ADVANCED FILE/FOLDER OPERATIONS")
print("="*60)

print("""
💡 From Automate the Boring Stuff:
- Moving files with shutil
- Copying files and folders
- Walking directory trees
- Pathlib for modern path handling
""")

# ============================================================================
# SHUTIL MODULE - ADVANCED FILE OPERATIONS
# ============================================================================

import shutil

print("\n1. SHUTIL - Copy and Move Files:")

# Create test file
with open("original.txt", "w") as f:
    f.write("This is the original file.")

# Copy file
shutil.copy("original.txt", "copied.txt")
print("✓ Copied original.txt → copied.txt")

# Move/Rename file
shutil.move("copied.txt", "moved.txt")
print("✓ Moved copied.txt → moved.txt")

# Copy with metadata (timestamps, permissions)
shutil.copy2("original.txt", "copied_with_metadata.txt")
print("✓ Copied with metadata")

# ============================================================================
# WALKING DIRECTORY TREES (os.walk)
# ============================================================================

print("\n2. WALKING DIRECTORY TREES (os.walk):")
print("""
Use case: Find all .txt files in current and subdirectories
Perfect for: Batch operations, searching, organizing files
""")

# Create test directory structure
os.makedirs("test_walk/subfolder", exist_ok=True)
with open("test_walk/file1.txt", "w") as f:
    f.write("test")
with open("test_walk/subfolder/file2.txt", "w") as f:
    f.write("test")

# Walk through directory tree
txt_files = []
for folder, subfolders, files in os.walk("test_walk"):
    for file in files:
        if file.endswith(".txt"):
            full_path = os.path.join(folder, file)
            txt_files.append(full_path)
            print(f"  Found: {full_path}")

print(f"Total .txt files found: {len(txt_files)}")

# ============================================================================
# PATHLIB - MODERN PATH HANDLING (Python 3.4+)
# ============================================================================

print("\n3. PATHLIB - Modern Path Handling:")
from pathlib import Path

print("""
Why Pathlib?
- Object-oriented approach to paths
- Cross-platform (Windows/Linux/Mac)
- Easier to read and use
- Replaces many os.path functions
""")

# Create Path object
current_dir = Path.cwd()
print(f"Current directory: {current_dir}")

# Path operations
file_path = Path("test_walk") / "file1.txt"
print(f"File path: {file_path}")
print(f"  Exists: {file_path.exists()}")
print(f"  Is file: {file_path.is_file()}")
print(f"  Name: {file_path.name}")
print(f"  Suffix: {file_path.suffix}")
print(f"  Parent: {file_path.parent}")

# Glob with pathlib
print("\n4. Finding files with Pathlib glob:")
txt_files = list(Path("test_walk").rglob("*.txt"))
print(f"Found {len(txt_files)} .txt files:")
for f in txt_files:
    print(f"  {f}")

# ============================================================================
# SAFE FILE OPERATIONS
# ============================================================================

print("\n5. SAFE FILE OPERATIONS:")

def safe_move_files_by_extension(source_dir, dest_dir, extension):
    """Move all files with given extension to destination"""
    Path(dest_dir).mkdir(exist_ok=True)

    moved_count = 0
    for file in Path(source_dir).rglob(f"*.{extension}"):
        dest_path = Path(dest_dir) / file.name
        shutil.move(str(file), str(dest_path))
        print(f"  Moved: {file.name} → {dest_dir}/")
        moved_count += 1

    return moved_count

# Example: Move all .txt files to backup folder
# count = safe_move_files_by_extension("test_walk", "backup_folder", "txt")
# print(f"Total files moved: {count}")

print("""
💡 Automation Ideas:
1. Organize downloads folder by file type
2. Backup files modified today
3. Find duplicate files by size/name
4. Clean old temporary files
5. Batch rename files with pattern
""")

# Cleanup demo files
print("\n\nCleaning up demo files...")
demo_files = ["demo.txt", "demo_copy.txt", "newfile.txt", "multiline.txt", "app.log", "config.txt", "original.txt", "moved.txt", "copied_with_metadata.txt"]
for f in demo_files:
    safe_delete(f)

# Clean up test directories
import shutil as sh
for folder in ["test_walk", "test_directory"]:
    if os.path.exists(folder):
        sh.rmtree(folder)
        print(f"Deleted folder: {folder}")
