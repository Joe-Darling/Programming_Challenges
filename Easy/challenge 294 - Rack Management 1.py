"""
Challenge: Rack Management 1

Description:
Today's challenge is inspired by the board game Scrabble. Given a set of 7 letter tiles and a word, determine whether
you can make the given word using the given tiles.
Feel free to format your input and output however you like. You don't need to read from your program's input if you
don't want to - you can just write a function that does the logic. I'm representing a set of tiles as a single string,
but you can represent it using whatever data structure you want.

Bonus 1:
Handle blank tiles (represented by "?"). These are "wild card" tiles that can stand in for any single letter.

Bonus 2:
Given a set of up to 20 letter tiles, determine the longest word from the enable1 English word list that can be
formed using the tiles.

Bonus 3:
Consider the case where every tile you use is worth a certain number of points, given on the Wikpedia page for Scrabble.
E.g. a is worth 1 point, b is worth 3 points, etc.
For the purpose of this problem, if you use a blank tile to form a word, it counts as 0 points. For instance, spelling
"program" from "progaaf????" gets you 8 points, because you have to use blanks for the m and one of the rs, spelling
prog?a?. This scores 3 + 1 + 1 + 2 + 1 = 8 points, for the p, r, o, g, and a, respectively.
Given a set of up to 20 tiles, determine the highest-scoring word from the word list that can be formed using the tiles.

Result:
Success!
Standard: Took about 3 minutes
Bonus 1: Took about 2 minutes
Bonus 2: Took about 20 minutes
Bonus 3: Took about 40 minutes
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


def longest(tiles_as_string):
    tiles = []
    for tile in tiles_as_string:
        tiles.append(tile)
    longest_word = ""
    file = open("D:\\Files\Python Projects\DailyProgrammer\Files\enable1.txt", "r")
    for word in file:
        word = word.strip("\n")
        if scrabble(tiles, word) and len(word) > len(longest_word):
            longest_word = word
    return longest_word


def highest(tiles_as_string):
    tiles = []
    for tile in tiles_as_string:
        tiles.append(tile)
    highest_score = "?"
    file = open("D:\\Files\Python Projects\DailyProgrammer\Files\enable1.txt", "r")
    for word in file:
        word = word.strip("\n")
        if scrabble(tiles_as_string, word) and score_word(tiles_as_string, word) > score_word(tiles_as_string, highest_score):
            highest_score = word
    return highest_score, score_word(tiles_as_string, highest_score)


def score_word(tiles_as_string, word):
    tiles = []
    for tile in tiles_as_string:
        tiles.append(tile)

    chr_val = {"a": 1, "b": 3, "c": 3, "d": 2, "e": 1, "f": 4, "g": 2, "h": 4, "i": 1, "j": 8, "k": 5, "l": 1, "m": 3,
               "n": 1, "o": 1, "p": 3, "q": 10, "r": 1, "s": 1, "t": 1, "u": 1, "v": 4, "w": 4, "x": 8, "y": 4, "z": 10,
               "?": 0}
    points = 0

    for letter in word:
        if letter not in tiles:
            continue
        else:
            tiles.remove(letter)
            points += chr_val[letter]
    return points

#print(scrabble("aopelp", "apple"))
#print(highest("flajrwerwe"))
print(highest("??y"))


