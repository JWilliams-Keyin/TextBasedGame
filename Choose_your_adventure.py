# This is an adventure game with multiple branching paths #

######## Imported Functions ########
import time
from random import randint
import Dialogue
import InputValidation
####################################

i = True

while i == True:

  ######## Variables Definitions ########
  path = int(0) # Gives the user the path that they input #
  hunt = False # Triggers after first choice in hunting path, transitions to the rest of the path #
  deer = int(0) # Another variable similar to the hunt variable #
  hit = int(0) # Tracks if the user hits the deer #
  store = False # Triggers after first choice in grocery store path, transitions to the rest of the path #
  go_home = False # Triggers at the end of each path to transition to the ending #
  arrows = int(3) # Set to 3 and decreases depending on what you decide to do in the hunting path #
  success = int(0) # Variable that tracks if the player's hunt was successful or not #
  aislesVisited = int(0) # Variable that tracks if the player has visited the aisles in the store path #
  clothingVisited = int(0) # Variable that tracks if the player has visited the clothing store in the store path #
  floralVisited = int(0) # Variable that tracks if the player has visited the floral department in the store path #
  bag = int(0) # Variable that tracks if the player collected the bag in the store path #
  knife = int(0) # Variable that tracks if the player collected the knife in the store path #
  department = int(0) # Variable that sets the department that the player goes to #
  clothes = int(0) # Variables that tracks if the player went to the clothing store #
  floral = int(0) # Variable that tracks if the player went to the floral department #
  outcome = int(0) # Determines what will be said to the player at the end of the game #
  plan1 = int(0)
  plan2 = int(0)
  plan3 = int(0)
  plan4 = int(0)
  # The plan variables track which way the player can end the game #
  retry = int(0) # Variable that restarts the game #
  start = InputValidation.playerInput(1, 'Type 1 to start the game') # Variable that starts the game #
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
    store = True
  ####################################

  ######## Hunting Loop ########

  # This loop contains the code for the hunting path and stores the values of the variables affected by it towards the end. This will affect the final part of the game. #

  if hunt == True:
    if deer == int(1):
      arrows = int(1)
      Dialogue.legHit()
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
    j = True
    while j == True:
      Dialogue.groceryStoreChoices()
      department = InputValidation.playerInput(4, 'Type the number of the place you want to go to')

      if department == int(1):
        if aislesVisited == int(0):
          Dialogue.aislesText()
          aislesVisited = int(1)
        elif aislesVisited == int(1):
          Dialogue.aislesRevisited()
        
        if knife == int(0):
          Dialogue.aislesCanClosed()
        elif knife == int(1):
          Dialogue.aislesCanOpened()
        
        if bag == int(0):
          Dialogue.aislesNoBag()
        elif bag == int(1):
          Dialogue.aislesBag()
      elif department == int(2):
        if clothingVisited == int(0):
          Dialogue.clothingText()
          clothingVisited = int(1)
          bag = int(1)
        elif clothingVisited == int(1):
          Dialogue.clothingRevisited()
      elif department == int(3):
        if floralVisited == int(0):
          Dialogue.floralText()
          floralVisited = int(1)
          knife = int(1)
        elif floralVisited == int(1):
          Dialogue.floralRevisited()
      elif department == int(4):
        i = False

    Dialogue.headHome()

    if bag == int(1):
      Dialogue.bagOfCans()
    elif knife == int(1):
      Dialogue.energized()
    
    if bag == int(0):
      Dialogue.lessCans()
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

    Dialogue.atHome()

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

    Dialogue.takeInventoryTwo()

    if arrows == int(2):
      Dialogue.twoArrowsChoice()
      outcome = int(1)
    elif arrows == int(1):
      Dialogue.oneArrowChoice
      outcome = int(2)
    elif knife == int(1):
      Dialogue.knifeChoice
      outcome = int(3)
    else:
      outcome =int(4)
    
    Dialogue.macheteChoice()
    Dialogue.leaveChoice()

    if outcome == int(1):
      plan1 = InputValidation.playerInput(3, 'Type the number of the way you want to deal with the situation')
    elif outcome == int(2):
      plan2 = InputValidation.playerInput(3, 'Type the number of the way you want to deal with the situation')
    elif outcome == int(3):
      plan3 = InputValidation.playerInput(3, 'Type the number of the way you want to deal with the situation')
    elif outcome == int(4):
      plan4 = InputValidation.playerInput(3, 'Type the number of the way you want to deal with the situation')

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

  ######## Restart Prompt #########

  Dialogue.restart()
  retry = InputValidation.playerInput(2, '1 to retry, 2 to quit')

  if retry == int(2):
    i = False

quit()