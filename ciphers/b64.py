#!/usr/bin/python
# base64 cipher [encoding] package for the the codex project

# created by : Fyzz

import base64

# help menu for cipheringing process
help_menu = """
USAGE:
  key b64 [FLAGS] [OPTIONS]

FLAGS:
  -d, --decode  Decrypt input text or file
  -e, --encode  Encrypt input text or file

OPTIONS:
  -i, --inputFile <input file>   Input file to encrypt or decrypt
  -o, --output <output file>     Output file for encrypted or decrypted text
  -t, --text <text>              Input text to encrypt or decrypt

EXAMPLES:
  key b64 -e -t "hello"
"""

# encode base64
def encode(input):

    text = input.text.encode('ascii')
    b64_bytes = base64.b64encode(text)
    output = b64_bytes.decode('ascii')

    return [output, True]

    

# decode base64
def decode(input):

    text = input.text.encode('ascii')
    b64_bytes = base64.b64decode(text)
    output = b64_bytes.decode('ascii')

    return [output, True]
