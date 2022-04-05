from ..foreign.foreign_plug import ForeignPlug

from ..basic.korea_plug import KoreaPlug


class KoreaPlugAdapter(ForeignPlug):

    def __init__(self, korea_plug: KoreaPlug):
        self.__korea_plug = korea_plug

    def plug_in(self):
        print('어댑터를 사용해서')
        self.__korea_plug.stick()

    def plug_out(self):
        print('어댑터를 사용해서')
        self.__korea_plug.pull_out()
