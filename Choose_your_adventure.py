# This is an adventure game with multiple branching paths. Type prompted numbers to play #

# Imports #

import time
from random import randint
import Dialogue
import InputValidation

# Game Loop #

i = True
while i == True:

  # Variable Definitions #

  path = int(0)
  hunt = False 
  deer = int(0) 
  hit = int(0)
  store = False 
  go_home = False 
  arrows = int(3) 
  success = int(0) 
  aislesVisited = int(0) 
  clothingVisited = int(0) 
  floralVisited = int(0) 
  bag = int(0) 
  knife = int(0) 
  department = int(0) 
  clothes = int(0) 
  floral = int(0)
  outcome = int(0) 
  plan1 = int(0)
  plan2 = int(0)
  plan3 = int(0)
  plan4 = int(0)
  retry = int(0)
  start = InputValidation.playerInput(1, 'Type 1 to start the game')

  # Start #

  if start == int(1):
    Dialogue.startingText()
    path = InputValidation.playerInput(2, 'Type the number of the path that you want to take')

  # First Choices #

  if path == int(1):
    Dialogue.deerHunt()
    deer = InputValidation.playerInput(2, 'Type the number of what you want to do')
    hunt = True
  elif path == int(2):
    Dialogue.enterGroceryStore()
    store = True

  # Hunting Path #

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

  # Grocery Store Path #

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
        j = False

    Dialogue.headHome()

    if bag == int(1):
      Dialogue.bagOfCans()
    elif knife == int(1):
      Dialogue.energized()
    
    if bag == int(0):
      Dialogue.lessCans()
    go_home = True

  # Endings #

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
      Dialogue.knifeChoice()
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

  # Restart Prompt #

  Dialogue.restart()
  retry = InputValidation.playerInput(2, '1 to retry, 2 to quit')

  if retry == int(2):
    i = False

quit()