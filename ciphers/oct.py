#!/usr/bin/python

# octal cipher [encoding] package for the the codex project
# created by : Fyzz

# help menu for cipheringing process
help_menu = """
USAGE:
  key oct [FLAGS] [OPTIONS]

FLAGS:
  -d, --decode  Decrypt input text or file
  -e, --encode  Encrypt input text or file

OPTIONS:
  -i, --inputFile <input file>   Input file to encrypt or decrypt
  -o, --output <output file>     Output file for encrypted or decrypted text
  -t, --text <text>              Input text to encrypt or decrypt

EXAMPLES:
  key oct -e -t "hello"
"""

# encode octal
def encode(input):
    text = input.text
    output = []

    for character in text:
        output.append(oct(ord(character))[2:])
    
    return [" ".join(output),True]

# decode octal
def decode(input):
    text = input.text.split(" ")
    output = ''

    for character in text:
        output += chr(int(character, base = 8))

    return [output,True]
