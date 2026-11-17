# ------------------------------------------------------------------------
#
#  Function: hidden_pond
#
#  Inputs: health (integer)
#  Returns: health (integer)
#
#  Description: Player discovers a hidden pond that restores health.
#
#  Author: Yaya Edwards
#
# ------------------------------------------------------------------------
import random
def hidden_pond(health):
health = random.randint(3,8)

 print ("Hidden Pond")
 print("You found a hidden pond!")

 print(f"You gained {healing} health points.")
 return health + healing
