#!/bin/bash
# installer for SkeletonKey
# created by : Soulsender and C0SM0
# DO NOT FUCK WITH THIS SCRIPT

# color variables
red="\e[0;91m"
green="\e[0;92m"
blue="\e[0;94m"
bold="\e[1m"
reset="\e[0m"

function staging {
    # continue prompt
    while true
    do
    read -r -p "This will copy SkeletonKey to your home directory. If you already had SkeletonKey installed, this will reinstall it. Would you like to continue? [Y/n]" input
    case $input in
        [yY][eE][sS]|[yY])
        echo -e "${green}Continuing...${reset}"
        sleep 2
        install=true
        break
        ;;

        [nN][oO]|[nN])
        echo -e "${red}Operation canceled.${reset}"
        break
        exit 0
        ;;

        *)
        echo -e "${red}Invalid input...${reset}"
        ;;

    esac
    done

    # staging
    echo -e "${blue}[*] Staging process...${reset}"
    rm -rf ~/.SkeletonKey
    cd ..
    cp -r SkeletonKey ~/.SkeletonKey
    echo -e "${green}[+] Complete${reset}"
}

function alias_workflow {
    # set up alias workflow
    echo -e "${blue}[*] Setting up alias...${reset}"

    # check if it already exists in bashrc
    if ! cat ~/.bashrc | grep "SkeletonKey_PATH" > /dev/null; then
        # Do it in one command instead of repeating yourself.
        echo "
        export SkeletonKey_PATH=\"~/.SkeletonKey\"
        alias key=\"python3 ~/.SkeletonKey/main.py\"
        " >> ~/.bashrc
    fi

    #check if it already exists in zshrc
    if ! cat ~/.zshrc | grep "SkeletonKey_PATH" > /dev/null; then
        # Do it in one command instead of repeating yourself.
        echo "export SkeletonKey_PATH=\"~/.SkeletonKey\"\nalias key=\"python3 ~/.SkeletonKey/main.py\"
        " >> ~/.zshrc
    fi
	
	# check if it already exists in xonshrx
    if ! cat ~/.xonshrc | grep "~/.SkeletonKey/main.py" > /dev/null; then
        # Do it in one command instead of repeating yourself.
        echo "aliases[\"key\"] = [\"python3\", \"~/.SkeletonKey/main.py\"]" >> ~/.xonshrc
    fi

    echo -e "${green}[+] Completed${reset}"
}

function debian_install {
    sudo apt update
    sudo apt-get install -y python3 python3-pip python-dev
}

function void_install {
    sudo xbps-install -Sy python3 python3-pip python3-devel
}

function arch_install {
    sudo pacman -Sy python python-pip python-setuptools
}

function python_install {
    pip install -r requirements.txt
}

# check if run with sudo
if [ "$EUID" -eq 0 ]; then
    echo -e "${red}[!] Do not run as root. ${reset}The installation script will prompt you for root access."
    exit 1
fi

# arguments
while [ -n "$1" ]
do
case "$1" in
--help) 
  echo -e "
${green}SUPPORTED DISTROS:${reset}
- Debian
    - Raspbian (Raspberry Pi OS)
    - Parrot
    - Ubuntu
    - Kali
    - Mint
    - Elementary OS
    - Zorin
    - MX
    - Pop
    - Deepin
- Arch
    - Manjaro
    - Garuda
    - Artix
    - EndeavourOS
    - ArcoLinux
    - RebornOS
- Void 

${red}UNSUPPORTED DISTROS:${reset}
see ./install.sh --unsupported-distro

${green}SUPPORTED SHELLS:${reset}
- bash
- zsh

${red}UNSUPPORTED SHELLS:${reset}
see ./install.sh --unsupported-shell

Please see the SkeletonKey README for more infomation about unsupported distros and shells:
${blue}https://github.com/CosmodiumCS/SkeletonKey${reset}
"
  exit 0
;;
--unsupported-distro)
    # call alias workflow function
    alias_workflow
    staging
    exit 0
;;
--unsupported-shell)
    # call alias workflow function
    python_install
    staging
    echo -e ${blue}"Your run configs are:"${reset}
    ls -a ~ | grep "rc"
    echo -e "${red} Please enter this command, where \".rc\" is your shell run config:"${reset}
    echo -e "echo \"export SkeletonKey_PATH=\"~/.SkeletonKey\" && alias key=\"python3 ~/.SkeletonKey/main.py\"\" >> ~/.rc"
    exit 0
;;
esac
shift
done

# install lsb_release command because arch and void are quirky and don't want to have it by default even though it's literally like 1mb
sudo pacman -Sy --noconfirm lsb-release &>/dev/null
sudo xbps-install -y lsb-release &>/dev/null
sudo apt install -y lsb-release &>/dev/null

# get distro
distro=$(lsb_release -i | cut -f 2-)

# list of valid distros
debian_systems=("Ubuntu" "Debian" "Linuxmint" "Kali" "Parrot" "elementary OS" "MX" "Zorin" "Pop" "Deepin" "Raspbian" "Raspberry Pi Foundation")
arch_systems=("Arch Linux" "Manjaro Linux" "Garuda" "Artix")

if [[ " ${debian_systems[*]} " == *"$distro"* ]]; then
    # installing tools for debian
    echo -e "${blue}[*] ${red}$distro${reset} system detected."
    echo -e "${blue}[*] Installing tools...${reset}"
	echo -e "${blue}[~] Enter sudo prompt : ${reset}"
    debian_install
    python_install
    echo -e "${green}[+] Completed${reset}"

elif [[ " ${arch_systems[*]} " == *"$distro"* ]]; then
    # installing tools for arch
    echo -e "${blue}[*] ${blue}Arch${reset} system detected."
    echo -e "${blue}[*] Installing tools...${reset}"
    arch_install
    python_install
    echo -e "${green}[+] Completed${reset}"

elif [[ "$distro" == "Void" ]]; then
    # installing tools for void
    echo -e "${blue}[*] ${green}$distro${reset} system detected."
    echo -e "${blue}[*] Installing tools...${reset}"
    void_install
    python_install
    echo -e "${green}[+] Completed${reset}"

else
    echo -e "${red}[!] Unknown distro: \"$distro\", please see documentation for unknown distros.${reset}"
    exit 1
fi

# call alias workflow
alias_workflow

# call staging
staging

# clean up
echo -e "${green}[+] Installation Successful"
echo -e "[+] You might have to restart your terminal"
echo -e "[+] Type 'key' in a new terminal to launch SkeletonKey${reset}"
echo -e ${red}"[!] If typing 'key' does not work, check you have a supported shell with 'which \$SHELL'${reset}"
