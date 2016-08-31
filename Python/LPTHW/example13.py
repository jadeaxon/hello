from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "cla => commandline argument"
print "cla[0] =", script
print "cla[1] =", first
print "cla[2] =", second
print "cla[3] =", third
print

answer = raw_input("What is your name? ");
print "So, %s, you think you know about commandline arguments." % answer

