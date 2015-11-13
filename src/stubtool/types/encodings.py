from __future__ import absolute_import

import encodings.big5
import encodings.cp037


EncodingMap = type(encodings.cp037.encoding_table)
MultibyteCodec = type(encodings.big5.codec)
