# TextBasedGame
This is a repo containing my simple text-based game made in Python.

Type the prompted numbers to proceed in the game

This game was originally made back in my high school computer science class, so the name of the main file is inconsistant with the names of the new files I made, which use normal naming conventions. Older builds also contain excessive comments, which I removed to make the code more readable

The first build of the game was very messy and had many lines dedicated to dialogue in the main file. Since remaking it, I put all of the dialogue in one file and called each section of dialogue using functions to try and code with object-oriented principles

The first build also had no input validation, and would crash upon a wrong input. In the remake, there is a single file that handles all inputs in a function that is called whenever the player needs to make an input. Each input requires the parameters of the number of choices for the input, and the prompt that is given to the user. This way, each input is tailored to each different scenario

This was a fun little project for me to work on, and I hope you enjoy it!