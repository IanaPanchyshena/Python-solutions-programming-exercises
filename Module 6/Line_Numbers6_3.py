# Line_Numbers6_3
# Write a program that asks the user for the name of a file.
# The program should display the contents of the file with each line preceded
# with a line number followed by a colon.
# The line numbering should start at 1.
# (lineNumbers.txt)

def main():
    fileName=input('Please enter a name a file: ')
    print()
    openFile=open(fileName,'r')
    line=openFile.readline()
    lineNumber=1
    
    while line!='':
        print(str(lineNumber)+':',line.rstrip('\n'))
        line=openFile.readline()
        lineNumber+=1
        

main()
