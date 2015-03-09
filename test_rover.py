import rover
import unittest

class TestSequenceFunctions(unittest.TestCase):

    def init(self):
        global plat_size 
        plat_size = [5, 5]
        global x_coordinate 
        x_coordinate = 1
        global y_coordinate 
        y_coordinate = 2
        global direction 
        direction = 'N'
        global instructions 
        instructions = 'LMLMLMLMM' 
        
        rover.follow_instructions()

    def test_x_coordinate(self):
        self.assertEqual(rover.x_coordinate, 1)
    def test_y_coordinate(self):
        self.assertEqual(rover.y_coordinate, 3)
    def test_direction(self):
        self.assertEqual(rover.direction, 'N')

        
if __name__ == '__main__':
    unittest.main()