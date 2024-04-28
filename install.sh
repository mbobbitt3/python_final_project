#!/bin/bash

# URL of the file to download
FILE_URL="https://github.com/NationalSecurityAgency/ghidra/releases/download/Ghidra_11.0.3_build/ghidra_11.0.3_PUBLIC_20240410.zip"

# Determine the user's home directory
HOME_DIR="$HOME"

# Destination directory for download
DEST_DIR="$HOME_DIR/ghidra"

# Create the destination directory if it doesn't exist
mkdir -p "$DEST_DIR"

# Download the file
curl -L -o "$DEST_DIR/ghidra_11.0.3.zip" "$FILE_URL"

# Unzip the downloaded file into the destination directory
unzip -o "$DEST_DIR/ghidra_11.0.3.zip" -d "$DEST_DIR"

# Optionally, remove the zip file after extraction
rm "$DEST_DIR/ghidra_11.0.3.zip"

#add headless analyzer to PATH
echo "export PATH=$PATH:$DEST_DIR/ghidra_11.0.3_PUBLIC/support/" >> $HOME_DIR/.bashrc
#make projects direcotry
mkdir -p $HOME/ghidra_projects
# Output a message indicating completion
echo "Ghidra has been downloaded and unzipped to $DEST_DIR"
