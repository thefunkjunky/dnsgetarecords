from setuptools import setup, find_packages
 
setup(
    name = "dnsgetarecords",
    version = "0.1",
    description='Return DNS IPv4 A-Records for target domain.',
    author='J Garrett Anderson',
    author_email='j.garrett.anderson@gmail.com',
    packages = find_packages(),
    test_suite = "dnsgetarecords",
    entry_points = {
        'console_scripts': ['dnsgetarecords=dnsgetarecords.run:main'],
    },
    )