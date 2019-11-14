from string import ascii_letters

play = True
vowels = "AaEeIiOoUu"

def checkSyllable(syllable):
    for i in range(len(syllable)):
        if syllable[i] not in ascii_letters and syllable[i] != "*":
            return False
    return True

while True:
    playAgain = ""
    syllableUsed = False
    nextSyllable = True

    syllable1 = input("Enter the first gibberish syllable: ")
    while not checkSyllable(syllable1):
        syllable1 = input("Syllable must contain only letters or a wildcard: ")

    syllable2 = input("Enter the second gibberish syllable: ")
    while not checkSyllable(syllable2):
        syllable2 = input("Syllable must contain only letters or a wildcard: ")

    word = input("Enter a word to translate: ")
    gibberishWord = ""

    for i in range(len(word)):
        if word[i] in vowels:
            if nextSyllable:
                if syllableUsed:
                    gibberishWord = gibberishWord + syllable2
                else:
                    gibberishWord = gibberishWord + syllable1
                    syllableUsed = True

                nextSyllable = False
        else:
            nextSyllable = True

        gibberishWord = gibberishWord.replace("*", word[i])
        gibberishWord = gibberishWord + word[i]

    print("New gibberish word: " + gibberishWord)

    while playAgain != "y" or playAgain != "n":
        playAgain = input("Do you want to play again (y/n)? ")

    if playAgain == "n":
        break
    elif playAgain == "y":
        continue
