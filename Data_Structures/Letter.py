'''
------------------------------------------------------------------------
Letter Object Class
------------------------------------------------------------------------
Author: Scott Vodon
ID:     181686100
Email:  vodo6100@mylaurier.ca
__updated__ = 2019 M03 22
------------------------------------------------------------------------
'''
class Letter:

    def __init__(self, letter):
        """
        -------------------------------------------------------
        Initialize a Letter object.
        Use: l = Letter(char)
        -------------------------------------------------------
        Parameters:
            letter - an single uppercase letter of the alphabet (str)
        Returns:
            A new Letter object (Letter)
        -------------------------------------------------------
        """
        assert letter.isalpha() and letter.isupper(), "Invalid letter"

        self.letter = letter
        self.count = 0
        self.comparisons = 0

    def __str__(self):
        """
        -------------------------------------------------------
        Creates a formatted string of Letter data.
        Use: print(m)
        Use: s = str(m)
        -------------------------------------------------------
        Returns:
            The values of self.letter (str)
        -------------------------------------------------------
        """
        return "{}: {}, {}".format(self.letter, self.count, self.comparisons)

    def __eq__(self, target):
        """
        -------------------------------------------------------
        Compares this Letter against another Letter for equality.
        Use: source == target
        -------------------------------------------------------
        Parameters:
            target - Letter to compare to (Letter)
        Returns:
            result - True if the letters match, False otherwise (boolean)
        -------------------------------------------------------
        """
        self.count += 1
        self.comparisons += 1
        result = self.letter == target.letter
        return result

    def __lt__(self, target):
        """
        -------------------------------------------------------
        Determines if this Letter comes before another.
        Use: source < target
        -------------------------------------------------------
        Parameters:
            target - Letter to compare to (Letter)
        Returns:
            result - True if source precedes target, False otherwise (boolean)
        -------------------------------------------------------
        """
        self.comparisons += 1
        result = self.letter < target.letter
        return result

    def __le__(self, target):
        """
        -------------------------------------------------------
        Determines if this Letter precedes or is or equal to another.
        Use: source <= target
        -------------------------------------------------------
        Parameters:
            target - Letter to compare to (Letter)
        Returns:
            result - True if this Letter precedes or is equal to target,
              False otherwise (boolean)
        -------------------------------------------------------
        """
        self.comparisons += 1
        result = self.letter <= target.letter
        return result
