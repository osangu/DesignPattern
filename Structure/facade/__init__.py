from notebook import NoteBook
from notebook_facade import NoteBookFacade

if __name__ == '__main__':

    notebook = NoteBookFacade(NoteBook())

    notebook.turn_on()

    notebook.turn_off()

    notebook.coding()

    notebook.see_lesson()