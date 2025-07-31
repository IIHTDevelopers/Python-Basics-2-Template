
def get_low_stock_items(inventory, reorder_level):
    return [item for item, stock in inventory if stock < reorder_level]

def calculate_inventory_value(inventory, prices):
    return sum(stock * prices[item] for item, stock in inventory if item in prices)

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

low_stock_items = get_low_stock_items(inventory_data, 10)
print("Items to Restock:", low_stock_items)

total_inventory_value = calculate_inventory_value(inventory_data, item_prices)
print("Total Inventory Value: $", total_inventory_value)
