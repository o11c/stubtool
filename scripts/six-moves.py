#!/usr/bin/env python

import os.path
import sys

dir = os.path.dirname(os.path.abspath(__file__))
if os.path.basename(dir) == 'scripts':
    dir = os.path.join(os.path.dirname(dir), 'src')
    sys.path.insert(0, dir)
del dir

from stubtool.main import main

if __name__ == '__main__':
    main([sys.argv[0], sys.argv[1], 'six.moves'])
