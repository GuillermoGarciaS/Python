class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, data):
        self.data = data

    def setNext(self, next):
        self.next = next

    def __str__(self):
        return str(self.data)

soda = Node("Ayato")
game = Node("Fallout")
album = Node("For You")

soda.setNext(game)
game.setNext(album)

print(soda.getNext())
print(game.getNext())