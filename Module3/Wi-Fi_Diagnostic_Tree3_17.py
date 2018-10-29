# Wi-Fi_Diagnostic_Tree3_17
def main():
    print('Reboot the computer and try to connect.')
    step1=str(input('Did that fix the problem? (Yes or No): '))
    if step1=='Yes':
        print('You fixed a bad Wi-Fi connection!')
    if step1== 'No':
        print('Rebbot the router and try to connect.')
        
        step2=str(input('Did that fix the problem? (Yes or No): '))
        if step2=='Yes':
            print('You fixed a bad Wi-Fi connection!')
        if step2== 'No':
            print('Make sure the cables beetween the router'\
                      ' & modem are plugged in firmly.')

            step3=str(input('Did that fix the problem? (Yes or No): '))
            if step3=='Yes':
                print('You fixed a bad Wi-Fi connection!')
            if step3=='No':
                print('Move the router to a new location and try to connect.')

                step4=str(input('Did that fix the problem? (Yes or No): '))
                if step4=='Yes':
                    print('You fixed a bad Wi-Fi connection!')
                if step4== 'No':
                    print('Get a new router.')
        

main()
                         
