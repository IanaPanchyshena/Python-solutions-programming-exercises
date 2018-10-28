#Day_of_the_Week3_1
def main():
#start program
    
    # assign all variables for numbers from 1-7
    Monday=1
    Tuesday=2
    Wednesday=3
    Thursday=4
    Friday=5
    Saturday=6
    Sunday=7
    # ask user to enter number in the range from 1 to 7
    today_day=int(input('Enter the number in the range from 1 to 7: '))
    # determines corresponding day for number that user entered
    if today_day==1:
        print('Monday')
    elif today_day==2:
        print('Tuesday')
    elif today_day==3:
        print('Wedneday')
    elif today_day==4:
        print('Thursday')
    elif today_day==5:
        print('Friday')
    elif today_day==6:
        print('Saturday')
    elif today_day==7:
        print('Sunday')
    else:
        print('Error message')
            
#end program
main()
