#!/usr/bin/env python

import pickle

# Open a file for writing.
f = open('hello_file.py', 'r') 
print f

# Slurp.
contents = f.read()
print len(contents)

print

# Write back out every line in the file.
f.seek(0) # Rewind back to the first byte.
for line in f:
    print line,

# Use a while loop and readline method to do the same thing less concisely.
f.seek(0)
while True:
    line = f.readline()
    if line == "": break
    print line,
    
f.close()

f = open('temporary.tmp', 'w')
f.write("This will be written to the temp file.\n")
f.close()


# This automatically closes the file after using even if exceptions occur.
# Therefore, it is the prefered way to work with files.
with open('temporary.tmp', 'r') as f:
    contents = f.read()
    print contents,


# For writing complex data to files, Python uses a module named 'pickle'.  You pickle and unpickle things.
# This is essentially the same as Java serialization.
aHash = {'key': 'value'}
with open('pickled.obj', 'w') as f:
    pickle.dump(aHash, f)

aHash = None
with open('pickled.obj', 'r') as f:
    aHash = pickle.load(f)
    print aHash

    

