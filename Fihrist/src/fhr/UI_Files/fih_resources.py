# -*- coding: utf-8 -*-

# Resource object code
#
# Created by: The Resource Compiler for PyQt5 (Qt v5.15.2)
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore


qt_resource_data = b"\
\x00\x00\x01\x25\
\x89\
\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d\x49\x48\x44\x52\x00\
\x00\x00\x10\x00\x00\x00\x10\x08\x06\x00\x00\x00\x1f\xf3\xff\x61\
\x00\x00\x00\x09\x70\x48\x59\x73\x00\x00\x0b\x13\x00\x00\x0b\x13\
\x01\x00\x9a\x9c\x18\x00\x00\x00\xd7\x49\x44\x41\x54\x78\x9c\x63\
\x60\xa0\x36\x90\x9b\xf9\x45\x12\x9b\xb8\xfc\xb4\x8f\x16\x8a\xd3\
\x3e\x87\x2a\x4f\xfd\x26\x8b\x53\xb3\xf2\x94\x0f\x2a\x0a\x53\x3f\
\xbd\x54\x98\xfa\x39\x1f\x5d\x4e\x71\xea\xa7\x95\x8a\xd3\x3e\xff\
\x57\x98\xfe\x39\x0c\xab\x66\xd9\xc9\x5f\xa5\x14\xa7\x7d\x7a\x00\
\x52\xa4\x38\xed\xd3\x5f\xc5\x69\x9f\x82\x51\x5c\x30\xe3\xa3\x25\
\xc8\x05\x2a\x13\xbf\xca\x60\x68\x56\x99\xf8\x86\x4f\x71\xda\xa7\
\xf3\x10\xcd\x10\xac\x30\xf5\xd3\x4f\xc5\x69\x9f\x5d\xe0\x2e\x98\
\xf6\x79\x15\x54\x2e\x14\xa7\x17\x14\xa7\x7d\x0e\x85\x2a\x5a\x45\
\x56\x18\x28\xe2\x31\x80\x60\x18\x0c\x13\x03\x54\x26\x7e\x95\x01\
\x19\x02\x8a\x32\xaa\xb9\x40\x61\xca\x27\x3b\xc5\xa9\x9f\xbe\xa3\
\x45\xf1\x65\xb9\x69\x1f\x04\x89\x76\x81\xe2\xb4\x4f\xc1\x90\xc4\
\x05\x4e\x64\x0f\x40\x89\x8e\xe4\x30\x50\x98\xfe\x29\x5d\x71\xda\
\xe7\x37\xf2\x33\x3f\x69\x90\x15\x06\x20\x80\x2b\xa3\x51\x04\x00\
\x62\x5c\xcc\x9a\x8e\x3f\x9f\xf2\x00\x00\x00\x00\x49\x45\x4e\x44\
\xae\x42\x60\x82\
"

qt_resource_name = b"\
\x00\x09\
\x0c\x78\x54\x88\
\x00\x6e\
\x00\x65\x00\x77\x00\x50\x00\x72\x00\x65\x00\x66\x00\x69\x00\x78\
\x00\x1b\
\x09\x04\x8e\x27\
\x00\x69\
\x00\x63\x00\x6f\x00\x6e\x00\x73\x00\x38\x00\x2d\x00\x75\x00\x70\x00\x2d\x00\x64\x00\x6f\x00\x77\x00\x6e\x00\x2d\x00\x61\x00\x72\
\x00\x72\x00\x6f\x00\x77\x00\x2d\x00\x31\x00\x36\x00\x2e\x00\x70\x00\x6e\x00\x67\
"

qt_resource_struct_v1 = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x02\
\x00\x00\x00\x18\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
"

qt_resource_struct_v2 = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x02\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x18\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x01\x86\x40\xd8\x58\xb5\
"

qt_version = [int(v) for v in QtCore.qVersion().split('.')]
if qt_version < [5, 8, 0]:
    rcc_version = 1
    qt_resource_struct = qt_resource_struct_v1
else:
    rcc_version = 2
    qt_resource_struct = qt_resource_struct_v2

def qInitResources():
    QtCore.qRegisterResourceData(rcc_version, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(rcc_version, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
