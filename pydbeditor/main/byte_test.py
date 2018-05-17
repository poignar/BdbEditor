#!/usr/bin/env python
#coding:utf-8

#byte_val = b"03090002"
#print(byte_val,type(byte_val))

#str_val = byte_val.decode(encoding='utf_8', errors='strict')
str_val = '030a0002'
print(str_val,type(str_val))

hex_data = bytes().fromhex(str_val)
print(hex_data, type(hex_data))

a = [hex(x) for x in bytes(hex_data)]
print(a)

b = list(reversed(a))
print(b)

c = [int(x,16) for x in b]
print(c)

d = bytes(c)
print(d)

e = d.hex()
print(e)

