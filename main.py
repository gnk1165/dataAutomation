import random
import csv
from datetime import datetime, timedelta

genreList = ["African", "Boomba", "K-pop", "J-pop", "Trot", "Experimental", "Lo-fi", "Harsh noise wall", "Blues",
             "Reggae", "Calypso", "Mambo", "Salsa", "Novelty Rock", "Country", "Folk", "Bluegrass", "Zydeco",
             "Elevator Music", "Ambient", "Crunk", "Disco", "New-age", "Eurobeat", "Drum and Bass", "Dubstep", "Techo",
             "Electronica", "Chiptune", "House", "Hip hop", "Jazz", "Boogie-woogie", "Samba", "Soul", "Surf",
             "Teen pop", "Funk", "Doo Wop", "Beebop", "R&B", "Grunge", "Math Rock", "Paisley Underground",
             "Christian Rock", "Rap", "Garage", "Death Metal", "Heavy Metal", "Tuning Drone", "Classic Rock",
             "Punk Rock", "Soft Rock", "Rock and Roll", "Swing"]

all_albums_data, album_csv, album_belongs_to_csv, genre_csv = [], [], [], []
album_includes, created_by = [], []
song_belongs_to, artists, songs, albums, albumNames = [], [], [], [], []


# generate a datetime in format yyyy-mm-dd
def gen_datetime(min_year=1990, max_year=2020):
    start = datetime(min_year, 1, 1, 00, 00, 00)
    years = max_year - min_year + 1
    end = start + timedelta(days=365 * years)
    date = start + (end - start) * random.random()
    date = str(date).split()
    return date[0]


def gen_genre():
    return random.randint(0, 56)


def getGenre(album):
    g = album.genre
    if random.random() < 0.10:
        return gen_genre()
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
        self.genre = gen_genre()
        self.releaseDate = gen_datetime()
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


# generates album.csv
def gen_album_csv(alb):
    album1 = album(alb)
    all_albums_data.append(album1)

    a1 = [album1.releaseDate, album1.name]
    for an_list in album_csv:
        if a1[1] in an_list:
            break
    else:
        album_csv.append(a1)

    file = open('album.csv', "w+")
    file.close()
    file = open('album.csv', 'a+', newline='')
    with file:
        write = csv.writer(file)
        write.writerows(album_csv)
    file.close()


# generates album_belongs_to.csv
def gen_album_belongs_to_csv():
    temp_list = []
    for element in all_albums_data:
        album_id = all_albums_data.index(element)
        genre_id = element.genre
        a_list = [album_id, genre_id]
        temp_list.append(a_list)

    for x in temp_list:
        if x not in album_belongs_to_csv:
            album_belongs_to_csv.append(x)

    file = open('album_belongs_to.csv', "w+")
    file.close()
    file = open('album_belongs_to.csv', 'a+', newline='')
    with file:
        write = csv.writer(file)
        write.writerows(album_belongs_to_csv)
    file.close()


def gen_genre_csv():
    for x in genreList:
        id = genreList.index(x)
        genre_csv.append([x, id + 4])

    file = open('genre.csv', "w+")
    file.close()
    file = open('genre.csv', 'a+', newline='')
    with file:
        write = csv.writer(file)
        write.writerows(genre_csv)
    file.close()


def gen_song_belongs_to():
    x = range(1, 605)
    for n in x:
        sbt = [n, random.randint(1, 58)]
        song_belongs_to.append(sbt)

    file = open('song_belongs_to.csv', "w+")
    file.close()
    file = open('song_belongs_to.csv', 'a+', newline='')
    with file:
        write = csv.writer(file)
        write.writerows(song_belongs_to)
    file.close()


def gen_artist(fName):
    with open(fName, encoding="utf8") as csv_file:
        an_list = []

        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            elif len(artists) < 100:
                artist = row[3]
                if artist not in an_list:
                    an_list.append(artist)
                    artists.append([artist])

        print(artists)
        print(len(artists))

        file = open('artist.csv', "w+")
        file.close()
        file = open('artist.csv', 'a+', newline='')
        with file:
            write = csv.writer(file)
            write.writerows(artists)
        file.close()


def gen_songs_and_artist(fName):
    with open(fName, encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count +=1
            elif line_count < 600:
                alb = row[2]
                artist = row[3]
                name = row[12]
                release_date = gen_datetime()

                minutes = int(float(row[5])) / 60000
                seconds = int(float(row[5])) / 1000

                delta = timedelta(
                    minutes=minutes,
                    seconds=seconds
                )

                s1 = [release_date, name, delta, 0]
                songs.append(s1)
                line_count += 1
            else:
                break

        file = open('songs.csv', "w+")
        file.close()
        file = open('songs.csv', 'a+', newline='')
        with file:
            write = csv.writer(file)
            write.writerows(songs)
        file.close()


def gen_created_by():
    used_artist = []
    artist_range = range(1, 111)
    album_range = range(3, 258, 1)

    for x in artist_range:
        used_artist.append(int(x))

    for n in album_range:
        alb_id = random.randint(1, len(used_artist))
        used_artist.index(alb_id)
        a_id = [n, alb_id]
        created_by.append(a_id)

    file = open('created_by.csv', "w+")
    file.close()
    file = open('created_by.csv', 'a+', newline='')
    with file:
        write = csv.writer(file)
        write.writerows(created_by)
    file.close()


def gen_album_includes():
    used_alb = []
    alb_range = range(1, 257)
    song_range = range(7, 606, 1)

    for x in alb_range:
        used_alb.append(int(x))

    for n in song_range:
        alb_id = random.randint(1, len(used_alb))
        used_alb.index(alb_id)
        a_id = [n, alb_id]
        album_includes.append(a_id)

    file = open('album_includes.csv', "w+")
    file.close()
    file = open('album_includes.csv', 'a+', newline='')
    with file:
        write = csv.writer(file)
        write.writerows(album_includes)
    file.close()


def gen_csv(fName):
    gen_songs_and_artist(fName)
    gen_artist(fName)
    gen_song_belongs_to()
    album_belongs_to()
    gen_album_includes()
    gen_created_by()


def album_belongs_to():
    an_list = []
    i = 1
    while i != 258:
        genre_id = random.randint(1, 57)
        an_list.append([i, genre_id])
        i += 1

    file = open('album_belongs_to.csv', "w+")
    file.close()
    file = open('album_belongs_to.csv', 'a+', newline='')
    with file:
        write = csv.writer(file)
        write.writerows(an_list)
    file.close()


if __name__ == '__main__':
    gen_csv('songAttributes_1999-2019.csv')
