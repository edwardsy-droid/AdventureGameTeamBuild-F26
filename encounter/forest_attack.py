# ------------------------------------------------------------------------
#
#  Function: forest_attack
#
#  Inputs: health (integer)
#  Returns: health (integer)
#
#  Description: Player is attacked by wolves and loses a random amount 
#  of health.
#
#  Author: John Hook
#
# ------------------------------------------------------------------------

import random
import time

def forest_attack(health):

    damage_dealt = random.randint(5, 10)

    print("You are walking through the forest, wary because there are dangers...")

    time.sleep(3)

    print("You hear rustling")

    time.sleep(1)

    print("*rustle*")

    time.sleep(1)
    
    print("*rustle rustle*")

    time.sleep(5)
    
    print("*LOUDER RUSTLING*")

    time.sleep(1)

    print(f'You are attacked suddenly by {random.randint(2, 5)} wolves, dealing {damage_dealt} damage.')

    return health-damage_dealt
