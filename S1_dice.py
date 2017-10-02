# -*- coding: utf-8 -*-
"""
Created on Fri Sep 08 08:23:24 2017

@author: dupres
"""

import random
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def dice_game():
    p1_score = 0
    p2_score = 0
    gamble = 0
    dice = 0
    print("Welcome to Dice game !")

    gamemode = raw_input("What mode would you like to play ?\nWrite 's' to play against IA\nWrite 'm' to play against another player\nMode : ")
    if gamemode == 's':      
        while p1_score < 100 and p2_score < 100:
            cls()
            gamble = 0
            print("\nP1 : "+str(p1_score))
            print("P2 : "+str(p2_score))
            print("Player 1 turn !"+"\n")
            print("Gamble : "+str(gamble))
            dice = roll()
            while dice!=1:
                gamble = gamble + dice
                if raw_input("Would you like to roll again ?\nGamble : "+str(gamble)+"\ny or n : ") =="y" :
                    dice = roll()
                else:
                    p1_score = gamble + p1_score
                    dice = 1
            gamble = 1
            p1_score = gamble + p1_score
            print("Too bad !\n")
            
            gamble = 0
            print("\nP1 : "+str(+p1_score))
            print("P2 : "+str(p2_score))
            print("Gamble : "+str(gamble))
            print("Player 1 turn !"+"\n")
            roll()
            while dice<>1:
                gamble = dice + gamble
                if random.randint(1,3) > 1 :
                    dice = roll()
                else:
                    p2_score = gamble + p2_score
                    dice = 1
            gamble = 1
            p2_score += gamble
            print("Too bad !\n")
        
        cls()
        if p1_score > p2_score :
            print("Player 1 wins !")
        else :
            print("Player 2 wins !")
        print("\nP1 : "+str(p1_score)+"\n")
        print("P2 : "+str(p2_score)+"\n")
    else:
        print("\nMulti")
        print(gamemode)
        
        
def roll():
    dice = random.randint(1,6)
    print(dice)
    return dice

#----------------------------------------------------------------------
dice_game()