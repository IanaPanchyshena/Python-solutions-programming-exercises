#Odd_Even Counter5_16
# In this chapter, you saw an example of how to write an algorithm that determines
# whether a number is even or odd. Write a program that generates 100 random numbers
# and keeps a count of how many of those random numbers are even,
# and how many of them are odd.

import random
def main():
    even_number=0
    odd_number=0
    
    for i in range (1,101):
        number=random.randint(0,101)
        print(number,end=' ')
        if(even_odd_count(number)== True):
            even_number+=1
        else:
            odd_number+=1
    print()
    print(even_number,'numbers are even and', odd_number,'numbers are odd!')
            

def even_odd_count(number):
    return number%2==0
        
    
    



main()
