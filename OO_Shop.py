# Object Oriented progam:
import csv
import sys

class Product:
    # Initializing attributes of the class:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    # repr method returns a string format of an object in Python:
    def __repr__(self):
        return f'NAME: {self.name} PRICE: {self.price}'


class ProductStock:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity
    
    def name(self):
        return self.product.name
    
    def unit_price(self):
        return self.product.price
        
    def __repr__(self):
        return f"{self.product} QUANTITY: {self.quantity}"


class Customer:
    def __init__(self, path):
        self.shopping_list = []
        # Reading data from a csv file:
        with open(path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            # Python 'next' method reads the next line/row in a file each time it's called:
            first_row = next(csv_reader)
            sec_row = next(csv_reader)
            # Extracting the first element from the row, which is element '0':
            self.name = sec_row[0]
            self.budget = float(sec_row[1])
            for row in csv_reader:
                item = row[2]
                price = Shop.item_price(self, "shop1.csv", item)
                quantity = float(row[3])
                self.shopping_list = [item, self.budget, price, quantity]
        

    def deduct_money(self, path, amount):
            r = csv.reader(open(path), delimiter=',')
            csv_reader = next(r)
            csv_reader2 = next(r) 
            lines = list(csv_reader2)
            for line in lines:
                line[1] == float(line[1]) - float(amount)
                # 'csv.writer()' converts data into a delimited string:
                writer = csv.writer(open(path, "w", newline = ''))
                # 'writerows()' writes all the data of 'lines' object into a file:
                writer.writerows(lines)
    
    def updating(self):
        cust_budget = self.shopping_list[1]
        print("Customer budget: {}".format(cust_budget))
        item = self.shopping_list[0]
        print(item)
        quantity = self.shopping_list[3]
        if (item == Shop.item_identity(self, "shop1.csv", item)):
            price = Shop.item_price(self, "shop1.csv", item)
            cost = float(price) * int(quantity)
            print("********")
            sh1 = Shop("shop1.csv")
            print("------")
            print(item)
            print(price)
            print("------")
            # At last! !!!
            if (cust_budget >= cost):
                sh1.add_money(cost)
                sh1.update_quantity(item, quantity)
                path = input("Enter your customer csv file: ")
                Customer.deduct_money(path, cost)
            elif (quantity > sh1.item_quantity("shop1.csv", item)):
                print("We don't have enough in stock!")
                print("We can offer you {} {}".format(int(sh1.item_quantity("shop1.csv", self.item)), self.item))
                #Deduct the price from customer balance
                newTotalCost = price * sh1.item_quantity("shop1.csv", self.item)
                print("==================")
                print("The cost of {} {} will be: €{}".format(sh1.item_quantity("shop1.csv", self.item), self.item, newTotalCost))
                print("==================")
                #self.budget -= newTotalCost
                #Add the price of that to shop 
                sh1.add_money(newTotalCost)
                #Deduct from the shops quantity
                sh1.update_quantity(self.item, sh1.item_quantity("shop1.csv", self.item))
                #print("Shop balance is now: €{}".format(lines[0][0]))
                print("====================")
                print("{} is now out of stock.".format(self.item))
                sys.exit()
            else:
                print("You dont' have enough for the transaction!")
                sys.exit()
        else:
            print("We don't have what you are looking for!")

    
    def __repr__(self):
        
        str = f"{self.name} wants to buy: "
        print(str)
        item = self.shopping_list[0]
        quantity = int(self.shopping_list[3])
        print("{} of {}".format(quantity, item))


class Shop:
    def __init__(self, path):
        self.stock = []
        with open(path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            first_row = next(csv_reader)
            #secondRow = next(csv_reader)
            self.cash = float(first_row[0])
            self.item = first_row[1]
            self.price = float(first_row[2])
            self.quantity = int(first_row[3])
            #print(self.cash)
            for row in csv_reader:
                p = Product(row[1], float(row[2]))
                ps = ProductStock(p, float(row[3]))
                #price = float(row[2])
                self.stock.append(ps)
                #print(self.stock)
    
    def item_quantity(self, path, item):
        with open(path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                if item == row[1]:
                    return float(row[3])

    def item_identity(self, path, item):
        with open(path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            #first_row = next(csv_reader)
            #secondRow = next(csv_reader)
            for row in csv_reader:
                #print(row[1])
                if item == row[1]:
                    return row[1]

    def add_money(self, amount): 
        r = csv.reader(open("shop1.csv")) 
        lines = list(r)
        lines[0][0] = self.cash + amount
        print("Shop balance is now: €{}".format(lines[0][0]))
        #lines[0][0] = "{:.2f}".format(self.cash + amount)
        writer = csv.writer(open("shop1.csv", "w", newline = ''))
        writer.writerows(lines)

    def update_quantity(self, item, quantity):
        r = csv.reader(open("shop1.csv")) 
        lines = list(r)
        for line in lines:
            #print(line[3])
            if line[1] == item:
                line[3] = int(line[3]) - int(quantity)
        writer = csv.writer(open("shop1.csv", "w", newline = ''))
        writer.writerows(lines)

    
    def item_price(self, path, item):
        with open(path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            #first_row = next(csv_reader)
            for row in csv_reader:
                if item == row[1]:
                    return float(row[2])

    def __repr__(self):
        str = ""
        str += f'Shop has {self.cash} in cash\n'
        for item in self.stock:
            str += f"{item}\n"
        return str


class live_customer:
    def __init__(self):
        self.name = input("Enter your name : ")
        self.item = input("Enter your desired item : ")
        self.quantity = int(input("How many? : "))
        self.budget = float(input("Enter your budget : €"))
        print("{} wants {} of {} and has a budget of €{}".format(self.name, self.quantity, self.item, self.budget))
        # Made an instance of the Shop class:
        sh = Shop("shop1.csv")
        price = sh.item_price("shop1.csv", self.item)
        if (self.item != sh.item_identity("shop1.csv", self.item)):
            print("No such item in stock!")
            sys.exit()
        print("==================")
        print("Price of your item is: €{:.2f}".format(price))
        print("==================")
        #self.cash = sh.add_money(self.budget)
        #print(self.cash)
        totalCost = price * self.quantity
        # Instance of the Customer class:
        #cu = Customer("cust1.csv")
        #totalCost = ps2.cost
        if (self.budget < totalCost):
            ValueError
            print("You do not have enough money for your order!")
            sys.exit()
        elif (self.quantity > sh.item_quantity("shop1.csv", self.item)):
            print("We don't have enough of that item at the moment!")
            print("We can offer you {} {}".format(int(sh.item_quantity("shop1.csv", self.item)), self.item))
            #Deduct the price from customer balance
            newTotalCost = price * sh.item_quantity("shop1.csv", self.item)
            print("==================")
            print("The cost of {} {} will be: €{}".format(sh.item_quantity("shop1.csv", self.item), self.item, newTotalCost))
            print("==================")
            #self.budget -= newTotalCost
            #Add the price of that to shop 
            sh.add_money(newTotalCost)
            #Deduct from the shops quantity
            sh.update_quantity(self.item, sh.item_quantity("shop1.csv", self.item))
            #print("Shop balance is now: €{}".format(lines[0][0]))
            print("====================")
            print("{} is now out of stock.".format(self.item))
            print("====================")
            #new_cust_balance = cu.deduct_money(totalCost)
            new_cust_balance = self.budget - newTotalCost
            print("Please take your change of €{}".format(new_cust_balance))
            print("Thanks please come again")
            sys.exit()
        print("The cost of {} {} will be €{}".format(sh.item_quantity("shop1.csv", self.item), self.item, totalCost))
        print("=================")
        sh.add_money(totalCost)
        #print(new_shop_balance)
        #print("Shop balance is now: €{}".format(new_shop_balance))
        #new_shop_quantity = sh.deduct_qu("shop1.csv", self.item, self.quantity)
        sh.update_quantity(self.item, self.quantity)
        print("=================")
        new_cust_balance = self.budget - totalCost
        print(new_cust_balance)
        print("Take a receipt of your change in euros: €{}".format(new_cust_balance))
        print("Thanks please come again")


def menu():
    print("---------------------")
    print("THIS IS THE MAIN MENU")
    print("---------------------")
    print("SELECT AN OPTION: ")
    print("1. Displaying the shop stock") 
    print("2  Customer orders")
    print("3. Live customer")
    enter = int(input("\n Please select option from the main menu: "))
    if (enter == 1):
        s1 = Shop("shop1.csv")
        print("Showing the shop stock")
        print(s1.stock)
        print(s1)
       
    elif (enter == 2):    
        c1 = Customer("customer1.csv")
        c1.updating()
        c2 = Customer("customer1.csv")
        print(c2)
        c2.updating()
        c3 = Customer("customer3.csv")
        c3.updating()
        c4 = Customer("customer4.csv")
        c4.updating()
        c5 = Customer("customer5.csv")
        c5.updating()


    elif (enter == 3):            
        live_customer()

    else:
        print("\nInvalid selection!")
        print("You must enter a number between 1 and 3.\n")
        menu()


if __name__ == "__main__":
    menu()