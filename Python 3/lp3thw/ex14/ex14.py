#!/usr/bin/env python3

# Import argument variable (vector) from the sys module.
from sys import argv
# Unpack the args.
script, user_name, prompt = argv
# Use a custom prompt.
prompt = f"{prompt}> "

# Introduce script.
print(f"Hi, {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")

# Ask user if he likes the script.
print(f"Do you like me {user_name}?")
likes = input(prompt)

# Ask where user lives.
print(f"Where do you live {user_name}?")
lives = input(prompt)

# Ask for computer type.
print("What kind of computer do you have?")
computer = input(prompt)

# Main output.
print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}.  Not sure where that is.
And you have a computer.  Nice.
""")

