import json, random,requests

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lettersLeft= list(alphabet)

phrasesAndHints = (requests.get('http://localhost:5000')).json()
random_json_Key= random.choice(list(phrasesAndHints.keys()))
random_json_Value = phrasesAndHints[random_json_Key]
phrase = random_json_Key
hint = random_json_Value
tries = 7 

running = True

def DisplayPhrase(lettersGuessed):
    # grab guessed letter's index and apply the letter to the phrase
    displayLetters = list()
    displayLetters.extend("                      ")# create space
    for i in phrase:
        if i.isalpha():
            if i in lettersGuessed:
                displayLetters.extend(i)# guessed letter
            else:
                displayLetters.extend("_") # unguessed letter
        else:
            displayLetters.extend(" ") # create space between words
    if "_" not in displayLetters: # returns false to end the game if all words are filled
        return False

    return ''.join(displayLetters) # keeps string on same line



def ReturnUsedLettersGuessed():
    # create list of guessed letter's indexes and return them
    letters = list()
    for index, i in  enumerate(lettersLeft):
        if i == "_":
            letters.extend(alphabet[index])
    return letters

def ResetGame():
    global lettersLeft
    global lettersLeft 
    global phrasesAndHints 
    global random_json_Key
    global random_json_Value 
    global phrase
    global hint
    global tries
    
    lettersLeft = list(alphabet)
    phrasesAndHints = (requests.get('http://localhost:5000')).json()
    random_json_Key= random.choice(list(phrasesAndHints.keys()))
    random_json_Value = phrasesAndHints[random_json_Key]
    phrase = random_json_Key
    hint = random_json_Value
    tries = 7
    
def WinOrLose():
    if tries <1:
        print("YOU LOSE :(")
        yesNo = input("Play again? ")
        if yesNo.upper() == "NO":  
            exit()
        else:
            ResetGame()
    if DisplayPhrase(ReturnUsedLettersGuessed()) == False: # all letters are guessed
        print("YOU WIN!")
        yesNo = input("Play again? ")
        if yesNo.upper() == "NO":  
            exit()
        else:
            ResetGame()
def main():
    ResetGame()
    while running == True:
        WinOrLose()
        print("")
        print("                     ",' '.join(lettersLeft)) # pretty up formatting of letters left
        print("")
        print((DisplayPhrase(ReturnUsedLettersGuessed())), "       ", hint,"           tries :",tries)
        print("")
        while True:
            
            guess = (input("choose a letter : ")).upper()
           
            if guess in ReturnUsedLettersGuessed(): # check if letter was already guessed
                print("Letter already guessed. Try again")
            elif guess not in phrase: # check if letter is in phrase and deduct tries and letter if not
                if len(guess) != 1 or  guess.isdigit():
                    print("Not a letter")
                    break
                tries -= 1
                indexOfLetter = lettersLeft.index(guess)# grab index of guessed letter and replace it with _
                lettersLeft[lettersLeft.index(guess)] = "_"
                break
            else:
                indexOfLetter = lettersLeft.index(guess) # correct guess, replace letter with _
                lettersLeft[lettersLeft.index(guess)] = "_"
                break
        
if __name__=='__main__':
    main()
