from abc import abstractmethod, ABC
from collections import Counter
import random


class GameLogic(ABC):

    @staticmethod
    def roll_dice(num):
        """
        Rolls the dice num times

        Arguments:
            num {integer} -- how many times to roll the dice
        
        Output:
            Returns a tuple of length num

        """
        try:
            roll_dice_array=[]
            for i in range(num):
                roll_dice_array.append(random.randint(1,6))
            return tuple(roll_dice_array)
        except Exception as error:
            print(f'this is error in roll dice method {error}')

  
    @staticmethod
    def calculate_score(calc):
        """
        Returns an integer representing the roll’s score according to rules of game.

        Arguments:
            calc {tuple} -- is a tuple of integers that represent a dice roll.
        
        Output:
            Returns the score according to rules of the game

        """
        try:
            x = Counter(calc).most_common()

            #Empty
            if len(calc) == 0:
                return 0

            #straight case (1,2,3,4,5,6)    
            if x[0][1] == 1 and len(calc) == 6:
                return 1500

            #pairs
            pairs=0
            if len(calc) == 6 and len(Counter(calc).most_common())==3:
                for i in range(3):
                    if Counter(calc).most_common()[i][1]==2:
                        pairs+=1
            if pairs==3:
                return 1500


            else:
                common=(Counter(calc).most_common())
                len_common= len(Counter(calc).most_common()) 
                sum=0
                
                for i in range(len_common):
                    num = common[i][0]
                    cmn = common[i][1]
                    base=num*100

                    # The case for ones
                    if num ==1:
                        if cmn >2 :
                            base = num*1000
                        else: 
                            sum+= base * (cmn)
                    # The case for 5
                    if num ==5:
                        if cmn < 3 :
                            sum+= num*10 *cmn
                    # The general formula   
                    if cmn>1 :
                        sum += base * (cmn-2)    
                    
                return sum
        except Exception as error:
                print(f'this is error in roll dice method {error}')
                
            

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






if __name__=="__main__":
    roll = GameLogic.roll_dice(6)
    print('roll',roll)    
    print(GameLogic.calculate_score(roll))





