from collections import namedtuple
from flatdict import FlatDict
import json

def replacew(item):
    """
    Replace whitespace with dashes in keys and flatten nested dictionary.
    """
    return {k.replace(' ', '-'):replacew(v)
            if isinstance(v, dict)
            else v
            for k, v in item.items()}

class Bible(FlatDict):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._versions = set()
        self._books = set()
        self._chapters = set()
        self._verses = {} # a dictionary of bible verses
        # Key we can use to look up bible verses later on
        Key = namedtuple('Key', ['version', 'book', 'chapter', 'verse'])
        for key in self.keys():
                splitkey = key.split(':')
                if len(splitkey) > 3:
                    version, book, chapter, verse = splitkey
                    chapter = int(chapter)
                    verse = int(verse)
                    text = self[key]
                    chapter_nt = Bible.Chapter(book, chapter)
                    self._versions.add(version)
                    self._books.add(book)
                    self._chapters.add(chapter_nt)
                    self._verses[Key(version, book, chapter, verse)] = \
                        Bible.Verse(version, book, chapter, verse, text)

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

        i.e. bible.get_verse('Jeremiah', 51, 6) -> '"Flee from Babylon! Run for your lives! ...'
        """
        lookup = self._verses.get((version, book, chapter, verse))
        return lookup.text if lookup is not None else lookup


if __name__ == "__main__":
    versions = ('NIV', 'MSG', 'NLT')
    path = "./bibles/{version}/{version}.json"
    paths = [path.format(version=version) for version in versions]
    dictionary = {}
    for p, v in zip(paths, versions):
        with open(p) as foo:
            # remove whitespace from dictionary keys
            data = replacew(json.load(foo))
            # make the bible version the top-level key in the dictionary
            data = {v:data}
            dictionary.update(data)
    bible = Bible(dictionary)
    print(bible)
