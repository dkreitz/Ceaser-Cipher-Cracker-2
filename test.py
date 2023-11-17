# Assuming the Vigenere cipher implementation is already available, we can use it to
# decrypt the message using frequency analysis
import freqAnalysis
import vigenereCipher

encrypted_message = 'W uch hvwg kcfzr fsqcfr kvwzs aoywbu o kspgwhs tcf kcfzr fsqcfrg.'

def getFrequencyScore(message):
  # Implement code to calculate the frequency score of the message based on English words
  freqAnalysis.englishFreqMatchScore(message)
  pass


def decryptMessage(message):
  freqScores = []
  for key in range(26):
    decryptedText = vigenereCipher.decryptMessage(key, message)
    score = getFrequencyScore(decryptedText)
    freqScores.append((key, score))
  freqScores.sort(key=lambda x: x[1], reverse=True)
  return vigenereCipher.decryptMessage(freqScores[0][0], message)

print(decryptMessage(encrypted_message))