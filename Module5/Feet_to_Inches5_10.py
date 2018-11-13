# Feet_to_Inches5_10

# The Feet to Inches Problem One foot equals 12 inches.
# Write a function named feet_to_inches that accepts a number of feet
# as an argument and returns the number of inches in that many feet.
# Use the function in a program that prompts the user
# to enter a number of feet then displays
# the number of inches in that many feet.

# COnstant for the number of inches per foot.
INCHES_PER_FOOT=12

def main():
    # Get a number of feet from the user.
    feet=int(input('Enter a number of feet: '))

    # Convert that to inches.
    print(feet,'equals',feet_to_inches(feet),'inches.')

# The fee_to_inches function converts feet to inches.
def feet_to_inches(feet):
    return feet*INCHES_PER_FOOT

# Call the main function.
main()

