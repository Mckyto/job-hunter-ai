from abc import ABC, abstractmethod


class BaseSearcher(ABC):

    @abstractmethod
    def search(self):
        """
        Returnează o listă de obiecte Job.
        """
        pass