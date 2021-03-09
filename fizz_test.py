import unittest
import fizz_code

class test(unittest.TestCase):
	def test1(self):
		self.assertEqual(fizz_code.fizz(5), ['1', '2', 'Fizz', '4', 'Buzz'])

	def test2(self):
		self.assertEqual(fizz_code.fizz(5), ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz'])

if __name__ == '__main__':
	unittest.main()
