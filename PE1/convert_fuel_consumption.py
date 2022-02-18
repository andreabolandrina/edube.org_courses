#!/usr/bin/env python3

# 4.3.1.10 LAB: Converting fuel consumption
# 
# A car's fuel consumption may be expressed in many different ways. 
# For example, in Europe, it is shown as the amount of fuel consumed per 100 kilometers.
# 
# In the USA, it is shown as the number of miles traveled by a car using one gallon of fuel.
# 
# Your task is to write a pair of functions converting l/100km into mpg, and vice versa.

# The functions:
#     are named liters_100km_to_miles_gallon and miles_gallon_to_liters_100km respectively;
#     take one argument (the value corresponding to their names)

# Here is some information to help you:
#     1 American mile = 1609.344 metres;
#     1 American gallon = 3.785411784 litres.

def liters_100km_to_miles_gallon(liters):
    gallons = liters / 3.785411784
    miles = 100 / 1.609344
    return miles / gallons

def miles_gallon_to_liters_100km(miles):
    liters = 3.785411784
    km = miles * 1.609344
    liter_per_km = liters / km
    return liter_per_km * 100
    

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
