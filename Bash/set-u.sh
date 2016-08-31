#!/usr/bin/env bash

set -u # Do not allow undefined vars.
# set -x

# Q. How do we check if a var is undefined w/ blowing up set -u?
# + expands to alt if var is both set and not empty.  Else becomes nothing.
# XT_PLAYER_IFACE=eth0
if [ ! -n "${XT_PLAYER_IFACE+1}" ]; then
	echo "Var undefined.  Setting."
	XT_PLAYER_IFACE=eth1
else
	echo "Already defined."
fi
echo "$XT_PLAYER_IFACE"


DEFAULT=bar

arg_test() {
	local foo=${1:-$DEFAULT}
	echo $foo
}

# Q. Can a var expand into the default and satisfy -u?
# A. Yes.
arg_test




