from abc import ABC, abstractmethod


class BaseSearcher(ABC):

    @abstractmethod
    def search(self):
        pass