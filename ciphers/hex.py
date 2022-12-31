#!/usr/bin/python
# reverse cipher package for the the codex project
# created by : C0SM0

# help menu for ciphering process
help_menu = """
USAGE:
  key hex [FLAGS] [OPTIONS]

FLAGS:
  -d, --decrypt  Decrypt input text or file
  -e, --encrypt  Encrypt input text or file

OPTIONS:
  -i, --inputFile <input file>   Input file to encrypt or decrypt
  -o, --output <output file>     Output file for encrypted or decrypted text
  -t, --text <text>              Input text to encrypt or decrypt

EXAMPLES:
  key hex -e -t "hello"
"""

# encode hex
def encode(input):
    # encode to hex
    text = input.text
    output = text.encode("utf-8").hex()

    return [output, True]

# decode hex
def decode(input):
    # decode to hex
    text = input.text
    output = bytes.fromhex(text).decode("utf-8")

    return [output, True]
