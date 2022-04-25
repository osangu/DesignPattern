
from ..animal.impl.baby_cow import BabyCow
from ..animal.impl.baby_pig import BabyPig
from ..animal.impl.baby_dock import BabyDock
from ..farm.farm import Farm


class MyFarm(Farm):

    def new_pig(self) -> BabyPig: return BabyPig('꿀꿀이')

    def new_dock(self) -> BabyDock: return BabyDock('꼬ㅒ꼬ㅒㄲ이')

    def new_cow(self) -> BabyCow: return BabyCow('흑우')
