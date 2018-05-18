#!/usr/bin/env python
#coding:utf-8

from ctypes import *
from dbutil import comn_tools
import collections

class atg_i3r_cb_interface(Structure):
    _fields_ = [('rep_cb_hdr_total_length', c_ulong),
                ('rep_cb_hdr_struct_length', c_ulong),
                ('rep_cb_hdr_cb_type', c_ulong),
                ('rep_cb_hdr_format_number', c_ulong),
                ('row_status', c_ubyte),
                ('admin_status', c_ubyte),
                ('oper_status', c_ubyte),
                ('instance_index', c_ulong),
                ('if_index', c_ulong),
                ('if_name', c_ubyte * 16),
                ('if_type', c_ulong),
                ('if_flags', c_ulong),
                ('if_mtu', c_ulong),
                ('remote_router_id', c_ulong),
                ('remote_if_id', c_ulong),
                ('resource_class', c_ulong),
                ('use_ospf_router_id', c_ubyte),
                ('ospf_router_id', c_ubyte * 4),
                ('use_isis_system_id', c_ubyte),
                ('isis_system_id', c_ubyte * 6),
                ('physical_address_length', c_ubyte),
                ('physical_address', c_ubyte * 16),
                ('containing_bundle_if_id', c_ulong),
                ('is_enni_level', c_ulong),
                ('enni_remote_rc_id', c_ubyte * 4),
                ('local_endpoint_id', c_ubyte * 4),
                ('remote_endpoint_id', c_ubyte * 4),
                ('next_hop_address_type', c_ubyte),
                ('next_hop_address_length', c_ubyte),
                ('next_hop_address_pad1', c_ubyte * 2),
                ('next_hop_address_address', c_ubyte * 32),
                ('remote_signaling_address_type', c_ubyte),
                ('remote_signaling_address_length', c_ubyte),
                ('remote_signaling_address_pad1', c_ubyte * 2),
                ('remote_signaling_address_address', c_ubyte * 32),
                ('opaque_param_len', c_ulong),
                ('opaque_param', c_ubyte * 256),
                ('uni_version', c_ulong),
                ('remote_ipv6_router_id_type', c_ubyte),
                ('remote_ipv6_router_id_length', c_ubyte),
                ('remote_ipv6_router_id_pad1', c_ubyte * 2),
                ('remote_ipv6_router_id_address', c_ubyte * 32),
                ('created_by_mib', c_ubyte),
                ('in_operation', c_ubyte),
                ('lock_data_link', c_ulong),
                ('if_tunnel_id_total_length', c_ulong),
                ('if_tunnel_id_struct_length', c_ulong),
                ('if_tunnel_id_tnnl_index', c_ushort),
                ('if_tunnel_id_tnnl_instance', c_ushort),
                ('if_tunnel_id_tnnl_ingress_lsrid_type', c_ubyte),
                ('if_tunnel_id_tnnl_ingress_lsrid_length', c_ubyte),
                ('if_tunnel_id_tnnl_ingress_lsrid_pad1', c_ubyte * 2),
                ('if_tunnel_id_tnnl_ingress_lsrid_address', c_ubyte * 32),
                ('if_tunnel_id_tnnl_egress_lsrid_type', c_ubyte),
                ('if_tunnel_id_tnnl_egress_lsrid_length', c_ubyte),
                ('if_tunnel_id_tnnl_egress_lsrid_pad1', c_ubyte * 2),
                ('if_tunnel_id_tnnl_egress_lsrid_address', c_ubyte * 32),
                ('emulated_if', c_ubyte),
                ('bypass_prot_if_idx', c_ulong),
                ('local_transport_node_id', c_ulong),
                ('remote_sc_pc_id', c_ulong),
                ('remote_transport_node_id', c_ulong),
                ('board_type', c_ulong),
                ('line_number', c_ulong),
                ('if_route_offset', c_ulong),
                ('if_route_total_length', c_ulong),
                ('igp_shortcut_metric_type', c_ulong),
                ('igp_shortcut_metric_value', c_ulong),
                ('signaling_interface', c_ulong),
                ('lambda_can_switch', c_ubyte),
                ('relay_otu_number', c_ushort),
                ('is_relay', c_ubyte),
                ('relay_otu_free_number', c_ushort),
                ('min_lambda_index', c_ulong),
                ('normal_otu_number', c_ushort)]
    
def atg_i3r_cb_interface_fill_data(struct_ptr, cb_type):
    res_dict = collections.OrderedDict()
    res_dict['cb_type'] = '0x' + cb_type
    res_dict['rep_cb_hdr_total_length'] = comn_tools.hex_reverse(hex(struct_ptr[0].rep_cb_hdr_total_length), 4)
    res_dict['rep_cb_hdr_struct_length'] = comn_tools.hex_reverse(hex(struct_ptr[0].rep_cb_hdr_struct_length), 4)
    res_dict['rep_cb_hdr_cb_type'] = comn_tools.hex_reverse(hex(struct_ptr[0].rep_cb_hdr_cb_type), 4)
    res_dict['rep_cb_hdr_format_number'] = comn_tools.hex_reverse(hex(struct_ptr[0].rep_cb_hdr_format_number), 4)
    res_dict['row_status'] = comn_tools.hex_reverse(hex(struct_ptr[0].row_status), 1)
    res_dict['admin_status'] = comn_tools.hex_reverse(hex(struct_ptr[0].admin_status), 1)
    res_dict['oper_status'] = comn_tools.hex_reverse(hex(struct_ptr[0].oper_status), 1)
    res_dict['instance_index'] = comn_tools.hex_reverse(hex(struct_ptr[0].instance_index), 4)
    res_dict['if_index'] = comn_tools.hex_reverse(hex(struct_ptr[0].if_index), 4)
    res_dict['if_name'] = comn_tools.array2str(struct_ptr[0].if_name, 16, 1)
    res_dict['if_type'] = comn_tools.hex_reverse(hex(struct_ptr[0].if_type), 4)
    res_dict['if_flags'] = comn_tools.hex_reverse(hex(struct_ptr[0].if_flags), 4)
    res_dict['if_mtu'] = comn_tools.hex_reverse(hex(struct_ptr[0].if_mtu), 4)
    res_dict['remote_router_id'] = comn_tools.hex_reverse(hex(struct_ptr[0].remote_router_id), 4)
    res_dict['remote_if_id'] = comn_tools.hex_reverse(hex(struct_ptr[0].remote_if_id), 4)
    res_dict['resource_class'] = comn_tools.hex_reverse(hex(struct_ptr[0].resource_class), 4)
    res_dict['use_ospf_router_id'] = comn_tools.hex_reverse(hex(struct_ptr[0].use_ospf_router_id), 1)
    res_dict['ospf_router_id'] = comn_tools.array2str(struct_ptr[0].ospf_router_id, 4, 1)
    res_dict['use_isis_system_id'] = comn_tools.hex_reverse(hex(struct_ptr[0].use_isis_system_id), 1)
    res_dict['isis_system_id'] = comn_tools.array2str(struct_ptr[0].isis_system_id, 6, 1)
    res_dict['physical_address_length'] = comn_tools.hex_reverse(hex(struct_ptr[0].physical_address_length), 1)
    res_dict['physical_address'] = comn_tools.array2str(struct_ptr[0].physical_address, 16, 1)
    res_dict['containing_bundle_if_id'] = comn_tools.hex_reverse(hex(struct_ptr[0].containing_bundle_if_id), 4)
    res_dict['is_enni_level'] = comn_tools.hex_reverse(hex(struct_ptr[0].is_enni_level), 4)
    res_dict['enni_remote_rc_id'] = comn_tools.array2str(struct_ptr[0].enni_remote_rc_id, 4, 1)
    res_dict['local_endpoint_id'] = comn_tools.array2str(struct_ptr[0].local_endpoint_id, 4, 1)
    res_dict['remote_endpoint_id'] = comn_tools.array2str(struct_ptr[0].remote_endpoint_id, 4, 1)
    res_dict['next_hop_address_type'] = comn_tools.hex_reverse(hex(struct_ptr[0].next_hop_address_type), 1)
    res_dict['next_hop_address_length'] = comn_tools.hex_reverse(hex(struct_ptr[0].next_hop_address_length), 1)
    res_dict['next_hop_address_pad1'] = comn_tools.array2str(struct_ptr[0].next_hop_address_pad1, 2, 1)
    res_dict['next_hop_address_address'] = comn_tools.array2str(struct_ptr[0].next_hop_address_address, 32, 1)
    res_dict['remote_signaling_address_type'] = comn_tools.hex_reverse(hex(struct_ptr[0].remote_signaling_address_type), 1)
    res_dict['remote_signaling_address_length'] = comn_tools.hex_reverse(hex(struct_ptr[0].remote_signaling_address_length), 1)
    res_dict['remote_signaling_address_pad1'] = comn_tools.array2str(struct_ptr[0].remote_signaling_address_pad1, 2, 1)
    res_dict['remote_signaling_address_address'] = comn_tools.array2str(struct_ptr[0].remote_signaling_address_address, 32, 1)
    res_dict['opaque_param_len'] = comn_tools.hex_reverse(hex(struct_ptr[0].opaque_param_len), 4)
    res_dict['opaque_param'] = comn_tools.array2str(struct_ptr[0].opaque_param, 256, 1)
    res_dict['uni_version'] = comn_tools.hex_reverse(hex(struct_ptr[0].uni_version), 4)
    res_dict['remote_ipv6_router_id_type'] = comn_tools.hex_reverse(hex(struct_ptr[0].remote_ipv6_router_id_type), 1)
    res_dict['remote_ipv6_router_id_length'] = comn_tools.hex_reverse(hex(struct_ptr[0].remote_ipv6_router_id_length), 1)
    res_dict['remote_ipv6_router_id_pad1'] = comn_tools.array2str(struct_ptr[0].remote_ipv6_router_id_pad1, 2, 1)
    res_dict['remote_ipv6_router_id_address'] = comn_tools.array2str(struct_ptr[0].remote_ipv6_router_id_address, 32, 1)
    res_dict['created_by_mib'] = comn_tools.hex_reverse(hex(struct_ptr[0].created_by_mib), 1)
    res_dict['in_operation'] = comn_tools.hex_reverse(hex(struct_ptr[0].in_operation), 1)
    res_dict['lock_data_link'] = comn_tools.hex_reverse(hex(struct_ptr[0].lock_data_link), 4)
    res_dict['if_tunnel_id_total_length'] = comn_tools.hex_reverse(hex(struct_ptr[0].if_tunnel_id_total_length), 4)
    res_dict['if_tunnel_id_struct_length'] = comn_tools.hex_reverse(hex(struct_ptr[0].if_tunnel_id_struct_length), 4)
    res_dict['if_tunnel_id_tnnl_index'] = comn_tools.hex_reverse(hex(struct_ptr[0].if_tunnel_id_tnnl_index), 2)
    res_dict['if_tunnel_id_tnnl_instance'] = comn_tools.hex_reverse(hex(struct_ptr[0].if_tunnel_id_tnnl_instance), 2)
    res_dict['if_tunnel_id_tnnl_ingress_lsrid_type'] = comn_tools.hex_reverse(hex(struct_ptr[0].if_tunnel_id_tnnl_ingress_lsrid_type), 1)
    res_dict['if_tunnel_id_tnnl_ingress_lsrid_length'] = comn_tools.hex_reverse(hex(struct_ptr[0].if_tunnel_id_tnnl_ingress_lsrid_length), 1)
    res_dict['if_tunnel_id_tnnl_ingress_lsrid_pad1'] = comn_tools.array2str(struct_ptr[0].if_tunnel_id_tnnl_ingress_lsrid_pad1, 2, 1)
    res_dict['if_tunnel_id_tnnl_ingress_lsrid_address'] = comn_tools.array2str(struct_ptr[0].if_tunnel_id_tnnl_ingress_lsrid_address, 32, 1)
    res_dict['if_tunnel_id_tnnl_egress_lsrid_type'] = comn_tools.hex_reverse(hex(struct_ptr[0].if_tunnel_id_tnnl_egress_lsrid_type), 1)
    res_dict['if_tunnel_id_tnnl_egress_lsrid_length'] = comn_tools.hex_reverse(hex(struct_ptr[0].if_tunnel_id_tnnl_egress_lsrid_length), 1)
    res_dict['if_tunnel_id_tnnl_egress_lsrid_pad1'] = comn_tools.array2str(struct_ptr[0].if_tunnel_id_tnnl_egress_lsrid_pad1, 2, 1)
    res_dict['if_tunnel_id_tnnl_egress_lsrid_address'] = comn_tools.array2str(struct_ptr[0].if_tunnel_id_tnnl_egress_lsrid_address, 32, 1)
    res_dict['emulated_if'] = comn_tools.hex_reverse(hex(struct_ptr[0].emulated_if), 1)
    res_dict['bypass_prot_if_idx'] = comn_tools.hex_reverse(hex(struct_ptr[0].bypass_prot_if_idx), 4)
    res_dict['local_transport_node_id'] = comn_tools.hex_reverse(hex(struct_ptr[0].local_transport_node_id), 4)
    res_dict['remote_transport_node_id'] = comn_tools.hex_reverse(hex(struct_ptr[0].remote_transport_node_id), 4)
    res_dict['board_type'] = comn_tools.hex_reverse(hex(struct_ptr[0].board_type), 4)
    res_dict['line_number'] = comn_tools.hex_reverse(hex(struct_ptr[0].line_number), 4)
    res_dict['if_route_offset'] = comn_tools.hex_reverse(hex(struct_ptr[0].if_route_offset), 4)
    res_dict['if_route_total_length'] = comn_tools.hex_reverse(hex(struct_ptr[0].if_route_total_length), 4)
    res_dict['igp_shortcut_metric_type'] = comn_tools.hex_reverse(hex(struct_ptr[0].igp_shortcut_metric_type), 4)
    res_dict['igp_shortcut_metric_value'] = comn_tools.hex_reverse(hex(struct_ptr[0].igp_shortcut_metric_value), 4)
    res_dict['signaling_interface'] = comn_tools.hex_reverse(hex(struct_ptr[0].signaling_interface), 4)
    res_dict['lambda_can_switch'] = comn_tools.hex_reverse(hex(struct_ptr[0].lambda_can_switch), 1)
    res_dict['relay_otu_number'] = comn_tools.hex_reverse(hex(struct_ptr[0].relay_otu_number), 2)
    res_dict['is_relay'] = comn_tools.hex_reverse(hex(struct_ptr[0].is_relay), 1)
    res_dict['relay_otu_free_number'] = comn_tools.hex_reverse(hex(struct_ptr[0].relay_otu_free_number), 2)
    res_dict['min_lambda_index'] = comn_tools.hex_reverse(hex(struct_ptr[0].min_lambda_index), 4)
    res_dict['normal_otu_number'] = comn_tools.hex_reverse(hex(struct_ptr[0].normal_otu_number), 2)
    
    return res_dict

def atg_i3r_cb_interface_analyse(data_ptr, cb_type):
    hex_str = bytes().fromhex(data_ptr)
    hex_str_buffer = create_string_buffer(hex_str)
    struct_ptr = cast(hex_str_buffer, POINTER(atg_i3r_cb_interface))
    print('struct_entity_len', sizeof(struct_ptr[0]))
    struct_dict = atg_i3r_cb_interface_fill_data(struct_ptr, cb_type)
    
    return struct_dict

def atg_i3r_cb_interface_fill_struct(struct_dict):
    struct_entity = atg_i3r_cb_interface()
    struct_len = sizeof(atg_i3r_cb_interface)
    struct_entity.rep_cb_hdr_total_length = int(comn_tools.hex_reverse(struct_dict['rep_cb_hdr_total_length'], 4), 16)
    struct_entity.rep_cb_hdr_cb_type = int(comn_tools.hex_reverse(struct_dict['rep_cb_hdr_cb_type'], 4), 16)
    _ = comn_tools.str2array(struct_dict['if_name'], struct_entity.if_name, 1)
    struct_entity.normal_otu_number = int(comn_tools.hex_reverse(struct_dict['normal_otu_number'], 2), 16)

    
    return struct_entity, struct_len
    

def atg_i3r_cb_interface_dict2str(struct_dict, cb_type):
    struct_entity, struct_len = atg_i3r_cb_interface_fill_struct(struct_dict)
    hex_str = comn_tools.struct2str(struct_entity, struct_len, cb_type)
    
    return hex_str
    