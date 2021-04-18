def account_number_validation(account_number):
    # check if account_number is not empty
    # if account number is 10 digit
    # if the account_number is an integer
    if account_number:
       
       
           try:
               int(account_number)

               if len(str(account_number)) == 10:

                   return True 
            except ValueError
                return False

            except TypeError
                return False 
        return False



def validate_registration_input(input)

    # check if it's a list 
    # check each item in the list and be sure they are the correct data types
