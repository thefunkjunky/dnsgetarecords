#!/usr/bin/env python

# Notice
# ----------------------------------------------------------------
# Copyright (C) 2016  J Garrett Anderson
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version, a copy of the GNU GPL (version 3)
# is included in the root directory of this repository in a file named
# LICENSE.TXT, please review it for further details.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# General Information
# ----------------------------------------------------------------
# Name: run.py (dnsgetarecords)
# Version: v0.1
# Release: Review
# Author: J Garrett Anderson
# Usage: Run script with domain URL as an argument.
# Run script with -h or --help for more detailed usage info.


# Description:  A library package and command-line python utility that accepts a domain argument, 
# and returns a list of DNS A-record IPv4 addresses.



### Disclaimer
### --------------------------------------------------------------
### This script and all accompanying configuration, directive, executable, and
### log files together with the directory structures, and other miscellanious files
### necessary for the proper operation of the same hereinafter will be referred to
### as "the software".
### By acknowledging the presence of this software on your computing infrastructure
### and by not removing it or otherwise hindering its normal operation, you agree to
### to assume all responsibility for the consequences of enabling, continuing to run,
### or otherwise operating this software, in addition to this you also agree to
### indemnify and hold the author(s) harmless against any  possible damages
### either resulting from running this software as is or damages resulting
### from your own modification and subsequent execution of the software.
### If you do not agree with the terms of this disclaimer, please promptly
### terminate the execution or scheduled execution of this software; please also
### promptly uninstall, or remove this software from your computing infrastructure.

import sys
import argparse
from socket import setdefaulttimeout

from dnsgetarecords import ARecordFetcher

def main():
    """ Main function to execute when script is run directly from the command line"""

    # Configure argument parser
    parser = argparse.ArgumentParser(
        description="Returns a list of IPv4 IPs from a given domain\'s DNS A-records.")
    parser.add_argument("domain", 
        help="Target domain, from which A-Record IP addresses will be returned.")
    parser.add_argument("-t", "--timeout", default = 5,
        help="Sets DNS query timeout length in seconds.  Default = 5.0 s.")
    parser.add_argument("-m", "--maxitems", default = 3,
        help="Sets maximum number of IPs to be returned.  Default = 3.")
    parser.add_argument("-v", "--verbose",
        help="Toggles Human-Readable format.  Default is False, which returns"\
        " IPs formatted as a Python list.", 
        action="store_true")
    args = parser.parse_args()

    # Initialize 'ARecordFetcher' class as 'ipfetch' object
    ipfetch = ARecordFetcher()

    # Set default timeout length in seconds
    setdefaulttimeout(args.timeout)

    # Check to ensure relatively recent version of Python being run
    cur_version = sys.version[:5:]
    if ipfetch.check_py_version(cur_version):
        pass
    else:
        print("Current Python version {} is untested.  Please use "\
            "Python version 2.6, 3.3, or higher.".format(cur_version))
        exit()

    # Attempt to populate DNS IP records list for target domain
    ip_list = ipfetch.getIPs(args.domain)
    if not ip_list:
        exit()

    # Trim IP_addr list
    ip_trim_list = ipfetch.trimlist(ip_list, args.maxitems)
    if not ip_list:
        exit()


    # Check if entries in ip_trim_list are valid IPv4 addresses
    if not ipfetch.check_IP_addr(ip_trim_list):
        exit()

    # If human readable, prints verbose results.  If not, prints raw list
    if args.verbose:
        print("DNS IPv4 A-record addresses returned for domain {}:\n".format(args.domain))
        for ipaddr in ip_trim_list:
            print("{}".format(ipaddr))
    else:
        print(ip_trim_list)

if __name__ == '__main__':
    main()