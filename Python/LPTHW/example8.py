# Use a formatter string with print to run various values through it.
formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing.",
    "That you could type up right.",
    "But it didn't sing.", # A bit strange here.
    "So, I said goodnight."
) # print



