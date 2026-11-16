# ------------------------------------------------------------------------
#
#  Function: knight_promotion
#
#  Inputs: title (string)
#  Returns: title (string)
#
#  Description: Player may be promoted to Knight depending on a 
#    random outcome.
#
#  Author: Jon Yamamoto
#
# ------------------------------------------------------------------------

import random
import time

def knight_promotion(title):
    print("The king offers you a chance at Knight Promotion ")
    print("he asks you to show him you greatest skill")
    
    if random.randint(1, 2) == 1:
        print("You challenge the kings champion to a duel")
        time.sleep(1)
        if random.randint(1, 2) == 1:
            print("You win the duel and are promoted to Knight!")
            return "Knight"
        print("You lose the duel and are not promoted")
        return title
    else:
        print("You decide to show off your magic trick skills")
        print("The king chuckles...")
        time.sleep(1)
        print("Before he calls the gaurds to throw you out")
        return title
