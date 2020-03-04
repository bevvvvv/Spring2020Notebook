"""
CMPSC 101 HW4
The purpose of this program is to take a recipe as input in order to
determine how much of each ingredient is needed for the specified number of servings.

DO NOT DUPLICATE FOR EDUCATIONAL PURPOSES ONLY
"""

print('This is a recipe scaler for serving large crowds!')
print('Enter one ingredient per line, with a numeric value first.')
print('Indicate the end of input with an empty line.')

quants = {}
units = {}

# get input
while True:
    line = input()
    if line.strip() == '':
        break
    quant, unit, item = line.split(' ', 2) # first two are quant and unit, item can have space
    if item in quants.keys():
        continue # likely unnecessary
    quants[item] = quant
    units[item] = unit

# print recipe recorded
for item in quants.keys():
    quant = quants[item]
    unit = units[item]
    print("%5s %10s %s" % (quant, unit, item))

# get scalar
recipe_servings = int(input('How many does this recipe serve? '))
required_servings = int(input('How many people must be served? '))
scalar = (required_servings // recipe_servings)
# round up
if required_servings % recipe_servings != 0:
    scalar += 1

print('Multiplying the recipe by ',scalar)

# output new recipe amounts
for item in quants.keys():
    quant = quants[item]
    unit = units[item]
    if '/' in quant:
        numer, slash, denom = quant.partition('/')
        quant = str(scalar * int(numer)) + slash + denom
    else:
        quant = str(scalar * int(quant))
    print("%5s %10s %s" % (quant, unit, item))