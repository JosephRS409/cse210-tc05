import random #? Do we need this?

class Console:
    """A code template for a computer console. The responsibility of this 
    class of objects is to get text or numerical input and display text output.
    
    Stereotype:
        Service Provider, Interfacer

    Attributes:
         N/A
    """
    def __init__(self):
        self.prompt = ""
        self.mode = "normal"
        self.parachute = []
     
    def read(self, prompt): #prompt (string): The prompt to display on each line.
        """Gets text input from the user through the screen.

        Args: 
            self (Screen): An instance of Screen.
            prompt (string): The prompt to display to the user.

        Returns:
            string: The user's input as text.
        """
        return input(prompt)

    def read_number(self, prompt):
        """Gets numerical input from the user through the screen.

        Args: 
            self (Screen): An instance of Screen.
            prompt (string): The prompt to display to the user.

        Returns:
            float: The user's input as a float.
        """ # Changes the user's input from a letter to a number.
        return float(input(prompt))
        
    def write(self, text):
        """Displays the given text on the screen. 

        Args: 
            self (Screen): An instance of Screen.
            text (string): The text to display.
        """
        print(text)

    def set_gamemode(self):
        choice = input("Which gamemode would you like to play on? Easy or Normal? E/N: ")

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
            self.parachute = ["___","/___\\","\\   /","\\ /","0"]
        elif self.mode == "easy":
            self.parachute = ["___","/___\\","\\","/","\\","/","0"]

    def display_jumper(self):
        if len(self.parachute) == 7:
            print(f" {self.parachute[0]}\n{self.parachute[1]}\n{self.parachute[2]}   {self.parachute[3]}\n {self.parachute[4]} {self.parachute[5]}\n  {self.parachute[6]}\n /|\\\n / \\")
        elif len(self.parachute) == 5:
            print(f" {self.parachute[0]}\n{self.parachute[1]}\n{self.parachute[2]}\n {self.parachute[3]}\n  {self.parachute[4]}\n /|\\\n / \\")

