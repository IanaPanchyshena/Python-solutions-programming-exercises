# Calories_Burned4_2

# Running on a particular treadmill you burn 4.2 calories per minute.
# Write a program that uses a loop to display the number of calories
# burned after 10, 15, 20, 25, and 30 minutes.
# Printe the table headings.
# Print minutes and their calories.



def main():
    
    # Printe the table headings.
    print('Minutes\tCalories')
    print('-------','-------')

    # Print minutes and their calories.
    for num in [10,15,20,25]:
        per_minute=4.2*num
        print(num,'\t',format(per_minute,'.2f'))
    




main()
