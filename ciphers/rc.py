#!/usr/bin/python

# reverse cipher package for the the codex project
# created by : C0SM0

# help menu for ciphering process
help_menu = """
+-------------------------------------------------------+
|  [+] ARGUMENTS Reverse Cipher                         |
|  [+] ARG 2. Additional Aruments                       |                                       
|          [-t <plaintext>] --------- Input Text        |
|          [-i <input file>] -------- Input File [.txt] |
|          [-o <output file>] ------- Output File       |
+-------------------------------------------------------+
|  [+] Example:                                         |
|  cryptex rc -e -t hello                               |
+-------------------------------------------------------+
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
