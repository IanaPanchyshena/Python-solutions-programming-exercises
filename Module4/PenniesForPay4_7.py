# Pennies for Pay4_7
# Write a program that calculates the amount of money
# a person would earn over a period of time if his or her salary is one penny
# the first day, two pennies the second day, and continues to double each day.
# The program should ask the user for the number of days.
# Display a table showing what the salary was for each day,
# then show the total pay at the end of the period.
# The output should be displayed in a dollar amount, not the number of pennies.

def main():
    salary=0.01
    total=0
    num_days=int(input('Enter the number of days: '))
    print('Day\tSalary')
    print('--------------')
    print()
    for days in range(num_days):
        salary=2**days
        print(days+1,'\t',salary)

        total+=salary
        total_dol=total*0.01
    print('Total pay $', total_dol)


main()
  
