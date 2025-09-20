import time

beef_burgers = {
    'Cheeseburger': 4.99,
    'Double Cheeseburger': 5.50,
    'The Clogger': 6.70
}
current_bugr = {
     
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

def customise(choice):
    customise_option = input(f"1. Add\n2. Remove\nWould you like to add or remove items from the {choice}?")
    if customise_option == "1":
        print(choice)
        if choice == "['Double Cheeseburger']":
             print('df')
        input(f"1.Patty $0.80\n2.Cheese $0.30\n3.Pickles $0.20\n4.Ketchup $0.20\n5.Mustard $0.20\n6.Onions $0.20\nyour burger currently {prettyprint(current_bugr)} has What would you like to add?")
    elif customise_option == "2":
        print("sddf")
    else:
        print("wsdfg")

def chonky(choice):
    custom_choice = input(f"1. yes\n2. no\nwould you like to customise the {choice}?")
    if custom_choice == "1":
         customise(choice)
    elif custom_choice =="2":
         print(f"standard {choice}")
    else:
         print("thats not an option")
         chonky()

def addbugr(choice):
    global total_order, total_order_prices
    chonky([choice])
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
    print(f"your total is {acurrency(total_order_prices)}")
    is_it_correct = input("1. Yes\n2. No\nis this correct?")
    if is_it_correct == "1":
        end_time = time.time()
        timered = round(end_time - start_time)
        w_a_i_t = timered/10
        print(f"thank you for eating at Beef Burger Co\nhave a great day :)\n\nyour order will be ready in {round(w_a_i_t)} minutes")
    elif is_it_correct == "2":
         print("understood")
         menu()
         customer_order()
    else:
        print("please use a proper option")
        check_out()


start_time = time.time()
print('Welcome to the Beef Burger Co. menu!')
menu()
customer_order()

