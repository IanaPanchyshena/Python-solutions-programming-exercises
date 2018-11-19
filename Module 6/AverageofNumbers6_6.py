# 6. Average of Numbers
# Assume a file containing a series of integers is named numbers.txt
# and exists on the computer’s disk.
# Write a program that calculates the average of all the numbers
# stored in the file.

def main():
    openFile=open('numbers.txt','r')
    total=0
    counter=0

   
    for line in openFile:
        counter+=1
        total+=int(line)
        average=total/counter
        print(line,end='')
        
    print('The total is',total)
       
    print('The average is',format(average,'.0f'))

    openFile.close()
    
main()
