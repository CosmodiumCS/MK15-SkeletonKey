#!/usr/bin/python
# New Rot47 cipher for the the codex project

# created by : Fyzz

# help menu for cipheringing process
help_menu = """
+-------------------------------------------------------+
|  [+] ARGUMENTS Rot47                                  |
|  [+] ARG 1. Process                                   |
|          [-e] ---------- Encrypt                      |
|          [-d] ---------- Decrypt                      |
+-------------------------------------------------------+
|  [+] ARG 2. Additional Aruments                       |
|          [-t <plaintext>] --------- Input Text        |
|          [-i <input file>] -------- Input File [.txt] |
|          [-o <output file>] ------- Output File       |
+-------------------------------------------------------+ 
|  [+] Example:                                         |
|          cryptex r47 -e -t hello                      |
+-------------------------------------------------------+
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