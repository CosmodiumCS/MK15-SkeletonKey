#!/usr/bin/python

# reverse cipher package for the the codex project
# created by : C0SM0

# help menu for ciphering options
help_menu = """
+-----------------------------------------------------+
|  [+] ARGUMENTS Multiplicative-Cipher                |
|  [+] ARG 1. Ciphering Process                       |
|        [-e] ---------- Encrypt                      |
|        [-d] ---------- Decrypt                      |
+-----------------------------------------------------+
|  [+] ARG 2. Additional Aruments                     |
|        [-k <int key>] ----------- Key               |
|        [-t <plaintext>] --------- Input Text        |
|        [-i <input file>] -------- Input File [.txt] |
|        [-o <output file>] ------- Output File       | 
+-----------------------------------------------------+   
|  [+] Example:                                       |
|  cryptex mc -e -k 7 -t hello                        |
+-----------------------------------------------------+
"""

# symbols that can't be processed through the cipher
symbols = ['\n', '\t', ' ', '.', '?', '!', ',', '/', '\\', '<', '>', '|',
           '[', ']', '{', '}', '@', '#', '$', '%', '^', '&', '*', '(', ')',
           '-', '_', '=', '+', '`', '~', ':', ';', '"', "'", '0', '1', '2', '3',
           '4', '5', '6', '7', '8', '9']

# check indexes for ciphering processes
index_dict = {
    'a':0,
    'b':1,
    'c':2,
    'd':3,
    'e':4,
    'f':5,
    'g':6,
    'h':7,
    'i':8,
    'j':9,
    'k':10,
    'l':11,
    'm':12,
    'n':13,
    'o':14,
    'p':15,
    'q':16,
    'r':17,
    's':18,
    't':19,
    'u':20,
    'v':21,
    'w':22,
    'x':23,
    'y':24,
    'z':25,
}

# gets index from letter
def get_index(letter):
    for l, i in index_dict.items():
        if letter == l:
            return i

# gets letter from index
def get_letter(index):
    for l, i in index_dict.items():
        if index == i:
            return l

# gets inverse for decryption
def inverse(a):
    for x in range(1, 26):
        if (((a%26) * (x%26)) % 26 == 1):
            return x
    return -1

# encodes multiplicative cipher
def encode(input):
    output = ''
    text = input.text
    key = input.key

    if key and text:
        # encryption process
        key = int(key)
        for character in text:

            # checks if character is symbol
            if character in symbols:
                output += character

            # checks if character is upper
            elif character.isupper():
                index = get_index(character.lower())
                new_index = (index * key) % 26
                cipher_character = get_letter(new_index)
                output += cipher_character.upper()

            # checks if character is lower
            else:
                index = get_index(character)
                new_index = (index * key) % 26
                cipher_character = get_letter(int(new_index))
                output += cipher_character

        return [output, True]
    else:
        return ["Please provide -k <key> argument", False]


# decodes multiplicative cipher
def decode(input):
    output = ''
    text = input.text
    key = input.key

    if key and text:
        # decryption process
        inverse_key = inverse(int(key))
        for character in text:

            # checks if character is symbol
            if character in symbols:
                output += character

            # checks if character is upper
            elif character.isupper():
                index = get_index(character.lower())
                new_index = (index * inverse_key) % 26
                cipher_character = get_letter(new_index)
                output += cipher_character.upper()

            # check if character is lower
            else:
                index = get_index(character)
                new_index = (index * inverse_key) % 26
                cipher_character = get_letter(new_index)
                output += cipher_character
                
        return [output, True]
    else:
        return ["Please provide -k <key> argument", False]
        


