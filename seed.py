try:
    from pathlib import Path
except ImportError:
    from pathlib2 import Path
from tqdm import tqdm
import django, os, sys, bibleparser

# configure django so as to be able to use the models api
bibler = Path('.', 'bibler')
sys.path.append(str(bibler))
os.environ['DJANGO_SETTINGS_MODULE'] = 'bibler.settings'
django.setup()

from bible_rest.models import BibleVerse

bibles_path = Path('.', 'bibles')
bible = bibleparser.Bible(path=bibles_path)

# tqdm will give us a progress bar for how quickly the database is seeded
for verse in tqdm(bible.verses):
    verse = verse._asdict()
    BibleVerse.objects.get_or_create(**verse)
    # bible_verse = BibleVerse(**verse)
    # bible_verse.save()
