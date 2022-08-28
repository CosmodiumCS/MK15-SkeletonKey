#!/usr/bin/python

# leetspeek for [cryptex] project
# created by : Fyzz

# help menu for cipheringing process
help_menu = """
+------------------------------------------------------+
| [+] ARGUMENTS L33T 5P34K                             |
| [+] ARG 1. Process                                   |
|         [-e] ---------- Encrypt                      |
|         [-d] ---------- Decrypt                      |      
+------------------------------------------------------+                                             
| [+] ARG 2. Additional Aruments                       |
|         [-t <plaintext>] --------- Input Text        | 
|         [-i <input file>] -------- Input File [.txt] |
|         [-o <output file>] ------- Output File       |
+------------------------------------------------------+
| [+] Example:                                         |
|         cryptex l33t -e -t hello                     |
+------------------------------------------------------+
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