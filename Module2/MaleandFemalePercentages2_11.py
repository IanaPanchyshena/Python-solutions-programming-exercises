# Male and Female Percentages

def main():
    # ask to enter the namber of females and males.
    females=int(input('How many females in your class? '))
    males=int(input('How many males in your class? '))

    # calculate the total of females and males.
    total=females+males

    # calculate the percentage females and males.
    percent_females=females/total*100
    percent_males=males/total*100

    # display the percentage of males and females in the class.
    print('The percentage of females in your class is ',format(percent_females,'.0f'))
    print('The percentage of males in your class is ',format(percent_males,'.0f'))
 
main()
