# ColorMixer3_7

# The colors red, blue, and yellow are known as the primary colors
# because they cannot be made by mixing other colors.
# When you mix two primary colors, you get a secondary color, as shown here:
# When you mix red and blue, you get purple.
# When you mix red and yellow, you get orange.
# When you mix blue and yellow, you get green.
# Design a program that prompts the user to enter
# the names of two primary colors to mix.
# If the user enters anything other than “red,” “blue,” or “yellow,”
# the program should display an error message.
# Otherwise, the program should display the name of the secondary color
# that results.

def main():
    color=input('Enter one of the three colors: red, blue, yellow: ')
    color2=input('Enter one of the three colors: red, blue, yellow: ')
    if color=='red' and color2=='blue' or\
       color=='blue' and color2=='red':
        print('You get the purple color')
    elif color=='yellow' and color2=='red' or\
         color=='red' and color2=='yellow':
        print('You get the orange color')
    elif color=='blue' and color2=='yellow' or\
         color=='yellow' and color2=='blue':
        print('You get the green color!')
    else:
        print(color2)

main()
