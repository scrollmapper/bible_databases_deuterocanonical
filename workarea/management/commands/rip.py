from django.core.management.base import BaseCommand, CommandError
#from books.models import Verse
import csv
import os
from pprint import pprint
from books.models import *
from django.template.defaultfilters import slugify

def make_verse(book, chapter, verse, text):
    
    
    v = Verse()
    v.book = book
    v.chapter = int(chapter)
    v.verse = int(verse)
    v.chapter_str = chapter
    v.verse_str = verse
    v.text = text
    v.save()
    print(v.book, v.chapter_str, v.verse_str, v.text)

class Command(BaseCommand):
    help = 'Commits a book from a text file properly formatted'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)

    def handle(self, *args, **options):
        path = os.path.join('tmp',"%s.csv"%options['path'])
                        
        if not os.path.exists(path):
            raise CommandError('"%s" does not exist' % path)
        
        key={}
        
        #get key
        reader = csv.reader(open('tmp/key_english.csv'))
        print(reader)
        for row in reader:
            if(row[0].isdigit()):
                key[row[0]] = row[1]
        
        
        
        #get bible verses
        reader = csv.reader(open(path))
                
        for row in reader:
            if(row[1].isdigit()):
                print(key[row[1]])
                
                book, created = Book.objects.get_or_create(slug=slugify(row[1]), name=row[1], canonical=True)
                
                make_verse(book, row[2], row[3], row[4])
