"""
Main application script that reads from inventory.py and calculates total stock value.
"""

from inventory import inventory


def calculate_total_stock_value():
    """
    Calculate the total stock value by summing (quantity * price) for all items.
    
    Returns:
        float: Total stock value
    """
    total_value = 0.0
    
    for item in inventory:
        item_value = item["quantity"] * item["price"]
        total_value += item_value
        print(f"{item['item_name']}: {item['quantity']} units × ${item['price']:.2f} = ${item_value:.2f}")
    
    return total_value


def main():
    """Main function to run the inventory value calculation."""
    print("=" * 60)
    print("INVENTORY STOCK VALUE CALCULATION")
    print("=" * 60)
    print()
    
    total_value = calculate_total_stock_value()
    
    print()
    print("-" * 60)
    print(f"Total Stock Value: ${total_value:,.2f}")
    print("=" * 60)


if __name__ == "__main__":
    main()

