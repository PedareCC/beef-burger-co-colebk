import time

beef_burgers = {
    'Cheeseburger': 4.99,
    'Double Cheeseburger': 5.50,
    'The Clogger': 6.70
}

def prettyprint(dic):
    return ', '.join([f'{key} {dic[key]}x' for key in dic.keys()])

total_order = {
    
}          
total_order_prices = 0  

def acurrency(x):
    return f"${x:.2f}"

def menu():
    print('--- Beef Burger Menu ---')
    print(f"1. Cheeseburger for {acurrency(beef_burgers['Cheeseburger'])}")
    print(f"2. Double Cheeseburger for {acurrency(beef_burgers['Double Cheeseburger'])}")
    print(f"3. The Clogger for {acurrency(beef_burgers['The Clogger'])}")
    print('4. Go to checkout.')

def addbugr(choice):
    global total_order, total_order_prices
    if choice not in total_order:
            total_order[choice] = 1
    else:
            total_order[choice] += 1
    total_order_prices = total_order_prices + beef_burgers[choice]
    total_order_prices = round(total_order_prices, 2)
    print(f"understood your full order at the moment is {prettyprint(total_order)} ")
    print(f"your order price at the moment is {acurrency(total_order_prices)} ")
    customer_order()    
     

def customer_order():
        global total_order, total_order_prices
        order = input('Select what you would like to order: ')
  
        if order == "1":
            addbugr('Cheeseburger')
        elif order == "2":
            addbugr('Double Cheeseburger')
        elif order == "3":
            addbugr('The Clogger')
        elif order == "4":
            if not total_order:
                 print("\nyou cant order nothing\n")
                 customer_order()
            else:
                check_out()
        else:
             print("\nthats not an option\n")
             menu()
             print(f"your order currently contains{prettyprint(total_order)}")
             customer_order()

def check_out():
    print('\n--- Your Order Summary ---')
    print(f"you have ordered {prettyprint(total_order)}")
    print(f"your total is {total_order_prices}")
    is_it_correct = input("1. Yes\n2. No\nis this correct?")
    if is_it_correct == "1":
        print("thank you for eating at Beef Burger Co\nhave a great day :)\n\nyour order will be ready in")
    elif is_it_correct == "2":
         print("understood")
         menu()
         customer_order()
    else:
        print("please use a proper option")
        check_out()
    
start_time = time.time()
time.sleep(1)
end_time = time.time()

print(end_time - start_time)
a = round(end_time - start_time)
print(a)
print('Welcome to the Beef Burger Co. menu!')
menu()
customer_order()

