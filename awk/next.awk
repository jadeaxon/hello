#!/usr/bin/awk -f

# Convert these kind of input records to the kind shown below.
# Username:Firstname:Lastname:Telephone number

# dn: uid=Username, dc=example, dc=com
# cn: Firstname Lastname
# sn: Lastname
# telephoneNumber: Telephone number

# The 'next' command skips all remaining rules for the current record.

BEGIN { IFS=":" }
/^$/ { next } # Skip blank lines.
{ print "dn: uid=" $1 ", dc=example, dc=com" }
{ print "cn: " $2, $3 }
{ print "sn: " $3 }
{ print "telephoneNumber: " $4 }
{ print "" } # Prints a single newline.





