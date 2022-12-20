#!/usr/bin/env python3

# made by : H4Z3

import blowfish # https://pypi.org/project/blowfish/
from operator import xor
from os import urandom

help_menu = """
┌──────────────────────────────────────────────────────────────────────────────────┐
│ [■] ARGUMENTS Blowfish                                                           │
│ [■] ARG 1. Encrypting/Decrypting Process                                         │
│  └───┬─ [-e] ────────────────────────────────── Encrypt                          │
│      └─ [-d] ────────────────────────────────── Decrypt                          │
│ [■] ARG 2. Additional Aruments                                                   │
│  └───┬─ [-t <text>] ─┬───────────────────────── Input Text                       │
│      │               └─ Read mode description                                    │
│      ├─ [-k <key> ] ─┬───────────────────────── Encryption Key                   │
│      │               ├─ 4 to 56 characters                                       │
│      │               └─ Required for all modes                                   │
│      ├─ [-iv <iv>] ─┬────────────────────────── Encryption IV                    │
│      │              └─ 8 bytes                                                   │
│      ├─ [-nc <nonce>] ─┬─────────────────────── Encryption Nonce                 │
│      │                 └─ Not required                                           │
│      ├─ [-i <input file>] ───────────────────── Input File [.txt]                │
│      └─ [-o <output file>] ──────────────────── Output File                      │
│ [■] ARG 3. Mode                                                                  │
│  ├───── [-md <mode>] ────────────────────────── Encryption Mode                  │
│  └──┬─ [Block] ──────── Encrypt 8 bytes of data                                  │
│     ├─ [ECB] ─┬──────── Electronic Codebook Mode                                 │
│     │         └─ Plaintext data must be an exact multiple of 8 bytes             │
│     ├─ [ECB-CTS] ─┬──── Electronic Codebook Mode with Cipher Text Stealing       │
│     │             └─ Plaintext data must be greater than 8 bytes                 │
│     ├─ [CBC] ─┬──────── Cipher-Block Chaining mode                               │
│     │         ├─ Plaintext data must be an exact multiple of 8 bytes             │
│     │         └─ IV required                                                     │
│     ├─ [CBC-CTS] ─┬──── Cipher-Block Chaining with Ciphertext Stealing           │
│     │             ├─ Plaintext data must be greater than 8 bytes                 │
│     │             └─ IV required                                                 │
│     ├─ [PCBC] ─┬─────── Propagating Cipher-Block Chaining Mode                   │
│     │          ├─ Plaintext data must be an exact multiple of 8 bytes            │
│     │          └─ IV required                                                    │
│     ├─ [CFB] ─┬──────── Cipher Feedback Mode                                     │
│     │         ├─ Plaintext can operate on any data of any length                 │
│     │         └─ IV required                                                     │
│     ├─ [OFB] ─┬──────── Output Feedback Mode                                     │
│     │         ├─ Plaintext can operate on any data of any length                 │
│     │         └─ IV required                                                     │
│     └─ [CTR] ─┬──────── Counter Mode                                             │
│               ├─ Plaintext can operate on any data of any length                 │
│               └─ Nonce is required, but will be generated if not present         │
├──────────────────────────────────────────────────────────────────────────────────┤
│ [■] Example:                                                                     │
│  key blowfish -e -t 'Hello World!' -k mySecretKey -iv 12345678 -md cfb           │
│  key blowfish -d -t 1a284cacd7cfc9b9ef46e142 -k mySecretKey -iv 12345678 -md cfb │
└──────────────────────────────────────────────────────────────────────────────────┘
"""

modes = ['block', 'ecb', 'ecb-cts', 'cbc', 'cbc-cts', 'pcbc', 'cfb', 'ofb', 'ctr']

def encode(args):
    text = args.text
    key = args.key
    mode = args.mode
    iv = args.iv
    nonce = args.nonce

    # check if key, text and mode is present
    if key and text and mode:
        # check for valid key length
        if len(key) >= 4 and len(key) <= 56 and mode.lower() in modes:
            # encryption key
            secret = blowfish.Cipher(bytes(key.encode('ascii')))

            if mode.lower() == 'block':
                # check for valid plaintext length
                if len(text.encode('utf-8')) == 8:
                    rawciphertext = secret.encrypt_block(bytes(text.encode('ascii')))
                    ciphertext = rawciphertext.hex()

                    output = "Encrypting | {}\nKey | {}\nMode | {}\nRaw Ciphertext | {}\nCiphertext | {}".format(
                            text, key, mode.lower().capitalize(), rawciphertext, ciphertext)

                    return [output, True]

                # invalid plaintext length handling
                else:
                    return ['Error: Invalid plaintext length, must be 8 bytes', False]
        
            elif mode.lower() == 'ecb':
                # check for valid plaintext length
                if len(text.encode('utf-8')) % 8 == 0:
                    rawciphertext = b''.join(secret.encrypt_ecb(bytes(text.encode('ascii'))))
                    ciphertext = rawciphertext.hex()

                    output = "Encrypting | {}\nKey | {}\nMode | {}\nRaw Ciphertext | {}\nCiphertext | {}".format(
                            text, key, mode.upper(), rawciphertext, ciphertext)

                    return [output, True]
                
                # invalid plaintext length handling
                else:
                    return ['Error: Invalid plaintext length, must be an exact multiple of 8 bytes']

            elif mode.lower() == 'ecb-cts':
                # check for valid plaintext length
                if len(text.encode('utf-8')) > 8:
                    rawciphertext = b''.join(secret.encrypt_ecb_cts(bytes(text.encode('ascii'))))
                    ciphertext = rawciphertext.hex()

                    output = "Encrypting | {}\nKey | {}\nMode | {}\nRaw Ciphertext | {}\nCiphertext | {}".format(
                            text, key, mode.upper(), rawciphertext, ciphertext)

                    return [output, True]

                # invalid plaintext length handling
                else:
                    return ['Error: Invalid plaintext length, must be greater than 8 bytes', False]

            elif mode.lower() == 'cbc':
                # check for valid plaintext length and if IV is present
                if len(text.encode('utf-8')) % 8 == 0 and len(iv.encode('utf-8')) == 8:
                    rawciphertext = b''.join(secret.encrypt_cbc(bytes(text.encode('ascii')),
                                                                bytes(iv.encode('ascii'))))
                    ciphertext = rawciphertext.hex()
    
                    output = "Encrypting | {}\nKey | {}\nIV | {}\nMode | {}\nRaw Ciphertext | {}\nCiphertext | {}".format(
                            text, key, iv, mode.upper(), rawciphertext, ciphertext)

                    return [output, True]

                else:
                    if iv != 8:
                        return ['Error: IV must be 8 bytes long', False]
                    
                    elif len(text.encode('utf-8')) % 8 != 0:
                        return ['Error: Plaintext length must be an exact multiple of 8 bytes', False]
                    
                    else:
                        return ['Error: Make sure your plaintext is an exact multiple of 8 bytes and your IV is 8 bytes long', False]

            elif mode.lower() == 'cbc-cts':
                # check for valid plaintext length and if IV is present
                if len(text.encode('utf-8')) > 8 and len(iv.encode('utf-8')) == 8:
                    rawciphertext = b''.join(secret.encrypt_cbc_cts(bytes(text.encode('ascii')),
                                                                    bytes(iv.encode('ascii'))))
                    ciphertext = rawciphertext.hex()

                    output = "Encrypting | {}\nKey | {}\nIV | {}\nMode | {}\nRaw Ciphertext | {}\nCiphertext | {}".format(
                            text, key, iv, mode.upper(), rawciphertext, ciphertext)

                    return [output, True]
                
                else:
                    if iv != 8:
                        return ['Error: IV must be 8 bytes long', False]
                    
                    elif len(text.encode('utf-8')) < 8:
                        return ['Error: Plaintext length must be greater than 8 bytes', False]
                    
                    else:
                        return ['Error: Make sure your plaintext is greater than 8 bytes and your IV is 8 bytes long', False]

            elif mode.lower() == 'pcbc':
                # check for valid plaintext length and if IV is present
                if len(text.encode('utf-8')) % 8 == 0 and len(iv.encode('utf-8')) == 8:
                    rawciphertext = b''.join(secret.encrypt_pcbc(bytes(text.encode('ascii')),
                                                                    bytes(iv.encode('ascii'))))
                    ciphertext = rawciphertext.hex()

                    output = "Encrypting | {}\nKey | {}\nIV | {}\nMode | {}\nRaw Ciphertext | {}\nCiphertext | {}".format(
                            text, key, iv, mode.upper(), rawciphertext, ciphertext)

                    return [output, True]
                
                else:
                    if len(iv) != 8:
                        return ['Error: IV must be 8 bytes long', False]
                    
                    elif len(text.encode('utf-8')) % 8 != 0:
                        return ['Error: Plaintext length must be an exact multiple of 8 bytes', False]
                    
                    else:
                        return ['Error: Make sure your plaintext is an exact multiple of 8 bytes and your IV is 8 bytes long', False]

            elif mode.lower() == 'cfb':
                # check if IV is present
                if len(iv.encode('utf-8')) == 8:
                    rawciphertext = b''.join(secret.encrypt_cfb(bytes(text.encode('ascii')),
                                                                    bytes(iv.encode('ascii'))))
                    ciphertext = rawciphertext.hex()

                    output = "Encrypting | {}\nKey | {}\nIV | {}\nMode | {}\nRaw Ciphertext | {}\nCiphertext | {}".format(
                            text, key, iv, mode.upper(), rawciphertext, ciphertext)

                    return [output, True]
                
                else:
                    return ['Error: IV must be 8 bytes long', False]

            elif mode.lower() == 'ofb':
                # check if IV is present
                if len(iv.encode('utf-8')) == 8:
                    rawciphertext = b''.join(secret.encrypt_ofb(bytes(text.encode('ascii')),
                                                                    bytes(iv.encode('ascii'))))
                    ciphertext = rawciphertext.hex()

                    output = "Encrypting | {}\nKey | {}\nIV | {}\nMode | {}\nRaw Ciphertext | {}\nCiphertext | {}".format(
                            text, key, iv, mode.upper(), rawciphertext, ciphertext)

                    return [output, True]
                
                else:
                    return ['Error: IV must be 8 bytes long', False]

            elif mode.lower() == 'ctr':
                # generate nonce if nonce is absent
                if nonce: pass
                else: nonce = int.from_bytes(urandom(8), "big")

                enc_counter = blowfish.ctr_counter(nonce, f = xor)
                rawciphertext = b''.join(secret.encrypt_ctr(bytes(text.encode('ascii')),
                                                            enc_counter))
                ciphertext = rawciphertext.hex()

                output = "Encrypting | {}\nKey | {}\nNonce | {}\nMode | {}\nRaw Ciphertext | {}\nCiphertext | {}".format(
                        text, key, nonce, mode.upper(), rawciphertext, ciphertext)

                return [output, True]

            else:
                return ['Error: Please choose a mode, run "blowfish" for the help menu', False]

        else:
            return ['Error: Invalid key length, must be between 4 and 56 bytes long']

    else:
        output = ''
        if key == None:
            output += 'Error: Key is not present\n'

        elif text == None:
            output += 'Error: Plaintext is not present\n'

        elif mode == None:
            output += 'Error: Mode is not present\n'

        else:
            output += 'Error: Double check your Key, Mode and Plaintext'

        return [output.strip(), False]

def decode(args):
    text = args.text
    key = args.key
    mode = args.mode
    iv = args.iv
    nonce = args.nonce

    # check if key, text and mode is present
    if key and text and mode:
        # check for valid key length
        if len(key) >= 4 and len(key) <= 56 and mode.lower() in modes:
            # encryption key
            secret = blowfish.Cipher(bytes(key.encode('ascii')))

            if mode.lower() == 'block': 
                # attempt decode
                try:
                    plaintext = secret.decrypt_block(bytes.fromhex(text)).decode()

                except:
                    plaintext = secret.decrypt_block(bytes.fromhex(text))

                output = "Decrypting | {}\nKey | {}\nMode | {}\nPlaintext | {}".format(
                        text, key, mode.lower().capitalize(), plaintext)

                return [output, True]
            
            elif mode.lower() == 'ecb':
                # attempt decode
                try:
                    plaintext = b''.join(secret.decrypt_ecb(bytes.fromhex(text))).decode()

                except:
                    plaintext = b''.join(secret.decrypt_ecb(bytes.fromhex(text)))

                output = "Decrypting | {}\nKey | {}\nMode | {}\nPlaintext | {}".format(
                        text, key, mode.upper(), plaintext)

                return [output, True]

            elif mode.lower() == 'ecb-cts':
                # attempt decode
                try:
                    plaintext = b''.join(secret.decrypt_ecb_cts(bytes.fromhex(text))).decode()

                except:
                    plaintext = b''.join(secret.decrypt_ecb_cts(bytes.fromhex(text)))

                output = "Decrypting | {}\nKey | {}\nMode | {}\nPlaintext | {}".format(
                        text, key, mode.upper(), plaintext)

                return [output, True]
            
            elif mode.lower() == 'cbc':
                # attempt decode
                try:
                    plaintext = b''.join(secret.decrypt_cbc(bytes.fromhex(text),
                                                            bytes(iv.encode('ascii')))).decode()
                
                except:
                    plaintext = b''.join(secret.decrypt_cbc(bytes.fromhex(text),
                                                            bytes(iv.encode('ascii'))))

                output = "Decrypting | {}\nKey | {}\nIV | {}\nMode | {}\nPlaintext | {}".format(
                        text, key, iv, mode.upper(), plaintext)

                return [output, True]
            
            elif mode.lower() == 'cbc-cts':
                # attempt decode
                try:
                    plaintext = b''.join(secret.decrypt_cbc_cts(bytes.fromhex(text),
                                                                bytes(iv.encode('ascii')))).decode()
                
                except:
                    plaintext = b''.join(secret.decrypt_cbc_cts(bytes.fromhex(text),
                                                                bytes(iv.encode('ascii'))))

                output = "Decrypting | {}\nKey | {}\nIV | {}\nMode | {}\nPlaintext | {}".format(
                        text, key, iv, mode.upper(), plaintext)

                return [output, True]

            elif mode.lower() == 'pcbc':
                # attempt decode
                try:
                    plaintext = b''.join(secret.decrypt_pcbc(bytes.fromhex(text),
                                                             bytes(iv.encode('ascii')))).decode()

                except:
                    plaintext = b''.join(secret.decrypt_pcbc(bytes.fromhex(text),
                                                             bytes(iv.encode('ascii'))))

                output = "Decrypting | {}\nKey | {}\nIV | {}\nMode | {}\nPlaintext | {}".format(
                        text, key, iv, mode.upper(), plaintext)

                return [output, True]

            elif mode.lower() == 'cfb':
                # attempt decode
                try:
                    plaintext = b''.join(secret.decrypt_cfb(bytes.fromhex(text),
                                                            bytes(iv.encode('ascii')))).decode()

                except:
                    plaintext = b''.join(secret.decrypt_cfb(bytes.fromhex(text),
                                                            bytes(iv.encode('ascii'))))

                output = "Decrypting | {}\nKey | {}\nIV | {}\nMode | {}\nPlaintext | {}".format(
                        text, key, iv, mode.upper(), plaintext)

                return [output, True]

            elif mode.lower() == 'ofb':
                # attempt decode
                try:
                    plaintext = b''.join(secret.decrypt_ofb(bytes.fromhex(text),
                                                            bytes(iv.encode('ascii')))).decode()

                except:
                    plaintext = b''.join(secret.decrypt_ofb(bytes.fromhex(text),
                                                            bytes(iv.encode('ascii'))))

                output = "Decrypting | {}\nKey | {}\nIV | {}\nMode | {}\nPlaintext | {}".format(
                        text, key, iv, mode.upper(), plaintext)

                return [output, True]

            elif mode.lower() == 'ctr':
                if nonce:
                    dec_counter = blowfish.ctr_counter(nonce, f=xor)
                    # attempt decode
                    try:
                        plaintext = b''.join(secret.decrypt_ctr(bytes.fromhex(text),
                                                                dec_counter)).decode()

                    except:
                        plaintext = b''.join(secret.decrypt_ctr(bytes.fromhex(text),
                                                                dec_counter))

                    output = "Decrypting | {}\nKey | {}\nNonce | {}\nMode | {}\nPlaintext | {}".format(
                            text, key, nonce, mode, plaintext)

                    return [output, True]

            else:
                return ['Error: Please choose a mode, run "blowfish" for the help menu', False]
        else:
            return ['Error: Invalid key length, must be between 4 and 56 bytes long']
    else:
        output = ''
        if key == None:
            output += 'Error: Key is not present\n'

        elif text == None:
            output += 'Error: Plaintext is not present\n'

        elif mode == None:
            output += 'Error: Mode is not present\n'

        else:
            output += 'Error: Double check your Key, Mode and Plaintext'

        return [output.strip(), False]
