#!/bin/bash
# Shell script to make inCharge_cli.py into executable
aux_file=./cli_code.py
file=./ev_group17

sleep 1s
if [ ! -e $aux_file ]; then
  echo "Fatal error: The file $aux_file does NOT exist"
  exit 1
else
  echo "File $aux_file seems ok"
fi
sleep 1s
if [ ! -e $file ]; then
  echo "Fatal error: The file $file does NOT exist"
  exit 1
else
  echo "File $file seems ok"
fi

cp $aux_file $file

sleep 1s

if [ ! -x "$file" ]; then
  chmod +x "$file"
  echo "$file is now executable"
else
  echo "$file is already executable"
fi

file=ev_group17

mkdir -p ~/bin
cp $file ~/bin
cp $file ~/.local/bin
export PATH="$PATH:$file"
. ~/.profile

sleep 2s
echo " "
echo "Try '$file --help' to see what we can do for you"
