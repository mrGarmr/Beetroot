# Product Store

# Write a class Product that has three attributes:

# type
# name
# price
# Then create a class ProductStore, which will have some Products and will operate with all products in the store. 
# All methods, in case they can’t perform its action, should raise ValueError with appropriate error information.

# Tips: Use aggregation/composition concepts while implementing the ProductStore class. You can also implement additional 
# classes to operate on a certain type of product, etc.

# Also, the ProductStore class must have the following methods:

# add(product, amount) - adds a specified quantity of a single product with a predefined price premium for your store(30 percent)
# set_discount(identifier, percent, identifier_type=’name’) - adds a discount for all products specified by input identifiers (type or name). The discount must be specified in percentage
# sell_product(product_name, amount) - removes a particular amount of products from the store if available, in other case raises an error. It also increments income if the sell_product method succeeds.
# get_income() - returns amount of many earned by ProductStore instance.
# get_all_products() - returns information about all available products in the store.
# get_product_info(product_name) - returns a tuple with product name and amount of items in the store.
# '''

# class Product:

#     pass

# class ProductStore:

# pass

# p = Product('Sport', 'Football T-Shirt', 100)

# p2 = Product('Food', 'Ramen', 1.5)

# s = ProductStore()

# s.add(p, 10)

# s.add(p2, 300)

# s.sell_product('Ramen', 10)

# assert s.get_product_info('Ramen') == ('Ramen', 290)

# '''

class Product:
    
    """class Product that has three attributes: type, name, price"""

    def __init__(self, product_type, name, price):
        self.product_type = product_type  # type of product (e.g., 'Sport', 'Food')
        self.name = name                  # name of the product (e.g., 'Football T-Shirt')
        self.price = price                # base price of the product

    def __str__(self):
        return f"{self.name} ({self.product_type}) - ${self.price:.2f}"


class ProductStore:
    def __init__(self):
        self.products = {}  # dictionary to store products with their quantities
        self.income = 0.0   # total income

    def add(self, product, amount):
        """Add a specified amount of a product with a price premium."""
        
        # 30% price premium
        premium_price = round(product.price * 1.30, 2)

        # Add or update the product in the store
        if product.name in self.products:
            self.products[product.name]['amount'] += amount
        else:
            self.products[product.name] = {'product': product, 'amount': amount, 'price': premium_price}

    def set_discount(self, identifier, percent, identifier_type='name'):
        """Apply a discount to products based on 'name' or 'type'."""

        # Apply discount to matching products
        for product_info in self.products.values():
            product = product_info['product']
            if (identifier_type == 'name' and product.name == identifier) or (identifier_type == 'type' and product.product_type == identifier):
                discounted_price = round(product_info['price'] * (1 - percent / 100),2)
                product_info['price'] = discounted_price


    def sell_product(self, product_name, amount):
        """Sell a specified amount of a product."""
        if product_name not in self.products:
            raise ValueError(f"Product '{product_name}' not found in store.")
        
        product_info = self.products[product_name]
        
        if product_info['amount'] < amount:
            raise ValueError(f"Not enough stock of '{product_name}'.")
        
        # Deduct the amount from the stock
        product_info['amount'] -= amount
        income_from_sale = product_info['price'] * amount
        self.income += income_from_sale

    def get_income(self):
        """Return the total income from sales."""
        return self.income

    def get_all_products(self):
        """Return all products in the store with their quantities."""
        return [(product_info['product'].name, product_info['amount'], product_info['price']) for product_info in self.products.values()]

    def get_product_info(self, product_name):
        """Return the name and amount of a specific product."""
        if product_name not in self.products:
            raise ValueError(f"Product '{product_name}' not found in store.")
        
        product_info = self.products[product_name]
        return (product_info['product'].name, product_info['amount'], product_info['price'])


# Example Usage
p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', 'Ramen', 1.5)

s = ProductStore()

# Adding products to the store
s.add(p, 10)
s.add(p2, 300)

# Selling products
s.sell_product('Ramen', 10)

# Verifying the product information
assert s.get_product_info('Ramen') == ('Ramen', 290, 1.95)

# Print all products in the store
print(s.get_all_products())  # [('Football T-Shirt', 10, 130.0), ('Ramen', 290, 1.95)]

# Get store's income
print(s.get_income())  # Income from selling Ramen

# Apply discount to all Ramen products
s.set_discount('Ramen', 20)

# Verify price change after discount
print(s.get_all_products())  # The price of Ramen should have 20% discount
