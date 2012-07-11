#! /usr/bin/env python


import actions
import os
import shutil
import tempfile


def test_action_context_should_default_dst_path_to_current_directory():
    assert actions.ActionContext().dstpath.abspath() == os.path.abspath(os.getcwd())

def test_action_context_should_initialize_relative_dst_path():
    assert actions.ActionContext(dstpath='path/to/dir').dstpath.abspath() == \
            os.path.join(os.getcwd(), 'path', 'to', 'dir')

def test_action_context_should_initialize_absolute_dst_path():
    assert actions.ActionContext(dstpath='/path/to/dir').dstpath.abspath() == \
            os.path.join('/', 'path', 'to', 'dir')

def test_action_context_should_default_src_path_to_current_directory():
    assert actions.ActionContext().srcpath.abspath() == os.path.abspath(os.getcwd())

def test_action_context_should_initialize_relative_src_path():
    assert actions.ActionContext(srcpath='path/to/dir').srcpath.abspath() == \
            os.path.join(os.getcwd(), 'path', 'to', 'dir')

def test_action_context_should_initialize_absolute_src_path():
    assert actions.ActionContext(srcpath='/path/to/dir').srcpath.abspath() == \
            os.path.join('/', 'path', 'to', 'dir')


def pytest_funcarg__dstdir(request):
    dstdir = tempfile.mkdtemp()
    def teardown():
        shutil.rmtree(dstdir)
    request.addfinalizer(teardown)
    return dstdir

def pytest_funcarg__context(request):
    return actions.ActionContext(dstpath=request.getfuncargvalue('dstdir'))


def test_action_context_should_create_file_when_invoked(context, dstdir):
    context.empty_file('empty_file.txt')
    assert os.path.isfile(os.path.join(dstdir, 'empty_file.txt'))

def test_action_context_should_remove_file_when_revoked(context):
    pass

def test_action_context_should_pretend_to_create_file_when_invoked(context):
    pass

def test_action_context_should_pretend_to_remove_file_when_revoked(context):
    pass

