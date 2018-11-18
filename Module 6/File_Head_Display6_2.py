# File_Head_Display6_2

# Write a program that asks the user for the name of a file.
# The program should display only the first five lines of the file’s contents.
# If the file contains less than five lines,
# it should display the file’s entire contents.

def main():
    name_file=input('Enter the name of file: ')
    file=open(name_file,'r')
    
    for i in range(1,6):
        line=file.readline()
        if line=='':
            break
        print(line,end='')
        
        
    file.close()

main()
