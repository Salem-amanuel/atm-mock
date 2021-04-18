#register 
# - first name, last name, password, email
# - generate user account


#login
# - account number and pasword 

#bank operations

#Initializing the system 
import random 
import Validation
import Database
from getpass import getpass 
#database = {
#   xxxxxxxxxxx:['Eyerusalem', 'Woldeamanuel', 'eyerusalem_woldeamanuel@yahoo.com', 'password']
#}  

#dictionary

import datetime
datetime = datetime.datetime.now()
print(datetime)

def init():

    
    print("welcome to bankPHP")

    haveAccount = int(input("Do you have account with us: (1) Y (2) N \n"))

    if(haveAccount == 1):
       
       login()
    elif(haveAccount == 2):
        
        print(register())
    else:
        print("You have selected invalid option")
        init()

        
def login():

    print("***** Login *****")
    
    account_number_from_user = input("What is your account number? \n")

    is_valid_account_number = Validation.account_number_validation(account_number_from_user)

    if is_valid_account_number:

        password = getpass("What is your password? \n")
        usee = databade.authenticate_user(account_number_from_user, password)
        if user:
            bank_operation(user)

        #for account_number, user_details in database.items():
           # if account_number == int(account_number_from_user):
              #  if user_details[3] == password:
                 #   bank_operation(user_details)
    
        print('Invalid account or password') 
        login()

    else:
        print("Account number Invalid: check that you have up to 10 digits and only integers")

        int()





def register(): 
    print("****** Register ******")

    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n") 
    password = getpass("create a password for yourself \n")

    account_number = generation_account_number()

    is_user_created = Database.create(account_number, first_name, last_name, email, password
    
    if is_user_created:
        print("Your Account has been created")
        print("*********************")
        print("Your account number is: %d" % accountNumber)
        print("keep your account number safe")
        print("*********************")

        login()

    else:
        print("Something went wrong please try again")
        register()


def bank_operation(user):

    print("Welcome %s %s " % (user[0], user[1]))
    
    selected_option = input("What would you like to do? (1) deposit (2) withdrawal (3)Complaint (4) logout (5) exit \n")
    
    if selected_option == 1:
            
        deposit_operation()
    elif selected_option == 2:

        withdrawal_operation() 
    elif selected_option == 3:

        Complaint()
    elif selected_option == 4:
             
        logout()
    elif selected_option == 5:
           
        exit()
    else:

        print("Invalid option selected")
        bank_operation(user)


def withdrawalOperation():
    Print("Withdrawal Operation")
    selected_option1 = int(input('please select an option'))
    selected_option2 = int(input('How much would you like to withdraw'))
    selected_option3 = int(input('please select an option'))
    selection_option4 = int(input('Take your cash! Exit!'))

    print(selectedOption)
    print('1. $100')
    print('2. $500')
    print('3. $1000')
         
        
    if(selected_option1 == 1):

        print('you selected %s' % selected_option)

    elif(selected_option == 2):
        print('you selected %s' % selected_option)
            
    elif(selected_option == 3):
        print('you selected %s' % selected_option)

        
    else:
        print('Invalid option selected, please try again')

         
   
def deposit_operation(selected_option):
    print("Withdrawal Operation")
    selected_option1 = int(input('How much would you like to Deposit'))
    selected_option2 = int(input('please select an option'))
    

    print(selected_option)
        
    print('(1) $1000')
    print('(2) $1500')
    print('(3) $2000')

    selected_option3 = int(input("please select an option"))

    if(selected_option1 == 1):

        print('you selected %s' % selected_option)

    elif(selected_option == 2):
        print('you selected %s' % selected_option)
            
    elif(selected_option == 3):
        print('you selected %s' % selected_option)
    
    else:
        print('Invalid option selected, please try again')

    selected_option4 = int(input('Insert cash! Exit!'))
     
   
def complaint():

    selected_option1 = int(input('What issue would you like to report'))
    selected_option2 = int(input('please select an option'))
    selected_option3 = int(input('please select an option'))
    selected_option4 = int(input('Thank you for contacting us! Exit!'))

          
    print(selected_option)   
    print('1. I can not make a withdrawal')
    print('2. I can not make a deposit')
    
    selected_option3 = int(input('please select an option'))

    if(selected_option1 == 1):
        print('you selected %s' % selected_option)

    elif(selected_option == 2):
        print('you selected %s' % selected_option)
              
    else:
        print('Invalid option selected, please try again')

    selected_option4 = int(input('Thank you for contacting us! Exit!'))

def generationAccountNumber():
    return random.randrange(1111111111,9999999999)


def set_current_balance(user_details, balance):
    user_details[4] = balance


def get_current_balance(user_details):
    return user_details[4]
    
def logout():
    login()






#### ACTUAL BANKING SYSTEM ####

init() 
generationAccountNumber()