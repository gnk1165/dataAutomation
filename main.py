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


def addAlbum(albumName, artist):
    if albumName in albumNames:
        albId = albumNames.index(albumName)
    else:
        albumNames.append(album)
        albums.append(album(albumName))
        albId = len(albumNames) - 1
    albums[albId].addArtist(artists.index(artist))
    albums[albId].addSong(len(songs))
    return albId


def read_csv(fName):
    # THIS NEEDS TO READ CSV
    f = open(fName, "r")
    lines = f.readlines()
    f.close()

    # Theoretically this still works, I don't know how csv do
    lines = lines[1:]
    for line in lines:
        line.split(",")
        alb = line[2]
        artist = line[3]
        length = line[5]
        name = line[12]
        albId = addAlbum(alb, artist)
        artId = addArtist(artist)
        songs.append(song(name, artId, albId, length))

    fSong = open("songs.csv", "w")
    for s in range(len(songs)):
        fSong.write((str(s) + "," + songs[s].string()))
    fSong.close()
    fAlbum = open("album.csv", "w")
    for a in range(len(albums)):
        fAlbum.write((str(a)) + "," + albums[a].string())
    fAlbum.close()
    fArtist = open("artist.csv", "w")
    for a in range(len(artists)):
        fArtist.write((str(a)) + "," + artist[a])
    fArtist.close()
    fGenre = open("genre.csv", "w")
    for g in range(len(genreList)):
        fGenre.write((str(g)) + "," + genreList[g])
    fArtist.close()
    fAlbmArt = open("AlbmArt.csv", "w")
    for al in range(len(albums)):
        aList = albums[al].artists
        for ar in range(aList):
            fAlbmArt.write(str(al) + "," + str(ar))
    fAlbmArt.close()
    fAlbmGnr = open("AlbmGnr.csv", "w")
    for al in range(len(albums)):
        fAlbmGnr.write(str(al) + "," + str(albums[al].genre))
    fAlbmGnr.close()
    fAlbmSng = open("AlbmSng.csv", "w")
    for al in range(len(albums)):
        sList = albums[al].songs
        for s in range(sList):
            fAlbmSng.write(str(al) + "," + str(s) + "," + str(sList[s]))
    fAlbmSng.close()
    fGnrSng = open("GnrSng.csv", "w")
    for s in range(len(songs)):
        fGnrSng.write(str(songs[s].genre) + "," + str(s))
    fGnrSng.close()
    fArtSng = open("ArtSng.csv", "w")
    for s in range(len(songs)):
        fArtSng.write(str(songs[s].artist) + "," + str(s))
    fGnrSng.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    read_csv("songAttributes_1999-2019.csv")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
