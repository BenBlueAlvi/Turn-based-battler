

import pygame
import random
import time
import math
#import pyganim
from decimal import *

from pygame.locals import *


clock = pygame.time.Clock()
pygame.mixer.init()
music = pygame.mixer.music.load("reformat.ogg")

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

printing = False
log = []



def bubble_sort(items):
	""" Implementation of bubble sort """
	for i in range(len(items)):
		for j in range(len(items)-1-i):
			if items[j] > items[j+1]:
				items[j], items[j+1] = items[j+1], items[j] 
	return items

timer = 0
def printb(text):
	global disptext
	global printing
	global log
	global timer
	
	newtext = font.render(text,True,BLACK)
	log.append(newtext)
	
	if not printing:
		disptext = newtext
		timer = 60

		

'''		
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
'''

		
class Type(object):
	def __init__(self, name, weks, strs):
		self.name = name
		self.weks = weks
		self.strs = strs
		self.img = pygame.image.load("assets/moveboxes/" + self.name.lower() +".png")

normal = Type("Normal", ["Tech", "Ghost"], ["nul"])
fire = Type("Fire", ["Water"], ["Earth"])
water = Type("Water", ["Air", "Electric", "Grass"], ["Fire"])
air = Type("Air", ["Earth", "Electric"], ["Water", "Fighting"])
earth = Type("Earth", ["Fire", "Grass", "Fighting", "Tech", "Astral"], ["Air", "Poison"])
dark = Type("Dark", ["Light"], ["Normal"])
light = Type("Light", ["Dark"], ["Normal"])
#-----------------------------------------
grass = Type("Grass", ["Fire","Ice", "Tech"], ["Water", "Earth"])
electic = Type("Electric", ["Earth"], ["Water", "Air"])
ice = Type("Fire", ["Fire", "Fighting"], ["Grass"])
fighting = Type("Fighting", ["Physic"], ["Normal"])
acid = Type("Acid", ["Earth", "Grass"], [""])
poison = Type("Poison", ["Dark"], ["Grass"])
blood = Type("Blood", ["Acid", "Poison"], ["Dark"])
ghost = Type("Ghost", ["Physic", "Magic"], ["Fighting", "Normal"])
magic = Type("Magic", ["Fighting", "Astral"], ["Chaos"])
astral = Type("Astral", ["Chaos"], ["Ghost", "Tech"])


physic = Type("Physic",["Normal", "astral"], ["Fighting"])
tech = Type("Tech", ["Electric", "Acid", "Astral"], ["Earth", "Chaos"])
unknown = Type("Unknown", ["none"], ["none"])
chaos = Type("Chaos", ["Tech"], ["Physic"])
turn = 0
class Effect(object):
	def __init__(self, effect):
		self.effect = effect
		self.endeffect = 0
		self.img = pygame.image.load("Assets/ui/" + effect + ".png")
		
	def update(self, target):
		if self.effect == "burn":
			damage = 25 + random.randint(1, 25)
			self.endeffect = random.randint(1,3)
			for i in thesebattlers:
				if i.ability == "watch them burn":
					self.endeffect = 0
					damage *= 2

			if target.ability == "tank" and damage > 100:
				damage = 100

			target.hp -= damage
			printb(target.name + " is on fire!   " + target.name + " takes " + str(damage) + " damage")
			
			
			if self.endeffect == 2:
				printb(target.name + " put out the fire!")
				target.effects.remove(self)
				
				
		if self.effect == "bleed":
			if target.ability == "tank":
				target.hp -= target.hp / 10
			else:
				target.hp -= target.hp / 4
			printb(target.name + " is on bleeding out!")
			self.endeffect = random.randint(1,3)
			if self.endeffect == 2:
				printb(target.name + " is no longer bleeding")
				target.effects.remove(self)
				
		if self.effect == "magicmute":
			target.power -= 1
			printb(target.name + " can't gain power!")
			self.endeffect = random.randint(1,3)
			if self.endeffect == 2:
				printb(target.name + " can gain power again!")
				target.effects.remove(self)
		
				
		if self.effect == "defend":
			target.con = target.basecon * target.basecon
			printb(target.name + " is defending!")
			self.endeffect += 1
			if self.endeffect == 2:
				target.effects.remove(self)
				printb(target.name + " is no longer defending!")
				self.resetStats(target)
				
		if self.effect == "forceshield":
			target.con = target.basecon * 3
			target.mag = target.basemag * 3
			printb(target.name + " has a shield up!")
			self.endeffect = random.randint(1,2)
			if self.endeffect == 2:
				target.effects.remove(self)
				printb(target.name + " no longer has a shield up!")
				self.resetStats(target)
				
		if self.effect == "confusion":
			target.con = target.basecon / 2
			target.mag = target.basemag / 2
			printb(target.name + " is confused!")
			self.endeffect = random.randint(1,2)
			if self.endeffect == 2:
				target.effects.remove(self)
				target.con = target.basecon
				target.mag = target.basemag
				printb(target.name + " is no longer confused!")
				self.resetStats(target)
				
		if self.effect == "immortal":
			target.con = 100000000
			target.mag = 100000000
			printb(target.name + " is invincible!")
			self.endeffect = random.randint(1,2)
			if self.endeffect == 2:
				target.effects.remove(self)
				
				printb(target.name + " is no longer invincible!")
				self.resetStats(target)
				
		if self.effect == "block":
			target.con = 100000000
			printb(target.name + " is blocking attacks!")
			self.endeffect = random.randint(1,2)
			
			if self.endeffect == 2:
				target.effects.remove(self)
				printb(target.name + " is no longer blocking attacks!")
				self.resetStats(target)
				
				
		if self.effect == "poison":
			damage = target.hp / 10
			if target.ability == "tank" and damage > 100:
				damage = 100
			target.hp -= damage
			printb(target.name + " is poisoned!   " + target.name + " takes " + str(damage) + " damage")
			self.endeffect = random.randint(1,4)
			if self.endeffect == 2:
				printb(target.name + " is no longer poisoned!")
				target.effects.remove(self)
				
		if self.effect == "rebuff":
			
			printb(target.name + " is encouraged!")
			target.str += target.basestr * 1.4
			target.int += target.baseint * 1.4
			if self.endeffect == 1:
				printb(target.name + " is no longer encouraged. :(")
				target.effects.remove(self)
				self.resetStats(target)
			self.endeffect += 1
			
		if self.effect == "meditate":
			
			printb(target.name + " is meditating!")
			target.power += 3
			target.con -= 10
			target.mag += 5
			if self.endeffect == 1:
				printb(target.name + " is no longer meditating!")
				target.effects.remove(self)
				self.resetStats(target)
			self.endeffect += 1
				
		if self.effect == "planAhead":
		
			printb(target.name + " is scheming!")
			
			target.crit += 2
			target.int += target.int / 10
			target.str += target.str / 10
			if self.endeffect == 1:
				printb(target.name + " is no longer scheming!")
				target.effects.remove(self)
				self.resetStats(target)
			self.endeffect += 1
		
		if self.effect == "dodgeUp":
			printb(target.name + " is prepared!")
			target.dodgeChance = target.basedodgeChance + 25
			if self.endeffect == 1:
				printb(target.name + " is no longer prepared!")
				target.effects.remove(self)
				self.resetStats(target)
			self.endeffect += 1
			
		if self.effect == "earthStage":
			self.resetStats(target)
			target.con += 50
			target.mag += 50
			target.int -= 20
			target.str -= 20
			try:
				target.effects.remove(moonStagef)
			except:
				pass
			try:
				target.effects.remove(otherStagef)
			except:
				pass
				
			
			
		if self.effect == "moonStage":
			self.resetStats(target)
			target.mag += 50
			target.int += 50
			target.str -= 25
			target.con -= 25
			try:
				target.effects.remove(earthStagef)
			except:
				pass
			try:
				target.effects.remove(otherStagef)
			except:
				pass
			
		if self.effect == "otherStage":
			self.resetStats(target)
			
			target.int += 75
			target.crit += 10
			target.dodgeChance += 20
			target.con -= 50
			target.mag -= 50
			try:
				target.effects.remove(moonStagef)
			except:
				pass
			try:
				target.effects.remove(earthStagef)
			except:
				pass
		
		if self.effect == "death":
			pass
			#Death stufff here
			
		
			
		else:
			pass
	def resetStats(self, target):
		target.con = target.basecon
		target.mag = target.basemag
		target.str = target.basestr
		target.int = target.baseint
		target.crit = target.basecrit
		target.dodgeChance = target.basedodgeChance
		target.agil = target.baseagil
			
	def buildNew(self):
		neweff = Effect(self.effect)
		return neweff
		
				
			
burn = Effect("burn")
magicmute = Effect("magicMute")
defense = Effect("defend")
bleed = Effect("bleed")
forceshield = Effect("forceShield")
confusion = Effect("confusion")
immortal = Effect("immortal")
block = Effect("block")
poison = Effect("poison")
rebuff = Effect("rebuff")
meditatef = Effect("meditate")
planAheadf = Effect("planAhead")
dodgeUp = Effect("dodgeUp")
death = Effect("death")
earthStagef = Effect("earthStage")
otherStagef = Effect("otherStage")
moonStagef = Effect("moonStage")

		

class Skill(object):
	def __init__(self, name, type, phys, atk, var, spd, crit, hitChance, cost, effects, spec):
		self.name = name
		self.type = type
		self.atk = atk
		self.var = var
		self.spd = spd
		self.phys = phys
		self.cost = cost
		self.spec = spec
		self.crit = crit
		
		self.hitChance = hitChance
		self.effects = effects
		self.text = font.render(name, True, WHITE)
		
		
	def use(self, user, target):
		
		message = ""

		hit = self.hitChance - target.dodgeChance

		if target.ability == "Cuteness" and hit > 70:
			hit = 70
		
		if user.ability == "Blood hunt" and hit < 75 and not ghost in target.types:
			hit = 75

		if random.randint(1,100) < hit or "trueHit" in self.spec:
			
		
			if self.phys:
				damage = (user.str + self.atk+ random.randint(0, self.var)) - target.con
			
			else:
				damage = (user.int + self.atk + random.randint(0, self.var)) - target.mag
			
			for i in target.types:
				if self.type.name in i.weks:
					damage *= 2
					message = " It's super effective!"
					
			for i in target.types:
				if self.type.name in i.strs:
					damage /= 2
					message = " It's not very effective!"
			
			
			
			if random.randint(1,30) + user.crit >= 30:
				damage *= 2
				message += " CRITICAL HIT!"
				if not len(self.effects) == 0:
					target.effects.append(self.effects[1])
			
			if not len(self.effects) == 0:
				if random.randint(1,self.effects[0]) == 1:
					target.effects.append(self.effects[1])
					
			if target.ability == "Creepus":
				user.marks += 1
					
			for i in self.spec:
			
				if i == "vampire":
					user.hp += damage
				
				if i == "defend":
					damage = 0
					user.effects.append(defense.buildNew())
				if i == "powerUp":
					damage = 0
					user.power += 2
				if i == "lifepact":
					damage = user.hp / 2 + user.int
					user.hp /=2
				
				if i == "fullmana":
					damage = ((user.power * (user.int + self.atk)) / 4) + self.atk
					user.power = 0
				if i == "shroud":
					user.con += 6
					user.mag += 6
				if i == "Shield":
					user.effects.append(forceshield.buildNew())
				if i == "atkUp":
					damage = 0
					user.effects.append(planAheadf)
				if i == "division":
					damage = target.hp/5
				if i == "immortal":
					user.effects.append(immortal.buildNew())
				if i == "heal":
					damage = 0
					target.hp += user.int * 3
					if target.ability == "3 worlds":
						target.hp -= user.int * 2
						
				if i == "block":
					damage = 0
					user.effects.append(block.buildNew())
				if i == "powerdrain":
					damage = 0 
					user.power += target.power
					target.power = 0
				
				if i == "revenge":
					damage = user.maxhp - user.hp
				if i == "recover":
					damage = 0
					heal =target.maxhp / 4 
					if target.ability == "3 worlds":
						heal /= 3
					target.hp += heal
					
				if i == "stare":
			
					target.con /=2
					target.mag /=2
				if i == "mark":
					
					target.marks += 1
				if i == "creepyAtk":
		
					damage = target.marks * user.int - target.mag * 2
				if i == "endeffect":
					
					user.effects = []
				if i == "nodam":
					damage = 0
				if i == "removeEff":
					target.effects = []
				if i == "removeUff":
					target.con = target.basecon
					target.mag = target.basemag
					target.int = target.baseint
					target.str = target.basestr
					target.crit = target.basecrit
					target.agil = target.baseagil
					
				if i == "lifeTransfer":
					user.hp -= user.hp/4
					target.hp += (user.hp/4) * 2
					
				if i == "powerTransfer":
					user.power -= user.power/4
					target.power += (user.power/4)
				if i == "meditate":
					user.effects.append(meditatef)
				if i == "dodgeUp":
					user.effects.append(dodgeUp)
				if i == "otherStage":
					user.effects.append(otherStagef)
				if i == "earthStage":
					user.effects.append(earthStagef)
				if i == "moonStage":
					user.effects.append(moonStagef)
				
			if user.hp > 0:
				if target.ability == "3 worlds":
					damage /= 3
				if target.ability == "tank" and damage > 100:
					damage = 100
				if damage < 0:
					damage = 0

				printb(user.name + " uses " + self.name + " and deals " + str(damage) + " damage to " + target.name + message)
				target.hp -= damage
				
		else:
			damage = 0
			printb(user.name + " missed!")
				
				
				
				
		
		
		
		
				
nothing = Skill("nothing", normal, True, 0, 0, 0, 0, 100, 0, [], ["nodam", "trueHit"])
basicAtk = Skill("Basic Attack", normal, True, 5, 5, 1, 0,90, 0, [], [""])
fireBall = Skill("Fire ball", fire, False, 7, 3, -1, 0,90, 2, [1, burn], [""])
waterSpout = Skill("Water Spout", water, False, 2, 10, -1, 0,90, 2, [], [""])
airBlast = Skill("Air Blast", air, False, 7, 1, 2, 0,95, 2, [], [""])
earthShot = Skill("Earth Shot", earth, False, 12, 4, -5, 0,90, 2, [], [""])
defend = Skill("Defend", normal, True, 0, 0, 0, 0,100, 0, [], ["defend", "trueHit"])
scar = Skill("Scar", dark, True, 30, 5, 2, 0,97, 1, [3,bleed], ["vampire"])
nuke = Skill("Nuke", fire, True, 200, 100, -4, 0,100, 20, [], ["trueHit", "hitAll"])
shardSwarm = Skill("Shard Swarm", chaos, False, 20, 30, 4, 0,90, 10, [], [""])
magicMute = Skill("Magic Mute", chaos, False, 0, 0, -2, 0,100, 5, [1,magicmute], ["trueHit"])
powerUp = Skill("Power Up", chaos, False, 0, 0, 10, 0,100, 2, [], ["powerup", "trueHit"])
magicAbsorb = Skill("Magic Absorb", chaos, False, 0, 0, 5, 0,100, 3, [], ["trueHit"])
destroy = Skill("Destroy", chaos, False, 100, 100, -100, 15,100, 7, [], [""])
vampire = Skill("Vampire", blood, False, 20, 10, 5, 20,90, 2, [], ["vampire", "vampire"])
meteorStorm = Skill("Meteor Storm", astral, False, 100, 50, -100, 0,50, 7, [2, burn], [""])
block = Skill("Block", fighting, True, 0, 0, 10, 0,100, 1, [], ["block", "trueHit"])
powerDrain = Skill("Power Drain", astral, False, 25, 25, -10, 0,100, 2, [], ["powerdrain", "trueHit"])
#-----------------------------------------------------------

slash = Skill("Slash", normal, True, 10, 10, 3, 5,90, 0, [], [""])
bite = Skill("Bite", normal, True, 20, 5, 0, 5,92, 2, [3,bleed], [""])
kick = Skill("Kick", fighting, True, 15, 10, 4, 0,90, 1, [], [""])
dodge = Skill("Dodge", fighting, True, 0, 0, 10, 0,100, 2, [], ["trueHit", "dodgeUp"])
rip = Skill("Rip", dark, True, 20, 10, -1, 0,90, 4, [1,bleed], [""])
consumeFlesh = Skill("Consume Flesh", blood, True, 30, 5, -5, 0,90, 3, [2,bleed], ["vampire"])

#----------------------------------------------------------------
chaosBolt = Skill("Chaos Bolt", chaos, False, 10, 20, 1, 0,90, 1, [], [""])
setFire = Skill("Set Fire", fire, False, 5, 20, -1, 0,90, 3, [3,burn], ["hitAll"])
forceShield = Skill("Force Shield", magic, False, 0, 0, -2, 0,100, 2, [], ["shield", "nodam", "trueHit"])
summon = Skill("Summon", magic, False, 0, 0, -4, 0,100, 4, [], ["trueHit"])
chaosBeam = Skill("Chaos Beam", chaos, False, 20, 20, -10, 0,94, 0, [], ["fullmana"])
meditate = Skill("Meditate", magic, False, 0, 0, 0, 0,100, -1, [], ["nodam", "trueHit", "meditate"])
lifePact = Skill("Life Pact", blood, False, 0, 0, -2, 0,100, 4, [], ["lifepact", "trueHit"])
shroud = Skill("Shroud", dark, False, 0, 0, 10, 0,100, 2, [], ["shroud", "trueHit"])
#-------------------------------------------------------------------
bludgeon = Skill("Bludgeon", fighting, True, 10, 2, -1, 0,90, 0, [], [""])
stab = Skill("Stab", fighting, True, 5, 7, 2, 0,100, 0, [], [""])
confuse = Skill("Confuse", physic, False, 0, 0, 10, 0,80, 2, [1,confusion], [""])
planAhead = Skill("Plan Ahead", tech, False, 0, 0, -10, 0,100, 2, [], ["atkUp", "trueHit"])
erase =Skill("Erase", unknown, False, 0, 0, -10, 0,100, 5, [], ["division"])
create = Skill("Create", unknown, False, 0,0, -10, 0,100, 5, [], ["immortal", "trueHit"])
mend = Skill("Mend", magic, False, 0,0, 1, 0,100, 3, [], ["heal", "trueHit"])
#------------------------------------------------------------------
energiBeam = Skill("Energy Beam", tech, False, 77, 10, -3, 0,90, 5, [], [""]) 
wellspring = Skill("Wellspring", tech, False, 0, 0, 3, 0,100, -10, [], ["trueHit"])
#-----------------------------------------------------------------
bladeFlash = Skill("Blade Flash", fighting, True, 6, 5, 10, 2,90, 1, [], [""])
cleave = Skill("Cleave", fighting, True, 20, 20, -2, 2,90, 2, [2, bleed], [""])
revenge = Skill("Revenge", dark, False, 0, 0, 10, 0,100, 5, [], ["revenge"])
#----------------------------------------------------------------------
obsidianBlast = Skill("Obsidian Blast", fire, False, 30, 10, -3, 0,90, 5, [1, burn] ,[""])
recover = Skill("Recover", magic, False, 0, 0, 10, 0,100, 7, [], ["recover", "endeffect", "trueHit"])
psionicRadiance = Skill("Psionic Radiance", physic, False, 30, 10, -2, 3,100, 3, [], [""])
#------------------------------------------------------------------------
stare = Skill("Stare", physic, False, 30, 10, -2, 15,100, 5, [], [""])
blink = Skill("Blink", physic, True, 5, 5, 1, 0,100, 0, [], ["mark"])
creepyAtk = Skill("Creep Attack", physic, False, 5, 5, 1, 0,90, 0, [], ["creepyAtk"])
inhale = Skill("Inhale", air, False, 0, 0, 3, 0,100, 0, [], ["defend", "mark"])
observe = Skill("Observe", unknown, False, 0, 0, 3, 0,100, 1, [], ["mark", "mark", "mark", "mark", "mark", "mark", "nodam"])
exhale = Skill("Exhale", air, False, 5, 10, 3, 0,90, 0, [], ["mark"])
#------------------------------------------------------------------------
sneeze = Skill("Sneeze", acid, False, 14, 6, 6, 0,90, 1, [2, poison], [""])

eggon = Skill("Egg On", normal, True, 0, 0, 10, 0,100, 2, [1, rebuff], ["trueHit"])
rebuke = Skill("Rebuke", normal, True, 0, 0, 10, 0,100, 1, [], ["removeEff", "removeUff", "trueHit"])

blast = Skill("Blast", tech, False, 20, 20, 5, 8, 95, 2, [2, burn], [""])
fission = Skill("Fission", fire, False, 20, 40, -1, 0, 90, 0, [2, burn], ["powerDown", "fullmana"])
fusion = Skill("Fusion", fire, False, 1, 40, -1, 0, 90, 1, [2,burn], ["powerUp"])

lifeTransfer = Skill("Life Transfer", blood, False, 0, 0, 10, 0,100, 2, [], ["lifeTransfer", "nodam"])
powerTransfer = Skill("Power Transfer", tech, False, 0, 0, 10, 0, 100, 0, [], ["powerTransfer", "nodam"])

earthStage = Skill("Earth Stage", astral, False, 10, 15, 10, 0, 100, 0, [], ["trueHit","hitAll","earthStage"])
moonStage = Skill("Moon Stage", astral, False, 10, 15, 10, 0, 100, 0, [], ["trueHit","hitAll","moonStage"])
otherStage = Skill("Otherworld Stage", astral, False, 10, 15, 10, 0, 100, 0, [], ["trueHit","hitAll","otherStage"])
voidSnap = Skill("Void Snap", astral, False, 20, 10, 4, 5, 97, 1, [2,bleed], [""])
chains = Skill("Chains", normal, True, 30, 2, 1, 5, 90, 1, [], [""])
earthenVortex = Skill("Earthen Vortex", earth, False, 30, 40, 5, 6, 90, 2, [], [""])
astralVortex = Skill("Astral Vortex", astral, False, 50, 40, 5, 6, 90, 3, [], [""])
chaosVortex = Skill("Chaos Vortex", chaos, False, 20, 60, 5, 6, 90, 2, [], [""])




class Char(object):
	def __init__(self, name, types, hp, str, int, con, mag, agil, crit, dodgeChance, lvl, xp, skills, ability, image, cords, menuImg):
		self.name = name
		self.hp = hp
		self.str = str
		self.basestr = str
		self.types = types
		self.int = int
		self.baseint = int
		self.con = con
		self.basecon = con
		self.mag = mag
		self.basemag = mag
		self.agil = agil
		self.baseagil = agil
		self.lvl = lvl
		self.xp = xp
		self.effects = []
		self.skills = skills
		self.image = image
		self.img = image
		self.cords = cords
		self.maxhp = hp
		self.crit = crit
		self.basecrit = crit
		self.dodgeChance = dodgeChance
		self.basedodgeChance = dodgeChance
		self.ability = ability
		self.marks = 0
		self.power = 0
		self.menuImg = menuImg
		self.goskill = "hoi"
		self.target = ["bob"]
		self.updated = False
		self.x = 0
		self.y = 0
		self.basey = 0
		self.basex = 0
		self.ym = 1
		
		
	def buildNew(self):
		newchar = Char(self.name, self.types, self.hp, self.str, self.int, self.con, self.mag, self.agil, self.crit, self.dodgeChance, self.lvl, self.xp, self.skills, self.ability, pygame.transform.scale(pygame.image.load(self.image), [50, 50]), self.cords, pygame.transform.scale(pygame.image.load(self.image), [42, 42]))
		newchar.img = pygame.image.load(self.image)
		newchar.target = [NOT]
		return newchar
		
	def reBuild(self):
		newchar = Char(self.name, self.types, self.hp, self.str, self.int, self.con, self.mag, self.agil, self.crit, self.dodgeChance, self.lvl, self.xp, self.skills, self.ability, self.image, self.cords, self.menuImg)
		newchar.img = self.image
		return newchar
		
NOT = Char("???", [unknown], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, [], "", "Assets/battlers/locked.png", [-1,0], "")

Mage = Char("Meigis", [normal, chaos], 500, 5, 15, 5, 15, 4, 0, 10, 1, 0, [basicAtk, fireBall, waterSpout, airBlast, earthShot, defend], "", "Assets/battlers/Mage.png", [5,0], "")

Mouther = Char("Mouther", [earth], 500, 20, 0, 10, 5, 4, 0, 10, 1, 0, [basicAtk, bite, consumeFlesh, defend], "", "Assets/battlers/Mouther.png", [4,0], "")

NotScaryGhost = Char("Not Scary Ghost", [ghost], 1000, 0, 0, 10, 75, 2, 0, 10, 1, 0, [basicAtk, sneeze, forceShield, recover], "tank", "Assets/battlers/Not_Scary_Ghost.png", [2, 15], "")
Creep = Char("Creepy Bald Guy", [physic, unknown], 750, 10, 10, 15, 50, 0, 0, 0, 1, 0, [creepyAtk, blink, stare, inhale, exhale, observe], "Creepus", "Assets/battlers/Creepy_Bald_Guy.png", [3, 15], "")
KnowingEye = Char("Knowing Eye", [physic, unknown, astral], 750, 0, 75, 0, 75, 5, 6, 5, 1, 0, [creepyAtk, observe, meditate, magicMute, forceShield, create], "Creepus", "Assets/battlers/wip.png", [4, 15], "")

Nic = Char("Nic", [chaos], 500, 15, 50, 10, 25, 4, 0, 10, 1, 0, [basicAtk, magicMute, shardSwarm, powerUp, defend], "", "Assets/battlers/nic.png", [5,8], "")



Scarlet = Char("Scarlet", [dark, blood], 100, 20, 20, 5, 20, 6, 0, 10, 1, 0, [basicAtk, scar, vampire, destroy, lifePact, defend], "", "Assets/battlers/vamp.png", [1,0], "")

Flan = Char("Flan", [dark,blood], 200, 35, 30, 10, 20, 7, 10, 20, 1, 0, [slash, rip, scar, vampire, destroy, lifePact, setFire, lifeTransfer], "watch them burn", "Assets/battlers/flandre.png", [5,7], "")
Nue = Char("Nue", [astral, dark], 300, 25, 40, 10, 50, 4, 15, 10, 1, 0, [basicAtk, meteorStorm, powerTransfer, forceShield, powerDrain, stab, meditate, defend], "Unidentifiable", "Assets/battlers/nue.png", [4,7], "")
Okuu = Char("Okuu", [fire, tech], 500, 15, 50, 30, 10, 1, 5, 5, 1, 0, [bludgeon, blast, fusion, fission, nuke, forceShield, recover], "Radiation", "Assets/battlers/reiji.png", [3,7], "")
Lapis = Char("Lapis", [astral], 400, 20, 20, 10, 10, 4, 5, 20, 1, 0, [chains, voidSnap, earthStage, moonStage, otherStage, earthenVortex, chaosVortex, astralVortex], "3 worlds", "Assets/battlers/lapis.png", [6,7], "")

Epic = Char("Epic", [tech], 1000, 25, 50, 35, 45, 7, 10, 10, 1, 0, [basicAtk,energiBeam, wellspring, defend], "", "Assets/battlers/epic.png", [7,8], "")

Coo33 = Char("Coo33", [dark, blood], 250, 50, 0, 30, 0, 10, 10, 10, 5, 0, [basicAtk, slash, bite, kick, dodge, rip, consumeFlesh, defend], "Blood hunt", "Assets/battlers/Coo33.png", [3,3], "")
Alpha = Char("Alpha", [normal, earth, fighting], 500, 50, -50, 30, 5, 5, 0, 10, 1, 0, [basicAtk, slash, cleave, bladeFlash, revenge, mend, defend], "", "Assets/battlers/alpha.png", [8,4], "")
Siv = Char("Siv", [normal, earth, dark, physic, chaos, magic], 250, 0, 50, 0, 38, 5, 7, 10, 1, 0, [basicAtk, chaosBolt, setFire, forceShield, chaosBeam, meditate, lifePact, shroud], "", "Assets/battlers/siv.png", [4,2], "")
CoosomeJoe = Char("Coosome Joe", [light, tech], 500, 25, 25, 25, 25, 5, 2, 10, 1, 0, [basicAtk, bludgeon, erase, create, confuse, planAhead, mend, defend], "", "Assets/battlers/Coosome.png",  [3, 8], "")
Durric = Char("Durric", [earth, light, fighting, physic], 1000, 25, 25, 75, 25, 0, 0, 1, 1, 0, [basicAtk, forceShield, cleave, obsidianBlast, recover, psionicRadiance, mend, defend], "Regen", "Assets/battlers/Durric.png", [4, 4], "")
Catsome = Char("Catsome", [light, ghost, physic], 1000, 10, 35, 10, 15, 5, 5, 10, 1, 0, [slash, bite, eggon, rebuke, mend, recover], "Cuteness", "Assets/battlers/catsome.png",[6,9], "")

NO = NOT.buildNew()	



		
unlockedchars = [Lapis.buildNew(), Flan.buildNew(), Okuu.buildNew(), Nue.buildNew(), Scarlet.buildNew(), Mage.buildNew(), Mouther.buildNew(), Nic.buildNew(), Siv.buildNew(), Coo33.buildNew(), CoosomeJoe.buildNew(), Epic.buildNew(), Alpha.buildNew(), Durric.buildNew(), Creep.buildNew(), NotScaryGhost.buildNew(), Catsome.buildNew(), KnowingEye.buildNew()]			

class Player(object):
	def __init__(self, name):
		self.acbattler = NOT.buildNew()
		self.battlers = [NOT.buildNew(), NOT.buildNew(), NOT.buildNew()]
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
		
	
	
dispchar2 = NO		
	
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
					
				if event.key == K_DOWN:
					thisplayer.y3 += 1
					
				if event.key == K_LEFT:
					thisplayer.x3 -= 1
				
					
				if event.key == K_RIGHT:
					thisplayer.x3 += 1
					
				if event.key == K_w:
					thisplayer.y1 -= 1
					
				if event.key == K_s:
					thisplayer.y1 += 1
					
				if event.key == K_a:
					thisplayer.x1 -= 1
				
					
				if event.key == K_d:
					thisplayer.x1 += 1
					
					
				if event.key == K_i:
					thisplayer.y2 -= 1
					
				if event.key == K_k:
					thisplayer.y2 += 1
					
				if event.key == K_j:
					thisplayer.x2 -= 1
				
					
				if event.key == K_l:
					thisplayer.x2 += 1
			
			
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
				dispchar = NO
				thisplayer.battlers[0] = NO

		
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
				dispchar2 = NO
				thisplayer.battlers[1] = NO

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
				dispchar2 = NO
				thisplayer.battlers[2] = NO

		x += 1

	if hitDetect(mouse_pos, mouse_pos, [529, 434], [698, 498]):
		if thisplayer == player2:
			if mouse_down:
				battling = True
				ready = False
			
				thesebattlers += player1.battlers + player2.battlers
				x = 0
				y = 0
				for i in thesebattlers:
					if y > 2:
						y = 0
						x += 1
					i.basex = x * 550 + 50
					i.basey = y * 100 + 50
					y += 1
					
				
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
	

	#testAnim.blit(gScreen, [0,0])

	pygame.display.flip()	
	clock.tick(60)
	
	
	thebattler = 0
	powergiven = False
	pickenm = False
	increment = 0
	timer = 0
	mincrement = 0
	
#--------------------------------------------------------------------------------------------------------------------------------------------------		
#--------------------------------------------------------------------------------------------------------------------------------------------------	
#--------------------------------------------------------------------------------------------------------------------------------------------------	
#--------------------------------------------------------------------------------------------------------------------------------------------------	
#--------------------------------------------------------------------------------------------------------------------------------------------------	
#--------------------------------------------------------------------------------------------------------------------------------------------------	
#--------------------------------------------------------------------------------------------------------------------------------------------------	
#--------------------------------------------------------------------------------------------------------------------------------------------------	
	
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
				i.update(thisbattler)
			if thisbattler.ability == "Unidentifiable":
				thisbattler.marks = 0
			if thisbattler.ability == "Radiation":
				for l in thesebattlers:
					l.hp -= 25
				printb(thisbattler.name + "'s radiation hurt everyone!")

			if thisbattler.ability == "Regen":
				thisbattler.hp += 25
				printb(thisbattler.name + " is healing themself!")
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
						print thisbattler.target[0]
						ready = False
						if "hitAll" in  thisbattler.goskill.spec:
							thisbattler.target = []
							if thisbattler in player1.battlers:
								thisbattler.target = player2.battlers
							elif thisbattler in player2.battlers:
								thisbattler.target = player1.battlers
						
						thebattler += 1
						
						pickenm = False
					y += 1
									
		

		else:
			thisbattler.goskill = nothing
			thebattler += 1
			pickenm = False
			ready = False
		
		
		
		
		
		
		
		agillist = []
		for i in thesebattlers:
			agillist.append(i)
		#print "thebattler:", thebattler
		if thebattler >= len(thesebattlers):
			
			
			#sorting
			for i in range(len(agillist)):
				for j in range(len(agillist)-1-i):
					if agillist[j].agil + agillist[j].goskill.spd  > agillist[j+1].agil + agillist[j+1].goskill.spd:
						agillist[j], agillist[j+1] = agillist[j+1], agillist[j] 
			for i in agillist:
				pass
				#print i.target
			if len(agillist[increment].target) > 1:
				if not printing:
					agillist[increment].goskill.use(agillist[increment],agillist[increment].target[mincrement])
				
					if mincrement > 2:
						agillist[increment].power -= agillist[increment].goskill.cost
				
			else:
				if not printing:
					agillist[increment].goskill.use(agillist[increment],agillist[increment].target[0])
					agillist[increment].power -= agillist[increment].goskill.cost
			if not printing:
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
				
					for i in thesebattlers:
						i.updated = False
			
			
			
			
			
			

    # --- Drawing code should go here
	
	#player
	#animation:
		if not printing and not thebattler >= len(thesebattlers):
			if thisbattler in player1.battlers:
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
					if not i == thesebattlers[thebattler] and not thebattler >= len(thesebattlers):
						gScreen.blit(i.image,[x * 550 + 50, y * 100 + 50])
				except:
					gScreen.blit(i.image,[x * 550 + 50, y * 100 + 50])
				
				pygame.draw.rect(gScreen, RED, [x* 550 + 50, y* 100 + 25,int(i.hp) / 20,5])
				 
				for f in i.effects:
					pygame.draw.rect(gScreen, RED, [x* 550 + 50, y* 100 + 25,int(i.hp) / 20,5])
					gScreen.blit(f.img, [x* 550 + 40, y * 100 + 25])
				
				
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
				i.effects.append(death)
				
			#reset character here
			
		for i in player1.battlers:
			if i.hp <= 0:
				player1.battlers.remove(i)
				
		for i in player2.battlers:
			if i.hp <= 0:
				player2.battlers.remove(i)
				
		if len(player1.battlers) == 0:
			printb("Player 2 WINS!")
			print "Player 2 Wins"
			player1.battlers.append([NO, NO, NO])
			break
			
		elif len(player2.battlers) == 0:
			printb("Player 1 WINS!")
			print "Player 1 Wins"
			player2.battlers.append([NO, NO, NO])
			break
		
		if timer > 0:
			timer -= 1
			gScreen.blit(disptext, [10, 320])
			printing = True
			pygame.draw.rect(gScreen, BLACK, [0,350,700,150])
		
		if timer <= 0:
			printing = False
		
		if thebattler == len(thesebattlers):
			pygame.draw.rect(gScreen, BLACK, [0,350,700,150])
	
 
		# --- Go ahead and update the screen with what we've drawn.
		pygame.display.flip()
 
		# --- Limit to 60 frames per second
		clock.tick(60)
		
		
		
		
	