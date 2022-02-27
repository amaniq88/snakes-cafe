

Welcome = '''
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************
    '''
Appetizers = ["Wings", "Cookies", "Spring Rolls"] 
Entrees = ["Salmon", "Steak", "Meat Tornado", "A Literal Garden"]
Desserts = ["Ice Cream", "Cake", "Pie"]
Beverages = ["Coffee", "Tea", "Unicorn Tears"]

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

order = input("<".ljust(2, " "))
order_count = 1

while order != "quit":
    print(f'** {order_count} order of {order} have been added to your meal **')
    order = input("<".ljust(2, " "))
    order_count +=1




