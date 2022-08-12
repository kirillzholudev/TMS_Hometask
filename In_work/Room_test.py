from math import ceil

sides = {"Length": 0,
         "Width": 0,
         "Height": 0}


class WinDoor:
    def __init__(self, x, y, name="unk"):
        self.x = x
        self.y = y
        self.name = name
        self.square = x * y

    def __repr__(self):
        return f'{self.name} {self.x}x{self.y}'


class Room:
    def __init__(self, x, y, z):
        self.square = 2 * z * (x + y)
        self.new_square = 0
        self.wd = []
        self.sides = sides
        self.x = x
        self.y = y
        self.z = z
        self.printSides()

    def printSides(self):
        sides['Length'] = self.x
        sides['Width'] = self.y
        sides['Height'] = self.z
        print('Room size:\n')
        for key, value in sides.items():
            print("{0}: {1}".format(key, value))

    def addWD(self, w, h, name='unk'):
        self.wd.append(WinDoor(w, h, name))

    def workSurface(self):
        self.new_square = self.square
        for i in self.wd:
            self.new_square -= i.square
        return self.new_square

    def wallpaper(self, dl, sh):  # Length and width of the roll
        roll_square = dl * sh
        total_roll = self.new_square / roll_square
        return f'You need {ceil(total_roll)} roll'


"""Program interface"""

print('Add the room parameters first')
ch1 = float(input("Length of room: "))
ch2 = float(input("Width of room: "))
ch3 = float(input("Height of room: "))
room_1 = Room(ch1, ch2, ch3)
print("Square of room: ", room_1.square)

while True:
    print("CHOICES:\n"
          "1. Add Windows or Doors\n"
          "2. Change sides of the room\n"
          "3. Calculate the amount of wallpaper")
    choice = input()

    if choice == '1':
        w = float(input("Width of door or window: "))
        h = float(input("Height of door or window: "))
        name = input("Name of door or window: ")
        room_1.addWD(w, h, name)
        print(room_1.wd)
        print('Work area: ', room_1.workSurface())
        continue

    if choice == '2':
        print("*** *** ***\n "
              "This part of the programme is still not working."
              "\n*** *** ***\n")
        continue

    if choice == '3':
        print('The area to wallpaper:', room_1.workSurface())
        dl = float(input('Roll length '))
        sh = float(input('Roll width '))
        print(room_1.wallpaper(dl, sh))
        break
    else:
        break