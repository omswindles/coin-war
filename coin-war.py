# Copyright (c) 2014 Elijah Whitham-Powell
# Assignment 6: coin-war.py
# Create a coin war game following the given rules. Both a random and manual input mode.
#

import random
import time



def generate_army():
    units = []
    for _ in range(5):
        units += str(random.randint(1, 2))
    return units


def display_(player):
    global army1
    global army2
    if player == 1:
        army = army1
        prisoners = prison1
    if player == 2:
        army = army2
        prisoners = prison2
    for i in range(len(army)):
        if army[i] == "1":
            print("H", end="")
        if army[i] == "2":
            print("T", end="")
    print(" ", end="")
    for i in range(len(prisoners)):
        if prisoners[i] == "1":
            print("H", end="")
        if prisoners[i] == "2":
            print("T", end="")
    print()



def battle(player1, player2):
    global prison1
    global prison2
    global army1
    global army2
    prisoners1 = prison1
    prisoners2 = prison2

    if player1[0] < player2[0]:
        player1 += player2[0] + player1[0]
        del player1[0]
        del player2[0]
        army1 = player1 + prisoners2 + prisoners1
        prison1 = []
        prison2 = []
        return "Player 1 won the battle."
    if player2[0] < player1[0]:
        player2 += player1[0] + player2[0]
        del player1[0]
        del player2[0]
        army2 = player2 + prisoners1 + prisoners2
        prison1 = []
        prison2 = []
        return "Player 2 won the battle."
    if player1[0] == player2[0]:
        prison1 += player1[0:2]
        prison2 += player2[0:2]
        del player1[0:2]
        del player2[0:2]
        return "Battle was a draw."


def battle_check():
    if not army1:
        print("Player 1 has no army. Player 2 has won the war.")
        return False
    if not army2:
        print("Player 2 has no army. Player 1 has won the war.")
        return False
    if not army1 and army2:
        prison_count1 = 0
        prison_count2 = 0
        for i in army1:
            if prison1[i] == 1:
                prison_count1 += 1
        for j in army2:
            if prison2[j] == 1:
                prison_count2 += 1
        if prison_count1 == prison_count2:
            print("No armies, the war is a DRAW?!?")
            return False
        elif prison_count1 > prison_count2:
            print("Player 1 wins! Player 2 has a lesser prisoner count.")
            return False
        elif prison_count2 > prison_count1:
            print("Player 2 Wins! Player 1 has a lesser prisoner count.")
            return False
    else:
        return True


def war():
    while battle_check():
        global current_round
        print("Round: " + str(current_round))
        time.sleep(.5)
        print("Player 1: ", end="")
        display_(1)
        print("Player 2: ", end="")
        display_(2)
        time.sleep(1)
        print("Result of Round " + str(current_round) + ": " + battle(army1, army2) + ".")
        print()
        current_round += 1
        
    else:
        print()
        print("GAME OVER!")
        print("Player 1: ", end="")
        display_(1)
        print("Player 2: ", end="")
        display_(2)
        print()
        battle_check()
    return True


def war_prep():
    global army1
    global army2
    troops1 = []
    troops2 = []
    print("Prepare for WAR!! Pick 5 troops must be 5 units long and contain either H's T's or both.")
    troops1 += str(input("Player 1 troop selection? "))
    troops2 += str(input("Player 2 troop selection? "))
    
    if not troops1:
        troops1 = generate_army()
    if not troops2:
        troops2 = generate_army()
    if len(troops1) != 5 or len(troops2) != 5:
        print("Army Selection Error: Each army must have 5 units or be left blank for random selection.")
        war_prep()
        
    index = 0  # initialize troop index for first troop conversion
    for current_troop in troops1:
        # convert troops from h or H to 1
        if current_troop == "H" or current_troop == "h":
            troops1[index] = "1"
        # convert troops from t or T to 2
        if current_troop == "T" or current_troop == "t":
            troops1[index] = "2"
        index += 1

    index = 0  # re-initialize troop index for second troop conversion
    for current_troop in troops2:
        # convert troops from h or H to 1
        if current_troop == "H" or current_troop == "h":
            troops2[index] = "1"
        # convert troops from t or T to 2
        if current_troop == "T" or current_troop == "t":
            troops2[index] = "2"
            
        index += 1  # increments index
            
    army1 = troops1
    army2 = troops2

    print("Army 1 Selection: ", end="")
    display_(1)
    print("Army 2 Selection: ", end="")
    display_(2)



army1 = []
army2 = []
prison1 = []
prison2 = []
current_round = 1  # initializes round counter
war_prep()
war()
