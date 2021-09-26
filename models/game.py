import random

class Game():

    def __init__(self):
        self.players = []
       

    def add_players_to_game(self, player):
        self.players.append(player)

    def number_of_players(self):
        return len(self.players)

    def who_wins(self, player1, player2):
        if player1.choice == player2.choice:
            return "No winner, play again!"
        elif player1.choice  == "rock":
            if player2.choice == "scissors":
                return "Player1 wins by playing rock!!"
            if player2.choice == "paper":
                return "Player2 wins by playing paper!!"
        elif player1.choice  == "paper":
            if player2.choice == "scissors":
                return "Player2 wins by playing scissors!!"
            if player2.choice == "rock":
                return "Player1 wins by playing paper!!"
        elif player1.choice  == "scissors":
            if player2.choice == "rock":
                return "Player2 wins by playing rock!!"
            if player2.choice == "paper":
                return "Player1 wins by playing scissors!!"

    def computer_random():
        computer = random.choice(1,2,3)
        if computer == 1:
            return computer == "rock"
        elif computer == 2:
            return computer == "paper"
        elif computer == 3:
            return computer == "scissors"

    def computer_game(self, player, computer):
        if player.choice == computer:
            return "No winner, play again!"
        elif player.choice  == "rock":
            if computer == "scissors":
                return "Player1 wins by playing rock!!"
            if computer == "paper":
                return "Computer wins by playing paper!!"
        elif player.choice  == "paper":
            if computer == "scissors":
                return "Computer wins by playing scissors!!"
            if computer == "rock":
                return "Player1 wins by playing paper!!"
        elif player.choice  == "scissors":
            if computer == "rock":
                return "Computer wins by playing rock!!"
            if computer == "paper":
                return "Player1 wins by playing scissors!!"

        


        
        
            



