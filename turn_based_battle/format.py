import pygame
import string
import random

def getEnemy();
	enemyID = random.randint(1,10)
	with open("enemies/"+enemyID+".txt") as f:
		i = -1
		for line in f:
			line = string.strip(line)
			i = i + 1
			if i = 0:
				name = line
			elif i = 1:
				image = line
			elif i = 2:
				hp = line
			elif i = 3:
				atk = line
			elif i = 4:
				defe = line
			elif i = 5:
				spd = line
			elif i = 6:
				lvl = line
			
	return [name, image, hp, atk, defe, spd, lvl]
			
			