import time

class MenuEspañol:
    def __init__(self):
        self.menu_items = ["|1| English", "|2| 日本語", "|3| Latin"]

    def display_menu(self):
        message = "¿Que idioma quieres aprneder?:"
        for char in message:
            print(char, end = '', flush = True)
            time.sleep(0.1)
        print()