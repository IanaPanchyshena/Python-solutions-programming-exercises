# Time_Calculator3_16
# Write a program that asks the user
# to enter a number of seconds and works as follows:

# There are 60 seconds in a minute.
# If the number of seconds entered by the user is greater than or equal to 60,
# the program should convert the number of seconds to minutes and seconds.

# There are 3,600 seconds in an hour.
# If the number of seconds entered by the user is greater
# than or equal to 3,600, the program should convert the number of seconds to hours, minutes, and seconds .

# There are 86,400 seconds in a day.
# If the number of seconds entered by the user is greater than or equal to 86,400,
# the program should convert the number of seconds to days, hours, minutes, and seconds.

def main():
    # ask user to enter a number of seconds.
    seconds=int(input('Enter a number of seconds: '))

    # add 3 conditions if >= 60; if >=3600; if >=86.400
    # print the result
    
    if seconds>=60 and seconds<3600:
       minutes=seconds//60
       seconds=seconds%60
       print('It is',minutes,'minutes and',seconds,'seconds')
    elif seconds>=3600 and seconds<=86400:
       hours=seconds//3600
       minutes=hours%60
       seconds=seconds%60
       print('It is',hours,'hours,',minutes,'minutes and',seconds,'seconds')
    elif seconds>=86400:
       days=seconds//86400
       hours=days%3600
       minutes=hours%60
       seconds=seconds%60
       print('It is',days,'days',hours,'hours,',minutes,'minutes and',seconds,'seconds')

main()
