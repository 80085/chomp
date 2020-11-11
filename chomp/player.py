import pickle
from abc import ABC, abstractmethod

from chomp.agent import QLearningAgent
from chomp.board import Board


class Player(ABC):

    @abstractmethod
    def choose_action(self, board: Board):
        pass

    @abstractmethod
    def end_round(self, reward: float):
        pass


class Computer(Player):

    def __init__(self, exp_rate=0.3):
        self.agent = QLearningAgent(policy=self._load_policy(), exp_rate=exp_rate)

    @staticmethod
    def _copy_board_and_get_new_hash(action, board: Board):
        new_board = board.copy()
        new_board.pick(action)
        return new_board.hash

    def choose_action(self, board: Board):
        action = self.agent.choose_action(
            board.available_actions(),
            lambda x: self._copy_board_and_get_new_hash(x, board)
        )
        board.pick(action)

    def end_round(self, reward: float):
        self.agent.end_iteration(reward)

    def save_policy(self):
        with open('policy', 'wb') as f:
            pickle.dump(self.agent.states, f)

    @staticmethod
    def _load_policy():
        try:
            with open('policy', 'rb') as f:
                return pickle.load(f)
        except FileNotFoundError:
            return None


class Human(Player):

    def choose_action(self, board: Board):
        while True:
            print(board.pretty())
            row = input('Row: ')
            col = input('Col: ')
            try:
                board.pick((int(row) - 1, int(col) - 1))
                break
            except ValueError:
                print(f'Bad action: {row, col}. Try again.')
                pass

    def end_round(self, reward: float):
        if reward == 1:
            print('Congratulations! You won!')
        else:
            print('Too bad, you lost.')
