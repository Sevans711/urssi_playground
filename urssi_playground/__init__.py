"""Playing around with stuff from URSSI tutorial, e.g. PyPI

This package has a multiline docstring, here is one of the lines,
here is another line. What happens to the extra lines from flit/hatch?
"""

x = 7
y = 'hello world'

__version__ = "2024.09.0"   # YYYY.0M.MICRO   # formatted like xarray versions.

from . import tools
from . import underground


def func_from_playground_init():
    '''wow this is a cool function huh!'''
    print('hello from playground init!')


from .underground import wet_dirt