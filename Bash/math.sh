#!/usr/bin/env bash

# You can put arithmetic expressions inside $(( )).
echo $(( 100 / 3 ))
echo $(( 11 * 11 ))

myvar="56"
echo $(( $myvar + 12 ))
echo $(( $myvar - $myvar ))

myvar=$(( $myvar + 1 ))
echo $myvar
