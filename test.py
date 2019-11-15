import unittest
from Car import Car

class TestCarMethods(unittest.TestCase):

    def test_car_init(self):
        car = Car()
        self.assertEqual(car.average_speed(), 0)

if __name__ == '__main__':
    unittest.main()
