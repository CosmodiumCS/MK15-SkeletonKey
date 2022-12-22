#!/usr/bin/python

# created by : Fyzz
# New Arg Parse

# help menu for cipheringing process
help_menu = """
USAGE:
  key bin [FLAGS] [OPTIONS]

FLAGS:
  -d, --decode  Decrypt input text or file
  -e, --encode  Encrypt input text or file

OPTIONS:
  -i, --inputFile <input file>   Input file to encrypt or decrypt
  -o, --output <output file>     Output file for encrypted or decrypted text
  -t, --text <text>              Input text to encrypt or decrypt

EXAMPLES:
  key bin -e -t "hello"
"""
# encode binary
def encode(input):
    text = input.text
    output = ' '.join(format(ord(x), 'b') for x in text)

    return [output, True]

# decode binary
def decode(input):
    text = input.text

    binary_list = text.split(' ')
    output = ''
    for binary in binary_list:
        output += chr(int(binary, 2))

    return [output,True]
