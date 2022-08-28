#!/usr/bin/python

# octal cipher [encoding] package for the the codex project
# created by : Fyzz

# help menu for cipheringing process
help_menu = """
+-------------------------------------------------------+
|  [+] ARGUMENTS Octal                                  |
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
|          cryptex oct -e -t hello                      |
+-------------------------------------------------------+
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