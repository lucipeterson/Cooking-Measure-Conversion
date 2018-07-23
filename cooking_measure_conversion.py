#cooking_measure_conversion.py
from fractions import Fraction
from sympy import collect, simplify

conversion_dict = {"tablespoons": 0.015, "ounces": 0.060, "cups": 0.250, "pints": 0.500, "quarts": 0.950, "gallons": 3.800,"tablespoon": 0.015, "ounce": 0.060, "cup": 0.250, "pint": 0.500, "quart": 0.950, "gallon": 3.800}
c = conversion_dict

start_units = input("What type of unit do you want to convert? ")
while start_units not in conversion_dict:
    start_units = input("What type of unit do you want to convert? ")
	
amount = int(input("How many? "))

end_units = input("What type of unit do you want to convert to?")

def gcd(x, y):
	gcd = 1
    
	if x % y == 0:
		return y
    
	for k in range(int(y / 2), 0, -1):
		if x % k == 0 and y % k == 0:
			gcd = k
			break  
	return gcd

if start_units == "tablespoons":
	print (str(c[start_units]*amount/c[end_units]) + end_units)
elif start_units == "ounces":
	print (c[start_units]*amount/c[end_units])
elif start_units == "cups":
	print (c[start_units]*amount/c[end_units])
elif start_units == "pints":
	print (c[start_units]*amount/c[end_units])
elif start_units == "quarts":
	print (c[start_units]*amount/c[end_units])
while start_units == "gallons":
	print (c[start_units]*amount/c[end_units])
	break
	

