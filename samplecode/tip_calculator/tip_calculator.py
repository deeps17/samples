#! /usr/bin/python

meal = 50
tax = 6
tip = 15

tax_value = (meal * tax / 100)
meal_with_tax = meal + tax_value
tip_value = (meal_with_tax * tip ) / 100

total = meal_with_tax + tip_value

print "The base cost of your meal was $%s" % meal 
print "You need to pay $ %.2f" % tax_value , " for tax."
print "Tipping at a rate of %s" % tip , '%%, you should leave $ %.2f' % tip_value , ' for a tip.'
print "The grand total of your meal is $%.2f" % total
