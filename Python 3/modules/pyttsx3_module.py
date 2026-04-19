#!/usr/bin/env python3

# The newer version breaks!!!
# PRE: pip3 install pyttsx3==2.91

import sys
import pyttsx3

if sys.platform != 'win32':
    print(f"ERROR: This won't run anywhere but directly on Windows: {sys.platform}.")
    sys.exit()

engine = pyttsx3.init()
engine.say('Hello. All my drive-bys be shootings.')
engine.runAndWait()  # The computer speaks.

# A line from the nonsense generator.
engine.say("The diseased jar of mayo patiently formatted the thirsty enchillada.")
engine.runAndWait()

