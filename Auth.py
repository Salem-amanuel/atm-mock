#register 
# - first name, last name, password, email
# - generate user account


#login
# - account number and pasword 

#bank operations

#Initializing the system 
import random 

database = {}  #dictionary

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

def generationAccountNumber():

    return random.randrange(1111111111,9999999999)


        
def login():

    print("***** Login *****")
    print("Choose bank operation")
    print('Invalid account or password')

    accountNumberFromUser = int(input("What is your account number? \n"))
    password = input("What is your password? \n")
       
    login()
    

def register(): 
    print("****** Register ******")

    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n") 
    password = input("create a password for yourself \n")

    accountNumber = generationAccountNumber()

    database[accountNumber] = [first_name, last_name, email, password]

    print("Your Account has been created")
    print("*********************")
    print("Your account number is: %d" % accountNumber)
    print("keep your account number safe")
    print("*********************")

    login()

    return database

def bankOperation(user):

    print("Welcome %s %s " % (user[0], user[1] ) )
    print("(1) deposit, (2) withdrawal, (3) logout, (4) exit")

    selectedoption = input("What would you like to do? (1) deposit (2) withdrawal (3) complaint (4) logout (5) exit \n")
    
    if selectedoption == 1:
            
        depositOperation("account balance")
    elif selectedoption == 2:
           
        withdrawalOperation("account balance")
    elif selectedoption == 3:
             
        logout()
    elif selectedoption == 4:
           
        exit()
    else:
        bankOperation(user)
        print("Invalid option selected")



def withdrawalOperation():
    
    selectedOption = int(input('please select an option') )
    selectedOption1 = int(input('How much would you like to withdraw') )
    selectedOption2 = int(input('please select an option') )
          
    print(selectedOption)
    print('1. $100')
    print('2. $500')
    print('3. $1000')
         
        
    if(selectedOption1 == 1):

        print('you selected %s' % selectedOption)

    elif(selectedOption == 2):
        print('you selected %s' % selectedOption)
            
    elif(selectedOption == 3):
        print('you selected %s' % selectedOption)

        
    else:
        print('Invalid option selected, please try again')

         
    selectionOption4 = int(input('Take your cash! Exit!') )



def depositOperation(selectedOption):
    
    selectedOption1 = int(input('How much would you like to Deposit') )
    selectedOption2 = int(input('please select an option') )

    print(selectedOption)
        
    print('1. $1000')
    print('2. $1500')
    
    print('3. $2000')
    selectedOption3 = int(input("please select an option") )
    if(selectedOption1 == 1):

        print('you selected %s' % selectedOption)

    elif(selectedOption == 2):
        print('you selected %s' % selectedOption)
            
    elif(selectedOption == 3):
        print('you selected %s' % selectedOption)

        
    else:
        print('Invalid option selected, please try again')

         
    selectionOption4 = int(input('Insert cash! Exit!'))



def complaint():

     selectedOption1 = int(input('What issue would you like to report'))
     selectedOption2 = int(input('please select an option'))

               
     print(selectedOption)
        
     print('1. I can not make a withdrawal')
     print('2. I can not make a deposit')
    
     selectedOption3 = int(input('please select an option'))

     if(selectedOption1 == 1):
        print('you selected %s' % selectedOption)

     elif(selectedOption == 2):
        print('you selected %s' % selectedOption)
            
     elif(selectedOption == 3):
        print('you selected %s' % selectedOption)

        
     else:
        print('Invalid option selected, please try again')

     selectionOption4 = int(input('Thank you for contacting us! Exit!'))

        
def logout():
    login()


#### ACTUAL BANKING SYSTEM ####

init() 
generationAccountNumber()