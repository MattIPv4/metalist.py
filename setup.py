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

import re

from setuptools import setup

with open("requirements.txt", "r") as f:
    requirements = f.readlines()

with open("README.md", "r") as f:
    readme = f.read()

with open("metalist/__init__.py", "r") as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('version is not set')

setup(
    name="metalist.py",
    author="MattIPv4",
    url="https://github.com/MattIPv4/metalist.py/",
    version=version,
    packages=['metalist'],
    python_requires=">= 3.5",
    include_package_data=True,
    install_requires=requirements,
    description='A simple API wrapper to post Discord bot stats to all known bot lists using metalist.xyz data.',
    long_description=readme,
    long_description_content_type="text/markdown",
    keywords="api wrapper discord bot bots stats statistics meta list metalist botlist",
    classifiers=(
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Natural Language :: English",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
    ),
    project_urls={
        'Funding': 'http://patreon.mattcowley.co.uk/',
        'Support': 'http://discord.mattcowley.co.uk/',
        'Source': 'https://github.com/MattIPv4/metalist.py/',
    },
)

# How2Ship:tm:
# 1. Update version in metalist/__init__.py
# 2. Run python3 setup.py sdist bdist_wheel bdist_egg
# 3. Run python3 -m twine upload dist/*
