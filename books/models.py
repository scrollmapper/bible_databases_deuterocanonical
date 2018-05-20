from django.db import models

# Create your models here.

from django.db import models

class Book(models.Model):
    slug = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=30)
    canonical = models.BooleanField(default=False)
    def __str__(self):
        return self.slug
       
class Verse(models.Model):
    position = models.AutoField(primary_key=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    chapter = models.IntegerField()
    verse = models.IntegerField()
    chapter_str = models.CharField(max_length=30)
    verse_str = models.CharField(max_length=30)
    text = models.TextField()
    def __str__(self):
        return "#%s %s %s %s"%(str(self.position), self.chapter_str, self.verse_str, self.text)
