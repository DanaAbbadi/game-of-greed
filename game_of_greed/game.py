from game_logic import Banker ,GameLogic

class Game():

    new_game=Banker()
    num_dice=6
    result=""
    round=1

    def __init__(self,roller=None):
        self.roller=roller or GameLogic.roll_dice

        
    def arguments_reset():
        Game.new_game.shelved=0
        Game.num_dice=6
        Game.result=""
        Game.round=1
        Game.new_game.balance=0



    
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
        if Game.round ==1 and Game.new_game.shelved ==0 :
            Game.result = Game.quitter()

        if Game.result=="y" or Game.result=="yes":
            print(f"Starting round {Game.round}")
            print(f"Rolling {Game.num_dice} dice...")
            roll=self.roller(Game.num_dice)
            self.print_roll(roll)
            enter=input("Enter dice to keep (no spaces), or (q)uit: ")
            if enter.lower() == "q" or enter.lower()=="quit":
                print(f"Total score is {Game.new_game.balance} points")
                print(f"Thanks for playing. You earned {Game.new_game.balance} points")
                Game.arguments_reset()

                
            else:
                if len(enter)<=6:
                    roll_list=[]
                    for i in range(len(enter)):
                        roll_list.append(int(enter[i]))
                    roll_tuple=tuple(roll_list)
                    Game.num_dice-=len(roll_tuple)
                    score=GameLogic.calculate_score(roll_tuple)
                    Game.new_game.shelved=Banker.shelf(Game.new_game,score)
                    print(f"You have {Game.new_game.shelved} unbanked points and {Game.num_dice} dice remaining")
                    enter_again=input("(r)oll again, (b)ank your points or (q)uit ")
                    # if enter.lower()== "r" or enter.lower() == "roll" or enter.lower() == "b"  or enter.lower() == "bank"  or enter.lower() == "q"  or enter.lower() == "quit":
                    if enter_again.lower()== "r" or enter_again.lower() == "roll":
                        self.play()
                    if enter_again.lower()== "b" or enter_again.lower() == "bank":
                        print(f"You banked {Game.new_game.shelved} points in round {Game.round}")
                        Game.round+=1
                        Game.num_dice=6
                        Game.banked_score=Banker.bank(Game.new_game)
                        print(f"Total score is {Game.new_game.balance} points")
                        self.play()
                    if enter_again.lower()== "q" or enter_again.lower() == "quit":
                        print(f"Total score is {Game.new_game.balance} points")
                        print(f"Thanks for playing. You earned {Game.new_game.balance} points")
                        Game.arguments_reset()
if __name__=="__main__":
    game=Game()
    game.play()




                        

                













