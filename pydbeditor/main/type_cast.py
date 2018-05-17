#!/usr/bin/env python
#coding:utf-8

from ctypes import *
from _ctypes import pointer

class mystruct(Structure):
    _fields_ = [('format_number', c_ulong),
                ('row_status',c_ubyte),
                ('admin_status',c_ubyte),
                ('oper_status',c_ubyte),
                ('instance_index',c_ulong)]

s = "a10000f1a2a3a400a50000f5"
print(sizeof(c_ulong))
#x = c_wchar_p(s)
#x = create_string_buffer(b"000000000202010001000000")
y = bytes().fromhex(s)
print(y)
z = create_string_buffer(y)
print(sizeof(z),repr(z.raw))
#print('x:', x)
#print(repr(x.raw))
#print('*x:', x.value)
#y = byref(x)
#print(y)
#x = '000000000202010001000000'
#y = c_char_p(x)    

px = cast(z, POINTER(mystruct))

print(type(px))
print(hex(px[0].format_number))
print(hex(px[0].row_status))
print(hex(px[0].admin_status))
print(hex(px[0].oper_status))
print(hex(px[0].instance_index))