# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: act_guaji.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import service as _service
from google.protobuf import service_reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import universal.public_pb2
import common_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='act_guaji.proto',
  package='act_guaji',
  serialized_pb='\n\x0f\x61\x63t_guaji.proto\x12\tact_guaji\x1a\x16universal/public.proto\x1a\x0c\x63ommon.proto\"\x8f\x01\n\tconfigMsg\x12\x10\n\x08rolePfId\x18\x01 \x01(\x05\x12\x0f\n\x07petPfId\x18\x02 \x01(\x05\x12\x17\n\x0froleOfflinePfId\x18\x03 \x01(\x05\x12\x16\n\x0epetOfflinePfId\x18\x04 \x01(\x05\x12\x15\n\risOfflineTask\x18\x05 \x01(\x08\x12\x17\n\x0fofflineTaskRing\x18\x06 \x01(\x05\x32\x7f\n\rterminal2main\x12\x32\n\x14rpcActGuajiGetConfig\x12\x0c.public.fake\x1a\x0c.public.fake\x12:\n\x14rpcActGuajiSetConfig\x12\x14.act_guaji.configMsg\x1a\x0c.public.fake2\x87\x01\n\rmain2terminal\x12\x37\n\x11rpcActGuajiConfig\x12\x14.act_guaji.configMsg\x1a\x0c.public.fake\x12=\n\x17rpcActGuajiConfigChange\x12\x14.act_guaji.configMsg\x1a\x0c.public.fakeB\x03\x90\x01\x01')




_CONFIGMSG = _descriptor.Descriptor(
  name='configMsg',
  full_name='act_guaji.configMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rolePfId', full_name='act_guaji.configMsg.rolePfId', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='petPfId', full_name='act_guaji.configMsg.petPfId', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='roleOfflinePfId', full_name='act_guaji.configMsg.roleOfflinePfId', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='petOfflinePfId', full_name='act_guaji.configMsg.petOfflinePfId', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='isOfflineTask', full_name='act_guaji.configMsg.isOfflineTask', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='offlineTaskRing', full_name='act_guaji.configMsg.offlineTaskRing', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=69,
  serialized_end=212,
)

DESCRIPTOR.message_types_by_name['configMsg'] = _CONFIGMSG

class configMsg(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CONFIGMSG

  # @@protoc_insertion_point(class_scope:act_guaji.configMsg)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\220\001\001')

_TERMINAL2MAIN = _descriptor.ServiceDescriptor(
  name='terminal2main',
  full_name='act_guaji.terminal2main',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=214,
  serialized_end=341,
  methods=[
  _descriptor.MethodDescriptor(
    name='rpcActGuajiGetConfig',
    full_name='act_guaji.terminal2main.rpcActGuajiGetConfig',
    index=0,
    containing_service=None,
    input_type=universal.public_pb2._FAKE,
    output_type=universal.public_pb2._FAKE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpcActGuajiSetConfig',
    full_name='act_guaji.terminal2main.rpcActGuajiSetConfig',
    index=1,
    containing_service=None,
    input_type=_CONFIGMSG,
    output_type=universal.public_pb2._FAKE,
    options=None,
  ),
])

class terminal2main(_service.Service):
  __metaclass__ = service_reflection.GeneratedServiceType
  DESCRIPTOR = _TERMINAL2MAIN
class terminal2main_Stub(terminal2main):
  __metaclass__ = service_reflection.GeneratedServiceStubType
  DESCRIPTOR = _TERMINAL2MAIN


_MAIN2TERMINAL = _descriptor.ServiceDescriptor(
  name='main2terminal',
  full_name='act_guaji.main2terminal',
  file=DESCRIPTOR,
  index=1,
  options=None,
  serialized_start=344,
  serialized_end=479,
  methods=[
  _descriptor.MethodDescriptor(
    name='rpcActGuajiConfig',
    full_name='act_guaji.main2terminal.rpcActGuajiConfig',
    index=0,
    containing_service=None,
    input_type=_CONFIGMSG,
    output_type=universal.public_pb2._FAKE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpcActGuajiConfigChange',
    full_name='act_guaji.main2terminal.rpcActGuajiConfigChange',
    index=1,
    containing_service=None,
    input_type=_CONFIGMSG,
    output_type=universal.public_pb2._FAKE,
    options=None,
  ),
])

class main2terminal(_service.Service):
  __metaclass__ = service_reflection.GeneratedServiceType
  DESCRIPTOR = _MAIN2TERMINAL
class main2terminal_Stub(main2terminal):
  __metaclass__ = service_reflection.GeneratedServiceStubType
  DESCRIPTOR = _MAIN2TERMINAL

# @@protoc_insertion_point(module_scope)