#!/usr/bin/python

# created by : Haze

help_menu = """
Monoalphabetic Cipher

USAGE:
    key mo [FLAGS] [OPTIONS]

FLAGS:
    -e, --encode  Encode
    -d, --decode  Decode

OPTIONS:
    -t, --text    Input Text
"""

key = { 'a': 'c', 'b': 'd', 'c': 'e', 'd': 'f', 'e': 'g',
        'f': 'h', 'g': 'i', 'h': 'j', 'i': 'k', 'j': 'l',
        'k': 'm', 'l': 'n', 'm': 'o', 'n': 'p', 'o': 'q',
        'p': 'r', 'q': 's', 'r': 't', 's': 'u', 't': 'v',
        'u': 'w', 'v': 'x', 'w': 'y', 'x': 'z', 'y': 'a',
        'z': 'b', ' ': ' ', '1': '1', '2': '2', '3': '3',
        '4': '4', '5': '5', '6': '6', '7': '7', '8': '8',
        '9': '9', '0': '0', '!': '!', '@': '@', '#': '#',
        '$': '$', '%': '%', '^': '^', '&': '&', '*': '*',
        '(': '(', ')': ')', '-': '-', '_': '_', '=': '=',
        '+': '+', '[': '[', ']': ']', '{': '{', '}': '}',
        '\\': '\\', '|': '|', ';': ';', ':': ':', "'": "'",
        '"': '"', ',': ',', '<': '<', '.': '.', '/': '/',
        '?': '?' }

def encode(args):
    text = args.text

    if text:
        ciphertext = ""
        for i in text:
            if i.isupper():
                ciphertext += key[i.lower()].upper()

            else:
                ciphertext += key[i]

        output = "Encoding | {}\nEncoded | {}".format(
                text, ciphertext)

        return [output, True]

    else:
        return ['Error: No plaintext used [-t]', False]

def decode(args):
    text = args.text

    if text:
        plaintext = ""
        for i in text:
            for k, v in key.items():
                if i.isupper():
                    if v.upper() == i:
                        plaintext += k.upper()

                else:
                    if v == i:
                        plaintext += k
        
        output = "Decoding | {}\nDecoded | {}".format(
                text, plaintext)

        return [output, True]

    else:
        return ['Error: No plaintext used [-t]', False]
