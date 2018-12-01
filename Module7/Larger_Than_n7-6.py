# Larger_Than_n7-6
# In a program, write a function that accepts two arguments: a list,
# and a number n. Assume that the list contains numbers.
# The function should display all of the numbers in the list
# that are greater than the number n.

def main():
    number=int(input('Enter the number: '))
    list_num=[1,2,3,4,66,55,44,77,88,99,57]
    print('Numbers in the list taht are greater than',number)

    funct(list_num,number)
    
def funct(list_num,number):
    for num in list_num:
        if num > number:
            print(num)
        
main()
