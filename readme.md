# Scrollmapper :: Deuterocanonical Project

[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=W8RKPHPUF398G)

Based on the Scrollmapper bible databases: https://github.com/scrollmapper/bible_databases

This is a Python / Django project for committing Deuterocanonical the books to database for study and research. 

Deuterocanonical books included thus far:
- 1st Enoch ("Ethiopic" Book of Enoch)
- 2nd Enoch ("Slavonic" "Secrets of Enoch")
- 3nd Enoch ("Hebrew" Book of Enoch)
- 2nd Esdras (also called 4 Esdras, Latin Esdras, or Latin Ezra)
- 1st and 2nd Book of Adam and Eve
- Jashar
- Jubilees
- Tobit
- Judith
- Esther (Greek)
- Wisdom
- Ecclesiasticus
- Baruch
- Song of Three
- Susanna
- Bel and the Dragon
- 1 Maccabees
- 2 Maccabees
- 1 Esdras
- 2 Esdras
- Manasseh

Future books will include:

- The Sheperd of Hermas
- Apocolypse of Peter
- ...and more like these.

NOTE: If you are not a coder and would simply prefer some nicely formatted versions of these books, then get them here: https://github.com/scrollmapper/bible_databases_deuterocanonical/tree/master/book_sources

---------------
# To Get Started

NOTE: It is suggested that you use a virtual environment running python 3 ( https://virtualenvwrapper.readthedocs.io/en/latest/ ).

First, make your virtual environment:
```
$ mkvirtualenv --python=/usr/bin/python3 scrollmapper
$ cdvirtualenv
```
Next, implement the project:
```
$ pip install django
$ git clone https://github.com/scrollmapper/bible_databases_deuterocanonical
$ cd bible_databases_deuterocanonical
$ ./manage.py runserver
```

Go to http://127.0.0.1:8000/admin/
Log in...
user name: scrollmapper
password: scrollmapper

Explore the models / database.

# Intended for Python/Django Literate Users
I have not yet developed the user-friendly front end. But users already familiar with SQlite or Django can utilize the databases easily.

In the case of utilizing the database via django, here is an example of getting the first chapter of Enoch:

```
$ ./manage.py shell
>>> from books.models import *
>>> enoch = Book.objects.filter(slug="enoch_1")
>>> chapter_1 = Verse.objects.filter(book=enoch[0], chapter=1)
>>> for v in chapter_1:
...     "%s %s"%(v.verse_str, v.text)
...

```
outputs...
```
'1 The words of the blessing of Enoch, wherewith he blessed the elect ⌈⌈and⌉⌉ righteous, who will be living in the day of tribulation, when all the wicked ⌈⌈and godless⌉⌉ are to be removed. '
'2 And he took up his parable and said--Enoch a righteous man, whose eyes were opened by God, saw the vision of the Holy One in the heavens, ⌈which⌉ the angels showed me, and from them I heard everything, and from them I understood as I saw, but not for this generation, but for a remote one which is for to come. '
'3 Concerning the elect I said, and took up my parable concerning them: \nThe Holy Great One will come forth from His dwelling, '
'4 And the eternal God will tread upon the earth, (even) on Mount Sinai, ⌈And appear from His camp⌉ And appear in the strength of His might from the heaven of heavens.\n'
'5 And all shall be smitten with fear And the Watchers shall quake, And great fear and trembling shall seize them unto the ends of the earth.\n'
'6 And the high mountains shall be shaken, And the high hills shall be made low, And shall melt like wax before the flame\n'
'7 And the earth shall be ⌈wholly⌉ rent in sunder, And all that is upon the earth shall perish, And there shall be a judgement upon all (men).\n'
'8 But with the righteous He will make peace.\nAnd will protect the elect, And mercy shall be upon them.\nAnd they shall all belong to God, And they shall be prospered, And they shall ⌈all⌉ be blessed.\n⌈And He will help them all⌉, And light shall appear unto them, ⌈And He will make peace with them⌉.\n'
'9 And behold! He cometh with ten thousands of ⌈His⌉ holy ones To execute judgement upon all, And to destroy ⌈all⌉ the ungodly:\nAnd to convict all flesh Of all the works ⌈of their ungodliness⌉ which they have ungodly committed, And of all the hard things which ungodly sinners ⌈have spoken⌉ against Him.\n\n'
>>> 

```









