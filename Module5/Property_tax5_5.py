# Property_Tax5_5

# A county collects property taxes on the assessment value of property,
# which is 60 percent of the property’s actual value.
# For example, if an acre of land is valued at $10,000,
# its assessment value is $6,000.
# The property tax is then 72¢ for each $100 of the assessment value.
# The tax for the acre assessed at $6,000 will be $43.20.
# Write a program that asks for the actual value of a piece
# of property and displays the assessment value and property tax.


def main():

    actual_value=float(input('Actual value of a piece of property: '))
    assesment_value=get_assesment_value(actual_value)
    property_tax=get_property_tax(assesment_value)
    print('The assessment value: $',assesment_value)
    print('Property tax: $',format(property_tax,'.2f'))


def get_assesment_value(value):
    return value*0.6

def get_property_tax(value):
    return value/100*0.72


main()
