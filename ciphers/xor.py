#!/usr/bin/python
# XOR Cipher
# created by : Fyzz

# help menu for cipheringing process
help_menu = """
+-------------------------------------------------------+
|  [+] ARGUMENTS Xor                                    |
|  [+] ARG 1. Process                                   |
|          [-e] ---------- Encrypt                      |
|          [-d] ---------- Decrypt                      |
+-------------------------------------------------------+
|  [+] ARG 2. Additional Aruments                       |
|          [-t <plaintext>] --------- Input Text        |
|          [-i <input file>] -------- Input File [.txt] |
|          [-o <output file>] ------- Output File       |
|          [-k <key>] --------------- Key               |
+-------------------------------------------------------+ 
|  [+] Example:                                         |
|          cryptex xor -e -t hello -k key               |
+-------------------------------------------------------+
"""

def encode(input):
    key = input.key
    text = input.text

    if key and text:
        output = " ".join([chr(ord(c1) ^ ord(c2)) for (c1,c2) in zip(text,key)])
        return [output, True]
    else:
        return ["Please provide -k <key> argument", False]
    

    return output

def decode(input):
    key = input.key
    text = input.text

    if key and text:
        output = " ".join([chr(ord(c1) ^ ord(c2)) for (c1,c2) in zip(text,key)])
        return [output, True]
    else:
        return ["Please provide -k <key> argument", False]