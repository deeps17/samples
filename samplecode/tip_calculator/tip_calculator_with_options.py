#! /usr/bin/python

from optparse import OptionParser

parser = OptionParser()

parser.add_option("-m", "--meal", dest="meal", help="base price of your meal", type="float")
parser.add_option("-t", "--tax", dest="tax", help="the tax percent (eg: 5 and not 5%)", type="int")
parser.add_option("-p", "--tip", dest="tip", help="the tip percent (eg: 5 and not 5%)", type="int")

#meal = float( sys.argv[1] )
#tax = int( sys.argv[2] ) 
#tip = int( sys.argv[3] )

(options, args) = parser.parse_args()

if not (options.meal):
	parser.error("You forgot to put the base cost of the meal")
if not (options.tax):
	parser.error("You forgot to put the percent tax")
if not (options.tip):
	parser.error("You forgot to put the percent tip")

tax_value = (options.meal * options.tax / 100)
meal_with_tax = options.meal + tax_value
tip_value = (meal_with_tax * options.tip ) / 100

total = meal_with_tax + tip_value

print "The base cost of your meal was $%s" % options.meal 
print "You need to pay ${0:.2f} for tax.".format(tax_value)
print "Tipping at a rate of {0}%, you should leave ${1:.2f} for a tip.".format(options.tip,tip_value)
print "The grand total of your meal is ${0:.2f}".format(total)
