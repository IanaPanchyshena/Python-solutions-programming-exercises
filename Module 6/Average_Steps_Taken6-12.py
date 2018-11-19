# Average_Steps_Taken6-12

# A Personal Fitness Tracker is a wearable device that tracks your physical
# activity, calories burned, heart rate, sleeping patterns, and so on.
# One common physical activity that most of these devices track
# is the number of steps you take each day.
# The steps.txt file contains the number of steps a person has taken each day
# for a year. There are 365 lines in the file, and each line contains
# the number of steps taken during a day.
# (The first line is the number of steps taken on January 1st,
# the second line is the number of steps taken on January 2nd, and so forth.)

# Write a program that reads the file, then displays
# the average number of steps taken for each month.
# (The data is from a year that was not a leap year, so February has 28 days.)

def getDays(month):
    if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
        return 31
    elif month==2:
        return 28
    else:
        return 30

def processMonth(month):
    days=getDays(month)
    total=0
    for day in range(1,days+1):
        line=int(file.readline().rstrip('\n'))
        total+=line
    average=total/days
    print(getMonth(month),'=',format(average,'.0f'))

def getMonth(month):
    if month==1:
        return 'January'
    elif month==2:
        return 'February'
    elif month==3:
        return 'March'
    elif month==4:
        return 'April'
    elif month==5:
        return 'May'
    elif month==6:
        return 'June'
    elif month==7:
        return 'July'
    elif month==8:
        return  'August'
    elif month==9:
        return 'September'
    elif month==10:
        return 'October'
    elif month==11:
        return 'November'
    elif month==12:
        return 'December'


def main():
    
    for month in range(1,13):
        processMonth(month)
        

file=open('steps.txt','r')

main()
