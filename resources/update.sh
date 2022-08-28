#!/bin/bash
# updater for Cryptex
# created by : C0SM0

# remove previous version
cd ~
rm -rf .Cryptex

# install new version
git clone https://github.com/AlexKollar/Cryptex.git

# install dependencies
cd Cryptex
chmod +x install.sh
./install.sh

# self delete
rm -rf ../update.sh
