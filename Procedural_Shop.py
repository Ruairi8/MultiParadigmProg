# Procedural style program:
import csv
import sys
 

def create_stock_shop():
    # Initializing an empty dictionary object, in which to place the shop items & information into:
    shop = {}
    # Parsing the csv file containing the shop items and information:
    with open("shop1.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        # Initializing an empty list object:
        shop["products"] = []
        for row in csv_reader:
            shop["cash"] = row[0]
            product = {}
            product["name"] = row[1]
            product["price"] = row[2]
            product["quantity"] = row[3]
            shop["products"].append(product)
    print(shop)
    return shop



# User-inputs from the 'live_cust()' function added as arguments:
def live_cust2(na_, it_, qu_, bu_):
    # Unpacking the shop["products"] list:
    for name, price, quantity in [i.items() for i in shop["products"]]:
        # Tuple unpacking to get names, prices and quantities:
        n_, name_val = name
        pr1, price_val = price
        q1, shop_quan = quantity
        if (it_ == name_val):
            cost = float(price_val) * int(qu_)
            print("============")
            print("The price of your item is: €{}".format(price_val))
            print("============")
            print("The cost of {} {} will be €{}".format(qu_, it_, cost))
            if (bu_ < cost):
                print("You do not have enough money for your order!")
                sys.exit()
            elif (qu_ > int(shop_quan)):
                print("We don't have enough of that item at the moment!")
                print("==================")
                print("We can offer you {} {}".format(int(shop_quan), it_))
                reducedCost = float(price_val) * int(shop_quan)
                print("==================")
                print("The cost of {} {} will be: €{}".format(shop_quan, it_, reducedCost))
                print("==================")
                r = csv.reader(open("shop1.csv")) 
                lines = list(r)
                for line in lines:
                    if line[1] == it_:
                        line[3] = 0
                # Shop cash is stored in the first column of the first row, using string slicing here:
                lines[0][0] = float(lines[0][0]) + reducedCost
                writer = csv.writer(open("shop1.csv", "w", newline = ''))
                writer.writerows(lines)
                # Fine:
                print("Shop balance is now: €{}".format(lines[0][0]))
                writer = csv.writer(open("shop1.csv", "w", newline = ''))
                writer.writerows(lines)
                print("====================")
                print("{} is now out of stock.".format(name_val))
                print("====================")
                #new_cust_balance = cu.deduct_money(totalCost)
                new_cust_balance = bu_ - reducedCost
                print("Please take your change of €{}".format(new_cust_balance))
                print("Thanks please come again")
            elif (bu_ > cost):
                print("==================")
                print("Price of your item is: €{}".format(price_val))
                print("==================\n")
                print("The cost of {} {} will be: €{}".format(qu_, it_, cost))
                r = csv.reader(open("shop1.csv")) 
                lines = list(r)
                for line in lines:
                    print(line[3])
                    if line[1] == it_:
                        line[3] = int(line[3]) - int(qu_)
                print(lines)
                print("\n---------")
                print(shop["cash"])
                # Shop cash is stored in the first column of the first row, using string slicing here:
                lines[0][0] = float(lines[0][0]) + cost
                writer = csv.writer(open("shop1.csv", "w", newline = ''))
                writer.writerows(lines)
                # Fine:
                print("Shop balance is now: €{}".format(lines[0][0]))
                new_shop_quantity = int(shop_quan) - int(qu_)
                print("====================")
                # Fine:
                print("There is now only {} {} left".format(new_shop_quantity, it_))
                print("====================")
                new_cust_balance = bu_ - cost
                print(new_cust_balance)
                print("Take a receipt of your change in euros: €{}".format(new_cust_balance))
                print("Thanks please come again")
            else:
                print("No such item in stock!")
                sys.exit()



def read_customer(path):
    customer = {}
    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        first_row = next(csv_reader)
        second_row = next(csv_reader)
        customer["name"] = second_row[0]
        customer["cash"] = float(second_row[1])
        customer["products"] = []
        for row in csv_reader:
            product = {}
            product["name"] = row[2]
            product["quantity"] = row[3]
            customer["products"].append(product)
            print("The items required ar: {}".format(customer["products"]))
            #if customer["products"] == shop["products"]:
            for k, v in [x.items() for x in customer["products"]]:
                for name, price, quantity in [y.items() for y in shop["products"]]:
                    cust_prod, cust_prod_name = k
                    cust_q, cust_quantity = v
                    n, name_values = name
                    pr, price_value = price
                    print("€{}".format(price_value))
                    print("Customer item(s): {}".format(name_values))
                    for cust_prod_name in name_values:
                        cost = int(product["quantity"]) * float(price_value)
                        print("The cost of the order will be: €{}".format(cost))
                    else:
                        print("That item is not in stock! ")
    return customer


def order_cost(customer):  
    for k, v in [x.items() for x in customer["products"]]:
        for name, price, quantity in [y.items() for y in shop["products"]]:
            cust_prod, cust_prod_name = k
            cust_q, cust_quantity = v
            n, name_value = name
            pr, price_value = price
            q, shop_quan = quantity
            if cust_prod_name == name_value:
                cost = float(price_value) * int(cust_quantity)
                print("The cost of your purchase is: €{}".format(cost))
                #shop_quan -= cust_quantity
                if cust_quantity > shop_quan:
                    print("We do not have enough in stock at the moment!")
                    sys.exit(1)
                elif cost > customer["cash"]:
                    print("You do not have enough for this transaction!")
                    sys.exit(1)
                else:
                    r = csv.reader(open("shop1.csv")) 
                    lines = list(r)
                    for line in lines:
                        print(line[3])
                        if line[1] == cust_prod_name:
                            line[3] = int(line[3]) - int(cust_quantity)
                    lines[0][0] = float(lines[0][0]) + cost
                    writer = csv.writer(open("shop1.csv", "w", newline = ''))
                    writer.writerows(lines)
                    


def print_prod(product):
    print(f'NAME: {product["name"]}, PRICE:{product["price"]}, QUANTITY:{product["quantity"]}')

def print_cust(customer):
    print(f'NaMe:{customer["name"]}, BuDgEt:{customer["cash"]}')
    for product in customer["products"]:
        print(f'NAME:{product["name"]}, QUANTITY: {product["quantity"]}')

def print_shop(shop):
    print(f'Initial cash balance:{shop["cash"]}')
    for product in shop["products"]:
        print_prod(product)

    
def menu():
    print("------------------------------")
    print("THIS IS THE MAIN MENU--------------")
    print("-----------------------------------")
    print("SELECT AN OPTION  ")
    print("1. Show shop stock") 
    print("2. Customer       ")
    print("3. Live customer  ")
    op = int(input("Select an option please: "))
    if (op == 1):
        print("Showing the shop stock")
        print_shop(shop)
        sys.exit(1)

    if (op == 2):
        # This format seemed to output fine:
        read_customer("customer3.csv")
        cust = read_customer("customer3.csv")
        order_cost(cust)
        sys.exit(1)

    if (op == 3):
        na_ = input("Enter your name : ")
        it_ = input("Enter your desired item : ")
        qu_ = int(input("How many? : "))
        bu_ = float(input("Enter your budget : €"))
        print("{} wants {} of {} and has a budget of €{}".format(na_, it_, qu_, bu_))
        live_cust2(na_, it_, qu_, bu_)
        #print_cust(cust)
        #order_cost(cust, shop)
        sys.exit(1)

    else:
        print("\nInvalid selection!")
        print("You must enter a number between 1 and 3.\n")
        menu()


if __name__ == "__main__":
    shop = create_stock_shop()
    menu()
