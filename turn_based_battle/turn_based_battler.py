import pygame
import random
import time
import math
import pyganim
import ai
import defs
from decimal import *
from pygame.locals import *

clock = pygame.time.Clock()

pygame.mixer.pre_init(22050, -16, 3, 8)
pygame.mixer.init()

mouseCoordDebug = False
musicPlay = True

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0,0,255)
GREY = (100,100,100)

done = False
running = True

pygame.init()
 
# Set the width and height of the screen [width, height]
size = (1250, 700)
gScreen = pygame.display.set_mode(size)
font = pygame.font.SysFont('Calibri', 15, True, False)
text = font.render("hi",True,BLACK)
 
pygame.display.set_caption("TBB: To Be Renamed")
#pygame.mixer.music.play(-1, 0.0)
pygame.mouse.set_visible(False)

mouse_down = False
disptext = font.render("Place holder",True,BLACK)

def bubble_sort(items):
	""" Implementation of bubble sort """
	for i in range(len(items)):
		for j in range(len(items)-1-i):
			if items[j] > items[j+1]:
				items[j], items[j+1] = items[j+1], items[j] 
	return items

recte = []
test = pyganim.getImagesFromSpriteSheet("Assets/ui/animationtest.png",rows = 5,cols=5, rects = recte)

frames = list(zip(test, [200] * 25))
testAnim = pyganim.PygAnimation(frames)
testAnim.play()

testNumber = defs.normNums.image_at([0,0,12,25])

testAnim = defs.SpreetSheet("Assets/animations/alpha.png", 1, 16)

turn = 0		
aitest = False

while not done:

	for event in pygame.event.get(): 
		if event.type == pygame.QUIT: 
			done = True 
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_down = True
				
		elif event.type == pygame.MOUSEBUTTONUP:
			mouse_down = False
	mouse_pos = pygame.mouse.get_pos()
	defs.gScreen.fill(WHITE)
	pygame.draw.rect(gScreen, RED, [10,50,16,16])
	defs.gScreen.blit(font.render("Multiplayer",True,BLACK), [10,65])
	pygame.draw.rect(gScreen, GREEN, [60,50,16,16])
	defs.gScreen.blit(font.render("Story",True,BLACK), [60,35])
	pygame.draw.rect(gScreen, BLUE, [110,50,16,16])
	defs.gScreen.blit(font.render("Ai testing",True,BLACK), [110,35])
	
	if defs.hitDetect(mouse_pos, mouse_pos, [10,50], [26, 66]):
		if mouse_down:
			mult = True
			defs.CharSelect(aitest, mult)
			mouse_down = False
	if defs.hitDetect(mouse_pos, mouse_pos, [60,50], [60 + 16, 66]):
		if mouse_down:
			mult = False
			defs.theWorld.run(mult)
			mouse_down = False
			
	if defs.hitDetect(mouse_pos, mouse_pos, [110,50], [110 +16, 66]):
		if mouse_down:
			mult = True
			aitest = True
			defs.CharSelect(aitest, mult)
			mouse_down = False
	
	if mouse_down:
		defs.gScreen.blit(defs.mouse_pointer2,mouse_pos)
	else:
		defs.gScreen.blit(defs.mouse_pointer,mouse_pos)
		
	defs.gScreen.blit(testNumber, [100, 100])
	defs.cootheme.play()
	pygame.display.flip()
	clock.tick(60)