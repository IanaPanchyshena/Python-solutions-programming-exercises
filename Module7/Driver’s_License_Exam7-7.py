# Driver’s_License_Exam7-7
# The local driver’s license office has asked you to create an application
# that grades the written portion of the driver’s license exam.
# The exam has 20 multiple-choice questions.
# Here are the correct answers: 
# 1. A 2. C 3. A 4. A 5. D 6. B 7. C 8. A 9. C 10. B
# 11. A 12. D 13. C 14.A 15.D 16. C 17. B 18. B 19. D 20. A
# Your program should store these correct answers in a list.
# The program should read the student’s answers for each of the 20 questions
# from a text file and store the answers in another list.
# (Create your own text file to test the application.)
# After the student’s answers have been read from the file,
# the program should display a message indicating
# whether the student passed or failed the exam.
# (A student must correctly answer 15 of the 20 questions to pass the exam.)
# It should then display the total number of correctly answered questions,
# the total number of incorrectly answered questions, and a list showing
# the question numbers of the incorrectly answered questions.



def correct_answers():
    list_answers=['A','C','A','A','D','B','C','A','C','B',
                    'A','D','C','A','D','C','B','B','D','A']
    return list_answers

def get_answers():
    user_list=[]
    read_file=open('user_answers.txt','r')
    for i in read_file:
        i=i.rstrip('\n')
        user_list.append(i)
    return user_list

def check_answers(list_answers,user_list):
    count=0
    print('Correct answers',list_answers)
    print('Your answers',user_list)
    wrong_answers=[]
    for i in range(20):
        if list_answers[i]==user_list[i]:
            count+=1
        else:
            wrong_answers.append(i)
    if count<15:
        print('You failed')
    else:
        print('You passed')
    print('The number of correctly answerd question is', count)
    print('The number of incorrectly answerd question is', 20 - count)
    print('The question numbers of the incorrectly answered quesions are',
          wrong_answers)

def main():
        list_answers=correct_answers()
        user_list=get_answers()
        check_answers(list_answers,user_list)
main()
    


    
