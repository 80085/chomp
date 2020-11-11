import argparse

import tqdm

from chomp.game import Game
from chomp.player import Human, Computer


def train_agent(size, iterations):
    trainee = Computer()
    game = Game((trainee, Computer()), size)
    for _ in tqdm.tqdm(range(iterations)):
        game.play()
    trainee.save_policy()


def play_game(size):
    game = Game((Human(), Computer(exp_rate=0.0)), size)
    while True:
        game.play()
        if input('Play again? (y/n): ').lower() != 'y':
            break


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', choices=['play', 'train'])
    parser.add_argument('size', nargs=2, type=int, help='Size of the board. rows x columns')
    parser.add_argument('--iterations', type=int, default=10000, help='How many games to train')
    args = parser.parse_args()
    if args.mode == 'play':
        play_game(args.size)
    elif args.mode == 'train':
        train_agent(args.size, args.iterations)
