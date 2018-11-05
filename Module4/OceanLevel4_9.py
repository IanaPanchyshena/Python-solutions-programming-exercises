# Tuition Increase4_10
# At one college, the tuition for a full-time student is $8,000 per semester.
# It has been announced that the tuition will increase
# by 3 percent each year for the next 5 years.
# Write a program with a loop that displays
# the projected semester tuition amount for the next 5 years.


def main():
    tuition=8000 # tuition per semestr
    print('Num.Years\Tuition$')
    print('------------------')
    print()
    for years in [1,2,3,4,5]:
        tuition+=(3/100)*tuition
        print(years,'\t',format(tuition,'7.2f'))

main()
