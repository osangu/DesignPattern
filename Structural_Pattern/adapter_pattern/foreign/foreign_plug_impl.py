from Structural_Pattern.adapter_pattern.foreign.foreign_plug import ForeignPlug


class ForeignPlugImpl(ForeignPlug):

    def plug_in(self):
        print('외국형 플러그를 꽂습니다')

    def plug_out(self):
        print('외국형 플러그를 뽑습니다')