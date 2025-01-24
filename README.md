# FootwearFortress👟

**FootwearFortress** is an inventory management tool designed to help users manage their shoe inventory efficiently. The tool allows users to view, restock, capture new stock, search for specific items, evaluate stock value, and identify top-selling products.

## Features

- **Capture Shoes**: Add new shoes to the inventory by entering the country, product code, product name, cost, and quantity.
- **View All Shoes**: Display all shoes currently in the inventory.
- **Restock Shoes**: Restock the shoe with the lowest quantity.
- **Search for a Shoe**: Search shoes by product code.
- **Evaluate Stock**: Calculate the total value of each item in the inventory.
- **Identify Top Products**: Identify the product with the highest quantity in the inventory.

## Usage

1. **Start the Program**: When the program runs, you will be presented with a menu of options.
2. **Select an Action**: Choose from the following options:
   - **Capture Shoes**: Add new shoes to your inventory.
   - **View All Shoes**: View the entire inventory.
   - **Restock Shoes**: Restock the shoe with the lowest stock.
   - **Search for a Shoe**: Search for a shoe by its product code.
   - **Calculate Value per Item**: Calculate and display the total value of each shoe.
   - **Find Product with Highest Quantity**: Identify the shoe with the highest quantity in your inventory.
   - **Exit**: Exit the program.
3. **Follow Prompts**: After selecting an option, follow the prompts to input data or view results.
4. **File Updates**: The `inventory.txt` file will be automatically updated with changes you make, such as capturing new shoes or restocking items.

### Example Workflow:
```
Welcome to FootwearFortress!
How can we assist you in building your shoe empire today?

1. Capture Shoes
2. View All Shoes
3. Restock Shoes
4. Search for a Shoe
5. Calculate Value per Item
6. Find Product with Highest Quantity
7. Exit

Enter your choice:
```

## Getting Started

To get started with **FootwearFortress**, follow these steps:

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/FaithMnisi/FootwearFortress.git
   ```

2. **Navigate to the project directory**:

   ```bash
   cd FootwearFortress
   ```

3. **Ensure you have the required files**:
   - Make sure there is an `inventory.txt` file in the same directory as the script. This file should follow the format:
     ```
     Country,Code,Product,Cost,Quantity
     ```

### Running the Program

Once you have cloned the repository and set up the files, you can run the program by executing the Python script:

```bash
python main.py
```

## License

This project is open-source and available for use without a specified license. Feel free to fork and modify it.
