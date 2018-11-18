import random

def generateRandomNuber():
    randomNumber=random.randint(1,3)
    return randomNumber

def getCompChoice(randomNumber):
    if randomNumber==1:
        compChoice='rock'
    elif randomNumber==2:
        compChoice='paper'
    elif randomNumber==3:
        compChoice='scissors'
    return compChoice

def getUserChoice():
    userChoice=input('Enter your choice: rock, paper or scissors: ')
    if userChoice=='' or userChoice=='rock' or userChoice=='paper' or userChoice=='scissors':
        return userChoice
    print('Error!You have to choose: rock,paper or scissors! ')
    return getUserChoice() 

def winnerIs(compChoice,userChoice):
    rockMessage='The rock smashes the scissors.'
    scissorsMessage='Scissors cuts paper.'
    paperMessage='Paper wraps rock.'
    winner='no winner'
    message=''

    if compChoice=='rock':
        if userChoice=='scissors':
            winner='Computer'
            message=rockMessage
        elif userChoice=='paper':
            winner='You'
            message=paperMessage
        
    elif compChoice=='scissors':
        if userChoice=='paper':
            winner='Computer'
            message=scissorsMessage
        elif userChoice=='rock':
            winner='You'
            message=rockMessage

    else:
        if userChoice=='rock':
            winner='Computer'
            message=paperMessage
        elif userChoice=='scissors':
            winner='You'
            message=scissorsMessage

    return winner, message

def start(compWins, userWins):
    randomNumber=generateRandomNuber()
    compChoice=getCompChoice(randomNumber)
    userChoice=getUserChoice()
    if userChoice=='':
        return
    print('The computer chose',compChoice)
    winner,message=winnerIs(compChoice,userChoice)

    if winner!='no winner':
        print(winner,'won(',message,')')
        if winner=='Computer':
            compWins+=1
        else:
            userWins+=1
    else:
        print('You both have the same choice')
       
    print('Score (Computer : User) ',compWins,':',userWins,'\n')
    
    start(compWins, userWins)

    
def main():
    compWins=0
    userWins=0
   
    start(compWins,userWins)
     
main()
