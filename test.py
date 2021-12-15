import unittest
from fractions import Fraction

from my_sum import sum

class TestSum(unittest.TestCase):
	# The three steps of a test case:
	# 1. Arrange
	# 2. Act
	# 3. Assert)
	def test_list_int(self):
		"""
		Test that it can sum a list of integers.
		"""
		data = [1,2,3]
		result = sum(data)
		self.assertEqual(result, 6, "Should be 6")

	def test_list_fraction(self):
		"""
		Test that it can sum a list of Fractions.
		"""
		data = [Fraction(1,4), Fraction(1,4), Fraction(2, 5)]
		result = sum(data)
		self.assertEqual(result, 1, "Should be 1")
	
	def test_bad_type(self):
		"""
		Tests that it fails when bad types are provided.
		"""
		data = "banana"
		with self.assertRaises(TypeError):
			result = sum(data)

if __name__ == "__main__":
	unittest.main()
