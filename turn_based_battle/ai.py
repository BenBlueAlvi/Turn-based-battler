import random
import defs
#thisbattler = runAI(thisbattler, battlers1, battlers2)

#Make note that hitall effect needs to be applied in your ai.
#take in thisbattler, battlers1, battlers2
def runAI(player, battlersL, battlersR):

	consort, dmgtaken, hptotal = [], [], []
	for i in battlersL:
		consort.append(i)
		dmgtaken.append(i)
		hptotal.append(i)
	#
	for i in range(len(consort)):
		for j in range(len(consort)-1-i):
			if consort[j].con < consort[j+1].con:
				consort[j], consort[j+1] = consort[j+1], consort[j]
	#greatest to least damage taken
	for i in range(len(dmgtaken)):
		for j in range(len(dmgtaken)-1-i):
			if dmgtaken[j].maxhp-dmgtaken[j].hp < dmgtaken[j+1].maxhp-dmgtaken[j+1].hp:
				dmgtaken[j], dmgtaken[j+1] = dmgtaken[j+1], dmgtaken[j]
	#greatest to least hp
	for i in range(len(hptotal)):
		for j in range(len(hptotal)-1-i):
			if hptotal[j].hp < hptotal[j+1].hp:
				hptotal[j], hptotal[j+1] = hptotal[j+1], hptotal[j]
	#Suggested order:
	'''
	test quantity of allies and other related stuff
	figure out what to save up for, who to use it on
	see if you are there
	if not, use basic attack
	'''

	if player.name == "Catsome":
		allies, prefferedtarget = len(battlersR), "self"

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
			if rebuff in player.effects or player.savingfor == "none":
				player.savingfor = "attack"
				prefferedtarget = "enemy"
		
		#Multiple allies
		if allies >= 2:
			if player.savingfor == "none" or player.savingfor == "heal":
				for i in hptotal:
					if i.hp < 800:
						player.savingfor = "heal"
						player.target = i
				if player.hp <= 200:
					player.prefferedtarget = "self"


		#applying savingfor
		if player.savingfor == "rebuke" and player.power >= 1:
			player.goskill = player.skills[3]
			player.savingfor = "none"
		elif player.savingfor == "eggon" and player.power >= 2:
			player.goskill = player.skills[2]
			player.savingfor = "none"
		else:
			rand, prefferedtarget = random.randint(0, 1), "enemy"
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


	if player.name == "Coo33":
		#selecting skill
		rand = random.randint(0, 1)
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
			if player.crit >= 8:
				player.goskill, player.target = player.skills[1], [dmgtaken[len(dmgtaken)-1]]
			else:
				player.target = [consort[0]]


	return player