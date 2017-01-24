#!/usr/bin/env bash

# PRE: You are building this in Cygwin.
# PRE: libnicethings.dll.a is deployed to /usr/local/lib
# PRE: libnicethings' headers are deployed to /usr/local/include
# PRE: Your PATH contains /usr/local/lib (when you try to run client or server).

set -e 

# This seems to be able to find the Nice Things headers in /usr/local/include.
gcc -c server.c 

# This does not seem to be able to find the lib in /usr/local/lib. 
# However, it can find it in /usr/lib (at compile time).
gcc server.o -L/usr/local/lib -lnicethings -o server

# At runtime, Cygwin somewhat insanely uses PATH env var to find *libraries*!
# So, you need:
# export PATH=$PATH:/usr/local/lib


