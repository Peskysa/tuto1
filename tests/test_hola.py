import unittest
from examples.hola import saludo
class ExampleTest(unittest.TestCase):
    def test_name(self):self.assertEqual(saludo(' Ana '),'Hola, Ana. Tu entorno Python funciona.')
    def test_empty(self):self.assertIn('Marco',saludo(' '))
if __name__=='__main__':unittest.main()
