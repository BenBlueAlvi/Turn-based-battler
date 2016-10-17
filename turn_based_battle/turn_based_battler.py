

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



musicPlay = True


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
 
pygame.display.set_caption("TBB: To Be Renamed")

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





	
unlockedchars = [defs.Koishi.buildNew(), defs.Lapis.buildNew(), defs.Flan.buildNew(), defs.Okuu.buildNew(), defs.Nue.buildNew(), defs.Scarlet.buildNew(), defs.Mage.buildNew(), defs.Mouther.buildNew(), defs.Nic.buildNew(), defs.Siv.buildNew(), defs.Coo33.buildNew(), defs.CoosomeJoe.buildNew(), defs.Epic.buildNew(), defs.Alpha.buildNew(), defs.Durric.buildNew(), defs.Creep.buildNew(), defs.Catsome.buildNew(), defs.KnowingEye.buildNew(), defs.Protagonist.buildNew(), defs.Worshipper.buildNew(), defs.miniCreep.buildNew()]			

#as off yet, not used

class Arena(object):
	def __init__(self, name, effect, img):
		self.name = name
		self.effect = effect
		self.img = img

		
		

class Battle(object):
	def __init__(self, battlers1, battlers2, arena, dialog, mult, music):
		self.battlers1 = battlers1
		self.battlers2 = battlers2
		self.music = music
		self.arena = arena
		self.dialog = dialog
		self.mult = mult
		if not self.mult:
			for i in self.battlers2:
				i.isAi = True
		for i in self.battlers1:
			if i.name == "???":
				i.isAi = True
		for i in self.battlers2:
			if i.name == "???":
				i.isAi = True
		
	def battle(self):
		
		thebattler = 0
		powergiven = False
		pickenm = False
		increment = 0
		mincrement = 0
		thesebattlers = []
		battling = True
		diatimer = 0
		talking = True
		ready = False
		mouse_down = False
		defs.printing = False
		textc = font.render(" ",True,BLACK)
		limit = 6
		if self.mult == False:
			limit = 6
		
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
		for i in thesebattlers:
			if i.name == "???":
				thesebattlers.remove(i)

		for i in self.dialog.prebattle:
			textc, text = [], []
			for l in range(len(i)):
				if l == 0:
					speaker = i[l]
					print speaker
				else:
					textc.append(font.render(i[l],True,BLACK))
					text.append(i[l])
					
					
			talking = 0
			while talking <= 120* len(textc):
				defs.gScreen.fill(WHITE)
				pygame.draw.rect(gScreen, BLACK, [0,350,700,150])
				talking += 1
				if thesebattlers[speaker] in self.battlers1:
					for l in range(len(textc)):
						defs.gScreen.blit(textc[l-1], [thesebattlers[speaker].basex, thesebattlers[speaker].basey - (30 + ((l-1) * font.size(text[l-1])[1]))])
				else:
					for l in range(len(textc)):
						defs.gScreen.blit(textc[l-1], [thesebattlers[speaker].basex - font.size(text[l-1])[0], thesebattlers[speaker].basey - (30 + ((l-1) * font.size(text[l-1])[1]))])
				
			
				for k in thesebattlers:	
					
					defs.gScreen.blit(k.image,[k.basex, k.basey])

				pygame.display.flip()
				clock.tick(60)
					
					
			
			
		
		
		
		
		while battling:
			self.music.play()
			for p in thesebattlers:
				#update effects and all that good stuff
				for i in p.effects:
					for k in thesebattlers:
						if k.ability == "watch them burn" and i == defs.burn:
						
							i.canend = False
							i.damage *= 2
					i.update(p)
				if p.ability == "Unidentifiable":
					p.marks = 0
				if p.ability == "Radiation":
					for l in thesebattlers:
						l.hp -= 25
					defs.printb(p.name + "'s radiation hurt everyone!")
					

				if p.ability == "Regen":
					p.hp += 25
					defs.printb(p.name + " is healing themself!")
				
					
				p.power += 1
				p.x = p.basex
				p.y = p.basey
				ready, selected = False, False
				
				thesedisplays = []
				for i in range(len(thesebattlers)-1):
					thesedisplays.append(random.randint(0, len(self.dialog.inbattle[i])-1))

				while not ready and not p.isAi:
					defs.gScreen.fill(WHITE)
					for event in pygame.event.get(): 
						if event.type == pygame.QUIT: 
							ready = True							
							battling = False
							break
						elif event.type == pygame.MOUSEBUTTONDOWN:
							mouse_down = True
						
						elif event.type == pygame.MOUSEBUTTONUP:
							mouse_down = False
							
					mouse_pos = pygame.mouse.get_pos()
					
					#displaying and picking skills
					if p.hp > 0:
						for i in p.skills:
						
							if x > 1:
								x = 0
								y += 1

							if hitDetect(mouse_pos, mouse_pos,[330 + x*175, y*30 + 370], [330 + x*175 + 165, y*30 + 370 + 25]):
								if mouse_down:
									mouse_down = False
									if True:
										selected = False
										if x == 0 and y ==0:
											if p.skills[0].cost <= p.power:
												p.goskill = p.skills[0]
												selected = True
											
										if x == 1 and y == 0:
											if p.skills[1].cost <= p.power:
												p.goskill = p.skills[1]
												selected = True
												
										if x == 0 and y == 1:
											if p.skills[2].cost <= p.power:
												p.goskill = p.skills[2]
												selected = True
										if x == 1 and y == 1:
											if p.skills[3].cost <= p.power:
												p.goskill = p.skills[3]
												selected = True
										if x == 0 and y == 2:
											if p.skills[4].cost <= p.power:
												p.goskill = p.skills[4]
												selected = True
										if x == 1 and y == 2:
											if p.skills[5].cost <= p.power:
												p.goskill = p.skills[5]
												selected = True
										if x == 0 and y == 3:
											if p.skills[6].cost <= p.power:
												p.goskill = p.skills[6]
												selected = True
										if x == 1 and y == 3:
											if p.skills[7].cost <= p.power:
												p.goskill = p.skills[7]
												selected = True
												
										if selected:
											mouse_down = False
											print "skill picked:", p.goskill.name
											pickenm = True
							x += 1
						
									
						if pickenm:	
							p.target = ["nul"]
							for i in thesebattlers:
								
									
								if hitDetect(mouse_pos, mouse_pos, (i.basex, i.basey), (i.basex + 50,i.basey + 50)):
								
									if mouse_down:
										p.target[0] = i
										ready = True
										
									mouse_down = False
								
								if ready:
									print p.target[0].name
									
									if "hitAll" in  p.goskill.spec:
										p.target = []
										if p in self.battlers1:
											p.target = self.battlers2
										elif p in self.battlers2:
											p.target = self.battlers1
									
									pickenm = False
								


						#----------------
						if p in self.battlers1:
							p.x += 50
							if not p.x == p.basex + 50:
								p.x = p.basex + 50
						else: 
							p.x -= 50
							if not p.x == p.basex - 50:
								p.x = p.basex - 50
						
						
						p.y += p.ym
						if p.y >= p.basey + 5 or p.y <= p.basey - 5:
							p.ym *= -1
						
						defs.gScreen.blit(p.image, [p.x, p.y])
					else:
						p.goskill = defs.nothing
						p.target = [p]
						ready = True

				
					for i in thesebattlers:	
						
						
						if i.hp > 0:
							
								
							
							if not i == p:
								defs.gScreen.blit(i.image,[i.basex,i.basey])
							
								
							
							pygame.draw.rect(gScreen, RED, [i.basex, i.basey - 10,int(i.hp) / 20,5])
							 
							for f in range(len(i.effects)):
								
								defs.gScreen.blit(i.effects[f].img, [i.basex - f * 10, i.basey])
							
							
						y += 1
					#ANIMATIONS!
					
					pygame.draw.rect(gScreen, BLACK, [0,350,700,150])
				
					defs.gScreen.blit(health_border, [10, 360])
					pygame.draw.rect(gScreen, GREY, [320, 360, 370, 130])
				
					x = 0
					y = 0

					if p.hp > 0:
						dispSkills(p)
					#------
					
					
					for i in range(len(thesebattlers)-1):
						texti = self.dialog.inbattle[i][thesedisplays[i]]
						displaythis = font.render(texti, True, BLACK)
						for l in range(len(texti)-1):
							print l
							
							defs.gScreen.blit(displaythis, [thesebattlers[i].basex, thesebattlers[i].basey - (30 + ((l) * font.size(l)[1]))])
					
					
					if mouse_down:
						defs.gScreen.blit(mouse_pointer2,mouse_pos)
					else:
						defs.gScreen.blit(mouse_pointer,mouse_pos)
					for i in thesebattlers:
						if i.hp <= 0:
							i.effects.append(defs.death)
							
						#reset character here
						
						
					#print "THE TIMER:", defs.timer
					
					
					
					
					if thebattler == len(thesebattlers):
						pygame.draw.rect(gScreen, BLACK, [0,350,700,150])


					pygame.display.flip()
			 
					# --- Limit to 60 frames per second
					clock.tick(60)
					
				if p.isAi:
					p = ai.runAI(p, self.battlers1, self.battlers2)
					print p.name + " has "+str(p.power)+" power, saving for: "+ p.savingfor + ". Using: " + p.goskill.name + " on " + p.target[0].name
			
			
			agillist = []
			for i in thesebattlers:
				agillist.append(i)
			for i in range(len(agillist)):
				for j in range(len(agillist)-1-i):
					
					if agillist[j].agil + agillist[j].goskill.spd  < agillist[j+1].agil + agillist[j+1].goskill.spd:
						agillist[j], agillist[j+1] = agillist[j+1], agillist[j] 
			
			for p in agillist:
				#print "thebattler:", thebattler
				
				if len(p.target) > 1:
					
					p.goskill.use(p,p.target[mincrement])
					
					if mincrement > 2:
						p.power -= p.goskill.cost
					
				else:
					
					p.goskill.use(p,p.target[0])
					p.power -= p.goskill.cost
			
				
				if len(p.target) > 1:
					mincrement+=1
					if mincrement > 2:
						mincrement = 0
					increment += 1
				else:
					increment += 1
				if increment > len(thesebattlers) - 1:
					increment = 0
				
				for i in thesebattlers:
					if i.hp <= 0:
						thesebattlers.remove(i)
						if i in self.battlers1:
							self.battlers1.remove(i)
						if i in self.battlers2:
							self.battlers2.remove(i)
						
			for i in thesebattlers:
				i.updated = False
			if len(self.battlers1) == 0:
				defs.printb("Player 2 WINS!")
				print "Player 2 Wins"
				for b in thesebattlers:
					b = b.reBuild()
				self.music.reset()
				self.music.stop()
				battling = False
				break
				
			elif len(self.battlers2) == 0:
				defs.printb("Player 1 WINS!")
				print "Player 1 Wins"
				for b in thesebattlers:
					b = b.reBuild()
				self.music.reset()
				self.music.stop()
				battling = False
				break

				

		# --- Drawing code should go here
		
		#player
		#animation:
			
			
			
			
			
			
				
				
		
			# --- Go ahead and update the screen with what we've drawn.
			pygame.display.flip()
	 
			# --- Limit to 60 frames per second
			clock.tick(60)
		player1.battlers = [defs.NOT.buildNew(), defs.NOT.buildNew(), defs.NOT.buildNew()]

#preb is list of lists, inb is dictionary, losb is list of lists, winb is list of lists
class Dialoge(object):
	def __init__(self, preb, inb, losb, winb):
		self.prebattle = preb
		self.inbattle = inb
		self.lossbattle = losb
		self.winbattle = winb

NoDial = Dialoge([[0, ""]],{0:[""], 1:[""], 2:[""], 3:[""], 4:[""], 5:[""]},[[0, ""]],[[0, ""]])

CatDial = Dialoge([[0, "Are you this 'Catosme' i've heard so much about?"], [1, "Yes, that is one title I reply to..."], [1, "Anyway, have you seen a little friend of mine running about?"], [0, "I was sent here by it to avenge it."], [1, "So it wants you to try to hit on me?"], [0, "Please no."], [1, "So we're going to skip the formalities", "and get right to the good parts, eh?"]], {0:[""], 1:["Come on, I know you can hit me harder than that!", "Looks hot over there, how about taking some of that off?", "ah, so THATS your weak spot!"]}, [[1, "Ah, that was nice being on top."], [0, "What is it with you and innuendos?"], [1, "I guess it's just one of the things in me."]], [[1, "Ah, I give! Safe word, Safe word!"], [1, "Please stop with the innuendos."]])
CatsomeFight = Battle([], [defs.NO, defs.Catsome.buildNew(), defs.NO], "", CatDial, False, defs.cattheme)
CooDial = Dialoge([[2, "Ah, Coosome! it's been a while!"], [3, "Indeed it has, Cat."], [0, "You know him?"], [2, "Of course! We are all over each other!"], [3, "What Cat means to say, is that we are one and the same."], [2, "We stick together! so Lets have a FOURSOME!"], [0, "But who else is joining me?"], [1, "I'll stand in for Catsome. Lets do this."]], {0:[""], 1:[""], 2:["Come on, I know you can hit me harder than that!", "Looks hot over there, how about taking some of that off?", "Hit 'em there! thats his weak spot!"]}, [[3, "You fought well.", "But not well enough."], [2, "Is that really all? I'm not satisfied yet."]], [[3, "Nice one, you fought well there."], [2, "Is it done already? I'm not quite satisfied yet..."]])
Coo33Fight = Battle([], [defs.Catsome.buildNew(), defs.NO, defs.CoosomeJoe.buildNew()], "", CooDial, False, defs.cootheme) 
C33Dial = Dialoge([[5, "Ah, Coosome! it's been a while!"], [4, "Indeed it has, Cat."], [1, "You know him?"], [5, "Of course! We are all over each other!"], [4, "What Cat means to say, is that we are one and the same."], [5, "We stick together! so Lets have a FOURSOME!"], [1, "But who else is joining me?"], [2, "I'll stand in for Catsome. Lets do this."]], {0:[""], 1:[""], 2:[""], 3:[""], 4:[""], 5:["Come on, I know you can hit me harder than that!", "Looks hot over there, how about taking some of that off?", "Hit 'em there! thats his weak spot!"]}, [[4, "You fought well.", "But not well enough."], [5, "Is that really all? I'm not satisfied yet."]], [[4, "Nice one, you fought well there."], [5, "Is it done already? I'm not quite satisfied yet..."]])
Coo33Fight = Battle([], [defs.CoosomeJoe.buildNew(), defs.Coo33.buildNew(), defs.Catsome.buildNew()], "", C33Dial, False, defs.cootheme)



			
class Stage(object):
	def __init__(self, name, playerbattlers, battles, cords):
		self.name = name
		self.battles = battles
		self.cords = cords
		self.completed = False
	def run(self):
		for i in self.battles:
			i.battlers1 = self.playerbattlers
		for i in self.battles:
			i.battle()
		
		

st1 = Stage("", "", [CatsomeFight,Coo33Fight], [317,48])
st2 = Stage("", "", [], [280, 221])
st3 = Stage("", "", [], [393,292])
st4 = Stage("", "", [], [540,313])
st5 = Stage("", "", [], [675,240])
st6 = Stage("", "", [], [720,360])
st7 = Stage("", "", [], [523,431])
st8 = Stage("", "", [], [359,516])
		

class World(object):
	def __init__(self, stages):
		self.stages = stages
		self.cords = [0,0]
		self.image = pygame.image.load("Assets/ui/maptest.png")
		self.vel = [0,0]
	
		
	def run(self, mult):
		mouse_down = False
		running = True
		while running:
			for event in pygame.event.get(): 
				if event.type == pygame.QUIT: 
					running = False
				elif event.type == pygame.MOUSEBUTTONDOWN:
					mouse_down = True
				
				elif event.type == pygame.MOUSEBUTTONUP:
					mouse_down = False
				if event.type == pygame.KEYDOWN:
		
					if event.key == K_w:
				
						self.vel[1] = 5
					
					if event.key == K_d:
				
						self.vel[0] = -5
					
					if event.key == K_s:
				
						self.vel[1] = -5
					
					if event.key == K_a:
				
						self.vel[0] = 5
					
				elif event.type == pygame.KEYUP:
			
					if event.key == pygame.K_d or event.key == pygame.K_a:
				
						self.vel[0] =0
					if event.key == pygame.K_w or event.key == pygame.K_s:
				
						self.vel[1] =0
				
			mouse_pos = pygame.mouse.get_pos()
			
			for i in self.stages:
				
				pygame.draw.rect(gScreen, RED, [i.cords[0], i.cords[1], 16,16])
				if hitDetect(mouse_pos, mouse_pos, [i.cords[0] + self.cords[0], i.cords[1]+ self.cords[1]], [i.cords[0] + 16, i.cords[1] + 16]):
					if mouse_down:
						i.playerbattlers = CharSelect(mult)
						i.run()
						i.completed = True
					
					
			
			self.cords[0] += self.vel[0]
			self.cords[1] += self.vel[1]
			defs.gScreen.fill(BLACK)
			
			defs.gScreen.blit(self.image, [self.cords[0], self.cords[1]])
			
			for i in self.stages:
				
				pygame.draw.rect(gScreen, RED, [i.cords[0] + self.cords[0], i.cords[1] + self.cords[1], 16,16])
			
			if mouse_down:
				defs.gScreen.blit(mouse_pointer2,mouse_pos)
			else:
				defs.gScreen.blit(mouse_pointer,mouse_pos)
   
			pygame.display.flip()
   
  
			clock.tick(60)
		

theWorld = World([st1])


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
		
		defs.gScreen.blit(i.text, [330+ 6 + x*175, y*30 + 370 + 5])
		if i.cost <= player.power:
			defs.gScreen.blit(i.type.img, [330 + x*175, y*30 + 370])
		
		else:
			defs.gScreen.blit(lockedskill, [330 + x*175, y*30 + 370])
			
		x += 1	
		
	pygame.draw.rect(gScreen, GREEN, [21,371,player.hp / 278,28])
	pygame.draw.rect(gScreen, BLUE, [10, 430, player.power * 2, 28])
	defs.gScreen.blit(font.render("HP: " + str(player.hp), True, (0,0,255)), [75, 376])
	defs.gScreen.blit(font.render("Power: " + str(player.power), True, (255,255,255)), [75, 426])
	defs.gScreen.blit(font.render(player.name + "'s turn", True, (255,255,255)), [75, 476])
	


		
aitest = False
def CharSelect(mult):
	global aitest
	done = False
	dispchar2 = defs.NO		
	
	battling = False

	thesebattlers = []
	thisplayer = player1
	mouse_down = False
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

			x += 1

		if hitDetect(mouse_pos, mouse_pos, [529, 434], [698, 498]):
			if thisplayer == player2:
				if mouse_down:
					if aitest:
						mult = False
						for i in player2.battlers:
							i.isAi = True
					theBattle = Battle(player1.battlers, player2.battlers, "", NoDial, mult, defs.cattheme)
		
					theBattle.battle()
					
					
					
					
			if mouse_down:
				if mult == False and aitest == False:
					return player1.battlers
				else:
					thisplayer = player2
					mouse_down = False
					time.sleep(1)
		
		
		defs.gScreen.fill(WHITE)
		defs.gScreen.blit(menuui, [0, 0])
		x = 0
		y = 0
		
		for i in range(384):
			loaded = False
			if x > 23:
				x = 0
				y += 1
			
			for f in unlockedchars:
				if f.cords[0] == x and f.cords[1] == y:
					defs.gScreen.blit(f.img, [3 + 22*x,3 + 22*y])
					loaded = True
			
			if not loaded:
				defs.gScreen.blit(lockedchar, [3 + 22*x,3 + 22*y])
				loaded = False
					
			x += 1
				
		defs.gScreen.blit(selector1, [thisplayer.x1*22 + 1, thisplayer.y1*22 + 1])
		defs.gScreen.blit(selector2, [thisplayer.x2*22 + 1, thisplayer.y2*22 + 1])
		defs.gScreen.blit(selector3, [thisplayer.x3*22 + 1, thisplayer.y3*22 + 1])
		
		for i in range(len(thisplayer.battlers)):
		
			localbattler = thisplayer.battlers[i]
		
			defs.gScreen.blit(dispchar2.image, [644, 370])
		
			defs.gScreen.blit(localbattler.menuImg, [4, i * 47 + 359])
			defs.gScreen.blit(font.render(localbattler.name, True, BLACK), [56, i * 47 + 359])
			
			atypes = ""
			for f in localbattler.types:
				atypes += f.name + " "
			defs.gScreen.blit(font.render(atypes, True, BLACK), [56, i * 47 + 375])
			defs.gScreen.blit(font.render("Str: " + str(localbattler.str) + "   Con: " + str(localbattler.con) + "   Int: " + str(localbattler.int) + "   Mdf: " + str(localbattler.mag) + "   Agil: " + str(localbattler.agil) + "   Crit: " + str(localbattler.crit), True, BLACK), [56, i * 47 + 391])
		
		if mouse_down:
			defs.gScreen.blit(mouse_pointer2,mouse_pos)
		else:
			defs.gScreen.blit(mouse_pointer,mouse_pos)
		
		testAnim.blit(gScreen, [0,0])
		
		
		defs.cootheme.reset()

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
done = False
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
	if hitDetect(mouse_pos, mouse_pos, [10,50], [26, 66]):
		if mouse_down:
			mult = True
			CharSelect(mult)
			mouse_down = False
	if hitDetect(mouse_pos, mouse_pos, [60,50], [60 + 16, 66]):
		if mouse_down:
			mult = False
			theWorld.run(mult)
			mouse_down = False
			
	if hitDetect(mouse_pos, mouse_pos, [110,50], [110 +16, 66]):
		if mouse_down:
			mult = True
			aitest = True
			CharSelect(mult)
			mouse_down = False
			
		

	
	if mouse_down:
			defs.gScreen.blit(mouse_pointer2,mouse_pos)
	else:
		defs.gScreen.blit(mouse_pointer,mouse_pos)
		
	defs.cootheme.play()

	pygame.display.flip()


	clock.tick(60)



	

		
		
	