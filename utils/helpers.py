"""
Helper functions for inventory management.
"""

import sys
from pathlib import Path

# Add parent directory to path for imports
parent_dir = Path(__file__).parent.parent
if str(parent_dir) not in sys.path:
    sys.path.insert(0, str(parent_dir))

from inventory import inventory


def highest_stock_item():
    """
    Find the item with the highest quantity in stock.
    
    Returns:
        dict: Item with highest stock quantity, or None if inventory is empty
    """
    if not inventory:
        return None
    
    return max(inventory, key=lambda item: item["quantity"])


def lowest_stock_item():
    """
    Find the item with the lowest quantity in stock.
    
    Returns:
        dict: Item with lowest stock quantity, or None if inventory is empty
    """
    if not inventory:
        return None
    
    return min(inventory, key=lambda item: item["quantity"])


def get_item_by_name(item_name):
    """
    Get an item from inventory by its name.
    
    Args:
        item_name (str): Name of the item to find
        
    Returns:
        dict: Item dictionary if found, None otherwise
    """
    for item in inventory:
        if item["item_name"].lower() == item_name.lower():
            return item
    return None


def get_total_items():
    """
    Get the total number of different items in inventory.
    
    Returns:
        int: Number of unique items
    """
    return len(inventory)

