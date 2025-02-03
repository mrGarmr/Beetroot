# Task 4

# Custom exception

# Create your custom exception named 'CustomException', you can inherit from base Exception class, 
# but extend its functionality to log every error message to a file named 'logs.txt'. 
# Tips: Use __init__ method to extend functionality for saving messages to file

import logging

class CustomException(Exception):

    def __init__(self, message):
        super().__init__(message)
        self.logger(message)

    def logger(self, message):
        logging.basicConfig(filename='logs.txt', level=logging.ERROR, format='%(asctime)s - %(message)s')
        logging.error(message)


try:
    raise CustomException("The wolf has stolen a goat")
except CustomException as e:
    print(f"Caught an exception: {e}")