# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: classification.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14\x63lassification.proto\";\n\x08\x42\x36\x34Image\x12\x10\n\x08\x62\x36\x34image\x18\x01 \x01(\t\x12\r\n\x05width\x18\x02 \x01(\x05\x12\x0e\n\x06height\x18\x03 \x01(\x05\":\n\x16\x43lassificationResponse\x12 \n\x08\x63\x61tegory\x18\x01 \x01(\x0e\x32\x0e.ImageCategory*%\n\rImageCategory\x12\x0b\n\x07NOT_CAT\x10\x00\x12\x07\n\x03\x43\x41T\x10\x01\x32@\n\x0e\x43lassification\x12.\n\x08\x43lassify\x12\t.B64Image\x1a\x17.ClassificationResponseb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'classification_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _IMAGECATEGORY._serialized_start=145
  _IMAGECATEGORY._serialized_end=182
  _B64IMAGE._serialized_start=24
  _B64IMAGE._serialized_end=83
  _CLASSIFICATIONRESPONSE._serialized_start=85
  _CLASSIFICATIONRESPONSE._serialized_end=143
  _CLASSIFICATION._serialized_start=184
  _CLASSIFICATION._serialized_end=248
# @@protoc_insertion_point(module_scope)