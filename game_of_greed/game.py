
from game_of_greed.game_logic import Banker ,GameLogic
import sys 

class Game():

    new_game=Banker()
    num_dice=6
    result=""
    round=1
    status=True
    


    def __init__(self,roller=None):
        self.roller=roller or GameLogic.roll_dice
        # self.roller=roller

    @staticmethod    
    def arguments_reset():
        Game.new_game.shelved=0
        Game.num_dice=6
        Game.result=""
        Game.round=1
        Game.new_game.balance=0
        Game.status = True



    
    @staticmethod
    def welcome():
        """
        * This function will appear once, only at the beggining of the game 
        * Will ask the user if he/she wants to play the game or quit
        """
        print("Welcome to Game of Greed")
        result=input("Wanna play?")
        result_lower=result.lower()
        if result_lower == "n" or result_lower =="no":
            print("OK. Maybe another time")
        return result_lower

    def to_quit(self):
        """
        To handle quiting
        """
        if Game.status :
            print(f"Total score is {Game.new_game.balance} points")
            print(f"Thanks for playing. You earned {Game.new_game.balance} points")        
        else:
            print(f"Thanks for playing. You earned {Game.new_game.balance} points")
        Game.arguments_reset()


    def print_roll(self,roll):
        """
        Prints the roll of dice
        """
        print(','.join([str(i) for i in roll]))



    def is_cheating(self,roll):
        """
        * Will be called if the user cheated, by the check method
        * Asks the user for anthor input, then calls check method again 
        * This recursive calling back and forth between check and is_cheating will continue untill either 
          stops cheating or just quits the game.

        * Arguments:
            roll -- the roll that the user cheated on
        """
        Game.status=False
        print("Cheater!!! Or possibly made a typo...")
        self.print_roll(roll)
        enter=input("Enter dice to keep (no spaces), or (q)uit: ")
        if enter.lower() == "q" or enter.lower()=="quit":
            self.to_quit()
            Game.status=True      
            return []
            
        else:
            return self.check(roll,enter)

    def check(self,roll,enter):
        """
        * To check if the user cheated, by comparing the numbers in the roll with what the user picked
        
        * Arguments:
            roll  -- the roll to check on
            enter -- what the user picked
        """
        if not enter.isalpha():
            if len(enter)<=6:
                roll_list=[]
                leng= len(enter)
                for i in range(leng): 
                    if roll.count(int(enter[i])):
                        if enter.count(enter[i]) <= roll.count(int(enter[i])):
                            roll_list.append(int(enter[i]))
                            
                        else:
                            roll_list = self.is_cheating(roll)
                            break
                    else:
                        roll_list = self.is_cheating(roll)

         
        return(roll_list)


    def zilch(self,roll):
        """
        When the user scores zero

        Arguments:  
            roll -- the dice roll that scored zero 
        """
        print('Zilch!!! Round over')
        print(f'You banked 0 points in round {Game.round}')
        print('Total score is 0 points')
        Game.round+=1
        Game.num_dice=6
        Game.new_game.shelved =0
        if roll ==6:
            Game.status = False
        self.play()


    def play(self):
        """
        * To play the game, this method will keep calling itself untill the game ends, by quitting the game
        * This method starts the rounds, roll the dice, calculate it's score and so on
        * Uses all the methods above

        """

        if Game.round ==1 and Game.new_game.shelved ==0 :
            Game.result = Game.welcome()

        if Game.result=="y" or Game.result=="yes":
            if not Game.new_game.shelved:
                print(f"Starting round {Game.round}")

            print(f"Rolling {Game.num_dice} dice...")
            roll=self.roller(Game.num_dice)
            self.print_roll(roll)
            GameLogic.how_many=0
            if not (GameLogic.calculate_score(roll)):
                self.zilch(len(roll))
                GameLogic.how_many=0
                sys.exit()
                
                



            enter=input("Enter dice to keep (no spaces), or (q)uit: ")
            # print('yyy')
            if enter.lower() == "q" or enter.lower()=="quit":
                self.to_quit()
               
            else:             
                roll_list = self.check(roll,enter)
                if roll_list :  
                    roll_tuple=tuple(roll_list)
                    Game.num_dice-=len(roll_tuple)
                    GameLogic.how_many=0
                    score = GameLogic.calculate_score(roll_tuple)
                    if len(roll_tuple) == 6 and GameLogic.how_many==6:
                        # print('hot dice:',GameLogic.how_many)
                        Game.status = False

                    if not score:
                        self.zilch(len(roll_tuple))

            
                    Game.new_game.shelved = Banker.shelf(Game.new_game,score)

                    print(f"You have {Game.new_game.shelved} unbanked points and {Game.num_dice} dice remaining")
                    enter_again=input("(r)oll again, (b)ank your points or (q)uit ")

                    if enter_again.lower()== "r" or enter_again.lower() == "roll":
                        if not Game.num_dice:
                            Game.num_dice=6
                        self.play()

                    if enter_again.lower()== "b" or enter_again.lower() == "bank":
                        print(f"You banked {Game.new_game.shelved} points in round {Game.round}")
                        Game.round+=1
                        Game.num_dice=6
                        Game.banked_score = Banker.bank(Game.new_game)
                        print(f"Total score is {Game.new_game.balance} points")
                        self.play()

                    if enter_again.lower()== "q" or enter_again.lower() == "quit":
                        self.to_quit()
                      

                        
                        
if __name__=="__main__":
    game=Game()
    game.play()




                        

                













