from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class BibleVerse(models.Model):
    version = models.CharField(max_length=20)
    book = models.CharField(max_length=20)
    chapter = models.IntegerField()
    verse = models.IntegerField()
    text = models.TextField()

    class Meta:
        unique_together = (('version', 'book', 'chapter', 'verse'),)

    def __str__(self):
        return "{}:{}:{} {}".format(*map(str, (self.book, self.chapter, self.verse, self.version)))
