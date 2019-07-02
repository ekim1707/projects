# Hero RPG Game: Part 2
# You will base your game on version 7 of the game and make mods to the game.

# Characters
# make the hero generate double damage points during an attack with a probability of 20%
# make a new character called Medic that can sometimes recuperate 2 health points after being attacked with a 
# probability of 20%
# make a character called Shadow who has only 1 starting health but will only take damage about once out of every
# ten times he is attacked.
# make a Zombie character that doesn't die even if his health is below zero
# come up with at least two other characters with their individual characteristics, and implement them.
# Give each enemy a bounty. For example, the prize for defeating the Goblin is 5 coins, for the Wizard it is 6 coins.
# Items
# make a SuperTonic item to the store, it will restore the hero back to 10 health points.
# add an Armor item to the store. Buying an armor will add 2 armor points to the hero - you will add "armor" as a new
# attribute to hero. Every time the hero is attacked, the amount of hit points dealt to him will be reduced by the value
# of the armor attribute.
# add an Evade item to the store. Buying an "evade" will add 2 evade points to the hero - another new attribute on the
# Hero object. The more evade he has, the more probable that he will evade an enemy attack unscathed. For example: 2
# evade points: 10% probably of avoiding attack, 4 evade points: 15% probability of avoiding attack. It should never be 
# possible to reach 100% evasion though.
# come up with at least two other items with their unique characteristics and implement them. You can add more attributes
# to the hero or the characters.
# Bonus
# allow items to be used on the battle field. The hero can carry the items with him, and you have the option of choosing
# to use a tonic at any turn in a battle.
# make a Swap item, which when used on a battle field, will swap the power values of the two characters for one turn.
# there is a bug in the store that allows the hero to buy items even if he has no coins. Fix this bug.

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
        random1 = random.randint(1, heroa.accuracy)
        if random1 == 1:
            enemya.health -= self.power
            print("You do %d damage." % self.power)
            if enemya.health <= 0:
                print(choice3 + " is dead.")
        else:
            print("You missed.")
    def print_status(self):
        print("You have %d health and %d power." % (self.health, self.power))
    # def double_dmg(self, enemy):
    #     double_power = self.power * 2
    #     print(double_power)
    #     reaper.health -= double_power
    #     print("You do %d damage to " + choice2.capitalize() + "." % double_power)

class HHealer(Healer):
    hero.health += self.heal


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
    def print_status(self):
        print("You have %d health and %d power." % (self.health, self.power))

class THealer(Healer):

# make a character called Shadow who has only 1 starting health but will only take damage about once out of every
# ten times he is attacked.
# make a Zombie character that doesn't die even if his health is below zero
# come up with at least two other characters with their individual characteristics, and implement them.

# self, health, power, accuracy, dodge, escape, reload
tracer = Hero(150, 30, 2, 'high', 'high', 0)
soldier = Hero(200, 40, 2, 'avg', 'high', 3)
pharah = Hero(200, 55, 2, 'low', 'avg', 6)
# mercy = HHealer(50, 30)
# zen = HHealer(30, 25)
reaper = Talon(250, 90, 1, 'low', 'high', 8)
junkrat = Talon(200, 50, 3, 'low', 'avg', 6)
widow = Talon(200, 120, 3, 'high', 'low', 12)
# baptiste = THealer(30, 20)
# ana = THealer(75, 70)

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
    print("ANA: +75 1/2 acc, +70 dmg 1/2 acc, Sleep Dart: guarantees enemy 1/1 acc for one turn, Nano Boost: restores enemy health full, 50% dmg assist, and hero dmg reduced 50% for 8 turns"), print("")
    print("")
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
    print("4. run")
    user_input = input()
    if user_input == "1":
        heroa.attack(enemya)
        enemya.attack(heroa)
    elif user_input == "2":
        enemya.attack(heroa)
    elif user_input == "3":
        print(heroa.print_status)
        print(enemya.print_status)
    elif user_input == "4":
        print("Goodbye.")
        break
    else:
        print("Invalid input %r" % user_input)