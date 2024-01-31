# Python cafe app

## Description

A simple application to practice TDD, error handling, and writing to files.

The app simulates a cafe and the user can interact with it as either the owner or a customer

### Owner
While interacting with the application as the owner the user can:
- Add and remove products from the stock dictionary in `data/cafe_data.py`
- Amend the price and stock level properties for existing items in the stock dictionary.


### Customer
As a customer you can view the menu and order items available in the stock dictionary. These items are removed from stock and stored in an order dictionary. If an item isn't in stock, or there isn't enough to fill the customer order, you'll be notified and asked to amend your order.

You can view the items stored in order, and then get the total by asking for the bill.

## Usage

Run the app with the following command in `python_cafe`:
```md
python cafe.py
```
 
 All interaction with the app is completed through the CLI. 

### Testing

Testing with pytest can be run by using the following command in `python_cafe`:
```md
pytest
``` 
