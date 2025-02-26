# File Context Manager class
# Create your own class, which can behave like a built-in function 'open'. 
# Also, you need to extend its functionality with counter and logging. 
# Pay special attention to the implementation of '__exit__' method, 
# which has to cover all the requirements to context managers mentioned here:

import logging
import time

class FileContextManager:
    '''Own class, which can behave like a built-in function 'open'.'''
    open_count = 0 #counter that increses when entering to contex
    
    def __init__(self, filepath, mode):
        self.filepath = filepath
        self.mode = mode
        self._file = None
        
        # Set up logging
        logging.basicConfig(level=logging.INFO, format="%(asctime)s -== %(levelname)s ==- %(message)s")
        self.logger = logging.getLogger("FileContextManager")
    
    # __enter__ is called when entering the context
    def __enter__(self):
        FileContextManager.open_count += 1  # the class-level open_count
        
        self.logger.info(f"Opening file: {self.filepath} (Total count: {FileContextManager.open_count})")
        self._file = open(self.filepath, self.mode)
        return self._file
    
    # __exit__ is called when exiting the context
    def __exit__(self, exc_type, exc_value, traceback):
        if self._file:
            self.logger.info(f"Closing file: {self.filepath}")
            self._file.close()

        # Log exception if there problem
        if exc_type:
            self.logger.error(f"Exception occurred: {exc_value}")
        return False

# Example usage:
if __name__ == "__main__":
    #  'example.txt' is a file present in your directory
    with FileContextManager("example.txt", "w") as file:
        file.write("Hello, world!\n")

    with FileContextManager("example.txt", "r") as file:
        content = file.read()
        print(content)

    # Further usage will continue to increment the count
    with FileContextManager("example.txt", "r") as file:
        content = file.read()
        print(content)
