# ============================================================================
# 10. PYTHON MODULES - EXTENDING FUNCTIONALITY
# ============================================================================
# WHAT: Import and use built-in Python modules for extra functionality
# WHY: Leverage pre-built code, avoid reinventing the wheel
# WHEN: Need specific functionality (random numbers, file paths, dates, etc.)

print("Python Built-in Modules Demo")
print("="*50)

# ============================================================================
# RANDOM MODULE - Generate random numbers
# ============================================================================
# WHY: Games, simulations, random sampling, testing

import random

print("\n# RANDOM MODULE")
print("Random integer 1-10:", random.randrange(1, 11))
print("Random choice from list:", random.choice(["red", "blue", "green"]))
print("Random float 0-1:", random.random())
print("Random integer (inclusive):", random.randint(1, 6))  # Like dice roll

# Shuffle a list
cards = ["A", "K", "Q", "J", "10"]
random.shuffle(cards)
print("Shuffled cards:", cards)

# ============================================================================
# OS MODULE - Operating system operations
# ============================================================================
# WHY: Work with files, directories, environment variables

import os

print("\n# OS MODULE")
print("Current directory:", os.getcwd())
print("Files in directory:", len(os.listdir(".")))
print("Operating system:", os.name)  # 'posix' (Mac/Linux) or 'nt' (Windows)

# ============================================================================
# DATETIME MODULE - Working with dates and times
# ============================================================================
# WHY: Timestamps, date calculations, formatting dates

from datetime import datetime, timedelta

print("\n# DATETIME MODULE")
now = datetime.now()
print("Current date/time:", now)
print("Formatted date:", now.strftime("%Y-%m-%d %H:%M"))

# Date arithmetic
tomorrow = now + timedelta(days=1)
print("Tomorrow:", tomorrow.strftime("%Y-%m-%d"))

# ============================================================================
# MATH MODULE - Mathematical functions
# ============================================================================
# WHY: Advanced math operations beyond basic operators

import math

print("\n# MATH MODULE")
print("Square root of 16:", math.sqrt(16))
print("Pi:", math.pi)
print("Ceiling of 4.2:", math.ceil(4.2))
print("Floor of 4.8:", math.floor(4.8))

print("\n# WHY USE MODULES:")
print("# - Don't reinvent the wheel - use tested code")
print("# - Access specialized functionality")
print("# - Keep your code clean and organized")
print("# - Thousands of modules available via pip")
