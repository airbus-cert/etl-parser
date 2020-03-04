# -*- coding: utf-8 -*-

"""
:see: https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-dtyp/cca27429-5689-4a16-b2b4-9325d93e4ba2
"""
from construct import Struct, Int8ul, Byte, Int32ul, Array, Const

# https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-dtyp/f992ad60-0fe4-4b87-9fed-beb478836861
Sid = Struct(
    "Revision" / Const(0x01, Int8ul),
    "SubAuthorityCount" / Int8ul,
    "IdentifierAuthority" / Byte[6],
    "SubAuthority" / Array(lambda this: this.SubAuthorityCount, Int32ul)
)