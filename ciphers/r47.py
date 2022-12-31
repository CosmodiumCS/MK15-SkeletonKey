#!/usr/bin/python
# New Rot47 cipher for the the codex project

# created by : Fyzz

# help menu for cipheringing process
help_menu = """
USAGE:
  key r47 [FLAGS] [OPTIONS]

FLAGS:
  -d, --decode  Decrypt input text or file
  -e, --encode  Encrypt input text or file

OPTIONS:
  -i, --inputFile <input file>   Input file to encrypt or decrypt
  -o, --output <output file>     Output file for encrypted or decrypted text
  -t, --text <text>              Input text to encrypt or decrypt

EXAMPLES:
  key r47 -e -t hello
"""

# encode r47
def encode(input):

    text = input.text
    output = ''

    for index in text:
        encoded = ord(index)
        if encoded >= 33 and encoded <= 126:
            output += chr(33 + ((encoded + 14) % 94))
        else:
            output += index
    return [output, True]
    

# decode r47
def decode(input):

    text = input.text
    output = ''

    for index in text:
        encoded = ord(index)
        if encoded >= 33 and encoded <= 126:
            output += chr(33 + ((encoded + 14) % 94))
        else:
            output += index
    return [output, True]
