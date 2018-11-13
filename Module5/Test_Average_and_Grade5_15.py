# Test_Average_and_Grade5_15

# Write a program that asks the user to enter five test scores.
# The program should display a letter grade for each score
# and the average test score.
# Write the following functions in the program: calc_average.
# This function should accept five test scores as arguments and return the
# average of the scores.

# determine_grade.
# This function should accept a test score as an argument
#and return a letter grade for the score based on the following grading scale:
# Score Letter Grade
#90–100 A / 80–89 B/  70–79 C / 60–69 D / Below 60F

number=5

def main():
    total=0
    for i in range(1,number+1):
        test=int(input('Enter the test score '+format(i,'d')+':'))
        
        grade=determine_grade(test)
        print('Grade is ',grade)
        total+=test
        
        
    average=calc_average(total)
    print('Average score is :',average,'%','and grade is',determine_grade(average))
    
def calc_average(test):
    return test/number 
        
def determine_grade(test):
    if test >90 and test<=100:
        return 'A'
    elif test>80 and test<=90:
        return 'B'
    elif test>70 and test<=79:
        return 'C'
    elif test>60 and test<=69:
        return 'D'
    else:
        return 'F'

main()
