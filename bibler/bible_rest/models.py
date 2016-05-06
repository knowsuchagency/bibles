from django.db import models

# Create your models here.
class BibleVersion(models.Model):
    name = models.CharField(max_length=20, unique=True)


class BibleBook(models.Model):
    name = models.CharField(max_length=30, unique=True)
    version = models.ForeignKey(BibleVersion)


class BibleChapter(models.Model):

    # Since chapters don't need to be duplicated across different
    # books and versions, we make make a unique composite field
    # based on the chapter number and the book
    class Meta:
        unique_together = ('number', 'book')

    number = models.IntegerField()
    book = models.ForeignKey(BibleBook)


class BibleVerse(models.Model):
    bible_version = models.ForeignKey(BibleVersion)
    chapter = models.ForeignKey(BibleChapter)
    book = models.ForeignKey(BibleBook)
    text = models.CharField(max_length=500)
