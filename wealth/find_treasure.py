# ------------------------------------------------------------------------
#
#  Function: find_treasure
#
#  Inputs: gold (integer)
#  Returns: gold (integer)
#
#  Description: Player finds treasure and gains a random amount of gold.
#
#  Author: Jesse
#
# ------------------------------------------------------------------------

import random

def find_treasure(gold):
    treasure = random.randint(1, 10)

    print("You found hidden treasure! You have collected", treasure, "gold! Congrats!")

    return gold + treasure
