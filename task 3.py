import random
def roll_dice():
    sides = int(input("Enter the number of sides on the dice: "))
    rolls = int(input("Enter the number of rolls: "))
    print("Rolling the dice...")
    for i in range(rolls):
        result = random.randint(1, sides)
        print(f"Roll {i + 1}: {result}")
if __name__ == "__main__":
    roll_dice()
