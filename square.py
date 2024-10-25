import unittest

'''
a (float): side of square
return value (float): square area
'''
def square_area(a: float) -> float:
  if a < 0:
    raise ValueError("Invalid side of square")
  return round(a * a, 10)

'''
a (float): side of square
return value (float): perimeter of square
'''
def square_perimeter(a: float) -> float:
  if a < 0:
    raise ValueError("Invalid side of square") 
  return round(4 * a, 10)

class SquareTestCase(unittest.TestCase):
  def test_one_area(self):
    res = square_area(1)
    self.assertEqual(res, 1)

  def test_integer_area(self):
    res = square_area(123)
    self.assertEqual(res, 15129)
  
  def test_float_area(self):
    res = square_area(15.976)
    self.assertEqual(res, 255.232576)

  def test_negative_value_excaption_area(self):
    self.assertRaises(ValueError, square_area, -456)

  def test_one_perimetr(self):
    res = square_perimeter(1)
    self.assertEqual(res, 4)

  def test_integer_perimeter(self):
    res = square_perimeter(6552)
    self.assertEqual(res, 26208)
  
  def test_float_perimeter(self):
    res = square_perimeter(1135.4976)
    self.assertEqual(res, 4541.9904)

  def test_negative_value_excaption_perimeter(self):
    self.assertRaises(ValueError, square_perimeter, -123)