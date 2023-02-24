<!-- variables -->
[ccs]: https://www.cosmodiumcs.com
[youtube]: https://www.youtube.com/c/CosmodiumCS
[onlyrat]: https://github.com/CosmodiumCS/OnlyRAT

<!-- title -->
# SkeletonKey:

> A Cryptographic Suite Created by The CosmodiumCS Development Team
---

## Overview:
SkeletonKey is an advanced cryptography hacking tool created by [Cosmodium CyberSecurity][ccs] (with an original joint development with SSG). It was originally refereed to as "[The Codex Project](https://github.com/CosmodiumCS/the-codex-project)", and later "Cryptex" after a joint development. After a group conflict, the CCS developers left the group to create "SkeletonKey", which aims to become a leading cryptographic hacking suite. SkeletonKey is capable of advanced encryption, decryption, and breaking ciphers through various methods. These methods include but are not limited to brute-forcing, cryptographic word-listing, letter frequencies, plaintext formatting, and cracking.

## Resources:
- [YouTube Video](https://www.cosmodiumcs.com/comings-soon)
- [YouTube Channel](https://youtube.com/cosmodiumcs)
- [Website](https://cosmodiumcs.com)
- [Earth Invader](https://github.com/CosmodiumCS/Earth-Invader) (SkeletonKey Discord Bot)

## Requirements:
- Linux (see `install.sh --help`)
- Either Bash or Zsh

## Installation:
1. Clone repository
```bash
git clone https://github.com/CosmodiumCS/SkeletonKey
```
2. Execute installer
> **YES** the SkeletonKey directory **IS** supposed to disappear
```bash
cd SkeletonKey
chmod +x
./install.sh
```
3. Restart your terminal

## Running SkeletonKey:
Run the following for help
```bash
key --help
```
- The help menu will return a list of all available ciphers
- You can append the flag for a cipher after `key` to get help for a cipher
- Here as an example for the Caesar Cipher `cc`
```key
key cc
``` 
- The returned arguments can be passed in addition
- These arguments are the most popular among the ciphers
- `-e` - encryption
- `-d` - decryption
- `-b` - breaking/brute-forcing
- `-k` - encryption key
- `-t` - input text
- `-i` - input file
- `-o` - output file
- However, each cipher will have its own unique arguments for additional features
```bash
key cc -e -t "hello world" -k 5
```

## Keyconsole:
The *Keyconsole* is a more expansive way of using SkeletonKey. It allows the user to open a console in their terminal that is directly connected to the SkeletonKey libraries (comparable to [Metasploit](https://www.metasploit.com/) or [OnlyRAT][onlyrat]). The *Keyconsole* can allow users to run multiple ciphers back to back to back.
- We can execute the *Keyconsole* by running the following:
```bash
key
```
- Now multiple ciphers can be run back to back with ease
```bash
[~] root@SkeletonKey $ cc -e -t "hello world" -k 5
...
[~] root@SkeletonKey $ vc -e -t "hello world" -k hello
```
- SkeletonKey also has various commands for console interaction
- `help` - displays help menu
- `update` - updates SkeletonKey to latest version
- `version` - displays current version
- `exit` - exits Keyconsole
- Any other command are run through the command line

## Updating SkeletonKey:
The development team will continuously be pushing out new versions of SkeletonKey. To prevent users from continuously having to clone the repository, we made an update function.
- **Argument Parsing**:
```bash
key --update
```
- **Keyconsole**:
```bash
key
[~] root@SkeletonKey $ update
```

## Uninstalling SkeletonKey:
If at any point you are unsatisfied with the SkeletonKey project [and its awesomeness], You can run the following to get it off of your computer.
- **Argument Parsing**:
```bash
key --remove
```
- **Keyconsole**:
```bash
key
[~] root@SkeletonKey $ remove
```

## Earth Invader Discord Bot:
The Earth Invader bot is a Discord API extension of SkeletonKey, bringing the same cryptography tools to Discord as if it was your own cryptography console! Check it out [here](https://github.com/CosmodiumCS/Earth-Invader).

## FAQ:
**What Linux distributions are supported?**
- Debian (debian-based)
	- Kali
	- Parrot
	- Ubuntu
	- Mint
- Arch
- Void
> See `--help` on `install.sh`.

**What Linux distributions are not supported?**
- With any unsupported distributions, you can use `--unsupported-distro` on `install.sh`.
- In addition, you will need to install:
	- **System Packages**:
		- Python3
		- Python Pip
	- P**ython Packages**:
		- After installing python pip, use `pip3 install -r requirements.txt`

## Original Devs:
- Blue Cosmo
- Fyzz
- Soulsender
- Haze

## Credits:
As an open source project, SkeletonKey and Earth Invader do use snippets of code inspired and based on other projects such as the following:
- [OnlyRAT](https://github.com/CosmodiumCS/OnlyRAT)
- [Nirsoft](https://www.nirsoft.net)
- [Satux](https://cosmodiumcs.com/coming-soon)
- [Scarab](https://github.com/Soulsender/Scarab)
