import rover
import unittest
r = rover.rover()

class TestSequenceFunctions(unittest.TestCase):

    def init(self):
        global r
        r.plat_size = [5, 5] 
        r.x_coordinate = 1
        r.y_coordinate = 2
        r.direction = 'N' 
        r.instructions = 'LMLMLMLMM' 
        

    def test_x_coordinate(self):
        global r
        r.follow_instructions()
        r.print_output()
        self.assertEqual(r.x_coordinate, 1)
    def test_y_coordinate(self):
        global r
        r.follow_instructions()
        r.print_output()
        self.assertEqual(r.y_coordinate, 3)
    def test_direction(self):
        global r
        r.follow_instructions()
        r.print_output()
        self.assertEqual(r.direction, 'N')

        
if __name__ == '__main__':
    unittest.main()