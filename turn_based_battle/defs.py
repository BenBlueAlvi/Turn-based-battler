import pygame
import time
import random
import math


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0,0,255)
GREY = (100,100,100)

pygame.init()
font = pygame.font.SysFont('Calibri', 15, True, False)

def bubble_sort(items):
	""" Implementation of bubble sort """
	for i in range(len(items)):
		for j in range(len(items)-1-i):
			if items[j] > items[j+1]:
				items[j], items[j+1] = items[j+1], items[j] 
log =[]				
timer = 0
printing = False			
def printb(text):
	global disptext
	global printing
	global log
	global timer
	
	newtext = font.render(text,True,BLACK)
	log.append(newtext)

	if not printing:
		disptext = newtext
		timer = 90
				

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


				
class Effect(object):
	def __init__(self, effect):
		self.effect = effect
		self.endeffect = 0
		self.img = pygame.image.load("Assets/ui/" + effect + ".png")
		self.canend = True
		self.damage =0
	def update(self, target):
		if self.effect == "burn":
			self.damage = 25 + random.randint(1, 25)
			self.endeffect = random.randint(1,3)
			

			

			target.hp -= self.damage
			printb(target.name + " is on fire!   " + target.name + " takes " + str(self.damage) + " damage")
		
			
			if self.endeffect == 2 and self.canend:
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
				
		if self.effect == "guarded":
			printb(target.name + " is being guarded by " + target.guarder.name + "!")
			if self.endeffect == 1:
				printb(target.name + " is no longer being guarded by " + target.guarder.name + "!")
				target.guarder = "nul"
				target.effects.remove(self)
				self.resetStats(target)
			self.endeffect += 1	
			
		if self.effect == "neverThere":
			printb(target.name + " dissapeared")
			target.dodgeChance += 100
			self.endeffect = random.randint(1,3)
			if self.endeffect == 1:
				printb(target.name + " reapeared!")
				
				target.effects.remove(self)
				self.resetStats(target)
			
		
		
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
guarded = Effect("guarded")

neverTheref = Effect("neverThere")

negeff = [burn, magicmute, bleed, poison, confusion]
poseff = [defense, forceshield, immortal, block, rebuff, meditatef, planAheadf, dodgeUp, earthStagef, otherStagef, moonStagef]


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
		
		if guarded in target.effects:
			target = target.guarder

		if target.ability == "Cuteness":
			hit -= 25
		if user.ability == "Blood hunt":
			hit += 25
		if user.ability == "Frenzy" and user.hp <= user.maxhp/5:
			hit += 2

		if random.randint(1,100) < hit or "trueHit" in self.spec:
			critical, effective = False, False

			if self.phys:
				damage = (user.str + self.atk+ random.randint(0, self.var)) - target.con
			else:
				damage = (user.int + self.atk + random.randint(0, self.var)) - target.mag
				
			for i in target.types:
				if self.type.name in i.weks:
					message = " It's super effective!"
					effective = True
			for i in target.types:
				if self.type.name in i.strs:
					damage /= 2
					message = " It's not very effective!"
					effective = False
					
			if random.randint(1,30) + user.crit >= 30:
				if effective:
					message += " CRITICAL HIT!"
				critical = True
				if not len(self.effects) == 0:
					target.effects.append(self.effects[1])
					
			if not len(self.effects) == 0:
				if random.randint(1,self.effects[0]) == 1:
					target.effects.append(self.effects[1])
					
			if target.ability == "Creepus":
				user.marks += 1
				if critical:
					user.marks += 1
				
			for i in self.spec:
				if i == "vampire":
					user.hp += damage
					if critical:
						user.hp += math.floor(damage/10)
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
					if critical:
						target.hp += user.int
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
					if critical:
						target.hp += math.floor(heal/5)
				if i == "stare":
					target.con /=2
					target.mag /=2
				if i == "mark":
					target.marks += 1
					if critical:
						target.marks += 1
				if i == "creepyAtk":
					damage = math.floor((user.int * (1.08 ** target.marks))/target.mag)
				if i == "endeffect":
					user.effects = []
				if i == "removeEff":
					for j in negeff:
						if j in target.effects:
							target.effects.remove(j)
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
					if critical:
						target.hp += math.floor(user.hp/5)
				if i == "powerTransfer":
					user.power -= user.power
					target.power += user.power
					if critical:
						target.power += 1
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
				if i == "againstOdds":
					if user in player1.battlers:
						for b in player2.battlers:
							
							damage += b.hp / 10
						for c in player1.battlers:
							damage += (c.maxhp - c.hp) / 6
					if user in player2.battlers:
						for b in player1.battlers:
							damage += b.hp / 10
						for c in player2.battlers:
							damage += (c.maxhp - c.hp) / 6
					damage += target.hp / 6
					damage = math.floor(damage) - target.con
				if i == "takeBlow":
					target.guarder = user
					target.effects.append(guarded)
				if i == "mindReading":
					user.dodgeChance += 5
					if critical:
						user.dodgeChance += 1

				if i == "neverThere":
					user.effects.append(neverTheref)


			if user.ability == "Frenzy" and user.hp <= user.maxhp/5:
				damage *= 1.25
						
			if user.hp > 0:
				if target.ability == "3 worlds":
					damage /= 3
				
				if effective:
					damage *= 2
				if critical:
					damage *= 2
				if damage < 0 or "nodam" in self.spec:
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
meteorStorm = Skill("Meteor Storm", astral, False, 100, 50, -100, 0,75, 7, [2, burn], [""])
block = Skill("Block", fighting, True, 0, 0, 10, 0,100, 1, [], ["block", "trueHit"])
powerDrain = Skill("Power Drain", astral, False, 25, 25, -10, 0,100, 2, [], ["powerdrain", "trueHit"])
#-----------------------------------------------------------
slash = Skill("Slash", normal, True, 11, 10, 3, 5,90, 0, [], [""])
bite = Skill("Bite", normal, True, 10, 5, 0, 5, 92, 0, [4,bleed], [""])
kick = Skill("Kick", fighting, True, 20, 5, 4, 0, 70, 1, [], [""])
dodge = Skill("Dodge", fighting, True, 0, 0, 10, 10, 100, 2, [], ["trueHit", "dodgeUp"])
rip = Skill("Rip", dark, True, 20, 15, -1, 0,90, 3, [1,bleed], [""])
consumeFlesh = Skill("Consume Flesh", blood, True, 30, 8, -5, 0,90, 3, [2,bleed], ["vampire"])
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
inhale = Skill("Inhale", air, False, 0, 0, 3, 0,100, 0, [], ["defend", "heal", "trueHit"])
observe = Skill("Observe", unknown, False, 0, 0, 3, 2, 100, 1, [], ["mark", "mark", "mark", "mark", "mark", "mark", "nodam", "trueHit"])
exhale = Skill("Exhale", air, False, 5, 10, 3, 0,90, 0, [], ["mark", "hitAll"])
#------------------------------------------------------------------------
sneeze = Skill("Sneeze", acid, False, 14, 6, 6, 0,90, 1, [2, poison], [""])

eggon = Skill("Egg On", normal, True, 0, 0, 10, 10, 100, 2, [1, rebuff], ["trueHit", "nodam"])
rebuke = Skill("Rebuke", normal, True, 0, 0, 10, 2, 100, 1, [], ["removeEff", "removeUff", "trueHit"])

blast = Skill("Blast", tech, False, 20, 20, 5, 8, 95, 2, [2, burn], [""])
fission = Skill("Fission", fire, False, 20, 40, -1, 0, 90, 0, [2, burn], ["powerDown", "fullmana"])
fusion = Skill("Fusion", fire, False, 1, 40, -1, 0, 100, 1, [2,burn], ["powerUp"])

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

againstOdds = Skill("Against The Odds", light, True, 0, 10, 3, 13, 90, 7, [], ["againstOdds"])
takeBlow = Skill("Take The Blow", fighting, True, 0, 0, 12, 10, 100, 1, [], ["takeBlow", "trueHit", "nodam"])
powerStrike = Skill("Power Strike", fighting, True, 75, 10, -1, 0, 40, 1, [], [""])
antiPhysic = Skill("Anti Physic", unknown, False, 30, 20, 5, 15, 90, 2, [], [""])
mindReading = Skill("Mind Reading", physic, False, 20, 20, 5, 2, 100, 1, [], ["mindReading"])
neverThere = Skill("Never There", physic, False, 0,0, 20, 0, 100, 2, [], ["trueHit", "neverThere"])
colorfulBullet = Skill("colorfulBullet", magic, False, 10,5, 1, 2, 90, 0, [], [""])




class Char(object):
	def __init__(self, name, types, hp, str, int, con, mag, agil, crit, dodgeChance, lvl, xp, skills, ability, image, cords, menuImg):
		self.name = name
		self.hp = hp
		self.maxhp = hp
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
		self.goskill = nothing
		self.target = ["bob"]
		self.updated = False
		self.x = 0
		self.y = 0
		self.basey = 0
		self.basex = 0
		self.ym = 1
		self.guarder = "hi"
		#AI stuff
		self.savingfor = "none"
		self.nextattack = ""
		
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

Nic = Char("Nic", [chaos], 500, 15, 50, 10, 25, 4, 0, 10, 1, 0, [basicAtk, magicMute, shardSwarm, powerUp, defend], "", "Assets/battlers/nic.png", [5,8], "")
Epic = Char("Epic", [tech], 1000, 25, 50, 35, 45, 7, 10, 10, 1, 0, [basicAtk,energiBeam, wellspring, defend], "", "Assets/battlers/epic.png", [7,8], "")

Scarlet = Char("Scarlet", [dark, blood], 100, 20, 20, 5, 20, 6, 0, 10, 1, 0, [basicAtk, scar, vampire, destroy, lifePact, defend], "", "Assets/battlers/vamp.png", [1,0], "")

Flan = Char("Flan", [dark,blood], 200, 35, 30, 10, 20, 7, 10, 20, 1, 0, [slash, rip, scar, vampire, destroy, lifePact, setFire, lifeTransfer], "watch them burn", "Assets/battlers/flandre.png", [5,7], "")
Nue = Char("Nue", [astral, dark], 300, 25, 40, 10, 50, 4, 15, 10, 1, 0, [basicAtk, meteorStorm, powerTransfer, forceShield, powerDrain, stab, meditate, defend], "Unidentifiable", "Assets/battlers/nue.png", [4,7], "")
Okuu = Char("Okuu", [fire, tech], 500, 15, 50, 30, 10, 1, 5, 5, 1, 0, [bludgeon, blast, fusion, fission, nuke, forceShield, recover], "Radiation", "Assets/battlers/reiji.png", [3,7], "")
Lapis = Char("Lapis", [astral], 400, 20, 20, 10, 10, 4, 5, 20, 1, 0, [chains, voidSnap, earthStage, moonStage, otherStage, earthenVortex, chaosVortex, astralVortex], "3 worlds", "Assets/battlers/lapis.png", [6,7], "")

Koishi = Char("Koishi", [unknown], 400, 10, 55, 20, 75, 10, 6, 30, 1, 0, [colorfulBullet,mindReading, antiPhysic, neverThere, erase, mend, voidSnap], "", "Assets/battlers/komeiji.png", [7,7], "")

Alpha = Char("Alpha", [normal, earth, fighting], 500, 50, -50, 30, 5, 5, 0, 10, 1, 0, [basicAtk, slash, cleave, bladeFlash, revenge, mend, defend], "", "Assets/battlers/alpha.png", [8,4], "")
Siv = Char("Siv", [normal, earth, dark, physic, chaos, magic], 250, 0, 50, 0, 38, 5, 7, 10, 1, 0, [basicAtk, chaosBolt, setFire, forceShield, chaosBeam, meditate, lifePact, shroud], "", "Assets/battlers/siv.png", [4,2], "")

Durric = Char("Durric", [earth, light, fighting, physic], 1000, 25, 25, 75, 25, 0, 0, 1, 1, 0, [basicAtk, forceShield, cleave, obsidianBlast, recover, psionicRadiance, mend, takeBlow], "Regen", "Assets/battlers/Durric.png", [4, 4], "")

Coo33 = Char("Coo33", [dark, blood], 250, 50, 0, 30, 0, 10, 10, 10, 5, 0, [basicAtk, slash, bite, kick, dodge, rip, consumeFlesh, defend], "Blood hunt", "Assets/battlers/Coo33.png", [3,3], "")
CoosomeJoe = Char("Coosome Joe", [light, tech], 500, 25, 25, 25, 25, 5, 2, 10, 1, 0, [basicAtk, bludgeon, erase, create, confuse, planAhead, mend, defend], "Frenzy", "Assets/battlers/Coosome.png",  [3, 4], "")
Catsome = Char("Catsome", [light, ghost, physic], 1000, 10, 35, 10, 15, 5, 5, 10, 1, 0, [slash, bite, eggon, rebuke, mend, recover], "Cuteness", "Assets/battlers/catsome.png",[6,9], "")

Creep = Char("Creepy Bald Guy", [physic, unknown], 750, 10, 10, 15, 50, 0, 0, 0, 1, 0, [creepyAtk, blink, stare, inhale, exhale, observe], "Creepus", "Assets/battlers/Creepy_Bald_Guy.png", [3, 15], "")
KnowingEye = Char("Knowing Eye", [physic, unknown, astral], 750, 0, 75, 0, 75, 5, 6, 5, 1, 0, [creepyAtk, observe, meditate, magicMute, forceShield, create], "Creepus", "Assets/battlers/wip.png", [4, 15], "")

Protagonist = Char("Protagonist", [normal], 750, 15, 15, 20, 10, 2, 6, 5, 1, 0, [basicAtk, powerStrike, meditate, planAhead, eggon, takeBlow, mend, againstOdds], "Frenzy", "Assets/battlers/wip.png", [1,1], "")

NO = NOT.buildNew()	