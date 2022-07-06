import random
class Dice:
    def roll(self):
        list = (random.randint(1,6) , random.randint(1,6))
        print(list)

dice = Dice()
dice.roll()