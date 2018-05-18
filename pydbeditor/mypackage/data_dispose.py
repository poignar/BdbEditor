#!/usr/bin/env python
#coding:utf-8

from ctypes import *
from mystructs import i3_structs
import collections


class Data_dispose():
    analyse_func = {'03090002': i3_structs.atg_i3r_cb_interface_analyse, 
                    '02000903': i3_structs.atg_i3r_cb_interface_analyse}
    
    dict2str_func ={'03090002': i3_structs.atg_i3r_cb_interface_dict2str,
                    '02000903': i3_structs.atg_i3r_cb_interface_dict2str}

    
    def __init__(self, input_file_name, output_file_name):
        self.ifile_name = input_file_name
        self.ofile_name = output_file_name
    
    def txt_read(self):
        filename = self.ifile_name
        key_data_dict = collections.OrderedDict()
        try:
            with open(filename, 'r') as f:
                get_lines = f.readlines()
                line_size = len(get_lines)
                for i in range(5,line_size - 1, 2):
                    key_str = get_lines[i]
                    key_len = len(key_str)
                    key_str = key_str.strip()
                    data_str = get_lines[i + 1]
                    data_len = len(data_str)
                    if data_len == key_len: #no data next line
                        data_str = str()
                        i = i - 1
                    else:
                        data_str = data_str.strip()
                    key_data_dict[key_str] = data_str
        except Exception as e:
            print('unable to load file: %s err: %s' % filename, e)
            
        return key_data_dict

    def cb_type_analyse(self, key_data_dict,
                          analyse_func_dict = analyse_func):
        entry_dict = collections.OrderedDict()
        cb_list = list()
        for key,value in key_data_dict.items():
            #print('key:', key, type(key))
            #print('value:', value, type(value))
            cb_type = value[:8]
            value = value[8:]
            cb_list.append(cb_type)
            #print('cb_type:', cb_type)
            if cb_type in analyse_func_dict:
                entry_dict[key] = analyse_func_dict[cb_type](value, cb_type)
        cb_counter_dict = dict(collections.Counter(cb_list))
        return entry_dict, cb_counter_dict
    
    def cb_datalist_create(self, entry_dict):
        data_list = list()
        for key_db, val_db in entry_dict.items():
            cb_type = val_db['cb_type'][2:]
            data_list.append(' ' + key_db)
            if len(val_db) > 0:
                if cb_type in Data_dispose.dict2str_func:
                    val_str = Data_dispose.dict2str_func[cb_type](val_db, cb_type)
                    #print('val_str:', val_str)
                    data_list.append(' ' + val_str)
        return data_list
                
        
    
    def txt_load(self, data_list):
        filename = self.ofile_name
        with open(filename, 'w+') as f:
            f.write("VERSION=3" + '\n'
                    "format=bytevalue" + '\n'
                    "type=btree" + '\n'
                    "db_pagesize=4096" + '\n'
                    "HEADER=END" + '\n')
            for line in data_list:
                f.write(line + '\n')
                
            f.write("DATA=END" + '\n')
        return
        
    
