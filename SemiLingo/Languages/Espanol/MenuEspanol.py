import time


class MenuEspanol:
    def __init__(self):
        self.menu_items = ["|1| English", "|2| Nihongo", "|3| Latin"]

    def display_menu(self):
        message = "¿Que idioma quieres aprneder?:"
        for char in message:
            print(char, end='', flush=True)
            time.sleep(0.1)
        print()
