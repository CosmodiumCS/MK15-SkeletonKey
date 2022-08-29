<!-- variables -->
[ccs]: https://www.cosmodiumcs.com
[ssg]: https://www.saintssec.com
[youtube]: https://www.youtube.com/c/CosmodiumCS
[onlyrat]: https://github.com/CosmodiumCS/OnlyRAT

<!-- title -->
# SkeletonKey

## Overview:
SkeletonKey is an advanced cryptography hacking tool created by a joint development between [The Societal Security Guild](https://saintssec.com) and [Cosmodium CyberSecurity][ccs]. It was originally two seperate tools, one reffered to as "[Cryptex](https://github.com/SSGorg/Cryptex)" and the other as "[The Codex Project](https://github.com/CosmodiumCS/the-codex-project)". But on May 2, 2022, the lead developers [Cythes](https://github.com/AlexKollar) and [Blue Cosmo](https://github.com/CosmodiumCS) joined forces to build a central cryptography tool. 

On August 10th of the same year, due to inner group conflict, many of the developers of Cryptex left to build their own tool named "SkeletonKey".

SkeletonKey is capable of advanced encryption, decryption, and breaking ciphers through various mehtods. These methods include but are not limited to bruteforcing, cryptographic wordlising, letter frequencies, plaintext formatting, and cracking.

## Earth Invader Discord Bot
The Earth Invader bot is a Discord API extension of SkeletonKey, bringing the same cryptography tools to Discord as if it was your own cryptography console!

See the repository [here](https://github.com/Soulsender/Earth-Invader).


<!-- EMBED YOUTUBE VIDEO HERE -->

## Requirements:
- Debian/Void/Arch based Linux OS
- Python 3.x

## Set-Up & Installation:
1. Clone repository
```
git clone https://github.com/CosmodiumCS/SkeletonKey
```
2. Execute installer
> **YES** the SkeletonKey directory **IS** supposed to dissapear
```
cd SkeletonKey
chmod +x
./install.sh
```

3. Restart your terminal

### Supported Distros
 - Debian (debian-based)
    - Kali
    - Parrot
    - Ubuntu
    - Mint
 - Arch
 - Void

> See `--help` on `install.sh`.

### Unsupported Distros
Any unsupported distros you can use `--unsupported-distro` on `install.sh`.

In addition, you will need to install:
 - System Packages:
    - Python3
    - Python Pip
 - Python Packages
    - these can be installed after installing python pip, with `pip3 install -r requirements.txt`



## Executing SkeletonKey
Run the following for help
```
key --help
```
- The help menu will return a list of all available ciphers
- You can append the flag for a cipher after `key` to get help for a cipher
- Here as an example for the Caesar Cipher `cc`
```
key cc
``` 
- The returned arguments can be passed in addition
- These arguments are the most popular among the ciphers
- `-e` - encryption
- `-d` - decryption
- `-b` - breaking/bruteforcing
- `-k` - encryption key
- `-t` - input text
- `-i` - input file
- `-o` - output file
- However, each cipher will have its own uniqe arguments for additional features
```
key cc -e -t "hello world" -k 5
```

## Cryptconsole:
The Cryptconsole is a more expansive way of using SkeletonKey. It allows the user to open a console in their terminal connected to the SkeletonKey libraries; comparable to [Metasploit](https://www.metasploit.com/) or [OnlyRAT][onlyrat]. The Cryptconsole can allow users to run multiple ciphers back to back to back.
- We can execute the cryptconsole by running the following
```
key
```
- Now multiple ciphers can be run back to back with ease
```
[~] root@SkeletonKey $ cc -e -t "hello world" -k 5
...
[~] root@SkeletonKey $ vc -e -t "hello world" -k hello
```
- SkeletonKey also has various commands for console interaction
- `help` - displays help menu
- `update` - updates crytpex to latest version
- `version` - displays current version
- `exit` - exits cryptconsole
- Any other command are run through the commandline

## Updating SkeletonKey:
The development team will continuously be pushing out new versions of SkeletonKey. To prevent users from continously having to clone the repository, we made an update function.
- Argument Parsing
```
key --update
```
- CryptConsole
```
key
[~] root@SkeletonKey $ update
```

## Uninstalling SkeletonKey:
If at anypoint you are unsatisfied or need to rid of the SkeletonKey project [and its awesomeness]. You can run the following to get it off of your computer.
- Argument Parsing
```
key --remove
```
- CryptConsole
```
key
[~] root@SkeletonKey $ remove
```

## About Us
**[Soul](https://soulsender.github.io): Lead Discord Bot Dev / Shellscripter / Project Manager**
Worked on multi-distro (debian/arch/void) installer support for `install.sh`. Lead developer on the [Earth Invader](https://github.com/Soulsender/Earth-Invader) discord bot. Credited with giving SkeletonKey its colors. Also might or might not have had something to do with the original beta name "Earth Invader". 

**[BlueCosmo](https://github.com/PrettyBoyCosmo): Lead Python / Shellscript Developer**
Started Cosmodium at 17 and since then has made significant changes in the cybersecurity community. A reasonably known content creator and python programming whiz to say the least.    
  
**[Fyzz](https://github.com/FyzzLive): Lead Python Developer**   
Cryptocurrency and cryptography expert, always happy to add another cipher.

**[Cythes](https://github.com/AlexKollar): Project Manager (Retired)**
I started learning computers around middle school age with my discovery & passion of PC Gaming.  A few years later I'd stumbled into Ubuntu 8.04 soon started learning programming, hacking on and off, while over the next decade working on projects ranging from Android personal safety applications to light game development.

**[Mart](https://github.com/marvhus): Developer**
I started tinkering with computers I think around primary school, then in junior high school I started doing more tech stuff, then in high school I started learning more proper programming, and I began to do a lot of programming in my spare time, and at school, but I was always at least 10 steps ahead of what my class was learning, and eventually I ended up finding this place.

## Testers:
- Matze
- Ibijon

## Sponsors:  
- GamerChillz

## Credits:
As an open source project, SkeletonKey and Earth Invader do use snippets of code inspired and based on other projects such as the following:

- [OnlyRAT](https://github.com/CosmodiumCS/OnlyRAT)
- [Nirsoft](https://www.nirsoft.net)
- [Satux](https://cosmodiumcs.com/coming-soon)
- [Scarab](https://github.com/Soulsender/Scarab)

## Resources:
- [Discord](https://discord.gg/tTKv8w8sHH)
