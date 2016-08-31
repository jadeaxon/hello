#!/usr/bin/env bash

set -e

# Q. Does this blow up if a subshell exits nonzero?
# A. Yes, the subshell failure does halt it.
fail=$(echo Hi; false) || true
echo "Subshell fail halts me, but I can use || true to get around it."
echo "fail = $fail"


