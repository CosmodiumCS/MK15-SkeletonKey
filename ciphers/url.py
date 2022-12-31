#!/usr/bin/python

import urllib.parse

# created by : Haze

help_menu = """
USAGE:
    url [FLAGS] [OPTIONS]

FLAGS:
    -e, --encode  Encode
    -d, --decode  Decode

OPTIONS:
    -t, --text  Input Text
"""

def encode(args):
    text = args.text

    if text:
        encoded = urllib.parse.quote(text)

        output = "Encoding | {}\nEncoded | {}".format(
            text, encoded)

        return [output, True]

    else:
        return ['Error: Make sure to add plaintext [-t]', False]

def decode(args):
    text = args.text

    if text:
        decoded = urllib.parse.unquote(text)

        output = "Decoding | {}\nDecoded | {}".format(
            text, decoded)

        return [output, True]

    else:
        return ['Error: Make sure to add plaintext [-t]', False]

