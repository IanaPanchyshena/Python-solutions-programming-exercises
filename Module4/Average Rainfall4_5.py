# Average Rainfall4_5
# Write a program that uses nested loops to collect data and calculate
# the average rainfall over a period of years.
# The program should first ask for the number of years.
# The outer loop will iterate once for each year.
# The inner loop will iterate twelve times, once for each month.
# Each iteration of the inner loop will ask the user for
# the inches of rainfall for that month.
# After all iterations, the program should display the number of months,
# the total inches of rainfall, and the average rainfall
# per month for the entire period.


def main():
    
    total_month=0
    total_inch=0
    num_years=int(input('Enter the number of years: '))
    for years in range (1,num_years+1):
        for month in range(1,13):
            rain_month=int(input('Enter the inches of  ' +\
                           'rainfall for that month '+format(month,'d')+':'))
            total_inch+=rain_month
            total_month+=1
    average=total_inch/total_month
    print('Number of month: ',total_month)
    print('Total inches of rainfall: ',format(total_inch,'.2f'))
    print('Average rainfall per month for the entire period: ', format(average,'.2f'))



main()
