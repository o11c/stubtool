from __future__ import absolute_import

import os
import ossaudiodev


oss_audio_device = type(ossaudiodev.open('r'))
oss_mixer_device = type(ossaudiodev.openmixer(os.devnull))
