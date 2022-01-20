import admin
import user
import hashlib
import data

adminusername = None
adminpassword = None

try:
    with open('admincredentials.txt', 'r') as f:
        details = f.readline()
        adminusername = details.split(':')[0]
        adminpassword = details.split(':')[1]
except:
    print("Please create admin account")
    username = input("enter username: ")
    password = input("enter password: ")
    repassword = input("Re-Enter Password: ")
    while repassword != password:
        print("Password Doesnt Match")
        password = input("Password: ")
        repassword = input("Re-Enter Password: ")
    res = hashlib.sha256(password.encode())
    password = res.hexdigest()
    adminusername = username
    adminpassword = password
    with open('admincredentials.txt', 'w') as f:
        f.write(username +":" + password)
    print('Admin account created successfully')


def login():
    if username == adminusername and password == adminpassword:
        return True
    elif user.validateuser(username, password):
        return True
    return False

data.ReadFiles()
while True:
    try:
        option = int(input("Enter 1 to login, 2 to Create new user, enter 0 to exit the application: "))
        if option not in [0, 1, 2]:
            raise ("only 0,1,2 are valid options")
        if option == 0:
            data.upadatefiles()
            break
        elif option == 2:
            user.createuser()
        elif option == 1:
            username = input("Enter UserName: ")
            res = hashlib.sha256(input("Enter Password: ").encode())
            password = res.hexdigest()
            if login():
                while True:
                    print("Login Successful")
                    if username == adminusername:
                        admin.adminFn()
                    else:
                        user.userfn()
                    break
            else:
                print("Log in Failed")

    except Exception as ex:
        print(ex)
        print("only 0,1,2 are valid options")
