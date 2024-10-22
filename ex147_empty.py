"""
Exercise 147: Checking for a Winning Card

A winning Bingo card contains a line of 5 numbers that have all been called. Players
normally record the numbers that have been called by crossing them out or marking
them with a Bingo dauber. In this exercise we will mark that a number has been
called by replacing it with a 0 in the Bingo card dictionary.

Write a function that takes a dictionary representing a Bingo card as its only
parameter. If the card contains a line of five zeros (vertical, horizontal or diagonal)
then your function should return True, indicating that the card has won. Otherwise
the function should return False.

Create a main program that demonstrates your function by creating several Bingo
cards, displaying them, and indicating whether or not they contain a winning line.
You should demonstrate your function with at least one card with a horizontal line,
at least one card with a vertical line, at least one card with a diagonal line, and at
least one card that has some numbers crossed out but does not contain a winning line.

You will probably want to import your solution to Exercise146 when completing
this exercise.

Example of a Bingo card:
+-----+-----+-----+-----+-----+
|  B  |  I  |  N  |  G  |  O  |
+-----+-----+-----+-----+-----+
|  5  | 20  | 34  | 49  | 65  |
+-----+-----+-----+-----+-----+
| 14  | 29  |  42 | 57  | 70  |
+-----+-----+-----+-----+-----+
|  8  | 19  |  F  | 55  | 66  |
+-----+-----+-----+-----+-----+
|  3  | 18  | 33  | 46  | 60  |
+-----+-----+-----+-----+-----+
|  2  | 22  | 37  | 52  | 68  |
+-----+-----+-----+-----+-----+
"""

#from ex146 import create_bingo_card


def is_winning_card(card):
    """
    Check if the given Bingo card has a winning line

    >>> is_winning_card({
    ...     'B': [1, 5, 10, 15, 20],
    ...     'I': [5, 10, 15, 20, 25],
    ...     'N': [10, 15, 20, 25, 30],
    ...     'G': [15, 20, 25, 30, 35],
    ...     'O': [20, 25, 30, 35, 40]
    ... })
    False

    >>> is_winning_card({
    ...     'B': [1, 1, 0, 0, 0],
    ...     'I': [0, 0, 0, 0, 0],
    ...     'N': [0, 0, 0, 0, 0],
    ...     'G': [0, 0, 0, 0, 0],
    ...     'O': [0, 0, 0, 0, 0]
    ... })
    True

    >>> is_winning_card({
    ...     'B': [0, 0, 0, 0, 0],
    ...     'I': [5, 0, 10, 15, 20],
    ...     'N': [10, 5, 0, 15, 25],
    ...     'G': [15, 10, 5, 0, 35],
    ...     'O': [20, 15, 0, 5, 0]
    ... })
    True

    >>> is_winning_card({
    ...     'B': [0, 5, 10, 15, 20],
    ...     'I': [5, 0, 10, 15, 20],
    ...     'N': [10, 5, 0, 15, 20],
    ...     'G': [15, 10, 5, 0, 20],
    ...     'O': [20, 15, 10, 5, 0]
    ... })
    True

    >>> is_winning_card({
    ...     'B': [0, 5, 10, 15, 0],
    ...     'I': [5, 10, 10, 0, 20],
    ...     'N': [10, 5, 0, 15, 20],
    ...     'G': [15, 0, 5, 10, 20],
    ...     'O': [0, 15, 10, 5, 0]
    ... })
    True

    """

    # TODO: def is_winning(card):
    for letter in 'BINGO':
        sum = 0
        for i in range(5):
            sum += card[letter][i]
        if sum == 0:
            return True #VERTICAL
    sum = 0 
    for b in range(5):
        for letter in 'BINGO':
            sum += card[letter][b]
        if sum == 0:
            return True #HORIZONTAL
    sum = 0 
    for c in range(5):
        letter = 'BINGO'[c]
        sum += card[letter][c]
        if sum == 0:
            return True #DIAGONAL CASE #1
    sum = 0
    for d in range(5):
        letter = 'BINGO'[d]
        sum += card[letter][4-d]
    if sum == 0:
        return True #DIAGONAL CASE#2
    
    return False # IF NONE RETURN FALSE

    
def main():
    pass


if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    print("=" * 70)
    if result.failed == 0:
        print("All tests passed!")
    else:
        print(f"{result.failed} tests failed!")
    print("=" * 70)

    print("main():")
    main()
