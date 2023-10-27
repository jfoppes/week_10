#!/usr/bin/env python3

#Jaocb Foppes CINF308 Progrmaing For INF Proejct 10 - Algorithyms - Stock Manager

import csv
import operator

""" This program reports stock of items for a warehouse
    stock levels will be pulled from and saved to a CSV file"""
    
'''Sample Data
stockRoom = {"watch":7,"iphone":10,"macbook":4,"ipad":5,"pencil":0,"wband":0} # dictionary of procuts and stock levels 
targetStock = {"watch":10,"iphone":15,"macbook":6,"ipad":5,"pencil":4,"wband":10} #dictionary or products and thier target stock 
'''

stockRoom = [] # dictionary of procuts and stock levels 
inStock = []
onOrder = {}

with open("stock.csv","r+") as s:# create lsit of products. each produt is a dictionairs 
    reader = csv.DictReader(s)
    for i in reader:
        stockRoom.append(i)
    for i in stockRoom:
        i["Stock_Level"] = int(i["Stock_Level"])
        i["Target_Stock"] = int(i["Target_Stock"])   


def weGotIt(): # this fuction determines what products are instock 
    global inStock
    for i in stockRoom: # for each key in the dict if the stock level value is >0 add the product to the inStock list 
        if i["Stock_Level"] >0:
            inStock.append(i)
    inStock = sorted(inStock, key=operator.itemgetter("Product_Name")) # sort the lsit alphabetically          
weGotIt()

def checkStock(): # this fucntion check the instock levels vs the target stock levels and outputs a list of things that need to be ordered and how many need to be ordered 
    global onOrder
    for i in stockRoom: # for each dixtioanry in the list of stockroom dictionaies 
        if i["Stock_Level"] < i["Target_Stock"]: # if the instock quantity is less than that target stock, add the item to the onOrder lsit wit hthe number we need to order
            need = i["Target_Stock"] - i["Stock_Level"]
            onOrder[i["Product_Name"]] = need # create list of procut names and the numbe rthat needs to be ordered 
    print("\nWe need to order the following products\n",onOrder) # this returns          

def inStockByCat():# this func takes a category as an input and output a list of produts in stock in that category
    allCats = []
    for i in inStock:
        if i["Product_Category"] not in allCats:
            allCats.append(i["Product_Category"])
    cat = input("""
                Which Category Would you like to view
                {Categories}
                """.format(Categories=allCats))
    for i in inStock:
        if i["Product_Category"]== cat:
            print(i["Product_Name"]+":",i["Stock_Level"],"in stock")
def outOfStock():
    pass  

def stockLevel(): #This fuction will show stock level of all products or a requested product
    choice = int(input("""
                   How wooud you like top view stock?
                   (1) for All In Stock Products
                   (2) to choose a specific Product Category
                   (3) to View Out of Stock Items
                   """))
    if choice == 1:
        print("\n\nWe have the following items in stock: \n",inStock)  
    elif choice == 2:
        inStockByCat()
    elif choice == 3:
        outOfStock()

def newProduct(): # this fuction will allow a user to define a enw prodcut with a name, product category, and stock level 
    pass

def incommingShipment(): # this fuction will allow a user to update/increment stock levels 
    pass

def deleteProduct(): #This fuction will allow a user to delete a product they no longer sell 
    pass

def welcome(): # This fuction is where the user will be able to choose what they want to do 
    choice = int(input("""
                   ***Welcome to Inventory Controll***
                   
                   Enter (1) to View Product Stock
                   
                   Enter (2) to Input incomming Shipment Data
                   
                   Enter (3) to Create a new Product
                   
                   Enter (4) to Delete a Product
                   """))
    if choice == 1:
        stockLevel()
    elif choice == 2:
        incommingShipment()
    elif choice == 3:
        newProduct()
    elif choice == 4:
        deleteProduct()
while True:
    welcome() 