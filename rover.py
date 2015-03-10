""" 
This is a simple brute-force implementation of Mars Rovers Problem.

PROBLEM: MARS ROVERS
 
A squad of robotic rovers are to be landed by NASA on a plateau on Mars. This plateau, which is curiously rectangular, must be navigated by the rovers so that their on-board cameras can get a complete view of the surrounding terrain to send back to Earth.
A rover's position and location is represented by a combination of x and y co-ordinates and a letter representing one of the four cardinal compass points. The plateau is divided up into a grid to simplify navigation. An example position might be 0, 0, N, which means the rover is in the bottom left corner and facing North. 
In order to control a rover, NASA sends a simple string of letters. The possible letters are 'L', 'R' and 'M'. 'L' and 'R' makes the rover spin 90 degrees left or right respectively, without moving from its current spot. 'M' means move forward one grid point, and maintain the same heading. 
Assume that the square directly North from (x, y) is (x, y+1).
 
INPUT:
The first line of input is the upper-right coordinates of the plateau, the lower-left coordinates are assumed to be 0, 0. 
The rest of the input is information pertaining to the rovers that have been deployed. Each rover has two lines of input. The first line gives the rover's position, and the second line is a series of instructions telling the rover how to explore the plateau. 
The position is made up of two integers and a letter separated by spaces, corresponding to the x and y co-ordinates and the rover's orientation. 
Each rover will be finished sequentially, which means that the second rover won't start to move until the first one has finished moving.
  
OUTPUT:
The output for each rover should be its final co-ordinates and heading.
 
INPUT AND OUTPUT

Test Input:
5 5
1 2 N
LMLMLMLMM
3 3 E
MMRMMRMRRM
 
Expected Output:
1 3 N
5 1 E

"""
class rover:
	def __init__(self):
		"""All the variables are initialised here."""
		self.x_coordinate = 0 
		self.y_coordinate = 0
		self.direction = 'N'
		self.left = 'L'
		self.right = 'R'
		self.move = 'M'
		self.north = 'N'
		self.south = 'S'
		self.east = 'E'
		self.west = 'W'
		self.instructions = ''
		self.plateau_size = []


	
	def set_data(self, plateau_size, x_coordinate, y_coordinate, direction, instructions):
		"""This function gets the input from main and sets all the variables of class."""
		self.plateau_size = plateau_size 
		self.x_coordinate, self.y_coordinate, self.direction = x_coordinate, y_coordinate, direction
		self.instructions = instructions



	def follow_instructions(self):
		"""This function iterates over each of the instruction and calls the respective command function."""
		for steps in self.instructions:
			if steps is self.left:
				self.turn_left()
			elif steps is self.right:
				self.turn_right()
			elif steps is self.move:
				self.move_forward()
			else:
				print("Wrong Instruction.")

	
	def move_forward(self):
		"""Moves the rover based on the present direction the the rover.
		   Assuming that the rover won't move after the plateau edge is reached."""
		if self.direction is self.north and self.y_coordinate < int(self.plateau_size[1]):
			self.y_coordinate = self.y_coordinate + 1
		elif self.direction is self.east and self.x_coordinate < int(self.plateau_size[0]):
			self.x_coordinate = self.x_coordinate + 1
		elif self.direction is self.south and self.y_coordinate > 0:
			self.y_coordinate = self.y_coordinate - 1
		elif self.direction is self.west and self.x_coordinate > 0:
			self.x_coordinate = self.x_coordinate - 1 

	
	def turn_left(self):
		"""Turns the rover left."""
		if self.direction is self.north:
			self.direction = self.west
		elif self.direction is self.east:
			self.direction = self.north
		elif self.direction is self.south:
			self.direction = self.east
		elif self.direction is self.west:
			self.direction = self.south 

	
	def turn_right(self):
		"""Turns the rover right."""
		if self.direction is self.north:
			self.direction = self.east
		elif self.direction is self.east:
			self.direction = self.south
		elif self.direction is self.south:
			self.direction = self.west
		elif self.direction is self.west:
			self.direction = self.north 

	
	def get_result(self):
		"""Returns the final result."""
		return self.x_coordinate, self.y_coordinate, self.direction



def main():
	r = rover()
	plateau_size = input().split()
	x_coordinate, y_coordinate, direction = input().split()
	instructions = input()
	r.set_data(plateau_size, int(x_coordinate), int(y_coordinate), direction.upper(), instructions.upper())
	r.follow_instructions()
	result = r.get_result()
	print(result[0], result[1], result[2])

if __name__ == '__main__': 
	main()
