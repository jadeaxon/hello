#!/usr/bin/env bash

read -p "Age? " age
if (( age < 21 )); then
	(( years_until_drink = 21 - age ))
	echo "You need to wait $years_until_drink years before you can legally drink."
else
	(( years = (age - 21) + 1 ))
	(( liters = years * 100 ))
	echo "You can legally drink.  However, this does not mean it is a good idea."
	echo "Statistically, you have drunk $liters liters of beer so far."
fi


