class Musicband:
    def __init__(self, name, date_of_birth):
        self._name = name
        self._birthday = date_of_birth
        self._albums = {}

    def add_album(self,album):
        self._albums[album.get_name()] = album

    def get_name(self):
        return self._name

    def get_albums(self):
        return self._albums.keys()

    def get_info(self, album=None):

        text = f'Name of a band: {self.get_name()},\nActing since {self.get_birthday()},\nAlbums:{self.get_albums()}'
        if album in self.get_albums():
            return self._albums[album].get_info
        return text

    def get_birthday(self):
        return self._birthday

class Album:
    def __init__(self, name, date, num_sales=0):
        self._name = name
        self._date = date
        self._sales = num_sales

    def update_sales(self, num_sales):
        self._sales = num_sales

    def get_name(self):
        return self._name

    def get_info(self):
        text = f'Album {self.get_name()},{self._date},{self._sales},sales'
        return text


if __name__ == '__main__':
    the_beatles = Musicband('The_beatles', 1960)
    # print(the_beatles.get_info())

    abbey_road = Album('Abbey_road', 1969, 19000000)
    the_beatles.add_album(abbey_road)

    # print(the_beatles.get_info())

    print(the_beatles.__dict__)
    print(the_beatles.__getitem__())
