# Inspired from the Vigenere Cipher (Polyalphabetic Substitution Cipher)
# http://inventwithpython.com/hacking (BSD Licensed)

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
  myMessage = 'Jacques knows how to write code.'

  translated = ''
  myKey = 'DREADNOUGHT'
  myMode = 'encrypt'  # set to 'encrypt' or 'decrypt'

  if myMode == 'encrypt':
    translated = encryptMessage(myKey, myMessage)
  elif myMode == 'decrypt':
    translated = decryptMessage(myKey, myMessage)

  print('%sed message:' % (myMode.title()))
  print(translated)


def encryptMessage(key, message):
  return translateMessage(key, message, 'encrypt')


def decryptMessage(key, message):
  return translateMessage(key, message, 'decrypt')


def translateMessage(key, message, mode):
  translated = []  # stores the encrypted/decrypted message string

  keyIndex = 0
  key = key.upper()

  for symbol in message:  # loop through each character in message
    num = LETTERS.find(symbol.upper())
    if num != -1:  # -1 means symbol.upper() was not found in LETTERS
      if mode == 'encrypt':
        num += LETTERS.find(key[keyIndex])  # add if encrypting
      elif mode == 'decrypt':
        num -= LETTERS.find(key[keyIndex])  # subtract if decrypting

      num %= len(LETTERS)  # handle the potential wrap-around

      # add the encrypted/decrypted symbol to the end of translated.
      if symbol.isupper():
        translated.append(LETTERS[num])
      elif symbol.islower():
        translated.append(LETTERS[num].lower())

      keyIndex += 1  # move to the next letter in the key
      if keyIndex == len(key):
        keyIndex = 0

    else:
      # The symbol was not in LETTERS, so add it to translated as is.
      translated.append(symbol)

  return ''.join(translated)


# If vigenereCipher.py is run (instead of imported as a module) call
# the main() function.
if __name__ == '__main__':
  main()
