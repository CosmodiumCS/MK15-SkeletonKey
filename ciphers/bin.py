#!/usr/bin/python

# created by : Fyzz
# New Arg Parse

# help menu for cipheringing process
help_menu = """
+------------------------------------------------------+
| [✓] ARGUMENTS Binary                                 |
| [✓] ARG 2. Additional Aruments                       |
|         [-t <plaintext>] --------- Input Text        |
|         [-i <input file>] -------- Input File [.txt] |
|         [-o <output file>] ------- Output File       |
+------------------------------------------------------+
| [✓] Example:                                         |
|  cryptex bin -e -t hello                             |
+------------------------------------------------------+
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