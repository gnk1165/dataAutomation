# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
from datetime import datetime, timedelta


genreList = {"African", "Boomba", "K-pop", "J-pop", "Trot", "Experimental", "Lo-fi", "Harsh noise wall", "Blues",
              "Reggae", "Calypso", "Mambo", "Salsa", "Novelty Rock", "Country", "Folk", "Bluegrass", "Zydeco",
              "Elevator Music", "Ambient", "Crunk", "Disco", "New-age", "Eurobeat", "Drum and Bass", "Dubstep", "Techo",
              "Electronica", "Chiptune", "House", "Hip hop", "Jazz", "Boogie-woogie", "Samba", "Pop", "Soul", "Surf",
              "Teen pop", "Funk", "Doo Wop", "Beebop", "R&B", "Grunge", "Math Rock", "Paisley Underground",
              "Christian Rock", "Rap", "Garage", "Death Metal", "Heavy Metal", "Tuning Drone", "Rock", "Classic Rock",
              "Punk Rock", "Soft Rock", "Rock and Roll", "Swing"}

albums = []
albumNames = []
artists = []
songs = []


def gen_datetime(min_year=1990, max_year=2020):
    # generate a datetime in format yyyy-mm-dd
    start = datetime(min_year, 1, 1, 00, 00, 00)
    years = max_year - min_year + 1
    end = start + timedelta(days=365 * years)
    date = start + (end - start) * random.random()
    date = str(date).split()
    return date[0]


def makeGenre():
    return random.randint(0, len(genreList))


def getGenre(album):
    g = album.genre
    if random.random() < 0.10:
        return makeGenre()
    return g


class song:
    def __init__(self, name, artist, album, length):
        self.name = name
        self.artist = artist
        self.album = album
        self.length = length
        self.genre = getGenre(album)
        self.releaseDate = album.releaseDate

    def string(self):
         return str(self.name) + "," + str(self.length) + "," + str(self.releaseDate)


class album:
    def __init__(self, name):
        self.name = name
        self.genre = makeGenre()
        self.releaseDate = gen_datetime(name)
        self.artists = []
        self.songs = []

    def addArtist(self, artist):
        if artist in self.artists:
            return
        self.artists.append(artist)

    def addSong(self, sng):
        self.songs.append(sng)

    def string(self):
        return str(self.name) + "," + str(self.releaseDate)



def addArtist(artist):
    if artist in artists:
        return artists.index(artist)
    artists.append(artist)
    return artists.index(artist)


def addAlbum(album, artist, name):
    if album in albumNames:
        return artists.index(artist)
    artists.append(artist)
    return artists.index(artist)


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
        albId = addAlbum(album, artist, name)
        artId = addArtist(artist)
        songs.append(song(name, artId, albId, length))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    gen_datetime()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
