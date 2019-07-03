# saving this personal project for later

import random

class Attack:
    def __init__(self, health, power, accuracy, dodge, escape, reload):
        self.health = health
        self.power = power
        self.accuracy = accuracy
        self.dodge = dodge
        self.escape = escape
        self.reload = reload
    def alive(self):
        if self.health <= 0:
            return False
        else:
            return True

class Healer:
    def __init__(self, heal, assist):
        self.heal = heal
        self.assist = assist

class Hero(Attack):
    def attack(self, enemy):
        if choice2 == 'mercy':
            horp = input('Do you want Mercy to Heal or Power Assist you? (H or P)?').lower()
            countera = 0
            while countera < 1: 
                if horp == 'h':
                    random1 = random.randint(1, (heroa.accuracy + enemya.dodge))
                    if random1 == 1:
                        enemya.health -= self.power
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
                            hera.health += hhealer.heal
                            print("You do %d damage." % self.power)
                            print(choice3.capitalize() + " was healed by %d." % thealer.heal)
                            print("You were healed by %d." % hhealer.heal)
                            countera += 1
                    else:
                        print("You missed.")
                        countera += 1
                elif horp == 'p':
                    random2 = random.randint(1, int(heroa.accuracy + enemya.dodge))
                    if random2 == 1:
                        enemya.health -= self.power + hhealer.assist
                        if enemya.health <= 0:
                            print(choice3 + " is dead.")
                            countera += 1
                            break
                        else:
                            enemya.health += thealer.heal
                            print("You do %d damage." % self.power)
                            print(choice3.capitalize() + " was healed by %d." % thealer.heal)
                            print("You were not healed.")
                            countera += 1
        else:
            random3 = random.randint(1, int(heroa.accuracy + enemya.dodge))
            if random3 == 1:
                enemya.health -= self.power + hhealer.assist
                if enemya.health <= 0:
                    print(choice3.capitalize() + " is dead.")
                else:
                    enemya.health += thealer.heal
                    heroa.health += hhealer.heal
                    print("You do %d damage." % self.power)
                    print(choice3.capitalize() + " was healed by %d." % thealer.heal)
                    print("You were healed by %d" % hhealer.heal)
            else:
                print("You missed.")
    def print_status(self):
        print("You have %d health, %d power, %d acc, %d dodge, %d escape, and %d shots remaining until reload." % (self.health, self.power, self.accuracy, self.dodge, self.escape, self.reload))
        print(choice3.capitalize() + " has %d health, %d power, %d acc, %d dodge, %d escape, and %d shots remaining until reload." % (enemya.health, enemya.power, enemya.accuracy, enemya.dodge, enemya.escape, enemya.reload))

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

# self, health, power, accuracy, dodge, escape, reload
tracer = Hero(150, 30, 2, 2, 3, 0)
soldier = Hero(200, 40, 2, 1, 3, 3)
pharah = Hero(200, 55, 2, 0, 2, 6)
mercy = Healer(50, 30)
zen = Healer(30, 25)
reaper = Talon(250, 90, 1, 0, 3, 8)
junkrat = Talon(200, 50, 3, 0, 2, 6)
widow = Talon(200, 120, 3, 2, 1, 12)
baptiste = Healer(30, 20)
ana = Healer(75, 70)

while 1 == 1:
    print("WELCOME TO OVERWATCH RPG"), print("")
    print("This is a 2v2 RPG featuring the heroes of Overwatch against Talon and their other enemies."), print("")
    print("HEROES"), print("")
    print("ATTACK: HP, DMG, ACC, Dodge, ESC, Reload FREQ, SEC, ULT"), print("")
    print("TRACER: 150, 30, 1/2, high, high, none, Recall: rest one turn and return to highest health in past 3 moves 12 cd, Pulse Bomb: 300 dmg 1/4 acc")
    print("SOLDIER76: 200, 40, 1/2, avg, high (returns full health), 3, Helix Rocket: 120 dmg 1/7 acc 8 cd, Visor: 1/1 acc for 6 straight turns")
    print("PHARAH: 200, 55 spl 120 dir, 1/2 spl 1/3 dir, low, avg, 6, Boop: instant kill 1/20 acc 9 cd, Barrage: 300 dmg 1/2 acc"), print("")
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
        break
    elif choice1 == 'soldier76':
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

while heroa.alive() and enemya.alive():
    print()
    my_random = random.randint(1, 5)
    print("What do you want " + choice1 + " to do?")
    print("1. primary fire")
    print("2. secondary ability")
    print("3. ultimate ability")
    print("4. check status")
    print("5. run")
    user_input = input()
    if user_input == "1":
        heroa.attack(enemya)
    elif user_input == "2":
        enemya.attack(heroa)
    elif user_input == "3":
        pass
    elif user_input == "4":
        heroa.print_status()
    elif user_input == "5":
        print("Goodbye.")
        break
    else:
        print("Invalid input %r" % user_input)