# Dataset for test-taker reference (do not modify)
inventory_data = [
    ("Tablet", 8),
    ("Pen Drive", 60),
    ("Router", 4),
    ("Camera", 2),
    ("HDMI Cable", 30)
]

item_prices = {
    "Tablet": 300,
    "Pen Drive": 20,
    "Router": 100,
    "Camera": 500,
    "HDMI Cable": 10
}

def get_low_stock_items(inventory, reorder_level):
    """
    TODO: Return a list of item names whose stock is less than reorder_level which is below 10
    """
    pass


def calculate_inventory_value(inventory, prices):
    """
    TODO: Calculate and return total inventory value 
    as (quantity * unit price) for each item.
    """
    pass


# Sample function calls (expected output should match test cases)
low_stock_items = get_low_stock_items(inventory_data, 10)
print("Items to Restock:", low_stock_items)

total_inventory_value = calculate_inventory_value(inventory_data, item_prices)
print("Total Inventory Value: $", total_inventory_value)

