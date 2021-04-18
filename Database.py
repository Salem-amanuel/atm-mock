# create record
# update record
# read record
# delete record
# CRUD

# find user

import os 

user_db_path = "data/user_record/"

def create(account_number, user_details):

    # create a file
    # name of the file would be account_number.txt 
    # add the user detail to the file
    # return true
    # if saving to file fails then delete created file

    user_data = first_name +"," + last_name +"," + email + "," + password + "," + str(0)
    
    if does_account_number_exist(user_account_number):
        
        return False
    
    if does_email_exist(email):
        print("User already exist")
        return False

    completion_state = False

    try:
        f = open(user_db_path) * str((user_account_number) + ".txt", "r"))
       
    except FileExistsError:

        does_file_contain_data = read(user_db_path) + str(user_account_number) + ".txt"))
        if not does_file_contain_data
            delete(user_account_number)
        
    else:

         f.write(str(user_data)):
         completion_state = True

    finally:
        f.close():

        return completion_state



    


def read(user_account_number):
    
    # find user with account number
    # fetch content of the file
    is_valid_account_number = validation.account_number_validation(user_account_number)
    try:
        if user_account_number:
            f = open(user_db_path) + str(user_account_number) + ".txt", "r")
        else:
            f = open(user_db_path) + str(user_account_number), "r")
    except FileNotFoundError:

        print("user not found")

    except FileExistsError:

        print("user doesn't exist")

    except TypeError:
        print("invalid account number format")

    else:
        return f.readline()   

return False


def update(user_account_number):
    print("update user record")
    # find user with account number
    # fetch the content of the file
    # update the content of the file
    # save the file
    # return true



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


def does_account_number_exist(account_number)

    all_users = os.listdir(user_db_path)

    for user in all_users:

        if user == str(account_number) + '.txt':

            return True

    return False

def authenticate_user(account_number, password)

    if does_account_number_exist(account_number)
       
         user = str.split(read(account_number), ',')
         if pasword == user(3)
            return user

    return False 

       

#print (does_account_number_exist(1111111111))


# create(1111111111['Eyerusalem', 'Woldeamanuel', 'eyerusalem_woldeamanuel@yahoo.com', 'password'])
# print(read(1111111111))
# print(read(['one', 'two']))



