"""module to store cafe stock """
stock = {
    "pasta" : {
        "price" : 5.00,
        "stock" : 5,
    },
    "sandwich" : {
        "price" : 4.50,
        "stock" : 2
    },
    "baked potato" : {
        "price" : 4.50,
        "stock" : 3
    },
    "chips" : {
        "price" : 2.50,
        "stock" : 0
    },
    "coffee" : {
        "price" : 2.00,
        "stock" : 10
    },
    "tea" : {
        "price" : 1.50,
        "stock" : 7
    }
}

owner_print_str = {
    "main" : """When using this application as owner, you have the following commands available:
          
          * stock - let's you view current stock and amend things like price, stock levels ect.
          * product - allows you to add or remove products
          * about - get more information abot currently availble functionality
          * help - get a list of commands
          * back - go back to the previous menu
          * exit - exit the app          
        """,
    "owner_stock" : """\nYou can amend any existing product by entering the following command:

          amend item

Where 'item' is the name of one of the products listed above. You will then be able to to choose whih property you would like to change.

To view other available commands enter 'help'
    """,
    "owner_stock_help" : """Following commands are available:
        * amend item - where item is the product you'd like to change the price or stock level of
        * back - tkes you back to the main owner mey
        * help - brings up this list of commands
        * exit - exit the app

    """,
    "amend_item" : """The following commands are available:
          
          * price x - where 'x' is the new price
          * stock x - where 'x' is the stock level
          * about - get more information abot currently availble functionality
          * help - get a list of commands
          * back - go back to the previous menu
          * exit - exit the app          
        """,
    "amend_item_about" : """price x - where x is the new price
        example: price 2.50
    price can be changed to any positive number

    stock x - where x is the new stock
        example: stock 7
    stock can be changed to any positive number""",
    "product" : """\nYou can either add or remove products to the the menu. Choose the required functionality with the following commands:

          add item
          remove item

Where 'item' is the name of the product you'd like to add/remove. 

To view other available commands enter 'help'
"""
}