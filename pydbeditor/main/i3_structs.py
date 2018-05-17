#!/usr/bin/env python
#coding:utf-8

from ctypes import *
import collections


class atg_i3r_cb_interface(Structure):
    _fields_ = [('rep_cb_hdr_total_length',c_ulong),
                ('rep_cb_hdr_struct_length',c_ulong),
                ('rep_cb_hdr_cb_type',c_ulong),
                ('rep_cb_hdr_format_number',c_ulong),
                ('row_status',c_ubyte),
                ('admin_status',c_ubyte),
                ('oper_status',c_ubyte),
                ('instance_index',c_ulong),
                ('if_index',c_ulong),
                ('if_name',c_ubyte * 16),
                ('if_type',c_ulong)]

    
def atg_i3r_cb_interface_fill_data(struct_ptr):
    res_dict = collections.OrderedDict()
    res_dict['rep_cb_hdr_total_length'] = hex(struct_ptr[0].rep_cb_hdr_total_length)
    res_dict['rep_cb_hdr_struct_length'] = hex(struct_ptr[0].rep_cb_hdr_struct_length)
    res_dict['rep_cb_hdr_cb_type'] = hex(struct_ptr[0].rep_cb_hdr_cb_type)
    res_dict['rep_cb_hdr_format_number'] = hex(struct_ptr[0].rep_cb_hdr_format_number)
    res_dict['rep_cb_hdr_format_number'] = hex(struct_ptr[0].rep_cb_hdr_format_number)
    res_dict['row_status'] = hex(struct_ptr[0].row_status)
    res_dict['admin_status'] = hex(struct_ptr[0].admin_status)
    res_dict['oper_status'] = hex(struct_ptr[0].oper_status)
    res_dict['instance_index'] = hex(struct_ptr[0].instance_index)
    res_dict['if_index'] = hex(struct_ptr[0].if_index)
    res_dict['if_name'] = hex(struct_ptr[0].if_name)
    res_dict['if_type'] = hex(struct_ptr[0].if_type)
    
    return res_dict

def atg_i3r_cb_interface_analyse(data_str):
    hex_str = bytes().fromhex(data_str) #字符串转成16进制字节流
    str_buffer = create_string_buffer(hex_str) #为新字节流分配内存
    struct_ptr = cast(str_buffer, POINTER(atg_i3r_cb_interface))
    res_dict = atg_i3r_cb_interface_fill_data(struct_ptr)
    
    return res_dict
    
    
    
