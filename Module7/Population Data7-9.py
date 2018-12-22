# Population Data7-8
# USPopulation.txt 
# The file contains the midyear population of the United States,
# in thousands, during the years 1950 through 1990.
# The first line in the file contains the population for 1950,
# the second line contains the population for 1951, and so forth.
# Write a program that reads the file’s contents into a list.
# The program should display the following data:
# The average annual change in population during the time period
# The year with the greatest increase in population during the time period
# The year with the smallest increase in population during the time period

import random
def create_file():
    file=open('USPopulation.txt','w')
    for line in range(40):
        number=random.randint(300000,350000)
        file.write(str(number)+'\n')
    file.close()

def main():
    #create_file()
    population_list=[]
    file=open('USPopulation.txt','r')
    
    

main()
