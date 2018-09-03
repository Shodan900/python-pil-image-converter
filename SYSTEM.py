import PIL
import math
from tkinter import *
import random
from PIL import Image

# Instantiate TK root.
root = Tk()

# Open image, get pixels, set width and height.
picture = input("Enter the file name of the image for processing:")
im = Image.open(picture)
px = im.load()
width, height = im.size
if width > 1024 or height > 1024:
	print("Image too big! limit to 1024x1024")
	exit()
pass

# How many times bigger is the canvas than the actual image?
imageCanvRatio = 2

# Set canvas Width and Height to twice image's width and height
canvas_width = math.floor(width * imageCanvRatio)
canvas_height = math.floor(height * imageCanvRatio)

# Make canvas and put it on the TK window.
w = Canvas(root, width=canvas_width, height=canvas_height, background="grey")
w.pack()


# Resolution of characters. Example: Every 
# 4x4 square of pixels will become one
# character if averageSpace = 4
# Think of it like a pixel resolution... except for characters.
averageSpace = 4

#Width of generated character-image in units of characters.
charWidth = math.floor(width / averageSpace)
#Height of generated character-image in units of characters.
charHeight = math.floor(height / averageSpace)

# Pixels currently being analyzed
pixelMemory = {}
# Initializes first square area 
# to be put into a table.
def initializeMemory(gridx, gridy):
	for y in range(gridy * averageSpace, gridy * averageSpace + averageSpace - 1):
		for x in range(gridx * averageSpace, gridx * averageSpace + averageSpace - 1):
			pixelMemory[y] = px[x, y]
		pass
	pass
pass

#Find the average color of an averageSpace by averageSpace grid of pixels
# Example: if averageSpace = 4, find the average color of a 4x4 grid of pixels.
def getAveragedColor(gx, gy):
	initializeMemory(gx, gy)
	rval = 0
	gval = 0
	bval = 0
	
	for i in pixelMemory:
		rval += pixelMemory[i][0]
		gval += pixelMemory[i][1]
		bval += pixelMemory[i][2]
	pass

	finalR = math.ceil(rval/math.pow(averageSpace, 2))
	finalG = math.ceil(gval/math.pow(averageSpace, 2))
	finalB = math.ceil(bval/math.pow(averageSpace, 2))
	return (finalR, finalG, finalB)
pass

randomChars = ("A", "O", "0", "P", "B", "V", "E", "R", "$", "Q", "Y", "D")

# Show all the characters with their colors on the canvas
def structureChars():
	for c in range(0, charHeight):
		for k in range(0, charWidth):
			#color rgb converted to 6 digit hex
			lol = '#%02x%02x%02x' % getAveragedColor(k, c)
			converted = lol[:7]
			char = randomChars[random.randint(0, len(randomChars) - 1)]
			#multiplied by two to fit the whole window area
			w.create_text(k * (averageSpace * imageCanvRatio), c * (averageSpace * imageCanvRatio), text=char, fill=converted)
		pass
	pass
pass
structureChars()

# Keep this at end
root.mainloop()