"""
Challenge: Rack Management 2

Description:
Today's challenge is loosely inspired by the board game Scrabble. You will need to download the enable1 English word
list in order to check your solution. You will also need the point value of each letter tile. For instance, a is worth
1, b is worth 3, etc. Here's the point values of the letters a through z:
[1,3,3,2,1,4,2,4,1,8,5,1,3,1,1,3,10,1,1,1,1,4,4,8,4,10]

For this challenge, the score of a word is defined as 1x the first letter's point value, plus 2x the second letters,
3x the third letter's, and so on. For instance, the score of the word daily is 1x2 + 2x1 + 3x1 + 4x1 + 5x4 = 31.
Given a set of 10 tiles, find the highest score possible for a single word from the word list that can be made using
the tiles.

Bonus 1:
Make your solution more efficient than testing every single word in the word list to see whether it can be formed.
For this you can spend time "pre-processing" the word list however you like, as long as you don't need to know
the tile set to do your pre-processing. The goal is, once you're given the set of tiles, to return your answer as
quickly as possible.

Bonus 2: Handle up to 20 tiles, as well as blank tiles (represented with ?). These are "wild card" tiles that may stand
in for any letter, but are always worth 0 points. For instance, "?ai?y" is a valid play (beacuse of the word daily)
worth 1x0 + 2x1 + 3x1 + 4x0 + 5x4 = 25 points.

Results:
Success!
Standard: Took about 16 minutes
Bonus 1: Not attempted
"""

def scrabble(tiles_as_string, word):
    tiles = []
    for tile in tiles_as_string:
        tiles.append(tile)
    for letter in word:
        if letter not in tiles:
            if "?" in tiles:
                tiles.remove("?")
            else:
                return False
        else:
            tiles.remove(letter)
    return True


def highest(tiles_as_string):
    tiles = []
    for tile in tiles_as_string:
        tiles.append(tile)

    file = open("C:\\Users\Joe\PycharmProjects\DailyProgrammer\Files\enable1.txt", "r")
    highest_score = ""
    for word in file:
        word = word.strip("\n")
        if scrabble(tiles_as_string, word) and get_score(word) > get_score(highest_score):
            highest_score = word
    return str(get_score(highest_score)) + ' ("{}")'.format(highest_score)



def get_score(word):
    score = 0
    chr_val = {"a": 1, "b": 3, "c": 3, "d": 2, "e": 1, "f": 4, "g": 2, "h": 4, "i": 1, "j": 8, "k": 5, "l": 1, "m": 3,
               "n": 1, "o": 1, "p": 3, "q": 10, "r": 1, "s": 1, "t": 1, "u": 1, "v": 4, "w": 4, "x": 8, "y": 4, "z": 10}
    for x in range(len(word)):
                score += chr_val[word[x]] * (x + 1)
    return score


print(highest("umnyeoumcp"))