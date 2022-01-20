import os
import json
import datetime as dt

fooddetails = []
orders = []
users = []


def ReadFiles():
    try:
        with open('fooddetails.txt', 'r') as fptr:
            data = fptr.readlines()
            for line in data:
                fooddetails.append(json.loads(line.replace("'",'"')))


        with open('orders.txt', 'r') as fptr:
            data = fptr.readlines()
            for line in data:
                orders.append(json.loads(line.replace("'",'"')))

        with open('users.txt', 'r') as fptr:
            data = fptr.readlines()
            for line in data:
                users.append(json.loads(line.replace("'",'"')))
    except Exception as ex:
        error = ex

def upadatefiles():
    try:
        with open('fooddetails.txt', 'w') as fptr:
            for line in fooddetails:
                fptr.writelines(str(line) +"\n")

        with open('orders.txt', 'w') as fptr:
            for line in orders:
                fptr.writelines(str(line) +"\n")

        with open('users.txt', 'w') as fptr:
            for line in users:
                fptr.writelines(str(line) + "\n")

    except Exception as ex:
        print(ex.args)

