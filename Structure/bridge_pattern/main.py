from Structure.bridge_pattern.platoon.solder_impl import SolderAmuge

from Structure.bridge_pattern.platoon.platoon_commander import PlatoonCommander

if __name__ == '__main__':

    solder = SolderAmuge()

    solder.fight()

    solder.make_encampment()

    platoon_commander = PlatoonCommander(SolderAmuge())

    platoon_commander.check_people()

    platoon_commander.command_fight()

    platoon_commander.command_make_encampment()