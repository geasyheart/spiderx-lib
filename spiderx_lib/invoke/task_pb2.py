# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: task.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='task.proto',
  package='task',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\ntask.proto\x12\x04task\"\xc8\x01\n\x0fSendTaskRequest\x12\x0e\n\x06policy\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\x12\x11\n\tsite_name\x18\x03 \x01(\t\x12\r\n\x05\x64\x65pth\x18\x04 \x01(\x05\x12\x0e\n\x06\x66\x61ther\x18\x05 \x01(\t\x12\x11\n\ttask_type\x18\x06 \x01(\t\x12\x13\n\x0b\x64ont_filter\x18\x07 \x01(\x08\x12\x0f\n\x07task_id\x18\x08 \x01(\t\x12\x1c\n\x04stat\x18\t \x01(\x0e\x32\x0e.task.StatType\x12\x0f\n\x07message\x18\n \x01(\t\"6\n\x11ReplyTaskResponse\x12\x10\n\x08\x65rr_code\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t*1\n\x08StatType\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x0b\n\x07\x46\x41ILURE\x10\x02\x32S\n\x0bTaskService\x12\x44\n\x10SendTaskByClient\x12\x15.task.SendTaskRequest\x1a\x17.task.ReplyTaskResponse\"\x00\x62\x06proto3')
)

_STATTYPE = _descriptor.EnumDescriptor(
  name='StatType',
  full_name='task.StatType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DEFAULT', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILURE', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=279,
  serialized_end=328,
)
_sym_db.RegisterEnumDescriptor(_STATTYPE)

StatType = enum_type_wrapper.EnumTypeWrapper(_STATTYPE)
DEFAULT = 0
SUCCESS = 1
FAILURE = 2



_SENDTASKREQUEST = _descriptor.Descriptor(
  name='SendTaskRequest',
  full_name='task.SendTaskRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='policy', full_name='task.SendTaskRequest.policy', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='url', full_name='task.SendTaskRequest.url', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='site_name', full_name='task.SendTaskRequest.site_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='depth', full_name='task.SendTaskRequest.depth', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='father', full_name='task.SendTaskRequest.father', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='task_type', full_name='task.SendTaskRequest.task_type', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dont_filter', full_name='task.SendTaskRequest.dont_filter', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='task_id', full_name='task.SendTaskRequest.task_id', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stat', full_name='task.SendTaskRequest.stat', index=8,
      number=9, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='task.SendTaskRequest.message', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=21,
  serialized_end=221,
)


_REPLYTASKRESPONSE = _descriptor.Descriptor(
  name='ReplyTaskResponse',
  full_name='task.ReplyTaskResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='err_code', full_name='task.ReplyTaskResponse.err_code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='task.ReplyTaskResponse.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=223,
  serialized_end=277,
)

_SENDTASKREQUEST.fields_by_name['stat'].enum_type = _STATTYPE
DESCRIPTOR.message_types_by_name['SendTaskRequest'] = _SENDTASKREQUEST
DESCRIPTOR.message_types_by_name['ReplyTaskResponse'] = _REPLYTASKRESPONSE
DESCRIPTOR.enum_types_by_name['StatType'] = _STATTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SendTaskRequest = _reflection.GeneratedProtocolMessageType('SendTaskRequest', (_message.Message,), {
  'DESCRIPTOR' : _SENDTASKREQUEST,
  '__module__' : 'task_pb2'
  # @@protoc_insertion_point(class_scope:task.SendTaskRequest)
  })
_sym_db.RegisterMessage(SendTaskRequest)

ReplyTaskResponse = _reflection.GeneratedProtocolMessageType('ReplyTaskResponse', (_message.Message,), {
  'DESCRIPTOR' : _REPLYTASKRESPONSE,
  '__module__' : 'task_pb2'
  # @@protoc_insertion_point(class_scope:task.ReplyTaskResponse)
  })
_sym_db.RegisterMessage(ReplyTaskResponse)



_TASKSERVICE = _descriptor.ServiceDescriptor(
  name='TaskService',
  full_name='task.TaskService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=330,
  serialized_end=413,
  methods=[
  _descriptor.MethodDescriptor(
    name='SendTaskByClient',
    full_name='task.TaskService.SendTaskByClient',
    index=0,
    containing_service=None,
    input_type=_SENDTASKREQUEST,
    output_type=_REPLYTASKRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_TASKSERVICE)

DESCRIPTOR.services_by_name['TaskService'] = _TASKSERVICE

# @@protoc_insertion_point(module_scope)
