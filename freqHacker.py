import time

import detectEnglish
import freqAnalysis


def caesar_decrypt(ciphertext, shift):

    # Reset the plaintext to an empty string:
    plaintext = ''

    for char in ciphertext:

        if char.isalpha():

            # Figure out the offset if the character is uppercase or lowercase:
            ascii_offset = ord('a') if char.islower() else ord('A')

            # Shift the ASCII value of the character by the shift amount:
            decrypted_char = chr((ord(char) - ascii_offset - shift) % 26 +
                                 ascii_offset)

            # Add the decrypted character to the plaintext:
            plaintext += decrypted_char

        else:
            plaintext += char

    return plaintext


def crack_caesar_cipher(ciphertext):

    # Start the timer
    startTime = time.time()

    # Use freqAnalysis to get the frequency order
    freq_order = freqAnalysis.getFrequencyOrder(ciphertext)
    print('freq_order: ', freq_order)

    # Loop through the most common letters in the frequency order
    for common_letter in freq_order:
        print()

        # Calculate the shift assuming the next most common letter in ciphertext
        shift = (ord(common_letter) - ord('E')) % 26
        print('shift: ', shift)

        # Decrypt the ciphertext using the shift
        decrypted_text = caesar_decrypt(ciphertext, shift)
        print('decrypted_text: ', decrypted_text)

        # Check if the decrypted text is English-like
        isEnglish = detectEnglish.isEnglish(decrypted_text)
        print('isEnglish: ', isEnglish)

        if isEnglish:
            # Stop the timer
            endTime = time.time()
            print('Found English text after %.6f seconds.' %
                  (endTime - startTime))
            return decrypted_text  # Return the decrypted text if it's English-like

        #print()

    return ''  # Return an empty string if no English-like text is found


def main():

    # read in the message from the input file:
    with open('caesar_message.txt', 'r') as file:
        ciphertext = file.read()
    print('ciphertext: ', ciphertext)

    crackedtext = crack_caesar_cipher(ciphertext)
    print('crackedtext: ', crackedtext)


if __name__ == '__main__':
    print()
    main()
    print()
