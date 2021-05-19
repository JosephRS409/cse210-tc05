from game.console import Console
from game.player import Player
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
        player (Player): An instance of the class of objects known as Player.
        jumper (Jumper): An instance of the class of objects known as Jumper.
    """
    
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self.console = Console()
        self.player = Player()
        self.keep_playing = True
        self.jumper = Jumper()
        self.word = Word()
        self.letters = []
        self.placeholder = []

    def split_word(self):
        """Gets a word form word and splits it into a list
        
        Args:
            self (Director): an instance of Director.
        """
        word = self.word.get_word()
        for letter in word:
            self.letters.append(letter)
            self.placeholder.append("_")

    def update_guesses(self):
        """Updaates the gueses and parachute"""
        # Side note I don't think we need a console and a player class,
        #  and i'm not sure which we'll keep so for now i'll pretend we're gonna use console to get user input
        if self.console.guess in self.letters:
            iterations = self.letters.count(self.console.guess)
            for _ in range(0, iterations):
                list_index  = self.letters.index(self.consoke.guess)
                self.placeholder.pop(list_index)
                self.placeholder.insert(list_index, self.console.guess)
                self.letters.pop(list_index)
                self.letters.insert(list_index, "")

    def display_word(self):
        word = ""
        for thing in self.placeholder:
            word = word + " " + thing
        print(word)