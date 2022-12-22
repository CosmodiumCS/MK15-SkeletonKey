#!/usr/bin/python

# leetspeek for [cryptex] project
# created by : Fyzz

# help menu for cipheringing process
help_menu = """
USAGE:
  key 1337 [FLAGS] [OPTIONS]

FLAGS:
  -d, --decode  Decrypt input text or file
  -e, --encode  Encrypt input text or file

OPTIONS:
  -i, --inputFile <input file>   Input file to encrypt or decrypt
  -o, --output <output file>     Output file for encrypted or decrypted text
  -t, --text <text>              Input text to encode or decode

EXAMPLES:
  key 1337 -e -t hello
"""

# leet chr
leet_dictionary_enc = {
    "a":"4",
    "b":"8",
    "e":"3",
    "g":"6",
    "i":"1",
    "o":"0",
    "s":"5",
    "t":"7"
}

# invert leet chr
leet_dictionary_dec = dict((v,k) for (k,v) in leet_dictionary_enc.items())

# encode leet
def encode(input):

    text = input.text.lower()
    output = ''

    for character in text:
        if character in leet_dictionary_enc:
            output += leet_dictionary_enc[character]
        else:
            output += character
    return [output.capitalize(), True]

# decode leet
def decode(input):

    text = input.text.lower()
    output = ''

    for character in text:
        if character in leet_dictionary_dec:
            output += leet_dictionary_dec[character]
        else:
            output += character
    return [output.capitalize(), True]
