# 1. Function to check and return low-stock items
def get_low_stock_items(inventory, reorder_level):
    """
    Identify and return items that are below the reorder level.
    """
    # TODO: Implement logic to filter low-stock items
    pass


# 2. Function to calculate the total inventory value
def calculate_inventory_value(inventory, prices):
    """
    Calculate and return the total value of all inventory items.
    """
    # TODO: Implement logic to calculate inventory value
    pass


## Dataset: Inventory (Item, Quantity) and Prices
inventory_data = [
    ("Laptop", 5),
    ("Mouse", 20),
    ("Keyboard", 12),
    ("Monitor", 3),
    ("USB Drive", 50)
]

item_prices = {
    "Laptop": 1000,
    "Mouse": 25,
    "Keyboard": 80,
    "Monitor": 300,
    "USB Drive": 15
}


def main():
    """
    Main function to execute inventory analysis.
    """
    # TODO: Call get_low_stock_items() and print low-stock items
    # TODO: Call calculate_inventory_value() and print total value
    # TODO: Call most_stocked_item() and print most stocked item
    pass


if __name__ == "__main__":
    main()
