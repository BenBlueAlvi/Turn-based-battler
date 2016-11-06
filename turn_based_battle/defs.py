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
size = (1250, 700)
gScreen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
class Music(object):
	def __init__(self, musicc):
		self.musicc = "Assets/music/"+musicc+".ogg"
		self.playing = True
		
	def play(self):
		if self.playing:
			pygame.mixer.music.stop()
			pygame.mixer.music.load(self.musicc)
			pygame.mixer.music.play(-1, 0.0)
			#pygame.mixer.music.set_endevent(intodone)
		self.playing = False
	def reset(self):
		self.playing = True
	def stop(self):
		pygame.mixer.music.stop()
	def fadeout(self, time):
		pygame.mixer.music.fadeout(time)
		
		
cattheme = Music("Raxxo_Patchy_Aid")
cootheme = Music("Raxxo_Stand_Your_Ground")
maicetheme = Music("A_Tiny_Tiny_Clever_Commander")
sivtheme = Music("WaterflameFinalBattle")
noutheme = Music("supierior_nouledge")
maptheme = Music("Raxxo_Bent_to_the_Core")
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

	
	newtext = font.render(text,True,WHITE)
	log.append(text)

	
	disptext = newtext
	timer = 90
	for i in range(timer):
		
					
				
	
		pygame.draw.rect(gScreen, BLACK, [0,size[1] - 150,size[0],150])
		#gScreen.blit(disptext, [10, 320 + size[1] - 500])
		gScreen.blit(disptext, [10, size[1] - 140])
		printing = True
		
		#pygame.draw.rect(gScreen, WHITE, [0,350 + size[1] - 500,700,150])
		#pygame.draw.rect(gScreen, BLACK, [0 + size[0] - 200,size[1] - 500,700,150])
		
		
			
		pygame.display.flip()	
		clock.tick(60)
	
						

def printc(text, battler, thesebattlers):
	global disptextc
	global printingc
	global logc
	global timerc
	
	newtextc = font.render(text,True,BLACK)
	logc.append(newtextc)

	
	disptextc = newtextc
	timerc = 90
	for i in range(timerc):
		gScreen.blit(disptextc, [thesebattlers[battler].x, thesebattlers[battler].y + 10])
		


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
minion = Type("Minion", ["none"], ["none"])

				
class Effect(object):
	def __init__(self, effect):
		self.effect = effect
		self.endeffect = 0
		self.img = pygame.image.load("Assets/ui/effects/" + effect + ".png")
		self.canend = True
		self.damage = 0
		
	def apply(self, target):
		if self.effect == "defend":
			target.con += target.basecon * target.basecon
			printb(target.name + " is defending!")
			target.effects.append(self.buildNew())
			
		if self.effect == "forceshield":
			target.con += target.basecon * 3
			target.mag += target.basemag * 3
			printb(target.name + " has a shield up!")
			target.effects.append(self.buildNew())
			
		if self.effect == "confusion":
			target.con -= target.basecon / 2
			target.mag -= target.basemag / 2
			printb(target.name + " is confused!")
			target.effects.append(self.buildNew())
			
		if self.effect == "rebuff":
			target.str += target.basestr * 1.4
			target.int += target.baseint * 1.4
			printb(target.name + " is encouraged!")
			target.effects.append(self.buildNew())
			
		if self.effect == "meditate":
			target.power += 3
			target.con -= 10
			target.mag += 5
			printb(target.name + " is meditating!")
			target.effects.append(self.buildNew())
			
		if self.effect == "planAhead":
			planned = False
			for i in target.effects:
				if i.effect == "planAhead":
					i.endeffect, planned = 0, True
			if not planned:
				target.effects.append(self.buildNew())
				printb(target.name + " is scheming!")
			else:
				printb(target.name+" is perfecting their plans!")
			target.misc += 1
			print "planned: ", target.misc
			target.crit += 2
			target.int = target.int + (target.int / 20)
			target.str = target.str + (target.str / 20)
			
		if self.effect == "dodgeUp":
			target.dodgeChance += 25
			printb(target.name + " is prepared!")
			target.effects.append(self.buildNew())
			
		if self.effect == "neverThere":
			target.dodgeChance += 100
			printb(target.name + " dissapeared")
			target.effects.append(self.buildNew())
			
		if self.effect == "slowed":
			target.agil -= 5
			target.dodgeChance -= 10
			printb(target.name + " is slowed!")
			target.effects.append(self.buildNew())
			
		if self.effect == "magicMute":
			printb(target.name+" is Muted!")
			target.effects.append(self.buildNew())
		if self.effect == "passedOut":
			printb(target.name+" passed out!")
			target.effects.append(self.buildNew())
		if self.effect == "mindSpiked":
			printb(target.name+" has been mind spiked!")
			target.effects.append(self.buildNew())
			
	def end(self, target):
		target.effects.remove(self)
		
		if self.effect == "defend":
			printb(target.name + " is no longer defending!")
			target.con -= target.basecon * target.basecon
			
		if self.effect == "forceshield":
			target.con -= target.basecon * 3
			target.mag -= target.basemag * 3
			printb(target.name + " no longer has a shield up!")
		
		if self.effect == "confusion":
			target.con += target.basecon / 2
			target.mag += target.basemag / 2
			printb(target.name + " is no longer confused!")
		
		if self.effect == "rebuff":
			target.str -= target.basestr * 1.4
			target.int -= target.baseint * 1.4
			printb(target.name + " is no longer encouraged. :(")
		
		if self.effect == "meditate":
			target.con += 10
			target.mag -= 5
			printb(target.name + " is no longer meditating!")
		
		if self.effect == "planAhead":
			for i in range(target.misc):
				target.crit = target.crit - 2
				target.int = target.int - (target.int / 20)
				target.str = target.str - (target.str / 20)
			target.misc = 0
			printb(target.name + " is no longer scheming!")
		
		if self.effect == "dodgeUp":
			target.dodgeChance -= 25
			printb(target.name + " is no longer prepared!")
		
		if self.effect == "neverThere":
			target.dodgeChance -= 100
			printb(target.name + " reapeared!")
			
		if self.effect == "slowed":
			target.agil -= 5
			target.dodgeChance -= 10
			printb(target.name + " is no longer slowed!")
		if self.effect == "passedOut":
			printb(target.name + " is no longer passed out!")
		if self.effect == "mindSpiked":
			printb(target.name + " is no longer mind spiked!")
		
		
	def update(self, target):
		if self.effect == "magicMute":
			target.power -= 1
			printb(target.name+"'s power was Muted!")
			if self.endeffect == 1:
				self.end(target)
			self.endeffect += 1
		
		if self.effect == "burn":
			self.damage = 25 + random.randint(1, 25)
			self.endeffect = random.randint(1,3)
			target.hp -= self.damage
			printb(target.name + " is on fire!   " + target.name + " takes " + str(self.damage) + " damage")
			if self.endeffect == 2 and self.canend:
				printb(target.name + " put out the fire!")
				self.end(target)
				
		if self.effect == "bleed":
			target.hp -= target.hp / 4
			printb(target.name + " is on bleeding out!")
			self.endeffect = random.randint(1,3)
			if self.endeffect == 2:
				printb(target.name + " is no longer bleeding")
				self.end(target)

		if self.effect == "defend":
			self.endeffect += 1
			if self.endeffect == 2:
				self.end(target)
				
		if self.effect == "forceshield":
			self.endeffect = random.randint(1,2)
			if self.endeffect == 2:
				self.end(target)
				
		if self.effect == "confusion":
			self.endeffect = random.randint(1,2)
			if self.endeffect == 2:
				self.end(target)
				
		if self.effect == "poison":
			damage = target.hp / 10
			target.hp -= damage
			printb(target.name + " is poisoned!   " + target.name + " takes " + str(damage) + " damage")
			self.endeffect = random.randint(1,4)
			if self.endeffect == 2:
				printb(target.name + " is no longer poisoned!")
				self.end(target)
				
		if self.effect == "rebuff":
			if self.endeffect >= 1:
				self.end(target)
			self.endeffect += 1
			
		if self.effect == "meditate":
			if magicMute in target.effects:
				printb(target.name + "'s Meditate was Muted!")
			else:
				printb(target.name + " is Meditating.")
				target.power += 3
			if self.endeffect == 1:
				self.end(target)
			self.endeffect += 1
				
		if self.effect == "planAhead":
			if self.endeffect == 1:
				self.end(target)
			self.endeffect += 1
		
		if self.effect == "dodgeUp":
			
			if self.endeffect == 1:
				self.end(target)
			self.endeffect += 1
			
		if self.effect == "earthStage":
			self.resetStats(target)
			target.con += 50
			target.mag += 50
			target.int -= 20
			target.str -= 20
			try:
				moonStagef.end(target)
			except:
				pass
			try:
				otherStagef.end(target)
			except:
				pass
				
		if self.effect == "moonStage":
			self.resetStats(target)
			target.mag += 50
			target.int += 50
			target.str -= 25
			target.con -= 25
			try:
				earthStagef.end(target)
			except:
				pass
			try:
				otherStagef.end(target)
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
				moonStagef.end(target)
			except:
				pass
			try:
				earthStagef.end(target)
			except:
				pass
				
		if self.effect == "guarded":
			printb(target.name + " is being guarded by " + target.guarder.name + "!")
			if self.endeffect == 1:
				printb(target.name + " is no longer being guarded by " + target.guarder.name + "!")
				target.guarder = "nul"
				self.end(target)
			self.endeffect += 1	
			
		if self.effect == "neverThere":
			self.endeffect = random.randint(1,3)
			if self.endeffect == 1:
				self.end(target)

		if self.effect == "slowed":
			self.endeffect = random.randint(1,3)
			if self.endeffect == 1:
				self.end(target)
				
		if self.effect == "passedOut":
			self.endeffect = random.randint(1,2)
			if self.endeffect == 1:
				self.end(target)
		if self.effect == "mindSpike":
			self.endeffect = random.randint(1,3)
			if self.endeffect == 1:
				self.end(target)
		
		if self.effect == "death":
			pass
			#Death stufff here

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
passedOut = Effect("passedOut")
neverTheref = Effect("neverThere")
slowed = Effect("slowed")
mindSpiked = Effect("mindSpiked")

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
		self.desc = ""
		
		
	def use(self, user, target, battlers1, battlers2, thesebattlers):
		
		message = ""
		hit = self.hitChance - (target.dodgeChance + target.equipDodgeChance)
		
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
				damage = (user.str + user.equipStr + self.atk+ random.randint(0, self.var)) - (target.con + target.equipCon)
			else:
				damage = (user.int + user.equipInt + self.atk + random.randint(0, self.var)) - (target.mag + target.equipMag)
				
			for i in target.types:
				if self.type.name in i.weks:
					message = " It's super effective!"
					effective = True
			for i in target.types:
				if self.type.name in i.strs:
					damage /= 2
					message = " It's not very effective!"
					effective = False
					
			if random.randint(1,30) + user.crit + user.equipCrit > 30:
				if effective:
					message += " CRITICAL HIT!"
				else:
					message = "CRITICAL HIT!"
				critical = True
				if not len(self.effects) == 0:
					self.effects[1].apply(target)
					
			if not len(self.effects) == 0:
				if random.randint(1,self.effects[0]) == 1:
					self.effects[1].apply(target)
					
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
					defense.apply(user)
				if i == "powerUp":
					damage = 0
					if magicMute in user.effects:
						printb(user.name+"'s power was Muted!")
					else:
						user.power += 2
				if i == "lifepact":
					damage = user.hp / 2 + user.int
					user.hp /=2
				if i == "fullmana":
					damage = ((user.power * (user.int + self.atk)) / 8)
					user.power = 0
				if i == "shroud":
					user.con += 6
					user.mag += 6
				if i == "Shield":
					forceshield.apply(user)
				if i == "atkUp":
					damage = 0
					planAheadf.apply(user)
				if i == "division":
					damage = target.hp/5
				if i == "immortal":
					immortal.apply(user)
				if i == "heal":
					damage = 0
					target.hp += 100
					if target.ability == "3 worlds":
						target.hp -= user.int * 2
					if critical:
						target.hp += user.int
				if i == "block":
					damage = 0
					block.apply(user)
				if i == "powerdrain":
					damage = 0
					if magicMute in user.effects:
						printb(user.name+"'s Power drain was Muted!")
						user.power += math.floor(target.power/5)
					else:
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
					temp = target.mag
					if temp <= 0:
						temp = (-1)/(-1 + temp)
						print "Detected devision by 0. Modding to: "+str(temp)
					damage = math.floor((user.int * (1.08 ** target.marks))/target.mag)
				if i == "endeffect":
					user.effects = []
				if i == "removeEff":
					for j in negeff:
						if j in target.effects:
							j.end(target)
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
					transfered = 0
					if critical:
						transfered += 1
					if magicMute in target.effects:
						printb(user.name+"'s Transfer was Muted!")
						transfered = math.floor(transfered/5)
					target.power += transfered
					user.power -= user.power
					printb(user.name + " transfered "+str(transfered)+" power to "+target.name)
				if i == "meditate":
					meditatef.apply(user)
				if i == "dodgeUp":
					dodgeUp.apply(user)
				if i == "otherStage":
					otherStagef.apply(user)
				if i == "earthStage":
					earthStagef.apply(user)
				if i == "moonStage":
					moonStagef.apply(user)
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
					guarded.apply(target)
				if i == "mindReading":
					user.dodgeChance += 5
					if critical:
						user.dodgeChance += 1

				if i == "neverThere":
					neverTheref.apply(user)
				
				if i == "createCreep":
					spawned = miniCreep.buildNew()
					if user in battlers1 and len(battlers1) < 3:
						battlers1.append(spawned)
						thesebattlers.append(spawned)
					elif user in battlers2 and len(battlers2) < 3:
						spawned.isAi = True
						battlers2.append(spawned)
						thesebattlers.append(spawned)
					
					else:
						pass
					x = 0
					y = 0
					for i in thesebattlers:
						if y > 2:
							y = 0
							x += 1
						i.basex = x * (size[0] - 150) + 50
						i.basey = y * 75 + 325
						y += 1
				
				if i == "createWorship":
					spawned = Worshipper.buildNew()
					if user in battlers1 and len(battlers1) < 3:
						battlers1.append(spawned)
						thesebattlers.append(spawned)
					elif user in battlers2 and len(battlers2) < 3:
						spawned.isAi = True
						battlers2.append(spawned)
						thesebattlers.append(spawned)
					else:
						pass
					x = 0
					y = 0
					for i in thesebattlers:
						if y > 2:
							y = 0
							x += 1
						i.basex = x * (size[0] - 150) + 50
						i.basey = y * 75 + 325
						y += 1

				if i == "createCubes":
					spawned = Cubes.buildNew()
					if user in battlers1 and len(battlers1) < 3:
						battlers1.append(spawned)
						thesebattlers.append(spawned)
					elif user in battlers2 and len(battlers2) < 3:
						spawned.isAi = True
						battlers2.append(spawned)
						thesebattlers.append(spawned)
					
					else:
						pass
					x = 0
					y = 0
					for i in thesebattlers:
						if y > 2:
							y = 0
							x += 1
						i.basex = x * (size[0] - 150) + 50
						i.basey = y * 75 + 325
						y += 1
				if i == "mindSpike":
					mindSpiked.apply(target)


			if user.ability == "Frenzy" and user.hp <= user.maxhp/5:
				damage = math.floor(damage * 1.25)
						
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
				
				if mindSpiked in user.effects:
					printb(user.name + " is mind spiked!")
					printb("The mind spike dealt " + str(damage) + " back to " + user.name)
					user.hp -= damage
					
				target.hp -= damage
				
		else:
			damage = 0
			printb(user.name + " missed!")
				
#Skill("", normal, True, 0, 0, 0, 0, 100, 0, [], [""])


nothing = Skill("nothing", normal, True, 0, 0, 0, 0, 100, 0, [], ["nodam", "trueHit"])
nothing.desc = ""
basicAtk = Skill("Basic Attack", normal, True, 5, 5, 1, 0,90, 0, [], [""])
basicAtk.desc = "A basic attack, like using a weapon or claws."
fireBall = Skill("Fire ball", fire, False, 7, 3, -1, 0,90, 2, [1, burn], [""])
fireBall.desc = "Summons a small fireball, chance to cause burn."
waterSpout = Skill("Water Spout", water, False, 2, 10, -1, 0,90, 2, [], [""])
waterSpout.desc = "Creates a fountain of water."
airBlast = Skill("Air Blast", air, False, 7, 1, 2, 0,95, 2, [], [""])
airBlast.desc = "A strong blast of air pushes foes away"
earthShot = Skill("Earth Shot", earth, False, 12, 4, -5, 0,90, 2, [], [""])
earthShot.desc = "Magical rock throwing."
axeLegs = Skill("Axe Legs", fighting, True, 65, 25, 7, 2, 99, 0, [], [""])
axeLegs.desc = "Strong axe blades click into place before spinning rapidly, quickly removing your foe's limbs."
defend = Skill("Defend", normal, True, 0, 0, 0, 0,100, 0, [], ["defend", "trueHit"])
defend.desc = "Brace yourself against incomming physical damage."
scar = Skill("Scar", dark, True, 30, 5, 2, 0,97, 1, [3,bleed], ["vampire"])
scar.desc = "Mangle your foe's flesh and steal a bit of their life, can cause horrible bleeding."
nuke = Skill("Nuke", fire, True, 200, 100, -4, 0,100, 20, [], ["trueHit", "hitAll"])
nuke.desc = "Drops a nuke on all foes, dealing heavy damage."
shardSwarm = Skill("Shard Swarm", chaos, False, 20, 30, 4, 0,90, 10, [], [""])
shardSwarm.desc = "Summons a swarm of sharp energy shards to slice up your foes."
magicMute = Skill("Magic Mute", chaos, False, 0, 0, -2, 0,100, 5, [1,magicmute], ["trueHit"])
magicMute.desc = "Prevents opponents from gaining power."
powerUp = Skill("Power Up", chaos, False, 0, 0, 10, 0,100, 2, [], ["powerup", "trueHit"])
powerUp.desc = "Builds power by absorbing choatic energy."

destroy = Skill("Destroy", chaos, False, 100, 100, -100, 15,100, 7, [], [""])
destroy.desc = "Destroys absolutely everything, but takes a long time to cast."
vampire = Skill("Vampire", blood, False, 20, 10, 5, 20,90, 2, [], ["vampire", "vampire"])
vampire.desc = "Drains the blood of your foes to heal yourself."
meteorStorm = Skill("Meteor Storm", astral, False, 100, 50, -100, 0,75, 7, [2, burn], [""])
meteorStorm.desc = "Calls down a meteor storm to crush opponents, can cause burns."
block = Skill("Block", fighting, True, 0, 0, 10, 0,100, 1, [], ["block", "trueHit"])
block.desc = "Prevents incomming physical damage."
powerDrain = Skill("Power Drain", astral, False, 25, 25, -10, 0,100, 2, [], ["powerdrain", "trueHit"])
powerDrain.desc = "Drains power from opponents to use for yourself."
#-----------------------------------------------------------
tangle = Skill("Tangle", grass, True, 4, 5, 0, 7, 100, 1, [1, slowed], [""])
tangle.desc = "Tangles foes within a strong vine."
#-----------------------------------------------------------
slash = Skill("Slash", normal, True, 11, 10, 3, 5,90, 0, [], [""])
slash.desc = "Splice up foes with a sword or claw."
bite = Skill("Bite", normal, True, 10, 5, 0, 5, 92, 0, [4,bleed], [""])
bite.desc = "Take a large bite out of your foe, has a chance of causeing bleeding."
kick = Skill("Kick", fighting, True, 20, 5, 4, 0, 70, 1, [], [""])
kick.desc = "Kick your foes in the face!"
dodge = Skill("Dodge", fighting, True, 0, 0, 10, 10, 100, 2, [], ["trueHit", "dodgeUp"])
dodge.desc = "Prepare yourself to dodge the next attack."
rip = Skill("Rip", dark, True, 20, 15, -1, 0,90, 3, [1,bleed], [""])
rip.desc = "Rip your foes to shreds and cause heavy bleeding"
consumeFlesh = Skill("Consume Flesh", blood, True, 30, 8, -5, 0,90, 3, [2,bleed], ["vampire"])
consumeFlesh.desc = "Eat some of the foe's flesh that you ripped off. Has a chance to cause bleeding."
#----------------------------------------------------------------
chaosBolt = Skill("Chaos Bolt", chaos, False, 10, 20, 1, 0,90, 1, [], [""])
chaosBolt.desc = "Cause a bolt of chaotic energy to bounce between foes, searing the flesh."
setFire = Skill("Set Fire", fire, False, 5, 20, -1, 0,90, 3, [1,burn], ["hitAll"])
setFire.desc = "Watch them all burn to ashes."
forceShield = Skill("Force Shield", magic, False, 0, 0, -2, 0,100, 2, [], ["shield", "nodam", "trueHit"])
forceShield.desc = "Put up a shield of energy to block incomming damage."

chaosBeam = Skill("Chaos Beam", chaos, False, 20, 20, -10, 0,94, 0, [], ["fullmana"])
chaosBeam.desc = "Convert all of your power into choatic energy then blast it at your foe."
meditate = Skill("Meditate", magic, False, 0, 0, 0, 0,100, 0, [], ["nodam", "trueHit", "meditate"])
meditate.desc = "Gain power through inner focus."
lifePact = Skill("Life Pact", blood, False, 0, 0, -2, 0,100, 4, [], ["lifepact", "trueHit"])
lifePact.desc = "Make a pact with your foe, if you take damage, so do they."
shroud = Skill("Shroud", dark, False, 0, 0, 10, 0,100, 2, [], ["shroud", "trueHit"])
shroud.desc = "Shroud yourself in darkness to avoid getting hit."
#-------------------------------------------------------------------
bludgeon = Skill("Bludgeon", fighting, True, 10, 2, -1, 0,90, 0, [], [""])
bludgeon.desc = "Bash your foe's brains in with a blunt weapon."
stab = Skill("Stab", fighting, True, 5, 7, 2, 0,100, 0, [], [""])
stab.desc = "Stab Stab Stab!"
confuse = Skill("Confuse", physic, False, 0, 0, 10, 0,80, 2, [1,confusion], [""])
confuse.desc = "Confuse your foe to lower their damage and defenses."
planAhead = Skill("Plan Ahead", tech, False, 0, 0, -10, 0,100, 0, [], ["atkUp", "trueHit"])
planAhead.desc = "Focus on planning your next move, immporving its weak points."
erase =Skill("Erase", unknown, False, 0, 0, -10, 0,100, 5, [], ["division"])
erase.desc = "Use the magic of the pencil to erase foes from existance."
create = Skill("Create", unknown, False, 0, 0, -10, 0,100, 0, [], ["createCreep", "trueHit"])
create.desc = "Create a creep"
create2 = Skill("Create", unknown, False, 0, 0, -10, 0,100, 0, [], ["createWorship", "trueHit"])
create2.desc = "Create a worshiper to worship you, giving you power."
create3 = Skill("Create", unknown, False, 0, 0, -10, 0,100, 0, [], ["createCubes", "trueHit"])
create3.desc = "Clone more CUBES!"
mend = Skill("Mend", magic, False, 0,0, 1, 0,100, 3, [], ["heal", "trueHit"])
mend.desc = "Heal yourself or an ally."
#------------------------------------------------------------------
zap = Skill("Lightning", electic, False, 5, 10, 3, 4, 100, 0, [], [""])
zap.desc = "A stray electron zaps your foe."
energiBeam = Skill("Energy Beam", tech, False, 77, 10, -3, 0,90, 5, [], [""])
energiBeam.desc = "A strong electronic beam fries foes."
wellspring = Skill("Wellspring", tech, False, 0, 0, 3, 0,100, -10, [], ["trueHit"])
wellspring.desc = "Generate power through technology."
#-----------------------------------------------------------------
bladeFlash = Skill("Blade Flash", fighting, True, 6, 5, 10, 2,90, 1, [], [""])
bladeFlash.desc = "Quick draw your sword, cutting into your foe before anyone else can act."
cleave = Skill("Cleave", fighting, True, 20, 20, -2, 2,90, 2, [2, bleed], [""])
cleave.desc = "Bring back your blade for a heavy blow, can cause bleeding."
revenge = Skill("Revenge", dark, False, 0, 0, 10, 0,100, 5, [], ["revenge"])
revenge.desc = "All the rage you have against your foes is released in a fury of blows."
#----------------------------------------------------------------------
obsidianBlast = Skill("Obsidian Blast", fire, False, 30, 10, -3, 0,90, 5, [1, burn] ,[""])
obsidianBlast.desc = "Create burnning obsidian shards to burn your foe."
recover = Skill("Recover", magic, False, 0, 0, 10, 0,100, 7, [], ["recover", "endeffect", "trueHit"])
recover.desc = "Recover lost energy, ending all negative effects and healing yourself."
psionicRadiance = Skill("Psionic Radiance", physic, False, 47, 10, -2, 3,100, 3, [], [""])
psionicRadiance.desc = "Use the power of physic energy to cause horrible headaches."
#------------------------------------------------------------------------
stare = Skill("Stare", physic, False, 30, 10, -2, 15,100, 5, [], [""])
stare.desc = "Jiiiiiiiiiiiiiiiiii"
blink = Skill("Blink", physic, True, 5, 5, 1, 0,100, 0, [], ["mark"])
blink.desc = "Blink Blink"
creepyAtk = Skill("Creep Attack", physic, False, 5, 5, 1, 0,90, 0, [], ["creepyAtk"])
creepyAtk.desc = "Use all the knowledge you have about your enemy to find their weakest point."
inhale = Skill("Inhale", air, False, 0, 0, 3, 0,100, 0, [], ["defend", "heal", "trueHit"])
inhale.desc = "Inhale to absorb some healthy particles, healing yourself and defending."
observe = Skill("Observe", unknown, False, 0, 0, 3, 2, 100, 1, [], ["mark", "mark", "mark", "mark", "mark", "mark", "nodam", "trueHit"])
observe.desc = "Watch your foe to learn about them."
exhale = Skill("Exhale", air, False, 5, 10, 3, 0, 85, 0, [], ["mark", "hitAll"])
exhale.desc = "Breath out to cause minor damage to all foes."
#------------------------------------------------------------------------
sneeze = Skill("Sneeze", acid, False, 14, 6, 6, 0,90, 1, [2, poison], [""])
sneeze.desc = "Sneeze to cause minor damage and chance of poison."

eggon = Skill("Egg On", normal, True, 0, 0, 10, 10, 100, 2, [1, rebuff], ["trueHit", "nodam"])
eggon.desc = "Cheer on yourself or your friends to increase damage and hit chance."
rebuke = Skill("Rebuke", normal, True, 0, 0, 10, 2, 100, 1, [], ["removeEff", "trueHit", "nodam"])
rebuke.desc = "Cheer on your friends to remove all their negative effects."

blast = Skill("Blast", tech, False, 20, 20, 5, 8, 95, 2, [2, burn], [""])
blast.desc = "Fire a bolt of energy into your foes. Can cause burns."
fission = Skill("Fission", fire, False, 20, 40, -1, 0, 90, 0, [2, burn], ["powerDown", "fullmana"])
fission.desc = "Break appart nearby atoms to cause major damage."
fusion = Skill("Fusion", fire, False, 1, 40, -1, 0, 100, 1, [2,burn], ["powerUp"])
fusion.desc = "Collect nearby atoms from foes in order to gain power and cause burns."

lifeTransfer = Skill("Life Transfer", blood, False, 0, 0, 10, 0,100, 2, [], ["lifeTransfer", "nodam"])
lifeTransfer.desc = "Transfer some life force to an ally."
powerTransfer = Skill("Power Transfer", tech, False, 0, 0, 10, 0, 100, 0, [], ["powerTransfer", "nodam", "trueHit"])
powerTransfer.desc = "Transfer some power to an ally."

earthStage = Skill("Earth Stage", astral, False, 10, 15, 10, 0, 100, 0, [], ["trueHit","hitAll","earthStage"])
earthStage.desc = ""
moonStage = Skill("Moon Stage", astral, False, 10, 15, 10, 0, 100, 0, [], ["trueHit","hitAll","moonStage"])
moonStage.desc = ""
otherStage = Skill("Otherworld Stage", astral, False, 10, 15, 10, 0, 100, 0, [], ["trueHit","hitAll","otherStage"])
otherStage.desc = ""
voidSnap = Skill("Void Snap", astral, False, 30, 10, 4, 5, 97, 1, [2,bleed], [""])
voidSnap.desc = "Open a hole in the fabric of reality to cause damage. May cause bleeding."
chains = Skill("Chains", normal, True, 30, 2, 1, 5, 90, 1, [], [""])
chains.desc = "Whip foes with chains."
earthenVortex = Skill("Earthen Vortex", earth, False, 30, 40, 5, 6, 90, 2, [2, slowed], ["hitAll"])
earthenVortex.desc = "Cause a vortex of earthen energy."
astralVortex = Skill("Astral Vortex", astral, False, 50, 40, 5, 6, 90, 3, [], ["hitAll"])
astralVortex.desc = "Cause a vortex of astral energy."
chaosVortex = Skill("Chaos Vortex", chaos, False, 20, 60, 5, 6, 90, 2, [], ["hitAll"])
chaosVortex.desc = "Cause a vortex of chaotic energy."

againstOdds = Skill("Against The Odds", light, True, 0, 10, 3, 13, 90, 7, [], ["againstOdds"])
againstOdds.desc = "Against odds stacked against you, you still come out on top."
takeBlow = Skill("Take The Blow", fighting, True, 0, 0, 12, 10, 100, 1, [], ["takeBlow", "trueHit", "nodam"])
takeBlow.desc = "Prepare to take a blow for an ally."
powerStrike = Skill("Power Strike", fighting, True, 75, 10, -1, 0, 40, 1, [], [""])
powerStrike.desc = "Put all of your strength into one attack. Has a low chance of hitting."
antiPhysic = Skill("Anti Physic", unknown, False, 30, 20, 5, 15, 90, 2, [], [""])
mindReading = Skill("Mind Reading", physic, False, 20, 20, 5, 2, 100, 2, [], ["mindReading"])
mindReading.desc = "Read your foes mind to gain knowledge about their next attack."
neverThere = Skill("Never There", physic, False, 0,0, 20, 0, 100, 2, [], ["trueHit", "neverThere"])
neverThere.desc = "You were never there in the first place."
colorfulBullet = Skill("colorfulBullet", magic, False, 10,5, 1, 2, 90, 0, [], [""])
colorfulBullet.desc = "Summon a few bullets of magic energy to injure your foes."
never = Skill("And Never Come Back", unknown, False, 200, 50, 20, 5, 100, 7, [], ["trueHit"])
never.desc = "Never. Come. Back."
mindDisk = Skill("Mind disk", physic, False, 20, 10, 4, 5, 100, 0, [2, slowed], ["dodgeUp"])
mindDisk.desc = "Thow a mind disk at a foe to slow them. Increases your dodge chance."
daggerStorm = Skill("Dagger Storm", light, True, 40, 50, 10, 7, 99, 3, [], ["hitAll"])
daggerStorm.desc = "Summon a swarm of daggers to shred your foes."
eldritchAppuratus = Skill("Eldritch Appuratus", tech, False, 0, 0, 3, 2, 100, 3, [], ["powerUp", "recover"])
windSlash = Skill("Wind Slash", air, False, 20, 10, 5, 3, 90, 1, [], [])
windSlash.desc = "Slash so fast, your opponents will not even know what hit them."
rejuvinate = Skill("rejuvinate", magic, False, 0,0, 5, 3, 100, 4, [], ["recover", "recover"])
rejuvinate.desc = "Heal yourself alot."
mindSpike = Skill("Mind Spike", physic, False, 0,0, 5, 3, 100, 3, [], ["mindSpike", "nodam"])
mindSpike.desc = "Make them pay for hurting you or your friends."


instantkill = Skill("Insta kill", unknown, False, 99999, 9999, 99, 15, 100, 0, [], ["trueHit"])
instantkill.desc = "BAM! You dead now."


class Equip(object):
	def __init__(self, name, atk, int, con, mag, agil, crit, dodgeChance, lvl, slot):
		self.name = name
		self.atk = atk
		self.int = int
		self.con = con
		self.mag = mag
		self.agil = agil
		self.crit = crit
		self.dodgeChance = dodgeChance
		self.lvl = lvl
		self.slot = slot
		
emptySlot = Equip("Nothing", 0, 0, 0, 0, 0, 0, 0, 0, "")


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
		self.power = 1
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
		self.misc = 0
		self.vital = True
		#AI stuff
		self.savingfor = "none"
		self.aimisc = 0
		self.isAi = False
		self.equips = {"Head":emptySlot, "Chest":emptySlot, "Legs":emptySlot, "Feet":emptySlot, "Weapon":emptySlot}


	def updateEquips(self):
		self.equipStr = self.equips["Head"].str + self.equips["Chest"].str + self.equips["Legs"].str + self.equips["Feet"].str + self.equips["Weapon"].str
		self.equipInt = self.equips["Head"].int + self.equips["Chest"].int + self.equips["Legs"].int + self.equips["Feet"].int + self.equips["Weapon"].int
		self.equipCon = self.equips["Head"].con + self.equips["Chest"].con + self.equips["Legs"].con + self.equips["Feet"].con + self.equips["Weapon"].con
		self.equipMag = self.equips["Head"].mag + self.equips["Chest"].mag + self.equips["Legs"].mag + self.equips["Feet"].mag + self.equips["Weapon"].mag
		self.equipAgil = self.equips["Head"].agil + self.equips["Chest"].agil + self.equips["Legs"].agil + self.equips["Feet"].agil + self.equips["Weapon"].agil
		self.equipCrit = self.equips["Head"].crit + self.equips["Chest"].crit + self.equips["Legs"].crit + self.equips["Feet"].crit + self.equips["Weapon"].crit
		self.equipDodgeChance = self.equips["Head"].dodgeChance + self.equips["Chest"].dodgeChance + self.equips["Legs"].dodgeChance + self.equips["Feet"].dodgeChance + self.equips["Weapon"].dodgeChance
		
		
		
		
		
	def buildNew(self):
		newchar = Char(self.name, self.types, self.hp, self.str, self.int, self.con, self.mag, self.agil, self.crit, self.dodgeChance, self.lvl, self.xp, self.skills, self.ability, pygame.transform.scale(pygame.image.load(self.image), [50, 50]), self.cords, pygame.transform.scale(pygame.image.load(self.image), [42, 42]))
		newchar.img = pygame.image.load(self.image)
		newchar.target = [NOT]
		return newchar
		
	def reBuild(self):
		newchar = Char(self.name, self.types, self.hp, self.str, self.int, self.con, self.mag, self.agil, self.crit, self.dodgeChance, self.lvl, self.xp, self.skills, self.ability, self.image, self.cords, self.menuImg)
		newchar.img = self.image
		return newchar
	
		
NOT = Char("???", [unknown], 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, [nothing], "", "Assets/battlers/locked.png", [-1,0], "")

Mage = Char("Meigis", [normal, chaos], 500, 5, 15, 5, 15, 4, 0, 10, 1, 0, [basicAtk, fireBall, waterSpout, airBlast, earthShot, defend], "", "Assets/battlers/Mage.png", [5,0], "")

Mouther = Char("Mouther", [earth], 500, 20, 0, 10, 5, 4, 0, 10, 1, 0, [basicAtk, bite, consumeFlesh, defend], "", "Assets/battlers/Mouther.png", [4,0], "")

Maice = Char("Maice", [normal], 500, 15, 15, 10, 10, 6, 2, 11, 1, 0, [basicAtk, slash, bite, eggon], "", "Assets/battlers/nazrin.png", [3, 0], "") 

Nic = Char("Nic", [chaos], 500, 15, 50, 10, 25, 4, 0, 10, 1, 0, [basicAtk, magicMute, shardSwarm, powerUp, defend], "", "Assets/battlers/nic.png", [5,8], "")
Epic = Char("Epic", [tech], 1000, 25, 50, 35, 45, 7, 10, 10, 1, 0, [basicAtk,energiBeam, wellspring, defend], "", "Assets/battlers/epic.png", [7,8], "")

Scarlet = Char("Scarlet", [dark, blood], 100, 20, 20, 5, 20, 6, 0, 10, 1, 0, [basicAtk, scar, vampire, destroy, lifePact, defend], "", "Assets/battlers/vamp.png", [1,0], "")

Flan = Char("Flan", [dark,blood], 200, 35, 30, 10, 20, 7, 10, 20, 1, 0, [slash, rip, scar, vampire, destroy, lifePact, setFire, lifeTransfer], "watch them burn", "Assets/battlers/flandre.png", [5,7], "")
Nue = Char("Nue", [astral, dark], 300, 25, 40, 10, 50, 4, 15, 10, 1, 0, [basicAtk, meteorStorm, powerTransfer, forceShield, powerDrain, stab, meditate, defend], "Unidentifiable", "Assets/battlers/nue.png", [4,7], "")
Okuu = Char("Okuu", [fire, tech], 500, 15, 50, 30, 10, 1, 5, 5, 1, 0, [bludgeon, blast, fusion, fission, nuke, forceShield, recover], "Radiation", "Assets/battlers/reiji.png", [3,7], "")
Lapis = Char("Lapis", [astral], 400, 20, 20, 10, 10, 4, 5, 20, 1, 0, [chains, voidSnap, earthStage, moonStage, otherStage, earthenVortex, chaosVortex, astralVortex], "3 worlds", "Assets/battlers/lapis.png", [6,7], "")

Koishi = Char("Koishi", [unknown, physic], 400, 10, 55, 80, 100, 10, 6, 30, 1, 0, [colorfulBullet,mindReading, antiPhysic, neverThere, never, recover, voidSnap], "", "Assets/battlers/komeiji.png", [7,7], "")
#def __init__(self, name, types, hp, str, int, con, mag, agil, crit, dodgeChance, lvl, xp, skills, ability, image, cords, menuImg):
Nou = Char("Nou Furueteru", [physic], 300, 10, 50, 55, 90, 11, 7, 25, 1, 0, [colorfulBullet, mindDisk, mindReading, recover, forceShield, rejuvinate, meditate, defend], "", "Assets/battlers/Nou.png", [8,8], "")

Alpha = Char("Alpha", [normal, earth, fighting], 500, 50, -50, 30, 5, 5, 0, 10, 1, 0, [basicAtk, slash, cleave, bladeFlash, revenge, mend, defend], "", "Assets/battlers/alpha.png", [8,4], "")
Siv = Char("Siv", [normal, earth, dark, physic, chaos, magic], 250, 0, 50, 0, 38, 5, 7, 10, 1, 0, [basicAtk, chaosBolt, setFire, forceShield, chaosBeam, meditate, lifePact, shroud], "", "Assets/battlers/siv.png", [4,2], "")

Durric = Char("Durric", [earth, light, fighting, physic], 1000, 25, 25, 75, 25, 0, 0, 1, 1, 0, [basicAtk, forceShield, cleave, obsidianBlast, recover, psionicRadiance, mend, takeBlow], "Regen", "Assets/battlers/Durric.png", [4, 4], "")

Coo33 = Char("Coo33", [dark, blood], 250, 50, 0, 30, 0, 10, 10, 10, 5, 0, [basicAtk, slash, bite, kick, dodge, rip, consumeFlesh, defend], "Blood hunt", "Assets/battlers/Coo33.png", [3,3], "")
CoosomeJoe = Char("Coosome Joe", [light, tech], 500, 25, 25, 25, 25, 5, 2, 10, 1, 0, [basicAtk, bludgeon, erase, create2, confuse, planAhead, mend, defend], "Frenzy", "Assets/battlers/Coosome.png",  [3, 4], "")
Catsome = Char("Catsome", [light, physic], 1000, 10, 35, 10, 15, 5, 5, 10, 1, 0, [slash, bite, eggon, rebuke, mend, recover], "Cuteness", "Assets/battlers/catsome.png",[6,9], "")
Cubes = Char("Cubes", [tech], 400, 25, 35, 60, 30, 4, 5, 30, 1, 0, [zap, energiBeam, wellspring, planAhead, create3], "", "Assets/battlers/wip.png", [0,13], "")

Creep = Char("Creepy Bald Guy", [physic, unknown], 750, 10, 10, 15, 50, 0, 0, 0, 1, 0, [creepyAtk, blink, stare, inhale, exhale, observe], "Creepus", "Assets/battlers/Creepy_Bald_Guy.png", [3, 15], "")
KnowingEye = Char("Knowing Eye", [physic, unknown, astral], 750, 0, 75, 0, 75, 5, 6, 5, 1, 0, [creepyAtk, observe, meditate, magicMute, forceShield, create], "Creepus", "Assets/battlers/knowingeye.png", [4, 15], "")

Protagonist = Char("Protagonist", [normal], 750, 25, 15, 20, 10, 2, 6, 5, 1, 0, [basicAtk, powerStrike, eggon, mend, instantkill], "Frenzy", "Assets/battlers/wip.png", [1,1], "")

Axeurlegs = Char("Axurlegs", [grass], 10, 30, 0, 0, 1, 2, 3, 0, 1, 0, [axeLegs], "", "Assets/battlers/wip.png", [10,0], "")
Dandylion = Char("Dandy Lion", [grass], 600, 20, 15, 5, 20, 2, 2, 10, 1, 0, [slash, bite, tangle], "Frenzy", "Assets/battlers/wip.png", [11,0], "")

Worshipper = Char("Worshipper", [magic, chaos, minion], 300, 5, 15, 6, 10, 0, 0, 0, 1, 0, [basicAtk, fireBall, powerTransfer, lifeTransfer, meditate], "Frenzy", "Assets/battlers/wip.png", [2,0], "")
miniCreep = Char("Creepy Bald Guy", [physic, unknown, minion], 300, 6, 6, 8, 10, 0, 0, 0, 1, 0, [creepyAtk, blink, stare, inhale, exhale, observe], "Creepus", "Assets/battlers/Creepy_Bald_Guy.png", [3, 14], "")


NO = NOT.buildNew()	



		
	



