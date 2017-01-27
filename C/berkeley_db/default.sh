#!/usr/bin/env bash

set -o pipefail

./build.sh |& tee build.out
if (( $? != 0 )); then
	vim -q build.out
else
	rm -f build.out
fi

