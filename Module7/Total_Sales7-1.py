# Total Sales7-1
# Design a program that asks the user to enter a store’s sales for each day
# of the week. The amounts should be stored in a list.
# Use a loop to calculate the total sales for the week and display the result. 




def main():
    week_days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    amount_list=[]
    total=0
    print("Enter a store's sales for each day of the week.")

    for day_sale in week_days:
        day_sales=float(input(day_sale+': ') )
        amount_list.append(day_sales)

    for day_sale in amount_list:
        total+=day_sale
        
    print('The total sales for the week',total)
    
main()
