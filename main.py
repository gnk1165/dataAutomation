# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

genreList = ["African", "Boomba", "K-pop", "J-pop", "Trot", "Experimental", "Lo-fi", "Harsh noise wall", "Blues",
             "Reggae", "Calypso", "Mambo", "Salsa", "Novelty Rock", "Country", "Folk", "Bluegrass", "Zydeco",
             "Elevator Music", "Ambient", "Crunk", "Disco", "New-age", "Eurobeat", "Drum and Bass", "Dubstep", "Techo",
             "Electronica", "Chiptune", "House", "Hip hop", "Jazz", "Boogie-woogie", "Samba", "Pop", "Soul", "Surf",
             "Teen pop", "Funk", "Doo Wop", "Beebop", "R&B", "Grunge", "Math Rock", "Paisley Underground",
             "Christian Rock", "Rap", "Garage", "Death Metal", "Heavy Metal", "Tuning Drone", "Rock", "Classic Rock",
             "Punk Rock", "Soft Rock", "Rock and Roll", "Swing"]


def makeGenre():
    pass


def getDate(album):
    pass


class song:
    def __init__(self, name, artist, album, length):
        self.name = name
        self.artist = artist
        self.album = album
        self.length = length
        self.genre = makeGenre()
        self.releaseDate = getDate(album)
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def read_csv(fName):
    f = open(fName)
    lines = f.readlines()
    f.close()

    for line in lines:
        line.split(",")
        album = line[2]
        artist = line[3]
        length = line[5]
        name = line[12]



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
