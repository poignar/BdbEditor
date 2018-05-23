#!/usr/bin/env python
#coding:utf-8

from ctypes import *
from mystructs import i3_structs
from dbutil import comn_tools
import collections


class Data_dispose():
    # a dict of functions to get data from txt strings and generate data dictionary
    # notice: the cbtype id may reversed in different system we must support that
    analyse_dict = {'03090002': [i3_structs.atg_i3r_cb_interface, i3_structs.atg_i3r_cb_interface_fill_data], 
                    '02000903': [i3_structs.atg_i3r_cb_interface, i3_structs.atg_i3r_cb_interface_fill_data],
                    '03090005': [i3_structs.atg_i3r_cb_mpls_interface, i3_structs.atg_i3r_cb_mpls_interface_fill_data],
                    '05000903': [i3_structs.atg_i3r_cb_mpls_interface, i3_structs.atg_i3r_cb_mpls_interface_fill_data]}
    
    # a dict of functions to get data strings with data from dictionary
    loadback_dict ={'03090002': i3_structs.atg_i3r_cb_interface_fill_struct,
                    '02000903': i3_structs.atg_i3r_cb_interface_fill_struct,
                    '03090005': i3_structs.atg_i3r_cb_mpls_interface_fill_struct,
                    '05000903': i3_structs.atg_i3r_cb_mpls_interface_fill_struct}

    # class Data_dispose init function with input/output filename
    def __init__(self, input_file_name, output_file_name):
        self.ifile_name = input_file_name
        self.ofile_name = output_file_name
    
    # read key/data from txtfile and return key/data dictionary
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

    # function to get data from txt strings and generate data dictionary
    def cb_type_analyse(self, key_data_dict):
        entry_dict = collections.OrderedDict()
        cb_list = list()
        for key,value in key_data_dict.items():
            #print('key:', key, type(key))
            #print('value:', value, type(value))
            cb_type = value[:8]
            value = value[8:]
            cb_list.append(cb_type)
            #print('cb_type:', cb_type)
            if cb_type in Data_dispose.analyse_dict:
                hex_str = bytes().fromhex(value)
                hex_str_buffer = create_string_buffer(hex_str)
                struct_ptr = cast(hex_str_buffer, POINTER(Data_dispose.analyse_dict[cb_type][0]))
                print('struct_entity_len', sizeof(struct_ptr[0]))
                entry_dict[key] = Data_dispose.analyse_dict[cb_type][1](struct_ptr, cb_type)
        cb_counter_dict = dict(collections.Counter(cb_list))
        return entry_dict, cb_counter_dict
    
    # function to get data strings with data from dictionary
    def cb_datalist_create(self, entry_dict):
        data_list = list()
        for key_db, val_db in entry_dict.items():
            cb_type = val_db['cb_type'][2:]
            data_list.append(' ' + key_db)
            if len(val_db) > 0:
                if cb_type in Data_dispose.loadback_dict:
                    struct_entity, struct_len = Data_dispose.loadback_dict[cb_type](val_db)
                    print('struct_load_len', struct_len)
                    hex_str = comn_tools.struct2str(struct_entity, struct_len, cb_type)
                    data_list.append(' ' + hex_str)
        return data_list
                
        
    # load string list back to txt file
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
        
    
