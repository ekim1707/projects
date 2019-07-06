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
    def __init__(self, heal, assist, ultimate, mercyvar):
        self.heal = heal
        self.assist = assist
        self.ultimate = ultimate
        self.mercyvar = mercyvar

class Hero(Attack):
    def attack(self, enemy):
        if choice2 == 'mercy':
            countera = 0
            while countera < 1: 
                horp = input('Do you want Mercy to Heal or Power Assist you? (H or P)? ').lower()
                if horp == 'h':
                    hhealer.mercyvar = 1
                    random1 = random.randint(1, (heroa.accuracy + enemya.dodge))
                    if random1 == 1:
                        enemya.health -= self.power
                        self.ultimate = int(self.power * 0.10)
                        if enemya.health <= 0:
                            print(choice3 + " is dead.")
                            countera += 1
                            break
                        else:
                            print("You do %d damage." % self.power)
                            print("You will be healed by %d next turn." % (hhealer.heal))
                            print("You gained an extra %d ult charge + 2 passive charge." % self.ultimate)
                            print(choice2.capitalize() + " gained 2 passive ult charge.")
                            if choice3 == 'reaper':
                                if enemya.health >= 250:
                                    thealer.mercyvar = 1
                                else:
                                    randomthh = random.randint(1, (enemya.dodge + 3))
                                    if randomthh == 1:
                                        enemya.health += thealer.heal
                                        thealer.ultimate = int(thealer.heal * 0.10)
                                        enemya.health = min(250, enemya.health)
                                        print("After healing, " + choice3.capitalize() + "'s health is %d." % enemya.health)
                                        print(choice3.capitalize() + " gained 2 passive ult charge.")
                                    else:
                                        thealer.ultimate = 0
                                        print(choice4.capitalize() + "'s healing attempt missed.")
                                        print(choice3.capitalize() + "'s health is %d." % enemya.health)
                                        print(choice3.capitalize() + " gained 2 passive ult charge.")
                                        print(choice4.capitalize() + " gained 2 passive ult charge.")
                            else:
                                if enemya.health >= 200:
                                    thealer.mercyvar = 1
                                else:
                                    randomthh1 = random.randint(1, (enemya.dodge + 3))
                                    if randomthh1 == 1:
                                        enemya.health += thealer.heal
                                        thealer.ultimate = int(thealer.heal * 0.10)
                                        enemya.health = min(200, enemya.health)
                                        print("After healing, " + choice3.capitalize() + "'s health is %d." % enemya.health)
                                        print(choice3.capitalize() + " gained 2 passive ult charge.")
                                    else:
                                        thealer.ultimate = 0
                                        print(choice4.capitalize() + "'s healing attempt missed.")
                                        print(choice3.capitalize() + "'s health is %d." % enemya.health)
                                        print(choice3.capitalize() + " gained 2 passive ult charge.")
                                        print(choice4.capitalize() + " gained 2 passive ult charge.")
                            countera += 1
                    else:
                        print("You missed.")
                        countera += 1
                        self.ultimate = 0
                elif horp == 'p':
                    hhealer.mercyvar = 0
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
                            print("You do %d damage." % newpower)
                            print("You will not be healed next turn.")
                            print("You gained an extra %d ult charge + 2 passive charge." % self.ultimate)
                            print(choice2.capitalize() + " gained 2 passive ult charge.")
                            if choice3 == 'reaper':
                                if enemya.health >= 250:
                                    thealer.mercyvar = 1
                                else:
                                    randomthh2 = random.randint(1, (enemya.dodge + 3))
                                    if randomthh2 == 1:
                                        enemya.health += thealer.heal
                                        thealer.ultimate = int(thealer.heal * 0.10)
                                        enemya.health = min(250, enemya.health)
                                        print("After healing, " + choice3.capitalize() + "'s health is %d." % enemya.health)
                                        print(choice3.capitalize() + " gained 2 passive ult charge.")
                                    else:
                                        thealer.ultimate = 0
                                        print(choice4.capitalize() + "'s healing attempt missed.")
                                        print(choice3.capitalize() + "'s health is %d." % enemya.health)
                                        print(choice3.capitalize() + " gained 2 passive ult charge.")
                                        print(choice4.capitalize() + " gained 2 passive ult charge.")
                            else:
                                if enemya.health >= 200:
                                    thealer.mercyvar = 1
                                else:
                                    randomthh3 = random.randint(1, (enemya.dodge + 3))
                                    if randomthh3 == 1:
                                        enemya.health += thealer.heal
                                        thealer.ultimate = int(thealer.heal * 0.10)
                                        enemya.health = min(200, enemya.health)
                                        print("After healing, " + choice3.capitalize() + "'s health is %d." % enemya.health)
                                        print(choice3.capitalize() + " gained 2 passive ult charge.")
                                    else:
                                        thealer.ultimate = 0
                                        print(choice4.capitalize() + "'s healing attempt missed.")
                                        print(choice3.capitalize() + "'s health is %d." % enemya.health)
                                        print(choice3.capitalize() + " gained 2 passive ult charge.")
                                        print(choice4.capitalize() + " gained 2 passive ult charge.")
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
                # hhealer.ultimate = int((self.power * hhealer.heal)/2)
                if enemya.health <= 0:
                    print(choice3.capitalize() + " is dead.")
                else:
                    print("You do %d damage." % newpower1)
                    print("You will be healed by %d next turn." % (hhealer.heal))
                    print("You gained an extra %d ult charge + 2 passive charge." % self.ultimate)
                    print(choice2.capitalize() + " gained 2 passive ult charge.")
                    if choice3 == 'reaper':
                        if enemya.health >= 250:
                            thealer.mercyvar = 1
                        else:
                            randomthh5 = random.randint(1, (enemya.dodge + 3))
                            if randomthh5 == 1:
                                enemya.health += thealer.heal
                                thealer.ultimate = int(thealer.heal * 0.10)
                                enemya.health = min(250, enemya.health)
                                print("After healing, " + choice3.capitalize() + "'s health is %d." % enemya.health)
                                print(choice3.capitalize() + " gained 2 passive ult charge.")
                            else:
                                thealer.ultimate = 0
                                print(choice4.capitalize() + "'s healing attempt missed.")
                                print(choice3.capitalize() + "'s health is %d." % enemya.health)
                                print(choice3.capitalize() + " gained 2 passive ult charge.")
                                print(choice4.capitalize() + " gained 2 passive ult charge.")
                    else:
                        if enemya.health >= 200:
                            thealer.mercyvar = 1
                        else:
                            randomthh6 = random.randint(1, (enemya.dodge + 3))
                            if randomthh6 == 1:
                                enemya.health += thealer.heal
                                thealer.ultimate = int(thealer.heal * 0.10)
                                enemya.health = min(200, enemya.health)
                                print("After healing, " + choice3.capitalize() + "'s health is %d." % enemya.health)
                                print(choice3.capitalize() + " gained 2 passive ult charge.")
                            else:
                                thealer.ultimate = 0
                                print(choice4.capitalize() + "'s healing attempt missed.")
                                print(choice3.capitalize() + "'s health is %d." % enemya.health)
                                print(choice3.capitalize() + " gained 2 passive ult charge.")
                                print(choice4.capitalize() + " gained 2 passive ult charge.")
            else:
                print("You missed.")
                self.ultimate = 0

    def secondary(self, enemy):
        if choice1 == 'tracer':
            hhealer.mercyvar = 1
            print(recall)
            heroa.health = max(recall)
            print("Your health has been restored to " + str(heroa.health))
        elif choice1 == 'soldier':
            counterb = 0
            if choice2 == 'mercy':
                while counterb < 1: 
                    horps = input('Do you want Mercy to Heal or Power Assist you? (H or P)? ').lower()
                    if horps == 'h':
                        hhealer.mercyvar = 1
                        randoms1 = random.randint(1, (2 + enemya.dodge))
                        if randoms1 == 1:
                            self.ultimate = int(120 * 0.10)
                            enemya.health -= 120
                            if enemya.health <= 0:
                                print(choice3 + " is dead.")
                            else:
                                if choice3 == 'reaper':
                                    if enemya.health >= 250:
                                        thealer.mercyvar = 1
                                    else:
                                        randomthh7 = random.randint(1, (enemya.dodge + 3))
                                        if randomthh7 == 1:
                                            enemya.health += thealer.heal
                                            thealer.ultimate = int(thealer.heal * 0.10)
                                            enemya.health = min(250, enemya.health)
                                            print("After healing, " + choice3.capitalize() + "'s health is %d." % enemya.health)
                                            print(choice3.capitalize() + " gained 2 passive ult charge.")
                                        else:
                                            thealer.ultimate = 0
                                            print(choice4.capitalize() + "'s healing attempt missed.")
                                            print(choice3.capitalize() + "'s health is %d." % enemya.health)
                                            print(choice3.capitalize() + " gained 2 passive ult charge.")
                                            print(choice4.capitalize() + " gained 2 passive ult charge.")
                                else:
                                    if enemya.health >= 200:
                                        thealer.mercyvar = 1
                                    else:
                                        randomthh8 = random.randint(1, (enemya.dodge + 3))
                                        if randomthh8 == 1:
                                            enemya.health += thealer.heal
                                            thealer.ultimate = int(thealer.heal * 0.10)
                                            enemya.health = min(200, enemya.health)
                                            print("After healing, " + choice3.capitalize() + "'s health is %d." % enemya.health)
                                            print(choice3.capitalize() + " gained 2 passive ult charge.")
                                        else:
                                            thealer.ultimate = 0
                                            print(choice4.capitalize() + "'s healing attempt missed.")
                                            print(choice3.capitalize() + "'s health is %d." % enemya.health)
                                            print(choice3.capitalize() + " gained 2 passive ult charge.")
                                            print(choice4.capitalize() + " gained 2 passive ult charge.")
                            counterb += 1
                        else:
                            print("You missed.")
                            self.ultimate = 0
                            counterb += 1
                    if horps == 'p':
                        hhealer.mercyvar = 0
                        randoms2 = random.randint(1, (2 + enemya.dodge))
                        if randoms2 == 1:
                            self.ultimate = int(160 * 0.13)
                            enemya.health -= 160
                            if enemya.health <= 0:
                                print(choice3 + " is dead.")
                            else:
                                if choice3 == 'reaper':
                                    enemya.health += thealer.heal
                                    thealer.ultimate = int(thealer.heal * 0.10)
                                    enemya.health = min(250, enemya.health)
                                else:
                                    enemya.health += thealer.heal
                                    thealer.ultimate = int(thealer.heal * 0.10)
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
                            thealer.ultimate = int(thealer.heal * 0.10)
                            enemya.health = min(250, enemya.health)
                        else:
                            enemya.health += thealer.heal
                            thealer.ultimate = int(thealer.heal * 0.10)
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
            hhealer.mercyvar = 1
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
                    enemya.health += thealer.heal
                    thealer.ultimate = int(thealer.heal * 0.10)
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
                    enemya.health += thealer.heal
                    thealer.ultimate = int(thealer.heal * 0.10)
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
        print(choice3.capitalize() + "'s ult charge is at %d percent." % (min(100, ulte)))
        print(choice4.capitalize() + "'s ult charge is at %d percent." % (min(100, thealult)))
        # print(choice3.capitalize() + "'s ult charge is at %d percent." % min(100, ulte))

class Talon(Attack):
    def attack(self, enemy):
        randomt = random.randint(1, (enemya.accuracy + heroa.dodge))
        if randomt == 1:
            if self.health > 0:
                self.ultimate = int(self.power * 0.10)
                heroa.health -= self.power
                print(choice3.capitalize() + " did %d damage." % self.power)
                if thealer.mercyvar == 1:
                    randomta1 = random.randint(1, (heroa.dodge + 3))
                    if randomta1 == 1:
                        thealer.ultimate = int(thealer.assist * 0.10)
                        heroa.health -= thealer.assist
                        print(choice3.capitalize() + " connected and did %d damage." % self.power)
                    if heroa.health <= 0:
                        print("You are dead.")
                        else:

                else:
                    print(choice4.capitalize() + " missed.")
                    print(choice3.capitalize() + " gained an extra %d ult charge and 2 passive charge." % self.ultimate)
                    print(choice4.capitalize() + " gained %d ult charge and 2 passive charge." % thealer.ultimate)
                else:
                    if choice3 == 'tracer':
                        if choice2 == 'mercy':
                            print(hhealer.mercyvar)
                            if hhealer.mercyvar == 1:
                                heroa.health += hhealer.heal
                                hhealer.ultimate = int(hhealer.heal * 0.10)
                                heroa.health = min(150, heroa.health)
                        else:
                            heroa.health += hhealer.heal
                            hhealer.ultimate = int(hhealer.heal * 0.10)
                            heroa.health = min(150, heroa.health)
                    else:
                        if choice2 == 'mercy':
                            if hhealer.mercyvar == 1:
                                heroa.health += hhealer.heal
                                hhealer.ultimate = int(hhealer.heal * 0.10)
                                heroa.health = min(200, heroa.health)
                        else:
                            heroa.health += hhealer.heal
                            hhealer.ultimate = int(hhealer.heal * 0.10)
                            heroa.health = min(200, heroa.health)
                    print("You gained 2 passive ult charge.")
                    print("After healing, your health is %d." % heroa.health)
                    print(choice2.capitalize() + " gained %d ult charge along with 2 passive charge." % hhealer.ultimate)
        else:
            print(choice3.capitalize() + " missed.")
            self.ultimate = 0
    
    # def secondary(self, enemy):

    # def ultabl(self, enemy):

    # def healult(self, enemy):

# self, health, power, accuracy, dodge, ultimate
tracer = Hero(150, 30, 1, 2, 0)
soldier = Hero(200, 40, 1, 1, 0)
pharah = Hero(200, 55, 2, 0, 0)
mercy = Healer(50, 0.30, 0, 0)
zen = Healer(30, 0.25, 0, 0)
reaper = Talon(250, 90, 1, 0, 0)
junkrat = Talon(200, 50, 3, 0, 0)
widow = Talon(200, 120, 3, 1, 0)
baptiste = Healer(30, 20, 0, 0)
ana = Healer(75, 70, 0, 0)

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
    print("REAPER: 250, 90, 1/1, low, high, 8, Wraith Form: cannot give or take dmg for 3 straight turns but receives healing 8 cd, Death Blossom: deals 170 dmg for 3 straight turns")
    print("JUNKRAT: 200, 50, 1/3, low, avg, 6, Steel Trap: (varied probability) acc drops to 1 for 4 straight turns 10 cd, Riptire: 600 dmg 1/2 acc")
    print("WIDOWMAKER: 200, 120 bs 200 hs, 1/3 bs 1/4 hs, high, low, 12, Grapple: rest one turn and restore health 10 cd, Infra-Sight: increase acc 1/2 bs 1/4 hs for 15 turns"), print("")
    print("SUPPORT (*Note: Enemy healers will always attack until healing is required):"), print("")
    print("BAPTISTE: +60 1/2 acc, +75 dmg 1/2 acc, Immortality Field: prevents enemy health from dropping below 20 percent for 8 turns 20 cd, Amp Matrix: dmg assist increased to 40% for 4 turns")
    print("ANA: +75 1/2 acc, +70 dmg 1/2 acc, Sleep Dart: guarantees enemy 1/1 acc for one turn 12 cd, Nano Boost: restores enemy health full, 50% dmg assist, and hero dmg reduced 50% for 8 turns")
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
cooldowne = 10
ulth = 0
healult = 0
ulte = 0
thealult = 0
while heroa.alive() and enemya.alive():
    while 1 == 1:
        ulth = min(ulth, 100)
        healult = min(healult, 100)
        my_random = random.randint(1, 5)
        print("What do you want to do?")
        print("1. primary fire")
        print("2. secondary ability")
        print("3. ultimate ability")
        print("4. check status")
        print("5. run")
        user_input = input()
        if user_input == "1":
            if choice1 == 'tracer':
                recall.append(heroa.health)
                if len(recall) > 3:
                    recall.pop(0)
                print(recall)
            heroa.attack(enemya)
            cooldownh += 1
            ulth += (2 + heroa.ultimate)
            healult += 2
            ulte += 2
            thealult += (2 + thealer.ultimate)
            break
        elif user_input == "2":
            if choice1 == 'tracer':
                recall.append(heroa.health)
                if len(recall) > 3:
                    recall.pop(0)
            if choice1 == 'tracer':
                if cooldownh < 12:
                    print("Sec ability still on cooldown.")
                else:
                    heroa.secondary(enemya)
                    cooldownh = 0
                    ulth += (2 + heroa.ultimate)
                    healult += 2
                    ulte += 2
                    thealult += (2 + thealer.ultimate)
                    break
            elif choice1 == 'soldier':
                if cooldownh < 8:
                    print("Sec ability still on cooldown.")
                else:
                    heroa.secondary(enemya)
                    cooldownh = 0
                    ulth += (2 + heroa.ultimate)
                    healult += 2
                    ulte += 2
                    thealult += (2 + thealer.ultimate)
                    break
            elif choice1 == 'pharah':
                if cooldownh < 9:
                    print("Sec ability still on cooldown.")
                else:
                    heroa.secondary(enemya)
                    cooldownh = 0
                    ulth += (2 + heroa.ultimate)
                    healult += 2
                    ulte += 2
                    thealult += (2 + thealer.ultimate)
                    break
        elif user_input == "3":
            if choice1 == 'tracer':
                recall.append(heroa.health)
                if len(recall) > 3:
                    recall.pop(0)
            if ulth == 100:
                heroa.ultabl(enemya)
                ulth = 0
                healult += 2
                ulte += 2
                thealult += (2 + thealer.ultimate)
                cooldownh += 1
                break
            else:
                print("Ultimate ability not sufficiently charged.")
        elif user_input == "4":
            heroa.print_status()
        elif user_input == "5":
            print("Goodbye.")
            heroa.health = 0
            break
        else:
            print("Invalid input %r" % user_input)

    while heroa.alive() and enemya.alive(): 
        if healult >= 100:
            while 1 == 1:
                user_input3 = input("Use heal ult? ('Y' or 'N'): ").lower()
                if user_input3 == 'y':
                    heroa.healult(enemya)
                    healult = 0
                    break
                elif user_input3 == 'n':
                    break
                else:
                    print("Invalid choice.")
        break

    while heroa.alive():
        print(choice3.capitalize() + " will now attack. Ults will be used when possible, and sec abilities will be used as appropriate.")
        user_input2 = input("Press ENTER to continue.")
        if choice3 == 'reaper':
            # if ulte == 100:
            #     enemya.ult(heroa)
            #     cooldowne += 1
            # elif enemya.health < heroa.power:
            #     if cooldowne = 8:
            #         enemya.secondary(heroa)
            #         cooldowne = 0
            if 1 == 2:
                pass
            else:
                enemya.attack(heroa)
                ulth += 2
                healult += (2 + hhealer.ultimate)
                ulte += (2 + enemya.ultimate)
                thealult += (2 + thealer.ultimate)
                cooldowne += 1
                break
        if choice3 == 'junkrat':
            # if ulte == 100:
            #     enemya.ult(heroa)
            #     cooldowne += 1
            # elif cooldowne = 10:
            #     print("Junkrat laid a trap with his turn.")
            #     cooldowne = 0
            if 1 == 2:
                pass
            else:
                enemya.attack(heroa)
                ulth += 2
                healult += (2 + hhealer.ultimate)
                ulte += (2 + enemya.ultimate)
                thealult += (2 + thealer.ultimate)
                cooldowne += 1
                break
        if choice3 == 'widowmaker':
            # if enemya.health < heroa.power:
            #     if cooldowne = 10:
            #         enemya.secondary(heroa)
            #         cooldowne = 0
            # elif ulte == 100:
            #     enemya.ult(heroa)
            #     cooldowne += 1
            if 1 == 2:
                pass
            else:
                enemya.attack(heroa)
                ulth += 2
                healult += (2 + hhealer.ultimate)
                ulte += (2 + enemya.ultimate)
                thealult += (2 + thealer.ultimate)
                cooldowne += 1
                break