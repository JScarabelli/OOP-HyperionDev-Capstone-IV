#========The beginning of the class==========

# creating a class and its attributes.
class Shoes:

    def __init__(self, country, code, product, cost, quantity):

        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # returns the cost of the shoes.
    def get_cost(self):

        return self.cost

    # returns the quantity of the shoes.
    def get_quantity(self):

        return self.quantity

    # returns a string representation of a class.
    def __str__(self):

        return "MyShoes Object"


#=============Shoe list===========

# The list will be used to store a list of objects of shoes.

shoes_list = []

#==========Functions outside the class==============


# function to read the inventory.txt file to append and return this object into the shoes_list.
def read_shoes_data():

    from tabulate import tabulate

    try:
        with open('inventory.txt', 'r') as f:
            # skip the first line
            next(f)
            for line in f:
                data = line.split(',')
                shoes = Shoes(data[0], data[1], data[2], data[3], data[4])
                shoes_list.append(shoes)

        # iterates through the shoes_list.
        data = []
        for shoe in shoes_list:
            data.append([shoe.country, shoe.code, shoe.product, shoe.cost, shoe.quantity])
        headers = ["Country", "Code", "Product", "Cost", "Quantity"]

        # print in a tabulate format the data retrieved.
        print(tabulate(data, headers, tablefmt="grid"))

        f.close()
    except FileNotFoundError:
        print("Error: File not found")

    return shoes_list


# This function allows the user to create a shoe object and append this object inside the shoes_list.
def capture_shoes():

    # requesting user for details of the shoe.
    print("Please enter the details of the shoe.")
    country = input("Country: ")
    code = input("Code: ")
    product = input("Product: ")
    cost = input("Cost: ")
    quantity = input("Quantity: ")

    # appending it to the shoes_list
    shoes = Shoes(country, code, product, cost, quantity)
    shoes_list.append(shoes)

    return shoes_list


# function that iterates over the shoes_list and returns the details from the __str__ class Shoes
def view_all():

    # import the tabulate module.
    from tabulate import tabulate

    # iterates through the shoes_list.
    data = []
    for shoe in shoes_list:
        data.append([shoe.country, shoe.code, shoe.product, shoe.cost, shoe.quantity])
    headers = ["Country", "Code", "Product", "Cost", "Quantity"]

    # print in a tabulate format the data retrieved.
    print(tabulate(data, headers, tablefmt="grid"))


# function that finds lowest quantity and re-stocked if the user wishes and updates the inventory.txt file.
def re_stock():

    # find the shoe with lowest quantity
    min_quantity = shoes_list[0].quantity
    min_quantity_shoe = shoes_list[0]
    for shoe in shoes_list:
        if int(shoe.quantity) < int(min_quantity):
            min_quantity = shoe.quantity
            min_quantity_shoe = shoe

    # prompt user
    print(f"{min_quantity_shoe.product} has the lowest quantity. Please enter the amount to add:")
    amount = int(input())

    # update the quantity
    min_quantity_shoe.quantity = int(min_quantity) + amount

    # update the data in the file
    with open('inventory.txt', 'r+') as f:
        data = f.readlines()
        f.seek(0)
        for line in data:
            if min_quantity_shoe.code in line:
                new_quantity = int(min_quantity) + amount
                line = line.replace(min_quantity, str(new_quantity))
            f.write(line)
        f.truncate()
    return shoes_list


# function that searches for a shoe through the shoe code.
def search_shoe():

    code_search = input("Please enter the shoe code: ")
    success_flag = False

    # Loop through the list searching for this item
    for count, shoe in enumerate(shoes_list):
        # If a matching item is found change the flag
        if shoe.code == code_search:
            success_flag = True

    # If our search is successful display the corresponding data
    if success_flag:
        print(f"Product:\t\t{shoes_list[count].product}\nCountry of Origin:\t{shoes_list[count].country}"
              f"\nQuantity:\t\t{shoes_list[count].quantity}\nCost:\t\t\t£{shoes_list[count].cost}\n"
              f"Code:\t\t\t{shoes_list[count].code}\n")
    # if not tell user no data found
    else:
        print("Sorry.  No shoe found with that code.")


# function that returns the value of each shoe in the shoes_list.
def value_per_item():

    # loop through the shoes_list
    for shoe in shoes_list:
        value = int(shoe.cost) * int(shoe.quantity)
        print(f"The value for {shoe.product} is £{value}")


# function that determines the product with the highest quantity and being for sale.
def highest_qty():

    # find the shoe with highest quantity
    max_quantity = shoes_list[0].quantity
    max_quantity_shoe = shoes_list[0]
    for shoe in shoes_list:
        if int(shoe.quantity) > int(max_quantity):
            max_quantity = shoe.quantity
            max_quantity_shoe = shoe

    # print the result
    print(f"The {max_quantity_shoe.product} is for sale!\n")


#==========Main Menu=============

# menu that executes each function above.

while True:
    print("Welcome to the Shoe Inventory\n")
    print("1. Read shoes data\n2. Capture shoes data\n3. View all shoes\n4. "
          "Re-stock shoe\n5. Search shoe\n6. Value per item\n7. Highest quantity\n8. Quit\n")
    selection = int(input("Please select an option: "))

    # condition to execute each function depending on the user's choice.
    if selection == 1:
        read_shoes_data()
    elif selection == 2:
        capture_shoes()
    elif selection == 3:
        view_all()
    elif selection == 4:
        re_stock()
    elif selection == 5:
        search_shoe()
    elif selection == 6:
        value_per_item()
    elif selection == 7:
        highest_qty()
    elif selection == 8:
        print("Thank you for using the inventory system")
        break
    else:
        print("Invalid selection. Please try again")



"""
# Ask for the code
    code = input("Please enter the code of the shoe: ")

    # Check if the code is not blank
    if code != '':

        # Check if the code exists in the list
        if any(shoe.code == code for shoe in shoes_list):

            # Search for the code in the list
            for shoe in shoes_list:
                if shoe.code == code:
                    print(f"Country: {shoe.country}\nCode: {shoe.code}\nProduct: {shoe.product}\n"
                          f"Cost: {shoe.cost}\nQuantity: {shoe.quantity}")
                    return Shoes(shoe.country, shoe.code, shoe.product, int(shoe.cost), int(shoe.quantity))
                else:
                    print("No shoe found with that code")
                    return None


"""


