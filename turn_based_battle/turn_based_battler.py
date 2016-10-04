

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
pygame.mixer.init()
#music = pygame.mixer.music.load("reformat.ogg")

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0,0,255)
GREY = (100,100,100)




health = 278
player_attack = 10
player_turn = True
gameover = False

player_x = 50
player_y = 150
player_x_vel = 0
player_y_vel = 0
animate = True
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
gScreen = pygame.display.set_mode(size)

font = pygame.font.SysFont('Calibri', 15, True, False)
text = font.render("hi",True,BLACK)
 
pygame.display.set_caption("My Game")

#pygame.mixer.music.play(-1, 0.0)
pygame.mouse.set_visible(False)

#Images:
mouse_pointer = pygame.image.load('Assets/mouse.png')
mouse_pointer2 = pygame.image.load('Assets/mouse2.png')
health_border = pygame.image.load('Assets/health_border.png')

testEnemy = ["James", "null", 50, 1, 1, 1, 1]

enemy = testEnemy
mouse_down = False
disptext = font.render("Place holder",True,BLACK)
menuui = pygame.image.load("assets/ui/menu.png")
lockedchar = pygame.image.load("assets/battlers/locked.png")
lockedskill = pygame.image.load("assets/moveboxes/locked.png")
selector1 = pygame.image.load("assets/ui/selector1.png")
selector2 = pygame.image.load("assets/ui/selector2.png")
selector3 = pygame.image.load("assets/ui/selector3.png")





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

class SpreetSheet(object):
	def __init__(self, img, row, colm):
		self.img = img
		self.row = row
		self.colm = colm
		self.animation = pyganim.PygAnimation(list(zip(pyganim.getImagesFromSpriteSheet(self.img, rows = self.row, cols = self.colm, rects = []),[200] * self.row * self.colm)))
		self.animation.play()
	def image_at(self, rectangle):
		rect = pygame.Rect(rectangle)
		image = pygame.Surface(rect.size).convert()
		image.blit(self.sheet, (0, 0), rect)
		return image

		

turn = 0







	
unlockedchars = [defs.Koishi.buildNew(), defs.Lapis.buildNew(), defs.Flan.buildNew(), defs.Okuu.buildNew(), defs.Nue.buildNew(), defs.Scarlet.buildNew(), defs.Mage.buildNew(), defs.Mouther.buildNew(), defs.Nic.buildNew(), defs.Siv.buildNew(), defs.Coo33.buildNew(), defs.CoosomeJoe.buildNew(), defs.Epic.buildNew(), defs.Alpha.buildNew(), defs.Durric.buildNew(), defs.Creep.buildNew(), defs.Catsome.buildNew(), defs.KnowingEye.buildNew(), defs.Protagonist.buildNew(), defs.Worshipper.buildNew(), defs.miniCreep.buildNew()]			

#as off yet, not used

class Arena(object):
	def __init__(self, name, effect, img):
		self.name = name
		self.effect = effect
		self.img = img
		
class Battle(object):
	def __init__(self, battlers1, battlers2, arena, dialog, mult):
		self.battlers1 = battlers1
		self.battlers2 = battlers2
		self.arena = arena
		self.dialog = dialog
		self.mult = mult
	def battle(self):
		
		thebattler = 0
		powergiven = False
		pickenm = False
		increment = 0
		aiSet = False
		mincrement = 0
		thesebattlers = []
		battling = True
		ready = False
		mouse_down = False
		defs.printing = False
		limit = 6
		if self.mult == False:
			limit = 3
		
		thesebattlers += self.battlers1 + self.battlers2
		for i in self.battlers1:
			print i.name
		for i in self.battlers2:
			print i.name

		x = 0
		y = 0
		for i in thesebattlers:
			if y > 2:
				y = 0
				x += 1
			i.basex = x * 550 + 50
			i.basey = y * 100 + 50
			y += 1
		
		
		while battling:

			gScreen.fill(WHITE)
			try:
				thisbattler = thesebattlers[thebattler]
			except:
				pass
				
			for event in pygame.event.get(): 
				if event.type == pygame.QUIT: 
					done = True 
					battling = False
				elif event.type == pygame.MOUSEBUTTONDOWN:
					mouse_down = True
				
				elif event.type == pygame.MOUSEBUTTONUP:
					mouse_down = False
					
			# --- Game logic should go here
			mouse_pos = pygame.mouse.get_pos()
		
			#health-=0.01
			if not thisbattler.updated:
			
				for i in thisbattler.effects:
					for k in thesebattlers:
						if k.ability == "watch them burn" and i == defs.burn:
						
							i.canend = False
							i.damage *= 2
					i.update(thisbattler)
				if thisbattler.ability == "Unidentifiable":
					thisbattler.marks = 0
				if thisbattler.ability == "Radiation":
					for l in thesebattlers:
						l.hp -= 25
					defs.printb(thisbattler.name + "'s radiation hurt everyone!")
					

				if thisbattler.ability == "Regen":
					thisbattler.hp += 25
					defs.printb(thisbattler.name + " is healing themself!")
				
					
				thisbattler.power += 1
				thisbattler.x = thisbattler.basex
				thisbattler.y = thisbattler.basey
				thisbattler.updated = True
				
			if thisbattler.hp > 0:
				for i in thisbattler.skills:

					if x > 1:
						x = 0
						y += 1

					if hitDetect(mouse_pos, mouse_pos,[330 + x*175, y*30 + 370], [330 + x*175 + 165, y*30 + 370 + 25]):
						if mouse_down:
							mouse_down = False
							if True:
								selected = False
								if x == 0 and y ==0:
									if thisbattler.skills[0].cost <= thisbattler.power:
										thisbattler.goskill = thisbattler.skills[0]
										selected = True
									
								if x == 1 and y == 0:
									if thisbattler.skills[1].cost <= thisbattler.power:
										thisbattler.goskill = thisbattler.skills[1]
										selected = True
										
								if x == 0 and y == 1:
									if thisbattler.skills[2].cost <= thisbattler.power:
										thisbattler.goskill = thisbattler.skills[2]
										selected = True
								if x == 1 and y == 1:
									if thisbattler.skills[3].cost <= thisbattler.power:
										thisbattler.goskill = thisbattler.skills[3]
										selected = True
								if x == 0 and y == 2:
									if thisbattler.skills[4].cost <= thisbattler.power:
										thisbattler.goskill = thisbattler.skills[4]
										selected = True
								if x == 1 and y == 2:
									if thisbattler.skills[5].cost <= thisbattler.power:
										thisbattler.goskill = thisbattler.skills[5]
										selected = True
								if x == 0 and y == 3:
									if thisbattler.skills[6].cost <= thisbattler.power:
										thisbattler.goskill = thisbattler.skills[6]
										selected = True
								if x == 1 and y == 3:
									if thisbattler.skills[7].cost <= thisbattler.power:
										thisbattler.goskill = thisbattler.skills[7]
										selected = True
										
								if selected:
									mouse_down = False
									print "skill picked:", thisbattler.goskill.name
									pickenm = True
					x += 1
				
				x = 0
				y = 0					
				if pickenm:	
					thisbattler.target = ["nul"]
					for i in thesebattlers:
						if y > 2:
							y = 0
							x += 1
							
						if hitDetect(mouse_pos, mouse_pos, (x *550 + 50, y * 100 + 50), (x * 550 + 50 + 50, y* 100 + 50 + 50)):
						
							if mouse_down:
								if x == 0 and y == 0:
									thisbattler.target[0] = thesebattlers[0]
									ready = True
								if x == 0 and y == 1:
									thisbattler.target[0] = thesebattlers[1]
									ready = True
								if x == 0 and y == 2:
									thisbattler.target[0] = thesebattlers[2]
									ready = True
								if x == 1 and y == 0:
									thisbattler.target[0] = thesebattlers[3]
									ready = True
								if x == 1 and y == 1:
									thisbattler.target[0] = thesebattlers[4]
									ready = True
								if x == 1 and y == 2:
									thisbattler.target[0] = thesebattlers[5]
									ready = True
							mouse_down = False
						
						if ready:
							print thisbattler.target[0].name
							ready = False
							
							if "hitAll" in  thisbattler.goskill.spec:
								thisbattler.target = []
								if thisbattler in self.battlers1:
									thisbattler.target = self.battlers2
								elif thisbattler in self.battlers2:
									thisbattler.target = self.battlers1
							
							thebattler += 1
							
							
							pickenm = False
						y += 1
										
			else:
				thisbattler.goskill = defs.nothing
				thebattler += 1
				pickenm = False
				ready = False
			
			agillist = []
			for i in thesebattlers:
				agillist.append(i)
			#print "thebattler:", thebattler
			if thebattler >= limit:
				if self.mult == False:
					if aiSet == False:
						for i in self.battlers2:
							i = ai.runAI(i, self.battlers1, self.battlers2)
							print i.name + " has "+str(i.power)+" power, saving for: "+ i.savingfor + ". Using: " + i.goskill.name + " on " + i.target[0].name
							aiSet = True
				#sorting
				for i in range(len(agillist)):
					for j in range(len(agillist)-1-i):
						
						if agillist[j].agil + agillist[j].goskill.spd  < agillist[j+1].agil + agillist[j+1].goskill.spd:
							agillist[j], agillist[j+1] = agillist[j+1], agillist[j] 
				
				if len(agillist[increment].target) > 1:
					if not defs.printing:
						agillist[increment].goskill.use(agillist[increment],agillist[increment].target[mincrement])
					
						if mincrement > 2:
							agillist[increment].power -= agillist[increment].goskill.cost
					
				else:
					if not defs.printing:
						agillist[increment].goskill.use(agillist[increment],agillist[increment].target[0])
						agillist[increment].power -= agillist[increment].goskill.cost
			
				if not defs.printing:
					if len(agillist[increment].target) > 1:
						mincrement+=1
						if mincrement > 2:
							mincrement = 0
							increment += 1
					else:
						increment += 1
					if increment > len(thesebattlers) - 1:
						increment = 0
						thebattler = 0
						aiSet = False
						for i in thesebattlers:
							i.updated = False


		# --- Drawing code should go here
		
		#player
		#animation:
			if not thebattler >= len(thesebattlers):
				if thisbattler in self.battlers1:
					thisbattler.x += 50
					if not thisbattler.x == thisbattler.basex + 50:
						thisbattler.x = thisbattler.basex + 50
				else: 
					thisbattler.x -= 50
					if not thisbattler.x == thisbattler.basex - 50:
						thisbattler.x = thisbattler.basex - 50
				
				
				thisbattler.y += thisbattler.ym
				if thisbattler.y >= thisbattler.basey + 5 or thisbattler.y <= thisbattler.basey - 5:
					thisbattler.ym *= -1
				
				gScreen.blit(thisbattler.image, [thisbattler.x, thisbattler.y])

			x = 0
			y = 0
			for i in thesebattlers:	
				if y > 2:
					y = 0
					x += 1
				
				if i.hp > 0:
					try:
						if not i == thesebattlers[thebattler]: #and not thebattler >= len(thesebattlers):
							gScreen.blit(i.image,[x * 550 + 50, y * 100 + 50])
					except:
						gScreen.blit(i.image,[x * 550 + 50, y * 100 + 50])
					
					pygame.draw.rect(gScreen, RED, [x* 550 + 50, y* 100 + 25,int(i.hp) / 20,5])
					 
					for f in range(len(i.effects)):
						
						gScreen.blit(i.effects[f].img, [x* 550 + 40 - f * 10, y * 100 + 25])
					
					
				y += 1
			#ANIMATIONS!
			
			pygame.draw.rect(gScreen, BLACK, [0,350,700,150])
			#pygame.draw.rect(gScreen, WHITE, [10,360,300,50])
			gScreen.blit(health_border, [10, 360])
			pygame.draw.rect(gScreen, GREY, [320, 360, 370, 130])
		
			x = 0
			y = 0

			if thisbattler.hp > 0:
				dispSkills(thisbattler)
			
			if mouse_down:
				gScreen.blit(mouse_pointer2,mouse_pos)
			else:
				gScreen.blit(mouse_pointer,mouse_pos)
			for i in thesebattlers:
				if i.hp <= 0:
					i.effects.append(defs.death)
					
				#reset character here
				
			for i in self.battlers1:
				if i.hp <= 0:
					self.battlers1.remove(i)
					
			for i in self.battlers2:
				if i.hp <= 0:
					self.battlers2.remove(i)
					
			if len(self.battlers1) == 0:
				defs.printb("Player 2 WINS!")
				print "Player 2 Wins"
				player1.battlers.append([NO, NO, NO])
				break
				
			elif len(self.battlers2) == 0:
				defs.printb("Player 1 WINS!")
				print "Player 1 Wins"
				player2.battlers.append([NO, NO, NO])
				break
			#print "THE TIMER:", defs.timer
			if defs.timer > 0:
				defs.timer -= 1
				gScreen.blit(defs.disptext, [10, 320])
				defs.printing = True
				pygame.draw.rect(gScreen, BLACK, [0,350,700,150])
			
			if defs.timer <= 0:
				defs.printing = False
				defs.timer = 0
			
			if thebattler == len(thesebattlers):
				pygame.draw.rect(gScreen, BLACK, [0,350,700,150])
		
			# --- Go ahead and update the screen with what we've drawn.
			pygame.display.flip()
	 
			# --- Limit to 60 frames per second
			clock.tick(60)


class Player(object):
	def __init__(self, name):
		self.acbattler = defs.NOT.buildNew()
		self.battlers = [defs.NOT.buildNew(), defs.NOT.buildNew(), defs.NOT.buildNew()]
		self.name = name
		self.wins = 0
		self.losses = 0
	
		self.ready = False
		self.resolved = True
		self.x1 = 0
		self.y1 = 0
		self.x2 = 0
		self.y2 = 0
		self.x3 = 0
		self.y3 = 0
		self.turn = True
		self.powergiven = False
		self.effectResolved = False
	
player1 = Player("1")
player2 = Player("2")

done = False

def dispSkills(player):
	global lockedskill
	x = 0
	y = 0

	for i in player.skills:
		
		if x > 1:
			x = 0
			y += 1
		
		gScreen.blit(i.text, [330+ 6 + x*175, y*30 + 370 + 5])
		if i.cost <= player.power:
			gScreen.blit(i.type.img, [330 + x*175, y*30 + 370])
		
		else:
			gScreen.blit(lockedskill, [330 + x*175, y*30 + 370])
			
		x += 1	
		
	pygame.draw.rect(gScreen, GREEN, [21,371,player.hp / 278,28])
	pygame.draw.rect(gScreen, BLUE, [10, 430, player.power * 2, 28])
	gScreen.blit(font.render("HP: " + str(player.hp), True, (0,0,255)), [75, 376])
	gScreen.blit(font.render("Power: " + str(player.power), True, (255,255,255)), [75, 426])
	gScreen.blit(font.render(player.name + "'s turn", True, (255,255,255)), [75, 476])
	

def hitDetect(pt1, pt2, pt3, pt4):
	'''Determine if 2 rectangles overlap. Rect 1 is defined as pt1 & pt2. Rect 2 is defined as pt3 & pt4.
	Each point is a 2-tuple with the x & y: pt1 = (32, 55)'''

	# Test upper left point
	if pt4[0]>pt1[0]>pt3[0]and pt4[1]>pt1[1]>pt3[1]:
		return True

	# Test lower right point
	if pt4[0]>pt2[0]>pt3[0]and pt4[1]>pt2[1]>pt3[1]:
		return True

	# Test lower left point
	if pt4[0]>pt1[0]>pt3[0]and pt4[1]>pt2[1]>pt3[1]:
		return True

	# Test upper right point
	if pt4[0]>pt2[0]>pt3[0]and pt4[1]>pt1[1]>pt3[1]:
		return True
		
dispchar2 = defs.NO		
	
battling = False

thesebattlers = []
thisplayer = player1

while not done:
	for event in pygame.event.get(): 
		if event.type == pygame.QUIT: 
			done = True 
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_down = True
			
		elif event.type == pygame.MOUSEBUTTONUP:
			mouse_down = False
			
		elif event.type == pygame.KEYDOWN:
				if event.key == K_UP:
					thisplayer.y3 -= 1
					if thisplayer.y3 < 0:
						thisplayer.y3 = 15
				if event.key == K_DOWN:
					thisplayer.y3 += 1
					if thisplayer.y3 > 15:
						thisplayer.y3 = 0
				if event.key == K_LEFT:
					thisplayer.x3 -= 1
					if thisplayer.x3 < 0:
						thisplayer.x3 = 23
				if event.key == K_RIGHT:
					thisplayer.x3 += 1
					if thisplayer.x3 > 23:
						thisplayer.x3 = 0
				if event.key == K_w:
					thisplayer.y1 -= 1
					if thisplayer.y1 < 0:
						thisplayer.y1 = 15
				if event.key == K_s:
					thisplayer.y1 += 1
					if thisplayer.y1 > 15:
						thisplayer.y1 = 0
				if event.key == K_a:
					thisplayer.x1 -= 1
					if thisplayer.x1 < 0:
						thisplayer.x1 = 23
				if event.key == K_d:
					thisplayer.x1 += 1
					if thisplayer.x1 > 23:
						thisplayer.x1 = 0
				if event.key == K_i:
					thisplayer.y2 -= 1
					if thisplayer.y2 < 0:
						thisplayer.y2 = 15
				if event.key == K_k:
					thisplayer.y2 += 1
					if thisplayer.y2 > 15:
						thisplayer.y2 = 0
				if event.key == K_j:
					thisplayer.x2 -= 1
					if thisplayer.x2 < 0:
						thisplayer.x2 = 23
				if event.key == K_l:
					thisplayer.x2 += 1
					if thisplayer.x2 > 23:
						thisplayer.x2 = 0
			
	mouse_pos = pygame.mouse.get_pos()
	y = 0
	x = 0
	for i in range(384):
		
		if x > 23:
			x = 0
			y += 1
		
		for f in unlockedchars:
			if thisplayer.x1 == f.cords[0] and thisplayer.y1 == f.cords[1]:
				
				dispchar = f
				
				thisplayer.battlers[0] = f.reBuild()
				break
				
			else:
				dispchar = defs.NO
				thisplayer.battlers[0] = defs.NO

		x += 1
		
	y = 0
	x = 0
	for i in range(384):
		
		if x > 23:
			x = 0
			y += 1
		
		for f in unlockedchars:
			if thisplayer.x2 == f.cords[0] and thisplayer.y2 == f.cords[1]:
				
				dispchar2 = f
				
				thisplayer.battlers[1] = f.reBuild()
				break
	
			else:
				dispchar2 = defs.NO
				thisplayer.battlers[1] = defs.NO

		x += 1
		
	y = 0
	x = 0
	for i in range(384):
		
		if x > 23:
			x = 0
			y += 1
		for f in unlockedchars:
			if thisplayer.x3 == f.cords[0] and thisplayer.y3 == f.cords[1]:
				
				dispchar2 = f
				
				thisplayer.battlers[2] = f.reBuild()
				break
				
			else:
				dispchar2 = defs.NO
				thisplayer.battlers[2] = defs.NO

		x += 1

	if hitDetect(mouse_pos, mouse_pos, [529, 434], [698, 498]):
		if thisplayer == player2:
			if mouse_down:
				
				theBattle = Battle(player1.battlers, player2.battlers, "", "", False)
	
				theBattle.battle()
				
				
		if mouse_down:
			thisplayer = player2
			mouse_down = False
			time.sleep(1)
	
	
	gScreen.fill(WHITE)
	gScreen.blit(menuui, [0, 0])
	x = 0
	y = 0
	
	for i in range(384):
		loaded = False
		if x > 23:
			x = 0
			y += 1
		
		for f in unlockedchars:
			if f.cords[0] == x and f.cords[1] == y:
				gScreen.blit(f.img, [3 + 22*x,3 + 22*y])
				loaded = True
		
		if not loaded:
			gScreen.blit(lockedchar, [3 + 22*x,3 + 22*y])
			loaded = False
				
		x += 1
			
	gScreen.blit(selector1, [thisplayer.x1*22 + 1, thisplayer.y1*22 + 1])
	gScreen.blit(selector2, [thisplayer.x2*22 + 1, thisplayer.y2*22 + 1])
	gScreen.blit(selector3, [thisplayer.x3*22 + 1, thisplayer.y3*22 + 1])
	
	for i in range(len(thisplayer.battlers)):
	
		localbattler = thisplayer.battlers[i]
	
		gScreen.blit(dispchar2.image, [644, 370])
	
		gScreen.blit(localbattler.menuImg, [4, i * 47 + 359])
		gScreen.blit(font.render(localbattler.name, True, BLACK), [56, i * 47 + 359])
		
		atypes = ""
		for f in localbattler.types:
			atypes += f.name + " "
		gScreen.blit(font.render(atypes, True, BLACK), [56, i * 47 + 375])
		gScreen.blit(font.render("Str: " + str(localbattler.str) + "   Con: " + str(localbattler.con) + "   Int: " + str(localbattler.int) + "   Mdf: " + str(localbattler.mag) + "   Agil: " + str(localbattler.agil) + "   Crit: " + str(localbattler.crit), True, BLACK), [56, i * 47 + 391])
	
	if mouse_down:
		gScreen.blit(mouse_pointer2,mouse_pos)
	else:
		gScreen.blit(mouse_pointer,mouse_pos)
	
	testAnim.blit(gScreen, [0,0])

	pygame.display.flip()	
	clock.tick(60)
	
	
	
#--------------------------------------------------------------------------------------------------------------------------------------------------		
#--------------------------------------------------------------------------------------------------------------------------------------------------	
#--------------------------------------------------------------------------------------------------------------------------------------------------	
#--------------------------------------------------------------------------------------------------------------------------------------------------	
#--------------------------------------------------------------------------------------------------------------------------------------------------	
#--------------------------------------------------------------------------------------------------------------------------------------------------	
#--------------------------------------------------------------------------------------------------------------------------------------------------	
#--------------------------------------------------------------------------------------------------------------------------------------------------	
	

		
		
	