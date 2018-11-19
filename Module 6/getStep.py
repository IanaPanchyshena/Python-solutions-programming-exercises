
import random 
def main():
    fileStep=open('steps.txt','w')
    for day in range(1,366):
        step=getStep()
        fileStep.write(str(step)+'\n')
    fileStep.close()

def getStep():
    number=random.randint(1000,3000)
    return number

        
main()
