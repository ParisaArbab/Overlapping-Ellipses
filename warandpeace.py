"""
Author: Parisa Arbab
Date: Feb 27 2024
Statement:“I have not given or received any unauthorized assistance on this assignment.”
YouTube Link:https://youtu.be/dOsJMuAIfqg

answered this question in the above link:
 Explain how your pseudo random numbers are produced.
 Generate 10,000 pseudo random numbers.  What is the min, max, and mean?  Does that make
sense?

"""
import random


class WarAndPeacePseudoRandomNumberGenerator :
    """
    A pseudo-random number generator (PRNG) using the text file "war-and-peace.txt".
    """

    def __init__(self, seed=None) :
        """
        Initializes the PRNG object with an optional seed.

        Args:
            seed (int): The seed value for initializing the random number generator.
        """
        if seed is not None :
            random.seed ( seed )

    def random(self) :
        """
        Generates a pseudo-random number between 0 and 1 using characters from "war-and-peace.txt".

        Returns:
            float: A pseudo-random number between 0 and 1.
        """
        with open ( 'war-and-peace.txt', 'r' ) as file :
            text = file.read ()
            random_index = random.randint ( 0, len ( text ) - 1 )  # Answer to question 1
            random_char = text[ random_index ]
            random_number = ord ( random_char ) / 255  # normalize to range [0,1)
            return random_number


# Create PRNG object
prng = WarAndPeacePseudoRandomNumberGenerator ()

# Generate 10,000 pseudo-random numbers
random_numbers = [ prng.random () for _ in range ( 10000 ) ]

# Calculate min, max, and mean
min_number = min ( random_numbers )  # Answer to question 2
max_number = max ( random_numbers )  # Answer to question 2
mean_number = sum ( random_numbers ) / len ( random_numbers )  # Answer to question 2

print ( "Min:", min_number )  # Min and Max are range of random numbers
print ( "Max:", max_number )
print ( "Mean:", mean_number )   # sum of all numbers divide by how many there are (10000)
