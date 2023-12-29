#!/usr/bin/env python3

#
# convert.py
# Convert a BCH script to its hexadecimal bytecode.
# Usage: python3 convert.py <file_path>
# Ensure that each opcode or data element is on a new line without spaces, comments, or indents in the file to be converted.
# https://www.bitcoincashsite.com/blog/token-pioneers-cashtokens-tutorial-4
#

import argparse

OPCODES = {
    "OP_0": "00",
    "OP_UTXOTOKENCOMMITMENT": "cf",
    "OP_2": "52",
    "OP_SPLIT": "7f",
    "OP_OVER": "78",
    "OP_EQUAL": "87",
    "OP_IF": "63",
    "OP_ELSE": "67",
    "OP_ENDIF": "68",
    "OP_DROP": "75",
    "OP_TOALTSTACK": "6b",
    "OP_8": "58",
    "OP_12": "5c",
    # Add other opcodes as needed
}


def script_to_hex(script):
    hex_script = []
    for line in script.strip().split('\n'):
        line = line.strip()
        if line.startswith("<") and line.endswith(">"):
            # Process data elements inside angle brackets
            data_element = line[1:-1]
            if data_element.startswith("0x"):
                # Remove '0x' prefix and convert to bytes
                data_element = bytes.fromhex(data_element[2:])
            else:
                # Treat as a regular string and convert to bytes
                data_element = data_element.encode()

            # Append the length of the data element and the data element itself in hex
            hex_script.append(f"{len(data_element):02x}{data_element.hex()}")
        else:
            # Append the hex code for the opcode
            hex_script.append(OPCODES.get(line, ''))
    return ''.join(hex_script)


def read_script_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()


# Set up the argument parser
parser = argparse.ArgumentParser(
    description='Convert a Bitcoin Cash script to its hexadecimal bytecode.')
parser.add_argument(
    'file_path', help='Path to the file containing the script to be converted')

# Parse arguments
args = parser.parse_args()

# Read the script from the provided file path and convert it
script = read_script_from_file(args.file_path)
print(script_to_hex(script))
