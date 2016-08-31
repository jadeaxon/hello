#!/usr/bin/env python

# This is the modern commandline argument/option parser.  It supercedes optparse and getopt.
# It still has some warts, but they will probably get fixed eventually.
# I can't get it to do exactly what I want, but I guess it's better than rolling your own.
import argparse

# A module for pretty printing data.
import pprint

import math

printer = pprint.PrettyPrinter(indent=4)

# Define a hash to translate crap lowercase that is bugging me in argparse.
lookup = {
    "usage: ": "Usage: ",
    "optional arguments": "Options",
    "positional arguments": "Arguments",
    "[--file FILES]": "[--file FILES]...", # This one doesn't work.
}

# Define a function that uses the transation hash.
def gettext(s):
    return lookup.get(s, s)

# Some kind of voodoo that splices the function/method into the argparse module.
argparse._ = gettext


#-------------------------------------------------------------------------------
# DEFINE COMMANDLINE ARGUMENTS
#-------------------------------------------------------------------------------

# First, you create a parser.
# The %(prog)s format specifier is available to fill in the program name in your usage messages.
parser = argparse.ArgumentParser(
    description='Either finds the maximum of or sums a list of integers.',
    epilog='This gets displayed after the option help.',
    # usage='%(prog)s [--sum] N [N...]', # You can use superfluous trailing commas.  Nice.
    formatter_class=argparse.RawTextHelpFormatter,
    add_help=False,
)

# The -h and --help options are defined by default.

# "%(variable)s" - interpolates variable inside double quotes as a string; like "$variable" or "${variable}" in Perl,
# Obviously, this doesn't work quite like I think it does.
# You still have to use "formatter" % (var1, ..., varN) or "formatter" % hash() to interpolate/format variables,
# The string arg passed to the method below must get interpolated deeper in the code.
#
# Add an option to print out the program's version.
version_number = "O.1"
parser.add_argument(
    '--version',
    action='version',
    # FAIL: version="%(prog)s %(version_number)s",
    version="%(prog)s version " + str(version_number),
    help='Print this program\'s version and exit.',
)


# Override the default help options.
# The reason I don't use the default is because it uses a brain-dead all lowercase help string.
parser.add_argument(
    '--help',
    '-h',
    action='help',
    help='Print detailed program help and exit.',
)


parser.add_argument(
    '--value', # How this option must appear on the commandline.
    metavar='V', # Use V in usage statement instead of VALUE.
    required=True, # This 'option' is not optional.
    action='store', # This is the default action.
    nargs=1, # This is probably the default.
    default=None, # This is the default default value.
    type=int, # The type of the option's value.
    help='A numeric value.', # Option specific help message.
)

# This is how to do a simple true/false flag.
parser.add_argument(
    '--flag',
    default=False,
    action='store_true',
    # nargs=0, # You can't specify this directly, but it seems to be the default.
    help='Turn the flag --flag on.',
)


# This option stores a constant value if present.
parser.add_argument(
    '--constant',
    action='store_const',
    const=42, # This value is used with _const actions.
    help='Store 42 in --constant option.'
)

# Next, you use add_argement to tell it about the options and arguments you expect on the commandline.
parser.add_argument(
    'integers', # Internal field name to use in parsing result object.
    metavar='N', # Placeholder in usage/help output.
    type=int, # This arg is an integer.
    nargs='+', # There must be one or more of this kind or arg.
    help='An integer for the accumulator.' # Option-specific help message to print.
)

# --file file1.ext --file file2.ext will make a list of files stored in a field called 'files'.
parser.add_argument(
    '--file',
    action='append',
    dest='files',
    help='Creates a list of file.  Use --file multiple times.',
)

parser.add_argument(
    '--sum', # Option as it should appear on commandline.
    dest='accumulate', # Name of field/method in parse result object.
    action='store_const', # ?
    const=sum, # The sum built-in should be used.  Not sure how it knows exactly when to use this.
    default=max, # Function to use if --sum is not specified.
    help='Sum the integers (default: find the max).'
)


# You can define custom actions via classes that implement argparse.Action.
class CustomAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        # print '%r %r %r' % (namespace, values, option_string)
        print 'Hello, custom action!'
        setattr(namespace, self.dest, values)

parser.add_argument(
    '--custom',
    action=CustomAction,
    nargs=1,
    help='Demonstrates custom argument processing.',
)
        

# You can add your own custom argument types.  You just need a function (callable) that takes a string, returns
# a string, and throw an exception if the value is invalid.
#
# Here we define an option whose value must be a perfect square.

def perfect_square(string):
    value = int(string)
    sqrt = math.sqrt(value)
    if sqrt != int(sqrt):
        msg = "%r is not a perfect square." % string
        raise argparse.ArgumentTypeError(msg)
    return value


parser.add_argument(
    '--psquare', 
    nargs=1,
    type=perfect_square,
    help='The value must be a perfect square.',
)


# You can add groups of mutually exclusive (xor) options.
# You can specify that choosing one is required.
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('--chocolate', action='store_true') # Each one defaults to false automatically.
group.add_argument('--vanilla', action='store_true')
group.add_argument('--strawberry', action='store_true')


# You can also have options or arguments whose values have to come from a restricted set of choices.
parser.add_argument('--choice', nargs=1, choices=['cheaper', 'faster', 'better'])


#-------------------------------------------------------------------------------
# MAIN
#-------------------------------------------------------------------------------

# Parsing the commandline creates an object.  Usually a Namespace object.
# The object contains a field for each argument added to the parser.
# It appears the field can actually be a method.  Or a list.
#
# This module does respect that -- on commandline ends option parsing for current command.
args = parser.parse_args() # Automatically uses sys.argv if nothing passed in.

# Now that we've parsed the commandline, we can start getting down to business.
# The next thing you'd typically do is read in environment variables and configuration files.
# Then, you'd do whatever main processing task you want to do now that your complete context is known.

print args.accumulate(args.integers)
if args.flag:
    print '--flag true'
else:
    print '--flag false'

# Well, looks like Namespace objects don't pretty print.  More fundamental Python types do.
# However, the vars function seems to return a hash, which does pretty print.
printer.pprint(vars(args))


