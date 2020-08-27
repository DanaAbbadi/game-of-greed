from collections import Counter
from random import randint
from abc import abstractmethod, ABC


class GameLogic:
    @staticmethod
    def roll_dice(num=6):
        return tuple([randint(1, 6) for _ in range(num)])

    @staticmethod
    def calculate_score(dice):
        """
        dice is a tuple of integers represent the user's selected dice pulled out from current roll
        """

        if len(dice) > 6:
            raise Exception("Cheating Cheater!")

        counts = Counter(dice)

        if len(counts) == 6:
            return 1500

        if len(counts) == 3 and all(val == 2 for val in counts.values()):
            return 1500

        score = 0

        ones_used = fives_used = False

        for num in range(1, 6 + 1):

            pip_count = counts[num]

            if pip_count >= 3:

                if num == 1:

                    ones_used = True

                elif num == 5:

                    fives_used = True

                score += num * 100

                # handle 4,5,6 of a kind
                score += score * (pip_count - 3)

                # 1s are worth 10x
                if num == 1:
                    score *= 10

        if not ones_used:
            score += counts.get(1, 0) * 100

        if not fives_used:
            score += counts.get(5, 0) * 50

        return score

    @staticmethod
    def validate_keepers(roll, keepers):
        return not Counter(keepers) - Counter(roll)

    @staticmethod
    def get_scorers(dice):
        all_dice_score = GameLogic.calculate_score(dice)

        if all_dice_score == 0:
            return tuple()

        scorers = []

        for i in range(len(dice)):
            sub_roll = dice[:i] + dice[i + 1 :]
            sub_score = GameLogic.calculate_score(sub_roll)

            if sub_score != all_dice_score:
                scorers.append(dice[i])

        return tuple(scorers)

class Banker(ABC):

    def __init__(self):
        self.balance = 0
        self.shelved = 0
    
    
    def shelf(self,num):
        """
        Will temporarily store unbanked points

        Argument:
            num{int} --  is the amount of points (integer) to add to shelf.          
        """
        self.shelved +=num
        return self.shelved

    def bank(self):
        """
        Add any points on the shelf to total and reset shelf    
        """
        self.balance += self.shelved
        self.shelved = 0
        return self.balance

    def clear(self):
        self.shelved = 0