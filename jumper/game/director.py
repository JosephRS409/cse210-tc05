<<<<<<< HEAD
from game.console import Console
from game.word import Word
=======
from game.player import Player
>>>>>>> master
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
<<<<<<< HEAD
        self.console = Console()
        self.word = Word()
=======
        self.player = Player()
>>>>>>> master
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
        
    #def start_game(self):
        #Starts the game loop to control the sequence of play.
        
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
<<<<<<< HEAD
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
=======
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
            self.guesses.append(self.player.guess) # Adds the letter to the 
                # list of already guessed letters.
            self.jumper.parachute[self.i] = " " # Replaces the next part of the parachute 
                                                     # with a  blank
            self.i +=1 # This adds 1 to a counter for incorrect guesses
>>>>>>> master

    def display_word(self):
        """Displays amount of letters in the word as _ for the player to guess
        
        Args:
            self (Director): an instance of Director.
        """

        # Make the placeholder list look pretty and display for user.
        word = ""
        for thing in self.placeholder: # Displays the word with a space between each letter
            word = word + " " + thing
        print(word)
<<<<<<< HEAD
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

=======

    def able_to_play(self):
        """Check to see if the player wins/can continue to play
        
        Args:
            self (Director): an instance of Director.
        """

        if self.other_letters == self.placeholder: # Checks to see if the player has guessed all letters in the word.
            print("Congratulations! you Win!")
            return False
        elif self.player.guess.lower() == "quit": # Checks to see if the player wants to quit.
            return False
        elif self.i == len(self.jumper.parachute): # Checks to see if the player has lost.
            self.jumper.display_jumper()
            print(f"the word was {self.game_word}")
            print("you suck") # This needs no explanation.
                # "If it does, it applies to you." -- Joseph
            return False
        else:
            return True

    def start_game(self):
        """Plays the Game
        
        Args:
            self (Director): an instance of Director.
        """
        
        self.split_word() # Splits the word into a list.
        self.jumper.set_gamemode() # Sets the gamemode.
        self.jumper.set_jumper() # Sets the jumper depending on difficulty.
        while self.keep_playing == True:
            self.display_word() # Displays the word.
            self.jumper.display_jumper() # Displays the jumper.
            self.player.guess_letter() # Has player guess a letter.
            self.update_guesses() # Updates the lists with the guesses.
            self.keep_playing = self.able_to_play() #Checks to see if you can keep playing.
>>>>>>> master
