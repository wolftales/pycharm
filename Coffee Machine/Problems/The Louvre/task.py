class Painting:
    museum = 'the Louvre'

    def __init__(self, title, artist, creation_date):
        self.title = title
        self.artist = artist
        self.creation_date = creation_date

    def print(self):
        print(f'"{self.title}" by {self.artist} ({self.creation_date}) hangs in {Painting.museum}.')


title = input()
artist = input()
creation_date = int(input())

mona = Painting(title, artist, creation_date)
mona.print()
