from typing import List

from project.album import Album


class Band:
    def __init__(self, name):
        self.name = name
        self.albums: List[Album] = []

    def add_album(self, album: Album):
        if album not in self.albums:
            self.albums.append(album)
            return f"Band {self.name} has added their newest album {album.name}."
        return f"Band {self.name} already has {album.name} in their library."

    def remove_album(self, album_name: str):
        try:
            album = next((a for a in self.albums if a.name == album_name))
            if not album.published:
                self.albums.remove(album)
                return f"Album {album.name} has been removed."
            return f'Album has been published. It cannot be removed.'

        except StopIteration:
            return f"Album {album_name} is not found."

    def details(self):
        result = [f"Band {self.name}", '\n'.join(a.details() for a in self.albums)]
        return '\n'.join(result)