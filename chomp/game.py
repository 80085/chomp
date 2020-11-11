import itertools
import random

from chomp.board import Board


class Game:
    def __init__(self, players, size):
        self.players = [*players]
        self.size = size

    def play(self):
        board = Board(*self.size)
        random.shuffle(self.players)
        players = itertools.cycle(self.players)
        current_player = None
        while not board.ended:
            current_player = next(players)
            current_player.choose_action(board)
        current_player.end_round(0)
        next(players).end_round(1)
