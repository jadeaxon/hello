#!/usr/bin/env bash

# Get current month and year.
month=$(date +%-m) # 1..12
year=$(date +%Y) # e.g., 2014

# Accept args if supplied.
if [ "$1" ]; then
	month="$1"
fi

if [ "$2" ]; then
	year="$2"
fi

# $# reports the number of positional args.  This does not include the name of the command as an
# arg.
if (( $# >= 3 )); then
	echo "Usage: months [month] [year]"
	exit 1
fi

# Report info about each month.
if (( month == 1 )); then
	echo "31 days"

elif (( month == 2 )); then

	# Oversimplification.
	if (( year % 4 == 0 )); then
		echo "Jump for joy!  It's a leap year!"
		echo "29 days"
	else
		echo "28 days"
	fi

elif (( month == 3 )); then
	echo "31 days"
elif (( month == 4 )); then
	echo "30 days"
elif (( month == 5 )); then
	echo "31 days"
elif (( month == 6 )); then
	echo "30 days"
elif (( month == 7 )); then
	echo "31 days"
elif (( month == 8 )); then
	echo "31 days"
elif (( month == 9 )); then
	echo "30 days"
elif (( month == 10 )); then
	echo "31 days"
elif (( month == 11 )); then
	echo "30 days"
elif (( month == 12 )); then
	echo "31 days"
else
	echo "Invalid month: $month"

fi


