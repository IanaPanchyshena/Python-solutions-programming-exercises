# Paint_Job_Estimator5_8

# A painting company has determined
# that for every 112 square feet of wall space,
# one gallon of paint and eight hours of labor will be required.
# The company charges $35.00 per hour for labor.
# Write a program that asks the user to enter
# the square feet of wall space to be painted and the price of the paint per gallon.
# The program should display the following data:
# The number of gallons of paint required
# The hours of labor required
# The cost of the paint
# The labor charges
# The total cost of the paint job

def main():
    wall_space=float(input('Enter the square feet of wall space: '))
    price_paint=float(input('Enter the price of the paint per gallon: '))

    number_paint=get_number_paint(wall_space)
    hours_labor=get_hours_labor(wall_space)
    cost_paint=get_cost_paint(number_paint,price_paint)
    labor_charges=get_labor_charges(hours_labor)
    total_cost=get_total_cost(cost_paint,labor_charges)

    print('The number of gallons of paint required: ', format(number_paint,'.2f'))
    print('The hours of labor required: ', format(hours_labor,'.2f'))
    print('The cost of the paint: $', format(cost_paint,'.2f'),sep='')
    print('The labor charges: $',format(labor_charges,'.2f'),sep='')
    print('The total cost of the paint job: $',format(total_cost,'.2f'),sep='')

def get_number_paint(space):
    return space/112
def get_hours_labor(space):
    return space/112*8
def get_cost_paint(number_paint,price_paint):
    return number_paint*price_paint
def get_labor_charges(hours):
    return hours*35
def get_total_cost(paint,labor):
    return paint+labor

main()
