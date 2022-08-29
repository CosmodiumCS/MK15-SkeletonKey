#!/bin/bash
# updater for SkeletonKey
# created by : C0SM0

# remove previous version
cd ~
rm -rf .SkeletonKey

# install new version
git clone https://github.com/CosmodiumCS/SkeletonKey

# install dependencies
cd SkeletonKey
chmod +x install.sh
./install.sh

# self delete
rm -rf ../update.sh
