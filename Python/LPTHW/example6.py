x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

# Apparently the %r interpolation of a string puts single quotes around it.
# Perhaps %r means "representation".
print "I said: %r." % x

# Whereas the %s does not.
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

# The + operator is overloaded to concatenate strings.
print w + e

