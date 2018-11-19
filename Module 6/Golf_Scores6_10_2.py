# Golf_Scores6_10_2

# The Springfork Amateur Golf Club has a tournament every weekend.
# The club president has asked you to write two programs:

# 2. A program that reads the records from the golf.txt
# file and displays them.


def main():
    file=open('golf.txt','r')
    name=file.readline()
    print('Name','Score')
    print('-----','----')

    while name!= '':
        score=file.readline()
        print(name.rstrip('\n'),'-',score.rstrip('\n'))
        name=file.readline()


    file.close()
main()
        


    
