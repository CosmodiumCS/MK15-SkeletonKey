#!/usr/bin/python

# created by : Mart | marvhus

from googletrans import Translator, LANGUAGES

# help menu for cipheringing process
help_menu = """
+----------------------------------------------------------+
| [✓] ARGUMENTS Google Translate                           |
|  [+] ARG 1. Ciphering Process                            |
|          [-tr] ---------- Translate                      |
|          [-b] ----------- Brute Force                    |
|          [-lang] -------- List languags                  |
+----------------------------------------------------------+
| [✓] ARG 2. Additional Aruments                           |
|         [-t <plaintext>] ------------ Input Text         |
|         [-src <language>] ----------  Src Language       |
|              [not required for bruteforcing '-b']        |
|         [-dest <language>] ---------- Dest Language      |
|              [not required for bruteforcing '-b']        |
|         [-i <input file>] ----------- Input File [.txt]  |
|         [-o <output file>] ---------- Output File        |
+----------------------------------------------------------+
| [✓] Example:                                             |
|  cryptex translate -tr -t "Hei"                          |
|  cryptex translate -b -t "こんにちは"                    |
+----------------------------------------------------------+
"""

# decode function [!] Each Cipher Must Have This <---------- [!]
def translate(args):
    # Getting text from all passed in args
    # All other args can be grabbed the same way
    # Example key = input.key | range = input.range
    text = args.text
    src_lang = args.src
    dest_lang = args.dest
    
    if text and src_lang in LANGUAGES and dest_lang in LANGUAGES:
        # Run Decode
        output = f'Translating | {text}\n'

        translator = Translator()

        translated = translator.translate(text, src=src_lang, dest=dest_lang)

        output += f'Translated | {translated.text}\n'
        output += f'Source Lang | {translated.src}\n'
        output += f'Destination Lang | {translated.dest}\n'

        # Output content as string for main.py to print
        # Pass True if Success Message
        return [output,True]
    else:
        # Pass False if Fail Message
        # Return Nothing to have no output

        # No valid text
        if not text:
            return ['No input text', False]

        # No valid source language
        if not src_lang in LANGUAGES:
            return [f'{src_lang} is not a valid short language code', False]

        # No valid destination language
        if not dest_lang in LANGUAGES:
            return [f'{dest_lang} is not a valid short language code', False]
        
        # Something else happned
        return ['Unknow Error', False]

# brute function [!] Optional Per Cipher <----------------- [!]
def brute(args):
    # Getting text from all passed in args
    # All other args can be grabbed the same way
    # Example key = input.key | range = input.range
    text = args.text
    
    if text:
        # Run Decode
        output = f'Bruteforcing | {text}\n'

        translator = Translator()

        translated = translator.translate(text)

        output += f'Translated | {translated.text}\n'
        output += f'Source Lang | {translated.src}\n'
        output += f'Destination Lang | {translated.dest}\n'

        # Output content as string for main.py to print
        # Pass True if Success Message
        return [output,True]
    else:
        # Pass False if Fail Message
        # Return Nothing to have no output

        # No input text
        if not text:
            return ['No input text', False]

        return ['Unknown Error', False]

def languages():

    output = "----- Short ----- Long -----\n"

    for _, lang in enumerate(LANGUAGES):
        output += f'    - {lang}  \t- {LANGUAGES[lang]}\n'

    return [output, True]
