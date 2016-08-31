#!/usr/bin/env python

# Python uses try/except/finally syntax.  It is very similar to Java exception handling.
# Python defines a number of built in exception classes (like Java does).

# Prompt user for a number until you get a valid response.
prompt = "Please enter a number: "
while True:
    try:
        response = raw_input(prompt)
        number = int(response)
        break # If we reach here, we got a good value since no exception was thrown.
    
    # Only the first matching except block will be executed when an exception is thrown.
    # If no exception is thrown, they are all ignored.  
    # The finally block executes last whether or not an exception was thrown.
    #
    # You can use an 'as' clause to name the caught exception.
    except EOFError as eof:
        print
        print "Goodbye!"
        exit(0)

    except ValueError:
        print "Error: '{0}' is not a number.".format(response)
    
    # With no argument, 'except' catches everything.
    # With no argument, 'raise' rethrows the caught exception.
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise

    # Just like in Java, the finally block is always executed.
    finally:
        pass

print "You entered {0}.".format(number)


# You can define and raise your own exceptions.
class CustomException(Exception):
    """User defined exception class."""
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return repr(self.value)


raise CustomException("A user defined exception class instance was thrown.")



