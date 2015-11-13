from __future__ import absolute_import

import zlib


Compress = type(zlib.compressobj())
Decompress = type(zlib.decompressobj())
