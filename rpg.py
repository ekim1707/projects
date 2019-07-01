# Hero RPG 1
# Grade: N/A
# View Grade Information. Opens a dialogue
# RPG Game 1
# Take the RPG game and rewrite it using objects.

# Fork Hero RPG Starting Template

# As you complete each step, commit, push, and tag the final working version. In the future we'll base a refactor off 
# of one the steps.

# Step 1
# Make a Hero class to store the health and power of the hero, and make a Goblin class to store the health and power 
# of the goblin. Use a hero object in place of the variables hero_health and hero_power and use a goblin object in place
# of the variables goblin_health and goblin_powerall through out the app.

class Hero:
    def __init__(self, health, power):
        self.health = health
        self.power = power

# Step 2
# Take the code for the hero attacking the goblin and extract it into a method (call it attack) of the Hero class. 
# Replace the existing code with a call to the attack method. Hint: attack should take in the goblin (enemy) as a 
# parameter: hero.attack(goblin)

    def attack(self, enemy):

class Goblin:
    def __init__(self, health, power):
        self.health = health
        self.power = power

# Step 3
# Similarly, take the code for the goblin attacking the hero and extract it into a method (also call it attack) of 
# the Goblin class. Replace the existing code with a call to the attack method. It should look like goblin.attack(hero).

    def attack(self, enemy):

# Step 4
# Refactor the while condition:

# while goblin.health > 0 and hero.health > 0:
# to

# while goblin.alive() and hero.alive():
# The health checks should be moved to within the alive methods of Hero and Goblin respectively.

# Step 5
# Take the code for printing the health status of the hero and move it into a method called print_status of Hero. Do the
# same for the goblin.

# Step 6
# Do you see a lot of duplicated or similar code between Hero and Goblin? What if you can share the duplicated code 
# between them? You can by using inheritance! Create a new class called Characterand make both Hero and Goblin inherit 
# from it.

# Step 7
# The alive methods on Hero and Goblin should be identical. Move it into Character, and remove them from Hero and 
# Goblin - now they can simply inherit it from Character.

# Step 7: Bonus Challenge
# The methods attack and print_status method in Hero and Goblin look almost identical, but not quite. Is it possible to 
# move them into the Character class as well? Give it a try.

# Step 8: Bonus Challenge 2
# Create a zombie character that cannot die and have it fight the hero instead of the goblin.