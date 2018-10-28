#IngredientAdjuster2_10

def main():
    # ask the user how many cookies he or she wants to make.
    x=float(input('How many cookies do you want to make? '))

    # assign variables to sugar,butter,flour.
    sugar=1.5
    butter=1
    flour=2.75

    # calculate number of cups each ingredients for one cookies.
    sugar48=1.5/48
    butter48=1/48
    flour48=2.75/48

    # calculate number of cups each ingredients for the specified number of cookies.
    sugar_x=sugar48*x
    butter_x=butter48*x
    flour_x=flour48*x

    # print result.
    print('You needed this ingredients:')
    print('sugar:',format(sugar_x,'.2f'),'cups')
    print('butter:',format(butter_x,'.2f'),'cups')
    print('flour:',format(flour_x,'.2f'),'cups')

main()

