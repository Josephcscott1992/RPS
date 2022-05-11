import random


moves = ['rock', 'paper', 'scissors']


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class CyclePlayer(Player):
    def __init__(self):
        self.cycle = None

    def move(self):
        if self.cycle is None:
            index = 0
        else:
            index = moves.index(self.cycle)
            index = (index + 1) % len(moves)

        self.cycle = moves[index]

        return self.cycle


class HumanPlayer(Player):
    def move(self):
        result = None
        while result not in moves:
            result = str.lower(input(f"Choose your move! ({moves}) GO!:\n"))
            result = str.strip(result)
        return result


class CopyPlayer(Player):
    def __init__(self):
        self.copy = None

    def move(self):
        if self.copy is None:
            return moves[0]
        else:
            return self.copy

    def learn(self, my_move, their_move):
        self.copy = their_move


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_opponent = 0
        self.p2_you = 0

    def play_game(self):
        print("Rock, Paper, Scissors GO! \n")
        round_number = self.rounds()
        for round in range(round_number):
            print(f"\nRound {round}:")
            self.play_round()
            print()
        print("Game over!")
        self.game_winner()

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"You played {move2}.\nYour opponent played {move1}.")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        self.round_winner(move1, move2)

    def round_winner(self, move1, move2):
        p1_won_round = beats(move1, move2)
        winner = ""
        if p1_won_round:
            winner = "Opponent won the"
            self.p1_opponent += 1
        elif move1 != move2:
            winner = "You won the"
            self.p2_you += 1
        else:
            winner = "Result is a tie"
        print(f"{winner} round!")
        print(f"Current Score: Opponent: {self.p1_opponent} " +
              f"You: {self.p2_you}")

    def game_winner(self):
        print(f"\nFinal Results: Opponent: {self.p1_opponent} " +
              f"You: {self.p2_you}")
        winner = ""
        if self.p1_opponent > self.p2_you:
            winner = "Your opponent won the"
        elif self.p2_you > self.p1_opponent:
            winner = "You won the"
        else:
            winner = "Result is a tie"
        print(f"{winner} game!")

    def rounds(self):
        round_number = -1
        while round_number <= 0:
            response = input("Firstly, how many rounds would you like to "
                             "play? (1 or more): \n")
            try:
                round_number = int(response)
            except ValueError:
                round_number = -1
        return round_number


def select_opponent():
    all_opponents = [Player, RandomPlayer, CyclePlayer, CopyPlayer]
    opponent = random.choice(all_opponents)
    print(f"In this match you are playing against: {opponent.__name__}. \n"
          "Game Start!\n")
    return opponent


if __name__ == '__main__':
    opponent = select_opponent()
    game = Game(opponent(), HumanPlayer())
    game.play_game()
