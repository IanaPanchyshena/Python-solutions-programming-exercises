# Roulette_Wheel_Colors3_9 

def main():
    pockets_number=int(input('Enter number from 0 to 36: '))

    if pockets_number==0:
        print('Pockets are green')
    elif pockets_number>=1 and pockets_number<=10:
        if pockets_number%2==0:
            print('Pockets are black!')
        else:
            print('Pockets red')
    elif pockets_number>=11 and pockets_number<=18:
        if pockets_number%2==0:
            print('Pockets are red!')
        else:
            print('Pockets are black')
    elif pockets_number>=19 and pockets_number<=28:
        if pockets_number%2==0:
            print('Pockets are black!')
        else:
            print('Pockets are red')
    elif pockets_number>=29 and pockets_number<=36:
        if pockets_number%2==0:
            print('Pockets are red!')
        else:
            print('Pockets are black!')
    else:
        print('You should enter number from 0 to 36 ')
            


main()
