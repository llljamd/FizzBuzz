import unittest
import fizz_code

class test(unittest.TestCase):
	def test1(self):
		self.assertEqual(fizz_code.fizz(5), ['1', '2', 'Fizz', '4', 'Buzz'])

if __name__ == '__main__':
	unittest.main()
