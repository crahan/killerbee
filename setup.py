# NOTE: See the README file for a list of dependencies to install.

from __future__ import print_function
import sys

try:
    from setuptools import setup, Extension
except ImportError:
    print("No setuptools found, attempting to use distutils instead.")
    from distutils.core import setup, Extension

zigbee_crypt = Extension('zigbee_crypt',
                         sources = ['zigbee_crypt/zigbee_crypt.c'],
                         libraries = ['gcrypt'],
                         include_dirs = ['/usr/local/include', '/usr/include', '/sw/include/', 'zigbee_crypt'],
                         library_dirs = ['/usr/local/lib', '/usr/lib','/sw/var/lib/']
                         )

setup(name        = 'killerbee',
      version     = '3.0.0-beta.2',
      description = 'ZigBee and IEEE 802.15.4 Attack Framework and Tools',
      author = 'Joshua Wright, Ryan Speers',
      author_email = 'jwright@willhackforsushi.com, ryan@riverloopsecurity.com',
      license   = 'LICENSE.txt',
      packages  = ['killerbee'],
      scripts = ['tools/zbdump', 'tools/zbgoodfind', 'tools/zbid', 'tools/zbreplay',
                 'tools/zbconvert', 'tools/zbdsniff', 'tools/zbstumbler', 'tools/zbassocflood',
                 'tools/zbscapy', 'tools/zbwireshark', 'tools/zbkey',
                 'tools/zbwardrive', 'tools/zbopenear', 'tools/zbfakebeacon',
                 'tools/zborphannotify', 'tools/zbpanidconflictflood', 'tools/zbrealign', 'tools/zbcat',
                 'tools/zbjammer', 'tools/kbbootloader'],
      install_requires=['pyserial>=2.0', 'pyusb', 'pycrypto', 'rangeparser', 'scapy'],
      # NOTE: pygtk doesn't install via distutils on non-Windows hosts
      ext_modules = [zigbee_crypt],
      )
