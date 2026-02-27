# This is an adventure game with multiple branching paths #

print('WARNING: DO NOT PRESS ENTER UNTIL A NUMBER IS TYPED. DO NOT INPUT ANY NUMBERS THAT ARE NOT PROMPTED, AS THE GAME WILL CRASH')

######## Imported Functions ########
import time
from random import randint
import Dialogue
import InputValidation
####################################

######## Variables Definitions ########
path = int(0) # Gives the user the path that they input #
hunt = False # Triggers after first choice in hunting path, transitions to the rest of the path #
deer = int(0) # Another variable similar to the hunt variable #
hit = int(0) # Tracks if the user hits the deer #
store = False # Triggers after first choice in grocery store path, transitions to the rest of the path #
go_home = False # Triggers at the end of each path to transition to the ending #
hungry = int(0) # Variable that tracks if the user ate food in the store path #
arrows = int(3) # Set to 3 and decreases depending on what you decide to do in the hunting path #
success = int(0) # Variable that tracks if the player's hunt was successful or not #
visited = int(0) # Variable that tracks if the player has visited a department1 in the store path #
bag = int(0) # Variable that tracks if the player collected the bag in the store path #
knife = int(0) # Variable that tracks if the layer collected the knife in the store path #
department1 = int(0) # Variable that sets the first department1 that the player goes to #
department2 = int(0) # Variable that sets the second department1 the player wants to do to #
clothes = int(0) # Variables that tracks if the player went to the clothing store #
floral = int(0) # Variable that tracks if the player went to the floral department1 #
outcome = int(0) # Determines what will be said to the player at the end of the game #
plan1 = int(0)
plan2 = int(0)
plan3 = int(0)
plan4 = int(0)
# The plan variables track which way the player can end the game #
retry = int(0) # Variable that restarts the game #
start = int(input('Type 1 to start the game ')) # Variable that starts the game #
#######################################

######## Beginning Loop ########

# This loop starts the game once the user presses 1 #
# It also contains the code for choosing a path #

if start == int(1):
  Dialogue.startingText()
  path = InputValidation.playerInput(2, 'Type the number of the path that you want to take')
################################

######## First Choices Loop ########

# This loop contains all of the first choices for each path #

if path == int(1):
  Dialogue.deerHunt()
  deer = InputValidation.playerInput(2, 'Type the number of what you want to do')
  hunt = True
elif path == int(2):
  Dialogue.enterGroceryStore()
  department1 = InputValidation.playerInput(3, 'Type the number of the place you want to go to')
  store = True
####################################

######## Hunting Loop ########

# This loop contains the code for the hunting path and stores the values of the variables affected by it towards the end. This will affect the final part of the game. #

if hunt == True:
  if deer == int(1):
    arrows = int(1)
    Dialogue.legHit
    go_home = True
    success = int(1)
  elif deer == int(2):
    arrows = 2
    Dialogue.neckShot()
    hit = randint(1, 2)
    time.sleep(2)
    if hit == int(1):
      Dialogue.neckHit()
      go_home = True 
      success = int(1)
    elif hit == int(2):
      Dialogue.neckMiss()
      go_home = True
      success = int(2)
##############################

######## Grocery Store Loop ########

# This loop contains all of the code for the grocery store path and the values of the variables affected by it in the end #

if store == True:
  if department1 == int(2):
    print('Since nobody else is here, you think that you may as well look around a bit')
    time.sleep(3)
    print('You enter the clothing store and find what looks to be the remains of an old camp')
    time.sleep(3)
    print('After searching around for a bit, you find a big reusable bag!')
    clothes = 1
    bag = int(1)
    time.sleep(3)
  elif department1 == int(3):
    print('Since nobody else is here, you think you may as well look around a bit')
    time.sleep(3)
    print('Before you enter the department, you observe from the counter')
    time.sleep(3)
    print('There are many dead plants lying around in what looks to be old flower arrangements')
    time.sleep(3)
    print('Then, you notice a small plaque on the wall. It reads:')
    time.sleep(3)
    print('"Community Votes 2020 Platinum Winner, Best Florists and Flower Shops"')
    time.sleep(3)
    print('Huh. Whoever ran this floral department must have done a really good job')
    time.sleep(3)
    print('When you search the drawers behind the counter, you manage to find an unusually sharp knife!')
    floral = int(1)
    knife = int(1)
    time.sleep(4)
  
  if clothes == int(1):
    print('Where will you go now?')
    time.sleep(3)
    print('The aisles (1)')
    print('The floral department (3)')
    department2 = int(input('Type the number of the place you want to go to '))
  elif floral == int(1):
    print('Where will you go now?')
    time.sleep(3)
    print('The aisles (1)')
    print('The clothing store (2)')
    department2 = int(input('Type the number of the place you want to go to '))

  if department2 == int(2):
    print('You enter the clothing store and find what looks to be the remains of an old camp')
    time.sleep(3)
    print('After searching around for a bit, you find a big reusable bag!')
    bag = int(1)
    visited = int(1)
    time.sleep(3)
  elif department2 == int(3):
    print('Before you enter the department, you observe from the counter')
    time.sleep(3)
    print('There are many dead plants lying around in what looks to be old flower arrangements')
    time.sleep(3)
    print('Then, you notice a small plaque on the wall. It reads:')
    time.sleep(3)
    print('"Community Votes 2020 Platinum Winner, Best Florists and Flower Shops"')
    time.sleep(3)
    print('Huh. Whoever ran this floral department must have done a really good job')
    time.sleep(3)
    print('When you search the drawers behind the counter, you manage to find an unusually sharp knife!')
    knife = int(1)
    visited = int(1)
    time.sleep(4)

  if visited == int(1):
    print('Now that you have searched the other two departments, you decide to search the aisles')
    department1 = int(1)
    time.sleep(4)

  if department1 == int(1):
    print('The first aisle is labelled "Cleaning Supplies", so nothing useful there')
    time.sleep(3)
    print('The next two aisles are also useless, but the aisle after that has some cans left on the shelves!')
    time.sleep(3)
    print('There are 5 cans of fruit, 6 cans of veggies, and 3 cans of tuna')
    time.sleep(3)
    print('Seems like whoever lived here left before they could gather the rest of the food')
    time.sleep(3)
  elif department2 == int(1):
    print('The first aisle is labelled "Cleaning Supplies", so nothing useful there')
    time.sleep(3)
    print('The next two aisles are also useless, but the aisle after that has some cans left on the shelves!')
    time.sleep(3)
    print('There are 5 cans of fruit, 6 cans of veggies, and 3 cans of tuna')
    time.sleep(3)
    print('Seems like whoever lived here left before they could gather the rest of the food')
    time.sleep(3)

  if knife == int(1):
    print('Since you grabbed the knife earlier, you try to open a can of fruit')
    time.sleep(3)
    print('The knife was so sharp that you could stab a hole in the can and peel off the top!')
    time.sleep(4)
    print('You quickly eat the contents of the can')
    time.sleep(2)
    hungry = int(1)
    print('You are no longer starving!')
    time.sleep(3)
  else:
    print('If only you had something to open one of these cans, you are so hungry that you would crack one open right now')
    time.sleep(4)

  if bag == int(1):
    print('Since you got the bag at the old camp, you are able to take all of the cans!')
    time.sleep(3)
    print('This could definetly keep you fed for a few days at least')
    time.sleep(3)
  else:
    print("You don't have any bags with you, so you are only able to take two of each can")
    time.sleep(3)

  print('You head home')

  if bag == int(1):
    print('carrying all of the cans you found')
    time.sleep(4)
  elif knife == int(1):
    print('feeling energized')
    time.sleep(4)
  
  if bag == int(0):
    print('with 6 cans of food')
    time.sleep(4)
  go_home = True
####################################

######## Ending Loops ########

# This section contains the code for the end of the game, which is switched up depending on which path you take #

if go_home == True:
  Dialogue.longDay()
 
  if success == int(1):
    Dialogue.huntingSuccess()
  elif success == int(2):
    Dialogue.huntingFail()

  Dialogue.atHome

  if success == int(1):
    Dialogue.atHomeHuntingSuccess()
  elif bag == int(1):
    Dialogue.atHomeBag()
  elif bag == int(0):
    Dialogue.atHomeCans()

  Dialogue.takeInventoryOne()
  
  if arrows == int(2):
    Dialogue.twoArrows()
  elif arrows == int(1):
    Dialogue.oneArrow()
  elif knife == int(1):
    Dialogue.knife()
  elif hungry == int(1):
    Dialogue.energy()

  Dialogue.takeInventoryTwo()

  if arrows == int(2):
    Dialogue.twoArrowsChoice()
    outcome = int(1)
  elif arrows == int(1):
    Dialogue.oneArrowChoice
    outcome = int(2)
  elif hungry == int(1):
    Dialogue.knifeChoice
    outcome = int(3)
  else:
    outcome =int(4)
  
  Dialogue.macheteChoice()
  Dialogue.leaveChoice()

  if outcome == int(1):
    plan1 = int(input('Type the number of the way you want to deal with the situation '))
  elif outcome == int(2):
    plan2 = int(input('Type the number of the way you want to deal with the situation '))
  elif outcome == int(3):
    plan3 = int(input('Type the number of the way you want to deal with the situation '))
  elif outcome == int(4):
    plan4 = int(input('Type the number of the way you want to deal with the situation '))

  # Ending 1 #
  if plan1 == int(1):
    Dialogue.marksmanEnding()
  # Ending 2 #
  elif plan2 == int(1):
    Dialogue.concussionEnding()
  # Ending 3 #
  elif plan3 == int(1):
    Dialogue.swiftNinjaEnding()
  # Ending 4 #
  elif plan1 == int(2):
    Dialogue.corneredEnding()
  elif plan2 == int(2):
    Dialogue.corneredEnding()
  elif plan3 == int(2):
    Dialogue.corneredEnding()
  elif plan4 == int(2):
    Dialogue.corneredEnding()
  # Ending 5 #
  elif plan1 == int(3):
    Dialogue.cowardEnding()
  elif plan2 == int(3):
    Dialogue.cowardEnding()
  elif plan3 == int(3):
    Dialogue.cowardEnding()
  elif plan4 == int(3):
    Dialogue.cowardEnding()

##############################

quit()