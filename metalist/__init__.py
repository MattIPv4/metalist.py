"""
 *  metalist.py: A simple API wrapper to post Discord bot stats to all known bot lists using metalist.xyz data.
 *  <https://github.com/MattIPv4/metalist.py/>
 *  Copyright (C) 2018 Matt Cowley (MattIPv4) (me@mattcowley.co.uk)
 *
 *  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
 *   documentation files (the "Software"), to deal in the Software without restriction, including without limitation
 *   the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and
 *   to permit persons to whom the Software is furnished to do so, subject to the following conditions:
 *
 *  The above copyright notice and this permission notice shall be included in all copies or substantial portions of
 *   the Software.
 *
 *  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
 *   THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 *   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
 *   CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
 *   IN THE SOFTWARE.
 *
 *   <https://github.com/MattIPv4/metalist.py/blob/master/LICENSE>
"""

__title__ = 'metalist.py'
__author__ = 'MattIPv4'
__license__ = 'MIT'
__copyright__ = 'Copyright 2018, MattIPv4'
__version__ = '1.0.2'

name = "metalist"

from collections import namedtuple

from .baseclient import BaseClient
from .client import Client
from .exceptions import *

VersionInfo = namedtuple('VersionInfo', 'major minor micro releaselevel serial')

version_info = VersionInfo(major=1, minor=0, micro=2, releaselevel='final', serial=0)

import warnings

warnings.warn("metalist.py has been deprecated, please consider using discordlists.py instead", DeprecationWarning)
