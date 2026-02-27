# Code to validate user inputs #

def playerInput(numChoices, prompt):
    loop = True
    while loop == True:
        try:
            userInput = int(input(f'{prompt} '))
            loop = False
            return userInput
        except ValueError:
            print(f'Invalid input. Please input a valid number (1 - {numChoices})')
        except 0 < int(userInput) < int(numChoices):
            print(f'Invalid input. Please input a valid number (1 - {numChoices})')
