import time

class Menu:
    def __init__(self):
        self.menu_items = ["|1| Español", "|2| English", "|3| 日本語", "|4| Latin"]

    def display_menu(self):
        message = "Chose a language..."
        for char in message:
            print(char, end = '', flush = True)
            time.sleep(0.1)
        print()

        for item in self.menu_items:
            time.sleep(0.5)
            print(item)
            time.sleep(0.5)

    def get_choice(self):
        while True:
            try:
                choice = int(input())
                if 1 <= choice <= len(self.menu_items):
                    return choice
                else:
                    print("Invalid choice, please choose a valid language by selecting a numbet between 1 and ", len(self.menu_items))
                
            except ValueError:
                print("Invalid input. please enter a number.")
if __name__ == "__main__":
    menu = Menu()
    menu.display_menu()
    choice = menu.get_choice()
    