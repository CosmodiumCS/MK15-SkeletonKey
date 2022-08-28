#!/usr/bin/python

# caesar cipher package for the the codex project
# created by : C0SM0

# help menu for cipheringing process
help_menu = """
+---------------------------------------------------------+
|  [+] ARGUMENTS Caesar-Cipher                            |
|  [+] ARG 1. Ciphering Process                           |
|          [-e] ---------- Encrypt                        |
|          [-d] ---------- Decrypt                        |
|          [-b] ---------- Brute Force                    |
+---------------------------------------------------------+
|  [+] ARG 2. Additional Aruments                         |
|          [-k <int key>] ----------- Key                 |
|              [not required for bruteforcing '-b']       |
|          [-r <start,finish>] ------ Range               |
|          [-t <plaintext>] --------- Input Text          |
|          [-i <input file>] -------- Input File [.txt]   |
|          [-o <output file>] ------- Output File         |
|          [-e <plaintext>] --------- Custom exclude list |
+---------------------------------------------------------+  
|  [+] Example:                                           |
|          cryptex cc -e -k 5 -t hello -ex "asd[]"        |
+---------------------------------------------------------+
"""

# encodes caesar
def encode(input):
    output = ''
    text = input.text
    key = input.key
    exclude = input.exclude if input.exclude else "\n\t .?!,/\\<>|[]{}@#$%^&*()-_=+`~:;\"'0123456789"

    # encryption process
    if text and key:
        for character in text:
            if character in exclude:
                output += character
            elif character.isupper():
                output += chr((ord(character) + int(key) - 65) % 26 + 65)
            else:
                output += chr((ord(character) + int(key) - 97) % 26 + 97)
        return [output, True]
    else:
        return ["Please provide -k <key> argument", False]


# decodes caesar
def decode(input):
    output = ''
    text = input.text
    key = input.key
    exclude = input.exclude if input.exclude else "\n\t .?!,/\\<>|[]{}@#$%^&*()-_=+`~:;\"'0123456789"

    # decryption process
    if text and key:
        for character in text:
            if character in exclude:
                output += character
            elif character.isupper():
                output += chr((ord(character) - int(key) - 65) % 26 + 65)
            else:
                output += chr((ord(character) - int(key) - 97) % 26 + 97)

        return [output, True]
    else:
        return ["Please provide -k <key> argument", False]

# bruteforce caeser
def brute(input):
    output = []
    text = input.text
    exclude = input.exclude if input.exclude else "\n\t .?!,/\\<>|[]{}@#$%^&*()-_=+`~:;\"'0123456789"
    range_ = input.range.split(",") if input.range else [0, 27]
    shift_key = int(range_[0])

    if text:
        range_ = input.range.split(",") if input.range else [0, 27]
        shift_key = int(range_[0])

        for shift in range(int(range_[0]), int(range_[1])):
            shift_key += 1
            inner_output = ''
            for character in text:
                if character in exclude:
                    inner_output += character
                elif character.isupper():
                    inner_output += chr((ord(character) -
                                        shift - 65) % 26 + 65)
                else:
                    inner_output += chr((ord(character) -
                                        shift - 97) % 26 + 97)
            if inner_output != text:
                output.append(f'Key [{shift_key -1}] | {inner_output}')
        return ["\n".join(output), True]
    else:
        return ["Please provide -t <string input> argument", False]
