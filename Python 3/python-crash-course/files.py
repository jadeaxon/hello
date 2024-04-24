from pathlib import Path

# Read data from a text file.

# The Visual Studio Code terminal runs from your home directory, not the directory where this file lives.
# Let's get the directory where this file lives.
import os, sys
file_dir = os.path.dirname(__file__)
print(file_dir)

# You can use / in paths on Windows too.
file = Path(f'{file_dir}\data.txt')
characters = file.read_text()
lines = characters.splitlines()

for character in characters:
    print(character)

for line in lines:
    print(line)

# If you have numbers, use int() or float() to convert the strings you read in from the file.

# Output to a file.
file = Path(f'{file_dir}\output.txt')
file.write_text('This is what we will write to the file.')

contents = ""
contents += "Let's build up some content.\n"
contents += "To write to the file.\n"
contents += "This will overwrite whatever was in there.\n"
file.write_text(contents)





