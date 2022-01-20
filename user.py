import data
import hashlib
import datetime as dt

userid = None


def validateuser(username, password):
    for user in data.users:
        if user["username"] == username and user["password"] == password:
            global userid
            userid = user["userid"]
            return True
    return False


def createuser():
    username = input("Full Name: ")
    phonenumber = input("Phone Number: ")
    email = input("Email: ")
    address = input("Address: ")
    password = input("Password: ")
    repassword = input("Re-Enter Password: ")
    while repassword != password:
        print("Password Doesnt Match")
        password = input("Password: ")
        repassword = input("Re-Enter Password: ")

    user = User(username,phonenumber,email,address,password)



def updatestock(foodids):
    for item in foodids:
        for food in data.fooddetails:
            if food["foodid"] == item:
                food["stock"] = int(food["stock"]) - 1


def validatestock(orderlist,orderdic):
    seletedorders = {}
    for i in orderlist:
        for item in data.fooddetails:
            if item['foodid'] == orderdic[i]:
                if item['foodid'] in seletedorders:
                    seletedorders[item['foodid']] += 1
                else:
                    seletedorders[item['foodid']] = 1
    for foodid in seletedorders:
        for item in data.fooddetails:
            if item['foodid'] == foodid:
                if seletedorders[foodid] > int(item['stock']):
                    print('only',item['stock'],item['name'],'are available in stock')
                    print('you ordered',seletedorders[foodid])
                    print('please order again with value lesser than stock')
                    return False
    return True

class User:

    def __init__(self,username,phonenumber,email,address,password,userid = None,update = False):
        if update:
            self.userid = userid
        else:
            self.userid = dt.datetime.now().strftime("%m%d%Y%H%M%S")
        res = hashlib.sha256(password.encode())
        password = res.hexdigest()

        data.users.append({'userid': self.userid, 'username': username, 'phonenumber': phonenumber, 'email': email, 'address': address,
             'password': password})
        if update:
            print('updated successful')
        else:
            print("Account Created SuccessFully")
            print('please be noted that username for login is your full Name')


    def placeorder():
        n = 1
        orderdic = {}
        seletedorders = []
        for item in data.fooddetails:
            if item['active'] == 'True' and int(item['stock']) > 0:
                print('%s)%s (%s) [INR %s]' % (n, item["name"], item["quantity"], item["price"]))
                orderdic[n] = item['foodid']
                n += 1
        if n == 1:
            print("No item is available to buy")
            return
        print('enter 0 to cancel')
        order = input("enter comma seperated order numbers, if multiple same orders then repeat order numbers: ")
        if order =='0':
            return
        orderlist = list(map(int, order.split(',')))
        if validatestock(orderlist,orderdic) == False:
            return
        print("selected orders are :- ")
        totalamount = 0
        n = 1
        for i in orderlist:
            for item in data.fooddetails:
                if item['foodid'] == orderdic[i]:
                    print('%s)%s (%s) [%s]' % (n, item["name"], item["quantity"], item["price"]))
                    n += 1
                    seletedorders.append(item['foodid'])
                    totalamount += int(item["price"]) - int(item["price"]) * float(item['discount']) / 100
                    break
        print('Total Amount after discount:', totalamount)
        orderconfirm = int(input("enter 1 to confirm order, 0 to cancel: "))
        if orderconfirm == 1:
            updatestock(seletedorders)
            data.orders.append({'userid': userid, 'orders': seletedorders, 'datetime': str(dt.datetime.now())})
            print("order placed")

    def userorderhistory(userid):
        noordersplaced = True
        for val in data.orders:
            orderedtime = None
            orderidcount = {}
            if val['userid'] == userid:
                orderedtime = val['datetime']

                for item in val['orders']:
                    if item in orderidcount:
                        orderidcount[item] += 1
                    else:
                        orderidcount[item] = 1
                        noordersplaced = False

            i = 1
            if orderedtime == None:
                continue
            print('ordered on:', orderedtime)
            for order in orderidcount:
                for item in data.fooddetails:
                    if item['foodid'] == order:
                        sno = str(i) + ')'
                        print(sno, item['name'], 'X', orderidcount[order])
                        i += 1

        if noordersplaced:
            print('no orders placed yet')
        print("\n\n")


def updateuser(userid):
    print('updating user')
    username = input("Full Name: ")
    phonenumber = input("Phone Number: ")
    email = input("Email: ")
    address = input("Address: ")
    password = input("Password: ")
    repassword = input("Re-Enter Password: ")
    while repassword != password:
        print("Password Doesnt Match")
        password = input("Password: ")
        repassword = input("Re-Enter Password: ")
    tempuser = None
    for user in data.users:
        if user['userid'] == userid:
            tempuser = user
            break
    data.users.remove(tempuser)
    user = User(username, phonenumber, email, address, password, userid=userid,update=True)
    print("profile updated")

def userfn():
    while True:
        data.upadatefiles()
        print('1) Place New Order')
        print('2) Order History')
        print('3) Update Profile')
        print("enter 0 to logout ")
        choose = int(input())
        if choose == 1:
            User.placeorder()
        if choose == 2:
            User.userorderhistory(userid)
        if choose == 3:
            try:
                updateuser(userid)
            except Exception as ex:
                print(ex.agrs)
        if choose == 0:
            return
