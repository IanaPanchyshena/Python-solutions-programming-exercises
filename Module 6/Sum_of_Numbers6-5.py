# Sum_of_Numbers6-5

# Assume a file containing a series of integers is named numbers.txt
# and exists on the computer’s disk.
# Write a program that reads all of the numbers
# stored in the file and calculates their total.

def main():
    openFile=open('numbers.txt','r')
    total=0

   
    for line in openFile:
        total+=int(line)
        print(line,end='')
            
    print('The total is',total)

    openFile.close()
    
main()
