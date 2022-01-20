import datetime as dt

import data
from data import fooddetails


def addFoodItem():
    name = input("Name: ")
    quantity = input("Quantity: ")
    price = input("Price: ")
    discount = input("Discount(%): ")
    stock = input("Stock: ")
    adminuser = Admin(name,quantity,price,discount,stock)


class Admin:

    def __init__(self,name,quantity,price,discount, stock):
        self.foodid = dt.datetime.now().strftime("%m%d%Y%H%M%S")
        fooddetails.append({'foodid': self.foodid, 'name': name, 'quantity': quantity, 'price': price, 'discount': discount,
                          'stock': stock,'active':'True'})
        print("item added, Food Id :", self.foodid)

    def editfoodItem(foodid):
        edititem = None
        for item in fooddetails:
            if item['foodid'] == foodid:
                edititem = item
                break
        if edititem is None:
            print(foodid, "not found")
        else:
            print(edititem)
            name = input("Updated Name: ")
            quantity = input("Updated Quantity: ")
            price = input("Updated Price: ")
            discount = input("Updated Discount(%): ")
            stock = input("Updated Stock: ")
            fooddetails.remove(edititem)
            fooddetails.append({'foodid': foodid, 'name': name, 'quantity': quantity, 'price': price, 'discount': discount,
                 'stock': stock,'active':'True'})
            print('item updated successfully')

    def viewAllFoodItems():
        for item in fooddetails:
            if item['active'] == 'True':
                for key in item:
                  print(key,":",item[key])
        print('.................................')
    def deleteFoodItem(foodid):
        delitem = None
        for item in fooddetails:
            if item['foodid'] == foodid:
                delitem = item
                break
        if delitem is None:
            print(foodid, "not found")
        else:
            fooddetails.remove(delitem)
            delitem['active'] = 'False'
            fooddetails.append(delitem)
            print(delitem['name'], "successfully deleted")


def adminFn():
    while True:
        print('1) Add new food item ')
        print('2) Edit food item ')
        print('3) View All food items ')
        print('4) Remove food item ')
        print("enter 0 to logout ")
        choose = int(input())
        if choose == 0:
            return
        elif choose == 1:
            addFoodItem()
        elif choose == 2:
            Admin.editfoodItem(input("enter food id: "))
        elif choose == 3:
            Admin.viewAllFoodItems()
        elif choose == 4:
            Admin.deleteFoodItem(input("enter food id: "))
        data.upadatefiles()

