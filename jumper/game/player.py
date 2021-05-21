class Player:
    """A code template for the Player. That is you! The responsibility 
    of this class of objects is to try and save the Jumper from 
    certain peril and doom, like in "Hangman."
    
    Stereotype:
        Information Holder ##Not sure about this one yet.

    Attributes:
        
    """

    def __init__(self):
        """Class constructor. Declares and initializes instance attributes.

        Args:
            self (Player): An instance of Player.
        """
        self.guess = ""
        
        
    def guess_letter(self):
        """Gets the letter guess form the player"""
        self.guess = input("Enter your guess or Quit to quit: ")
        #Gets the letter guess form the player.
    