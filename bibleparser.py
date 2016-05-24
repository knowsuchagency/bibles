from __future__ import print_function
from collections import namedtuple
from flatdict import FlatDict
try:
    from pathlib import Path
except ImportError:
    from pathlib2 import Path

import json

def replacew(item):
    """
    Replace whitespace with dashes in keys and flatten nested dictionary.
    """
    return {k.replace(' ', '-'): replacew(v)
    if isinstance(v, dict)
    else v
            for k, v in item.items()}


class Bible(FlatDict):
    def __init__(self, path=__file__):
        """Initialize a Bible object from a filepath. Assume module is adjacent to bibles filepath.

        example:
        root/
            bibleparser.py
            bibles/
                ESV/
                    ESV.json
                MSG/
                ...
        """
        if path.endswith('bibleparser.py'):
            bibles_path = Path(__file__).parent.joinpath('bibles')
        else:
            bibles_path = Path(path)
        bible_paths = list(bibles_path.rglob("*.json"))
        dictionary = {}
        for path in bible_paths:
            with path.open() as foo:
                # remove whitespace from dictionary keys
                data = replacew(json.load(foo))
                # make the bible version the top-level key in the dictionary
                data = {path.stem: data}
                dictionary.update(data)

        # Use the FlatDict initializer to populate our dictionary
        super(Bible, self).__init__(dictionary)
        self._versions = set()
        self._books = set()
        self._chapters = set()
        self._verses = {}  # a dictionary of bible verses
        # The key for our Bible._verses dictionary
        Key = namedtuple('Key', ['version', 'book', 'chapter', 'verse'])
        for key in self.keys():
            splitkey = key.split(':')
            if len(splitkey) > 3:
                version, book, chapter, verse = splitkey
                chapter = int(chapter)
                verse = int(verse)
                # A few verses have no text, so we replace them with empty strings
                text = self[key] or ''
                self._versions.add(version)
                self._books.add(book)
                self._chapters.add(Bible.Chapter(book, chapter))
                self._verses[Key(version, book, chapter, verse)] = Bible.Verse(version, book, chapter, verse, text)

    Chapter = namedtuple('Chapter', ['book', 'chapter'])
    Verse = namedtuple('Verse', ['version', 'book', 'chapter', 'verse', 'text'])

    @property
    def versions(self):
        """
        Return a list of bible versions.
        """
        return list(self._versions)

    @property
    def books(self):
        """
        Return a list of books.
        """
        return list(self._books)

    @property
    def verses(self):
        """
        :return: List of all verses for each bible version
        """
        return list(verse for verse in self._verses.values())

    @property
    def chapters(self):
        """
        Return a list of chapter namedtuples, each with 'book' and 'chapter' fields.
        """
        return list(self._chapters)

    def __repr__(self):
        return "Bible(versions={versions})".format(versions=self.versions)

    def __str__(self):
        return self.__repr__()

    def get_verse(self, book, chapter, verse, version='NIV'):
        """
        Return the text for a verse based on the bible version, book, chapter, and verse number.
        The version will default to the new international version if not specified.
        If no verse is found, return None

        i.e. bible.get_verse('Jeremiah', 51, 6) -> '"Flee from Babylon! Run for your lives! ...'
        """
        lookup = self._verses.get((version, book, chapter, verse))
        return lookup.text if lookup is not None else lookup


if __name__ == "__main__":
    bible = Bible()
    print(bible)
