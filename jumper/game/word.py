import pandas as pd
import random

class Word:
    """A class to choose the word, decide if letters are found, and keep track of found letters
    
    Stereotype:
        Information Holder ##Not sure about this one yet.

    Attributes:
        
    """

    def __init__(self):
        """Class constructor. Declares and initializes instance attributes.

        Args:
            self (Word): An instance of Word.
        """

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