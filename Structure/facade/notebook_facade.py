from notebook import NoteBook


class NoteBookFacade:

    def __init__(self, notebook: NoteBook):
        self.__notebook = notebook

    def coding(self): self.__notebook.coding()

    def turn_on(self): self.__notebook.turn_on()

    def turn_off(self): self.__notebook.turn_off()

    def see_lesson(self): self.__notebook.see_lesson()