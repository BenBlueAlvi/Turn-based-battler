import defs
import random
import time
import pygame
import math
pygame.init()
BLACK = (0,0,0)
WHITE = (255, 255, 255)
font = pygame.font.SysFont('Calibri', 15, True, False)
text = font.render("hi",True,BLACK)
clock = pygame.time.Clock()
def PreDialogeRun(battle, battlers1, battlers2, thesebattlers):
	running = True
	print "Dialog go!"
	for i in range(100):
		print "dialog loop", i
		if battle.name == "Maice Fight":
			print "Maice Fight"
			if i == 0:
				textc = "Umm, Mouse?"
				speaker = 0
			elif i == 1:
				textc = "Yes?"
				speaker = 1
			elif i == 2:
				textc = "Have you any information on the cult of zarism?"
				speaker = 0
			elif i == 3:
				textc = "Do not speak that name here."
				speaker = 1
			elif i == 4:
				textc = "That cult must never be mentioned"
				speaker = 1
			elif i == 5:
				textc = "Anyway, I must be going now, I am running away."
				speaker = 1
			elif i == 6:
				textc = "From the police? I think not!"
				speaker = 0
			else:
				break
		
		elif battle.name == "Nou Fight":
			print "Nou fight"
			if i == 0:
				for i in battlers1:
					if i.name == "Alpha":
						textc = "Finaly, a person in this empty rift."
						speaker = i.battlerpos
						break
					elif i.name == "Durric":
						textc = "And who would this be?"
						speaker = i.battlerpos
						break
					elif i.name == "CoosomeJoe":
						textc = "Oh, why hello there"
						speaker = i.battlerpos
					else:
						textc = "!"
						speaker = 0
						
					
			else:
				break
				
		else:
			print "Broken"
			if i == 0:
				textc = "UHHHHH SOMETHING BROKE"
				speaker = 1
				
		
		talking = 0
		textf = font.render(textc, True, BLACK)
		while talking <= 120 * len(textc) and running:
			for event in pygame.event.get(): 
				if event.type == pygame.QUIT: 
					running = False 
				if event.type == pygame.KEYDOWN:
					print "skip"
					talking = 120 * len(textc) +1
			
			defs.gScreen.fill(WHITE)
			defs.gScreen.blit(battle.arena.img, [0,0])
			pygame.draw.rect(defs.gScreen, BLACK, [0,defs.size[1] - 150,defs.size[0],150])
			talking += 1
			if thesebattlers[speaker] in battlers1:
				# Dialog bubble --> pygame.draw.rect(defs.gScreen, WHITE, [thesebattlers[speaker].basex + 55, thesebattlers[speaker].basey - 10, font.size(textc)[0], font.size(textc)[1]])
				defs.gScreen.blit(textf, [thesebattlers[speaker].basex + 55, thesebattlers[speaker].basey - 10])
				
			else:
				pygame.draw.rect(defs.gScreen, BLACK, [0,defs.size[1] - 150,defs.size[0],150])
				defs.gScreen.blit(textf, [thesebattlers[speaker].basex - font.size(textc)[0], thesebattlers[speaker].basey - 10])
			
			for k in thesebattlers:
				defs.gScreen.blit(k.image,[k.basex, k.basey])	
			

			pygame.display.flip()
			clock.tick(60)
		if not running:
			break
#---------------------------------------------------------------			
def LossDialogeRun(battle, battlers1, battlers2, thesebattlers):
	running = True
	print "Dialog go!"
	for i in range(10):
		print "dialog loop", i
		if battle.name == "Maice Fight":
			print "Maice Fight"
			if i == 0:
				textc = "Umm, Mouse?"
				speaker = 0
			elif i == 1:
				textc = "Yes?"
				speaker = 1
			elif i == 2:
				textc = "Have you any information on the cult of zarism?"
				speaker = 0
			elif i == 3:
				textc = "Do not speak that name here."
				speaker = 1
			elif i == 4:
				textc = "That cult must never be mentioned"
				speaker = 1
			elif i == 5:
				textc = "Anyway, I must be going now, I am running away."
				speaker = 1
			elif i == 6:
				textc = "From the police? I think not!"
				speaker = 0
			else:
				break
		
		elif battle.name == "Nou Fight":
			print "Nou fight"
			if i == 0:
				for i in battlers1:
					if i.name == "Alpha":
						textc = "Finaly, a person in this empty rift."
						speaker = i.battlerpos
						break
					elif i.name == "Durric":
						textc = "And who would this be?"
						speaker = i.battlerpos
						break
					elif i.name == "CoosomeJoe":
						textc = "Oh, why hello there"
						speaker = i.battlerpos
					else:
						textc = "!"
						speaker = 0
						
					
			else:
				break
				
		else:
			print "Broken"
			if i == 0:
				textc = "UHHHHH SOMETHING BROKE"
				speaker = 1
		
		
		talking = 0
		textf = font.render(textc, True, BLACK)
		while talking <= 120 * len(textc) and running:
			for event in pygame.event.get(): 
				if event.type == pygame.QUIT: 
					running = False 
			print "Talking!"
			defs.gScreen.fill(WHITE)
			defs.gScreen.blit(battle.arena.img, [0,0])
			
			talking += 1
			if thesebattlers[speaker] in battlers1:
				
				defs.gScreen.blit(textf, [thesebattlers[speaker].basex + 55, thesebattlers[speaker].basey - 10])
				
				defs.gScreen.blit(textf, [thesebattlers[speaker].basex - font.size(textc)[0], thesebattlers[speaker].basey - 10])
			
			for k in thesebattlers:
				defs.gScreen.blit(k.image,[k.basex, k.basey])	
			
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					talking = 120 * len(textc) +1

			pygame.display.flip()
			clock.tick(60)
		if not running:
			break

#---------------------------------------------------------------
			
def WinDialogeRun(battle, battlers1, battlers2, thesebattlers):
	running = True
	print "Dialog go!"
	for i in range(10):
		print "dialog loop", i
		if battle.name == "Maice Fight":
			print "Maice Fight"
			if i == 0:
				textc = "Umm, Mouse?"
				speaker = 0
			elif i == 1:
				textc = "Yes?"
				speaker = 1
			elif i == 2:
				textc = "Have you any information on the cult of zarism?"
				speaker = 0
			elif i == 3:
				textc = "Do not speak that name here."
				speaker = 1
			elif i == 4:
				textc = "That cult must never be mentioned"
				speaker = 1
			elif i == 5:
				textc = "Anyway, I must be going now, I am running away."
				speaker = 1
			elif i == 6:
				textc = "From the police? I think not!"
				speaker = 0
			else:
				break
		
		elif battle.name == "Nou Fight":
			print "Nou fight"
			if i == 0:
				for i in battlers1:
					if i.name == "Alpha":
						textc = "Finaly, a person in this empty rift."
						speaker = i.battlerpos
						break
					elif i.name == "Durric":
						textc = "And who would this be?"
						speaker = i.battlerpos
						break
					elif i.name == "CoosomeJoe":
						textc = "Oh, why hello there"
						speaker = i.battlerpos
					else:
						textc = "!"
						speaker = 0
						
					
			else:
				break
				
		else:
			print "Broken"
			if i == 0:
				textc = "UHHHHH SOMETHING BROKE"
				speaker = 1
				
		
		
		
		talking = 0
		textf = font.render(textc, True, BLACK)
		while talking <= 120 * len(textc) and running:
			for event in pygame.event.get(): 
				if event.type == pygame.QUIT: 
					running = False 
			print "Talking!"
			defs.gScreen.fill(WHITE)
			defs.gScreen.blit(battle.arena.img, [0,0])
			pygame.draw.rect(defs.gScreen, BLACK, [0,defs.size[1] - 150,defs.size[0],150])
			talking += 1
			if thesebattlers[speaker] in battlers1:
				
				defs.gScreen.blit(textf, [thesebattlers[speaker].basex + 55, thesebattlers[speaker].basey - 10])
			else:
				
				defs.gScreen.blit(textf, [thesebattlers[speaker].basex - font.size(textc)[0], thesebattlers[speaker].basey - 10])
			
			for k in thesebattlers:
				defs.gScreen.blit(k.image,[k.basex, k.basey])	
			
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					talking = 120 * len(textc) +1

			pygame.display.flip()
			clock.tick(60)
		if not running:
			break
		
	

		
	
	