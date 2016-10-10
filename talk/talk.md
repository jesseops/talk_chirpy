## `print('Hello, World!')`

---

### `__init__`
- Speedy development lifecycle
- Popular for education
- Actually useful for real work

----

![image](images/do_it_live.jpg)

----

![image](images/python_codeeval_popular.png)
http://blog.codeeval.com/codeevalblog/2016/2/2/most-popular-coding-languages-of-2016

----

![image](images/philipguo.png)
http://cacm.acm.org/blogs/blog-cacm/176450-python-is-now-the-most-popular-introductory-teaching-language-at-top-u-s-universities/fulltext

----

### etc...
http://blog.trinket.io/why-python/

http://lorenabarba.com/blog/why-i-push-for-python/

https://www.oreilly.com/ideas/python-in-education

https://www.python.org/community/sigs/current/edu-sig/

----

- Dropbox
- Instagram
- Calibre
- Reddit
- Quora

... a lot more

---

## Code Review!!!

----

![image](images/notimeforthat.jpg)

Note: This is a Python talk, so today we're going to <change slide>

---

### Instead...
- Flask is easy
- Unit tests are awesome

Note: Flask - framework for application, unittest - ensure code works as intended

----

## NO JAVASCRIPT!
You don't want to read my JavaScript...

---

## Flask
A simple to use, flexible tool for building web applications.
Huge community of contributors.

----

1000+ community plugins/extensions (via Pip search)
http://flask.pocoo.org/extensions/

----

Major users:
- Netflix
- Pinterest
- LinkedIn
- Twilio
- Reddit

---

## Unittests
Help to ensure code behaves as expected. Throw a fit if you introduce a bug (in well tested code)

----

Tests are only as good as you make them

---

Before we start...

Note: find out the level of Python(or general programming) knowledge available

---

Python 101
- Strings
- Lists
- Dictionaries
- imports
- Classes

----

#### Strings
```python
name = 'Jesse'
name.lower()
# jesse
print('Hello, {}!'.format(name))
# Hello, Jesse!
```

----

#### Lists
```python
people = ['Jesse']
people.append('Natasha')
print(people)
# ['Jesse', 'Natasha']
people.extend(['Roman', 'Kaladin'])
print(people)
# ['Jesse', 'Natasha', 'Roman', 'Kaladin']

print(people[-1])
# Kaladin

print(people[2:])
# ['Roman', 'Kaladin']
```

----

#### Dictionaries
```python
book = {'title': '101 ways to prepare SPAM'}
print(book)
# {'title': '101 ways to prepare SPAM'}
book['author'] = 'BDFL Guido van Rossum'
book['year'] = '1991'
print(book)
# {'author': 'BDFL Guido van Rossum', 'year': '1991', 'title': '101 ways to prepare SPAM'}
```

----

#### imports
```python

import sys

from sys import version

from sys import version as irenamedthis

sys.version == version == irenamedthis
# True
```

---

### Classes
OOB doesn't have to be scary...

----

Classes are a way of tying functions to the data they operate on.

----

An `object` is just an instance of a Class

----

Each object has the same functionality others, but the specific data contained changes

----

`__dunder__`
This method is 'special'. Usually used for allowing arguments to be passed to objects, overloading operators (+, -, *, =, etc)

----

```python

class Car():
    def __init__(self, color, four_wheel_drive=None):
        self.color = color
        self.four_wheel_drive = four_wheel_drive

    def __repr__(self):
        return "{} - {}".format(self.__class__.__name__,
                                self.color)

my_suv = Car('blue', four_wheel_drive=True)
my_car = Car('blue', four_wheel_drive=False)

print(my_suv)
# Car - Blue

```

---

## Lab

Let's write some code.