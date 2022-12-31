#!/usr/bin/python

# Rot13 package for the the codex project
# created by : C0SM0 | Fyzz

# imports
import os

# help menu for cipheringing process
help_menu = """
USAGE:
  key r13 [FLAGS] [OPTIONS]

FLAGS:
  -d, --decode  Decrypt input text or file
  -e, --encode  Encrypt input text or file

OPTIONS:
  -i, --inputFile <input file>   Input file to encrypt or decrypt
  -o, --output <output file>     Output file for encrypted or decrypted text
  -t, --text <text>              Input text to encrypt or decrypt

EXAMPLES:
  key r13 -e -t hello
"""

def encode(args):
    from ciphers.cc import encode
    args.key = 13
    return encode(args)

def decode(args):
    from ciphers.cc import decode
    args.key = 13
    return decode(args)
