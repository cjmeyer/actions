#! /usr/bin/env python

def setup(fn):
    return _with_setup(fn, lambda request: fn())

def teardown(fn):
    return _with_setup(fn, lambda request: request.addfinalizer(fn))

def _with_setup(fn, action):
    def funcarg(request):
        action(request)
        return request

    funcarg.__doc__ = fn.__doc__
    funcarg.__name__ = 'pytest_funcarg__{0}'.format(fn.__name__)
    
    module = __import__(fn.__module__)
    setattr(module, funcarg.__name__, funcarg)

    return funcarg

