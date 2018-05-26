from django.core.management.base import BaseCommand, CommandError
#from books.models import Verse

import os
import re
from books.models import *

def make_verse(book, verse):
    verse_num = re.findall(r'\[\d+[A-z]?:\d+[A-z]?\]?.', verse);
    verse = verse.replace(verse_num[0], '')
    
    chapter_verse = [v.strip() for v in verse_num[0].replace('[', '').replace(']','').split(':')]
    
    v = Verse()
    v.book = book
    v.chapter = int(re.sub('[^0-9]','', chapter_verse[0]))
    v.verse = int(re.sub('[^0-9]','', chapter_verse[1]))
    v.chapter_str = chapter_verse[0]
    v.verse_str = chapter_verse[1]
    v.text = verse
    v.save()
    print("\n\n")
    print(v.book, v.chapter_str, v.verse_str, v.text)

class Command(BaseCommand):
    help = 'Commits a book from a text file properly formatted'

    def add_arguments(self, parser):
        parser.add_argument('--book', type=str)

    def handle(self, *args, **options):
        book = os.path.join('book_sources',options['book'],"%s.txt"%options['book'])
        
        if not os.path.exists(book):
            raise CommandError('"%s" does not exist' % book)
                
        f = open(book, 'r')
        text = f.read()
    
        book, created = Book.objects.get_or_create(slug=options['book'])
        
        Verse.objects.filter(book=book).delete()
        
        verses = re.findall("\[\d+[A-z]?:\d+[A-z]?\][\s\S]*?(?=\[\d+[A-z]?:\d+[A-z]?\]|$)", text)
                
        for v in verses:
            make_verse(book, v)
        
        '''
        for poll_id in options['poll_id']:
            try:
                poll = Poll.objects.get(pk=poll_id)
            except Poll.DoesNotExist:
                raise CommandError('Poll "%s" does not exist' % poll_id)

            poll.opened = False
            poll.save()

            self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % poll_id))
        '''
        
