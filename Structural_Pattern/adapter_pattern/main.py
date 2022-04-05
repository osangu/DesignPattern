from Structural_Pattern.adapter_pattern.basic.korea_plug_impl import KoreaPlugImpl

from Structural_Pattern.adapter_pattern.adapter.korea_plug_adapter import KoreaPlugAdapter

if __name__ == '__main__':

    plug_by_adapter = KoreaPlugAdapter(KoreaPlugImpl())

    plug_by_adapter.plug_in()

    plug_by_adapter.plug_out()
