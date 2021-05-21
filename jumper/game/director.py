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
        self.letters = [] # The list of letters of the word randomly chosen.
            #  i.e. ["w", "o", "r", "d"]
            # Changes so you can accommodate for multiple letters.
        self.placeholder = [] # The empty word that updates with correct guesses.
            # i.e. "guessed 'd'" --> [_ _ _ d]
        self.other_letters = [] # Similar to the first letters list. Stays the 
            # same in order to check the word against for winning.
        self.i = 0
        self.guesses = [] # The list of previous guesses.
        self.game_word = ""

    def split_word(self):
        """Gets a word from the Word class and splits it into a list.
        
        Args:
            self (Director): an instance of Director.
        """
        self.game_word = self.word.get_word() # This is to choose the game word.
        for letter in self.game_word:
            self.letters.append(letter) # Puts the word into the letter list, 
                # iterating by letter.
            self.other_letters.append(letter) # " ditto  " This list stays static
                # to compare to the updating placeholder list
            self.placeholder.append("_") # Makes the "_" per letter.

    def update_guesses(self):
        """Updates the guesses and parachute
        
        Args:
            self (Director): an instance of Director.
        """

        if self.player.guess in self.guesses:
            pass  # If a guess is repeated, do nothing.
        elif self.player.guess in self.letters: # if guess is correct.
            self.guesses.append(self.player.guess) # update the guesses list.
            iterations = self.letters.count(self.player.guess) # for the word
                # "test", there are two iterations of "T"
            for _ in range(0, iterations): # For each time the correct 
                    # guess appears in the word,
                    # This loop updates the placeholder and letters lists.
                list_index  = self.letters.index(self.player.guess) # This is the location
                    # of the first instance of the correct guess in letters.
                self.placeholder.pop(list_index) # This deletes the correct guess from the
                    # placeholder list.
                    # This is the series of underscores, representing the word, that
                    # the User sees.
                self.placeholder.insert(list_index, self.player.guess) # Once the correct
                    # guess is deleted from placeholder, this replaces an "_" with the 
                    # correct guess.
                self.letters.pop(list_index) # This deletes the letter from the letters 
                    # list so that list_index can find the next instance if there are 
                    # multiple instances.
                self.letters.insert(list_index, "") # This replaces deleted letter with a 
                    # space to preserve indexes in the letters list.

        elif self.player.guess.isalpha() and len(self.player.guess) == 1:
            # If guess is incorrect but valid (isalpha makes sure it is a letter and
                      # len(self.player.guess) == 1 makes sure only one letter is guessed)
            self.guesses.append(self.player.guess) # Updates the guesses list.
            self.jumper.parachute[self.i] = " " # Replaces part of the parachute with a
                                                # blank.
            self.i +=1 # This is a counter for incorrect guesses.

    def display_word(self):
        """Displays amount of letters in the word as _ for the player to guess
        
        Args:
            self (Director): an instance of Director.
        """

        word = ""
        for thing in self.placeholder:
            word = word + " " + thing
        print(word)

    def able_to_play(self):
        """Check to see if the player wins/can continue to play
        
        Args:
            self (Director): an instance of Director.
        """

        if self.other_letters == self.placeholder:
            print("Congratulations! you Win!")
            return False
        elif self.player.guess.lower() == "quit":
            return False
        elif self.i == len(self.jumper.parachute):
            self.jumper.display_jumper()
            print(f"the word was {self.game_word}")
            print("you suck")
            return False
        else:
            return True

    def start_game(self):
        """Plays the Game
        
        Args:
            self (Director): an instance of Director.
        """
        
        self.split_word()
        self.jumper.set_gamemode()
        self.jumper.set_jumper()
        while self.keep_playing == True:
            self.display_word()
            self.jumper.display_jumper()
            self.player.guess_letter() # Has player guess a Lettre
            self.update_guesses() # Updates the lists with the guesses
            self.keep_playing = self.able_to_play() #CHecks to see if you can keep playing
