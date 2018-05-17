#!/usr/bin/env python
#coding:utf-8

str_val = '0x3090002'
print(str_val)
str_val = str_val[2:]
print(str_val)
str_val = str_val.zfill(8)
print(str_val)
hex_data = bytes().fromhex(str_val)
print('hex_data', hex_data)
a = [hex(x) for x in bytes(hex_data)]
print('a',a)
b = list(reversed(a))
print('b',b)
c = [int(x,16) for x in b]
print('c',c)
res = bytes(c).hex()
print('res',res)
res = '0x' + res
print(res)
