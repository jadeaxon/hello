#!/usr/bin/env bash

# Get current month and year.
# month=$(date +%-m) # 1..12
touch foo
month=$(ls -la --time-style +%-m foo | awk '{ print $6 }')
# year=$(date +%Y) # e.g., 2014
year=$(ls -la --time-style +%Y foo | awk '{ print $6 }')
rm foo

# Accept args if supplied.
if [ "$1" ]; then
	month="$1"
fi

if [ "$2" ]; then
	year="$2"
fi

# Report info about each month.
case "$month" in
	1) echo "31 days" ;;
	2)
		# Oversimplification.
		if (( year % 4 == 0 )); then
			echo "Jump for joy!  It's a leap year!"
			echo "29 days"
		else
			echo "28 days"
		fi
		;;

	3) echo "31 days" ;;
	4) echo "30 days" ;;
	5) echo "31 days" ;;
	6) echo "30 days" ;;
	7) echo "31 days" ;;
	8) echo "31 days" ;;
	9) echo "30 days" ;;
	10) echo "31 days" ;;
	11) echo "30 days" ;;
	12) echo "31 days" ;;
	*)
		echo "Invalid month: $month" ;;
esac



