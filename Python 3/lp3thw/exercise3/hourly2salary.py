#!/usr/bin/env python3

# Convert hourly wage to salary.
hours_per_year = 2080
for hourly in range(51):
    salary = hourly * hours_per_year
    print("${0}\t${1}".format(hourly, salary))


