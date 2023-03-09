# import getpasscd
import sys
import os
import getpass
from colorama import Fore, Back, Style

# Variables
username = getpass.getuser() # Get username
header = Fore.RED + f'{username}' + Fore.WHITE + '@' + Fore.RED + 'SkeletonKey $ ' + Fore.RESET # header for user input
local_path = f'/home/{username}/.SkeletonKey' if username != 'root' else '/root/.SkeletonKey' # local path to skelkey
cipher = f'{local_path}/ciphers/' # local path to ciphers

# Colors
SUCCESS = '\033[92m'
FAIL = '\033[91m'
END = '\033[0m'

version = open(f'{local_path}/version.txt').read().strip()
banner = Fore.RED + f'''
                     _,=;::::::;=,,_
                 _,;,ss*\":::::\'""sss;;,_
               ,;,sSSSss::::::::*\"sSSss;;,
             ,;,sSSSKKk*:::::::::*kkKKKKk;,
            ,;kKKKKEEee::::::::::,eEEELEEe;,
           ,;;;eEEEEEEe*:::::::::,lL\",LLLl;;;
           ;ll;;LLLLLLl::::::::_Ll *LLLLl;ll;
           ;*ll,lLLLEee:::::::*:::EeEEEE;*eE;
           ;;*EeeEEEEee::::::::::*eEEEEE;eE;;
           ;;;e\'eeEEeEe,_::::::_,eeEEEET;Tt;;
            ;;t;\"\'\'  \'""=:::::::="\'   \'";;Tt\'
             Ttt         \";::;*         t;T;
             t;Tt.,,_ _,_::::;;     __,tT;T
            =t;;*TTt=-=-=T:\' \';T=_=_=tTT;,Tt=
            tTTT;\"ttT TT;t"   :tt tTo00;OO\'0
              0Oo*oOOOo\'0\"    \':O OO0o0oOo0\'
   ,,          ;OO:  \"0::,_,:,_::0*   OO0;
 ,KkkK,       ,;0::  ;;,,,::::,,;;;   :O0;
/k(  )k\\,,;k,,K;;,k,,,,;;;;;;;;;;;\',,,:;0,,,,,,__,yyyyyy***y
{{KK}}{{KK}}KKKKKKKKKKKKKKKEEe.,eeEEEEEEEEYYYYYYYYYYYYYYYYYYYYY*
\\k(  )k/\"";k""K;;"k"";;"""""\'\'\'\'\'\';;\'\'O\'\'\'}}YYY"YY"""\'\'"""
 \'KkkK\'       \"  0.0o\';;;;;,,,;;;;"*N:;N  YYYyyy,
   \'\'            \'\"n*n*n \'";;;;" n.n,n"    yYYy""
                    \"n nNNn::*nNNn"n
                      n,nN::::nNN*\"
                        \"Nn,_,nN"

            SkeletonKey Version : {version}\n
''' + Fore.RESET

help_menu = Fore.CYAN + """
┌─────────────────────────────────────────────────────────────┐
│ [■] EXAMPLE: key cc -e -t "Encrypt Me" -k 5                 │
│                                                             │
│ [■] ARG 1. Cipher                                           │
│       [cc] ───────── Caesar Cipher                          │
│       [vc] ───────── Vingenere Cipher                       │
│       [rc] ───────── Reverse Cipher                         │
│       [mc] ───────── Multiplicative Cipher                  │
│       [ct] ───────── Code Transcript                        │
│       [se] ───────── Static Encryption                      │
│       [mo] ───────── Monoalphabetic Cipher                  │
│       [url] ──────── URL Encoding                           │
│       [xor] ──────── XOR Cipher                             │
│       [r13] ──────── ROT 13 Encoding                        │
│       [r47] ──────── ROT 47 Encoding                        │
│       [b64] ──────── Base64 Encoding                        │
│       [bin] ──────── Binary Encoding                        │
│       [pix] ──────── Image Pixel                            │
│       [hex] ──────── Hex Encoding                           │
│       [oct] ──────── Octal Encoding                         │
│       [mor] ──────── Morse Code Cipher                      │
│       [pho] ──────── Phonetic Alphabet Cipher               │
│       [md5] ──────── MD5 Hash                               │
│       [1337] ─────── L33T 5P34K Encoding                    │
│       [menc] ─────── MENC Encoding                          │
│       [sha1] ─────── SHA1 Hash                              │
│       [sha224] ───── SHA224 Hash                            │
│       [sha384] ───── SHA384 Hash                            │
│       [sha512] ───── SHA512 Hash                            │
│       [blake2b] ──── Blake2b Hash                           │
│       [blake2s] ──── Blake2s Hash                           │
│       [twofish] ──── Twofish Encryption                     │
│       [blowfish] ─── Blowfish Encryption                    │
│       [translate] ── Google Translate API                   │
├─────────────────────────────────────────────────────────────┤
│ [■] ARG 2. Ciphering Method                                 │
│       [-e] ────────── Encrypt/Encode                        │
│       [-d] ────────── Decrypt/Decode                        │
│       [-b] ────────── Break/Brute Force                     │
│                                                             │
│ [■] Google Translate API                                    │
│       [-tr] ───────── Translate                             │
│       [-lang] ─────── List Languages                        │
├─────────────────────────────────────────────────────────────┤
│ [■] Additional Arguments                                    │
│       [-t] ────────── Input Text                            │
│       [-i] ────────── Input File                            │
│       [-o] ────────── Output File                           │
│       [-k] ────────── Encryption Key                        │
│       [-s] ────────── Hash Salt                             │
│       [-r] ────────── Range                                 │
│       [-w] ────────── Wordlist                              │
│       [-a] ────────── Custom Alphabet                       │
│       [-md] ───────── Encryption Mode                       │
│       [-src] ──────── Source Language                       │
│       [-dest] ─────── Destination Language                  │
│       [-lingo] ────── Set Language ["en_US" Default]        │
│       [-words] ────── Pull Words From Output                │
├─────────────────────────────────────────────────────────────┤
│ [■] SkeletonKey Arguments                                   │
│       [--help] ────── help                                  │
│       [--version] ─── version                               │
│       [--update] ──── update                                │
└─────────────────────────────────────────────────────────────┘
""" + Fore.RESET
