import unittest

from tests.example_class import ExampleClass


class TestExampleClass(unittest.TestCase):

  def test_private_method1(self):
    example_class = ExampleClass()
    ok = example_class._ExampleClass__my_private_method()

    self.assertEqual(ok, 'OK')

  def test_private_method2(self):
    example_class = ExampleClass()
    ok = example_class.__my_private_method()

    self.assertEqual(ok, 'OK')

  def test_public_method(self):
    example_class = ExampleClass()
    ok = example_class.public_method()

    self.assertEqual(ok, 'OK')

if __name__ == '__main__':
  unittest.main(argv=['first-arg-is-ignored'], exit=False)
