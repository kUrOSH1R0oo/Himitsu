# Himitsu: Reverse Shell Payload and PTY Shell Generator

Himitsu is a versatile reverse shell generator tool designed for generating payloads and PTY shells. It supports multiple encoding formats (Base64, URL encoding, etc.) and can generate payloads tailored to different operating systems like Linux, Windows, and macOS. The tool also provides options for listing available shell types and generating PTY shells for remote sessions.

## Features
- **Reverse Shell Generation**: Generate reverse shell payloads for Linux, Windows, and macOS.
- **Encoding Options**: Option to encode the generated payload in Base64, Hex, ROT13, or URL encoding.
- **PTY Shell Generation**: Generate PTY shell payloads for remote terminal access.
- **Payload Listing**: List available reverse shell payload types for specific operating systems.
- **PTY Shell Listing**: List all available PTY Shell types.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Kuraiyume/Himitsu
   ```
2. Run the installer:
   ```bash
   ./installer.sh
   ```
3. Type 'himitsu' to run the Himitsu:
   ```
   himitsu -h
   ```

## Usage
### Command-line Arguments

| Argument                  | Description                                                                 |
|---------------------------|-----------------------------------------------------------------------------|
| `-ip, --ipaddress`         | Target IP address.                                                           |
| `-p, --port`               | Target port number.                                                          |
| `-os, --operating-system`  | Target operating system (linux, windows, macos).                             |
| `-pl, --payload`           | Payload for reverse shell (type of shell).                                   |
| `-pty, --pty-shell`        | Generate a PTY shell.                                                        |
| `-rlist, --revlist`        | List available reverse shell payload types for the specified OS.            |
| `-plist, --ptylist`        | List all the available PTY shell types.                                      |
| `-enc, --encode`           | Encode the payload in Base64, Hex, ROT13, or URL encoding formats.          |

## Example Commands
- **Generate Reverse Shell**:
  ```bash
  himitsu -ip 192.168.1.10 -p 4444 -os linux -pl bash
  ```
- **Generate Reverse Shell with Encoding**:
  ```bash
  himitsu -ip 192.168.1.10 -p 4444 -os linux -pl bash -enc base64
  ```
- **List Available Reverse Shells:**
  ```bash
  himitsu -rlist linux
  ```
- **Generate PTY Shell**:
  ```bash
  himitsu -pty bash
  ```
- **List All Available PTY Shell**:
  ```bash
  himitsu -plist
  ```

## License
This tool is provided for educational and authorized penetration testing purposes only. It is your responsibility to ensure that you are using this tool within the legal framework of your jurisdiction. Misuse of this tool may result in legal consequences.

## Disclaimer
This tool is provided as-is, without any warranty, express or implied. The creator is not responsible for any damages or consequences resulting from the use of this tool.

## Author
- Kuraiyume (A1SBERG)

