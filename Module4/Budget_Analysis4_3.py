# Budget Analysis4_3
# Write a program that asks the user to enter
# the amount that he or she has budgeted for a month.
# A loop should then prompt the user to enter
# each of his or her expenses for the month and keep a running total.
# When the loop finishes, the program should display the amount
# that the user is over or under budget.


def main():
    
    total=0
    expenses=1
    budget=float(input('Enter your Budget for the month: '))
    while expenses!=0:
        expenses=float(input('Enter your Expenses or "0" to quit: '))
        total+=expenses
    left=budget-total
    print('Your Expenses for this month:',format(total,'.2f'))
    print('Money in the Budget :',format(left,'.2f'))
            

main()
