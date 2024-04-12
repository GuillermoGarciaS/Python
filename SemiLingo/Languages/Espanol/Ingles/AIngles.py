import time

class TestIngles:
    def __init__(self):
        self.menu_items = ["|1| Basico", "|2| Intermedio", "|3| Avanzado", "|4| Test de evaluacion"]

    def display_optionsIngles(self):
        message = "¿Por donde quisieras empezar?"
        for char in message:
            print(char, end='', flush=True)
            time.sleep(0.1)
        print()

    def get_options(self):
        while True:
            try:
                user_choice = int(input())

                if 1<= user_choice <= len(self.menu_items):
                    return user_choice
                else:
                    print("Opcion invalida, favor de ingresar una opcion valida")

            except ValueError:
                print("Favor de ingresar una opcion valida")


if __name__ == '__main__':
    test = TestIngles()
    test.display_options()
    choice = test.get_options()

    if choice == 1:
        print("principiante")
    elif choice == 2:
        print("intermedio")
    elif choice == 3:
        print("avanzado")
    else:
        print("Test de evaluacion")
