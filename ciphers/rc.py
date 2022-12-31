#!/usr/bin/python

# reverse cipher package for the the codex project
# created by : C0SM0

# help menu for ciphering process
help_menu = """
USAGE:
  key rc [FLAGS] [OPTIONS]

FLAGS:
  -d, --decrypt  Decrypt input text or file
  -e, --encrypt  Encrypt input text or file

OPTIONS:
  -i, --inputFile <input file>   Input file to encrypt or decrypt
  -o, --output <output file>     Output file for encrypted or decrypted text
  -t, --text <text>              Input text to encrypt or decrypt

EXAMPLES:
  key rc -e -t "hello"
"""

# encode reverse
def encode(input):
    text = input.text
    output = text[::-1]
    return [output, True]

# decode reverse
def decode(input):
    text = input.text
    output = text[::-1]
    return [output, True]
