# Caesar Cipher
# https://www.nostarch.com/crackingcodes (BSD Licensed)
import random

# Every possible symbol that can be encrypted:
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# The string to be encrypted/decrypted:
#message = 'Julian needs a bath.'

# Read in the message from the input file:
with open('original_message.txt', 'r') as file:
    message = file.read()

# The encryption/decryption key:
#key = 13

# Set the key using a random number within the range of the SYMBOLS:
key = random.randint(0, len(SYMBOLS) - 1)
print('key: ', key)

# Whether the program encrypts or decrypts:
mode = 'encrypt'  # Set to either 'encrypt' or 'decrypt'.

# Stores the encrypted/decrypted form of the message:
translated = ''

# Capitalize the message:
message = message.upper()

for symbol in message:

  # Note: Only symbols in the `SYMBOLS` string can be encrypted/decrypted.
  if symbol in SYMBOLS:

    translatedIndex = 0
    symbolIndex = SYMBOLS.find(symbol)

    # Perform encryption/decryption:
    if mode == 'encrypt':
      translatedIndex = symbolIndex + key
    elif mode == 'decrypt':
      translatedIndex = symbolIndex - key

    # Handle wrap-around, if needed:
    if translatedIndex >= len(SYMBOLS):
      translatedIndex = translatedIndex - len(SYMBOLS)
    elif translatedIndex < 0:
      translatedIndex = translatedIndex + len(SYMBOLS)

    # Append the encrypted/decrypted symbol:
    translated = translated + SYMBOLS[translatedIndex]

  else:
    # Append the symbol without encrypting/decrypting:
    translated = translated + symbol

# Output the translated string:
print(translated)

# Save the translated string to a file:
with open('caesar_message.txt', 'w') as file:
    file.write(translated)
