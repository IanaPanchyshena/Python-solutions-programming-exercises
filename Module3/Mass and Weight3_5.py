# Mass and Weight3_5

# Scientists measure an object’s mass in kilograms and its weight in newtons.
# If you know the amount of mass of an object
# in kilograms, you can calculate its weight in newtons
# with the following formula: weight=mass×9.8
# Write a program that asks the user to enter an object’s mass,
# then calculates its weight.
# If the object weighs more than 500 newtons,
# display a message indicating that it is too heavy.
# If the object weighs less than 100 newtons,
# display a message indicating that it is too light.

def main():
# start program

    mass=float(input('Enter mass in kilograms: '))
    weight=mass*9.8
    if weight>500:
        print(weight,'newtons','- that it is too heavy')
    else:
        if weight<100:
            print(weight,'newtons','- is too light')

# end program
main()
