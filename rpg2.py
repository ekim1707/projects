import random

bountyhero = 0
bountymedic = 0
bountysniper = 0

breaker = 0
while breaker < 1:
    print("Bounty total: Hero = %d, Medic = %d, Sniper = %d." % (bountyhero, bountymedic, bountysniper))

    class Character:
        def __init__(self, health, power, bounty, armor, evade):
            self.health = health
            self.power = power
            self.bounty = bounty
            self.armor = armor
            self.evade = evade
        def alive(self):
            if choice2 == 'zombie':
                return True
            elif self.health <= 0:
                return False
            else:
                return True

    class Hero(Character):

        def attack(self, enemy):
            if choice2 == 'shadow':
                random1 = random.randint(1, 10)
                if random1 != 1:
                    print("You missed.")
                else:
                    random10 = random.randint(1, 10)
                    if random10 == 1:
                        villain.health -= (self.power * 2)
                        print("You do %d damage." % (self.power * 2))
                    else:
                        villain.health -= self.power
                        print("You do %d damage." % self.power)
                    if villain.health <= 0:
                        print("The " + choice2 + " is dead.")
            else:
                random2 = random.randint(1, 10)
                if random2 == 1:
                    villain.health -= (self.power * 2)
                    print("You do %d damage." % (self.power * 2))
                    if choice2 == 'zombie':
                        pass
                    elif villain.health <= 0:
                        print("The " + choice2 + " is dead.")
                else:
                    villain.health -= self.power
                    print("You do %d damage." % self.power)
                    if choice2 == 'zombie':
                        pass
                    elif villain.health <= 0:
                        print("The " + choice2 + " is dead.")
        def print_status(self):
            print("You have %d health, %d power, %d armor, and %d evade." % (self.health, self.power, self.armor, self.evade))

    class Goblin(Character):
        def attack(self, enemy):
            if self.health > 0:
                randomnum1 = random.randint(1, (heroa.evade + 1))
                if randomnum1 == 1:
                    print("You successfully dodged.")
                else:
                    heroa.health -= (self.power - heroa.armor)
                    print("The goblin does %d damage to you." % (self.power - heroa.armor))
            if heroa.health <= 0:
                print("You are dead.")
        def print_status(self):
            print("The goblin has %d health and %d power." % (self.health, self.power))

    class Medic(Character):

        def attack(self, enemy):
            if choice2 == 'shadow':
                random3 = random.randint(1, 10)
                if random3 != 1:
                    print("You missed.")
                else:
                    villain.health -= self.power
                    print("You do %d damage." % self.power)
            else:
                villain.health -= self.power
                print("You do %d damage." % self.power)
                if choice2 == 'zombie':
                    pass
                elif villain.health <= 0:
                    print("The " + choice2 + " is dead.")
            random4 = random.randint(1, 10)
            if random4 == 1:
                self.health += 2
                print("You managed to self-heal +2 hp.")
        def print_status(self):
            print("You have %d health, %d power, %d armor, and %d evade." % (self.health, self.power, self.armor, self.evade))

    class Shadow(Character):

        def attack(self, enemy):
            print("The " + choice2 + " does no damage to you.")
        def print_status(self):
            print("The shadow has %d health and %d power." % (self.health, self.power))

    class Zombie(Character):

        def attack(self, enemy):
            if self.health > 0:
                randomnum2 = random.randint(1, (heroa.evade + 1))
                if randomnum2 == 1:
                    print("You successfully dodged.")
                else:
                    heroa.health -= (self.power - heroa.armor)
                    print("The zombie does %d damage to you." % (self.power - heroa.armor))
                if heroa.health <= 0:
                    print("You are dead.")
        def print_status(self):
            print("The zombie has %d health and %d power." % (self.health, self.power))

    class Sniper(Character):

        def attack(self, enemy):
            if choice2 == 'shadow':
                random5 = random.randint(1, 10)
                if random5 != 1:
                    print("You missed.")
                else:
                    random9 = random.randint(1, 2)
                    if random9 == 1:
                        villain.health = -10
                        print("Headshot. The " + choice2 + " is dead.")
                    else:
                        villain.health -= self.power
                        print("You do %d damage." % self.power)
            else:
                random6 = random.randint(1, 5)
                if random6 == 1:
                    if choice2 == 'zombie':
                        villain.health -= 200
                        print("200 damage headshot.")
                    else:
                        villain.health = -10
                        print("Headshot. The " + choice2 + " is dead.")
                else:
                    random7 = random.randint(1, 2)
                    if random7 == 1:
                        villain.health -= self.power
                        print("You do %d damage." % self.power)
                        if choice2 == 'zombie':
                            pass
                        elif villain.health <= 0:
                            print("The" + choice2 + " is dead.")
                    else:
                        print("You missed.")
        def print_status(self):
            print("You have %d health, %d power, %d armor, and %d evade." % (self.health, self.power, self.armor, self.evade))

    class Hacker(Character):

        def attack(self, enemy):
            if self.health > 0:
                randomnum3 = random.randint(1, (heroa.evade + 1))
                if randomnum3 == 1:
                    print("You successfully dodged.")
                else:
                    heroa.health -= (self.power - heroa.armor)
                    print("The hacker does %d damage to you." % (self.power - heroa.armor))
                    random8 = random.randint(1, 3)
                    if random8 == 1:
                        print("You were also hacked! The hacker does 3 straight extra turns of damage to you (45).")
                        heroa.health -= ((self.power * 3) - heroa.armor)
                    if heroa.health <= 0:
                        print("You are dead.")
        def print_status(self):
            print("The hacker has %d health and %d power." % (self.health, self.power))

    tracer = Hero(150, 20, 0, 0, 1)
    reaper = Goblin(250, 40, 8, 0, 0)
    mercy = Medic(180, 5, 0, 0, 2)
    ashe = Shadow(1, 0, 7, 0, 0)
    roadhog = Zombie(0, 0, 10, 0, 0)
    widow = Sniper(200, 120, 0, 0, 3)
    sombra = Hacker(200, 15, 5, 0, 0)

    while 1 == 1:
        print("Hero: 150 health, 20 dmg, 0 armor, 3 evade")
        print("Medic: 180 health, 5 dmg, 0 armor, 2 evade, possible +2 self-heal when attacking")
        print("Sniper: 200 health, 120 dmg, 0 armor, 1 evade, has 1/5 chance of instakill headshot every turn")
        print("Goblin: 250 health, 40 dmg")
        print("Shadow: 1 health, 0 dmg, only takes dmg 1/10 times")
        print("Zombie: 0 health, 10 dmg, doesn't die regardless of health")
        print("Hacker: 200 health, 15 dmg, can hack you for 3 straight turns")
        print("Press ENTER to continue")
        togglebreak = input()
        break
    while 1 == 1:
        choice = input("Hero, Medic, or Sniper? ").lower()
        if choice == 'hero':
            heroa = tracer
            break
        elif choice == 'medic':
            heroa = mercy
            break
        elif choice == 'sniper':
            heroa = widow
            break
        else:
            print("Invalid choice.")
    while 1 == 1:
        choice2 = input("Goblin, Shadow, Zombie, or Hacker? ").lower()
        if choice2 == 'goblin':
            villain = reaper
            break
        elif choice2 == 'shadow':
            villain = ashe
            break
        elif choice2 == 'zombie':
            villain = roadhog
            break
        elif choice2 == 'hacker':
            villain = sombra
            break
        else:
            print("Invalid choice.")
    x = 0
    while villain.alive() and heroa.alive():
        print("What do you want to do?")
        print("1. fight the " + choice2)
        print("2. do nothing")
        print("3. check status")
        print("4. flee")
        print("5. buy item")
        user_input = input()
        if user_input == "1":
            heroa.attack(choice2)
        elif user_input == "2":
            villain.attack(choice)
        elif user_input == "3":
            heroa.print_status()
            villain.print_status()
        elif user_input == "4":
            x = 1
            print("Goodbye.")
            break
        elif user_input == "5":
            while 1 == 1:
                print("Item Inventory:")
                print('SuperTonic: 5 coins [S]')
                print('Armor: 3 coins [A]')
                print('Evade: 4 coins [E]')
                print('RedBull: 5 coins [R]')
                print('Quit: [Q]')
                itemchoice = input('Enter your choice: ').lower()
                if itemchoice == 's':
                    if choice == 'hero':
                        if (bountyhero - 5) < 0:
                            print("Not enough money.")
                        else:
                            bountyhero -= 5
                            heroa.health += 10
                            print("Health restored by 10.")
                    if choice == 'medic':
                        if (bountymedic - 5) < 0:
                            print("Not enough money.")
                        else:
                            bountymedic -= 5
                            heroa.health += 10
                            print("Health restored by 10.")
                    if choice == 'sniper':
                        if (bountysniper - 5) < 0:
                            print("Not enough money.")
                        else:
                            bountysniper -= 5
                            heroa.health += 10
                            print("Health restored by 10.")
                elif itemchoice == 'a':
                    if choice == 'hero':
                        if (bountyhero - 5) < 0:
                            print("Not enough money.")
                        else:
                            bountyhero -= 5
                            heroa.armor += 2
                            print("Armor restored by 2.")
                    if choice == 'medic':
                        if (bountymedic - 5) < 0:
                            print("Not enough money.")
                        else:
                            bountymedic -= 5
                            heroa.armor += 2
                            print("Armor restored by 2.")
                    if choice == 'sniper':
                        if (bountysniper - 5) < 0:
                            print("Not enough money.")
                        else:
                            bountysniper -= 5
                            heroa.armor += 2
                            print("Armor restored by 2.")
                elif itemchoice == 'e':
                    if choice == 'hero':
                        while 1 == 1:
                            if (bountyhero - 5) < 0:
                                print("Not enough money.")
                            elif heroa.evade == 10:
                                print("Evade attribute already full.")
                            elif heroa.evade == 9:
                                heroa.evade += 1
                            else:
                                bountyhero -= 5
                                heroa.evade += 2
                                print("Evade restored by 2.")
                                break
                    if choice == 'medic':
                        while 1 == 1:
                            if (bountymedic - 5) < 0:
                                print("Not enough money.")
                            elif heroa.evade == 10:
                                print("Evade attribute already full.")
                            elif heroa.evade == 9:
                                heroa.evade += 1
                            else:
                                bountymedic -= 5
                                heroa.evade += 2
                                print("Evade restored by 2.")
                                break
                    if choice == 'sniper':
                        while 1 == 1:
                            if (bountysniper - 5) < 0:
                                print("Not enough money.")
                            elif heroa.evade == 10:
                                print("Evade attribute already full.")
                            elif heroa.evade == 9:
                                heroa.evade += 1
                            else:
                                bountysniper -= 5
                                heroa.evade += 2
                                print("Evade restored by 2.")
                                break
                elif itemchoice == 'r':
                    if choice == 'hero':
                        if (bountyhero - 5) < 0:
                            print("Not enough money.")
                        else:
                            bountyhero -= 5
                            heroa.power += 5
                            print("Power augmented by 5.")
                    if choice == 'medic':
                        if (bountymedic - 5) < 0:
                            print("Not enough money.")
                        else:
                            bountymedic -= 5
                            heroa.power += 5
                            print("Power augmented by 5.")
                    if choice == 'sniper':
                        if (bountysniper - 5) < 0:
                            print("Not enough money.")
                        else:
                            bountysniper -= 5
                            heroa.power += 5
                            print("Power augmented by 5.")
                elif itemchoice == 'q':
                    break
                else:
                    print("Invalid choice.")
                break             
        else:
            print("Invalid input %r" % user_input)
    if x == 0:
        if choice == 'hero':
            bountyhero += villain.bounty
        elif choice == 'medic':
            bountymedic += villain.bounty
        elif choice == 'sniper':
            bountysniper += villain.bounty
    else:
        pass

    while 1 == 1:
        playagain = input("Play again? ('Y' or 'N'): ").lower()
        if playagain == 'n':
            breaker += 1
            break
        elif playagain == 'y':
            break
        else:
            print("Invalid input.")
