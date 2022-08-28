#!/usr/bin/python
# base64 cipher [encoding] package for the the codex project

# created by : Fyzz

import base64

# help menu for cipheringing process
help_menu = """
+-------------------------------------------------------+
|  [+] ARGUMENTS Base64                                 |
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
|          cryptex b64 -e -t "hello"                    |
+-------------------------------------------------------+
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