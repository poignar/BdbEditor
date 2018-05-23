#!/usr/bin/env python
#coding:utf-8

'''This file is just for test,you can call the funcs in qt project'''

from mypackage.data_dispose import Data_dispose
from mystructs import i3_structs
from dbutil import comn_tools

def main_test():

    testo = Data_dispose('lmp__.txt','lmpnew.txt')
    
    key_data_pair = testo.txt_read()
    
    res_dict, cb_counter = testo.cb_type_analyse(key_data_pair)    
    
    temp = list()
    for kv in res_dict.items():
        print(kv)
    
    for kv in cb_counter.items():
        print(kv)
    
    data_list = testo.cb_datalist_create(res_dict)
    
    testo.txt_load(data_list)
    
    #i3_structs.cb_datalist_create(struct_ptr)
        
main_test()
