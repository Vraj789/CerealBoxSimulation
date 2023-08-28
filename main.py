# Simulate buying happy meals at random McDonalds in the US. For each happy Meal
# you will get a prize. The goal is to determine how many happy meals you will need to
# buy before you get all 6 different prizes.
# • Each trial will give you a number that represents the number of happy meals bought
# before all 6 prizes are found. Each prize is equally likely.
# • Store each of these numbers into an array.
# • Create a histogram of this array. If done correctly it will be skewed right. (look this up)
# Extension to Level 2
# • Prizes are no longer equally likely to occur. If a restaurant is already visited the
# likelihood of getting the same prize again is 90%.
# • Assume there are 100 different restaurants and all are equally likely to be eaten at.

from random import randint
import matplotlib.pyplot as plt


prizes = [0,0,0,0,0,0]
Trip = []

def RandomPrizes():
    global prizes
    sum = 0
    trips = 0
    print(prizes)
    for i in range(0,1000):
        while 0 in prizes:
            x = randint(0, 5)
            prizes[x] += 1
            trips = trips + 1
        Trip.append(trips)
        sum = sum + Trip[i]
        trips = 0
        prizes = [0,0,0,0,0,0]
    print(Trip)
    print(sum/1000)



def usingStandardArray():
    global Trip
    plt.hist(Trip, bins=range(min(Trip), max(Trip) + 2), align="mid", color="blue", histtype='bar', ec='black')
    plt.title("Random Dice Sums")
    plt.xlabel("Num of Trips")
    plt.ylabel("Frequency")
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    # plt.legend()
    plt.show()






def main():
    RandomPrizes()
    usingStandardArray()

main()