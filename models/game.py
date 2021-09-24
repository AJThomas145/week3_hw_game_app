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
                return "Player1 is the winner!!"
            if player2.choice == "paper":
                return "Player2 is the winner!!"
        elif player1.choice  == "paper":
            if player2.choice == "scissors":
                return "Player2 is the winner!!"
            if player2.choice == "rock":
                return "Player1 is the winner!!"
        elif player1.choice  == "scissors":
            if player2.choice == "rock":
                return "Player2 is the winner!!"
            if player2.choice == "paper":
                return "Player1 is the winner!!"

        
        
            



