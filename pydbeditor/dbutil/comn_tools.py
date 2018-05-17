#!/usr/bin/env python
#coding:utf-8

from ctypes import *
import binascii as ba

def hex_reverse(data_str, data_len):
    str_val = data_str[2:]
    str_val_fill = str_val.zfill(data_len * 2)
    hex_data = bytes().fromhex(str_val_fill)
    list_before_rev = [hex(x) for x in bytes(hex_data)]
    list_after_rev = list(reversed(list_before_rev))
    rev_data = [int(x,16) for x in list_after_rev]
    rev_str = bytes(rev_data).hex()
    res_str = '0x' + rev_str
    return res_str

def array2str(data_array, array_len, data_len):
    res_str = str()
    for i in range(array_len):
        res_str = res_str + hex_reverse(hex(data_array[i]), data_len)[2:]
    res_str = '0x' + res_str
    return res_str

def str2array(data_str, data_array, data_len):
    data_str = data_str[2:]
    str_len = len(data_str)
    array_len = len(data_array)
    step = str_len // array_len
    for i in range(len(data_array)):
        tem_str = data_str[(i * step):(i * step + step)]
        tem_str = hex_reverse('0x' + tem_str, data_len)
        int_data = int(tem_str, 16)
        data_array[i] = int_data
    
    return data_array

def struct2str(struct_entity, struct_len, cb_type):
    hex_str_buffer = cast(pointer(struct_entity), POINTER(c_char * struct_len))
    x = hex_str_buffer[0].raw
    hex_str = str(ba.b2a_hex(x))[2:-1]
    hex_str = cb_type + hex_str
    return hex_str
    
        