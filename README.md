# Inventory Management System

A simple Python application for managing inventory and calculating stock values.

## Project Description

This project provides a basic inventory management system that:
- Stores inventory items with their names, quantities, and prices
- Calculates the total stock value
- Provides helper functions for inventory analysis

## Project Structure

```
status-accounting/
├── inventory.py          # Inventory data (list of items)
├── app.py                # Main application script
├── utils/
│   └── helpers.py        # Helper functions
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## Files Description

### `inventory.py`
Contains a list of inventory items. Each item is a dictionary with:
- `item_name`: Name of the item (string)
- `quantity`: Number of units in stock (integer)
- `price`: Price per unit (float)

### `app.py`
Main script that:
- Reads inventory data from `inventory.py`
- Calculates the total stock value (sum of quantity × price for all items)
- Displays item-wise calculations and the total value
- Contains functions for calculating item values, formatting output, and displaying inventory reports

### `utils/helpers.py`
Helper functions for inventory analysis:
- `highest_stock_item()`: Returns the item with the highest quantity (or None if inventory is empty)
- `lowest_stock_item()`: Returns the item with the lowest quantity (or None if inventory is empty)
- `get_item_by_name(item_name)`: Finds an item by name (case-insensitive, returns None if not found)
- `get_total_items()`: Returns the total number of different items in inventory

### `requirements.txt`
Python dependencies (currently none required for basic functionality)

## Installation

1. Clone or download this repository
2. Navigate to the project directory:
   ```bash
   cd status-accounting
   ```

3. (Optional) Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. Install dependencies (if any):
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Main Application

To calculate and display the total stock value:

```bash
python app.py
```

This will display:
- Each item with its quantity, price, and calculated value
- The total stock value at the end

### Using Helper Functions

You can import and use the helper functions in your own scripts:

```python
from utils.helpers import highest_stock_item, lowest_stock_item

# Get item with highest stock
highest = highest_stock_item()
print(f"Highest stock: {highest['item_name']} ({highest['quantity']} units)")

# Get item with lowest stock
lowest = lowest_stock_item()
print(f"Lowest stock: {lowest['item_name']} ({lowest['quantity']} units)")
```

## Example Output

When running `app.py`, you'll see output like:

```
============================================================
INVENTORY STOCK VALUE CALCULATION
============================================================

Laptop: 15 units × $999.99 = $14999.85
Mouse: 50 units × $29.99 = $1499.50
Keyboard: 30 units × $79.99 = $2399.70
...

------------------------------------------------------------
Total Stock Value: $XX,XXX.XX
============================================================
```

## Requirements

- Python 3.6 or higher
- No external dependencies required (see `requirements.txt`)

## License

This project is for educational purposes.

