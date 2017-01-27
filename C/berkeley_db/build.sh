#!/usr/bin/env bash

set -e

gcc -c main.c
gcc main.o -ldb -o bdb
rm -f main.o


