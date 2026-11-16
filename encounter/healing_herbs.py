
# ------------------------------------------------------------------------
#
#  Function: healing_herbs
#
#  Inputs: health (integer)
#  Returns: health (integer)
#
#  Description: Player discovers healing herbs that restore a small
#    amount of health.
#
#  Author: Eli Tattershall
#
# ------------------------------------------------------------------------

import random

def healing_herbs(health):
    healing = random.randint(3, 8)
    print("You found some healing herbs!")
    print(f"You gained {healing} health points.")
    return health + healing
