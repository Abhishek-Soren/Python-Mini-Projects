# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 16:30:31 2023

@author: ASUS
"""

import random
ans = ""



def draw_card(participant):
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    choice = random.choice(cards)
    participant.append(choice)



def calculate_score(participant):
    if sum(participant) == 21 and len(participant) == 2:
        return 0
    
    if 11 in participant and sum(participant) > 21:
        index_found = participant.index(11)
        participant[index_found] = 1
        
    return sum(participant)



def compare(p_score, c_score):
    if p_score > 21 and c_score > 21:
        return "You went over. You lose 😤"


    if p_score == c_score:
        return "Draw 🙃"
    elif c_score == 21:
        return "Lose, Dealer has Blackjack 😱"
    elif p_score == 21:
        return "Win with a Blackjack 😎"
    elif p_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Dealer went over. You win 😁"
    elif p_score > c_score:
        return "You win 😃"
    else:
        return "You lose 😤"



def blackjack():
    
    player_deck = []
    player_score = 0

    comp_deck = []
    comp_score = 0
    
    for i in range(2) :
        draw_card(player_deck)
        draw_card(comp_deck)
    
    is_game_over = False
    
    while not is_game_over :
            
        player_score = calculate_score(player_deck)
        comp_score = calculate_score(comp_deck)
        
        print(f"Your cards : {player_deck}. Your Score : {player_score}")
        print(f"Dealer's first card : {comp_deck[0]}")
        
        if player_score == 21 or comp_score == 21 or player_score > 21:
            is_game_over = True
            
        else :
            choice = input("Draw more cards? Type 'y' or 'n' :").lower()
            if choice == "y" :
                draw_card(player_deck)
            else:
                is_game_over = True
    
    
    while comp_score < 17 and comp_score != 21:
        draw_card(comp_deck)
        comp_score = calculate_score(comp_deck)
        
    
    print(f"\n\n\nYour Final Deck {player_deck}: . Your Final Score : {player_score}.")
    print(f"Dealer's Final Deck {comp_deck}: . Dealer's Final Score : {comp_score}.")
        
        
    print(compare(player_score, comp_score))
        


ans = "y"
while ans == "y":
    ans = input("Would you like to play BlackJack? Type 'y' or 'n' : ").lower()
    if ans == "y":
        blackjack()
    
    else :
        print ("Thank you for coming. :)")