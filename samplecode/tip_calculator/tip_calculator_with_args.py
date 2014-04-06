#! /usr/bin/python

import sys

meal = float(sys.argv[1])
tax = int(sys.argv[2])
tip = int(sys.argv[3])


tax_value = (meal * tax / 100)
meal_with_tax = meal + tax_value
tip_value = (meal_with_tax * tip ) / 100

total = meal_with_tax + tip_value

print "The base cost of your meal was $%s" % meal 
print "You need to pay ${0:.2f} for tax.".format(tax_value)
print "Tipping at a rate of {0}%, you should leave ${1:.2f} for a tip.".format(tip,tip_value)
print "The grand total of your meal is ${0:.2f}".format(total)
