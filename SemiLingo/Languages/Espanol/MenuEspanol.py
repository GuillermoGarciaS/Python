import time

from SemiLingo.Languages.Espanol.Ingles.AIngles import TestIngles


class MenuEspanol:
    def __init__(self):
        self.menu_items = ["|1| Ingles", "|2| Nihongo", "|3| Latin"]

    def display_MenuEspanol(self):
        message = "¿Que idioma quieres aprender?: "
        for char in message:
            print(char, end='', flush=True)
            time.sleep(0.1)
        print()

        for item in self.menu_items:
            time.sleep(0.4)
            print(item)
            time.sleep(0.4)

    def get_choice(self):
        while True:
            try:
                user_choice = int(input())
                if 1 <= user_choice <= len(self.menu_items):
                    return user_choice
                else:

                    print("Opción inválida, favor de ingresar una opción válida")

            except ValueError:
                print("Favor de ingresar una opción válida")


if __name__ == '__main__':
    menuE = MenuEspanol()
    menuE.display_MenuEspanol()
    choice = menuE.get_choice()

    if choice == 1:
        LIngles = TestIngles()
        LIngles.display_optionsIngles()

    else:
        print("¿Qué haces aquí?")
