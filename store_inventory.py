import os
import math

# Define the Shoe class and its attributes
class Shoe:
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # Define get_cost() to return the cost of shoes
    def get_cost(self):
        return self.cost

    # Define get_quantity() to return the shoe quantity
    def get_quantity(self):
        return self.quantity

    # Define __str__ to return the class Shoe
    def __str__(self):
        return f"Country: {self.country}, Code: {self.code}, Product: {self.product}, Cost: {self.cost}, Quantity: {self.quantity}"

# Define function to read shoe data from the file
def read_shoes_data(file_name, shoes_list):
    try:
        file_path = os.path.join(os.path.dirname(__file__), file_name)
        print("File path:", file_path)  # Debugging
        with open(file_path, 'r') as file:
            next(file)  # Skip the header line
            for line in file:
                country, code, product, cost, quantity = line.strip().split(',')
                shoe = Shoe(country, code, product, float(cost), int(quantity))
                shoes_list.append(shoe)
        print("Shoe data loaded successfully.")
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Define function to capture shoe data
def capture_shoes(shoes_list):
    while True:
        try:
            country = input("Enter country: ")
            if not country:
                # Display error message if country is blank
                raise ValueError("Country cannot be empty")

            code = input("Enter the product code: ")
            if not code:
                # Display error message if product code is blank
                raise ValueError("Product code cannot be empty")

            # Check if the code already exists
            if any(shoe.code == code for shoe in shoes_list):
                print("Product code already exists. Please enter a different code.")
                continue

            product = input("Enter the product name: ")
            if not product:
                # Display error message if product name is empty
                raise ValueError("Product name cannot be empty")

            cost = input("Enter the price of the product: ")
            if not cost or not cost.isdigit():
                # Display error message if value for cost is incorrect
                raise ValueError("Invalid input. Cost must be a number.")

            quantity = input("Enter the quantity of the product: ")
            if not quantity or not quantity.isdigit():
                # Display error message if value for quantity is not an integer
                raise ValueError("Invalid input. Quantity must be a whole number.")

            cost = float(cost)
            quantity = int(quantity)

            shoe = Shoe(country, code, product, cost, quantity)

            # Add new shoes to shoe list
            shoes_list.append(shoe)
            print("Shoe added successfully.")

            # Update inventory file
            update_shoes_file(shoes_list)

            break  # Exit the loop if all inputs are valid
        except ValueError as ve:
            print(f"Error: {ve}. Please try again.")
        except Exception as e:
            print("An error occurred:", e)

# Define function to view all shoes
def view_all(shoes_list):
    if not shoes_list:
        print("No shoes available.")
    else:
        for index, shoe in enumerate(shoes_list, start=1):
            print(f"Shoe {index}:")
            print(shoe)

# Define function to restock shoes
def re_stock(shoes_list):
    if not shoes_list:
        print("No shoes available for restocking.")
        return

    # Find shoes with the lowest quantity
    lowest_quantity_shoe = min(shoes_list, key=lambda shoe: shoe.quantity)
    # Display shoes with lowest quantity
    print(f"The shoe with the lowest quantity is: {lowest_quantity_shoe}")

    # Ask user if they would like to restock the item with the lowest quantity
    add_quantity = input(f"Do you want to restock {lowest_quantity_shoe.product}? (yes/no): ").lower()
    if add_quantity == 'yes':
        try:
            # Ask user how many units need to be restocked
            additional_quantity = int(input(f"How many units of {lowest_quantity_shoe.product} do you want to add?: "))
            # Increment shoe with the lowest quantity
            lowest_quantity_shoe.quantity += additional_quantity
            print(f"{additional_quantity} units of {lowest_quantity_shoe.product} added successfully.")
            
            # Update inventory.txt
            update_shoes_file(shoes_list)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    else:
        print("No restocking performed.")

# Define function to search for a shoe by code
def search_shoe(shoes_list, code):
    for shoe in shoes_list:
        if shoe.code == code:
            # Display shoe information if the code enters matches the shoe code in inventory.txt
            print(f"Shoe found: {shoe}")
            return
    # Display message if the shoe code entered doesn't match any code in inventory.txt
    print("Shoe not found.")

# Define function to calculate value per item
def value_per_item(shoes_list):
    for shoe in shoes_list:
        # Calculate total value for each item
        total_value = shoe.cost * shoe.quantity
        # Print the total value for each item
        print(f"The total value of {shoe.product} is: {total_value}")

# Define function to find product with highest quantity
def highest_qty(shoes_list):
    if not shoes_list:
        print("No shoes available.")
    else:
        # Find shoes with the highest quantity
        highest_quantity_shoe = max(shoes_list, key=lambda shoe: shoe.quantity)
        # Display shoes with the highest quantity
        print(f"The product with the highest quantity is: {highest_quantity_shoe}")

# Function to update inventory.txt
def update_shoes_file(shoes_list):
    try:
        file_path = os.path.join(os.path.dirname(__file__), 'inventory.txt')
        with open(file_path, 'w') as file:
            file.write("Country,Code,Product,Cost,Quantity\n")
            for shoe in shoes_list:
                file.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n")
        print("Inventory file updated successfully.")
    except Exception as e:
        print(f"An error occurred while updating the inventory file: {e}")

# Main function
def main():
    shoes_list = []
    file_name = 'inventory.txt'
    read_shoes_data(file_name, shoes_list)

    while True:
        # Display menu
        print("\nWelcome to FootwearFortress")
        print("How can we assist you in building your shoe empire today?")
        print("1. Capture Shoes")
        print("2. View All Shoes")
        print("3. Restock Shoes")
        print("4. Search for a Shoe")
        print("5. Calculate Value per Item")
        print("6. Find Product with Highest Quantity")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            capture_shoes(shoes_list)
        elif choice == "2":
            view_all(shoes_list)
        elif choice == "3":
            re_stock(shoes_list)
        elif choice == "4":
            code = input("Enter the shoe code to search: ")
            search_shoe(shoes_list, code)
        elif choice == "5":
            value_per_item(shoes_list)
        elif choice == "6":
            highest_qty(shoes_list)
        elif choice == "7":
            print("\nThanks for visiting FootwearFortress! Wishing you success and stylish strides ahead!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
