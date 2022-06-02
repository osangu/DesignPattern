from abc import ABC, abstractmethod


class Watcher(ABC):

    @abstractmethod
    def notice(self, is_cat_die): pass
