from smqtk.tests.utils.test_plugin_get import DummyInterface


__author__ = 'paul.tunison@kitware.com'


class ImplFoo (DummyInterface):

    @classmethod
    def is_usable(cls):
        return True

    def inst_method(self, val):
        return 'foo'+str(val)


class ImplBar (DummyInterface):

    @classmethod
    def is_usable(cls):
        return True

    def inst_method(self, val):
        return 'bar'+str(val)


class ImplNotUsable (DummyInterface):

    @classmethod
    def is_usable(cls):
        return False

    def inst_method(self, val):
        return 'notUsable'+str(val)


class SomethingElse (list):
    pass
