# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: serviceMisc.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import service as _service
from google.protobuf import service_reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import universal.public_pb2
import common_pb2
import im_pb2
import task_pb2
import props_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='serviceMisc.proto',
  package='',
  serialized_pb='\n\x11serviceMisc.proto\x1a\x16universal/public.proto\x1a\x0c\x63ommon.proto\x1a\x08im.proto\x1a\ntask.proto\x1a\x0bprops.proto2\xac\x01\n\x15gameServerMiscService\x12.\n\x0erpcGoAhead2get\x12\x0e.common.int32_\x1a\x0c.public.fake\x12\x30\n\x10rpcGoAhead2IdGet\x12\x0e.common.int64_\x1a\x0c.public.fake\x12\x31\n\x0crpcHeartBeat\x12\x0e.common.int32_\x1a\x11.common.int32Pair2\xa0\x01\n\x15gameClientMiscService\x12,\n\x0brpcAddProps\x12\x0f.props.propsMsg\x1a\x0c.public.fake\x12+\n\x0brpcDelProps\x12\x0e.common.int64_\x1a\x0c.public.fake\x12,\n\x0brpcModProps\x12\x0f.props.propsMsg\x1a\x0c.public.fakeB\x03\x90\x01\x01')





DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\220\001\001')

_GAMESERVERMISCSERVICE = _descriptor.ServiceDescriptor(
  name='gameServerMiscService',
  full_name='gameServerMiscService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=95,
  serialized_end=267,
  methods=[
  _descriptor.MethodDescriptor(
    name='rpcGoAhead2get',
    full_name='gameServerMiscService.rpcGoAhead2get',
    index=0,
    containing_service=None,
    input_type=common_pb2._INT32_,
    output_type=universal.public_pb2._FAKE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpcGoAhead2IdGet',
    full_name='gameServerMiscService.rpcGoAhead2IdGet',
    index=1,
    containing_service=None,
    input_type=common_pb2._INT64_,
    output_type=universal.public_pb2._FAKE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpcHeartBeat',
    full_name='gameServerMiscService.rpcHeartBeat',
    index=2,
    containing_service=None,
    input_type=common_pb2._INT32_,
    output_type=common_pb2._INT32PAIR,
    options=None,
  ),
])

class gameServerMiscService(_service.Service):
  __metaclass__ = service_reflection.GeneratedServiceType
  DESCRIPTOR = _GAMESERVERMISCSERVICE
class gameServerMiscService_Stub(gameServerMiscService):
  __metaclass__ = service_reflection.GeneratedServiceStubType
  DESCRIPTOR = _GAMESERVERMISCSERVICE


_GAMECLIENTMISCSERVICE = _descriptor.ServiceDescriptor(
  name='gameClientMiscService',
  full_name='gameClientMiscService',
  file=DESCRIPTOR,
  index=1,
  options=None,
  serialized_start=270,
  serialized_end=430,
  methods=[
  _descriptor.MethodDescriptor(
    name='rpcAddProps',
    full_name='gameClientMiscService.rpcAddProps',
    index=0,
    containing_service=None,
    input_type=props_pb2._PROPSMSG,
    output_type=universal.public_pb2._FAKE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpcDelProps',
    full_name='gameClientMiscService.rpcDelProps',
    index=1,
    containing_service=None,
    input_type=common_pb2._INT64_,
    output_type=universal.public_pb2._FAKE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpcModProps',
    full_name='gameClientMiscService.rpcModProps',
    index=2,
    containing_service=None,
    input_type=props_pb2._PROPSMSG,
    output_type=universal.public_pb2._FAKE,
    options=None,
  ),
])

class gameClientMiscService(_service.Service):
  __metaclass__ = service_reflection.GeneratedServiceType
  DESCRIPTOR = _GAMECLIENTMISCSERVICE
class gameClientMiscService_Stub(gameClientMiscService):
  __metaclass__ = service_reflection.GeneratedServiceStubType
  DESCRIPTOR = _GAMECLIENTMISCSERVICE

# @@protoc_insertion_point(module_scope)