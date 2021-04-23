# create record
# update record
# read record
# delete record
# CRUD

# find user

import os 
import Validation
user_db_path = "data/user_record/"
auth_session_path = "data/auth_session/"

def create(account_number, user_details, email, password, account_balance):

    # create a file
    # name of the file would be account_number.txt 
    # add the user detail to the file
    # return true
    # if saving to file fails then delete created file

    user_data = ("first_name" +"," + "last_name" +"," + "email" + "," + "password" + "," + str(0))
    
    if does_account_number_exist(account_number):
        return False
    
    if does_email_exist(email):
        print("User already exist")
        return False

    completion_state = False

    try:
        f = open(user_db_path) + str((account_number) + ".txt", "x")
       
    except FileExistsError:
        does_file_contain_data = read(user_db_path) + str((account_number) + ".txt")

        if not does_file_contain_data:
            delete(account_number)
        
        else:

            f.write(str(user_data))
            completion_state = True

    finally:
        f.close()

        return completion_state



def create_auth_session(user_account_number):
    duplicate_user_record_file = open(user_db_path + str(user_account_number) + ".txt").read()
    f = open(auth_session_path + str(user_account_number) + ",txt", "x")
    f.write(str(duplicate_user_record_file));



def read(user_account_number):
    
    # find user with account number
    # fetch content of the file
    is_valid_account_number = Validation.account_number_Validation(user_account_number)
    try:
        if user_account_number:
            f = open(user_db_path) + str((user_account_number) + ".txt", "r")
        else:
            f = open(user_db_path) + str((user_account_number), "r")

    except FileNotFoundError:

        print("user not found")

    except FileExistsError:

        print("user doesn't exist")

    except TypeError:

        print("invalid account number format")

    else:
        return f.readline()   

    return False





def update_user_record(user_account_number, user):
    
    # find user with account number
    # fetch the content of the file
    # update the content of the file
    # save the file
   
    print("update user record")
    print(read(user_account_number))
    user = str.split(read(user_account_number), ',')
    balance = str(int(user[4]) + int(user_account_number))
    print(balance)

    user[4] = balance
   
    f = open(str(user_account_number) + ".txt", "w")
    f.write(updated_info)
    f.close()
    f = open(str(user_account_number) + ".txt", "r")
    print(f.read)



def update_auth_session(user_account_number, user):
    print("Update user record")
    print(read(user_account_number))
    user = str.split(read(user_account_number), ',')
    balance = str(int(user[4]) + int(user_account_number))
    print(balance)

    user[4] = balance
   
    f = open(str(user_account_number) + ".txt", "w")
    f.write(updated_info)
    f.close()
    f = open(str(user_account_number) + ".txt", "r")
    print(f.read)

def delete(user_account_number):
    # find user with account number 
    # delete the user record(file)
    # return true

    is_delete_successful = False
    
    if os.path.exists(user_db_path + str(user_account_number) + ".txt"):
        
        try:   
           
            os.remove(user_db_path + str(user_account_number) + ".txt")
            is_delete_successful = True

        except FileNotFoundError:
            
            print("user not found")

        finally:
             
            return is_delete_successful 



def does_email_exist(email):
    all_users = os.listdir(user_db_path)

    for user in all_users:
       user_list = str.split(read(user), ',')
       if email in user_list:
           return True

    return False


def does_account_number_exist(account_number):

    all_users = os.listdir(user_db_path)

    for user in all_users:

        if user == str(account_number) + '.txt':

            return True

    return False

def authenticate_user(account_number, password):

    if does_account_number_exist(account_number):
       
         user = str.split(read(account_number), ',')
         if password == user(3):
            return user

    return False 

       

#print (does_account_number_exist(1111111111))

# print(read(['one', 'two']))



