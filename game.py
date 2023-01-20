from player import Player
from human import Human
from ai import AI

class Game:
    def __init__(self):
        self.player_one = Human("Bob")
        self.player_two = Human("Joe")
    def display_welcome(self):
        self.display_welcome = print("Welcome to Rock, Paper, Scissors, Lizard, Spock!")
    def display_rules(self):
        self.display_rules = print("Rules: Each player picks a gesture from the list to try to win the round./n Rock crushes Scissors. /n Scissors cuts Paper /n Paper covers Rock /n Rock crushes Lizard /n Lizard poisons Spock /n Spock smashes Scissors /n Scissors decapitates Lizard /n Lizard eats Paper /n Paper disproves Spock /n Spock vaporizes Rock. /n The winner of the round wins a point. Game will continue until best of 3 rounds")
    def choose_game(self): 
        self.choose_game = input("Please select number of human players for this game. Choose 1 or 2.")
        if self.choose_game == 1:
            self.player_two = AI()
        else:
            self.player_two = Human()
    
    def play_game(self):
    
        while self.player_one.wins <2 or self.player_two.wins <2:
            self.player_one.choose_gesture()
            self.player_two.choose_gesture()
            if self.player_one.selected_gesture == "Rock" and self.player_two.selected_gesture == "Scissors":
                self.player_one.wins += 1
            elif self.player_one.selected_gesture == "Scissors" and self.player_two.selected_gesture == "Paper":
                self.player_one.wins += 1
            elif self.player_one.selected_gesture == "Paper" and self.player_two.selected_gesture == "Rock":
                self.player_one.wins += 1
            elif self.player_one.selected_gesture == "Rock" and self.player_two.selected_gesture == "Lizard":
                self.player_one.wins += 1
            elif self.player_one.selected_gesture == "Lizard" and self.player_two.selected_gesture == "Spock":
                self.player_one.wins += 1
            elif self.player_one.selected_gesture == "Spock" and self.player_two.selected_gesture == "Scissors":
                self.player_one.wins += 1
            elif self.player_one.selected_gesture == "Scissors" and self.player_two.selected_gesture == "Lizard":
                self.player_one.wins += 1
            elif self.player_one.selected_gesture == "Lizard" and self.player_two.selected_gesture == "Paper":
                self.player_one.wins += 1
            elif self.player_one.selected_gesture == "Paper" and self.player_two.selected_gesture == "Spock":
                self.player_one.wins += 1
            elif self.player_one.selected_gesture == "Spock" and self.player_two.selected_gesture == "Rock":
                self.player_one.wins += 1
            

