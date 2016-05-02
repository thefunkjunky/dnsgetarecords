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
# Name: dnsgetarecords.py (dnsgetarecords)
# Version: v0.1
# Release: Review
# Author: J Garrett Anderson
# Usage: 
# 

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
import re

# The primary functionality of this script is through the following function,
# which has been shortened in name to "gethost"
from socket import gethostbyname_ex as gethost
from socket import gaierror, timeout, setdefaulttimeout, inet_aton

class ARecordFetcher(object):
    """Returns a list of IPv4 IPs from domain's DNS A-Records"""
    def __init__(self):
        super(ARecordFetcher, self).__init__()

    def getIPs(self, domain = "localhost"):
        """ Returns a list of IPs for 'domain' argument """
        # convert 'domain' to string, in case of erroneous type being passed
        domain = str(domain)

        # Kind warning for those who entered an IP address instead of a domain
        try: 
            inet_aton(domain)
            print("Warning: an IP address was given instead of a domain name.")
        except:
            pass

        # Try to query DNS records to populate A-Record IP list
        # Prints errors and returns None if exceptions found
        try:
            iplist = gethost(domain)[2]
        except gaierror as ge:
            if ge.errno == -2:
                print("Error: Domain '{}' invalid, or unknown. "\
                  "Please check proper spelling and format.\n"\
                  "(e.g.: python dns_get_A_record_IPs.py google.com )".format(domain))
            elif ge.errno == -3:
                print("Error: Domain '{}' unreachable. Please check your connection.".format(domain))
            return None
        except timeout:
            print("Error: Connection to {} timed out.".format(domain))
            return None

        return iplist

    def trimlist(self, iplist, maxIPs = 3):
        """ Trim iplist if length is greater than maxIPs. 
        Print error and return None if length == 0 """
        
        if len(iplist) > 0:
            iplist = iplist[:maxIPs:]
            return iplist
        else:
            print("Error: No IP A-records found.")
            return None

    def check_IP_addr(self, iplist):
        """ Checks if IP addresses in iplist are correct IPv4 format.  
        If correct, returns True """

        if type(iplist) != list:
            print("Error: please provide a list of IPv4 addresses to check (as a list of strings).")
            return False

        for ip_addr in iplist:
            # Converts ip_addr to string, in case of bad type being passed
            ip_addr = str(ip_addr)

            # Checks ip_addr format
            try: 
                inet_aton(ip_addr)
            except:
                print("Error: '{}' is an invalid IPv4 address.\n"\
                    "Please use a valid IPv4 address (e.g.: 192.168.0.1)".format(ip_addr))
                return False
        return True


    def check_py_version(self, cur_version):
        """ Check to ensure relatively recent version of Python being used
        (2.6+, 3.3+) """

        # convert cur_version to string, in case of erroneous type being passed
        cur_version = str(cur_version)

        acceptable_python_versions_regex = r"(^(2\.[6-9])(\.?\d{1,2})?$)|(^(3\.[3-9])(\.?\d{1,2})?$)"
        pyversions_regex_compiled = re.compile(acceptable_python_versions_regex)
        pyversions_match = pyversions_regex_compiled.match(cur_version)

        # If match is found, return True.  If no match, return False
        if pyversions_match:
            return True
        else:
            return False

