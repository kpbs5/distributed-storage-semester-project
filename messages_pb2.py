# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: messages.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='messages.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0emessages.proto\"\x93\x01\n\x11storedata_request\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t\x12\x13\n\x0bis_delegate\x18\x02 \x01(\x08\x12\x14\n\x0creplications\x18\x03 \x01(\x05\x12\x15\n\rnodes_visited\x18\x04 \x03(\t\x12\x14\n\x0csend_to_node\x18\x05 \x01(\x05\x12\x14\n\x0cstorage_mode\x18\x06 \x01(\t\"9\n\x0fgetdata_request\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t\x12\x14\n\x0cstorage_mode\x18\x02 \x01(\t\"0\n\x17\x66ragment_status_request\x12\x15\n\rfragment_name\x18\x01 \x01(\t\"e\n\x18\x66ragment_status_response\x12\x15\n\rfragment_name\x18\x01 \x01(\t\x12\x12\n\nis_present\x18\x02 \x01(\x08\x12\x0f\n\x07node_id\x18\x03 \x01(\t\x12\r\n\x05\x63ount\x18\x04 \x01(\x05\"-\n\x06header\x12#\n\x0crequest_type\x18\x01 \x01(\x0e\x32\r.request_type\"f\n\x18recode_fragments_request\x12\x15\n\rfragment_name\x18\x01 \x01(\t\x12\x14\n\x0csymbol_count\x18\x02 \x01(\x05\x12\x1d\n\x15output_fragment_count\x18\x03 \x01(\x05*u\n\x0crequest_type\x12\x17\n\x13\x46RAGMENT_STATUS_REQ\x10\x00\x12\x15\n\x11\x46RAGMENT_DATA_REQ\x10\x01\x12\x1b\n\x17STORE_FRAGMENT_DATA_REQ\x10\x02\x12\x18\n\x14RECODE_FRAGMENTS_REQ\x10\x03\x62\x06proto3'
)

_REQUEST_TYPE = _descriptor.EnumDescriptor(
  name='request_type',
  full_name='request_type',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FRAGMENT_STATUS_REQ', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FRAGMENT_DATA_REQ', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STORE_FRAGMENT_DATA_REQ', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RECODE_FRAGMENTS_REQ', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=531,
  serialized_end=648,
)
_sym_db.RegisterEnumDescriptor(_REQUEST_TYPE)

request_type = enum_type_wrapper.EnumTypeWrapper(_REQUEST_TYPE)
FRAGMENT_STATUS_REQ = 0
FRAGMENT_DATA_REQ = 1
STORE_FRAGMENT_DATA_REQ = 2
RECODE_FRAGMENTS_REQ = 3



_STOREDATA_REQUEST = _descriptor.Descriptor(
  name='storedata_request',
  full_name='storedata_request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='filename', full_name='storedata_request.filename', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='is_delegate', full_name='storedata_request.is_delegate', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='replications', full_name='storedata_request.replications', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nodes_visited', full_name='storedata_request.nodes_visited', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='send_to_node', full_name='storedata_request.send_to_node', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='storage_mode', full_name='storedata_request.storage_mode', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=19,
  serialized_end=166,
)


_GETDATA_REQUEST = _descriptor.Descriptor(
  name='getdata_request',
  full_name='getdata_request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='filename', full_name='getdata_request.filename', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='storage_mode', full_name='getdata_request.storage_mode', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=168,
  serialized_end=225,
)


_FRAGMENT_STATUS_REQUEST = _descriptor.Descriptor(
  name='fragment_status_request',
  full_name='fragment_status_request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='fragment_name', full_name='fragment_status_request.fragment_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=227,
  serialized_end=275,
)


_FRAGMENT_STATUS_RESPONSE = _descriptor.Descriptor(
  name='fragment_status_response',
  full_name='fragment_status_response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='fragment_name', full_name='fragment_status_response.fragment_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='is_present', full_name='fragment_status_response.is_present', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='node_id', full_name='fragment_status_response.node_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='count', full_name='fragment_status_response.count', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=277,
  serialized_end=378,
)


_HEADER = _descriptor.Descriptor(
  name='header',
  full_name='header',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='request_type', full_name='header.request_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=380,
  serialized_end=425,
)


_RECODE_FRAGMENTS_REQUEST = _descriptor.Descriptor(
  name='recode_fragments_request',
  full_name='recode_fragments_request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='fragment_name', full_name='recode_fragments_request.fragment_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='symbol_count', full_name='recode_fragments_request.symbol_count', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='output_fragment_count', full_name='recode_fragments_request.output_fragment_count', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=427,
  serialized_end=529,
)

_HEADER.fields_by_name['request_type'].enum_type = _REQUEST_TYPE
DESCRIPTOR.message_types_by_name['storedata_request'] = _STOREDATA_REQUEST
DESCRIPTOR.message_types_by_name['getdata_request'] = _GETDATA_REQUEST
DESCRIPTOR.message_types_by_name['fragment_status_request'] = _FRAGMENT_STATUS_REQUEST
DESCRIPTOR.message_types_by_name['fragment_status_response'] = _FRAGMENT_STATUS_RESPONSE
DESCRIPTOR.message_types_by_name['header'] = _HEADER
DESCRIPTOR.message_types_by_name['recode_fragments_request'] = _RECODE_FRAGMENTS_REQUEST
DESCRIPTOR.enum_types_by_name['request_type'] = _REQUEST_TYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

storedata_request = _reflection.GeneratedProtocolMessageType('storedata_request', (_message.Message,), {
  'DESCRIPTOR' : _STOREDATA_REQUEST,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:storedata_request)
  })
_sym_db.RegisterMessage(storedata_request)

getdata_request = _reflection.GeneratedProtocolMessageType('getdata_request', (_message.Message,), {
  'DESCRIPTOR' : _GETDATA_REQUEST,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:getdata_request)
  })
_sym_db.RegisterMessage(getdata_request)

fragment_status_request = _reflection.GeneratedProtocolMessageType('fragment_status_request', (_message.Message,), {
  'DESCRIPTOR' : _FRAGMENT_STATUS_REQUEST,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:fragment_status_request)
  })
_sym_db.RegisterMessage(fragment_status_request)

fragment_status_response = _reflection.GeneratedProtocolMessageType('fragment_status_response', (_message.Message,), {
  'DESCRIPTOR' : _FRAGMENT_STATUS_RESPONSE,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:fragment_status_response)
  })
_sym_db.RegisterMessage(fragment_status_response)

header = _reflection.GeneratedProtocolMessageType('header', (_message.Message,), {
  'DESCRIPTOR' : _HEADER,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:header)
  })
_sym_db.RegisterMessage(header)

recode_fragments_request = _reflection.GeneratedProtocolMessageType('recode_fragments_request', (_message.Message,), {
  'DESCRIPTOR' : _RECODE_FRAGMENTS_REQUEST,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:recode_fragments_request)
  })
_sym_db.RegisterMessage(recode_fragments_request)


# @@protoc_insertion_point(module_scope)
