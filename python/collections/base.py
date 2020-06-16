import abc


class PriorityQueue(abc.ABC):

    def __init__(self, asc=True):
        self.asc = asc

    @abc.abstractmethod
    def push(self, x):
        raise NotImplementedError

    @abc.abstractmethod
    def pop(self):
        raise NotImplementedError

    @abc.abstractmethod
    def top(self):
        raise NotImplementedError

    @abc.abstractmethod
    def __len__(self):
        raise NotImplementedError
