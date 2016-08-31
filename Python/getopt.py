#!/usr/bin/env python

# The getopt module parses commandline arguments.
import getopt, sys, os

def main():
    try:    
        # getopt.getopt returns two values: the hash of parsed options and the remaining commandling args list.
        # sys.argv[1:] means "parse all the commandline args".  Note that sys.argv[0] is the command's name.
        # The second arg to getopt is short options.  Letters with a colon after them require an argument.
        # The third arg to getopy is long options.  Long options needing an argument have a = after them.
        # 
        # On the commandline, you write a short option a -o (one dash) and a long option as --long (two dashes).
        opts, args = getopt.getopt(sys.argv[1:], "ho:v", ["help", "version", "output="])
    except getopt.GetoptError, err:
        # If options parsing fails, print usage information and exit:
        print str(err) # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    
    # Set script state based on parsed options.
    output = None
    verbose = False
    for option, argument in opts:
        if option == "-v":
            verbose = True
        elif option == "--version":
            print "hello_getopt version 0.001"
            sys.exit()
        elif option in ("-h", "--help"):
            help()
            sys.exit()
        elif option in ("-o", "--output"):
            output = argument
        else:
            assert False, "unhandled option"
    
    
def usage():
    script_name = os.path.basename(__file__)
    print "Usage: %s OPTIONS ARGUMENTS..." % script_name
    print "Type '%s --help' for more information." % script_name

help_string = """
This is the long help message.  It tells you how to use the command.
I am not sure how to use variable interpolation inside a here document
(aka, document string) like you can in Perl.  Also, you need to somehow
remove the first newline from this string.

"""    
    
def help():
    global help_string
    # Need to remove extra newline from top of string.
    print help_string
    

# Not sure what this means.
if __name__ == "__main__":
    main()
    
    
print "Rest of script?"    