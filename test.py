import unittest
from Car import Car

class TestCar(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        self.car = Car()
        unittest.TestCase.__init__(self, *args, **kwargs)

    def test_turn_on(self):
        self.assertTrue(self.car.turn_on())


    def test_turn_of(self):
        self.assertFalse(self.car.turn_off())

    def test_move_without_turn_on(self):
        self.assertTrue(self.car.move(1000))

    def test_move(self):
        self.assertTrue(self.car.turn_on())
        self.assertTrue(self.car.move(1000))

if __name__ == '__main__':
    unittest.main()
