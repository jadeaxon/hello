#!/usr/bin/awk -f

# awk => Alfred Aho, Peter Weinberger, and Brian Kernighan.
# <condition> { <command> }

# awk breaks down text files into records that are then broken down further into fields.

# BEGIN fires once before records are processed.
BEGIN { print "Hello, awk!" }

# A line with no condition triggers for all records.
# The default awk program is to simple print back out all incoming records.
# Huh, it appears that I am wrong.  So, let's explicitly do this.
{ print $0 }

# To suppress this implicit command, use the -n option.

# END fires once after all records are processed.
END { print "Goodbye, cruel world!" }

