#!/usr/bin/env bash

# To bulid up libraries of common functions, just shove all related functions in a file.
# Then call 'source <function_library>.sh' from your script.
# Shove all this in SVN under something like /utility/bash/*.sh.  Now you can factor your code.
# Make a .deb package that deploys it to /usr/src/bash_utilities/*.sh.
# Or /usr/src/bash/lib/*.sh.  Mimic how Perl stores its modules.


# This is the most portable syntax for declaring functions.
# The function declaration must precede its use.
#
# A function is called in the same process as its caller.
# Therefore, changes to environment variables remain visible to caller when function returns.
# Use 'local' to declare local variables.  Changes are only visible to function and functions it calls.
# That is, anything above it on call stack does not see changes, but anything below it does (unless they use local).

# The first element of the FUNCNAME variable is set to the currently executing function's name.
# FUNCNAME is kind of like a function call stack.
# Thus, you can write code conditional on caller/callee/args.  But not object type (no objects)
# or arg type (since args don't really have type).

# Functions receive args as positional parameters via $1, $2, etc. $# and $@.
# $0 remains the name of the parent script.

# If you redefine a function, the new definition is used an no warning is given.

# type <function name> prints out the source code of just that function.

# A sourced file acts kind of like a nameless function.
# The 'return' statement can only be used in functions and sourced files.


# You can define functions in bash.
# They act more like separate scripts than functions.
# You call them just as if you were invoking a script.
# They use the same $1, $2, etc. and $@ variables to get their args.

# All variables declared in bash are global non-exported by default.  Even in functions.
# To declare a local function variable, preceded it with 'local'.

custom_function() {
    local quantity=20
    echo I would like $quantity ${1}s.
}


custom_function pie


#===============================================================================
# Defining Functions
#=============================================================================== 

# A function must be defined before it can be used.
# There are no function declarations as in C.
# Redefining a function simply overwrites it with new definition w/o warning.
# 'type <function name>' prints out a function's current source.
# Bash appears to have no namespace features.


example_function() {
	# Call to external commands (subshells) can't change directories in this script.
	# A user-defined function can.
	cd ~


	# Calling code will see the change to this environment variable on return.
	ENV_VAR="change visible to caller"

	# Set interfield separator to . locally.
	# 'local' works as it does in Perl: Called functions see the change; caller does not.
	local IFS=.

	# Local probably protects existing variables in the caller scope.  So, it is a good
	# idea to use it with all your function variables unless you clearly intend to mutate
	# an existing variable or return a value to the caller scope.
	#
	# A function automatically gets local versions of $1, $2, etc.
	#
	# There is no syntax for accessing shadowed variables in outer scopes.

	# Variables are either local or global (default).  A global variable can further be exported.
	# An exported variable will be copied to a subprocess once.  When the subprocess alters this copy,
	# this has no effect on the original version in the parent.

	echo "Called example_function()."

	return 0

}



# If you use () instead of {} to create function block, the function gets executed in a subshell instead of in the same
# process.
#
# In Cygwin, this does not happen.  I get same process id in both.
subshell_invoking_function() (
	echo "Executing user-defined function in subshell with process id $$."

)


output_redirecting_function() {
	echo "This will print to /dev/fd/1 (stdout) by default."
	echo "If an argument, \$1, is passed to function, output will go to that file." 
	echo "The redirection is evaluated at runtime."

} > ${1:-/dev/fd/1} 



#===============================================================================
# Exit Status and Return Values
#===============================================================================

# The return values in bash are unsigned bytes, 0 .. 255.
# A return value of 0 indicates success.  Any other value indicates an error.
# If you need to return some other type of value, use a global environment variable.
# 0 is implicitly returned if you don't use a return statement.
#
# So, in bash logic, 0 is true and everything else is false!
# If you want to use C-style logic, use (( )) context.
#
# These are not really return values.  They are exit statuses.  To return an actual value
# you either write it to a specific variable or write it to stdout.
# The last return/exit value is stored in special variable $?.  You must use $? immediately
# else the next command will overwrite it.
#
# $result would be a good convention for a place to store a return value from a function.
#
# If you don't use an explicit return, the return value of the last statement executed in
# the function is returned.
#
# A function does not "throw and exception" if one of its statements returns non-zero.
# It is up to you to check all exit statuses.

exit_status_vs_return_value() {
	result='Return value.' # Return a value via a global variable.
	echo "$result" # And/or return a value by printing it to stdout.
	return 1; # Return an exit status via a return statement.
}


return_value=$(exit_status_vs_return_value)
if (( $? == 0 )) {
	echo "Success!"
}
echo "$result"




#===============================================================================
# Calling Functions
#===============================================================================


# Notice that when you call a function, you don't use parenthesis. 
# You invoke it as if it were just another commandline command.
example_function
echo "Parent process id $$."
subshell_invoking_function

# A function can be called recursively.  That is, a function can call itself.



