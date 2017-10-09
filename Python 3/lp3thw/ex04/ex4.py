#!/usr/bin/env python3

# Total number of cars.
cars = 100
# Number of people, including driver, each car can hold.
space_in_a_car = 4.0
# Number of drivers.
drivers = 30
# Number of passengers.
passengers = 90
# Cars not driven due to lack of drivers.
# Where's my self-driving car Google, Apple, etc.?
cars_not_driven = cars - drivers
# Number of cars actually driven.
cars_driven = drivers
# Total person transportation capacity of the carpool.
carpool_capacity = cars_driven * space_in_a_car
# Average number of passengers in each car.
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")

print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")

