

from sys import api_version


Welcome = '''
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************
    '''
Appetizers = ["Wings", "Cookies", "Spring Rolls"] 
Appetizers_Counters = [ 0,0,0]
Entrees = ["Salmon", "Steak", "Meat Tornado", "A Literal Garden"]
Entrees_Counter = [0,0,0]
Desserts = ["Ice Cream", "Cake", "Pie"]
Desserts_Counter=[0,0,0]
Beverages = ["Coffee", "Tea", "Unicorn Tears"]
Beverages_Counter = [0,0,0]

print (Welcome)
print("Appetizers\n"
       "----------")
for i in Appetizers:
    print (i)

print("\n\nEntrees\n"
       "----------")
for i in Entrees:
    print (i)

print("\n\nDesserts\n"
       "----------")
for i in Desserts:
    print (i)

print("\n\nBeverages\n"
       "----------")
for i in Beverages:
    print (i)

orderMess = '''
***********************************
** What would you like to order? **
***********************************

    '''
print(orderMess)

order = ""
order_count = 1

while True :
    order = input("<".ljust(2, " "))
    if order == "quit":
        break
    elif order in Appetizers:
        Appetizers_Counters[Appetizers.index(order)] +=1
        print(f'** {Appetizers_Counters[Appetizers.index(order)]} order of {order} have been added to your meal **')
    elif order in Entrees:
        Entrees_Counter[Entrees.index(order)] +=1
        print(f'** {Entrees_Counter[Entrees.index(order)]} order of {order} have been added to your meal **')
    elif order in Desserts:
        Desserts_Counter[Desserts.index(order)] +=1
        print(f'** {Desserts_Counter[Desserts.index(order)]} order of {order} have been added to your meal **')
    elif order in Beverages:
        Beverages_Counter[Beverages.index(order)] +=1
        print(f'** {Beverages_Counter[Beverages.index(order)]} order of {order} have been added to your meal **')
    else:
        print("not in the menu !")



