import random

turn = True
#=============START OF STATS========================

class Enemy01:
    #HP and attack
    enemy01Health = 100
    enemy01Attack = 20
    #specials
    revival = enemy01Health + 50
    revivalChance = random.randrange(1,100)



class Enemy02:
    #HP and attack
    enemy02health = 250
    enemy02attack = 30
    #specials
    enemy02CritDamage = enemy02attack * 2
    enemy02CritChance = ()
    enemy02Unkillable = ()

class Player:
    #HP and attack
    playerHealth = 1000
    playerAttack = 20
    #Defense
    playerDefense = ()
    #specials
    playerCritDmg = ()
    critChance = ()

class Boss:
    #HP and attack
    bossHealth = 500
    bossAttack = 100
    #boss specials
    smashAttack = bossAttack * 3
    defenceBreaker = ()

#==========END OF STATS==============================
#==========START OF BATTLEING========================

print("An enemy has appeared!!")
print(f"player health = {Player.playerHealth}")
print(f"player attack = {Player.playerAttack}")
print()
print(f"Enemy health = {Enemy01.enemy01Health}")
print(f"Enemy attack = {Enemy01.enemy01Attack}")
print()

while turn:


    while Enemy01.enemy01Health > 0:
            playerChoice = int(input("would you like to Attack (1) or block (2)?"))
            if playerChoice == 2:
                Player.playerHealth = Player.playerHealth - Enemy01.enemy01Attack / 2
                print()
                print("you blocked the enemys attack")
                print()
                print(f"player health = {Player.playerHealth}")
                print(f"player attack = {Player.playerAttack}")
                print()
                print(f"Enemy health = {Enemy01.enemy01Health}")
                print(f"Enemy attack = {Enemy01.enemy01Attack}")
                print()

            if playerChoice < 2:
                Enemy01.enemy01Health = Enemy01.enemy01Health - Player.playerAttack
                Player.playerHealth = Player.playerHealth - Enemy01.enemy01Attack
                print()
                print("Both you and the enemy attacked.")
                print()
                print(f"player health = {Player.playerHealth}")
                print(f"player attack = {Player.playerAttack}")
                print()
                print(f"Enemy health = {Enemy01.enemy01Health}")
                print(f"Enemy attack = {Enemy01.enemy01Attack}")
                print()
                
            while Enemy01.enemy01Health <= 0:
                if  Enemy01.revivalChance >= 90:
                    Enemy01.revival
                    print("The enemy revived!")
                else:
                    print("You killed the enemy!!")
            #if Enemy01.enemy01Health <= 0:
                #print("You killed the enemy!!")



