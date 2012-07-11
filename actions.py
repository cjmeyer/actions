#! /usr/bin/env python


from path import path


class ActionContext(object):
    def __init__(self, srcpath=None, dstpath=None):
        self._srcpath = path(srcpath) if srcpath else path.getcwd()
        self._dstpath = path(dstpath) if dstpath else path.getcwd()

    @property
    def srcpath(self):
        return self._srcpath

    @property
    def dstpath(self):
        return self._dstpath

    def empty_file(self, dst):
        (self.dstpath / dst).touch()

