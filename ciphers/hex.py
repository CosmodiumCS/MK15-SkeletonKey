#!/usr/bin/python
# reverse cipher package for the the codex project
# created by : C0SM0

# help menu for ciphering process
help_menu = """
+-------------------------------------------------------+
|  [+] ARGUMENTS Hexadecimal                            |
|          [-e] -------- Encrypt                        |
|          [-d] -------- Decrypt                        |
|  [+] ARG 2. Additional Aruments                       |
|          [-t <plaintext>] --------- Input Text        |
|          [-i <input file>] -------- Input File [.txt] |
|          [-o <output file>] ------- Output File       |
+-------------------------------------------------------+
|  [+] Example:                                         |
|          cryptex hex -t hello                         |
+-------------------------------------------------------+
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