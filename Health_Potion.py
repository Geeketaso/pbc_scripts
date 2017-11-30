#health potion project

import random

health = 50

#difficulty is 1 for easy, 2 for medium 3 for hardest
difficulty = 3

potion_health = int(random.randint (25,50) / difficulty)

health = health + potion_health

print(health)



