#!/usr/bin/env python3

#
# encode.py
# Various utility functions.
# Usage: python3 encode.py -h
# https://www.bitcoincashsite.com/blog/token-pioneers-cashtokens-tutorial-4
#

import argparse


def utf8_to_hex(input_string):
    """ Convert UTF-8 string to hexadecimal representation """
    return input_string.encode().hex()


def hex_to_utf8(input_string):
    """ Convert hexadecimal string to UTF-8 representation """
    return bytes.fromhex(input_string).decode('utf-8')


def decimal_to_hex(input_string):
    """ Convert decimal string to hexadecimal representation """
    return hex(int(input_string)).lstrip("0x").rstrip("L")


def hex_to_decimal(input_string):
    """ Convert hexadecimal string to decimal representation """
    return str(int(input_string, 16))


def string_bytes(input_string, is_hex):
    """ Get the byte length of the input string. If is_hex is True, treats the string as hexadecimal. """
    if is_hex:
        return len(input_string) // 2
    else:
        return len(input_string.encode())


# Set up the argument parser
parser = argparse.ArgumentParser(
    description='This script converts between UTF-8, Hexadecimal, Decimal and calculates byte length of strings. \
    Use -x to convert from UTF-8 to Hex, -u for Hex to UTF-8, -dx for Decimal to Hex, -xd for Hex to Decimal, \
    and -b to get the byte length of the input string. The --ishex flag indicates if the input string is hexadecimal \
    (used with -b).')

# Adding arguments
parser.add_argument(
    'input', help='The input string to be converted or evaluated')
parser.add_argument('-x', '--tohex', action='store_true',
                    help='Convert a UTF-8 string to its Hexadecimal representation')
parser.add_argument('-u', '--toutf8', action='store_true',
                    help='Convert a Hexadecimal string to its UTF-8 representation')
parser.add_argument('-dx', '--todecimalhex', action='store_true',
                    help='Convert a Decimal string to its Hexadecimal representation')
parser.add_argument('-xd', '--tohexdecimal', action='store_true',
                    help='Convert a Hexadecimal string to its Decimal representation')
parser.add_argument('-b', '--bytes', action='store_true',
                    help='Calculate the byte length of the input string. Use --ishex to indicate if the input is in hexadecimal format')
parser.add_argument('--ishex', action='store_true',
                    help='Indicate if the input string is in hexadecimal format (used with -b)')

# Parse arguments
args = parser.parse_args()

# Perform conversion based on the flags
if args.tohex:
    print(utf8_to_hex(args.input))
elif args.toutf8:
    print(hex_to_utf8(args.input))
elif args.todecimalhex:
    print(decimal_to_hex(args.input))
elif args.tohexdecimal:
    print(hex_to_decimal(args.input))
elif args.bytes:
    print(string_bytes(args.input, args.ishex))
else:
    print("No valid conversion flag provided. Use the appropriate flag for the desired conversion.")
