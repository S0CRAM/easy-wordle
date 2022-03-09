#################
# Guessing game #
#   By S0CR4M   #
#################

#-- Imports
import random, os

#-- Alphabet list
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
popped = []

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
        character = input("Input a single letter: ")
        count = 0
        for x in wordle:
            if character == x:
                output[count] = character
            count += 1
        if output == wordle:
            break
        else:
            os.system("cls")
            check = False
            for x in  range(len(alpha)):
                if character == alpha[x]:
                    pop = alpha.pop(x)
                    popped.append(pop)
                    check = True
                    break
            if not(check):
                for x in range(len(popped)):
                    if character == popped[x]:
                        print("You have already tried that! \n")
            print("Remaining letters: " + str(alpha) + "\n")
            print("".join(output))
    os.system("cls")
    print("Congrats! The word is: " + word)
    return 0

if __name__ == "__main__":
    main()