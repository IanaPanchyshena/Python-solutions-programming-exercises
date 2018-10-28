# PlantingGrapevines2_13

def main():
    # ask to enter lenght_row, space_for_assembly,space_between_vines.
    lenght_row=float(input('Enter lenght of the row in feet: '))
    space_for_assembly=float(input('Enter amount of space used by an end-post assembly: '))
    space_between_vines=float(input('Enter amount of space between the vines, in feet: '))

    # calculate by formula V=R-2ES.
    number_grapevines=lenght_row-2*(space_for_assembly*space_between_vines)

    # dispaly the result #The number of grapevines that will fit in the row.
    print('The number of grapevines that will fit in the row: ',format(number_grapevines,'.0f'))
main()
