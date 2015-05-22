# -*- coding: utf-8 -*-
class Env(object):
    def __init__(self, parent=None):
        self.tbl = {}
        self.parent = parent

    def get(self, name):
        ret = self.tbl(name, None)
        if ret is None:
            if self.parent is None:
                return None
            else:
                return self.parent.get(name)
        else:
            return ret

    def put(self, name):
        self.tbl[name] = True

    def exists(self, name):
        return self.get(name) is True

    def exists_local(self, name):
        return name in self.tbl
