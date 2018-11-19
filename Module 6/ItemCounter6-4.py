# ItemCounter6-4

# Assume a file containing a series of names (as strings) is named names.txt
# and exists on the computer’s disk.
# Write a program that displays the number of names that are stored in the file.
# (Hint: Open the file and read every string stored in it.
# Use a variable to keep a count of the number of items
# that are read from the file.)

def main():
    contents=open('names.txt','r')
    line=contents.readline()
    counter=0

    while line!='':
        print(line,end='')
        line=contents.readline()
        counter+=1
        
    print('Total:',counter, 'names')
        
    
main()

                                                                                                                                                                                                             
