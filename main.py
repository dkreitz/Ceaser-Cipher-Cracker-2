englishLetterFreq = {'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75, 
                     'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78, 
                     'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97, 
                     'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15, 
                     'Q': 0.10, 'Z': 0.07}

ETAOIN = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Function to return the frequency of a letter in a string
def getLetterCount(message):
    letterCount = {letter: 0 for letter in LETTERS}
    for letter in message.upper():
        if letter in LETTERS:
            letterCount[letter] += 1
    return letterCount

# Function to return the first element of a list
def getItemAtIndexZero(x):
    return x[0]

def getFrequencyOrder(message):
    letterToFreq = getLetterCount(message)
    freqToLetter = {}
    for letter in LETTERS:
        freq = letterToFreq[letter]
        if freq not in freqToLetter:
            freqToLetter[freq] = [letter]
        else:
            freqToLetter[freq].append(letter)
    for freq in freqToLetter:
        freqToLetter[freq].sort(key=ETAOIN.find, reverse=True)
        freqToLetter[freq] = ''.join(freqToLetter[freq])
    freqPairs = list(freqToLetter.items())
    freqPairs.sort(key=getItemAtIndexZero, reverse=True)
    freqOrder = []
    for freqPair in freqPairs:
        freqOrder.append(freqPair[1])
    return ''.join(freqOrder)

def englishFreqMatchScore(message):
    freqOrder = getFrequencyOrder(message)
    matchScore = 0
    for commonLetter in ETAOIN[:6]:
        if commonLetter in freqOrder[:6]:
            matchScore += 1
        for uncommonLetter in ETAOIN[-6:]:
            if uncommonLetter in freqOrder[-6:]:
                matchScore += 1
    return matchScore