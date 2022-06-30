class Employee(object):
	def __init__(self, first_name, last_name, annual_sal):
		self.first_name = first_name
		self.last_name = last_name
		self.annual_sal = annual_sal
	def give_raise(self, additional_raise = 0):
		if additional_raise == 0:
			self.annual_sal += 5000 
		else:
			self.annual_sal += additional_raise

import unittest

class TestEmployee(unittest.TestCase):
	def setUp(self):
		self.will_kerby = Employee("william", "kerby", 65000)
	def test_give_raise(self):
		give_raise_response = self.will_kerby.give_raise()
		self.assertEqual(will_kerby.annual_sal, give_raise_response)
	def test_give_custom_raise(self):
		give_custom_raise_response = self.will_kerby.give_raise(3000)
		self.assertEqual(will_kerby.annual_sal,give_custom_raise_response + 5000)

unittest.main()