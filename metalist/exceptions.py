"""
 *  metalist.py: A simple API wrapper to post Discord bot stats to all known bot lists using themetalist.org data.
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


class MetalistException(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class RequestFailure(MetalistException):
    def __init__(self, status: int, response: str):
        super().__init__("{}: {}".format(status, response))


class Ratelimited(MetalistException):
    def __init__(self, json=None):
        super().__init__("The request to the API endpoint was ratelimited."
                         "\nMore data may be available in the 'ratelimit' attribute.")
        self.ratelimit = json


class EmptyResponse(MetalistException):
    def __init__(self):
        super().__init__("No response was received from the API")
