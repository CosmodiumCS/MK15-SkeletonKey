#!/usr/bin/env python3

# made by : H4Z3

# https://pypi.org/project/twofish/
from twofish import Twofish

help_menu = """
USAGE:
  key twofish [FLAGS] [OPTIONS]

FLAGS:
  -d, --decode   Decrypt input text or file
  -e, --encode   Encrypt input text or file

OPTIONS:
  -i, --inputFile <input file>   Input file to encrypt or decrypt
  -k, --key <key>                Encryption key (1-32 characters)
  -o, --output <output file>     Output file for encrypted or decrypted text
  -t, --text <text>              Input text to encrypt or decrypt (16 bytes)

EXAMPLES:
  key twofish -e -t YELLOWSUBMARINES -k mySecretKey
  key twofish -d -t 27570f92486cff1b8bf056671533864b -k mySecretKey
"""

def encode(args):
    text = args.text
    key = args.key

    # check for valid input
    if text and key:
        # check for valid block & key length
        if len(text.encode('utf-8')) == 16 and len(key) <= 32:
            secret = Twofish(bytes(key.encode('ascii')))
            rawciphertext = secret.encrypt(bytes(text.encode('ascii')))
            ciphertext = rawciphertext.hex()

            output = f"Encrypting | {text}\nKey | {key}\nRaw Ciphertext | {rawciphertext}\nCiphertext | {ciphertext}"

            # check for output file
            return [ciphertext, True] if args.output else [output, True]
        else:
            if len(text.encode('utf-8')) != 16:
                return [f'Error: Invalid Block Length {text}, must be 16 bytes', False]

            elif len(key) > 32:
                return [
                    f'Error: Invalid key Length {key}, must be 1 to 32 characters long',
                    False,
                ]

            else:
                return ['Error: Make sure to have a 16 byte block and a key', False]

    elif text is None and key is None:
        return ['Error: No text or key supplied', False]

    elif text is None:
        return ['Error: No text supplied', False]

    elif key is None:
        return ['Error: No key supplied', False]

    else:
        return ['Error: Make sure to use a 16 byte string and a key', False]

def decode(args):
    ciphertext = args.text
    key = args.key

    if ciphertext and key:
        return decryption(key, ciphertext, args)
    if ciphertext is None and key is None:
        return ['Error: No text or key supplied', False]

    elif ciphertext is None:
        return ['Error: No text supplied', False]

    elif key is None:
        return ['Error: No key supplied', False]

    else:
        return ['Error: Make sure to use a 16 byte string and a key', False]


def decryption(key, ciphertext, args):
    if len(key) > 32:
        return [
            f'Error: Invalid key Length {key}, must be 1 to 32 characters long',
            False,
        ]

    secret = Twofish(bytes(key.encode('ascii')))
    rawciphertext = bytes.fromhex(ciphertext)

    # decode attempt
    try:
        plaintext = secret.decrypt(bytes.fromhex(ciphertext)).decode()

    except Exception:
        plaintext = secret.decrypt(bytes.fromhex(ciphertext))

    output = f"Decrypting | {ciphertext}\nRaw Ciphertext | {rawciphertext}\nKey | {key}\nPlaintext | {plaintext}"

    return [plaintext, True] if args.output else [output, True]
