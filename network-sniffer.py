#!/usr/bin/env python3

__author__ = "Anthony Gedeon"

import argparse
import socket



if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="A Python Network Packet Sniffer.")

    parser.add_argument(
        "-i", 
        "--interface",
        type=str,
        default=None,
        help='Interface from which packets will be captured '
                            '(captures from all available interfaces by '
                            'default).')

    parser.add_argument(
        "-d", 
        "--display",
        help="Display packet data during sniffing")

    args = parser.parse_args()

    print(args)
