#!/bin/bash

# This script prepares a directory structure for a new OSCP machine writeup.
# Written by: Aaron Lichtman
# https://www.github.com/alichtman

[ -n "$1" ] && echo "No args permitted" && exit;

read -p "Are you sure? [y/N]" -n 1 -r
echo    # (optional) move to a new line
if [[ ! $REPLY =~ ^[Yy]$ ]]
then
    exit 1
fi

mkdir enum loot exploitation
mkdir exploitation/{privesc,foothold}
mkdir enum/{portscan,webscan}
cp -iv ~/Desktop/Development/writeups/hack-the-box/template-writeup.md writeup.md

cp -iv ~/OSCP/tools/priv-esc/linux/LinEnum.sh exploitation/privesc
cp -iv ~/OSCP/tools/priv-esc/linux/linpeas.sh exploitation/privesc
cp -Riv ~/OSCP/tools/priv-esc/linux/pspy/ exploitation/privesc
cp -iv ~/OSCP/tools/priv-esc/windows/winPEAS.bat exploitation/privesc
cp -iv ~/OSCP/tools/priv-esc/windows/winPEAS.exe exploitation/privesc
