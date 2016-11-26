# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: backEnd_center.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import service as _service
from google.protobuf import service_reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import universal.public_pb2
import universal.base_pb2
import connection_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='backEnd_center.proto',
  package='backEnd_center',
  serialized_pb='\n\x14\x62\x61\x63kEnd_center.proto\x12\x0e\x62\x61\x63kEnd_center\x1a\x16universal/public.proto\x1a\x14universal/base.proto\x1a\x10\x63onnection.proto\"\xdd\x01\n\nresumeInfo\x12\x0e\n\x06roleId\x18\x01 \x02(\x05\x12\r\n\x05level\x18\x02 \x01(\x05\x12\r\n\x05shape\x18\x03 \x01(\x05\x12\x0e\n\x06school\x18\x04 \x01(\x05\x12\x0c\n\x04name\x18\x05 \x01(\x0c\x12\x11\n\tsignature\x18\x06 \x01(\x0c\x12\x13\n\x0bserviceName\x18\x07 \x01(\x0c\x12\x13\n\x0bofflineTime\x18\x08 \x01(\x05\x12\x11\n\tguildName\x18\t \x01(\x0c\x12\x0f\n\x07guildId\x18\n \x01(\x05\x12\x12\n\nshapeParts\x18\x0b \x03(\x05\x12\x0e\n\x06\x63olors\x18\x0c \x03(\x05\"M\n\nresumeList\x12.\n\nresumeList\x18\x01 \x03(\x0b\x32\x1a.backEnd_center.resumeInfo\x12\x0f\n\x07iRoleId\x18\x02 \x01(\x03\"/\n\x0breqNameInfo\x12\x0f\n\x07iGender\x18\x01 \x02(\x05\x12\x0f\n\x07iRoleId\x18\x02 \x02(\x03\"\x1e\n\x0b\x63onfirmInfo\x12\x0f\n\x07iRoleId\x18\x01 \x02(\x03\":\n\nupdateInfo\x12\x0f\n\x07iRoleId\x18\x01 \x01(\x03\x12\r\n\x05sName\x18\x02 \x01(\x0c\x12\x0c\n\x04sOld\x18\x03 \x01(\x0c\"X\n\x0b\x62\x61\x63kEndInfo\x12\x0f\n\x07iZoneNo\x18\x01 \x02(\x05\x12\x14\n\x0ciBackEndType\x18\x02 \x02(\x05\x12\x11\n\tsZoneName\x18\x03 \x02(\x0c\x12\x0f\n\x07iPageNo\x18\x04 \x02(\x05\"\x89\x01\n\x08\x63hatInfo\x12\x0f\n\x07iRoleId\x18\x01 \x02(\x03\x12\x11\n\tiSendTime\x18\x02 \x01(\x05\x12\x10\n\x08sContent\x18\x03 \x01(\x0c\x12\x0e\n\x06iAudio\x18\x04 \x01(\x05\x12\x11\n\tiAudioLen\x18\x05 \x01(\x05\x12\x11\n\tiAudioIdx\x18\x06 \x01(\x05\x12\x11\n\tiSenderId\x18\x07 \x01(\x03\"-\n\x08tipsInfo\x12\x0f\n\x07iRoleId\x18\x01 \x02(\x03\x12\x10\n\x08sContent\x18\x02 \x02(\x0c\x32\xa1\x02\n\x0e\x63\x65nter2backEnd\x12&\n\x08rpcTest2\x12\x0c.public.fake\x1a\x0c.public.fake\x12=\n\x11rpcResumeListSend\x12\x1a.backEnd_center.resumeList\x1a\x0c.public.fake\x12\x34\n\nrpcChatGet\x12\x18.backEnd_center.chatInfo\x1a\x0c.public.fake\x12\x37\n\rrpcTipsCenter\x12\x18.backEnd_center.tipsInfo\x1a\x0c.public.fake\x12\x39\n\rrpcNearbySend\x12\x1a.backEnd_center.resumeList\x1a\x0c.public.fake2\xb8\x05\n\x0e\x62\x61\x63kEnd2center\x12&\n\x08rpcTest1\x12\x0c.public.fake\x1a\x0c.public.fake\x12\x37\n\nrpcGetName\x12\x1b.backEnd_center.reqNameInfo\x1a\x0c.base.bytes_\x12;\n\x0erpcConfirmName\x12\x1b.backEnd_center.confirmInfo\x1a\x0c.public.fake\x12\x31\n\x13rpcHotUpdate2center\x12\x0c.base.bytes_\x1a\x0c.public.fake\x12\x38\n\rrpcUpdateName\x12\x1a.backEnd_center.updateInfo\x1a\x0b.base.bool_\x12<\n\x10rpcBackEndReport\x12\x1b.backEnd_center.backEndInfo\x1a\x0b.base.bool_\x12;\n\x0frpcUpdateResume\x12\x1a.backEnd_center.resumeInfo\x1a\x0c.public.fake\x12<\n\x10rpcResumeListReq\x12\x1a.backEnd_center.resumeList\x1a\x0c.public.fake\x12\x46\n\x0crpcResumeReq\x12\x1a.backEnd_center.resumeInfo\x1a\x1a.backEnd_center.resumeInfo\x12\x35\n\x0brpcChatSend\x12\x18.backEnd_center.chatInfo\x1a\x0c.public.fake\x12\x38\n\x0crpcNearbyReq\x12\x1a.backEnd_center.resumeList\x1a\x0c.public.fake\x12)\n\x0brpcDelAudio\x12\x0c.base.int32_\x1a\x0c.public.fakeB\x03\x90\x01\x01')




_RESUMEINFO = _descriptor.Descriptor(
  name='resumeInfo',
  full_name='backEnd_center.resumeInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='roleId', full_name='backEnd_center.resumeInfo.roleId', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='level', full_name='backEnd_center.resumeInfo.level', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='shape', full_name='backEnd_center.resumeInfo.shape', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='school', full_name='backEnd_center.resumeInfo.school', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='backEnd_center.resumeInfo.name', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='signature', full_name='backEnd_center.resumeInfo.signature', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='serviceName', full_name='backEnd_center.resumeInfo.serviceName', index=6,
      number=7, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='offlineTime', full_name='backEnd_center.resumeInfo.offlineTime', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='guildName', full_name='backEnd_center.resumeInfo.guildName', index=8,
      number=9, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='guildId', full_name='backEnd_center.resumeInfo.guildId', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='shapeParts', full_name='backEnd_center.resumeInfo.shapeParts', index=10,
      number=11, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='colors', full_name='backEnd_center.resumeInfo.colors', index=11,
      number=12, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=105,
  serialized_end=326,
)


_RESUMELIST = _descriptor.Descriptor(
  name='resumeList',
  full_name='backEnd_center.resumeList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resumeList', full_name='backEnd_center.resumeList.resumeList', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iRoleId', full_name='backEnd_center.resumeList.iRoleId', index=1,
      number=2, type=3, cpp_type=2, label=1,
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
  serialized_start=328,
  serialized_end=405,
)


_REQNAMEINFO = _descriptor.Descriptor(
  name='reqNameInfo',
  full_name='backEnd_center.reqNameInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='iGender', full_name='backEnd_center.reqNameInfo.iGender', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iRoleId', full_name='backEnd_center.reqNameInfo.iRoleId', index=1,
      number=2, type=3, cpp_type=2, label=2,
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
  serialized_start=407,
  serialized_end=454,
)


_CONFIRMINFO = _descriptor.Descriptor(
  name='confirmInfo',
  full_name='backEnd_center.confirmInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='iRoleId', full_name='backEnd_center.confirmInfo.iRoleId', index=0,
      number=1, type=3, cpp_type=2, label=2,
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
  serialized_start=456,
  serialized_end=486,
)


_UPDATEINFO = _descriptor.Descriptor(
  name='updateInfo',
  full_name='backEnd_center.updateInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='iRoleId', full_name='backEnd_center.updateInfo.iRoleId', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sName', full_name='backEnd_center.updateInfo.sName', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sOld', full_name='backEnd_center.updateInfo.sOld', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
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
  serialized_start=488,
  serialized_end=546,
)


_BACKENDINFO = _descriptor.Descriptor(
  name='backEndInfo',
  full_name='backEnd_center.backEndInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='iZoneNo', full_name='backEnd_center.backEndInfo.iZoneNo', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iBackEndType', full_name='backEnd_center.backEndInfo.iBackEndType', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sZoneName', full_name='backEnd_center.backEndInfo.sZoneName', index=2,
      number=3, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iPageNo', full_name='backEnd_center.backEndInfo.iPageNo', index=3,
      number=4, type=5, cpp_type=1, label=2,
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
  serialized_start=548,
  serialized_end=636,
)


_CHATINFO = _descriptor.Descriptor(
  name='chatInfo',
  full_name='backEnd_center.chatInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='iRoleId', full_name='backEnd_center.chatInfo.iRoleId', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iSendTime', full_name='backEnd_center.chatInfo.iSendTime', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sContent', full_name='backEnd_center.chatInfo.sContent', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iAudio', full_name='backEnd_center.chatInfo.iAudio', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iAudioLen', full_name='backEnd_center.chatInfo.iAudioLen', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iAudioIdx', full_name='backEnd_center.chatInfo.iAudioIdx', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iSenderId', full_name='backEnd_center.chatInfo.iSenderId', index=6,
      number=7, type=3, cpp_type=2, label=1,
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
  serialized_start=639,
  serialized_end=776,
)


_TIPSINFO = _descriptor.Descriptor(
  name='tipsInfo',
  full_name='backEnd_center.tipsInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='iRoleId', full_name='backEnd_center.tipsInfo.iRoleId', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sContent', full_name='backEnd_center.tipsInfo.sContent', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
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
  serialized_start=778,
  serialized_end=823,
)

_RESUMELIST.fields_by_name['resumeList'].message_type = _RESUMEINFO
DESCRIPTOR.message_types_by_name['resumeInfo'] = _RESUMEINFO
DESCRIPTOR.message_types_by_name['resumeList'] = _RESUMELIST
DESCRIPTOR.message_types_by_name['reqNameInfo'] = _REQNAMEINFO
DESCRIPTOR.message_types_by_name['confirmInfo'] = _CONFIRMINFO
DESCRIPTOR.message_types_by_name['updateInfo'] = _UPDATEINFO
DESCRIPTOR.message_types_by_name['backEndInfo'] = _BACKENDINFO
DESCRIPTOR.message_types_by_name['chatInfo'] = _CHATINFO
DESCRIPTOR.message_types_by_name['tipsInfo'] = _TIPSINFO

class resumeInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RESUMEINFO

  # @@protoc_insertion_point(class_scope:backEnd_center.resumeInfo)

class resumeList(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RESUMELIST

  # @@protoc_insertion_point(class_scope:backEnd_center.resumeList)

class reqNameInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _REQNAMEINFO

  # @@protoc_insertion_point(class_scope:backEnd_center.reqNameInfo)

class confirmInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CONFIRMINFO

  # @@protoc_insertion_point(class_scope:backEnd_center.confirmInfo)

class updateInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _UPDATEINFO

  # @@protoc_insertion_point(class_scope:backEnd_center.updateInfo)

class backEndInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _BACKENDINFO

  # @@protoc_insertion_point(class_scope:backEnd_center.backEndInfo)

class chatInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CHATINFO

  # @@protoc_insertion_point(class_scope:backEnd_center.chatInfo)

class tipsInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TIPSINFO

  # @@protoc_insertion_point(class_scope:backEnd_center.tipsInfo)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\220\001\001')

_CENTER2BACKEND = _descriptor.ServiceDescriptor(
  name='center2backEnd',
  full_name='backEnd_center.center2backEnd',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=826,
  serialized_end=1115,
  methods=[
  _descriptor.MethodDescriptor(
    name='rpcTest2',
    full_name='backEnd_center.center2backEnd.rpcTest2',
    index=0,
    containing_service=None,
    input_type=universal.public_pb2._FAKE,
    output_type=universal.public_pb2._FAKE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpcResumeListSend',
    full_name='backEnd_center.center2backEnd.rpcResumeListSend',
    index=1,
    containing_service=None,
    input_type=_RESUMELIST,
    output_type=universal.public_pb2._FAKE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpcChatGet',
    full_name='backEnd_center.center2backEnd.rpcChatGet',
    index=2,
    containing_service=None,
    input_type=_CHATINFO,
    output_type=universal.public_pb2._FAKE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpcTipsCenter',
    full_name='backEnd_center.center2backEnd.rpcTipsCenter',
    index=3,
    containing_service=None,
    input_type=_TIPSINFO,
    output_type=universal.public_pb2._FAKE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpcNearbySend',
    full_name='backEnd_center.center2backEnd.rpcNearbySend',
    index=4,
    containing_service=None,
    input_type=_RESUMELIST,
    output_type=universal.public_pb2._FAKE,
    options=None,
  ),
])

class center2backEnd(_service.Service):
  __metaclass__ = service_reflection.GeneratedServiceType
  DESCRIPTOR = _CENTER2BACKEND
class center2backEnd_Stub(center2backEnd):
  __metaclass__ = service_reflection.GeneratedServiceStubType
  DESCRIPTOR = _CENTER2BACKEND


_BACKEND2CENTER = _descriptor.ServiceDescriptor(
  name='backEnd2center',
  full_name='backEnd_center.backEnd2center',
  file=DESCRIPTOR,
  index=1,
  options=None,
  serialized_start=1118,
  serialized_end=1814,
  methods=[
  _descriptor.MethodDescriptor(
    name='rpcTest1',
    full_name='backEnd_center.backEnd2center.rpcTest1',
    index=0,
    containing_service=None,
    input_type=universal.public_pb2._FAKE,
    output_type=universal.public_pb2._FAKE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpcGetName',
    full_name='backEnd_center.backEnd2center.rpcGetName',
    index=1,
    containing_service=None,
    input_type=_REQNAMEINFO,
    output_type=universal.base_pb2._BYTES_,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpcConfirmName',
    full_name='backEnd_center.backEnd2center.rpcConfirmName',
    index=2,
    containing_service=None,
    input_type=_CONFIRMINFO,
    output_type=universal.public_pb2._FAKE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpcHotUpdate2center',
    full_name='backEnd_center.backEnd2center.rpcHotUpdate2center',
    index=3,
    containing_service=None,
    input_type=universal.base_pb2._BYTES_,
    output_type=universal.public_pb2._FAKE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpcUpdateName',
    full_name='backEnd_center.backEnd2center.rpcUpdateName',
    index=4,
    containing_service=None,
    input_type=_UPDATEINFO,
    output_type=universal.base_pb2._BOOL_,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpcBackEndReport',
    full_name='backEnd_center.backEnd2center.rpcBackEndReport',
    index=5,
    containing_service=None,
    input_type=_BACKENDINFO,
    output_type=universal.base_pb2._BOOL_,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpcUpdateResume',
    full_name='backEnd_center.backEnd2center.rpcUpdateResume',
    index=6,
    containing_service=None,
    input_type=_RESUMEINFO,
    output_type=universal.public_pb2._FAKE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpcResumeListReq',
    full_name='backEnd_center.backEnd2center.rpcResumeListReq',
    index=7,
    containing_service=None,
    input_type=_RESUMELIST,
    output_type=universal.public_pb2._FAKE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpcResumeReq',
    full_name='backEnd_center.backEnd2center.rpcResumeReq',
    index=8,
    containing_service=None,
    input_type=_RESUMEINFO,
    output_type=_RESUMEINFO,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpcChatSend',
    full_name='backEnd_center.backEnd2center.rpcChatSend',
    index=9,
    containing_service=None,
    input_type=_CHATINFO,
    output_type=universal.public_pb2._FAKE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpcNearbyReq',
    full_name='backEnd_center.backEnd2center.rpcNearbyReq',
    index=10,
    containing_service=None,
    input_type=_RESUMELIST,
    output_type=universal.public_pb2._FAKE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rpcDelAudio',
    full_name='backEnd_center.backEnd2center.rpcDelAudio',
    index=11,
    containing_service=None,
    input_type=universal.base_pb2._INT32_,
    output_type=universal.public_pb2._FAKE,
    options=None,
  ),
])

class backEnd2center(_service.Service):
  __metaclass__ = service_reflection.GeneratedServiceType
  DESCRIPTOR = _BACKEND2CENTER
class backEnd2center_Stub(backEnd2center):
  __metaclass__ = service_reflection.GeneratedServiceStubType
  DESCRIPTOR = _BACKEND2CENTER

# @@protoc_insertion_point(module_scope)