#!/usr/bin/env python
# One problem with using this portable env-based shebang is that you can't pass options to python.

import os, sys

print "I'm going to fork now.  Whatever I write to stdout will now be filtered by the child."

# Creates a system pipe.
r, w = os.pipe() # these are file descriptors, not file objects

pid = os.fork()
if pid:
    # We are the parent.
    wFile = os.fdopen(w, 'a')
    sys.stdout = wFile

    print >> sys.stderr, 'PARENT (stderr): Created child with pid ' + str(pid) + '.'
    print >> sys.stderr, 'PARENT (stderr): Trying to pipe stuff to child.'
    print "Writing some junk to be filtered by the child process."
    print "Hope he gets this message."
    print "EOF" # Sentinel value.

    wFile.flush()
    wFile.close()
    # os.close(w) # Use os.close() to close a file descriptor.
    os.waitpid(pid, 0) # Make sure the child process gets reaped.
    # os.close(r)
    print >> sys.stderr, 'PARENT (stderr): Reaped child.'
    
    sys.stdout = sys.__stdout__ # Restore original.

else: # We are in the child process.
    print "I am the child process with pid " + str(pid) + "."
    r = os.fdopen(r) # Turn r into a file object.
    # txt = r.read()
    
    while True:
        # Is this blocking?  Seems to be.
        line = r.readline()
        line = line.rstrip()
        
        if line == "EOF":
            print >> sys.__stdout__, "CHILD: Reached EOF sentinel."
            break

        print >> sys.__stdout__, "CHILD: " + line

    # try:
    #    # Filter whatever the parent process writes to the 'w' end of the pipe.
    #    for line in r:
    #        print "CHILD: " + line
    # finally:
    #    r.close()
    
    # r.close()
    # os.close(r)
    
    print >> sys.__stdout__, "CHILD: Exiting."
    sys.exit(0)

print "This should be the parent again."



