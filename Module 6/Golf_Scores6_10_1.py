# Golf_Scores6_10_1

# The Springfork Amateur Golf Club has a tournament every weekend.
# The club president has asked you to write two programs:

# 1. A program that will read each player’s name and golf score
# as keyboard input, then save these as records in a file named golf.txt.
# Each record will have a field for the player’s name and a field for
# the player’s score.)


def main():
    infile = open('golf.txt','w')
    name = input("Enter player's name: ")

    while name != '':
        score = input("Enter player's score: ")

        infile.write(name+'\n')
        infile.write(score+'\n')
        name = input("Enter player's name: ")


    infile.close()

main()
