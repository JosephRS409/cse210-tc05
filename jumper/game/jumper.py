class Jumper:
    """The code for our land bound adventurer. The responsibility
    
    Stereotype:
        Information Holder ##Not sure about this one yet.

    Attributes:
        
    """

    def __init__(self):
        """Class constructor. Declares and initializes instance attributes.

        Args:
            self (Jumper): An instance of Jumper.
        """
        self.mode = "normal"
        self.parachute = []

    def set_gamemode(self):
        choice = input(
            "Which gamemode would you like to play on? Easy or Normal? E/N: ")

        if choice.lower() == "n":
            self.mode = "normal"
        elif choice.lower() == "e":
            self.mode = "easy"

    def set_jumper(self):
        """Sets the parachute based on the game difficulty
        
        Args: 
            self (Screen): An instance of Screen.
        """
        if self.mode == "normal":
            self.parachute = ["___", "/___\\", "\\   /", "\\ /", "0"]
        elif self.mode == "easy":
            self.parachute = ["___", "/___\\", "\\", "/", "\\", "/", "0"]

    def display_jumper(self):
        if len(self.parachute) == 7:
            print(
                f" {self.parachute[0]}\n{self.parachute[1]}\n{self.parachute[2]}   {self.parachute[3]}\n {self.parachute[4]} {self.parachute[5]}\n  {self.parachute[6]}\n /|\\\n / \\")
        elif len(self.parachute) == 5:
            print(
                f" {self.parachute[0]}\n{self.parachute[1]}\n{self.parachute[2]}\n {self.parachute[3]}\n  {self.parachute[4]}\n /|\\\n / \\")
