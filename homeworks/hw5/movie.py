from typing import List


class Movie:
    def __init__(self, id, title, date, link, genre_binary: List):
        self.id = id
        self.date = date
        self.link = link
        self.title = title
        self.genre_binary = genre_binary
        self.genre_human_readable = []

