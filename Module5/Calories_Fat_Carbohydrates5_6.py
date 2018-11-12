#Calories_Fat_Carbohydrates5_6

# A nutritionist who works for a fitness club helps members
# by evaluating their diets.
# As part of her evaluation, she asks members
# for the number of fat grams and carbohydrate grams that they consumed in a day.

# Then, she calculates the number of calories that result from the fat,
# using the following formula:
# calories from fat=fat grams×9

# Next, she calculates the number of calories that result from the carbohydrates,
# using the following formula:
# calories from carbs=carb grams × 4
# The nutritionist asks you to write a program that will make these calculations.


def main():
    number_fat=float(input('Enter number of fat grams that consumed in a day: '))
    number_carb=float(input('Enter number of carbohydrate grams'+
                                'that consumed in a day: '))

    calories_fat=get_calories_fat(number_fat)
    calories_carbs=get_calories_carbs(number_carb)

    print('The number of calories that result from the fat: ',calories_fat)
    print('The number of calories that result from the carbohydrates: ', calories_carbs)
    

def get_calories_fat(fat):
    return fat*9

def get_calories_carbs(carb):
    return carb*4


main()
