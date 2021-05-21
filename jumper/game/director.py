from game.console import Console
from game.word import Word
from game.jumper import Jumper
from game.word import Word

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        console (Console): An instance of the class of objects known as Console.
        keep_playing (boolean): Whether or not the game can continue.
        word (Word): An instance of the class of objects known as Player.
        jumper (Jumper): An instance of the class of objects known as Jumper.
    """
    
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self.console = Console()
        self.word = Word()
        self.keep_playing = True
        self.jumper = Jumper()
        self.word = Word()
        self.letters = []
        self.placeholder = []

    def split_word(self):
        """Gets a word form word and splits it into a list
        
    #def start_game(self):
        #Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        word = self.word.get_word()
        for letter in word:
            self.letters.append(letter)
            self.placeholder.append("_")

    def update_guesses(self):
        """Updates the guesses and parachute"""
        # Side note I don't think we need a console and a player class,
        #  and i'm not sure which we'll keep so for now i'll pretend we're gonna use console to get user input
        if self.console.guess in self.letters:
            iterations = self.letters.count(self.console.guess)
            for _ in range(0, iterations):
                list_index  = self.letters.index(self.console.guess)
                self.placeholder.pop(list_index)
                self.placeholder.insert(list_index, self.console.guess)
                self.letters.pop(list_index)
                self.letters.insert(list_index, "")

    def display_word(self):
        word = ""
        for thing in self.placeholder:
            word = word + " " + thing
        print(word)
        while self.keep_playing:
            self.get_inputs() # First display the prompt and get the inputs.
                                # via Console class
            self.do_updates() #
            self.do_outputs()

    def get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting a letter from the User in the Jumper class via the 
        console class.

        Args:
            self (Director): An instance of Director.
        """
        message = self.hunter.get_message()
        self.console.write(message)
        location = self.console.read_number("Enter a location [1-1000]: ") # User input here.
        self.hunter.move(location) # This is the new location of the hunter.
        
    def do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, the .

        Args:
            self (Director): An instance of Director.
        """
        self.rabbit.watch(self.hunter.location) # The location of the hunter is sent to the 
            # rabbit watch method.
        
    def do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means the rabbit provides a hint.

        Args:
            self (Director): An instance of Director.
        """
        hint = self.rabbit.get_hint()
        self.console.write(hint)
        self.keep_playing = (self.rabbit.distance[-1] != 0)
        """
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

