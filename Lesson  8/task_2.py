#The sys module.

#The “sys.path” list is initialized from the PYTHONPATH environment variable. 
# Is it possible to change it from within Python? If so, does it affect where Python looks for module files? 
# Run some interactive tests to find it out.

 
import sys
import os

# 1. Print the initial sys.path

print('Initializing sys.path:\n')
print(*sys.path, sep='\n')
print(50*'*', end='\n\n')

# 2. Add a new directory to sys.path

try:
    os.mkdir('test_directory')
except FileExistsError:
    print('Directory is already exists.')

new_dir = os.path.abspath('test_directory')  
sys.path.append(new_dir)

print('New sys.path after adding test_directory:\n\n')
print(*sys.path, sep='\n')
print(50*'*', end='\n\n')

# 3. Try importing a new module from the new added directory
my_file = open(new_dir + '/mymodule.py', 'w+')
my_file.write('print("mymodule imported successfully!")')
my_file.close()

try:
    import mymodule
except ImportError:
    print("\nmymodule not found!")

print(50*'*', end='\n\n')

# 4. Remove the newly added directory, closing mymodule and print sys.path again
sys.modules.pop('mymodule')
sys.path.remove(new_dir)

print("\nsys.path after removing the directory:")
print(*sys.path, sep='\n')
print(50*'*', end='\n')

# 5. Try importing again after removal
try:
    import mymodule
except ImportError:
    print("\nmymodule not found!")