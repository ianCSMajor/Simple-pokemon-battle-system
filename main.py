import utils
numbers = [3, 1, 200, 2, 5, 100]
print(numbers)
maximum = utils.find_max(numbers)
print(maximum)
import random
from utils import party
class DiceFunctions:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second


diceRoll = DiceFunctions()
print(diceRoll.roll())

pokemon = ["Squirtle", "Charizar", "Pikachu"]
nintendo = party(pokemon)

print(f"{nintendo} is unable to battle.")

