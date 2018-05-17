#!/usr/bin/env python
#coding:utf-8

import i3_structs

class data_dispos:
    analyse_func = {'02000903': atg_i3r_cb_interface}
    
    def _init_(self):
        pass
    
    def txt_read(self):
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

    def cb_type_classify(self, dict_val, func_dict):
        entry_dict = {}
        for key,value in dict_val.items():
            print('key:', key, type(key))
            print('value:', value, type(value))
            cb_type = value[0:8]
            print('cb_type:', cb_type)
            entry_dict[key] = func_dict[cb_type](key, value)
        return entry_dict
        
    
