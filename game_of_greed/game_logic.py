from abc import abstractmethod, ABC
from collections import Counter
import random


class GameLogic(ABC):
    @staticmethod
    def rule(num,cmn):
        if cmn>1 :
            # print('rule>1')
            return num*100 * (cmn-2)
        else :
            # print('rule=0')
            return 0
    @staticmethod
    def testt(num,repeat):
        #(1, 5, 6, 4, 1, 5)
        result=1
        # print(num)
        if num==5:
            if repeat == 1 or repeat == 2 :
                result= repeat * 50
                # print('5 <1')
                return result
            if repeat >2:
                # print('5 >5')
                return GameLogic.rule(num,repeat)
        if num==1:
            # print("repeate for 1:",repeat)
            if repeat == 1 or repeat == 2 :
                result= repeat * 100
                # print('one case lees 1')
                return result
            if repeat >2:
                result=(repeat-2) *1000
                # print('one case')
                return result
        


    @staticmethod   
    def tryyy(data):
        common=(Counter(data).most_common())
        len_common= len(Counter(data).most_common()) 
        sum=0
        for i in range(len_common):
            num = common[i][0]
            cmn = common[i][1]
            if num != 5 and num != 1:
                # print('inside tryyy:',num)
                sum +=GameLogic.rule(num,cmn)
            else:
                # print('inside tryyy num is 1:',num)
                sum+=GameLogic.testt(num,cmn)
        # print('tryyy the rule')
        return sum
    @staticmethod
    def calculate_score(calc):
            # common=Counter(calc).most_common
            x=Counter(calc).most_common(1)[0][1]
            # y=Counter(calc).most_common()[0]
            # print(x)
            if x == 1 and len(calc)==6:
                # print('str')
                return 1500
            pairs=0
            if x == 2 and len(calc)==6:
                for i in range(3):
                    if Counter(calc).most_common()[i][1]==2:
                        pairs+=1
                if pairs==3:
                    return 1500
                else:
                     return GameLogic.tryyy(calc)
                
            else:
                return GameLogic.tryyy(calc)

class Banker(ABC):

    def __init__(self):
        self.balance = 0
        self.shelved = 0
    
    
    def shelf(self,num):
        self.shelved = +num

    def bank(self):
        self.balance += self.shelved
        self.shelved = 0
        return self.balance

    def clear(self):
        self.shelved = 0




def roll_dice(num):
    roll_dice_array=[]
    for i in range(num):
        roll_dice_array.append(random.randint(1,6))
    return tuple(roll_dice_array)


if __name__=="__main__":
    roll=roll_dice(6)
    # data=[,1,1,1,1,1]
    print('roll',roll)    
    # repeat=Counter(data).most_common()[0][1]
    # x=Counter(data).most_common()[0][1]

    # print(GameLogic.calculate_score([6,1,4,4,4,6]))
    print(GameLogic.calculate_score(roll))

    # print(Counter(roll).most_common())
    # print(GameLogic.testt(5,1))




