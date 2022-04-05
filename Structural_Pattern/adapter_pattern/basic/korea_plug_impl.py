from Structural_Pattern.adapter_pattern.basic.korea_plug import KoreaPlug


class KoreaPlugImpl(KoreaPlug):

    def stick(self):
        print('한국형 플러그를 콘선트에 꽂습니다.\n\n')

    def pull_out(self):
        print('한국형 플러그를 뽑습니다.\n\n')
