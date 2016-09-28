import random
#thisbattler.goskill, thisbattler.target = runAI(thisbattler)
#catsomecoosome = AI("catsome", 1)

#Make note that hitall effect needs to be applied in your ai.
#take in thisbattler, battlers1, battlers2
def runAI(player, battlersL, battlersR):

	consort, hpsort = [], []
	for i in battlersL:
		consort.append(i)
		hpsort.append(i)
	for i in range(len(consort)):
		for j in range(len(consort)-1-i):
			if consort[j].con < consort[j+1].con:
				consort[j], consort[j+1] = consort[j+1], consort[j]
	#greatest to least damage taken
	for i in range(len(hpsort)):
		for j in range(len(hpsort)-1-i):
			if hpsort[j].maxhp-hpsort[j].hp < hpsort[j+1].maxhp-hpsort[j+1].hp:
				hpsort[j], hpsort[j+1] = hpsort[j+1], hpsort[j]
	#Suggested order:
	'''
	test quantity of allies and other related stuff
	figure out what to save up for, who to use it on
	see if you are there
	if not, use basic attack
	'''

	if player.name == "Catsome":
		allies, prefferedtarget = len(battlersR), "self"

		if allies == 1:
			#selecting skill
			if player.maxhp-player.hp > 400 and random.randint(0, 2) == 1 and player.savingfor == "none":
				player.savingfor = "heal"
			negeffects = [burn, magicmute, bleed, poison, confusion]
			for i in negeffects:
				if i in player.effects:
					player.savingfor = "rebuke"
			if savingfor == "none" and random.randint(0, 1) == 1:
				player.savingfor == "eggon"
			if rebuff in player.effects or savingfor == "none":
				player.savingfor == "attack"
				prefferedtarget = "enemy"
				
		if allies == 2:
			pass

		#applying savingfor
		if savingfor == "rebuke" and player.power >= 1:
			player.goskill = player.skills[3]
		if savingfor == "eggon" and player.power >= 2:
			player.goskill = player.skills[2]
		else:

		if player.savingfor == "attack" or player.savingfor == "none":
			rand = random.randint(0, 1)
			player.goskill = player.skills[rand]
			if player.crit >= 8:
				player.goskill = player.skills[1]

		#setting target
		if prefferedtarget == "self":
			player.target = [player]
		if prefferedtarget == "enemy":
			if player.goskill == player.skills[1]:
				player.target = [hpsort[len(hpsort)-1]]
			else:
				player.target = [consort[0]]



	return player.goskill, player.target