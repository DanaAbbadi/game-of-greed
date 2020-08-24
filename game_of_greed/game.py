from game_of_greed.game_logic import Banker ,GameLogic

class Game():
    def __init__(self,roller=None):
        self.roller=roller

    
    @staticmethod
    def quitter():
        print("Welcome to Game of Greed")
        result=input("Wanna play?")
        result_lower=result.lower()
        if result_lower == "n" or result_lower =="no":
            print("OK. Maybe another time")
        return result_lower
    
    def print_roll(self,roll):
        print(','.join([str(i) for i in roll]))




    def play(self):
        round=1
        num_dice=6
        score=0
        result = Game.quitter()
        if result=="y" or result=="yes":
            print(f"Starting round {round}")
            print(f"Rolling {num_dice} dice...")
            roll=self.roller(num_dice)
            self.print_roll(roll)
            enter=input("Enter dice to keep (no spaces), or (q)uit: ")
            if enter.lower() == "q" or enter.lower()=="quit":
                print(f"Total score is {score} points")
                print("Thanks for playing. You earned 0 points")
        
            
            while enter.lower() !="q" or enter.lower() != "quit":
                if len(enter)<=6:
                    roll_list=[]
                    for i in range(len(enter)):
                        roll_list.append(int(enter[i]))
                    roll_tuple=tuple(roll_list)
                    score=GameLogic.calculate_score(roll_tuple)
                    unbank=Banker.shelf(score)
                    print(f"You have {unbank} unbanked points and {6-len(enter)} dice remaining")
                    enter=input("(r)oll again, (b)ank your points or (q)uit ")
                    if enter.lower()== "r" or enter.lower() == "roll" or enter.lower() == "b"  or enter.lower() == "bank"  or enter.lower() == "q"  or enter.lower() == "quit":


                    













