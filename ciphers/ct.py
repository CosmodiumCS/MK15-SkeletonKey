#!/usr/bin/python

# created by : C0SM0

# imports
import enchant
import string

# help menu for cipheringing process
help_menu = """
USAGE:
  key ct [FLAGS] [OPTIONS]

FLAGS:
  -b, --bruteforce   Bruteforce input text or file

OPTIONS:
  -i, --inputFile <input file>   Input file to encrypt or decrypt
  -o, --output <output file>     Output file for encrypted or decrypted text
  -t, --text <text>              Input text to encrypt or decrypt
  -a, --alphabet "<letters>"     Use a custom alphabet ["A" will always be iterated through]
  -words, --words                Pull out words from decoded transcripts
  -lingo, --lingo <dictionary>   Set language for words to pull out [default "en_US"]

NOTES:
  This program can get very memory intensive and crash your
  computer, so keep the transcripts short :)

  lowercase text can be used to escape the code transcript
  so if we knew the first two letters were "b" and "a", we
  could filter as such:

  key ct -b -t "baAAs!"

EXAMPLES:
  key ct -b -t "ABCC"
  key ct -b -t "ABCC" -words -l "en_US"
  key ct -b -t "ABCC" -words -a "EFGH123"
"""

# -a, --alphabet <sequence>      Input custom alphabet to iterate through # add me

# decode function [!] Each Cipher Must Have This <---------- [!]
def encode(args):
    # Getting text from all passed in args
    # All other args can be grabbed the same way
    # Example key = input.key | range = input.range
    text = args.text
    
    return ['This cipher does not have encoding capabilites', False]

# decode function [!] Each Cipher Must Have This <---------- [!]
def decode(args):
    # Getting text from all passed in args
    # All other args can be grabbed the same way
    # Example key = input.key | range = input.range
    text = args.text

    return ['This cipher does not have decoding capabilites', False]


# dictionary detection
def dictionary(transcripts, language):

    # set language for dictionary detection
    language = enchant.Dict(language)
    output = []

    for transcript in transcripts:

        # show transcript if it is a word
        if language.check(transcript.lower()):
            output.append(transcript.lower()) 

    return output

# brute force code transcript
def decode_transcripts(transcript_list, alphabet, custom_alphabet, count=1):
    output_transcripts = []
    global TRANSCRIPT_SET
    global TRANSCRIPT

    for transcript in transcript_list:

        # ignore lowercase and special characters
        remove_lower = str.maketrans('', '', string.ascii_lowercase)
        remove_punctuation = str.maketrans('', '', string.punctuation)
        format_transcript = transcript.translate(remove_lower)
        new_transcript = format_transcript.translate(remove_punctuation)

        transcript_set = set(new_transcript)

        # get characters that are shared in both transcripts
        for character in (TRANSCRIPT_SET & transcript_set):
                
            for letter in (alphabet):
            # for letter in alphabet:
                # ignore repeated characters

                # TODO: fix theses goofy ahh checks
                if (len(transcript_set) == 1) and (letter in transcript_set) and ((new_transcript == transcript)): 
                    continue
                if (len(transcript_set) > 1) and (letter in transcript_set):
                    continue
               
                plaintext = transcript.replace(character, letter)
                output_transcripts.append(plaintext)

    output = list(set(output_transcripts))

    if count == len(TRANSCRIPT):
        return output

    return decode_transcripts(output, alphabet, custom_alphabet, (count+1))

# brute function [!] Optional Per Cipher <----------------- [!]
def brute(args):
    # Getting text from all passed in args
    text = args.text
    word = args.words
    lang = args.lingo 
    alphabet = args.alphabet
    custom_alphabet = False

    # format alphabet
    if 'A' not in alphabet:
        alphabet = set(alphabet)
        alphabet.add('A') 
        alphabet = ''.join(alphabet)
        custom_alphabet = True

    if text:
        # Run Decode
        output = f'Bruteforcing | {text}'

        global TRANSCRIPT_SET 
        global TRANSCRIPT
        TRANSCRIPT_SET = set(text)
        TRANSCRIPT = text

        transcripts = decode_transcripts([text], alphabet, custom_alphabet)

        # filter out words
        if word:
            print(word)
            words = dictionary(transcripts, lang)
            return [f'{output}\n{transcripts}\n\nWords:\n{words}',True]

        # Output content as string for main.py to print
        # Pass True if Success Message
        return [f'{output}\n\n{transcripts}',True]
    else:
        # Pass False if Fail Message
        # Return Nothing to have no output
        return ['An error occured, please try again', False]
