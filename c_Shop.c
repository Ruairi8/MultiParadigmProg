// C program:
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>

// Creating structs to store information:
struct Product {
    // The asterisk, '*' is used to initialize a pointer in c language:
	char* name;
	double price;
};

struct ProductStock {
	struct Product product;
	int quantity;
}ProductStock;

struct Shop {
	double cash;
	struct ProductStock stock[20];
	int index;
};

struct Customer {
    char* name;
    double budget;
    struct ProductStock shoppingList[18];
}cust;

// '#define allows a user to specify lengths, for example how many characters a variable name can have:
#define FILE_NAME 40
#define MAX_LINE_CHARS 300

int updateCashShop() {
	//creating pointers for our file, and a temporary file:
    FILE *file, *temp;
    char filename[FILE_NAME];
    char temp_filename[FILE_NAME];
    // character array to store each line read in from file to temp file:
    char buffer[MAX_LINE_CHARS];
    // store replacement line:
    char replace[MAX_LINE_CHARS];
    int replace_line = 1;

    // 'strcpy()' copies the string pointed by source to the destination:
    strcpy(temp_filename, "temp_");
    // 'strcat()' joins two strings together, the result is stored in 'temp_filename':
    strcat(temp_filename, "shop2.csv"); //or filename here
    fflush(stdin);

    printf("New line: ");
    fgets(replace, MAX_LINE_CHARS, stdin);

    file = fopen("shop2.csv", "r");
    temp = fopen(temp_filename, "w");

    bool keep_reading = true;
    int current_line = 1;

    do {
        // 'fgets()' reads a line from the stream and stores it in the buffer character array:
        fgets(buffer, MAX_LINE_CHARS, file);
        // 'feof()' picks up when the end of a file has been reached. The boolean 'keep_reading' 
        // is set to false if the end of the file has been reached:
        if (feof(file)) keep_reading = false;
        else if (current_line == replace_line)
           // 'fputs' writes the replace string into the temporary file: 
           fputs(replace, temp);
        else fputs(buffer, temp);
        // '++' is used to increment a variable by 1:
        current_line++;

    } while (keep_reading);
    fclose(file);
    fclose(temp);
    remove("shop2.csv");
    rename(temp_filename, "shop2.csv");
    //return 0;
}

// Creating a fucntion using the 'int' keyword:
int updateQuantityShop() {
	// ONLY READING FIRST LINE OF FILE
	//creating pointers for our file, and a temporary file:
    FILE *file, *temp;
    char filename[FILE_NAME];
    char temp_filename[FILE_NAME];
    // character array to store each line read in from file to temp file:
    char buffer[MAX_LINE_CHARS];
    // store replacement line:
    char replace[MAX_LINE_CHARS];
	// Maybe set this to amount of line in the file?
    int replace_line = 0;

    //filename = fopen("shop2.csv");

    strcpy(temp_filename, "in temporary file");
    strcat(temp_filename, "shop2.csv"); //or filename here
	
	printf("Replace line number: ");
	fgets(replace_line, MAX_LINE_CHARS, stdin);
	//scanf("%d", &replace_line);

    //fflush(stdin);

    printf("New line: ");
    fgets(replace, MAX_LINE_CHARS, stdin);

    file = fopen("shop2.csv", "r");
    temp = fopen(temp_filename, "w");

    bool keep_reading = true;
    int current_line = 0;

    do {
        fgets(buffer, MAX_LINE_CHARS, file);
        if (feof(file)) keep_reading = false;
        else if (current_line == replace_line)
           fputs(replace, temp);
        else fputs(buffer, temp);
        current_line++;

    } while (keep_reading);
    fclose(file);
    fclose(temp);
    remove("shop2.csv");
    rename(temp_filename, "shop2.csv");
    //return 0;
}


struct Shop createAndStockShop()
{
	struct Shop shop = { 200 };
    FILE * fp;
    char * line = NULL;
    size_t len = 0;
    ssize_t read;

    fp = fopen("shop2.csv", "r");
    // Error handling if there is nothing in the csv file:
    if (fp == NULL)
        exit(EXIT_FAILURE);

// 'getline()' function to read text in the file:
    while ((read = getline(&line, &len, fp)) != -1) {
        // 'strtok()' breaks a string into tokens divided by a specified delimiter, in this case a comma
        // because the csv file is comma-separated:
		char *n = strtok(line, ",");
		char *p = strtok(NULL, ",");
		char *q = strtok(NULL, ",");
        // 'atoi()' changes a string type to an integer type:
		int quantity = atoi(q);
        // 'atof()' changes a string type to a float type:
		double price = atof(p);
        // Dynamically allocating memory of a specified size:
		char *name = malloc(sizeof(char) * 50);
		strcpy(name, n);
		struct Product product = { name, price };
		struct ProductStock stockItem = { product, quantity };
		shop.stock[shop.index++] = stockItem;
		// printf("NAME OF PRODUCT %s PRICE %.2f QUANTITY %d\n", name, price, quantity);
    }
	return shop;
}


double find(struct Shop s, char* name){
    for(int i = 0; i < shop->index; i++){
        if(strcmp(name, shop->stock[i]->product->name) == 0){
            return shop->stock[i]->product->price;
        }
    }
    return -1;
};


struct Customer customer(path) {
	char* name;
	double budget;
	struct ProductStock{ shoppingList[10]; 
	                     int quantity; 
						 double price; };
	int index;
    FILE * fp;
    char * line = NULL;
    size_t len = 0;
    ssize_t read;

    fp = fopen(path, "r");
    if (fp == NULL)
        exit(EXIT_FAILURE);

    while ((read = getline(&line, &len, fp)) != -1) {
		char *n = strtok(line, ",");
		char *b = strtok(NULL, ",");
		char *i = strtok(NULL, ",");
		char *q = strtok(NULL, ",");
		double *budget = atof(b);
		char *item = malloc(sizeof(char) * 50);
		char *name = malloc(sizeof(char) * 50);
		int *quantity = atoi(q);
		strcpy(name, n);
		printf(budget, item, name, quantity);
        if (strcmp(item, product->name)!=0) {
			printf("We don't have that item!");
		}
		else if (quantity > shop->quantity) {
			printf("We don't have enough of this product!");
		}
		double TotalCost = 0;
        struct Product prod1 = { "Butter", 0.0 };
		struct Product prod2 = { "Milk", 0.0 };
		struct Product prod3 = { "Apples", 0.0 };
		struct Product prod4 = { "Potatoes", 0.0 };
		struct Product prod5 = { "Eggs (6 pack", 0.0 };
		struct ProductStock Stock1 = { prod1, 20 };
		struct ProductStock Stock2 = { prod2, 7 };
		struct ProductStock Stock3 = { prod3, 10 };
		struct ProductStock Stock4 = { prod4, 60 };
		struct ProductStock Stock5 = { prod5, 12 };
		struct ProductStock array[] = { Stock1, Stock2, Stock3, Stock4, Stock5};
		struct Shop shop = createAndStockShop();
        // Iterating through the array:
		for(int i =0; i < 5; i++) {
			struct Product p = array[i]->product;
			double price = find(shop, p->name);
			printf("The price of %s is %.2f\n", p->name, price)
			double items_cost = array[i]->quantity * p->price;
			printf("You want %d of %s, so that'll cost %.2f\n", array[i].quantity, p.name, items_cost);
			TotalCost += items_cost;
    }
    printf("Total cost to customer is: %.2f", TotalCost)
    return 0;
    };
}

//struct Customer liveCustomer
struct liveCustomer() {
    char *prod_name = (char*) malloc(10 * sizeof(char));
    char *quan = (char*) malloc(4 * sizeof(char)); 
    char *customter_name = malloc(sizeof(char) * 40);
    char *b = (char*) malloc(10 * sizeof(char)); 
    // read in customer name, budget
    printf("Enter your name:\t");
    scanf("%s", customer_name);
    printf("Enter your desired item:\t");
    scanf("%s", prod_name);
    printf("How many?");
    scanf("%d", quan);
    printf("Enter your budget:\t");
    scanf("%s",b);      
    // 'atoi()' used to convert a string type to an integer type:
    int quantity = atoi(quan);
    // 'atof() converts a string type to a floating point number:
    double budget = atof(b);
    double totalCost = quantity * shop.stock[i].product.price;
    double find(struct Shop s, char* prod_name);
    
    double totalCost = quantity * shop.stock[i].product.price;
        if (budget < totalCost) {
            printf("You don't have enough money for your order!");
            exit(0);
        }
        else if (quan > s.quantity) {
            printf("We don't have enough of that item at the moment!");
            printf("We can offer you %d %s", shop_quan, prod_name);
            reducedCost = float(price_val) * int(shop_quan);
            printf("==================");
            printf("Price of your item is: €%d", s.stock[i].product.price);
            printf("==================");
            printf("The cost of %d of %s will be: €%d", quan, prod_name, reducedCost)
            printf("================="); 
                }
        else {
            (printf("No such item!"));
        }
    for(int i = 0; i < s.index; i++){
        if(strcmp(prod_name, shop.stock[i].product.name) == 0) {
            updateQuantityShop();
            updateCashShop();
        }
    }
    return -1
    }
    printf("==================");
    printf("Price of your item is: €%d", product.price);
    printf("==================\n");
    struct Product product = { prod_name, price };
    struct ProductStock item = { product, prod_quan };
    //struct Customer customer(path) cust;
    cust.shoppingList[customer.index++] = item;
    printf("The cost of %d of %s is €%d", quantity, prod_name, totalCost);
    printf("====================");
    double new_shop_balance = shop.cash + totalCost;
    updateCashShop();
    updateQuantityShop();
    //new_shop_balance = sh.add_money(totalCost)
    printf("====================");
    printf(new_shop_balance);
    printf("Shop balance is now: €{}".format(new_shop_balance));
    new_shop_quantity = shop.quanity - quantity;
    printf("====================");
    printf("There is now only %d %s left.", new_shop_quantity, item);
    printf("Take a receipt of your change in euros: €%d", new_cust_balance);
    printf("====================");
    printf("Thanks please come again");           
    menu();
}


void printProduct(struct Product p)
{
	printf("PRODUCT NAME: %s \nPRODUCT PRICE: %.2f\n", p.name, p.price);
	printf("-------------\n");
}

void printCustomer(struct Customer c)
{
	printf("CUSTOMER NAME: %s \nCUSTOMER BUDGET: %.2f\n", c.name, c.budget);
	printf("-------------\n");
	for(int i = 0; i < c.index; i++)
	{
		printProduct(c.shoppingList[i].product);
		printf("%s ORDERS %d OF ABOVE PRODUCT\n", c.name, c.shoppingList[i].quantity);
		double cost = c.shoppingList[i].quantity * c.shoppingList[i].product.price; 
		printf("The cost to %s will be €%.2f\n", c.name, cost);
	}
}

struct Shop createAndStockShop()
{
	struct Shop shop = { 200 };
    FILE * fp;
    char * line = NULL;
    size_t len = 0;
    ssize_t read;

    fp = fopen("shop2.csv", "r");
    if (fp == NULL)
        exit(EXIT_FAILURE);

    while ((read = getline(&line, &len, fp)) != -1) {
        // printf("Retrieved line of length %zu:\n", read);
        // printf("%s IS A LINE", line);
		char *n = strtok(line, ",");
		char *p = strtok(NULL, ",");
		char *q = strtok(NULL, ",");
		int quantity = atoi(q);
		double price = atof(p);
		char *name = malloc(sizeof(char) * 50);
		strcpy(name, n);
		struct Product product = { name, price };
		struct ProductStock stockItem = { product, quantity };
		shop.stock[shop.index++] = stockItem;
		// printf("NAME OF PRODUCT %s PRICE %.2f QUANTITY %d\n", name, price, quantity);
    }
	return shop;
}

void printShop(struct Shop s)
{
	printf("Shop has %.2f in cash\n", s.cash);
	for (int i = 0; i < s.index; i++)
	{
		printProduct(s.stock[i].product);
		printf("The shop has %d of the above\n", s.stock[i].quantity);
	}
}

void menu() {
    int choice;
    do{
    printf("---------------------");
    printf("THIS IS THE MAIN MENU");
    printf("---------------------");
    printf("SELECT AN OPTION: ");
    printf("1. Display shop stock");
    printf("2  Customer Orders");
    printf("3. Live customer");
    printf("\n Please select option from the main menu: ");
    scanf("%d",&choice);
    
    switch(choice) { 
    case 1:
	    printf("Showing the stock\n");
		printf(Shop.stock);
		printf("*****************");
    case 2:
        Customer("customer1.csv");
        updateQuantityShop();
        updateCashShop();
        Customer("customer2.csv");
        updateQuantityShop();
        updateCashShop();
        Customer("customer3.csv");
        updateQuantityShop();
        updateCashShop();
        Customer("customer4.csv");
        updateQuantityShop();
        updateCashShop();
        Customer("customer5.csv");
	    updateQuantityShop();
	    updateCashShop();

	case 3:
	    printf(liveCustomer());
	case 4:
	    printf("Invalid entry! Please enter a number between 1 and 3: ");
		scanf("%d",&choice);
	}
	}
}

int main() {
    menu();
};



