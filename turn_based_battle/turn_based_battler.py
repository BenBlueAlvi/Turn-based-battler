import pygame
import random
import time
import math
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
selector2 = pygame.image.load("assets/ui/selector3.png")

hasprinted = False
log = []
def printb(text):
	global disptext
	global hasprinted
	global log
	log.append(text)
	newtext = font.render(text,True,BLACK)
	time.sleep(1)
	if hasprinted:
		disptext = newtext
		
		
		
	


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


physic = Type("Physic",["Normal"], ["Fighting"])
tech = Type("Tech", ["Electric", "Acid", "Astral"], ["Earth", "Chaos"])
unknown = Type("Unknown", ["none"], ["none"])
chaos = Type("Chaos", ["Tech"], ["Physic"])
turn = 0
class Effect(object):
	def __init__(self, effect):
		self.effect = effect
		self.endeffect = 0
		
	def update(self, target):
		if self.effect == "burn":
			damage = 25 + random.randint(1, 25)
			target.hp -= damage
			printb(target.name + " is on fire!   " + target.name + " takes " + str(damage) + " damage")
			self.endeffect = random.randint(1,3)
			if self.endeffect == 2:
				printb(target.name + " put out the fire!")
				target.effects.remove(self)
				
				
		if self.effect == "bleed":
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
			target.con += target.con
			printb(target.name + " is defending!")
			self.endeffect += 1
			if self.endeffect == 2:
				target.effects.remove(self)
				target.con = target.basecon
				printb(target.name + " is no longer defending!")
				
		if self.effect == "forceshield":
			target.con *= 3
			target.int *= 3
			printb(target.name + " has a shield up!")
			self.endeffect = random.randint(1,2)
			if self.endeffect == 2:
				target.effects.remove(self)
				target.con = target.basecon
				target.mag = target.basemag
				printb(target.name + " no longer shield up!")
				
		if self.effect == "confusion":
			target.con /= 2
			target.mag /= 2
			printb(target.name + " is confused!")
			self.endeffect = random.randint(1,2)
			if self.endeffect == 2:
				target.effects.remove(self)
				target.con = target.basecon
				target.mag = target.basemag
				printb(target.name + " is no longer confused!")
				
		if self.effect == "immortal":
			target.con = 100000000
			target.mag = 100000000
			printb(target.name + " is invincible!")
			self.endeffect = random.randint(1,2)
			if self.endeffect == 2:
				target.effects.remove(self)
				target.con = target.basecon
				target.mag = target.basemag
				printb(target.name + " is no longer invincible!")
				
		if self.effect == "block":
			target.con = 100000000
			printb(target.name + " is blocking attacks!")
			self.endeffect = random.randint(1,2)
			
			if self.endeffect == 2:
				target.effects.remove(self)
				printb(target.name + " is no longer blocking attacks!")
				target.con = target.basecon
				
				
		if self.effect == "poison":
			damage = target.hp / 10
			target.hp -= damage
			printb(target.name + " is poisoned!   " + target.name + " takes " + str(damage) + " damage")
			self.endeffect = random.randint(1,4)
			if self.endeffect == 2:
				printb(target.name + " is no longer poisoned!")
				target.effects.remove(self)
				
		
			
		else:
			pass
				
			
burn = Effect("burn")
magicmute = Effect("magicmute")
defense = Effect("defend")
bleed = Effect("Bleed")
forceshield = Effect("forceshield")
confusion = Effect("confusion")
immortal = Effect("immortal")
block = Effect("block")
poison = Effect("poison")

		

class Skill(object):
	def __init__(self, name, type, phys, atk, var, spd, crit, cost, effects, spec):
		self.name = name
		self.type = type
		self.atk = atk
		self.var = var
		self.spd = spd
		self.phys = phys
		self.cost = cost
		self.spec = spec
		self.crit = crit
		self.effects = effects
		self.text = font.render(name, True, WHITE)
		
		
	def use(self, user, target):
		print user.power
		message = ""
		if self.phys:
			damage = (user.acbattler.str + self.atk+ random.randint(0, self.var)) - target.acbattler.con
			
		else:
			damage = (user.acbattler.int + self.atk + random.randint(0, self.var)) - target.acbattler.mag
			
		
		
		for i in target.acbattler.types:
				
			if self.type.name in i.weks:
				damage *= 2
				message = " It's super effective!"
				
		for i in target.acbattler.types:
			
				
			if self.type.name in i.strs:
				damage /= 2
				message = " It's not very effective!"
		
		
		
		if random.randint(1,30) + user.acbattler.crit >= 30:
			damage *= 2
			message += " CRITICAL HIT!"
			if not len(self.effects) == 0:
				target.acbattler.effects.append(self.effects[1])
		
		
		if not len(self.effects) == 0:
			if random.randint(1,self.effects[0]) == 1:
				target.acbattler.effects.append(self.effects[1])
				
		for i in self.spec:
		
			if i == "vampire":
				user.acbattler.hp += damage
			
			if i == "defend":
				damage = 0
				user.acbattler.effects.append(defense)
			if i == "powerup":
				damage = 0
				target.power += 10
			if i == "lifepact":
				damage = user.acbattler.hp / 2 + user.acbattler.int
				user.acbattler.hp /=2
			if i == "meditate":
				damage = 0
				user.acbattler.hp += 25
				user.power += 5
				print "hi"
			if i == "fullmana":
				damage = (user.power * user.acbattler.int) / 3
				user.power = 0
			if i == "shroud":
				user.acbattler.con += 6
				user.acbattler.mag += 6
			if i == "Shield":
				user.acbattler.effects.append(forceshield)
			if i == "atkUp":
				damage = 0
				user.acbattler.str += 25
				user.acbattler.int += 25
			
			if i == "division":
				damage = target.acbattler.hp/5
			if i == "immortal":
				user.acbattler.effects.append(immortal)
			if i == "heal":
				damage = 0
				user.acbattler.hp += user.acbattler.int * 3
			if i == "block":
				damage = 0
				user.acbattler.effects.append(block)
			if i == "powerdrain":
				damage = 0 
				user.power += target.power
				target.power = 0
			
			if i == "revenge":
				damage = user.acbattler.maxhp - user.acbattler.hp
			if i == "recover":
				damage = 0
				user.acbattler.hp += user.acbattler.maxhp / 4
				
			if i == "stare":
		
				target.acbattler.con /=2
				target.acbattler.mag /=2
			if i == "mark":
		
				target.acbattler.marks += 1
			if i == "creepyAtk":
	
				damage = math.floor(((Decimal(target.acbattler.marks) / Decimal(10)) + 1) * Decimal(damage))
			
			if i == "endeffect":
				
				user.acbattler.effects = []
		
			
			
			
		if damage < 0:
			damage = 0
		target.acbattler.hp -= damage
		printb(user.acbattler.name + " uses " + self.name + " and deals " + str(damage) + " damage!" + message)
		
		
				

basicAtk = Skill("Basic Attack", normal, True, 5, 5, 1, 0, 0, [], [""])
fireBall = Skill("Fire ball", fire, False, 7, 3, -1, 0, 2, [1, burn], [""])
waterSpout = Skill("Water Spout", water, False, 2, 10, -1, 0, 2, [], [""])
airBlast = Skill("Air Blast", air, False, 7, 1, 2, 0, 2, [], [""])
earthShot = Skill("Earth Shot", earth, False, 12, 4, -5, 0, 2, [], [""])
defend = Skill("Defend", normal, True, 0, 0, 0, 0, 0, [], ["defend"])
scar = Skill("Scar", dark, True, 30, 5, 2, 0, 1, [3,bleed], ["vampire"])
nuke = Skill("Nuke", fire, True, 35, 10, -4, 0, 20, [], [""])
shardSwarm = Skill("Shard Swarm", chaos, False, 20, 30, 4, 0, 10, [], [""])
magicMute = Skill("Magic Mute", chaos, False, 0, 0, -2, 0, 5, [1,magicmute], [""])
powerUp = Skill("Power Up", chaos, False, 0, 0, 10, 0, 2, [], ["powerup"])
magicAbsorb = Skill("Magic Absorb", chaos, False, 0, 0, 5, 0, 3, [], ["magicabsorb"])
destroy = Skill("Destroy", chaos, False, 100, 100, -100, 15, 7, [], [""])
vampire = Skill("Vampire", blood, False, 20, 10, 5, 20, 2, [], ["vampire"])
meteorStorm = Skill("Meteor Storm", astral, False, 100, 50, -100, 0, 10, [2, burn], [""])
block = Skill("Block", fighting, True, 0, 0, 10, 0, 1, [], ["block"])
powerDrain = Skill("Power Drain", astral, False, 25, 25, -10, 0, 2, [], ["powerdrain"])
#-----------------------------------------------------------

slash = Skill("Slash", normal, True, 10, 10, 3, 5, 0, [], [""])
bite = Skill("Bite", normal, True, 20, 5, 0, 0, 2, [3,bleed], [""])
kick = Skill("Kick", fighting, True, 15, 10, 4, 0, 1, [], [""])
dodge = Skill("Dodge", fighting, True, 0, 0, 10, 0, 2, [], [""])
rip = Skill("Rip", dark, True, 20, 10, -1, 0, 4, [1,bleed], [""])
consumeFlesh = Skill("Consume Flesh", blood, True, 30, 5, -5, 0, 3, [2,bleed], ["vampire"])

#----------------------------------------------------------------
chaosBolt = Skill("Chaos Bolt", chaos, False, 10, 20, 1, 0, 1, [], [""])
setFire = Skill("Set Fire", fire, False, 5, 20, -1, 0, 3, [3,burn], [""])
forceShield = Skill("Force Shield", magic, False, 0, 0, -2, 0, 2, [], ["shield"])
summon = Skill("Summon", magic, False, 0, 0, -4, 0, 4, [], [""])
chaosBeam = Skill("Chaos Beam", chaos, False, 0, 0, -10, 0, 2, [], ["fullmana"])
meditate = Skill("Meditate", magic, False, 0, 0, 0, 0, -1, [], ["meditate"])
lifePact = Skill("Life Pact", blood, False, 0, 0, -2, 0, 4, [], ["lifepact"])
shroud = Skill("Shroud", dark, False, 0, 0, 10, 0, 2, [], ["shroud"])
#-------------------------------------------------------------------
bludgeon = Skill("Bludgeon", fighting, True, 10, 2, -1, 0, 1, [], [""])
stab = Skill("Stab", fighting, True, 5, 7, 2, 0, 0, [], [""])
confuse = Skill("Confuse", physic, False, 0, 0, 10, 0, 2, [1,confusion], [""])
planAhead = Skill("Plan Ahead", tech, False, 0, 0, -10, 0, 2, [], ["atkUp"])
erase =Skill("Erase", unknown, False, 0, 0, -10, 0, 5, [], ["division"])
create = Skill("Create", unknown, False, 0,0, -10, 0, 5, [], ["immortal"])
mend = Skill("Mend", magic, False, 0,0, 1, 0, 5, [], ["heal"])
#------------------------------------------------------------------
energiBeam = Skill("Energy Beam", tech, False, 77, 10, -3, 0, 5, [], [""]) 
wellspring = Skill("Wellspring", tech, False, 0, 0, 3, 0, -10, [], [""])
#-----------------------------------------------------------------
bladeFlash = Skill("Blade Flash", fighting, True, 6, 5, 10, 2, 1, [], [""])
cleave = Skill("Cleave", fighting, True, 10, 20, -2, 2, 2, [2, bleed], [""])
revenge = Skill("Revenge", dark, False, 0, 0, 10, 0, 5, [], ["revenge"])
#----------------------------------------------------------------------
obsidianBlast = Skill("Obsidian Blast", fire, False, 20, 10, -3, 0, 5, [1, burn] ,[""])
recover = Skill("Recover", magic, False, 0, 0, 10, 0, 7, [], ["recover", "endeffect"])
psionicRadiance = Skill("Psionic Radiance", physic, False, 30, 10, -2, 3, 3, [], [""])
#------------------------------------------------------------------------
stare = Skill("Stare", physic, False, 30, 10, -2, 15, 5, [], [""])
blink = Skill("Blink", physic, True, 5, 5, 1, 0, 0, [], ["mark"])
creepyAtk = Skill("Creep Attack", physic, False, 5, 5, 1, 0, 0, [], ["creepyAtk"])
inhale = Skill("Inhale", air, False, 0, 0, 3, 0, 0, [], ["defend", "mark"])
observe = Skill("Observe", unknown, False, 0, 0, 3, 0, 1, [], ["mark", "mark", "mark", "mark", "mark", "mark"])
exhale = Skill("Exhale", air, False, 5, 10, 3, 0, 0, [], ["mark"])
#------------------------------------------------------------------------
sneeze = Skill("Sneeze", acid, False, 14, 6, 6, 0, 1, [2, poison], [""])






class Char(object):
	def __init__(self, name, types, hp, str, int, con, mag, agil, crit, lvl, xp, skills, image, cords, menuImg):
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
		self.marks = 0
		self.power = 0
		self.menuImg = menuImg
		
		
	def buildNew(self):
		newchar = Char(self.name, self.types, self.hp, self.str, self.int, self.con, self.mag, self.agil, self.crit, self.lvl, self.xp, self.skills, pygame.transform.scale(pygame.image.load(self.image), [50, 50]), self.cords, pygame.transform.scale(pygame.image.load(self.image), [42, 42]))
		newchar.img = pygame.image.load(self.image)
		return newchar
		
NOT = Char("???", [unknown], "???", "???", "???", "???", "???", "???", "???", "???", "???", [], "Assets/battlers/locked.png", [-1,0], "")

Mage = Char("Meigis", [normal, chaos], 500, 5, 15, 5, 15, 4, 0, 1, 0, [basicAtk, fireBall, waterSpout, airBlast, earthShot, defend], "Assets/battlers/Mage.png", [5,0], "")
Mouther = Char("Mouther", [earth], 500, 20, 0, 10, 5, 4, 0, 1, 0, [basicAtk, defend], "Assets/battlers/Mouther.png", [4,0], "")
NotScaryGhost = Char("Not Scary Ghost", [ghost], 1000, 0, 0, 10, 75, 2, 0, 1, 0, [basicAtk, sneeze, forceShield, recover], "Assets/battlers/Not_Scary_Ghost.png", [2, 14], "")
Creep = Char("Creepy Bald Guy", [physic, unknown], 750, 10, 10, 15, 50, 0, 0, 1, 0, [creepyAtk, blink, stare, inhale, exhale, observe], "Assets/battlers/Creepy_Bald_Guy.png", [1, 7], "")

Nic = Char("Nic", [chaos], 500, 15, 50, 10, 25, 4, 0, 1, 0, [basicAtk, magicMute, shardSwarm, powerUp, defend], "Assets/battlers/nic.png", [5,8], "")

Scarlet = Char("Scarlet", [dark, blood], 100, 20, 20, 5, 20, 6, 0, 1, 0, [basicAtk, scar, vampire, destroy, lifePact, defend], "Assets/battlers/vamp.png", [1,0], "")
Nue = Char("Nue", [astral, dark], 300, 25, 40, 10, 50, 4, 15, 1, 0, [basicAtk, meteorStorm, planAhead, forceShield, powerDrain, stab, meditate, defend], "Assets/battlers/8bitnue.png", [4,7], "")

Epic = Char("Epic", [tech], 1000, 25, 50, 35, 45, 7, 10, 1, 0, [basicAtk,energiBeam, wellspring, defend], "Assets/battlers/epic.png", [7,7], "")

Coo33 = Char("Coo33", [dark, blood], 250, 50, 0, 30, 0, 10, 10, 1, 0, [basicAtk, slash, bite, kick, dodge, rip, consumeFlesh, defend], "Assets/battlers/Coo33.png", [3,3], "")
Alpha = Char("Alpha", [normal, earth, fighting], 500, 50, -50, 30, 5, 5, 0, 1, 0, [basicAtk, slash, cleave, bladeFlash, revenge, mend, defend], "Assets/battlers/alpha.png", [8,4], "")
Siv = Char("Siv", [normal, earth, dark, physic, chaos, magic], 250, 0, 50, 0, 38, 5, 7, 1, 0, [basicAtk, chaosBolt, setFire, forceShield, chaosBeam, meditate, lifePact, shroud], "Assets/battlers/siv.png", [4,2], "")
CoosomeJoe = Char("Coosome Joe", [light, tech], 500, 25, 25, 25, 25, 5, 2, 1, 0, [basicAtk, bludgeon, erase, create, confuse, planAhead, mend, defend], "Assets/battlers/Coosome.png", [3, 7], "")
Durric = Char("Durric", [earth, light, fighting, physic], 1000, 25, 25, 75, 25, 0, 0, 1, 0, [basicAtk, forceShield, cleave, obsidianBlast, recover, psionicRadiance, mend, defend], "Assets/battlers/Durric.png", [4, 4], "")

NO = NOT.buildNew()	
		


		
unlockedchars = [Nue.buildNew(), Scarlet.buildNew(), Mage.buildNew(), Mouther.buildNew(), Nic.buildNew(), Siv.buildNew(), Coo33.buildNew(), CoosomeJoe.buildNew(), Epic.buildNew(), Alpha.buildNew(), Durric.buildNew(), Creep.buildNew(), NotScaryGhost.buildNew()]			

class Player(object):
	def __init__(self, name):
		self.acbattler = NOT.buildNew()
		self.battlers = []
		self.name = name
		self.wins = 0
		self.losses = 0
		self.goskill = "hoi"
		self.ready = False
		self.resolved = True
		self.x = 0
		self.y = 0
		self.x1 = 0
		self.y1 = 0
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

	for i in player1.acbattler.skills:
		
		if x > 1:
			x = 0
			y += 1
		
		gScreen.blit(i.text, [330+ 6 + x*175, y*30 + 370 + 5])
		if i.cost <= player1.power:
			gScreen.blit(i.type.img, [330 + x*175, y*30 + 370])
		
		else:
			gScreen.blit(lockedskill, [330 + x*175, y*30 + 370])
			
		
			
		
		
	
		x += 1	
		
		
		
	
	
	pygame.draw.rect(gScreen, GREEN, [21,371,player1.acbattler.hp * Decimal(0.278),28])
	pygame.draw.rect(gScreen, BLUE, [10, 430, player1.power * 2, 28])
	gScreen.blit(font.render("HP: " + str(player1.acbattler.hp), True, (0,0,255)), [75, 376])
	gScreen.blit(font.render("Power: " + str(player1.power), True, (255,255,255)), [75, 426])
	gScreen.blit(font.render(player1.acbattler.name + "'s turn", True, (255,255,255)), [75, 476])
	


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


def CharSelect(player):
	

while not done:
	
	thisplayer = player1
	
	
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
					thisplayer1.x1 += 1
					
					
				if event.key == K_i:
					thisplayer.y2 -= 1
					
				if event.key == K_k:
					thisplayer.y2 += 1
					
				if event.key == K_j:
					thisplayer.x2 -= 1
				
					
				if event.key == K_l:
					player1.x2 += 1
			
			
	mouse_pos = pygame.mouse.get_pos()
	y = 0
	x = 0
	for i in range(384):
		
		if x > 23:
			x = 0
			y += 1
		
		for f in unlockedchars:
			if thisplayer.x == f.cords[0] and thisplayer.y == f.cords[1]:
				
				dispchar = f
				
				thisplayer.battlers[0] = f
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
				
				thisplayer.battlers[1] = f
				break
	
			else:
				dispchar2 = NO
				player1.battlers[1] = NO

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
				
				thisplayer.battlers[2] = f
				break
				
				
			else:
				dispchar2 = NO
				thisplayer.battlers[2] = NO

		x += 1

	if hitDetect(mouse_pos, mouse_pos, [529, 434], [698, 498]):
		if mouse_down:
			thisplayer = player2
		
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
			
	gScreen.blit(selector1, [player1.x*22 + 1, player1.y*22 + 1])
	gScreen.blit(selector2, [player2.x*22 + 1, player2.y*22 + 1])
	gScreen.blit(selector3, [player2.x*22 + 1, player2.y*22 + 1])
	

	for i in range(len(thisplayer.battlers)):
	
		localbattler = thisplayer.battlers[i]
	
		gScreen.blit(dispchar2.image, [644, 370])
	
		gScreen.blit(localbattler.image, [4, i * 47 + 359])
		gScreen.blit(font.render(localbattler.name, True, BLACK), [56, i * 47 + 359])
		atypes = ""
		for f in localbattler.types:
			atypes += f.name + " "
		gScreen.blit(font.render(atypes, True, BLACK), [63, 385])
		gScreen.blit(font.render("Str: " + str(localbattler.str) + "   Con: " + str(localbattler.con) + "   Int: " + str(localbattler.int) + "   Mdf: " + str(localbattler.mag) + "   Agil: " + str(localbattler.agil) + "   Crit: " + str(localbattler.crit), True, BLACK), [63, 405])
	
	


	
	if mouse_down:
		gScreen.blit(mouse_pointer2,mouse_pos)
	else:
		gScreen.blit(mouse_pointer,mouse_pos)

	pygame.display.flip()	
	clock.tick(60)
			
	while battling:
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
	
		if player1.acbattler.hp <= 0:
			gameover = True
			pygame.mixer.music.fadeout(1000)
		#health-=0.01
	
	
	
	
		hp = font.render("hp: "+ str(player1.acbattler.hp) + "/100",True,BLUE)
	
	
	
	
	
	
	
		
				
	
	
		if player1.resolved and player2.resolved:
			player1.ready = False
			player1.turn = True
			player2.ready = False
			turn += 1
			if not player1.powergiven:
				player1.power += 1
				for i in player1.acbattler.effects:
					i.update(player1.acbattler)
				player1.powergiven = True
			
			if not player2.powergiven:
				player2.power += 1
				for i in player2.acbattler.effects:
					i.update(player2.acbattler)
				player2.powergiven = True
			
			
				
			
			
			
		if player1.turn:	
			x = 0
			y = 0
			for i in player1.acbattler.skills:
		
				if x > 1:
					x = 0
					y += 1
		
				if hitDetect(mouse_pos, mouse_pos,[330 + x*175, y*30 + 370], [330 + x*175 + 165, y*30 + 370 + 25]):
					if mouse_down:
						if True:
							if x == 0 and y ==0:
								if player1.acbattler.skills[0].cost <= player1.power:
									player1.goskill = player1.acbattler.skills[0]
								else:
									player1.goskill = basicAtk
							elif x == 1 and y == 0:
								if player1.acbattler.skills[1].cost <= player1.power:
									player1.goskill = player1.acbattler.skills[1]
								else:
									player1.goskill = basicAtk
							elif x == 0 and y == 1:
								if player1.acbattler.skills[2].cost <= player1.power:
									player1.goskill = player1.acbattler.skills[2]
								else:
									player1.goskill = basicAtk
							elif x == 1 and y == 1:
								if player1.acbattler.skills[3].cost <= player1.power:
									player1.goskill = player1.acbattler.skills[3]
								else:
									player1.goskill = basicAtk
							elif x == 0 and y == 2:
								if player1.acbattler.skills[4].cost <= player1.power:
									player1.goskill = player1.acbattler.skills[4]
								else:
									player1.goskill = basicAtk
							elif x == 1 and y == 2:
								if player1.acbattler.skills[5].cost <= player1.power:
									player1.goskill = player1.acbattler.skills[5]
								else:
									player1.goskill = basicAtk
							elif x == 0 and y == 3:
								if player1.acbattler.skills[6].cost <= player1.power:
									player1.goskill = player1.acbattler.skills[6]
								else:
									player1.goskill = basicAtk
							elif x == 1 and y == 3:
								if player1.acbattler.skills[7].cost <= player1.power:
									player1.goskill = player1.acbattler.skills[7]
								else:
									player1.goskill = basicAtk
									
									
							mouse_down = False
							player1.ready = True
							player1.resolved = False
							player1.turn = False
							print "skill picked"
					
						#except:
							#printb("Skill locked!")
					
	
		
	
				x += 1
				
		
		if player2.turn:
			for i in player2.acbattler.skills:
		
				if x > 1:
					x = 0
					y += 1
		
				if hitDetect(mouse_pos, mouse_pos,[330 + x*175, y*30 + 370], [330 + x*175 + 165, y*30 + 370 + 25]):
					if mouse_down:
						if True:
							if x == 0 and y ==0:
								if player2.acbattler.skills[0].cost <= player2.power:
									player2.goskill = player2.acbattler.skills[0]
								else:
									player2.goskill = basicAtk
							elif x == 1 and y == 0:
								if player2.acbattler.skills[1].cost <= player2.power:
									player2.goskill = player2.acbattler.skills[1]
								else:
									player2.goskill = basicAtk
							elif x == 0 and y == 1:
								if player2.acbattler.skills[2].cost <= player2.power:
									player2.goskill = player2.acbattler.skills[2]
								else:
									player2.goskill = basicAtk
							elif x == 1 and y == 1:
								if player2.acbattler.skills[3].cost <= player2.power:
									player2.goskill = player2.acbattler.skills[3]
								else:
									player2.goskill = basicAtk
							elif x == 0 and y == 2:
								if player2.acbattler.skills[4].cost <= player2.power:
									player2.goskill = player2.acbattler.skills[4]
								else:
									player2.goskill = basicAtk
							elif x == 1 and y == 2:
								if player2.acbattler.skills[5].cost <= player2.power:
									player2.goskill = player2.acbattler.skills[5]
								else:
									player2.goskill = basicAtk
							elif x == 0 and y == 3:
								if player2.acbattler.skills[6].cost <= player2.power:
									player2.goskill = player2.acbattler.skills[6]
								else:
									player2.goskill = basicAtk
							elif x == 1 and y == 3:
								if player2.acbattler.skills[7].cost <= player2.power:
									player2.goskill = player2.acbattler.skills[7]
								else:
									player2.goskill = basicAtk
									
									
							mouse_down = False
							player2.ready = True
							player2.resolved = False
							player2.turn = False
							print "skill picked"
					
						#except:
							#printb("Skill locked!")
					
	
		
	
				x += 1
			
		if not player1.turn and not player2.ready:
			player2.turn = True
	
	
	
		if not player1.resolved and not player2.resolved and player1.ready and player2.ready:
			if player1.acbattler.agil + player1.goskill.spd >= player2.acbattler.agil + player2.goskill.spd:
				player_turn = True
			else:
				player_turn = False
	
		if player1.ready and player2.ready:
			
			if player_turn:
				if player1.acbattler.hp > 0:
					player1.goskill.use(player1, player2)
					
					player1.power -= player1.goskill.cost
					player1.resolved = True
					player1.powergiven = False
				
			
	
			if not player_turn:
				if player2.acbattler.hp > 0:
					player2.goskill.use(player2, player1)
					player2.power -= player2.goskill.cost
					player2.resolved = True
					player2.powergiven = False
				
			
			
	
		if player1.resolved:
			player_turn = False
		if player2.resolved:
			player_turn = True
	
		
		
		if player1.power > 100:
			player1.power = 100
		if player2.power > 100:
			player2.power = 100
		
    # --- Drawing code should go here
	
 
    
	
	#player
	#animation:
	
	
		gScreen.fill(WHITE)
		
		pygame.draw.rect(gScreen, RED, [50,125,player1.acbattler.hp / 20,5])
		gScreen.blit(player1.acbattler.image,[50, 150])
		
		pygame.draw.rect(gScreen, RED, [600,125,player2.acbattler.hp / 20,5])
		gScreen.blit(player2.acbattler.image,[600, 150])
	
		
		pygame.draw.rect(gScreen, BLACK, [0,350,700,150])
		#pygame.draw.rect(gScreen, WHITE, [10,360,300,50])
		gScreen.blit(disptext, [10, 320])
		hasprinted = True
		gScreen.blit(health_border, [10, 360])
		
		pygame.draw.rect(gScreen, GREY, [320, 360, 370, 130])
		

	
	
		x = 0
		y = 0

			
		if player1.turn:
			
			dispSkills(player1)
		elif player2.turn:
			dispSkills(player2)
	
		if mouse_down:
			gScreen.blit(mouse_pointer2,mouse_pos)
		else:
			gScreen.blit(mouse_pointer,mouse_pos)
		if player1.acbattler.hp <= 0:
			
			battling = False
			print player2.acbattler.name + " WON!"
			print log
			player1.acbattler.hp = player1.acbattler.maxhp
			player1.acbattler.effects = []
			player2.acbattler.hp = player2.acbattler.maxhp
			player2.acbattler.effects = []
			player2.power = 0
			player1.power = 0
			
			log = []
		elif player2.acbattler.hp <= 0:
			battling = False
			print player1.acbattler.name + " WON!"
			print log
			player1.acbattler.hp = player1.acbattler.maxhp
			player1.acbattler.effects = []
			player2.acbattler.hp = player2.acbattler.maxhp
			player2.acbattler.effects = []
			player2.power = 0
			player1.power = 0
			
			log = []
		
		if player1.ready and player2.ready:
			pygame.draw.rect(gScreen, BLACK, [0,350,700,150])
	
 
		# --- Go ahead and update the screen with what we've drawn.
		pygame.display.flip()
 
		# --- Limit to 60 frames per second
		clock.tick(60)
		
		
		
		
	