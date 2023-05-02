#!/usr/bin/python
# New Arg Parse and Cipher Call
# created by : Fyzz | C0SM0 | Soul

# imports
import argparse
from ast import For
from multiprocessing.context import ForkServerProcess
import mods.bits as b
import importlib
import readline
import sys
import os
from colorama import Fore, Back, Style
import string


# gets list of available ciphers
def get_ciphers():
    output_list = []
    directory = os.fsencode(b.cipher)

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        output_list.append(filename[:-3])

    return output_list

# updates skeletonkey
def update():

    cmd_prefix = f'{Fore.GREEN}[~] {Fore.RESET}'
    print("\n[*] Checking for updates...")

    # get latest version nubmer
    os.system("curl https://raw.githubusercontent.com/CosmodiumCS/SkeletonKey/main/version.txt| tee ~/.SkeletonKey/latest.txt")

    # save version nubmers to memory
    current_version = float(open(f"{b.local_path}/version.txt", "r").read())
    latest_version = float(open (f"{b.local_path}/latest.txt", "r").read())

    # remove version number file
    os.system("rm -rf ~/.SkeletonKey/latest.txt")

    # if new version is available, update
    if latest_version > current_version:
        print("\n[+] Update found")
        print(cmd_prefix + "Update SkeletonKey? [y/n]\n")

        # user input, option
        option = input(f"{b.header}")

        # update
        if option == "y":
            os.system("sh ~/.SkeletonKey/resources/update.sh")

    else:
        print("\n[+] SkeletonKey already up to date")

# output function
def output(data, output): 
    if data:
        if data[1] == True and data[1]:
            # file
            if output and ".png" not in output:
                with open(output, 'w') as f:
                    f.write(data[0])
                print(f'{b.SUCCESS}[✓] File Output Successful{b.END}')

            # command line interface
            else:
                print(f'\n{b.SUCCESS}[✓] Output:{b.END}\n{data[0]}\n')
        else:
            # exception
                print(f'\n{b.FAIL}[✖] Failed:{b.END}\n{data[0]}\n')

# uninstalls skeletonkey
def remove():

    cmd_prefix = f'{Fore.RED}[~] {Fore.RESET}'

    # confirmation
    print("\n" + cmd_prefix + "Are you sure you want to remove SkeletonKey? [y/n]\n")

    # user input
    option = input(b.header)

    # delete SkeletonKey
    if option == "y":
        os.system("rm -rf ~/.SkeletonKey")

# command line interface
def cli(args_exist):
    cmd_prefix = f'{Fore.CYAN}[~] {Fore.RESET}'

    # default arguments
    if args_exist:
        if sys.argv[1] in ['-h', '--help']:
            print(b.help_menu)
        elif sys.argv[1] in ['-u', '--update']:
            update()
        elif sys.argv[1] in ['-rm', '--remove', '--uninstall']:
            remove()

        elif '+' in sys.argv:
            text = sys.argv[sys.argv.index('-t') + 1]
            sys.argv[sys.argv.index('-t') + 1] = f'"{text}"'
            args = " ".join(sys.argv[1:])
            layers = args.split(' + ')
            text = ''
            for index, layer in enumerate(layers):
                if index == 0:
                    os.system(f'python3 ~/.SkeletonKey/main.py {layer} -lay')
                elif index != len(layers) - 1:
                    try:
                        with open('temp_storage.txt', 'r') as temp:
                            layerd_storage = temp.read()
                    except Exception:
                        pass
                    else:
                        os.system(f'python3 ~/.SkeletonKey/main.py {layer} -t "{layerd_storage}" -lay')
                else:
                    try:
                        with open('temp_storage.txt', 'r') as temp:
                            layerd_storage = temp.read()
                    except Exception:
                        pass
                    else:
                        os.system(f'python3 ~/.SkeletonKey/main.py {layer} -t "{layerd_storage}"')
                        os.remove('temp_storage.txt')

        else:
            parser = argparse.ArgumentParser(add_help=False, usage="")
            parser.add_argument('cipher', type=str)
            parser.add_argument('-e', '--encode', dest='encode', action='store_true')
            parser.add_argument('-d', '--decode', dest='decode', action='store_true')
            parser.add_argument('-b', '--brute', dest='brute', action='store_true')
            parser.add_argument('-i', '--inputFile', dest='inputFile', type=str)
            parser.add_argument('-ii', '--inputImage', dest='inputImage', type=str)
            parser.add_argument('-o', '--output', dest='output', type=str)
            parser.add_argument('-t', '--text', help='String Input\n', dest='text', type=str)
            parser.add_argument('-k', '--key', help='Str Key\n', dest='key', type=str)
            parser.add_argument('-s', '--salt', help='Hash Salt\n', dest='salt', type=str)
            parser.add_argument('-nc', '--nonce', help='Int Nonce\n', dest='nonce', type=int)
            parser.add_argument('-md', '--mode', dest='mode', type=str)
            parser.add_argument('-iv', dest='iv', type=str)
            parser.add_argument('-c', '--channel', dest='channel', type=str)
            parser.add_argument('-ex', '--exclude', help='Exclude Character\n', dest='exclude', type=str)
            parser.add_argument('-w', '--wordlist', help='Wordlist File\n', dest='wordlist', type=str)
            parser.add_argument('-r', '--range', help='Range\n', dest='range', type=str)
            # code transcripts
            parser.add_argument('-words', '--words', help='Filter out words\n', action='store_true')
            parser.add_argument('-lingo', '--lingo', help='Specify language ("lingo")', type=str, default='en_US')
            parser.add_argument('-a', '--alphabet', help='Specify custom alphabet\n', type=str, default=string.ascii_uppercase)
            # parser.add_argument('-a', '--alphabet', help='Specify custom alphabet\n', type=str)
            # Layered Encryption
            parser.add_argument('-lay', '--layerd', dest='layerd', action='store_true')
            # Google Translate
            parser.add_argument('-tr', '--translate', dest='translate', action='store_true')
            parser.add_argument('-lang', '--languages', dest='lang', action='store_true')
            parser.add_argument('-src', '--src', help='Source Language code\n', dest='src', type=str)
            parser.add_argument('-dest', '--dest', help='Destination Language code\n', dest='dest', type=str)
            # Static Encryption
            parser.add_argument('-f', '--file', help="Give a file path\n", dest='file', type=str)
            parser.add_argument('-iw', '--image_width', help="Image width used for SE", dest="image_width", type=int)
            #parser.add_argument('-m', '--mono', help="Make SE use monocromatic mode", dest="mono", action="store_true")
            # cryptographic payloads
            parser.add_argument('-g', '--generate', help='Choose Payload Generation Method\n', dest='generate', type=str)
            parser.add_argument('-p', '--payload', help='Choose Payload\n', dest='payload', type=str)
            parser.add_argument('-wc', '--webcredentials', dest='webcredentials', action='store_true')

            args = parser.parse_args()

            # reads input files for argument parsing
            if args.inputFile:
                with open(args.inputFile, 'r') as tmpFileVar:
                    args.text = tmpFileVar.read()
            # reads input file for wordlist
            if args.wordlist:
                with open(args.wordlist, 'r') as tmpFileVar:
                    args.wordlist = tmpFileVar.read().split('\n')
                    args.wordlist = list(filter(lambda x : len(x) > 0, args.wordlist))
            # execute skeletonkey libraries
            try:
                module = importlib.import_module(f'ciphers.{args.cipher}')

            except Exception:
                print(
                    f"{b.FAIL}\n{Fore.RED}"
                    + f"[✖] Cipher May Not Exist\nTry 'key -h' to see all ciphers{b.END}\n"
                    + Fore.RESET
                )

            else:
                func = None

                if args.layerd:
                    if args.encode:
                        layerd_storage = module.encode(args)[0]
                        with open('temp_storage.txt', 'w') as temp:
                            temp.write(layerd_storage)
                    elif args.decode:
                        layerd_storage = module.decode(args)[0]
                        with open('temp_storage.txt', 'w') as temp:
                            temp.write(layerd_storage)
                    else:
                        output(["For now '-tr' or '-b' can only be the final step in layerd encryption", False], False)
                        try:
                            os.remove('temp_storage.txt')
                        except Exception:
                            pass

                elif args.encode:
                    func = module.encode
                elif args.decode:
                    func = module.decode
                elif args.brute:
                    func = module.brute
                elif args.translate:
                    func = module.translate
                elif args.lang:
                    output(module.languages(), args.output)

                elif args.payload:
                    func = module.payload

                else:
                    print(Fore.CYAN + module.help_menu + Fore.RESET)

                if func:
                    output(func(args), args.output)
    else:
        # display banner
        print(b.banner)
        print(f'{cmd_prefix}Type "help" for help menu :')

        # loop code
        while True:
            # get user input
            user_input = input(b.header)

            # display help menu
            if user_input == 'help':
                print(b.help_menu)

            elif user_input == 'version':
                print(b.version)

            elif user_input in ['exit', 'quit']:
                exit()
                break

            elif user_input == 'update':
                update()

            elif user_input in ['uninstall', 'remove']:
                remove()

            elif user_input.split(' ')[0] not in get_ciphers():
                os.system(user_input)

            else:
                os.system(f'python3 ~/.SkeletonKey/main.py {user_input.replace("key", "")}')

# main code
def main():
    try:
        sys.argv[1]
    except IndexError:
        args_exist = False
    else:
        args_exist = True
    
    cli(args_exist)

# executes main code
if __name__ == '__main__':
    main()
