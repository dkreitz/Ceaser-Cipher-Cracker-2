# Inspired from Vigenere Cipher Dictionary Hacker
# http://inventwithpython.com/hacking (BSD Licensed)

import detectEnglish
import vigenereCipher


def main():
  # Read the input.txt file with the encrypted text
  with open('input.txt', 'r') as f:
    ciphertext = f.read()
    f.close()

  # Hack the text using the Vigenere Cipher
  hackedMessage = hackVigenere(ciphertext)

  if hackedMessage is not None:
    # SUCCESS
    print('Succeeded to hack encryption! (～￣▽￣)～ ')
    with open('output.txt', 'w') as f:
      f.write(hackedMessage)
      f.close()
  else:
    # FAIL
    print('Failed to hack encryption. (╯‵□′)╯︵┻━┻ ')


def hackVigenere(ciphertext):
  # Load in the dictionary of English words
  with open('dictionary.txt', 'r') as fo:
    words = fo.readlines()
    fo.close()

  # Loop through all possible keys using the entire dictionary of English words
  for word in words:
    word = word.strip()  # remove the newline character at the end

    decryptedText = vigenereCipher.decryptMessage(word, ciphertext)

    # If 40% of the decreypted words match English words,
    # check with user to see if the decrypted key has been found.
    if detectEnglish.isEnglish(decryptedText, wordPercentage=40):
      print()
      print('Possible encryption break:')
      print('Key ' + str(word) + ': ' + decryptedText[:100])
      print()
      print('Enter D for done, or just press Enter to continue breaking:')
      response = input('> ')

      if response.upper().startswith('D'):
        return decryptedText


if __name__ == '__main__':
  main()
