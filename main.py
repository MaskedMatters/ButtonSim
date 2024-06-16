import random
import math

def go(goal):
    points = 1
    high_score = 1
    chance = 0.01

    while high_score < goal:

        while not random.random() < chance:

            points += 1
            chance += 0.01

            high_score = max(points, high_score)
        
        print("Score: " + str(points) + ", Last Chance: " + str(chance))

        points = 1
        chance = 0.01
    
    print("Goal has been reached!")

go(50)
