#!/usr/bin/env python
#coding:utf-8

from ctypes import *
from dbutil import comn_tools
import collections

'''For each cbtype struct you should define a class, 2 functions for data analyse 
and 2 functions for data load back to txtfile '''

# structure class for atg_i3r_cb_interface cbtype
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
                ('in_operation', c_ulong),
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
                ('emulated_if', c_ulong),
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
                ('lambda_can_switch', c_ulong),
                ('relay_otu_number', c_ushort),
                ('is_relay', c_ulong),
                ('relay_otu_free_number', c_ushort),
                ('min_lambda_index', c_ulong),
                ('normal_otu_number', c_ushort)]
  

# get data from cbtype struct and fill data into dictionary   
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
    res_dict['if_name'] = comn_tools.array2str(struct_ptr[0].if_name, 1)
    res_dict['if_type'] = comn_tools.hex_reverse(hex(struct_ptr[0].if_type), 4)
    res_dict['if_flags'] = comn_tools.hex_reverse(hex(struct_ptr[0].if_flags), 4)
    res_dict['if_mtu'] = comn_tools.hex_reverse(hex(struct_ptr[0].if_mtu), 4)
    res_dict['remote_router_id'] = comn_tools.hex_reverse(hex(struct_ptr[0].remote_router_id), 4)
    res_dict['remote_if_id'] = comn_tools.hex_reverse(hex(struct_ptr[0].remote_if_id), 4)
    res_dict['resource_class'] = comn_tools.hex_reverse(hex(struct_ptr[0].resource_class), 4)
    res_dict['use_ospf_router_id'] = comn_tools.hex_reverse(hex(struct_ptr[0].use_ospf_router_id), 1)
    res_dict['ospf_router_id'] = comn_tools.array2str(struct_ptr[0].ospf_router_id, 1)
    res_dict['use_isis_system_id'] = comn_tools.hex_reverse(hex(struct_ptr[0].use_isis_system_id), 1)
    res_dict['isis_system_id'] = comn_tools.array2str(struct_ptr[0].isis_system_id, 1)
    res_dict['physical_address_length'] = comn_tools.hex_reverse(hex(struct_ptr[0].physical_address_length), 1)
    res_dict['physical_address'] = comn_tools.array2str(struct_ptr[0].physical_address, 1)
    res_dict['containing_bundle_if_id'] = comn_tools.hex_reverse(hex(struct_ptr[0].containing_bundle_if_id), 4)
    res_dict['is_enni_level'] = comn_tools.hex_reverse(hex(struct_ptr[0].is_enni_level), 4)
    res_dict['enni_remote_rc_id'] = comn_tools.array2str(struct_ptr[0].enni_remote_rc_id, 1)
    res_dict['local_endpoint_id'] = comn_tools.array2str(struct_ptr[0].local_endpoint_id, 1)
    res_dict['remote_endpoint_id'] = comn_tools.array2str(struct_ptr[0].remote_endpoint_id, 1)
    res_dict['next_hop_address_type'] = comn_tools.hex_reverse(hex(struct_ptr[0].next_hop_address_type), 1)
    res_dict['next_hop_address_length'] = comn_tools.hex_reverse(hex(struct_ptr[0].next_hop_address_length), 1)
    res_dict['next_hop_address_pad1'] = comn_tools.array2str(struct_ptr[0].next_hop_address_pad1, 1)
    res_dict['next_hop_address_address'] = comn_tools.array2str(struct_ptr[0].next_hop_address_address, 1)
    res_dict['remote_signaling_address_type'] = comn_tools.hex_reverse(hex(struct_ptr[0].remote_signaling_address_type), 1)
    res_dict['remote_signaling_address_length'] = comn_tools.hex_reverse(hex(struct_ptr[0].remote_signaling_address_length), 1)
    res_dict['remote_signaling_address_pad1'] = comn_tools.array2str(struct_ptr[0].remote_signaling_address_pad1, 1)
    res_dict['remote_signaling_address_address'] = comn_tools.array2str(struct_ptr[0].remote_signaling_address_address, 1)
    res_dict['opaque_param_len'] = comn_tools.hex_reverse(hex(struct_ptr[0].opaque_param_len), 4)
    res_dict['opaque_param'] = comn_tools.array2str(struct_ptr[0].opaque_param, 1)
    res_dict['uni_version'] = comn_tools.hex_reverse(hex(struct_ptr[0].uni_version), 4)
    res_dict['remote_ipv6_router_id_type'] = comn_tools.hex_reverse(hex(struct_ptr[0].remote_ipv6_router_id_type), 1)
    res_dict['remote_ipv6_router_id_length'] = comn_tools.hex_reverse(hex(struct_ptr[0].remote_ipv6_router_id_length), 1)
    res_dict['remote_ipv6_router_id_pad1'] = comn_tools.array2str(struct_ptr[0].remote_ipv6_router_id_pad1, 1)
    res_dict['remote_ipv6_router_id_address'] = comn_tools.array2str(struct_ptr[0].remote_ipv6_router_id_address, 1)
    res_dict['created_by_mib'] = comn_tools.hex_reverse(hex(struct_ptr[0].created_by_mib), 1)
    res_dict['in_operation'] = comn_tools.hex_reverse(hex(struct_ptr[0].in_operation), 4)
    res_dict['lock_data_link'] = comn_tools.hex_reverse(hex(struct_ptr[0].lock_data_link), 4)
    res_dict['if_tunnel_id_total_length'] = comn_tools.hex_reverse(hex(struct_ptr[0].if_tunnel_id_total_length), 4)
    res_dict['if_tunnel_id_struct_length'] = comn_tools.hex_reverse(hex(struct_ptr[0].if_tunnel_id_struct_length), 4)
    res_dict['if_tunnel_id_tnnl_index'] = comn_tools.hex_reverse(hex(struct_ptr[0].if_tunnel_id_tnnl_index), 2)
    res_dict['if_tunnel_id_tnnl_instance'] = comn_tools.hex_reverse(hex(struct_ptr[0].if_tunnel_id_tnnl_instance), 2)
    res_dict['if_tunnel_id_tnnl_ingress_lsrid_type'] = comn_tools.hex_reverse(hex(struct_ptr[0].if_tunnel_id_tnnl_ingress_lsrid_type), 1)
    res_dict['if_tunnel_id_tnnl_ingress_lsrid_length'] = comn_tools.hex_reverse(hex(struct_ptr[0].if_tunnel_id_tnnl_ingress_lsrid_length), 1)
    res_dict['if_tunnel_id_tnnl_ingress_lsrid_pad1'] = comn_tools.array2str(struct_ptr[0].if_tunnel_id_tnnl_ingress_lsrid_pad1, 1)
    res_dict['if_tunnel_id_tnnl_ingress_lsrid_address'] = comn_tools.array2str(struct_ptr[0].if_tunnel_id_tnnl_ingress_lsrid_address, 1)
    res_dict['if_tunnel_id_tnnl_egress_lsrid_type'] = comn_tools.hex_reverse(hex(struct_ptr[0].if_tunnel_id_tnnl_egress_lsrid_type), 1)
    res_dict['if_tunnel_id_tnnl_egress_lsrid_length'] = comn_tools.hex_reverse(hex(struct_ptr[0].if_tunnel_id_tnnl_egress_lsrid_length), 1)
    res_dict['if_tunnel_id_tnnl_egress_lsrid_pad1'] = comn_tools.array2str(struct_ptr[0].if_tunnel_id_tnnl_egress_lsrid_pad1, 1)
    res_dict['if_tunnel_id_tnnl_egress_lsrid_address'] = comn_tools.array2str(struct_ptr[0].if_tunnel_id_tnnl_egress_lsrid_address, 1)
    res_dict['emulated_if'] = comn_tools.hex_reverse(hex(struct_ptr[0].emulated_if), 4)
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
    res_dict['lambda_can_switch'] = comn_tools.hex_reverse(hex(struct_ptr[0].lambda_can_switch), 4)
    res_dict['relay_otu_number'] = comn_tools.hex_reverse(hex(struct_ptr[0].relay_otu_number), 2)
    res_dict['is_relay'] = comn_tools.hex_reverse(hex(struct_ptr[0].is_relay), 4)
    res_dict['relay_otu_free_number'] = comn_tools.hex_reverse(hex(struct_ptr[0].relay_otu_free_number), 2)
    res_dict['min_lambda_index'] = comn_tools.hex_reverse(hex(struct_ptr[0].min_lambda_index), 4)
    res_dict['normal_otu_number'] = comn_tools.hex_reverse(hex(struct_ptr[0].normal_otu_number), 2)
    
    return res_dict

# analyse string data 
'''def atg_i3r_cb_interface_analyse(data_ptr, cb_type, struct_type):
    hex_str = bytes().fromhex(data_ptr)
    hex_str_buffer = create_string_buffer(hex_str)
    struct_ptr = cast(hex_str_buffer, POINTER(struct_type))
    print('struct_entity_len', sizeof(struct_ptr[0]))
    struct_dict = atg_i3r_cb_interface_fill_data(struct_ptr, cb_type)
    
    return struct_dict'''

# get data from dictionary and fill data into cbtype struct 
def atg_i3r_cb_interface_fill_struct(struct_dict):
    struct_entity = atg_i3r_cb_interface()
    struct_len = sizeof(atg_i3r_cb_interface)
    struct_entity.rep_cb_hdr_total_length = int(comn_tools.hex_reverse(struct_dict['rep_cb_hdr_total_length'], 4), 16)
    struct_entity.rep_cb_hdr_cb_type = int(comn_tools.hex_reverse(struct_dict['rep_cb_hdr_cb_type'], 4), 16)
    _ = comn_tools.str2array(struct_dict['if_name'], struct_entity.if_name, 1)
    struct_entity.normal_otu_number = int(comn_tools.hex_reverse(struct_dict['normal_otu_number'], 2), 16)
    #struct_entity.normal_otu_number = int(comn_tools.hex_reverse('0x1a2b', 2), 16)

    
    return struct_entity, struct_len

# turn data of each key in dictionary to sting
'''def atg_i3r_cb_interface_dict2str(struct_dict, cb_type):
    struct_entity, struct_len = atg_i3r_cb_interface_fill_struct(struct_dict)
    hex_str = comn_tools.struct2str(struct_entity, struct_len, cb_type)
    
    return hex_str'''

class I3_LABEL_INFO(Structure):
    _fields_ = [('label_status',c_ubyte),
               ('num_shared_lsp',c_ubyte),
               ('label_op_fr',c_ubyte)]
                   
class atg_i3r_cb_mpls_interface(Structure):
     _fields_ = [('rep_cb_hdr_total_length', c_ulong),
                ('rep_cb_hdr_struct_length', c_ulong),
                ('rep_cb_hdr_cb_type', c_ulong),
                ('rep_cb_hdr_format_number', c_ulong),
                ('row_status', c_ubyte),
                ('admin_status', c_ubyte),
                ('oper_status', c_ubyte),
                ('instance_index', c_ulong),
                ('if_index', c_ulong),
                ('if_signalling_capabilities',c_ubyte),
                ('use_refr_msgs',c_ubyte),
                ('use_message_ids',c_ubyte),
                ('bundle_send_delay',c_ulong),
                ('rapid_retrans_interval',c_ulong),
                ('rapid_retrans_decay',c_ubyte),
                ('rapid_retrans_limit',c_ulong),
                ('refresh_interval',c_ulong),
                ('label_space_parms_label_space_type',c_ubyte),
                ('label_space_parms_gen_parms_min_label_flags',c_ushort),
                ('label_space_parms_gen_parms_min_label_pad',c_ubyte * 2),
                ('label_space_parms_gen_parms_min_label_len',c_ulong),
                ('label_space_parms_gen_parms_min_label_label',c_ubyte * 16),
                ('label_space_parms_gen_parms_max_label_flags',c_ushort),
                ('label_space_parms_gen_parms_max_label_pad',c_ubyte * 2),
                ('label_space_parms_gen_parms_max_label_len',c_ulong),
                ('label_space_parms_gen_parms_max_label_label',c_ubyte * 16),
                ('label_space_parms_atm_parms_min_vpi',c_ushort),
                ('label_space_parms_atm_parms_max_vpi',c_ushort),
                ('label_space_parms_atm_parms_min_vci',c_ushort),
                ('label_space_parms_atm_parms_max_vci',c_ushort),
                ('label_space_parms_fr_parms_dlci_length',c_ubyte),
                ('label_space_parms_fr_parms_min_dlci_flags',c_ushort),
                ('label_space_parms_fr_parms_min_dlci_pad',c_ubyte * 2),
                ('label_space_parms_fr_parms_min_dlci_len',c_ulong),
                ('label_space_parms_fr_parms_min_dlci_label',c_ubyte * 16),
                ('label_space_parms_fr_parms_max_dlci_flags',c_ushort),
                ('label_space_parms_fr_parms_max_dlci_pad',c_ubyte * 2),
                ('label_space_parms_fr_parms_max_dlci_len',c_ulong),
                ('label_space_parms_fr_parms_max_dlci_label',c_ubyte * 16),
                ('use_suggested_labels',c_ubyte),
                ('atm_vp_vc_capability',c_ubyte),
                ('bidir_vc_capability',c_ubyte),
                ('vc_merge_capability',c_ubyte),
                ('vp_merge_capability',c_ubyte),
                ('label_space_id',c_ushort),
                ('distribution_mode',c_ubyte),
                ('retention_mode',c_ubyte),
                ('path_vector_limit',c_ulong),
                ('hop_count_limit',c_ulong),
                ('hello_period',c_ulong),
                ('hello_decay',c_ulong),
                ('hello_tolerance',c_ulong),
                ('hello_persist',c_ulong),
                ('global_label_space',c_ubyte),
                ('switch_managed_label_space',c_ubyte),
                ('php_supported',c_ubyte),
                ('send_crypto_authentication',c_ubyte),
                ('rcv_crypto_authentication',c_ubyte),
                ('crypto_msg_delivery_tolerance',c_ushort),
                ('if_prop_flags',c_ulong),
                ('rsvp_egl_usage',c_ulong),
                ('ldp_egl_usage',c_ulong),
                ('refresh_multiple',c_ulong),
                ('refresh_slew_denominator',c_ulong),
                ('refresh_slew_numerator',c_ulong),
                ('blockade_multiple',c_ulong),
                ('use_legacy_frr_obj',c_ubyte),
                ('hello_addr_flags',c_ubyte),
                ('summary_refresh_interval',c_ulong),
                ('use_rsvp_hellos_for_all_p2p',c_ubyte),
                ('sdh_sig_type',c_ubyte),
                ('if_type',c_ulong),
                ('send_crypto_auth_type',c_ubyte),
                ('rcv_crypto_auth_type',c_ubyte),
                ('bfd_flags',c_ubyte),
                ('total_bandwidth',c_ulong),
                ('pc_used_bw',c_ulong * 2),
                ('sdh_intface_label_offset',c_ulong),
                ('sdh_intface_label_total_length',c_ulong),
                ('num_label_exec_intface',c_ulong),
                ('exec_intface_label_offset',c_ulong),
                ('exec_intface_label_total_length',c_ulong),
                ('num_label_fiber_intface',c_ulong),
                ('fiber_intface_label_offset',c_ulong),
                ('fiber_intface_label_total_length',c_ulong),
                ('num_ptn_label',c_ulong),
                ('ptn_label_offset',c_ulong),
                ('ptn_label_total_length',c_ulong),
                ('odu0_status',I3_LABEL_INFO * 160),
                ('hello_ttl',c_ulong),
                ('link_error',c_ulong) ]
                
def atg_i3r_cb_mpls_interface_fill_data(struct_ptr, cb_type):
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
    res_dict['if_signalling_capabilities'] = comn_tools.hex_reverse(hex(struct_ptr[0].if_signalling_capabilities), 1)
    res_dict['use_refr_msgs'] = comn_tools.hex_reverse(hex(struct_ptr[0].use_refr_msgs), 1)
    res_dict['use_message_ids'] = comn_tools.hex_reverse(hex(struct_ptr[0].use_message_ids), 1)
    res_dict['bundle_send_delay'] = comn_tools.hex_reverse(hex(struct_ptr[0].bundle_send_delay), 4)
    res_dict['rapid_retrans_interval'] = comn_tools.hex_reverse(hex(struct_ptr[0].rapid_retrans_interval), 4)
    res_dict['rapid_retrans_decay'] = comn_tools.hex_reverse(hex(struct_ptr[0].rapid_retrans_decay), 1)
    res_dict['rapid_retrans_limit'] = comn_tools.hex_reverse(hex(struct_ptr[0].rapid_retrans_limit), 4)
    res_dict['label_space_parms_label_space_type'] = comn_tools.hex_reverse(hex(struct_ptr[0].label_space_parms_label_space_type), 1)
    res_dict['label_space_parms_gen_parms_min_label_flags'] = comn_tools.hex_reverse(hex(struct_ptr[0].label_space_parms_gen_parms_min_label_flags), 2)
    res_dict['label_space_parms_gen_parms_min_label_pad'] = comn_tools.array2str(struct_ptr[0].label_space_parms_gen_parms_min_label_pad, 1)
    res_dict['label_space_parms_gen_parms_min_label_len'] = comn_tools.hex_reverse(hex(struct_ptr[0].label_space_parms_gen_parms_min_label_len), 4)
    res_dict['label_space_parms_gen_parms_min_label_label'] = comn_tools.array2str(struct_ptr[0].label_space_parms_gen_parms_min_label_label, 1)
    res_dict['label_space_parms_gen_parms_max_label_flags'] = comn_tools.hex_reverse(hex(struct_ptr[0].label_space_parms_gen_parms_max_label_flags), 2)
    res_dict['label_space_parms_gen_parms_max_label_pad'] = comn_tools.array2str(struct_ptr[0].label_space_parms_gen_parms_max_label_pad, 1)
    res_dict['label_space_parms_gen_parms_max_label_len'] = comn_tools.hex_reverse(hex(struct_ptr[0].label_space_parms_gen_parms_max_label_len), 4)
    res_dict['label_space_parms_gen_parms_max_label_label'] = comn_tools.array2str(struct_ptr[0].label_space_parms_gen_parms_max_label_label, 1)
    res_dict['label_space_parms_atm_parms_min_vpi'] = comn_tools.hex_reverse(hex(struct_ptr[0].label_space_parms_atm_parms_min_vpi), 2)
    res_dict['label_space_parms_atm_parms_max_vpi'] = comn_tools.hex_reverse(hex(struct_ptr[0].label_space_parms_atm_parms_max_vpi), 2)
    res_dict['label_space_parms_atm_parms_min_vci'] = comn_tools.hex_reverse(hex(struct_ptr[0].label_space_parms_atm_parms_min_vci), 2)
    res_dict['label_space_parms_atm_parms_max_vci'] = comn_tools.hex_reverse(hex(struct_ptr[0].label_space_parms_atm_parms_max_vci), 2)
    res_dict['label_space_parms_fr_parms_dlci_length'] = comn_tools.hex_reverse(hex(struct_ptr[0].label_space_parms_fr_parms_dlci_length), 1)
    res_dict['label_space_parms_fr_parms_min_dlci_flags'] = comn_tools.hex_reverse(hex(struct_ptr[0].label_space_parms_fr_parms_min_dlci_flags), 2)
    res_dict['label_space_parms_fr_parms_min_dlci_pad'] = comn_tools.array2str(struct_ptr[0].label_space_parms_fr_parms_min_dlci_pad, 1)
    res_dict['label_space_parms_fr_parms_min_dlci_len'] = comn_tools.hex_reverse(hex(struct_ptr[0].label_space_parms_fr_parms_min_dlci_len), 4)
    res_dict['label_space_parms_fr_parms_min_dlci_label'] = comn_tools.array2str(struct_ptr[0].label_space_parms_fr_parms_min_dlci_label, 1)
    res_dict['label_space_parms_fr_parms_max_dlci_flags'] = comn_tools.hex_reverse(hex(struct_ptr[0].label_space_parms_fr_parms_max_dlci_flags), 2)
    res_dict['label_space_parms_fr_parms_max_dlci_pad'] = comn_tools.array2str(struct_ptr[0].label_space_parms_fr_parms_max_dlci_pad, 1)
    res_dict['label_space_parms_fr_parms_max_dlci_len'] = comn_tools.hex_reverse(hex(struct_ptr[0].label_space_parms_fr_parms_max_dlci_len), 4)
    res_dict['label_space_parms_fr_parms_max_dlci_label'] = comn_tools.array2str(struct_ptr[0].label_space_parms_fr_parms_max_dlci_label, 1)
    res_dict['use_suggested_labels'] = comn_tools.hex_reverse(hex(struct_ptr[0].use_suggested_labels), 1)
    res_dict['atm_vp_vc_capability'] = comn_tools.hex_reverse(hex(struct_ptr[0].atm_vp_vc_capability), 1)
    res_dict['bidir_vc_capability'] = comn_tools.hex_reverse(hex(struct_ptr[0].bidir_vc_capability), 1)
    res_dict['vc_merge_capability'] = comn_tools.hex_reverse(hex(struct_ptr[0].vc_merge_capability), 1)
    res_dict['vp_merge_capability'] = comn_tools.hex_reverse(hex(struct_ptr[0].vp_merge_capability), 1)
    res_dict['label_space_id'] = comn_tools.hex_reverse(hex(struct_ptr[0].label_space_id), 2)
    res_dict['distribution_mode'] = comn_tools.hex_reverse(hex(struct_ptr[0].distribution_mode), 1)
    res_dict['retention_mode'] = comn_tools.hex_reverse(hex(struct_ptr[0].retention_mode), 1)             
    res_dict['path_vector_limit'] = comn_tools.hex_reverse(hex(struct_ptr[0].path_vector_limit), 4)
    res_dict['hop_count_limit'] = comn_tools.hex_reverse(hex(struct_ptr[0].hop_count_limit), 4)
    res_dict['hello_period'] = comn_tools.hex_reverse(hex(struct_ptr[0].hello_period), 4)
    res_dict['hello_decay'] = comn_tools.hex_reverse(hex(struct_ptr[0].hello_decay), 4)
    res_dict['hello_tolerance'] = comn_tools.hex_reverse(hex(struct_ptr[0].hello_tolerance), 4)
    res_dict['hello_persist'] = comn_tools.hex_reverse(hex(struct_ptr[0].hello_persist), 4)
    res_dict['global_label_space'] = comn_tools.hex_reverse(hex(struct_ptr[0].global_label_space), 1)
    res_dict['switch_managed_label_space'] = comn_tools.hex_reverse(hex(struct_ptr[0].switch_managed_label_space), 1)
    res_dict['php_supported'] = comn_tools.hex_reverse(hex(struct_ptr[0].php_supported), 1)
    res_dict['send_crypto_authentication'] = comn_tools.hex_reverse(hex(struct_ptr[0].send_crypto_authentication), 1)             
    res_dict['rcv_crypto_authentication'] = comn_tools.hex_reverse(hex(struct_ptr[0].rcv_crypto_authentication), 1)
    res_dict['crypto_msg_delivery_tolerance'] = comn_tools.hex_reverse(hex(struct_ptr[0].crypto_msg_delivery_tolerance), 2)
    res_dict['if_prop_flags'] = comn_tools.hex_reverse(hex(struct_ptr[0].if_prop_flags), 4)
    res_dict['rsvp_egl_usage'] = comn_tools.hex_reverse(hex(struct_ptr[0].rsvp_egl_usage), 4)
    res_dict['ldp_egl_usage'] = comn_tools.hex_reverse(hex(struct_ptr[0].ldp_egl_usage), 4)
    res_dict['refresh_multiple'] = comn_tools.hex_reverse(hex(struct_ptr[0].refresh_multiple), 4)
    res_dict['refresh_slew_denominator'] = comn_tools.hex_reverse(hex(struct_ptr[0].refresh_slew_denominator), 4)
    res_dict['refresh_slew_numerator'] = comn_tools.hex_reverse(hex(struct_ptr[0].refresh_slew_numerator), 4)
    res_dict['blockade_multiple'] = comn_tools.hex_reverse(hex(struct_ptr[0].blockade_multiple), 4)
    res_dict['use_legacy_frr_obj'] = comn_tools.hex_reverse(hex(struct_ptr[0].use_legacy_frr_obj), 1)             
    res_dict['hello_addr_flags'] = comn_tools.hex_reverse(hex(struct_ptr[0].hello_addr_flags), 1)
    res_dict['summary_refresh_interval'] = comn_tools.hex_reverse(hex(struct_ptr[0].summary_refresh_interval), 4)
    res_dict['use_rsvp_hellos_for_all_p2p'] = comn_tools.hex_reverse(hex(struct_ptr[0].use_rsvp_hellos_for_all_p2p), 1)
    res_dict['sdh_sig_type'] = comn_tools.hex_reverse(hex(struct_ptr[0].sdh_sig_type), 1)
    res_dict['if_type'] = comn_tools.hex_reverse(hex(struct_ptr[0].if_type), 4)
    res_dict['send_crypto_auth_type'] = comn_tools.hex_reverse(hex(struct_ptr[0].send_crypto_auth_type), 1)
    res_dict['rcv_crypto_auth_type'] = comn_tools.hex_reverse(hex(struct_ptr[0].rcv_crypto_auth_type), 1)
    res_dict['bfd_flags'] = comn_tools.hex_reverse(hex(struct_ptr[0].bfd_flags), 1)
    res_dict['total_bandwidth'] = comn_tools.hex_reverse(hex(struct_ptr[0].blockade_multiple), 4)
    res_dict['pc_used_bw'] = comn_tools.array2str(struct_ptr[0].pc_used_bw, 4)             
    res_dict['sdh_intface_label_offset'] = comn_tools.hex_reverse(hex(struct_ptr[0].sdh_intface_label_offset), 4)
    res_dict['sdh_intface_label_total_length'] = comn_tools.hex_reverse(hex(struct_ptr[0].sdh_intface_label_total_length), 4)
    res_dict['num_label_exec_intface'] = comn_tools.hex_reverse(hex(struct_ptr[0].num_label_exec_intface), 4)
    res_dict['exec_intface_label_offset'] = comn_tools.hex_reverse(hex(struct_ptr[0].exec_intface_label_offset), 4)
    res_dict['exec_intface_label_total_length'] = comn_tools.hex_reverse(hex(struct_ptr[0].exec_intface_label_total_length), 4)
    res_dict['num_label_fiber_intface'] = comn_tools.hex_reverse(hex(struct_ptr[0].num_label_fiber_intface), 4)
    res_dict['fiber_intface_label_offset'] = comn_tools.hex_reverse(hex(struct_ptr[0].fiber_intface_label_offset), 4)
    res_dict['fiber_intface_label_total_length'] = comn_tools.hex_reverse(hex(struct_ptr[0].fiber_intface_label_total_length), 4)
    res_dict['num_ptn_label'] = comn_tools.hex_reverse(hex(struct_ptr[0].num_ptn_label), 4)
    res_dict['ptn_label_offset'] = comn_tools.hex_reverse(hex(struct_ptr[0].ptn_label_offset), 4)
    res_dict['ptn_label_total_length'] = comn_tools.hex_reverse(hex(struct_ptr[0].ptn_label_total_length), 4)
    res_dict['odu0_status'] = comn_tools.strutarray2str(struct_ptr[0].odu0_status, I3_LABEL_INFO)
    res_dict['hello_ttl'] = comn_tools.hex_reverse(hex(struct_ptr[0].hello_ttl), 4)
    res_dict['link_error'] = comn_tools.hex_reverse(hex(struct_ptr[0].link_error), 4)
    
    return res_dict
    
def atg_i3r_cb_mpls_interface_fill_struct(struct_dict):
    struct_entity = atg_i3r_cb_mpls_interface()
    struct_len = sizeof(atg_i3r_cb_mpls_interface)
    _ = comn_tools.str2structarray(struct_dict['odu0_status'], struct_entity.odu0_status, I3_LABEL_INFO)
    
    return struct_entity, struct_len
    