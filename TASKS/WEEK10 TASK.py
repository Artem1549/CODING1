import random


class Dog():
    def __init__(self,sideNum, diceNum, rolledNum):
        self.sideNum = sideNum
        self.diceNum = diceNum
        self.rolledNum = rolledNum

    def calc(self):
    
        for dice in range(1, self.diceNum + 1):
         

            for rolls in range(1, self.rolledNum + 1):

                side = random.randint(1,self.sideNum)
                print("Dice number: " + str(dice) + ". Roll: " + str(rolls) + ". Rolled: " + str(side))


    

print("Enter the number of sides: ")
sideNum = int(input())
print("Enter the number of dice: ")
diceNum = int(input())
print("Enter the number of rolls: ")
rolledNum = int(input())
dice = Dog(sideNum,diceNum,rolledNum)
dice.calc()

 
