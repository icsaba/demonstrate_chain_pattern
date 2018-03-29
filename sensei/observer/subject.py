import abc


class Subject(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            raise Exception('Observer does not exist')

    def notify(self):
        for observer in self._observers:
            observer.update(self)
