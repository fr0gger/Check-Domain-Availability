#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Thomas Roccia | Check domain availability
# pip install pywhois

import argparse
import whois
import signal
import sys

# handle ctrl c
def signal_handler(sig, frame):
    print(' You pressed Ctrl+C!')
    sys.exit(0)

# check if domain exist
def whois_domain(domain):
    try:
        whois.whois(domain)
        print('\033[0m' + "[+] %s already exist!" % domain)
    except whois.parser.PywhoisError:
        print('\033[91m' + "[!] %s is available!" % domain)

# check domains from file
def check_list(filename):
    domains = []
    with open(filename) as f:
        domains = f.readlines()

    for domain in domains:
        whois_domain(domain.strip())

# check single domain exist
def check_domain(domain):
    whois_domain(domain)


# main function
def main():
    # select arguments
    parser = argparse.ArgumentParser(description='checkDomain.py by Thomas Roccia')
    parser.add_argument("-d", "--domain", help="Check single domain", required=False)
    parser.add_argument("-f", "--file", help="Check domain list", required=False)
    args = parser.parse_args()

    # handle ctrl+c
    signal.signal(signal.SIGINT, signal_handler)

    if args.domain:
        check_domain(args.domain)

    if args.file:
        check_list(args.file)


if __name__ == '__main__':
    main()