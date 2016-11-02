import random
import defs
import math
#thisbattler = runAI(thisbattler, battlers1, battlers2)

'''
Battlers with AI, in the order:
Axeurlegs, Maice, Worshipper, Creep 
Nou, Knowing eye, Lapis, Catsome, Coo33, Coosome

'''


#Make note that hitall effect needs to be applied in your ai.
#take in thisbattler, battlers1, battlers2
def runAI(player, battlersL, battlersR):
	for i in battlersL:
		if i.name == "???" or i == defs.NO or i == defs.NOT:
			battlersL.remove(i)
	for i in battlersR:
		if i.name == "???" or i == defs.NO or i == defs.NOT:
			battlersR.remove(i)
	consort, mgdsort, dmgtaken, potdam = [], [], [], []
	for i in battlersL:
		dmgtaken.append(i)
		consort.append(i)
		mgdsort.append(i)
		potdam.append(i)
	#greatest to least damage taken of enemies
	for i in range(len(dmgtaken)):
		for j in range(len(dmgtaken)-1-i):
			if dmgtaken[j].maxhp-dmgtaken[j].hp < dmgtaken[j+1].maxhp-dmgtaken[j+1].hp:
				dmgtaken[j], dmgtaken[j+1] = dmgtaken[j+1], dmgtaken[j]
	#Least to greatest Constitution of opponents
	for i in range(len(consort)):
		for j in range(len(consort)-1-i):
			if consort[j].con > consort[j+1].con:
				consort[j], consort[j+1] = consort[j+1], consort[j]
	#Least to greatest Magic defence of opponents
	for i in range(len(mgdsort)):
		for j in range(len(mgdsort)-1-i):
			if mgdsort[j].mag < mgdsort[j+1].mag:
				mgdsort[j], mgdsort[j+1] = mgdsort[j+1], mgdsort[j]
	#Greatest to Least potential damage of enemies
	for i in range(len(potdam)):
		for j in range(len(potdam)-1-i):
			if potdam[j].int + potdam[j].str > potdam[j+1].int + potdam[j+1].str:
				potdam[j], potdam[j+1] = potdam[j+1], potdam[j]

	
	#allies
	hptotal = []
	for i in battlersR:
		hptotal.append(i)
	#greatest to least hp of allies
	for i in range(len(hptotal)):
		for j in range(len(hptotal)-1-i):
			if hptotal[j].hp < hptotal[j+1].hp:
				hptotal[j], hptotal[j+1] = hptotal[j+1], hptotal[j]

	allies = battlersR
	for i in allies:
		if i == defs.NO:
			allies.remove(i)
	rand = random.randint(0, 1)

	#Suggested order:
	'''
	test quantity of allies and other related stuff
	figure out what to save up for, who to use it on
	see if you are there
	if not, use basic attack
	'''
	
#LESSER DUDES
	if player.name == "???":
		player.goskill, player.target = player.skills[0], [player]
	
	if player.name == "Axurlegs":
		player.goskill, player.target = player.skills[0], [consort[0]]
	
	if player.name == "Maice":
		if len(allies) > 1 and not defs.rebuff in player.effects:
			player.savingfor = "eggon"
		if player.savingfor == "none" or defs.rebuff in player.effects:
			player.savingfor = "bite"
		if player.savingfor == "bite":
			if player.power >= player.skills[2].cost:
				player.goskill, player.target = player.skills[2], [potdam[0]]
			else:
				if rand == 0:
					player.goskill, player.target = player.skills[0], [potdam[0]]
				else:
					player.goskill, player.target = player.skills[1], [potdam[0]]
		if player.savingfor == "eggon":
			if player.power >= player.skills[3].cost:
				player.goskill, player.target = player.skills[3], [allies[random.randint(0,len(allies)-1)]]
			else:
				if rand == 0:
					player.goskill, player.target = player.skills[0], [potdam[0]]
				else:
					player.goskill, player.target = player.skills[1], [potdam[0]]
		else:
			player.savingfor = "bite"
				
	if player.name == "Worshipper":
		#set up target
		if player.aimisc == 0 or player.misc != True:
			#player.misc is if the worshipper is supporting
			player.misc = False
			for i in battlersR:
				if not defs.minion in i.types:
					player.misc = True
					try:
						if player.aimisc.int + player.aimisc.str < i.int + i.str:
							player.aimisc = i
					except:
						player.aimisc = i
					print "now worshipping: "+i.name
			if player.aimisc == 0:
				player.aimisc = player
		if player.aimisc.hp <= 0:
			player.misc = False
		#do the stuff
		if player.misc:
			player.goskill, player.target = player.skills[4], [player.aimisc]
			if player.aimisc.hp <= 200:
				player.savingfor = "lifetransfer"
			else:
				player.savingfor = "powertransfer"
			if player.power >= 2 and player.savingfor == "lifetransfer":
				player.goskill = player.skills[3]
			if player.power >= 5 and player.savingfor == "powertransfer":
				player.goskill = player.skills[2]

		else:
			player.target = [battlersL[random.randint(0, len(battlersL)-1)]]
			if player.power >= 2:
				player.goskill = player.skills[1]
			else:
				player.goskill = player.skills[0]
						
	if player.name == "Creepy Bald Guy":
		support = False
		for i in battlersR:
			if i.name == "Knowing Eye":
				support = True
		if support:
			player.goskill = player.skills[5]
			player.target = [potdam[0]]
		else:
			player.target = [battlersL[random.randint(0, len(battlersL))]]
			if player.target[0].mag > player.target[0].con:
				player.goskill = player.skills[1]
			else:
				player.goskill = player.skills[2]
				if player.power >= 5:
					player.goskill = player.skills[2]
			if rand == 1:
				player.goskill = player.skills[4]
			if player.hp < 100 and rand == 0:
				player.goskill = player.skills[3]
	
#BOSSES
	if player.name == "Nou Furueteru":
		if player.hp < player.maxhp / 3:
			player.savingfor = "rejuvinate"
		else:
			player.savingfor = "mindReading"
			
			
		if player.savingfor == "mindReading":
			if player.power >= player.skills[2].cost:
				player.goskill, player.target = player.skills[2], [potdam[0]]
			else:
				if rand == 1:
				
					player.goskill, player.target = player.skills[1], [potdam[0]]
				if rand == 0:
				
					player.goskill, player.target = player.skills[0], [potdam[0]]
		if player.savingfor == "rejuvinate":
			if player.power >= player.skills[5].cost:
				player.goskill, player.target = player.skills[2], [player]
			else:
				player.savingfor = "meditate"
				
		
		if player.savingfor == "meditate":
			if player.power >= player.skills[6].cost:
				player.goskill, player.target = player.skills[6], [player]
			else:
				player.goskill, player.target = player.skills[0], [potdam[0]]
		
		if player.savingfor == "forceShield":
			if player.power >= player.skills[4].cost:
				player.goskill, player.target = player.skills[4], [player]
			else:
				player.goskill, player.target = player.skills[0], [potdam[0]]
			
	if player.name == "Knowing Eye":
		player.aimisc -= 1
		print player.aimisc, rand
		if len(allies) < 3:
			player.savingfor = "create"
		if player.savingfor == "none":
			if rand == 0:
				player.savingfor = "mute"
			if rand == 1:
				player.savingfor = "shield"
		if player.aimisc <= 0:
			player.aimisc, player.goskill, player.target = 3, player.skills[0], [battlersL[0]]
			for i in battlersL:
				temp1, temp2 = i.mag, player.target[0].mag
				if temp1 < 1:
					temp1 = 1
				if temp2 < 1:
					temp2 = 1
				if i.marks/temp1 > player.target[0].marks/temp2:
					player.target = [i]
					break

		#create
		if player.savingfor == "create" and player.power >= defs.create.cost:
			player.goskill, player.target, player.savingfor = player.skills[5], [player], "none"

		#magic mute
		if player.savingfor == "mute" and player.power >= defs.magicMute.cost:			
			for i in potdam:
				if defs.magicmute not in i.effects:
					player.goskill, player.target, player.savingfor = player.skills[3], [i], "none"
					break
		
		if player.savingfor == "shield" and player.power >= defs.forceShield.cost:
			player.goskill, player.target, player.savingfor = player.skills[4], [player], "none"

		#meditate
		if player.savingfor in ["create", "mute", "shield"]:
			player.goskill, player.target = player.skills[2], [player]
		
		print player, player.goskill, player.target[0]

	if player.name == "Lapis":
		if player.savingfor == "none" and player.hp >= player.hp / 3 and rand == 0:
			player.goskill, player.target = player.skills[4], [battlersL] 
			player.savingfor = "astral vortex"
		if player.savingfor == "none" and player.hp >= payer.hp / 3 and rand == 1:
			player.goskill, player.target = player.skills[3], [battlersL] 
			player.savingfor = "chaos vortex"
		if player.savingfor == "none" and player.hp <= player.hp / 3:
			player.goskill, player.target = player.skills[2], [battlersL]
			player.savingfor = "earth vortex"
		if player.savingfor == "astral vortex":
			if player.power >= player.skills[7].cost:
				player.goskill, player.target = player.skills[7], [battlersL]
			else:
				player.goskill, player.target = player.skills[0], [potdam[0]]
		if player.savingfor == "chaos vortex":
			if player.power >= player.skills[5].cost:
				player.goskill, player.target = player.skills[5], [battlersL]
			else:
				player.goskill, player.target = player.skills[0], [potdam[0]]
		if player.savingfor == "earth vortex" and player.hp > player.max / 4:
			if player.power >= player.skills[6].cost:
				player.goskill, player.target = player.skills[6], [battlersL]
			else:
				player.goskill, player.target = player.skills[0], [potdam[0]]
		else:
			player.goskill, player.target = player.skills[1], [potdam[0]]
				
	if player.name == "Catsome":
		allies, prefferedtarget = len(allies), "self"
		print allies
		#solo
		if allies == 1 and player.savingfor == "none":
			#selecting skill
			if player.maxhp-player.hp > 400 and random.randint(0, 2) == 1 and player.savingfor == "none":
				player.savingfor = "heal"
			for i in defs.negeff:
				if i in player.effects:
					player.savingfor = "rebuke"
			if player.savingfor == "none" and random.randint(0, 1) == 1:
				player.savingfor = "eggon"
			if defs.rebuff in player.effects or player.savingfor == "none":
				player.savingfor = "attack"
				prefferedtarget = "enemy"
		
		#Multiple allies
		if allies >= 2:
			#heal ally if somewhat low hp
			if player.savingfor == "none" or player.savingfor == "heal":
				for i in hptotal:
					if i.hp < 800:
						player.savingfor = "heal"
						player.aimisc = i
						prefferedtarget = "ally"
				if defs.CoosomeJoe in battlersR or defs.Coo33 in battlersR:
					for i in hptotal:
						if i.hp < 700 and i.name == "Coo33" or i.hp < 700 and i.name == "Coosome Joe":
							player.savingfor = "heal"
							player.aimisc = i
				if player.hp <= 200 and random.randint(0, 2) == 1:
					prefferedtarget, player.savingfor = "self", "heal"
			#rebuke if ally has negative effect
			for i in hptotal:
				for x in defs.negeff:
					if x in i.effects:
						player.savingfor = "rebuke"
						player.aimisc = i
						prefferedtarget = "ally"
			#Egging on of allies
			if player.savingfor == "none" and rand == 1:
				player.savingfor = "eggon"
				player.target = [battlersR[random.randint(0, len(battlersR)-1)]]

		#applying savingfor
		elif player.savingfor == "eggon" and player.power >= 2:
			player.goskill = player.skills[2]
			player.savingfor = "none"
		if player.savingfor == "heal" and player.power >= 3:
			player.goskill = player.skills[4]
			player.savingfor = "none"
			if prefferedtarget != "self":
				prefferedtarget = "ally"
		if player.savingfor == "rebuke" and player.power >= 1:
			player.goskill = player.skills[3]
			player.savingfor = "none"
		else:
			prefferedtarget = "enemy"
			player.goskill = player.skills[rand]
			if player.crit >= 8:
				player.goskill = player.skills[1]

		#setting target
		if prefferedtarget == "self":
			player.target = [player]
		if prefferedtarget == "enemy":
			if player.goskill == player.skills[1]:
				player.target = [dmgtaken[len(dmgtaken)-1]]
			else:
				player.target = [consort[0]]
		if prefferedtarget == "ally":
			player.target = [player.aimisc]

	if player.name == "Coo33":
		#selecting skill
		if player.savingfor == "none" or player.hp <= 200:
			if player.hp <= 250 or rand == 0:
				player.savingfor = "consume"
			else:
				player.savingfor = "rip"
		#using a powerful attack
		if player.power >= 3:
			if player.savingfor == "consume" or player.crit >= 30:
				player.goskill, player.savingfor, player.target = player.skills[6], "none", [consort[0]]
			else:
				player.goskill, player.savingfor, player.target = player.skills[5], "none", [dmgtaken[len(dmgtaken)-1]]
		#if not enough power to use
		else:
			player.goskill = player.skills[rand]
			if player.crit >= 15:
				player.goskill, player.target = player.skills[1], [dmgtaken[len(dmgtaken)-1]]
			else:
				player.target = [consort[0]]
	
	if player.name == "Coosome Joe":
		if len(allies) < 3:
			player.savingfor = "create"
		if player.savingfor == "none":
			if player.hp > 250:
				doing = False
				for i in battlersL:
					if i.hp <= i.maxhp/5:
						doing = True
						break
				if doing:
					player.savingfor = "erase"
				else:
					player.savingfor = "mend"
			elif player.hp > 480 and rand == 1 or player.hp >= 500:
				player.savingfor = "planattack"
			else:
				player.savingfor = "mend"

		if player.savingfor == "create":
			if player.power >= defs.create2.cost:
				player.goskill, player.target, player.savingfor = player.skills[3], [player], "none"
			else:
				player.goskill, player.target = player.skills[rand], [consort[0]]

		if player.savingfor == "erase" and player.power >= create2.cost:
			player.goskill, player.target, player.savingfor = player.skills[2], [potdam[0]], "none"
			for i in range(len(potdam)):
				l = potdam[(len(potdam)-1)-i]
				if l.hp <= l.maxhp/5:
					player.target = l

		if player.savingfor == "mend":
			if player.power >= defs.mend.cost:
				player.goskill, player.target, player.savingfor = player.skills[6], [player], "none"
			else:
				player.goskill, player.target = player.skills[rand], [consort[0]]

		if player.savingfor == "planattack":
			if player.hp <= 400:
				player.goskill, player.target, player.savingfor = player.skills[1], [consort[0]], "none"
			else:
				player.goskill, player.target = player.skills[5], [player]
		print player.goskill, player.target, player.savingfor
		print player.goskill.name
	return player
