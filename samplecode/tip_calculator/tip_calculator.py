#! /usr/bin/python

#meal = 50
#tax = 6
#tip = 15
meal = float( raw_input("Enter the value of your meal (eg: 33.50 etc): "))
tax = int( raw_input("Enter the tax percent (eg: 3,5 and not 3%,5%): "))
tip = int( raw_input("Enter the tip percent (eg: 10,15 and not 10%, 15%): "))


tax_value = (meal * tax / 100)
meal_with_tax = meal + tax_value
tip_value = (meal_with_tax * tip ) / 100

total = meal_with_tax + tip_value

print "The base cost of your meal was $%s" % meal 
print "You need to pay ${0:.2f} for tax.".format(tax_value)
print "Tipping at a rate of {0}%, you should leave ${1:.2f} for a tip.".format(tip,tip_value)
print "The grand total of your meal is ${0:.2f}".format(total)
