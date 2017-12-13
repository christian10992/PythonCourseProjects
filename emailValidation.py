## This program will validate an email on the following critera:
## 1. The email domain must be in the format of 'g.austincc.edu'
## 2. The name must be all lower-case and only contain letters
## If the email is valid, it will return the user's first and last name capitalized.

def main():
    valid = False
    # get email
    email = str(input('Enter your ACC e-mail address: '))
    # validate email
    while valid == False:
        try:
            valid = validate(email)
            if valid == False:
                email = str(input('Invalid email. Ensure that it is correct' + \
                                  'and written in all lower=case' + \
                                  'and please try again: '))
        except:
            email = str(input('Invalid email. Ensure that it is correct ' + \
                                  'and written in all lower-case ' + \
                                  'and please try again: '))
    # process name    
    getName(email)
    

def validate(email):
    # split email into name and domain
    name_email = email.split('@')
    
    # split name into first and last
    first_last = name_email[0].split('.')
    first_name = first_last[0]
    last_name = first_last[1]

    # split domain into parts
    domain_parts = name_email[1].split('.')

    # validate that name is lowercase
    if first_name.islower() != True:
        valid = False
    elif last_name.islower() != True:
        valid = False
                
    # validate that domain is correct
    elif domain_parts[0] != 'g':
        valid = False
    elif domain_parts[1] != 'austincc':
        valid = False
    elif domain_parts[2] != 'edu':
        valid = False

    # if everything passes, return as valid
    else:
        valid = True

    #return validity status
    return valid
    

def getName(email):
    # split name and email
    name_email = email.split('@')
    # split first and last name, then capitalize them
    first_last = name_email[0].split('.')
    first_name = first_last[0].capitalize()
    last_name = first_last[1].capitalize()
    print()
    print('First name:', first_name)
    print('Last name:', last_name)


main()
