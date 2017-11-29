"""
Challenge: Spelling with Chemistry

Description:
Given a word, print the word as a series of elements with proper capitalization from the periodic table of elements.
Ex:
Input: Genius
Output: GeNiUS (germanium nickel uranium sulfur)

Results:
Success!
Standard: About 30 mins
"""


def create_word(table, word):
    result = ""
    elements_used = []
    while word != "":
        letter = word[0]
        for element in table:
            if element.lower() == letter.lower():
                result += element
                elements_used.append(table[element])
                word = word[1:]
                break
        letters = word[0:2]
        for element in table:
            if element.lower() == letters.lower():
                result += element
                elements_used.append(table[element])
                word = word[2:]
                break
    return result, elements_used


def main():
    table = {}
    file = open("D:\\Files\Python Projects\DailyProgrammer\Files\ptdata2.csv", "r")
    for line in file:
        line = line.replace(" ", "")
        line = line.replace('"', "")
        lst = line.split(",")
        table[lst[1]] = lst[2]
    file.close()
    word = input("Enter Word: ")
    result, lst = create_word(table, word)
    print(result, end=" (")
    elements_used = ""
    for ele in lst:
        elements_used += ele + ", "
    elements_used = elements_used[0:len(elements_used)-2]
    print(elements_used + ")")



main()