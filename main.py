#!/usr/bin/env python
# coding: utf-8

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""Created on Jul 2021.
@author: Wanderson Neto
"""

import sys
from pathlib import Path
import warnings

warnings.filterwarnings("ignore")

sys.path.append('def')
sys.path.append('config')

import menuInicial

if __name__ == "__main__":
    menuInicial.inicio()
    