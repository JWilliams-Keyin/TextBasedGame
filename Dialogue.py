# A file that contains all of the non-input text shown to the player #

import time

def startingText():
    print('It is a very distant future')
    time.sleep(2)
    print('The world has been thrown into chaos and society has fallen')
    time.sleep(2)
    print('You are a lone wanderer, trying to survive in this cruel world')
    time.sleep(3)
    print('You are extremely hungry, but you ran out of food the night before')
    time.sleep(3)
    print('You figure that it is time to get up and find something to eat')
    time.sleep(3)
    print('You have a handmade bow with 3 arrows and a machete')
    time.sleep(3)
    print('Behind your shelter is a vast forest')
    time.sleep(3)
    print('There is an abandoned grocery store a few miles away, but most of the food is inedible')
    time.sleep(3)
    print('Where will you get your food?')
    time.sleep(2)
    print('Go hunting in the forest (1)')
    print('Scavenge at the abandoned grocery store (2)')

def deerHunt():
    print('You exit your shelter, bow in hand, to go hunting')
    time.sleep(3)
    print('It took a long time, but you finally found a deer, grazing in an open part of the forest')
    time.sleep(3)
    print('It would be risky, but you could take a shot at it')
    time.sleep(3)
    print('One shot might not kill it though, so you may have to use multiple arrows')
    time.sleep(3)
    print('What will you do?')
    time.sleep(2)
    print('Shoot it in the leg, then go in for the kill (1)')
    print('Go for the neck (2)')

def legHit():
    print('You hit the deer in the leg!')
    time.sleep(2)
    print('It starts to limp away, so you take another shot and it collapses')
    time.sleep(3)
    print('You approach the deer and finally kill it with your machete')
    time.sleep(3)
    print('After butchering it for a while, you head home with some fresh meat and deer pelt')
    time.sleep(4)

def neckShot():
    print('You hold your breath as your heart races at the tought of potentially missing your shot')
    time.sleep(4)
    print('You draw your bow, pull back, and...')
    time.sleep(3)
    print('Fire!')
    time.sleep(2)

def neckHit():
    print('Yes! You hit the deer in the neck!')
    time.sleep(2)
    print('You see it fall over and have a sigh of relief')
    time.sleep(3)
    print('The shot you hit killed the deer instantly')
    time.sleep(3)
    print('After butchering it for a while, you head home with some fresh meat and deer pelt')
    time.sleep(4)

def neckMiss():
    print('No! You missed the deer!')
    time.sleep(2)
    print('It runs away into the forest')
    time.sleep(2)
    print('Feeling defeated, you decide to make your way back home to think of a new plan')
    time.sleep(3)

def huntingSuccess():
    print('Trudging through the forest, you feel yourself getting even hungrier as you think about cooking the deer')
    time.sleep(4)

def huntingFail():
    print('Trudging through the forest, you dwell on how you will get food now that your hunting attempt has failed') 
    time.sleep(4)

def enterGroceryStore():
    print('Even though it has been abandoned and likely picked clean, you hold out hope for the grocery store')
    time.sleep(4)
    print('After a long walk, you finally arrive')
    time.sleep(3)
    print('All of the windows are broken and thick green foliage has started growing on the walls')
    time.sleep(3)
    print('Thankfully, there seems to be nobody around, so you casually walk into the grocery store')
    time.sleep(3)
    print('You look around and see that there are three places to go: the aisles to your left, the clothing shop to your right, and a floral department next to the front door')
    time.sleep(6)
    print('Where will you go?')
    time.sleep(2)
    print('The aisles (1)')
    print('The clothing store (2)')
    print('The floral department1 (3)')

def aislesText():
    print('The first aisle is labelled "Cleaning Supplies", so nothing useful there')
    time.sleep(3)
    print('The next two aisles are also useless, but the aisle after that has some cans left on the shelves!')
    time.sleep(3)
    print('There are 5 cans of fruit, 6 cans of veggies, and 3 cans of tuna')
    time.sleep(3)
    print('Seems like whoever lived here left before they could gather the rest of the food')
    time.sleep(3)

def aislesRevisited():
    print('You go back to the aisle full of canned goods')
    time.sleep(3)

def aislesCanClosed():
    print('If only you had something to open one of these cans, you are so hungry that you would crack one open right now')
    time.sleep(3)

def aislesCanOpened():
    print('Since you grabbed the knife earlier, you try to open a can of fruit')
    time.sleep(3)
    print('The knife was so sharp that you could stab a hole in the can and peel off the top!')
    time.sleep(4)
    print('You quickly eat the contents of the can')
    time.sleep(2)
    print('You are no longer starving!')
    time.sleep(3)

def aislesNoBag():
    print("You don't have any bags with you, so you are only able to take a few cans")
    time.sleep(3)

def aislesBag():
    print('Since you got the bag at the old camp, you are able to take all of the cans!')
    time.sleep(3)
    print('This could definitely keep you fed for a few days at least')
    time.sleep(3)

def clothingText():
    print('You enter the clothing store and find what looks to be the remains of an old camp')
    time.sleep(3)
    print('After searching around for a bit, you find a big reusable bag!')
    time.sleep(3)

def clothingRevisited():
    print('You go back to the clothing store')
    time.sleep(3)
    print('You already took everything useful from here')
    time.sleep(3)

def floralText():
    print('Before you enter the department, you observe from the counter')
    time.sleep(3)
    print('There are many dead plants lying around in what looks to be old flower arrangements')
    time.sleep(3)
    print('When you search the drawers behind the counter, you manage to find an unusually sharp knife!')
    time.sleep(4)

def floralRevisited():
    print('You go back to the floral shop')
    time.sleep(3)
    print('Yep. The plants are still dead. Nothing left of use here')
    time.sleep(3)

def headHome():
    print('You head home')

def bagOfCans():
    print('carrying all of the cans you found')
    time.sleep(4)

def lessCans():
    print('with 3 cans of food')
    time.sleep(4)

def energized():
    print('feeling energized')
    time.sleep(4)

def starving():
    print('feeling extremely hungry')
    time.sleep(4)

def atHome():
    print('As you near your shelter, you notice people standing guard outside!')
    time.sleep(3)
    print('You quickly dart behind a nearby bush on a hill to observe')
    time.sleep(3)

def atHomeHuntingSuccess():
    print('You quietly lay down your deer meat and pelt in a bush for safe keeping')
    time.sleep(3)

def atHomeBag():
    print('You quietly lay down your bag of cans in a bush for safe keeping')
    time.sleep(3)

def atHomeCans():
    print('You take all of the cans out of your pockets and lay them in a bush for later')
    time.sleep(3)

def takeInventoryOne():
    print('You carefully peer through the leaves and see that there are three bandits standing guard outside your shelter')
    time.sleep(4)
    print('It seems these bandits are not very discrete, as you can hear loud footsteps and banging from your shelter')
    time.sleep(4)
    print("You can't make out what they are saying, but you can hear the voices of two people inside")
    time.sleep(3)
    print('You take inventory of what you have at the moment to deal with this situation')
    time.sleep(3)
    print('You have...')
    time.sleep(2)

def twoArrows():
    print('two arrows for your bow,')
    time.sleep(2)

def oneArrow():
    print('one arrow for your bow,')
    time.sleep(2)

def knife():
    print('the knife from the store,')
    time.sleep(2)

def energy():
    print('energy from the can of fruit, ')
    time.sleep(2)

def takeInventoryTwo():
    print('your machete,')
    time.sleep(2)
    print('and the knowledge of your shelter')
    time.sleep(2)
    print('What will you do?')
    time.sleep(3)

def twoArrowsChoice():
    print('Pick off two guards with your bow, then get the last one with your machete (1)')

def oneArrowChoice():
    print('Pick off one guard with your bow, then get the last two with your machete (1)')

def knifeChoice():
    print('Swiftly run in and get them all with your knife (1)')

def macheteChoice():
    print('Try with just your machete (2)')

def leaveChoice():
    print('Give up and find another shelter (3)')

def marksmanEnding():
    print('You wait until all of the guards are split up, then quickly shoot two of them, killing them instantly')
    time.sleep(4)
    print('You then sneak up to the last guard and pick him off with your machete')
    time.sleep(3)
    print('You wait until you think the coast is clear to go inside')
    time.sleep(3)
    print('As you sneak into the shelter, you can hear the two bandits in the other room, as if they are clueing up their raid')
    time.sleep(4)
    print('Quickly, you charge into the room and tackle one of the bandits, slashing them with your machete')
    time.sleep(3)
    print('Before you can get up, the other bandit takes out his knife and lands three quick slashes on your back')
    time.sleep(4)
    print('Though you are in pain, you swing the machete at the bandit and manage to finally kill him')
    time.sleep(3)
    print('It took some effort, but you managed to defend your shelter!')
    time.sleep(3)
    print('(Marksman Ending)')

def concussionEnding():
    print('You wait for the guards to separate, then pick off one of them with your bow')
    time.sleep(3)
    print('Then, you sneak behind another guard and take him out with the machete')
    time.sleep(3)
    print('You turn the corner to get the last guard when you both make eye contact')
    time.sleep(4)
    print('You try to quickly dash at him with the machete, but before you land the killing blow he manages to whack you over the head with his club')
    time.sleep(4)
    print('That hit was pretty hard, but you managed to walk out of it alive, but with your head spinning')
    time.sleep(4)
    print('Wearily, you wait until you think the coast is clear to go inside')
    time.sleep(3)
    print('As you sneak into the shelter, you can hear the two bandits in the other room, as if they are clueing up their raid')
    time.sleep(4)
    print('You charge in and attempt to slash one of them with your machete')
    time.sleep(3)
    print('But due to the hit you just took, you miss')
    time.sleep(3)
    print('The bandits quickly take out their weapons and overwhelm you')
    time.sleep(3)
    print('You perish at the hands of the bandits')
    time.sleep(3)
    print('(Concussion Ending)')

def swiftNinjaEnding():
    print('Since you are energized, you take out your knife and quietly sprint towards one of the guards, taking him out in one fell swoop')
    time.sleep(4)
    print('Then, you do the same with a second guard and finally the third')
    time.sleep(3)
    print('With the guards swiftly taken care of, you sneak into the shelter')
    time.sleep(3)
    print('As you sneak into the shelter, you can hear the two bandits in the other room, as if they are clueing up their raid')
    time.sleep(4)
    print('Quietly, you creep towards the entrance to the other room')
    time.sleep(3)
    print('Then, you lunge at the first bandit and stab him with your knife, killing him instantly')
    time.sleep(3)
    print('With your other hand, you immediately take out your machete and kill the other bandit before he even knew what was happening')
    time.sleep(4)
    print('You protected your shelter masterfully!')
    time.sleep(3)
    print('(Swift Ninja Ending)')

def starvingEnding():
    print('You take out your knife and quietly sprint towards one of the guards, taking him out in one fell swoop')
    time.sleep(4)
    print('Then, you do the same with a second guard, but you are starting to get sloppy')
    time.sleep(3)
    print('The third guard manages to get the jump on you before you can finish him off, and he beats you down')
    time.sleep(4)
    print('You perished at the hands of the bandits')
    time.sleep(3)
    print('(Starving Ending)')

def corneredEnding():
    print('When the guards are separated, you sneak up to one and take him out with your machete')
    time.sleep(3)
    print('You try to sneak to the next guard, but you find yourself surrounded!')
    time.sleep(3)
    print('You try to defend yourself, but the guards call out the other two bandits and they all start to take out their weapons')
    time.sleep(4)
    print('Four against one, you perish at the hands of the bandits')
    time.sleep(3)
    print('(Cornered Ending)')

def cowardEnding():
    print('Overwhelmed by the situation, you decide to flee and leave your shelter behind')
    time.sleep(3)
    print('(Coward Ending)')