
#bank operations

#Initializing the system 
import random 
import Validation
import Database
from getpass import getpass 

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
            auth_session_created = database.create_auth_session(account_number_from_user)
            bank_operation(user, account_number_from_user)

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



def generationAccountNumber():
    return random.randrange(1111111111,9999999999)



def bank_operation(user_details, account_number_from_user):

    print("Welcome %s %s " % (user[0], user[1]))
    
    selected_option = input("What would you like to do? (1) deposit (2) withdrawal (3)Complaint (4) logout (5) exit \n")
    
    if selected_option == 1:
       balance(user_details)
       bank_operation(user_details, account_number_from_user)
     
    elif selected_option == 2:
        deposit( user_details, account_number_from_user )
        bank_operation(user_details, account_number_from_user)

    elif selected_option == 3:
        withdrawal( user_details, account_number_from_user )
        bank_operation(user_details, account_number_from_user)
 
    elif selected_option == 4:
        Complaint()
        bank_operation(user_details, account_number_from_user)

    elif selected_option == 5:
        logout(account_number_from_user)

    elif selected_option == 6:
        print("Thank you %s %s. We look forward to seeing you again." % (user[0], user[1]))
        logout()
        exit()   
        
    else:
        print("Invalid option selected")
        bank_operation(user)


def balance(user_details):
    get_current_balance(user_details)
    print("Your balance is %s." % (user_details[4]))


def set_current_balance(user_details, balance):
    return user_details[4] = balance


def get_current_balance(user_details):
    return user_details[4]  

def withdrawal_operation(user_details, account_number_from_user):
    amount_to_withdrawal = int(input("How much would you like to withdraw? \n"))
    current_user_balance = get_current_balance(user_details)
    updated_balance = int(current_user_balance) - amount_to_withdrawal

    set_current_balance(user_details, updated_balance)
    database.update_user_record( account_number_from_user, user_details )
    database.update_auth_session( account_number_from_user, user_details )
    print(".git\Take your cash \n")

def deposit_operation(user_details, account_number_from_user):
    amount_to_deposit = int(input("How much would you like to deposit? \n"))
    current_user_balance = get_current_balance(user_details)
    updated_balance = int(current_user_balance) + amount_to_deposit

    set_current_balance(user_details, updated_balance)
    database.update_user_record( account_number_from_user, user_details )
    database.update_auth_session( account_number_from_user, user_details )
    print(".git\Your current balance is %s" % updated_balance)

def complaint():
    input("What issue would you like to report? \n')
    print("Thank you for contacting us")

def invalidOption():
    print("invalid option selected please try again")
    main_options(user_details, account_number_from_user)

def logout(account_number_from_user ):
    database.delete(account_number_from_user)
    login()





#### ACTUAL BANKING SYSTEM ####

