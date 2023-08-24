#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 16:08:17 2023

@author: Potato
"""

import random

art = '''
  ________                               ________                       
 /  _____/ __ __  ____   ______ ______  /  _____/_____    _____   ____  
/   \  ___|  |  _/ __ \ /  ___//  ___/ /   \  ___\__  \  /     \_/ __ \ 
\    \_\  |  |  \  ___/ \___ \ \___ \  \    \_\  \/ __ \|  Y Y  \  ___/ 
 \______  |____/ \___  /____  /____  >  \______  (____  |__|_|  /\___  >
        \/           \/     \/     \/          \/     \/      \/     \/ 
'''

print(art)

print ("---Welcome to the GUESSING GAME--- ")

COMP_NUM = random.randint(1, 100)
user_num = 0

print(f"Comp guess : {COMP_NUM}")

difficulty = input("\nChoose difficulty : 'hard' or 'easy' : ").lower()
count = 0

if difficulty == "hard" :
    count = 5
    
elif difficulty == "easy" :
    count = 10
    
else :
    print("Wrong answer")
    
    

def compare_num (num, diff) :
    if(diff == 0):
        print("\n\nSorry You are out of moves. ")
        print("You LOSE. ")
        print(f"Computer guess : {COMP_NUM}")
        return
    
    num = int(input ("\nEnter your guess : "))
    
    if num > COMP_NUM :
        print("Too High")
        print("Guess Again")
        compare_num(num, diff-1)
        
    elif num < COMP_NUM :
        print("Too low")
        print("Guess Again")
        compare_num(num, diff-1)
        
    else:
        print("\n\nCongratulations. You WIN. ")
        print(f"Your guess : {num}, Computer guess : {COMP_NUM}")
        return
    
    

compare_num(user_num, count)


