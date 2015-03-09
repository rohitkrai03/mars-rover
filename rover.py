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

# All the variables are defined globally here.
x_coordinate = 0 
y_coordinate = 0
direction = 'N'
left = 'L'
right = 'R'
move = 'M'
north = 'N'
south = 'S'
east = 'E'
west = 'W'
instructions = ''
plat_size = []


# This function gets the input from user and stores it into proper global variables after parsing.
def get_input():
	global x_coordinate
	global y_coordinate
	global direction
	global instructions
	global plat_size

	plat_size = input().split()
	x_coordinate, y_coordinate, direction = input().split()
	x_coordinate, y_coordinate = int(x_coordinate), int(y_coordinate)
	instructions = input()


# This function iterates over each of the instruction and calls the respective command function.
def follow_instructions():
	for steps in instructions:
		if steps is left:
			turn_left()
		elif steps is right:
			turn_right()
		elif steps is move:
			move_forward()
		else:
			print("Wrong Instruction.")

# Moves the rover based on the present direction the the rover.
def move_forward():
	global x_coordinate
	global y_coordinate
	global plat_size
	# Assuming that the rover won't move after the plateau edge is reached.
	if direction is north and y_coordinate < int(plat_size[1]):
		y_coordinate = y_coordinate + 1
	elif direction is east and x_coordinate < int(plat_size[0]):
		x_coordinate = x_coordinate + 1
	elif direction is south and y_coordinate > 0:
		y_coordinate = y_coordinate - 1
	elif direction is west and x_coordinate > 0:
		x_coordinate = x_coordinate - 1 

# Turns the rover left.
def turn_left():
	global direction

	if direction is north:
		direction = west
	elif direction is east:
		direction = north
	elif direction is south:
		direction = east
	elif direction is west:
		direction = south 

# Turns the rover right.
def turn_right():
	global direction

	if direction is north:
		direction = east
	elif direction is east:
		direction = south
	elif direction is south:
		direction = west
	elif direction is west:
		direction = north 

# Prints the final result.
def print_output():
	print(x_coordinate, y_coordinate, direction)



def main():
	get_input()
	follow_instructions()
	print_output()

if __name__ == '__main__': 
	main()