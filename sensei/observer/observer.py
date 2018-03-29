import abc


class Observer(object):
    __metaclass__ = abc.ABCMeta

    def update(self, subject):
        raise NotImplementedError()
