"""
File Purpose: tools whose main purpose is to work with implementation details of Python.

E.g. manipulate function docstrings
"""
import inspect
import textwrap
import pydoc
import IPython  # for display

TAB = ' '*4

def format_docstring(*args__format, sub_indent=None, sub_ntab=None, **kw__format):
    '''returns a decorator of f which returns f, after updating f.__doc__ via f.__doc__.format(...)
    sub_indent: None or str
    if provided, indent all lines (after the first line) for each multiline string, before formatting.
    sub_ntab: int
    if provided when sub_indent is None, use sub_indent = sub_ntab * TAB
    '''
    if sub_indent is None and sub_ntab is not None:
        sub_indent = TAB * sub_ntab
    if sub_indent is not None:
        args__format = [str(arg).replace('\n', '\n'+sub_indent) for arg in args__format]
        kw__format = {key: str(val).replace('\n', '\n'+sub_indent) for key, val in kw__format.items()}
    def return_f_after_formatting_docstring(f):
        f.__doc__ = f.__doc__.format(*args__format, **kw__format)
        return f
    return return_f_after_formatting_docstring

def printsource(obj, *, module=True, as_str=False):
    '''prints source code for object (e.g. call this on a function or class).
    module: bool
    whether to also tell module & type info about this object.
    as_str: bool
    if True, return result as a string instead of printing it.
    '''
    result = ''
    if module:
        if inspect.ismodule(obj):
            topline = f'module {obj.__name__}'
        else:
            mod = inspect.getmodule(obj)
            if mod is None:
                raise TypeError(f'inspect.getmodule(obj) is None, for obj with type={type(obj)}')
            else:
                mod = mod.__name__
            topline = f'{type(obj).__name__} {obj.__name__!r} from module {mod}'
        buffer = '-' * len(topline)  # line like "--------" of length len(topline)
        result += '# ' + topline + '\n'
        result += '# ' + buffer + '\n'
    result += str(inspect.getsource(obj))
    if as_str:
        return result
    else:
        print(result)

_paramdocs_displaysource = {
    'module': '''bool
    whether to also tell module & type info about this object.''',
}

@format_docstring(**_paramdocs_displaysource)
def displaysource(obj, *, module=True):
    '''display sourcecode for obj, including syntax highlighting. See also: printsource.
    module: {module}
    '''
    source = printsource(obj, module=module, as_str=True)
    IPython.display.display(IPython.display.Code(source, language='python'))
