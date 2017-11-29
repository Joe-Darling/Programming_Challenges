"""
Challenge: Looking for patterns

Description: You will be given a sequence that of letters and you must match with a dictionary. The sequence is a
pattern of equal letters that you must find.

Pattern:
XXYY means that you have a word that contains a sequence of 2 of the same letters followed by again 2 of the same
letters

succeed <- matches
success <- no match

XYYX means we have a word with at least four letters where you have a sequence of a letter, followed by 2 letters that
are the same and then again the first letter

narrate <- matches
hodor <- no match

Results:
Success!
Standard: Took about an hour
"""


def does_it_match(word, pattern, table):
    start = 0
    ind = start
    while len(word[start:]) >= len(pattern):
        for letter in table:
            table[letter] = ""
        for letter in pattern:
            if table[letter] == "":
                table[letter] = word[ind]
            else:
                if table[letter] != word[ind]:
                    break
            ind += 1
        if ind - len(pattern) >= start:
            return True
        start += 1
        ind = start
    return False


def main():
    pattern = input("Enter Patten: ")
    file = open("D:\\Files\Python Projects\DailyProgrammer\Files\enable1.txt", "r")
    table = {}
    for char in pattern:
        if char not in table.keys():
            table[char] = ""
    print("Words with pattern '" + pattern + "':")
    for word in file:
        word = word.rstrip()
        if does_it_match(word, pattern, table):
            print(word)


main()