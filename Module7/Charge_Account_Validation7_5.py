#Charge_Account_Validation7_5
# If you have downloaded the source code from
# charge_accounts.txt has a list of a company’s
# valid charge account numbers. Each account number is a seven-digit number,
# such as 5658845.
# Write a program that reads the contents of the file into a list.
# The program should then ask the user to enter a charge account number.
# The program should determine whether the number
# is valid by searching for it in the list. If the number
# is in the list, the program should display a message indicating
# the number is valid. If the number is not in the list,
# the program should display a message indicating the number is invalid.

def get_content(source):
    if source=='file':
        return read_file('charge_accounts.txt')
    elif source=='server':
        return read_server()

def read_file(file_name):
    new_file=open(file_name,'r')
    list_charge=new_file.readlines()
    new_file.close()
    return list_charge

def proccess_content(content):
    for index in range(0,len(content)):
        content[index]=content[index].rstrip('\n')
    return content

def get_input():
    return input('Enter a charge account number: ')

def check_account(search,list_charge):
    return search in list_charge

def print_results(search,result):
    if result:
        print(search,'number is valid')
    else:
        print(search,'number is not in the list')


def main():
    content=get_content('file')
    account_list=proccess_content(content)
    account=get_input()
    result=check_account(account,account_list)
    print_results(account,result)
    
main()
