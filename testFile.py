from Character import Character
from Character import Enemy



dave = Character("Dave", "A smelly zombie")
dave.describe()
dave.set_conversation("Hello you smelly human")
dave.talk()


Sarah = Enemy("Sarah", "Your worst nightmare")
Sarah.describe()
Sarah.set_conversation("Are you ready to fight? ")
Sarah.talk()
Sarah.set_weakness("Cheese")

print("What will you fight with? ")
fight_with = input()
Sarah.fight(fight_with)