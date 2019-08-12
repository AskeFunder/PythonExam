import time as t
from deck import Deck
from card import Card
from player import Player
from ai import AI
from game import Game

if __name__ == "__main__":
    game = Game.create_game()

    with game.player as p:
        with game.ai as ai:
            while p.money > 0:
                if game.placed_bet != None:
                    game.clear_bet()

                game.prepare_round()
                game.ai_busted = False
                game.player_busted = False
                print("Start of round: Player busted = {}, AI busted = {}".format(game.player_busted, game.ai_busted))

                game.show_hands_hidden()#print("Your hand: {} {}   AI hand: {} {}".format(p.show_hand(), p.calc_hand(), ai.show_hand(), ai.calc_hand_hidden()))
                game.take_bet(game.player)

                
                while True:
                    print("Your money: {}$   Your bet: {}$".format(p.money, game.placed_bet))
                    game.show_hands_hidden()#print("Your hand: {} {}   AI hand: {} {}".format(p.show_hand(), p.calc_hand(), ai.show_hand(), ai.calc_hand_hidden()))
                    print()
                    inp = input("Would you like to draw another card? Y/N  ")
                    print()

                    inp = str.lower(inp)
                    
                    if inp == "y":
                        if not p.draw_card(game.deck):
                            game.player_busted = True
                            
                            print()
                            game.show_hands()
                            print("{} were busted".format(p.name))
                            print("{} lost {}$".format(p.name, game.placed_bet))
                            #print("Your hand: {} {}   AI hand: {} {}".format(p.show_hand(), p.calc_hand(), ai.show_hand(), ai.calc_hand_hidden()))
                            print()
                            break
                    elif inp == "n":
                        print("Start of round: Player busted = {}, AI busted = {}".format(game.player_busted, game.ai_busted))
                        break
                        

                    if not game.player_busted:
                        if ai.calc_hand() < 16:
                            if not ai.draw_card(game.deck):
                                game.ai_busted = True
                                print()
                                print("{} were busted".format(ai.name))
                                game.show_hands()#print("Your hand: {} {}   AI hand: {} {}".format(p.show_hand(), p.calc_hand(), ai.show_hand(), ai.calc_hand_hidden()))
                                print("You win {}$".format(game.placed_bet))
                                p.money += (game.placed_bet * 2)

                                print()
                                break
                
                if not game.player_busted:
                    while ai.calc_hand() < 16:
                        if not ai.draw_card(game.deck):
                            game.ai_busted = True
                            print()
                            game.show_hands()#print("Your hand: {} {}   AI hand: {} {}".format(p.show_hand(), p.calc_hand(), ai.show_hand(), ai.calc_hand_hidden()))
                            print("{} were busted".format(ai.name))
                            print("You win {}$".format(game.placed_bet))
                            print()
                            p.money += (game.placed_bet * 2)

                            break
                        t.sleep(0.5)

                if game.ai_busted != True and game.player_busted != True:
                    print("No one was busted")
                    if p.calc_hand() > ai.calc_hand() and p.calc_hand() < 22 and ai.calc_hand() < 22:
                        print("{} wins {}$".format(p.name, (game.placed_bet * 2)))
                        game.show_hands()
                        print()
                        p.money += (game.placed_bet * 2)
                    else:
                        print("{} wins".format(ai.name))
                        game.show_hands()
                        print("You lose {}$".format(game.placed_bet))
                        print()

                print("End: Player busted = {}, AI busted = {}".format(game.player_busted, game.ai_busted))
                print("New game begins in 5 seconds")
                print()
                t.sleep(5)

        


        