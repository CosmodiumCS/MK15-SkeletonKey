#!/usr/bin/python
# vigenere cipher package for the the codex project
# created by : C0SM0

# imports
import os

# credits:
# - Andrew Paul for frequency formula

# help menu for cipheringing process
help_menu = """
+---------------------------------------------------------------+
|  [+] ARGUMENTS Vigenere Cipher                                |
|  [+] ARG 1. Ciphering Process                                 |
|          [-e] ---------- Encrypt                              |
|          [-d] ---------- Decrypt                              |
|          [-b] ---------- Brute Force                          |
+---------------------------------------------------------------+ 
|  [+] ARG 2. Additional Aruments                               |
|          [-k <key>] --------------- Key                       | 
|              [not required for bruteforcing '-b']             |
|          [-t <plaintext>] --------- Input Text                |
|          [-i <input file>] -------- Input File [.txt]         |
|          [-o <output file>] ------- Output File               |
|          [-l <max key length>] ---- Max Key Length [for '-b'] |
+---------------------------------------------------------------+
|  [+] Example:                                                 |
|          cryptex vc -e -t hello -k world                      |
+---------------------------------------------------------------+
"""

# letters for encryption process
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
MAX_KEY_LENGTH = 20
alphabet = 'abcdefghijklmnopqrstuvwxyz'

# symbols that can't be processed through the cipher
SYMBOLS = ['\n', '\t', ' ', '.', '?', '!', ',', '/', '\\', '<', '>', '|',
           '[', ']', '{', '}', '@', '#', '$', '%', '^', '&', '*', '(', ')',
           '-', '_', '=', '+', '`', '~', ':', ';', '"', "'", '0', '1', '2', '3',
           '4', '5', '6', '7', '8', '9']

# Array containing the relative frequency of each letter in the English language
english_frequences = [0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015,
					  0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749,
					  0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758,
					  0.00978, 0.02360, 0.00150, 0.01974, 0.00074]

# encode vigenere
def encode(input):
    output = []
    text = input.text
    key = input.key
    index = 0
   
    if text and key:
        # format key
        key = key.upper()
        # ciphering process
        for character in text:
            num = LETTERS.find(character.upper())

            # starts encryption
            if num != -1:
                num += LETTERS.find(key[index])
                num %= len(LETTERS)
                
                # check for symbols
                if character in SYMBOLS:
                    output.append(character)

                # check for uppercase
                elif character.isupper():
                    output.append(LETTERS[num])

                # check for lowercase and others
                else:
                    output.append(LETTERS[num].lower())

                # update index
                index += 1
                
                # stop process when ciphering is done
                if index == len(key):
                    index = 0

            # adds character in case of error
            else:
                output.append(character)
        return ["".join(output), True]
    else:
        return ["Please provide -k <key> argument", False]

# decode process
def decode(input):
    output = []
    text = input.text
    key = input.key
    index = 0

    if text and key:
        # format key
        key = key.upper()
        # ciphering process
        for character in text:
            num = LETTERS.find(character.upper())

            # starts encrypiton
            if num != -1:
                num -= LETTERS.find(key[index])
                num %= len(LETTERS)
                
                # check for symbols
                if character in SYMBOLS:
                    output.append(character)

                # check for uppercase
                elif character.isupper():
                    output.append(LETTERS[num])

                # check for lowercase and others
                else:
                    output.append(LETTERS[num].lower())

                # update index
                index += 1
                
                # stop process when ciphering is done
                if index == len(key):
                    index = 0

            # adds character in case of error
            else:
                output.append(character)
        return ["".join(output), True]
    else:
        return ["Please provide -k <key> argument", False]

# gets index through councidence
def get_index_c(ciphertext):
	
	N = float(len(ciphertext))
	frequency_sum = 0.0

	# using Index of Coincidence formula
	for letter in alphabet:
		frequency_sum += ciphertext.count(letter) * (ciphertext.count(letter)-1)

	# using Index of Coincidence formula
	ic = frequency_sum/(N*(N-1))
	return ic

# returns key length with highest average
def get_key_length(ciphertext):
	ic_table=[]

    # iterates through [possible] key sequences
	for guess_len in range(MAX_KEY_LENGTH):
		ic_sum = 0.0
		avg_ic = 0.0
		for i in range(guess_len):
			sequence = ''
			# breaks the ciphertext into sequences
			for j in range(0, len(ciphertext[i:]), guess_len):
				sequence += ciphertext[i+j]
			ic_sum += get_index_c(sequence)

		if not guess_len == 0:
			avg_ic = ic_sum / guess_len
		ic_table.append(avg_ic)

	# returns the most likeyly key length
	best_guess = ic_table.index(sorted(ic_table, reverse = True)[0])
	second_best_guess = ic_table.index(sorted(ic_table, reverse = True)[1])

	if best_guess % second_best_guess == 0:
		return second_best_guess
	else:
		return best_guess

# get the letter of the key that needs to be shifted
def freq_analysis(sequence):
	all_chi_squareds = [0] * 26

	for i in range(26):
		chi_squared_sum = 0.0

		sequence_offset = [chr(((ord(sequence[j])-97-i)%26)+97) for j in range(len(sequence))]
		v = [0] * 26

		# count the numbers of each letter in the sequence_offset already in ascii
		for l in sequence_offset:
			v[ord(l) - ord('a')] += 1
            
		# divide the array by the length of the sequence to get the frequency percentages
		for j in range(26):
			v[j] *= (1.0/float(len(sequence)))

		# compate frequencies
		for j in range(26):
			chi_squared_sum+=((v[j] - float(english_frequences[j]))**2)/float(english_frequences[j])

		# append it all
		all_chi_squareds[i] = chi_squared_sum

	# return the letter of the key that it needs to be shifted by
	shift = all_chi_squareds.index(min(all_chi_squareds))
	return chr(shift+97)

# gets key
def get_key(ciphertext, key_length):
	key = ''

	# calculate letter frequency table for each letter of the key
	for i in range(key_length):
		sequence = ''

		# breaks the ciphertext into sequences
		for j in range(0,len(ciphertext[i:]), key_length):
			sequence += ciphertext[i+j]

		key += freq_analysis(sequence)

	return key

def brute(input):
    text = ''.join(x.lower() for x in input.text if x.isalpha())

    # tries to get key
    try:
        # calculating the key data
        key_length = get_key_length(text)
        key = get_key(text, key_length)

        # outputting key data
        print(f'Most Probable Key Length: {key_length}')
        print(f'Key: {key}\n')

        # decrypting vigenere
        input.key = key
        print(input.key)
        decode(input)
    
    # if the plaintext was too small
    except ZeroDivisionError:
        print('The ciphertext you entered was to small for this algorithm\nPlease add more ciphertext')