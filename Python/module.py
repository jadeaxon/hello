#!/usr/bin/env python

# When you import a module, you use its name with no .py extension.
# This imports everything from module into this script (namespace).  Well, it imports the namespace into this namespace.
# It does not merge them.
#
# What does Python use as its PERL5LIB/CLASSPATH mechanism?
# Whatever it uses, it looks in the current directory (the one your launched the script from).
#
# Environment variable PYTHONPATH is used to locate a module.  If not set, something like .:/usr/local/lib/python
# is generally used by default.  If you import sys, the value is sys.path.
import user_module

import sys
print "Python will load modules from %s" % sys.path
print

# This form of import is like Java's 'import static'.  It imports names directly into this namespace, merging.
# It does not import names beginning with _.  These are considered private by convention.
from user_module import *

# If you just do a regular import, you have to prefix function calls with the module name.
# So, it is not like a 'import static' in Java.
name = user_module.module_function()

name = module_function()
print name
print

# When a .py file is run as a script, its module name, __name__, is set to "__main__".  Thus, you can detect if your
# file is being run as a script or imported as a module.
if __name__ == "__main__":
    print "I was invoked as a script."
else:
    print "I was imported as a module."
print

# Whatever executable content you have in your file is executed only once globally the first time the module is imported.
# It acts like static initializer blocks in Java.

# You can compile .py modules using the 'compileall' command.  This creates .pyc files.  They load faster but do not 
# exectue faster.  Well, I can't find the command in my installation.

# If you would like to know all the names/symbols defined in a module, use the 'dir' function.
print "Module user_module contains the following:"
print dir(user_module)
print

# List everything in this module.
print "Module " + __name__ + " contains the following:"
print dir()
print

# List all of Python's built-ins.
print "Here is a list of all of Python's built in things:"
print dir(__builtins__)
print



