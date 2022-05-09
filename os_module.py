# Python program to change the
# current working directory


'''import os

# Function to Get the current
# working directory
def current_path():
	print("Current working directory before")
	print(os.getcwd())
	print()


# Driver's code
# Printing CWD before
current_path()

# Changing the CWD
os.chdir('../')

# Printing CWD after
current_path()
'''

# Python program to explain os.makedirs() method

# importing os module
import os

# Leaf directory
directory = "Nikhil"

# Parent Directories
parent_dir = "D:/Pycharm projects/GeeksForGeeks/Authors"

# Path
path = os.path.join(parent_dir, directory)

# Create the directory
# 'Nikhil'
os.makedirs(path)
print("Directory '% s' created" % directory)

# Directory 'GeeksForGeeks' and 'Authors' will
# be created too
# if it does not exists


# Leaf directory
directory = "c"

# Parent Directories
parent_dir = "D:/Pycharm projects/GeeksforGeeks/a/b"

# mode
mode = 0o666

path = os.path.join(parent_dir, directory)

# Create the directory 'c'

os.makedirs(path, mode)
print("Directory '% s' created" % directory)

# 'GeeksForGeeks', 'a', and 'b'
# will also be created if
# it does not exists

# If any of the intermediate level
# directory is missing
# os.makedirs() method will
# create them

# os.makedirs() method can be
# used to create a directory tree
