# Falling_Distance5_13

# When an object is falling because of gravity,
# the following formula can be used to determine the distance
# the object falls in a specific time period: d=12gt2

# The variables in the formula are as follows:
# d is the distance in meters,
# g is 9.8,
# and t is the amount of time, in seconds, that the object has been falling.

# Write a function named falling_distance that accepts
# an object’s falling time (in seconds) as an argument.

# The function should return the distance, in meters,
# that the object has fallen during that time interval.

# Write a program that calls the function in a loop
# that passes the values 1 through 10 as arguments
# and displays the return value.


g=9.8
def main():
    
    for falling_time in range (1,10):
        falling_distance=get_falling_distance(falling_time)
        print('Time\tDistance')
        print(falling_time,'\t',format(falling_distance,'.1f'))
        print()

def get_falling_distance(falling_time):
    return 1/2*g*(falling_time**2)

main()
