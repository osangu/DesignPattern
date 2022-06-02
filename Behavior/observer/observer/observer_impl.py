from .observer_abst import Watcher


class Schrodinger(Watcher):

    def notice(self, is_cat_die):
        if is_cat_die == 'die':
            print('결국 이렇게 됬구먼!!!')
        else:
            print('다행이야!')
