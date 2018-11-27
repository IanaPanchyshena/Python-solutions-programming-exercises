# Rainfall Statistics 7_2

# Design a program that lets the user enter
# the total rainfall for each of 12 months into a list.
# The program should calculate and display the total rainfall for the year,
# the average monthly rainfall,
# the months with the highest
# and lowest amounts. 



def main():
    monthes = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    amount_list=[]
    total=0
    
    print('The total rainfall for each of 12 months.')

    for month in monthes:
        month_amount=float(input(month +': ') )
        amount_list.append(month_amount)

    for amount in amount_list:
        total+=amount

    print('The total rainfall for the year',total)
    print('The avarage monthly rainfall',format(total/12,'.2f'))

    max_rainfall_month = max(amount_list)
    max_index = amount_list.index(max_rainfall_month)
    max_month = monthes[max_index]

    min_rainfall_month = min(amount_list)
    min_index = amount_list.index(min_rainfall_month)
    min_month = monthes[min_index]

    print('The month with highest rainfall', max_month)
    print('The month with lowest rainfall', min_month)
    
    
main()
