# Adrian Cheung 101152541
import pygame		#import pygame

instructions = input("Welcome to Adrian's green screen program. Would you like to receive instructions? [yes/no] " ).upper()#User inputs if they want instructions. upper allows to user to enter an answer with any combination of cases and will still accept
if instructions == "YES":	#if the user requests instructions, this print statement will be shown on screen
	print("You are required to submit two BMP files into the program. A background image, and a green screen image that you may wish to blend in with the background where the image will have a transparent ghost like hue. You will then be required to submit x y coordinates for the center of the image. Please note that the program will not accept your entry if any of the pixels on the green screen image are cut off. After entering in the coordinates, enjoy!")
user_background = input("Please enter the file name for the background image you will be using ")
user_ghost = input("Please enter the file name for the green screen image you will be using ")

#Get image portion of the code
pygame.display.init()						#initializes display for pygame
background_image = pygame.image.load(user_background)		#loads the background image
(w, h) = background_image.get_rect().size			#gets the dimensions of the background image
drawing_window = pygame.display.set_mode((w, h))		#sets the display window to the size of the background image
drawing_window.blit(background_image, (0,0))			#copies the image on the drawing window at coordinates 0,0
ghost_image = pygame.image.load(user_ghost)			#loads the green screen image
(gw, gh) = ghost_image.get_rect().size				#gets the dimensions for the green screen image
pygame.display.update()						#updates the display

#Getting coordinates image of the code
while True:							#sets a loop that allows user to re enter coords if invalid
	centerw = int(input("Please enter the x coordinates of the centre of the green screen image "))	#asks user to enter x coords
	centerh = int(input("Please enter the y coordinates of the centre of the green screen image "))	#ask user to enter y coords
	xcoord = centerw - (gw // 2)									#calculations to find origin or image point
	ycoord = centerh - (gh // 2) 
	if xcoord < 0 or xcoord > w - gw or ycoord < 0 or ycoord > h - gh:				#coords are invalid due to these conditions
		print('Coordinates invalid. Please make sure your coordinates are within the realm of the screen. Full BMP file must be within the screen')
	else:
		break;											#if coords are valid, break out of loop

green = (0, 255, 0)						#definition of green

#Averaging out the colors and implementing them part of the assignment
for x in range(gw):						#nested loops to check through every pixel
	for y in range(gh):
		backgroundcolor = background_image.get_at((x +xcoord, y + ycoord))			#finds the RGB value of the background pixels
		ghostcolor = ghost_image.get_at((x, y))							#finds the RGB value of the green screen pixels
		averagecolor = ((ghostcolor[0] + backgroundcolor[0]) // 2, (ghostcolor[1] + backgroundcolor[1]) // 2 , (ghostcolor[2] + backgroundcolor[2]) // 2)													#finds the average color between these 2 pixels
		if ghostcolor != green:									#if the green screen pixel is not green
			background_image.set_at((x + xcoord, y + ycoord), averagecolor) 	#set the color to the average color of the 2 images	
		else:										#else
			background_image.set_at((x + xcoord,y + ycoord), backgroundcolor)	#just leave the background pixel remain the same

drawing_window.blit(background_image, (0, 0))				#copies the new image onto the drawing window 					
pygame.display.update()							#updates the display
while True:								#while loop that closes the pygame window if user clicks x on tab
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
