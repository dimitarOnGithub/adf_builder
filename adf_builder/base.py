from abc import ABC, abstractmethod


class ADFNode(ABC):

    @abstractmethod
    def to_dict(self):
        ...


class TopLevelNode(ADFNode, ABC):

    def __init__(self):
        self._content = []


class InlineNode(ADFNode, ABC):

    ...
