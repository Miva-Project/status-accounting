"""
Main application script that reads from inventory.py and calculates total stock value.
"""

from inventory import inventory


def calculate_item_value(item):
    """
    Calculate the value of a single inventory item.
    
    Args:
        item (dict): Item dictionary with 'quantity' and 'price' keys
        
    Returns:
        float: Item value (quantity * price)
    """
    return item["quantity"] * item["price"]


def calculate_total_stock_value():
    """
    Calculate the total stock value by summing (quantity * price) for all items.
    
    Returns:
        float: Total stock value
    """
    return sum(calculate_item_value(item) for item in inventory)


def format_item_line(item):
    """
    Format a single item for display.
    
    Args:
        item (dict): Item dictionary
        
    Returns:
        str: Formatted string for the item
    """
    item_value = calculate_item_value(item)
    return f"{item['item_name']}: {item['quantity']} units × ${item['price']:.2f} = ${item_value:.2f}"


def display_inventory_items():
    """
    Display all inventory items with their calculated values.
    """
    for item in inventory:
        print(format_item_line(item))


def display_header():
    """Display the header for the inventory report."""
    print("=" * 60)
    print("INVENTORY STOCK VALUE CALCULATION")
    print("=" * 60)
    print()


def display_footer(total_value):
    """
    Display the footer with total stock value.
    
    Args:
        total_value (float): Total stock value to display
    """
    print()
    print("-" * 60)
    print(f"Total Stock Value: ${total_value:,.2f}")
    print("=" * 60)


def main():
    """Main function to run the inventory value calculation."""
    display_header()
    display_inventory_items()
    total_value = calculate_total_stock_value()
    display_footer(total_value)


if __name__ == "__main__":
    main()

