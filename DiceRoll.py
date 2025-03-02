#DiceRoll.py
#Name: Colton Janes
#Date: 03/02/2025
#Assignment: Lab 6 - DiceRoll
import random

def main():
  #Create an empty list with possible roll values
  #Ammended below to be 11, not 12 positions as I kept getting 13 : 0 in output
  rolls = [0,0,0,0,0,0,0,0,0,0,0]
  maxRolls = 10000
  
  #Create two dice values ranging from 1 - 6 each and roll 10,000 times
  for r in range(maxRolls):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)

    #find the sum total of the two dice
    rollSum = dice1 + dice2
    rolls[rollSum - 2] = rolls[rollSum - 2] + 1

  #print statictics for dice rolls
  dice = 2
  print("Die Value : Count : Percentage of Rolls")
  for count in rolls:
    percentage = (count / maxRolls) * 100
    print(str(dice) + " : " + str(count) + " : " + str(round(percentage, 2)) + "%")
    dice = dice + 1

if __name__ == '__main__':
  main()