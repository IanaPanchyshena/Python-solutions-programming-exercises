# NameSearch7-8
# GirlNames.txt
# This file contains a list of the 200 most popular names given to girls born
# in the United States from the year 2000 through 2009.
# BoyNames.txt
# This file contains a list of the 200 most popular names
# given to boys born in the United States from the year 2000 through 2009.
# Write a program that reads the contents of the two files into two separate
# lists. The user should be able to enter a boy’s name, a girl’s name,
# or both, and the application will display messages indicating
# whether the names were among the most popular.

def get_names(file_name):
    list=[]
    f=open(file_name,'r')
    for line in f:
        list.append(line.rstrip('\n'))
    return list

def main():
    girl_names=get_names('GirlNames.txt')
    boy_names=get_names('BoyNames.txt')

    search=input("Enter a boy's or girl's name: ")
    found=0
    if search in girl_names:
        found=1
        print(search, "is the most popular girl's name")
    if search in boy_names:
        found=1
        print(search, "is the most popular boy's name")
    if found==0:
        print('Name not found')

main()

        
    

