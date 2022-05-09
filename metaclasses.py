'''class test : pass

test.x=45
test.foo = lambda self : print('hello')

print(test.x)'''


def test_method(self):
	print("This is Test class method!")

# creating a base class
class Base:
	def myfun(self):
		print("This is inherited method!")

# Creating Test class dynamically using
# type() method directly
Test = type('Test', (Base, ), dict(x="atul", my_method=test_method))

# Print type of Test
print("Type of Test class: ", type(Test))

# Creating instance of Test class
test_obj = Test()
print("Type of test_obj: ", type(test_obj))

# calling inherited method
test_obj.myfun()

# calling Test class method
test_obj.my_method()

# printing variable
print(test_obj.x)
