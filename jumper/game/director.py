from game.console import Console
from game.player import Player
from game.jumper import Jumper
import pandas as pd
import random

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

    def get_word(self):
        """Chooses a word for the game

        Args:
            self - Instance of the director

        Returns:
            word (str) -- Word for the game

        """
        df = pd.read_csv("wordbank.csv")
        column = df["category"]
        unique = column.unique()
        options = unique.tolist()

        valid = False
        while not valid:
            print("Please choose a category:")
            for option in options:
                print(option.title())
            category = input("\n>")

            if category.lower() in options:
                valid = True
            else:
                print(f"{category.title()} is not a category, please choose one from this list:\n {options}")


        filtered_df = df[(df["category"] == category)]
        word_choices = filtered_df["word"]
        print(word_choices)
        print(word_choices.unique().shape[0])
        num = random.randint(1,word_choices.unique().shape[0])
        word = word_choices.iloc[num-1]
        print(word)
        return word