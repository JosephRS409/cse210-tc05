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
        self.player = Player()
        self.keep_playing = True
        self.jumper = Jumper()
        self.word = Word()
        self.letters = []
        self.placeholder = []
        self.other_letters = []

    def split_word(self):
        """Gets a word form word and splits it into a list
        
        Args:
            self (Director): an instance of Director.
        """
        word = self.word.get_word()
        for letter in word:
            self.letters.append(letter)
            self.other_letters.append(letter)
            self.placeholder.append("_")

    def update_guesses(self):
        """Updaates the gueses and parachute"""
        if self.player.guess in self.letters:
            iterations = self.letters.count(self.player.guess)
            for _ in range(0, iterations):
                list_index  = self.letters.index(self.player.guess)
                self.placeholder.pop(list_index)
                self.placeholder.insert(list_index, self.player.guess)
                self.letters.pop(list_index)
                self.letters.insert(list_index, "")

    def display_word(self):
        """Displays amount of letters in the word as _ for the player to guess"""
        word = ""
        for thing in self.placeholder:
            word = word + " " + thing
        print(word)

    def able_to_play(self):
        if self.other_letters == self.placeholder:
            print("Congratulations! you Win!")
            return False
        else:
            play = input("keep playing? ")
            if play.lower() == "n" or play.lower() == "no":
                return False
            elif play.lower() == "y" or play.lower() == "yes":
                return True

    def start_game(self):
        """Plays the Game"""
        self.split_word()
        self.jumper.set_gamemode()
        self.jumper.set_jumper()
        while self.keep_playing == True:
            self.display_word()
            self.jumper.display_jumper()
            self.player.guess_letter()
            self.update_guesses()
            self.display_word()
            self.keep_playing = self.able_to_play()
