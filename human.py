from player import Player

class Human(Player):
    def __init__(self, name):
        super().__init__(name)

    def choose_gesture(self):
        for gesture in self.list_gestures:
            print(gesture)
        
        #Take in a User Input of their choice.

        #Assign the User Input to self.selected_gesture  self.selected_gesture = user_input
        

