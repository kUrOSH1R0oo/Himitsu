#!/bin/bash
if [ "$(id -u)" -ne 0 ]; then
    echo "[-] Error: This script must be run as root (use sudo)."
    exit 1
fi
SCRIPT_PATH="himitsu.py"
DEST_DIR="/usr/local/bin"
DEST_SCRIPT="$DEST_DIR/himitsu"
if [ ! -f "$SCRIPT_PATH" ]; then
    echo "[-] Error: The script '$SCRIPT_PATH' was not found."
    exit 1
fi
echo "[+] Moving '$SCRIPT_PATH' to '$DEST_DIR'"
cp "$SCRIPT_PATH" "$DEST_SCRIPT"
echo "[+] Setting execute permissions for '$DEST_SCRIPT'"
chmod +x "$DEST_SCRIPT"
if [ -x "$DEST_SCRIPT" ]; then
    echo "[+] Installation complete. You can now use 'himitsu' as a command."
else
    echo "[-] Error: The script could not be made executable."
    exit 1
fi

