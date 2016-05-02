#dnsgetarecords

###General Information

Name: dnsgetarecords

Version: v0.1  
Release: Review  
Author: J Garrett Anderson  
Description:  a Python command-line utility that accepts a domain URL,  
and returns a list of DNS A-record IPv4 addresses for the domain


usage:   

* Install .egg via easy_install   
```dnsgetarecords [-h] [-t TIMEOUT] [-m MAXITEMS] [-v] domain```

positional arguments:  
* domain: Target domain, from which A-Record IP addresses will be returned.

optional arguments:  
  * -h, --help            show this help message and exit
  * -t TIMEOUT, --timeout TIMEOUT
                        Sets DNS query timeout length in seconds. Default =
                        5.0 s.
  * -m MAXITEMS, --maxitems MAXITEMS
                        Sets maximum number of IPs to be returned. Default =
                        3.
  * -v, --verbose         Toggles Human-Readable format. Default is False, which
                        returns IPs formatted as a Python list.


