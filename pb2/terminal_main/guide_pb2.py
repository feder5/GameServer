# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: guide.proto

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
  name='guide.proto',
  package='guide',
  serialized_pb='\n\x0bguide.proto\x12\x05guide\x1a\x16universal/public.proto\x1a\x0c\x63ommon.proto\"?\n\x0bguideRecord\x12\x10\n\x08iGuideNo\x18\x01 \x02(\x05\x12\x0e\n\x06iIsEnd\x18\x02 \x02(\x05\x12\x0e\n\x06iIsNew\x18\x03 \x02(\x05\x32\xa8\x01\n\rterminal2main\x12\x31\n\x11rpcGuideAddRecord\x12\x0e.common.int32_\x1a\x0c.public.fake\x12\x31\n\x11rpcGuideEndRecord\x12\x0e.common.int32_\x1a\x0c.public.fake\x12\x31\n\x11rpcGuideNewRecord\x12\x0e.common.int32_\x1a\x0c.public.fake2z\n\rmain2terminal\x12\x32\n\x0erpcGuideRecord\x12\x12.guide.guideRecord\x1a\x0c.public.fake\x12\x35\n\x15rpcGuideChangeGuideNo\x12\x0e.common.int32_\x1a\x0c.public.fakeB\x03\x90\x01\x01')




_GUIDERECORD = _descriptor.Descriptor(
  name='guideRecord',
  full_name='guide.guideRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='iGuideNo', full_name='guide.guideRecord.iGuideNo', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iIsEnd', full_name='guide.guideRecord.iIsEnd', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iIsNew', full_name='guide.guideRecord.iIsNew', index=2,
      number=3, type=5, cpp_type=1, label=2,
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
  serialized_start=60,
  serialized_end=123,
)

DESCRIPTOR.message_types_by_name['guideRecord'] = _GUIDERECORD

class guideRecord(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GUIDERECORD

  # @@protoc_insertion_point(class_scope:guide.guideRecord)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\220\001\001')

_TERMINAL2MAIN = _descriptor.ServiceDescriptor(
  name='terminal2main',
  full_name='guide.terminal2main',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=126,
  serialized_end=294,
  methods=[
  _descriptor.MethodDescriptor(
    name='rpcGuideAddRecord',
    full_name='guide.terminal2main.rpcGuideAddRecord',
    index=0,
    containing_service=None,
    input_type=common_pb2._INT32_,
    output_type=universal.public_pb2._FAKE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpcGuideEndRecord',
    full_name='guide.terminal2main.rpcGuideEndRecord',
    index=1,
    containing_service=None,
    input_type=common_pb2._INT32_,
    output_type=universal.public_pb2._FAKE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpcGuideNewRecord',
    full_name='guide.terminal2main.rpcGuideNewRecord',
    index=2,
    containing_service=None,
    input_type=common_pb2._INT32_,
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
  full_name='guide.main2terminal',
  file=DESCRIPTOR,
  index=1,
  options=None,
  serialized_start=296,
  serialized_end=418,
  methods=[
  _descriptor.MethodDescriptor(
    name='rpcGuideRecord',
    full_name='guide.main2terminal.rpcGuideRecord',
    index=0,
    containing_service=None,
    input_type=_GUIDERECORD,
    output_type=universal.public_pb2._FAKE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpcGuideChangeGuideNo',
    full_name='guide.main2terminal.rpcGuideChangeGuideNo',
    index=1,
    containing_service=None,
    input_type=common_pb2._INT32_,
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