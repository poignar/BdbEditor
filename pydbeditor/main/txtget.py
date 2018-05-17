#!/usr/bin/env python
#coding:utf-8

from __future__ import print_function
import os
import sys



def txt_read():
    filename = 'lmp.txt'
    key_data_dict = {}
    try:
        with open(filename) as f:
            get_lines = f.readlines()
            line_size = len(get_lines)
            for i in range(5,line_size - 1, 2):
                key_str = get_lines[i]
                key_str = key_str.strip()
                data_str = get_lines[i + 1]
                data_str = data_str.strip()
                key_data_dict[key_str] = data_str
    except Exception as e:
        print('unable to load file: %s err: %s' % filename, e)
        
    return key_data_dict

def cb_type_classify(dict_val):
    entry_dict = {}
    for key,value in dict_val.items():
        print('key:', key, type(key))
        print('value:', value, type(value))
        cb_type = value[0:8]
        print('cb_type:', cb_type)
        entry_dict[key] = analyse_func[cb_type](key, value)
    return entry_dict
        
def atg_i3r_cb_interface(key_str, data_str):
    print('hit!')
    res = {}
    res['key'] = key_str
    data_str, res['type'] = get_byte(data_str,8)
    data_str, res['total_length'] = get_byte(data_str,8)
    data_str, res['struct_length'] = get_byte(data_str,8)
    
    return res
    
def get_byte(data_str, len_byte):
    get_value = data_str[0:len_byte]
    str_rem = data_str[len_byte:]
    return str_rem, get_value

analyse_func = {'02000903': atg_i3r_cb_interface}

dict_val = txt_read()
res_dict = cb_type_classify(dict_val)
for kv in res_dict.items():
    print(kv)
            