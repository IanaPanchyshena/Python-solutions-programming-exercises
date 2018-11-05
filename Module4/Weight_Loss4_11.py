# Weight_Loss4_11
# If a moderately active person cuts their calorie intake by 500 calories a day,
# they can typically lose about 4 pounds a month.
# Write a program that lets the user enter their starting weight,
# then creates and displays a table showing what their expected weight will be
# at the end of each month for
# the next 6 months if they stay on this diet.


def main():
    
  
    weight=float(input('Enter your starting weight: '))
    loss=4
    print('Month num\Weight')
    for month in range(6):
        weight-=loss
        print(month+1,'\t',weight)


main()
