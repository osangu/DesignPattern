from ..observer.observer_abst import Watcher

from random import randint

class Box:
    def __init__(self):
        self.croud = []

    def new_watcher(self, watcher: Watcher):
        self.croud.append(watcher)

    def watcher_leave_croud(self, watcher: Watcher):
        self.croud.pop(
            self.croud.index(watcher)
        )

    def look(self, is_cat_die):
        for i in self.croud: i.notice(is_cat_die)

    def open_box(self):
        die_or_live = randint(0, 1)
        if die_or_live:
            self.look('live')
        else:
            self.look('die')
