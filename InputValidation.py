# Code to validate user inputs #

def validate(numChoices, userInput):
    loop = True
    while loop == True:
        if 0 < int(userInput) <= numChoices:
            loop == False
            return userInput
        elif int(userInput) == ValueError:
            userInput == input(f'Please enter a valid number (1 - {numChoices}) ')
        else:
            userInput == input(f'Please enter a valid number (1 - {numChoices}) ')