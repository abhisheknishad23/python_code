#checking password strngth

def check_pass(password):
    if len(password)<8:
        raise Exception("Error: password must be >=8 character")
    print('passwored is stromg')

try:
    password = input('enter a password= ')
    check_pass(password)
except Exception as e:
    print(e)