try:
    from pathlib import Path
except ImportError:
    from pathlib2 import Path
from tqdm import tqdm
import django, os, bibleparser

# configure django so as to be able to use the models api
os.environ['DJANGO_SETTINGS_MODULE'] = 'bibler.settings'
django.setup()

from bible_rest.models import BibleVerse

bibles_path = Path('.', 'bibles')
bible = bibleparser.Bible(path=bibles_path)

virgin_db = BibleVerse.objects.count() == 0

# tqdm will give us a progress bar for how quickly the database is seeded
for verse in tqdm(bible.verses):
    verse = verse._asdict()

    # either populate the database for the first time or update it
    if virgin_db:
        BibleVerse(**verse).save()
    else:
        BibleVerse.objects.get_or_create(**verse)

