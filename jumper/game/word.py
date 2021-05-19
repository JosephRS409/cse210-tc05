import pandas as pd
import random

class Word:
    """A class to choose the word, decide if letters are found, and keep track of found letters
    
    Stereotype:
        Information Holder
        
    Attributes:
        (panda data/text file)
        
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
        df = pd.read_csv("wordbank.csv") # the dataframe 
        column = df["category"] 
        unique = column.unique() # 4 catagories
        options = unique.tolist() 

        valid = False ## This is the user picking a category.
        while not valid:
            print("Please choose a category:")
            for option in options:
                print(option.title())
            category = input("\n>")

            if category.lower() in options:
                valid = True
            else:
                print(f"{category.title()} is not a category, please choose one from this list:\n {options}")


        filtered_df = df[(df["category"] == category)] ## Filters the words by category (i.e. 
        word_choices = filtered_df["word"] ## sorts the words
#         print(word_choices) ## Used for testing
#         print(word_choices.unique().shape[0])
        num = random.randint(1,word_choices.unique().shape[0]) ## Adjusts the random based on category size.
        word = word_choices.iloc[num-1] ## Picks a word based on the random word.
#         print(word) ## Used for testing
        return word
