# Stadium_Seating5_7
# There are three seating categories at a stadium.
# Class A seats cost $20,
# Class B seats cost $15,
# and Class C seats cost $10.
# Write a program that asks how many tickets for each class of seats were sold,
# then displays the amount of income generated from ticket sales.

a=20
b=15
c=10

def main():
   
    sold_a=int(input('Enter how many tickets class A were sold: '))
    sold_b=int(input('Enter how many tickets class B were sold: '))
    sold_c=int(input('Enter how many tickets class C were sold: '))


    total_sold=get_total_sold(sold_a,sold_b,sold_c)
    print('The amount of income generated from tickets sales: $',total_sold)


def get_total_sold(sold_a,sold_b,sold_c):
    return sold_a*a+sold_b*b+sold_c*c
                     


main()
