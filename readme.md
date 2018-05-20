# Scrollmapper :: Deuterocanonical Project

Based on the Scrollmapper bible databases: https://github.com/scrollmapper/bible_databases

This is a Python / Django project for committing Deuterocanonical the books to database for study and research. 

Presently only the book of Enoch (Enoch 1) is included. Future books will include:

- Enoch 2, Enoch 3
- The traditional "Apocryphal" books.
- The Books of Adam and Eve
- 2 Esdras
- The Sheperd of Hermas
- Apocolypse of Peter
- ...and more like these.
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
