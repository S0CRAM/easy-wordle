#################
# Guessing game #
#   By S0CR4M   #
#################

#-- Imports
import random

#-- Functions
def get_word():
    wordlist = []
    dictionary = open("dictionary.txt", "r")
    for lines in dictionary.readlines():
        lines = lines.split("\n")
        wordlist.append(lines[0])
    word = random.randrange(0, len(wordlist)-1)
    return wordlist[word]

def main():
    word = get_word()
    wordLen = ""
    for x in range(len(word)):
        wordLen = wordLen + "_"
    print(wordLen)
    wordle = list(word)
    output = list(wordLen)
    while True:
        character = input("Input a single character: ")
        count = 0
        for x in wordle:
            if character == x:
                output[count] = character
            count += 1
        print("".join(output))
        if output == wordle:
            break
    print("Congrats!")
    return 0

if __name__ == "__main__":
    main()