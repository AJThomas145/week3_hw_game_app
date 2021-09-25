from models.player import Player
from models.game import *
from flask import render_template, request, redirect
from app import app


@app.route("/home")
def index():
    return render_template("index.html", title="Home")

@app.route("/home/<player1pick>/<player2pick>")
def play_game(player1pick, player2pick):
    player_1 = Player("Player1", player1pick)
    player_2 = Player("Player2", player2pick)
    game = Game()
    winner = game.who_wins(player_1, player_2)
    return render_template("winner.html", title="winner", winner=winner )