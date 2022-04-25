from abc import ABC, abstractmethod

from ..animal.impl.baby_cow import BabyCow
from ..animal.impl.baby_pig import BabyPig
from ..animal.impl.baby_dock import BabyDock


class Farm(ABC):

    @abstractmethod
    def new_pig(self) -> BabyPig: pass

    @abstractmethod
    def new_dock(self) -> BabyDock: pass

    @abstractmethod
    def new_cow(self) -> BabyCow: pass
