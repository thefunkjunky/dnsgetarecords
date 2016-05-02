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
# Name: test_dnsgetarecords.py
# Version: v0.1
# Release: Review
# Author: J Garrett Anderson
# Usage: python setup.py tests

# Description:  Unit Tests for dns_get_A_record_IPs.py, a Python 
# command-line utility that accepts a domain URL, and returns
# a list of DNS A-record IPv4 addresses for the domain



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

import os
import sys
import unittest
import socket

# Check to see if main module is available for import.
try:
    from dnsgetarecords import ARecordFetcher
except Exception as e:
    print("Error importing ARecordFetcher from dnsgetarecords.py.\n"\
        "Please check to make sure dnsgetarecords.py is in your Python path.\n"\
        "Current PYTHONPATH search locations (in order): \n{}\n"\
        "EXCEPTION error: {}\n".format(sys.path, e))
    exit()

<<<<<<< HEAD:dnsgetarecords/test_dnsgetarecords.py
class Test_IPFetcher(unittest.TestCase):
=======
class Test_IPFetchergit(unittest.TestCase):
>>>>>>> 4d0d7316e6473e5520eaffcf78b294ada750add6:dnsgetarecords/test_dnsgetarecords.py
    """ Tests for the DNS A-Record IP Fetcher utility """

    def setUp(self):
        """ Initialize ARecordFetcher class as object 'ipfetch' """
        self.ipfetch = ARecordFetcher()

    def test_python_version(self):
        """ Test if Python version test functions properly """
        ver = 2
        versioncheck = self.ipfetch.check_py_version(ver)
        self.assertEqual(versioncheck, False)

        ver = "2"
        versioncheck = self.ipfetch.check_py_version(ver)
        self.assertEqual(versioncheck, False)

        ver = "2.5"
        versioncheck = self.ipfetch.check_py_version(ver)
        self.assertEqual(versioncheck, False)

        ver = "2.5.5"
        versioncheck = self.ipfetch.check_py_version(ver)
        self.assertEqual(versioncheck, False)

        ver = "2.6"
        versioncheck = self.ipfetch.check_py_version(ver)
        self.assertEqual(versioncheck, True)

        ver = "2.6."
        versioncheck = self.ipfetch.check_py_version(ver)
        self.assertEqual(versioncheck, False)

        ver = "2.6.5"
        versioncheck = self.ipfetch.check_py_version(ver)
        self.assertEqual(versioncheck, True)

        ver = "2.6.7b"
        versioncheck = self.ipfetch.check_py_version(ver)
        self.assertEqual(versioncheck, False)

        ver = "2.6.777"
        versioncheck = self.ipfetch.check_py_version(ver)
        self.assertEqual(versioncheck, False)

        ver = "3"
        versioncheck = self.ipfetch.check_py_version(ver)
        self.assertEqual(versioncheck, False)

        ver = "3."
        versioncheck = self.ipfetch.check_py_version(ver)
        self.assertEqual(versioncheck, False)

        ver = "3.3"
        versioncheck = self.ipfetch.check_py_version(ver)
        self.assertEqual(versioncheck, True)

        ver = "3.3.11"
        versioncheck = self.ipfetch.check_py_version(ver)
        self.assertEqual(versioncheck, True)

        ver = "3.3.5b"
        versioncheck = self.ipfetch.check_py_version(ver)
        self.assertEqual(versioncheck, False)

        ver = "3.3.555"
        versioncheck = self.ipfetch.check_py_version(ver)
        self.assertEqual(versioncheck, False)

    def test_ip_checker(self):
        """ Tests the IP list format verification function """
        iplist = "google.com"
        results = self.ipfetch.check_IP_addr(iplist)
        self.assertEqual(results, False)

        iplist = 192.168
        results = self.ipfetch.check_IP_addr(iplist)
        self.assertEqual(results, False)

        iplist = ["google.com"]
        results = self.ipfetch.check_IP_addr(iplist)
        self.assertEqual(results, False)

        iplist = ["192.168.1.1", "google.com"]
        results = self.ipfetch.check_IP_addr(iplist)
        self.assertEqual(results, False)

        iplist = ["192.168.1.1"]
        results = self.ipfetch.check_IP_addr(iplist)
        self.assertEqual(results, True)

        iplist = ["192.168.1.1", 192.168]
        results = self.ipfetch.check_IP_addr(iplist)
        self.assertEqual(results, True)

        iplist = ["192.168.1.1", "192.168.1.2"]
        results = self.ipfetch.check_IP_addr(iplist)
        self.assertEqual(results, True)

    def test_trimlist(self):
        """ Test the list trimmer """
        list = ['1.1.1.1', '2.2.2.2', '3.3.3.3']

        maxIPs = 2
        trimlist = self.ipfetch.trimlist(list, maxIPs)
        self.assertEqual(trimlist, ["1.1.1.1", "2.2.2.2"])

        maxIPs = 5
        trimlist = self.ipfetch.trimlist(list, maxIPs)
        self.assertEqual(trimlist, ["1.1.1.1", "2.2.2.2", "3.3.3.3"])

        list = []
        maxIPs = 3
        trimlist = self.ipfetch.trimlist(list, maxIPs)
        self.assertEqual(trimlist, None)

    def test_getIPs(self):
        """ Test the DNS query engine.  How do I force bad socket connections?  Hrm... """
        # Set timeout to 3 seconds
        socket.setdefaulttimeout(3)

        domain = "localhost"
        results = self.ipfetch.getIPs(domain)
        self.assertEqual(results, ["127.0.0.1"])

        domain = "localho"
        results = self.ipfetch.getIPs(domain)
        self.assertEqual(results, None, msg="Error: Domain '{}' invalid, or unknown. "\
                      "Please check proper spelling and format.\n"\
                      "(e.g.: python dns_get_A_record_IPs.py google.com )".format(domain))

        domain = "127.0.0.1"
        results = self.ipfetch.getIPs(domain)
        self.assertEqual(results, ["127.0.0.1"], msg="Warning: an IP address was given instead of a domain name.")

        # How do I force a time-out and a ethernet disconnection?
        # Answer: self.assertRaises().  Have to refactor code to make it work, no time.

if __name__ == '__main__':
    unittest.main()