# Code to validate user inputs #

def playerInput(numChoices, prompt):
    i = True
    j = True
    while i == True:
        userInput = input(f'{prompt} ')
        try:
            int(userInput)
            if int(userInput) > int(numChoices):
                print(f'Invalid input. Please input a valid number (1 - {numChoices})')
            else:
                i = False
                return userInput
        except ValueError:
            print(f'Invalid input. Please input a valid number (1 - {numChoices})')