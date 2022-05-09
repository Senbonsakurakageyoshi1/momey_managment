# Python program to illustrate the concept
# of threading
# importing the threading module
from threading  import Thread
import os
import threading

def print_cube(num):
	"""
	function to print cube of given num
	"""
	print("Cube: {}".format(num * num * num))

def print_square(num):
	"""
	function to print square of given num
	"""
	print("Square: {}".format(num * num))

# Python program to illustrate the concept
# of threading


def task1():
	print("Task 1 assigned to thread: {}".format(threading.current_thread().name))
	print("ID of process running task 1: {}".format(os.getpid()))

def task2():
	print("Task 2 assigned to thread: {}".format(threading.current_thread().name))
	print("ID of process running task 2: {}".format(os.getpid()))


if __name__ == "__main__":
	# print ID of current process
	print("ID of process running main program: {}".format(os.getpid()))

	# print name of main thread
	print("Main thread name: {}".format(threading.current_thread().name))
	# creating thread
	t1 = Thread(target=print_square, args=(10,))
	t2 = Thread(target=print_cube, args=(10,))

	# starting thread 1
	t1.start()
	# starting thread 2
	t2.start()

	# wait until thread 1 is completely executed
	t1.join()
	# wait until thread 2 is completely executed
	t2.join()

	# both threads completely executed
	print("Done!")


