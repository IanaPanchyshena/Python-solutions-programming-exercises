# Magic Dates3_6
# The date June 10, 1960,
# is special because when it is written in the following format,
# the month times the day equals the year: 6/10/60
# Design a program that asks the user
# to enter a month (in numeric form), a day, and a two-digit year.
# The program should then determine whether
# the month times the day equals the year.
# If so, it should display a message saying the date is magic.
# Otherwise, it should display a message saying the date is not magic


def main():

    month=int(input('Enter month in numeric form: '))
    day=int(input('Enter date of day: '))
    year=int(input('Enter two-digit year: '))
    magic=month*day
    if magic==year:
        print('The date is magic')
    else:
        print('The date is not magic')
main()
