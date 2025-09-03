import time

beef_burgers = {
    'Cheeseburger': 4.99,
    'Double Cheeseburger': 5.50,
    'The Clogger': 6.70
}

total_order = []          
total_order_prices = []   

def acurrency(x):
    return f"${x:.2f}"

def menu():
    print('--- Beef Burger Menu ---')
    print(f"1. Cheeseburger for {acurrency(beef_burgers['Cheeseburger'])}")
    print(f"2. Double Cheeseburger for {acurrency(beef_burgers['Double Cheeseburger'])}")
    print(f"3. The Clogger for {acurrency(beef_burgers['The Clogger'])}")
    print('4. Go to checkout.')


def customer_order():
        order = input('Select what you would like to order: ')
  
        if order == 1:
            print("sdfg")

def check_out():
    print('\n--- Your Order Summary ---')


print('Welcome to the Beef Burger Co. menu!')
menu()
customer_order()
check_out()
