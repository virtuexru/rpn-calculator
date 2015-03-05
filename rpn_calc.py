"""
Author: Leonid Shalimov
What It Be: Reverse Polish Notation Calculator
"""
from operator import add, sub, mul, truediv
import string

_operators = {'+': add, '-': sub, '*': mul, '/': truediv}
_op_characters = ''.join(_operators.keys())

"""
The Handy Reverse Polish Notation Calculator
"""
def handy_rpn_calc(user_input = True):
  try:
    stack = []

    if user_input == True:
      print "Please input your calculation:"
      user_input = raw_input()

    # runs of consecutive whitespace are regarded as a single separator
    for token in string.split(user_input):
      if token in _operators:
        y, x = stack.pop(), stack.pop()
        z = _operators[token](x,y)
      elif token not in _op_characters:
        # raises ValueError on getting anything but a number
        z = float(token)
      stack.append(z)

    # ensures there are enough operators
    assert len(stack) <= 1

    # all glory to hypnotoad
    if len(stack) == 1:
      return stack.pop()
  except:
    raise

"""
Unit Tests
"""
import unittest

class TestHandyRpn(unittest.TestCase):
  def test_add(self):
    self.assertEqual(12, handy_rpn_calc('8      4    +'))
    self.assertEqual(11, handy_rpn_calc('3 8 +'))
    self.assertEqual(10, handy_rpn_calc('-4 14 +'))

  def test_subtract(self):
    self.assertEqual(-6, handy_rpn_calc('8 14   - '))
    self.assertEqual(4, handy_rpn_calc('9    5 -'))

  def test_random(self):
    self.assertEqual(-0.5, handy_rpn_calc('2 4 / 5 6 - *'))
    self.assertEqual(33, handy_rpn_calc('3 5 6 + *'))
    self.assertEqual(14, handy_rpn_calc('5 1 2 + 4 * 3 - +'))
    self.assertEqual(2, handy_rpn_calc('4 2 5 * + 1 3 2 * + /'))

  def test_raising(self):
    with self.assertRaises(ValueError):
      handy_rpn_calc('1 9 2 + 4 * D - /')

    with self.assertRaises(AssertionError):
      handy_rpn_calc('3 2 5 -')

    with self.assertRaises(IndexError):
      handy_rpn_calc('16 *')
    

if __name__ == '__main__':
  
  print handy_rpn_calc()
  print unittest.main()