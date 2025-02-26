# Writing tests for context manager
# Take your implementation of the context manager class from Task 1 and write tests for it. 
# Try to cover as many use cases as you can, positive ones when a file exists and everything works as designed. 
# And also, write tests when your class raises errors or you have errors in the runtime context suite.


# File Context Manager class
# Create your own class, which can behave like a built-in function 'open'. 
# Also, you need to extend its functionality with counter and logging. 
# Pay special attention to the implementation of '__exit__' method, 
# which has to cover all the requirements to context managers mentioned here:

import logging

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
        
        self._file = open(self.filepath, self.mode)

        FileContextManager.open_count += 1  # the class-level open_count
        
        self.logger.info(f"Opening file: {self.filepath} (Total count: {FileContextManager.open_count})")
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

import unittest
import os

# Assuming the FileContextManager class is already defined

class TestFileContextManager(unittest.TestCase):
    
    def setUp(self):
        """Set up test environment: create files and reset counter."""
        self.test_file = "test_file.txt"
        self.test_content = "Hello, test!"
        # Reset the class-level counter before each test
        FileContextManager.open_count = 0
        
        if os.path.exists(self.test_file):
            os.remove(self.test_file)  # Clean up before running a test
        
    def tearDown(self):
        """Clean up test environment after test is complete."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        
    def test_context_manager_file_exists_read_mode(self):
        """Test reading an existing file."""
  
        with open(self.test_file, "w") as f:
            f.write(self.test_content)
        
        with FileContextManager(self.test_file, "r") as file:
            content = file.read()
            self.assertEqual(content, self.test_content)
        
        # Ensure the file was closed
        self.assertEqual(FileContextManager.open_count, 1)
    
    def test_context_manager_file_does_not_exist_read_mode(self):
        """Test trying to read a non-existent file."""
        with self.assertRaises(FileNotFoundError):
            with FileContextManager(self.test_file, "r") as file:
                file.read()
        
        # The counter shouldn't change since an exception was raised
        self.assertEqual(FileContextManager.open_count, 0)

    def test_context_manager_file_exists_write_mode(self):
        """Test writing to an existing file."""
        with FileContextManager(self.test_file, "w") as file:
            file.write(self.test_content)
        
        # Check if file content is written
        with open(self.test_file, "r") as file:
            content = file.read()
            self.assertEqual(content, self.test_content)
        
        self.assertEqual(FileContextManager.open_count, 1)

    def test_context_manager_file_does_not_exist_write_mode(self):
        """Test creating a file in write mode if it does not exist."""
        # Ensure the file does not exist
        self.assertFalse(os.path.exists(self.test_file))
        
        with FileContextManager(self.test_file, "w") as file:
            file.write(self.test_content)
        
        # Check if the file was created and content was written
        self.assertTrue(os.path.exists(self.test_file))
        with open(self.test_file, "r") as file:
            content = file.read()
            self.assertEqual(content, self.test_content)
        
        self.assertEqual(FileContextManager.open_count, 1)

    def test_context_manager_counter_increment(self):
        """Test that the open count is correctly incremented."""
        with FileContextManager(self.test_file, "w") as file:
            file.write("First write")
        self.assertEqual(FileContextManager.open_count, 1)
        
        with FileContextManager(self.test_file, "r") as file:
            file.read()
        self.assertEqual(FileContextManager.open_count, 2)
        

    def test_context_manager_log_file_open_close(self):
        """Test if logging works as expected during file open/close."""
        with FileContextManager(self.test_file, "w") as file:
            file.write("Logging test")
        
        # Check if the log contains the correct messages
        with open(self.test_file, "r") as file:
            content = file.read()
            self.assertEqual(content, "Logging test")
        
        # Ensure the file was closed
        self.assertEqual(FileContextManager.open_count, 1)

if __name__ == "__main__":
    unittest.main()
