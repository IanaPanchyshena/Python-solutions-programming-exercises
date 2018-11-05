# nested_loops4_14
# Write a program that uses nested loops to draw this pattern:
# *******
# ******
# *****
# ****
# ***
# **
# * 

def main():
    for row in range(7,0, -1):
        for colum in range(row, 0, -1):
            print('*',end='')
        print()

main()
