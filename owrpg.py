# saving this personal project for later

import random

class Attack:
    def __init__(self, health, power, accuracy, dodge, ultimate):
        self.health = health
        self.power = power
        self.accuracy = accuracy
        self.dodge = dodge
        self.ultimate = ultimate
    def alive(self):
        if self.health <= 0:
            return False
        else:
            return True

class Healer:
    def __init__(self, heal, assist, ultimate):
        self.heal = heal
        self.assist = assist
        self.ultimate = ultimate

class Hero(Attack):
    def attack(self, enemy):
        if choice2 == 'mercy':
            countera = 0
            while countera < 1: 
                horp = input('Do you want Mercy to Heal or Power Assist you? (H or P)? ').lower()
                if horp == 'h':
                    random1 = random.randint(1, (heroa.accuracy + enemya.dodge))
                    if random1 == 1:
                        enemya.health -= self.power
                        self.ultimate = int(self.power * 0.10)
                        if enemya.health <= 0:
                            print(choice3 + " is dead.")
                            countera += 1
                            break
                        else:
                            if choice3 == 'reaper':
                                enemya.health += thealer.heal
                                enemya.health = min(250, enemya.health)
                            else:
                                enemya.health += thealer.heal
                                enemya.health = min(200, enemya.health)
                            mercyheal = 'y'
                            print("You do %d damage." % self.power)
                            print("You will be healed by %d next turn." % (hhealer.heal))
                            print("You gained an extra %d ult charge + 2 passive charge." % self.ultimate)
                            print(choice2.capitalize() + " gained 2 passive ult charge.")
                            print("After healing, " + choice3.capitalize() + "'s health is %d." % enemya.health)
                            print(choice3.capitalize() + " gained 2 passive ult charge.")
                            countera += 1
                    else:
                        print("You missed.")
                        countera += 1
                        self.ultimate = 0
                elif horp == 'p':
                    random2 = random.randint(1, (heroa.accuracy + enemya.dodge))
                    if random2 == 1:
                        newpower = (self.power + (self.power * hhealer.assist))
                        self.ultimate = int(newpower * 0.13)
                        enemya.health -= newpower
                        if enemya.health <= 0:
                            print(choice3 + " is dead.")
                            countera += 1
                            break
                        else:
                            if choice3 == 'reaper':
                                enemya.health += thealer.heal
                                enemya.health = min(250, enemya.health)
                                print(enemya.health)
                            else:
                                enemya.health += thealer.heal
                                enemya.health = min(200, enemya.health)
                                print(enemya.health)
                            print("You do %d damage." % newpower)
                            print("You will not be healed next turn.")
                            print("You gained an extra %d ult charge + 2 passive charge." % self.ultimate)
                            print(choice2.capitalize() + " gained 2 passive ult charge.")
                            print("After healing, " + choice3.capitalize() + "'s health is %d." % enemya.health)
                            print(choice3.capitalize() + " gained 2 passive ult charge.")
                            countera += 1
                    else:
                        print("You missed.")
                        countera += 1
                        self.ultimate = 0
                else:
                    print("Invalid answer.")
        else:
            random3 = random.randint(1, (heroa.accuracy + enemya.dodge))
            if random3 == 1:
                newpower1 = (self.power + (self.power * hhealer.assist))
                self.ultimate = int((newpower1 * 0.125))
                enemya.health -= newpower1
                hhealer.ultimate = int((self.power * hhealer.heal)/2)
                if enemya.health <= 0:
                    print(choice3.capitalize() + " is dead.")
                else:
                    if choice3 == 'reaper':
                        enemya.health += thealer.heal
                        enemya.health = min(250, enemya.health)
                        print(enemya.health)
                    else:
                        enemya.health += thealer.heal
                        enemya.health = min(200, enemya.health)
                        print(enemya.health)
                    print("You do %d damage." % newpower1)
                    print("You will be healed by %d next turn." % (hhealer.heal))
                    print("You gained an extra %d ult charge + 2 passive charge." % self.ultimate)
                    print(choice2.capitalize() + " gained 2 passive charge.")
                    print(choice3.capitalize() + " was healed by %d." % thealer.heal)
                    print(choice3.capitalize() + " gained 2 passive ult charge.")
            else:
                print("You missed.")
                self.ultimate = 0

    def secondary(self, enemy):
        if choice1 == 'tracer':
            heroa.health = max(recall)
            print("Your health has been restored to " + str(heroa.health))
        elif choice1 == 'soldier':
            counterb = 0
            if choice2 == 'mercy':
                while counterb < 1: 
                    horps = input('Do you want Mercy to Heal or Power Assist you? (H or P)? ').lower()
                    if horps == 'h':
                        randoms1 = random.randint(1, (2 + enemya.dodge))
                        if randoms1 == 1:
                            self.ultimate = int(120 * 0.10)
                            enemya.health -= 120
                            if enemya.health <= 0:
                                print(choice3 + " is dead.")
                            else:
                                if choice3 == 'reaper':
                                    enemya.health += thealer.heal
                                    enemya.health = min(250, enemya.health)
                                else:
                                    enemya.health += thealer.heal
                                    enemya.health = min(200, enemya.health)
                                print("Your helix rocket connects and does 120 damage.")
                                print("You will be healed by %d next turn." % hhealer.heal)
                                print("You gained an extra 2 passive charge.")
                                print(choice2.capitalize() + " gained 2 passive ult charge.")
                                print("After healing, " + choice3.capitalize() + "'s health is %d." % enemya.health)
                                print(choice3.capitalize() + "gained 2 passive ult charge.")
                                counterb += 1
                        else:
                            print("You missed.")
                            self.ultimate = 0
                            counterb += 1
                    if horps == 'p':
                        randoms2 = random.randint(1, (2 + enemya.dodge))
                        if randoms2 == 1:
                            self.ultimate = int(160 * 0.13)
                            enemya.health -= 160
                            if enemya.health <= 0:
                                print(choice3 + " is dead.")
                            else:
                                if choice3 == 'reaper':
                                    enemya.health += thealer.heal
                                    enemya.health = min(250, enemya.health)
                                else:
                                    enemya.health += thealer.heal
                                    enemya.health = min(200, enemya.health)
                                print("Your helix rocket connects and does 160 damage.")
                                print("You will be healed by %d next turn." % hhealer.heal)
                                print("You gained an extra %d ult charge + 2 passive charge." % self.ultimate)
                                print(choice2.capitalize() + " gained 2 passive ult charge.")
                                print("After healing, " + choice3.capitalize() + "'s health is %d." % enemya.health)
                                print(choice3.capitalize() + "gained 2 passive ult charge.")
                                counterb += 1
                        else:
                            print("You missed.")
                            self.ultimate = 0
                            counterb += 1
            else:
                randoms3 = random.randint(1, (2 + enemya.dodge))
                if randoms3 == 1:
                    self.ultimate = int(150 * 0.125)
                    enemya.health -= 150
                    if enemya.health <= 0:
                        print(choice3 + " is dead.")
                    else:
                        if choice3 == 'reaper':
                            enemya.health += thealer.heal
                            enemya.health = min(250, enemya.health)
                        else:
                            enemya.health += thealer.heal
                            enemya.health = min(200, enemya.health)
                        print("Your helix rocket connects and does 150 damage.")
                        print("You will be healed by %d next turn." % hhealer.heal)
                        print("You gained an extra %d ult charge + 2 passive charge." % self.ultimate)
                        print(choice2.capitalize() + " gained 2 passive ult charge.")
                        print("After healing, " + choice3.capitalize() + "'s health is %d." % enemya.health)
                        print(choice3.capitalize() + "gained 2 passive ult charge.")
                        counterb += 1
                else:
                    print("You missed.")
                    self.ultimate = 0
        elif choice1 == 'pharah':
            randomp = random.randint(1, 8 + enemya.dodge)
            if randomp == 1:
                enemya.health = 0
                print("Your boop connected. " + choice3.capitalize() + " fell off the map and died.")
            else:
                print("Your boop was not successful.")

    def ultabl(self, enemy):
        if choice1 == 'tracer':
            newrandom = random.randint(1, (2 + enemya.dodge))
            if newrandom == 1:
                enemya.health -= 300
                if enemya.health <= 0:
                    print("You stuck the pulse bomb, and " + choice3.capitalize() + " is dead.")
                else:
                    heroa.health += hhealer.heal
                    print("You stuck the pulse bomb and did 300 damage.")
                    print("You were healed by %d" % hhealer.heal)
                    print("Your ult charge is reset to 0 percent.")
                    print(choice3.capitalize() + " was healed by %d." % thealer.heal)
                    print(choice3.capitalize() + " gained 2 passive ult charge.")
            else:
                print("You missed.")
        if choice1 == 'soldier':
            print("Soldier76's visor is on, and he will not miss primary fire for the next six turns in a row.")
        if choice1 == 'pharah':
            newrandom1 = random.randint(1, (1 + enemya.dodge))
            if newrandom1 == 1:
                enemya.health -= 300
                if enemya.health <= 0:
                    print("Your rocket barrage killed " + choice3.capitalize() + ".")
                else:
                    heroa.health += hhealer.heal
                    print("Your barrage did 300 damage.")
                    print("You were healed by %d" % hhealer.heal)
                    print("Your ult charge is reset to 0 percent.")
                    print(choice3.capitalize() + " was healed by %d." % thealer.heal)
                    print(choice3.capitalize() + " gained 2 passive ult charge.")
            else:
                print("You missed.")
    
    def healult(self, enemy):
        if choice2 == 'mercy':
            print("Mercy will increase your health by 60 for 15 straight turns.")
        if choice2 == 'zen':
            print("Zenyatta will restore you health by 300 for 6 straight turns.")

    def print_status(self):
        print("You have %d health, %d power, %d acc, and %d dodge." % (self.health, self.power, self.accuracy, self.dodge))
        print(choice3.capitalize() + " has %d health, %d power, %d acc, and %d dodge." % (enemya.health, enemya.power, enemya.accuracy, enemya.dodge))
        if choice1 == 'tracer':
            print("Your sec ability cooldown count is at %d turns." % min(cooldownh, 12))
        if choice1 == 'soldier':
            print("Your sec ability cooldown count is at %d turns." % min(cooldownh, 8))
        if choice1 == 'pharah':
            print("Your sec ability cooldown count is at %d turns." % min(cooldownh, 9))
        print("Your ult charge is at %d percent." % min(100, ulth))
        print(choice2.capitalize() + "'s ult charge is at %d percent." % (min(100, healult)))
        # print(choice3.capitalize() + "'s ult charge is at %d percent." % min(100, ulte))

class Talon(Attack):
    def attack(self, enemy):
        random2 = random.randint(1, enemya.accuracy)
        if random2 == 1:
            if self.health > 0:
                heroa.health -= self.power
                print(choice3.capitalize() + " does %d damage to you." % self.power)
                if heroa.health <= 0:
                    print("You are dead."), print("")
        else:
            print(choice3.capitalize() + " missed.")

# self, health, power, accuracy, dodge, ultimate
tracer = Hero(150, 30, 1, 3, 0)
soldier = Hero(200, 40, 1, 2, 0)
pharah = Hero(200, 55, 2, 0, 0)
mercy = Healer(50, 0.30, 0)
zen = Healer(30, 0.25, 0)
reaper = Talon(250, 90, 1, 1, 0)
junkrat = Talon(200, 50, 3, 1, 0)
widow = Talon(200, 120, 3, 2, 0)
baptiste = Healer(30, 20, 0)
ana = Healer(75, 70, 0)

while 1 == 1:
    print("WELCOME TO OVERWATCH RPG"), print("")
    print("This is a 2v2 RPG featuring the heroes of Overwatch against Talon and their other enemies."), print("")
    print("HEROES"), print("")
    print("ATTACK: HP, DMG, ACC, Dodge, ESC, Reload FREQ, SEC, ULT"), print("")
    print("TRACER: 150, 30, 1/2, high, high, none, Recall: rest one turn and return to highest health in past 3 moves 12 cd, Pulse Bomb: 300 dmg 1/4 acc")
    print("SOLDIER76: 200, 40, 1/2, avg, high (returns full health), 3, Helix Rocket: 120 dmg 1/3 acc 8 cd, Visor: 1/1 acc for 6 straight turns")
    print("PHARAH: 200, 55 spl 120 dir, 1/2 spl 1/3 dir, low, avg, 6, Boop: instant kill 1/10 acc 9 cd, Barrage: 300 dmg 1/2 acc"), print("")
    print("SUPPORT: Heal/turn, DMG Assist, Sec, ULT"), print("")
    print("MERCY: +50, 30%, Resurrect: restores full health to fallen hero 30 cd, Valkyrie: increase to +60 h/t for 15 turns")
    print("ZENYETTA: +30, 25%, Orb: +48 dmg 1/5 acc, Transcendence: restores 300 hp for 6 straight turns"), print("")
    print("ENEMIES (*Note: Enemies will SEC and ULT as soon as they are able to."), print("")
    print("ATTACK:"), print("")
    print("REAPER: 250, 90, 1/1, low, high, 8, Shadow Step: for one turn either add 50 dmg or take a rest, Death Blossom: deals 170 dmg for 3 straight turns")
    print("JUNKRAT: 200, 50, 1/3, low, avg, 6, Steel Trap: 1/1 acc for 4 straight turns, Riptire: 600 dmg 1/2 acc")
    print("WIDOWMAKER: 200, 120 bs 200 hs, 1/3 bs 1/4 hs, high, low, 12, Grapple: rest one turn and restore health 10 cd, Infra-Sight: increase acc 1/2 bs 1/4 hs for 15 turns"), print("")
    print("SUPPORT (*Note: Enemy healers will always attack until healing is required):"), print("")
    print("BAPTISTE: +30 1/2 acc, +20 dmg 1/2 acc, Immortality Field: prevents enemy health from dropping below 20% for 4 turns, Amp Matrix: dmg assist increased to 40% for 4 turns")
    print("ANA: +75 1/2 acc, +70 dmg 1/2 acc, Sleep Dart: guarantees enemy 1/1 acc for one turn, Nano Boost: restores enemy health full, 50% dmg assist, and hero dmg reduced 50% for 8 turns")
    while 1 == 1:
        cont = input("Press ENTER to continue")
        break
    break

while 1 == 1:
    choice1 = input("Choose your hero (Tracer, Soldier76, or Pharah): ").lower()
    if choice1 == 'tracer':
        heroa = tracer
        recall = []
        break
    elif choice1 == 'soldier':
        heroa = soldier
        break
    elif choice1 == 'pharah':
        heroa = pharah
        break
    else:
        print("Invalid choice.")
while 1 == 1:
    choice2 = input("Choose your healer (Mercy or Zenyatta): ").lower()
    if choice2 == 'mercy':
        hhealer = mercy
        break
    elif choice2 == 'zenyatta':
        hhealer = zen
        break
    else:
        print("Invalid choice.")
while 1 == 1:
    choice3 = input("Choose your enemy (Reaper, Junkrat, or Widowmaker): ").lower()
    if choice3 == 'reaper':
        enemya = reaper
        break
    elif choice3 == 'junkrat':
        enemya = junkrat
        break
    elif choice3 == 'widowmaker':
        enemya = widow
        break
    else:
        print("Invalid choice.")
while 1 == 1:
    choice4 = input("Choose your enemy's healer (Baptiste or Ana): ").lower()
    if choice4 == 'baptiste':
        thealer = baptiste
        break
    elif choice4 == 'ana':
        thealer = ana
        break
    else:
        print("Invalid choice.")

cooldownh = 12
cooldowne = 0
ulth = 0
healult = 0
ulte = 0
while heroa.alive() and enemya.alive():
    ulth = min(ulth, 100)
    healult = min(healult, 100)
    my_random = random.randint(1, 5)
    if choice1 == 'tracer':
        recall.append(heroa.health)
        if len(recall) > 4:
            recall = [heroa.health]
    print("What do you want to do?")
    print("1. primary fire")
    print("2. secondary ability")
    print("3. ultimate ability")
    print("4. healer ultimate ability")
    print("5. check status")
    print("6. run")
    user_input = input()
    if user_input == "1":
        heroa.attack(enemya)
        cooldownh += 1
        ulth += (2 + heroa.ultimate)
        healult += 2
    elif user_input == "2":
        if choice1 == 'tracer':
            if cooldownh < 12:
                print("Sec ability still on cooldown.")
            else:
                heroa.secondary(enemya)
                cooldownh = 0
                ulth += (2 + heroa.ultimate)
                healult += 2
        elif choice1 == 'soldier':
            if cooldownh < 8:
                print("Sec ability still on cooldown.")
            else:
                heroa.secondary(enemya)
                cooldownh = 0
                ulth += (2 + heroa.ultimate)
                healult += 2
        elif choice1 == 'pharah':
            if cooldownh < 9:
                print("Sec ability still on cooldown.")
            else:
                heroa.secondary(enemya)
                cooldownh = 0
                ulth += (2 + heroa.ultimate)
                healult += 2
    elif user_input == "3":
        if ulth == 100:
            heroa.ultabl(enemya)
            ulth = 0
        else:
            print("Ultimate ability not sufficiently charged.")
    elif user_input == "4":
        if healult == 100:
            heroa.healult(enemya)
            healult = 0
        else:
            print("Healer ultimate ability not sufficiently charged.")
    elif user_input == "5":
        heroa.print_status()
    elif user_input == "6":
        print("Goodbye.")
        break
    else:
        print("Invalid input %r" % user_input)
    print(choice3 + " will now attack. Ults will be used as soon as possible, and sec abilities will be used as appropriate. Press ENTER to continue."
    user_input2 = input()
    if choice3 == 'reaper':
        