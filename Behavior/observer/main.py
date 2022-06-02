from Behavior.observer.observer.observer_abst import Watcher
from Behavior.observer.observer.observer_impl import Schrodinger
from Behavior.observer.source.subject import Box

if __name__ == '__main__':

    man1 = Schrodinger()
    man2 = Schrodinger()

    box = Box()

    box.enter_new_watcher(man1)
    box.enter_new_watcher(man2)
    box.open_box()

    box.leave_watcher(man1)
    box.open_box()