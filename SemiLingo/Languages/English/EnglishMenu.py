import time


class EnglishMenu:
    def __init__(self):
        self.menu_items = ["|1| Espanol", "|2| Nihongo", "|3| Latin"]

    def display_menu(self):
        message = "What language do you want to learn?:"
        for char in message:
            print(char, end='', flush=True)
            time.sleep(0.1)
        print()

    def get_choice(self):
        while True:
            try:
                user_choice = int(input())

                if 1 <= user_choice <= len(self.menu_items):
                    return user_choice
                else:
                    print("Opcion invalida, favor de ingresar una opcion valida")

            except ValueError:
                print("Favor de ingresar una opcion valida")


if __name__ == '__main__':
    menu = EnglishMenu()
    menu.display_menu()
    choice = menu.get_choice()

    if choice == 1:
        print("Ingles")
    else:
        print("Siquiera que haces aqui")