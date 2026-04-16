#!/usr/bin/env python3

from pathlib import Path

try:
    x = 1 / 0
    y = "string" + 1
except ZeroDivisionError as e:
    print("You can't divide by zero.")
except TypeError as e:
    print(e)
except Exception as e:
    print("Unexpected exception.")
except:
    # Best to avoid using this catchall.
    print("Unexpected exception.")
else:
    print("No exceptions occurred.")
finally:
    print("Always run the finally block.")
print()

# Make your own exceptions.
class ScriptError(Exception): pass
class BadProgrammer(Exception): pass

# Normalize the script's path.
path = Path(__file__).resolve()

try:
    raise ScriptError(f"Error in {path}.")
except ScriptError as e:
    print(e)

try:
    x = 1 / 0
except ZeroDivisionError as e:
    # You can chain exceptions together.
    raise BadProgrammer("bad programmer hard coded a divide by zero") from e


