from collections import namedtuple
from flatdict import FlatDict
import json

class Bible(namedtuple('Bible', ['version', 'path', 'content'])):
    def __new__(cls, *args, **kwargs):
        kwargs.setdefault('content', '')
        return super(Bible, cls).__new__(cls, *args, **kwargs)

    def __repr__(self):
        d = dict(v=self.version, p=self.path, c=type(self.content))
        return 'Bible(version={v}, path={p}, content={c})'.format(**d)

def replacew(d):
    """Remove whitespace from dictionary keys"""
    return   {k.replace(' ', '-'):replacew(v)
             if isinstance(v, dict)
             else v
             for k, v in d.items()}



if __name__ == "__main__":
    versions = ('NIV', 'MSG', 'NLT')
    path = "./{version}/{version}.json"
    version_path = {v: path.format(version=v) for v in versions}
    bibles = [Bible(v, p) for v, p in zip(versions, (path.format(version=s) for s in versions))]

    _bibles = bibles.copy()
    bibles = []
    for bible in _bibles:
        with open(bible.path) as foo:
            content = FlatDict(replacew(json.load(foo)))
            # content = replacew(content)
            b = bible._replace(content=content)
            bibles.append(b)
    print(bibles)
