
""""
Create a Game of Greed Player Bots
ONLY use public methods
- Game class constructor and play method
- DO NOT INJECT CUSTOM ROLL FUNCTION
- GameLogic, all methods available
"""
import builtins
import re
import time
# from game import Game,GameLogic 
from two_players import Game,GameLogic 


class BasePlayer:
    def __init__(self):
        self.old_print = print
        self.old_input = input
        builtins.print = self._mock_print
        builtins.input = self._mock_input
        self.total_score = 0

    def reset(self):
        builtins.print = self.old_print
        builtins.input = self.old_input
    # The default behaviour
    def _mock_print(self, *args, **kwargs):
        self.old_print(*args, **kwargs)
    def _mock_input(self, *args, **kwargs):
        return self.old_input(*args, **kwargs)
    @classmethod
    def play(cls, num_games=1):
        mega_total = 0
        for i in range(num_games):
            player = cls()
            game = Game() # doesn't pass a mock roller
            try:
                game.play()
            except SystemExit:
                # in game system exit is fine
                # because that's how they quit.
                pass
            mega_total += player.total_score
            player.reset()
        print(
            f"{num_games} games (maybe) played with average score of {mega_total // num_games}"
        )
class Ali(BasePlayer):
    def _mock_input(self, *args, **kwargs):
        return "n"
class NervousNellie(BasePlayer):
    def __init__(self):
        super().__init__()
        self.roll = None
    def _mock_print(self, *args, **kwargs):
        first_arg = args[0]
        first_char = first_arg[0]
        if first_char.isdigit():
            self.roll = tuple(int(char) for char in first_arg.split(","))
        elif first_arg.startswith("Thanks for playing."):
            self.total_score = int(re.findall(r"\d+", first_arg)[0])
        self.old_print(first_arg)
    def _mock_input(self, *args, **kwargs):
        prompt = args[0]
        if prompt.startswith("Wanna play?"):
            # self.old_print(prompt, 'y')
            return "y"
        elif prompt.startswith("Enter dice to keep (no spaces), or (q)uit:"):
            scorers = GameLogic.get_scorers(self.roll)
            keepers = "".join([str(ch) for ch in scorers])
            self.old_print(prompt, keepers)
            return keepers
        elif prompt.startswith("(r)oll again, (b)ank your points or (q)uit "):
            return "b"
        else:
            raise ValueError(f"Unrecognized prompt {prompt}")

class Mr_angry(BasePlayer):
    def __init__(self):
        super().__init__()
        self.roll = None
    def _mock_print(self, *args, **kwargs):
        first_arg = args[0]
        first_char = first_arg[0]
        if first_char.isdigit():
            self.roll = tuple(int(char) for char in first_arg.split(","))
        elif first_arg.startswith("Thanks for playing."):
            self.total_score = int(re.findall(r"\d+", first_arg)[0])
        self.old_print(first_arg)
    def _mock_input(self, *args, **kwargs):
        prompt = args[0]
        if prompt.startswith("Wanna play?"):
            # self.old_print(prompt, 'y')
            return "y"
        elif prompt.startswith("Enter dice to keep (no spaces), or (q)uit:"):
            scorers = GameLogic.get_scorers(self.roll)
            keepers = "".join([str(ch) for ch in scorers])
            self.old_print(prompt, keepers)
            return keepers
        elif prompt.startswith("(r)oll again, (b)ank your points or (q)uit "):
            scorers = GameLogic.get_scorers(self.roll)
            keepers = "".join([str(ch) for ch in scorers])
            if len(keepers)>=4:
                self.old_print(prompt, 'b')
                return "b"
            else:
                self.old_print(prompt, 'r')
                return "r"

        else:
            raise ValueError(f"Unrecognized prompt {prompt}")
if __name__ == "__main__":
        # Ali.play(20)
        # NervousNellie.play(100)
        # Mr_angry.play(1)
        game = Game()
        # while True:
        print(" 🎲 Welcome to Game of Greed 🎲 ")
        time.sleep(1)
        my_name = input('Please enter your name: ')
        print('Choose your opponent: ')
        print('Nervous Nellie    Enter 1')
        print('Mr.Angry          Enter 2')
        against = int(input())
        bot = 'Nervous Nellie' if against == 1 else 'Mr.Angry'
        print("  Who ever reaches 1000 first wins  ")
        print(" 🎲 Let the hunger games BEGIN!!🎲 ")

        while not Game.winning:
            time.sleep(1)

        # for i in range(3):
            print('***********************************************************************')
            # print('Game.winning: ', Game.winning)
            # print('*************************************************************************')
            # print('*******Starting the Round************')
            time.sleep(1)
            print(f'*************************** it\'s {my_name} Turn ***************************')
            if not Game.winning:
                    game.play()
                    # NervousNellie.play(1)
            time.sleep(1)
            print(f'**************************  it\'s {bot} Turn ********************************')

            if not Game.winning:
                if against == 2:
                    Mr_angry.play(1)
                else:
                    NervousNellie.play(1)
            
            print('Done this round')



