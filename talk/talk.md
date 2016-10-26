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

Before we start...

Note: find out the level of Python(or general programming) knowledge available

---

Python 101
- - -
- Strings
- Lists
- Dictionaries
- functions
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

----

#### Functions
```python
def say_hi(name):
    print('Hello, {}'.format(name))

say_hi('Guido van Rossum')
# Hello, Guido van Rossum
```

---

### Classes
OOP doesn't have to be scary...

----

## `Class`
> A way to group related data & functions together

----

## `object`
> A single `instance` of a particular `Class`

----

## `method`

> A different name for a `function` when it's attached to a `Class`

----

## `__init__`
> A 'special method' that allows you to pass data into an `object` at creation


----

Each `object` will have the same `methods` as others, but the data contained inside will differ

----

### Example

```python
class BankAccount():
    def __init__(self, account_name, opening_balance=0):
        self.name = account_name
        self.balance = opening_balance

    def withdraw(self, dollar_amount):
        if dollar_amount >= self.balance:
            print("Balance too low: ${:.2f} available".format(self.balance))
        else:
            self.balance = self.balance - dollar_amount
            return dollar_amount

    def deposit(self, dollar_amount):
        self.balance = self.balance + dollar_amount

    def __repr__(self):
        return "Bank Account '{}', Balance ${:.2f}".format(self.name, self.balance)
```

----

```python
class BankAccount():
    def __init__(self, account_name, opening_balance=0):
        self.name = account_name
        self.balance = opening_balance
```

----

```python
    def withdraw(self, dollar_amount):
        if dollar_amount >= self.balance:
            print("Balance too low: {}".format(self.balance))
        else:
            self.balance = self.balance - dollar_amount
            return dollar_amount
```

----

```python
    def deposit(self, dollar_amount):
        self.balance = self.balance + dollar_amount

```

----

```python
savings = BankAccount('savings', opening_balance=3.50)
print(savings)
# Bank Account 'savings', Balance $3.50
savings.deposit(200)
print(savings)
# Bank Account 'savings', Balance $203.50
savings.withdraw(1000)
# Balance too low: $203.50

```

---

## Clear as mud?

Note: Now that we have these basics out of the way, we're going to jump into...

---

## Code Review!!!

----

![image](images/notimeforthat.jpg)

Note: Well, no one wants to just sit through endless slides of code. You want to look at code, we can go hit stack overflow.

---

### Instead...

---

<!-- .slide: data-background-iframe="http://flask.pocoo.org" data-background-color="white"-->


Note: We're going to build a simple Flask application.

----

## NO JAVASCRIPT!

Note: You don't want to read my JavaScript... Anyway, built in HTML forms will suffice for this demo.

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

## Live coding?

----

![image](images/shakeshead.gif)

Note: Yeah, not so much.

---

Follow along on GitHub:

https://github.com/jesseops/talk_chirpy

Note: I'm going to walk you through an iterative process where we build a very very basic implementation, then build out features as we go

----

tags/hello-flask

https://github.com/jesseops/talk_chirpy/blob/hello-flask/code/chirpy/chirpy.py


----

tags/first-chirp

https://github.com/jesseops/talk_chirpy/blob/first-chirp/code/chirpy/chirpy.py

----

tags/embed-avatar

https://github.com/jesseops/talk_chirpy/blob/embed-avatar/code/chirpy/chirpy.py

----

tags/post-uuid

https://github.com/jesseops/talk_chirpy/blob/post-uuid/code/chirpy/chirpy.py

----

tags/delete-post

https://github.com/jesseops/talk_chirpy/blob/delete-post/code/chirpy/chirpy.py


---

Let's write some code.

![image](images/runaway.gif)

----

![image](images/do_it_live.jpg)
Note: Ok, maybe I lied about live coding... Let's replace our simple post object with something object oriented!

---

# Q&A

---

### Next steps

- - -

[A hands-on introduction to Python](https://www.youtube.com/watch?v=MirG-vJOg04)

[Learn Python the Hard Way](https://learnpythonthehardway.org/book)

[The Hitchhikers Guide to Python]('http://docs.python-guide.org/en/latest/')

[Code Academy - Python](https://www.codecademy.com/learn/python)

