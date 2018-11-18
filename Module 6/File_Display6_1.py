# File_Display6_1

def main():
    # Open the file.
    myfile=open('numbers.txt','r')
    # For each line the file:
    # Read line and display it.
    for line in myfile:
        number=int(line)
        print(number)
        

# Close the file.
main()
