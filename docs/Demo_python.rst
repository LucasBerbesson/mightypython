
Mighty Python
-------------

A list of python mini demos

Python est simple...
--------------------

| Python est un langage simple et minimaliste.
| C'est un langage de haut niveau.
| Il fait abstraction des caractéristiques techniques du matériel
  utilisé pour exécuter le programme.
| Pas de gestion de mémoire, de processeur, de registres ... juste du
  code fonctionnel ! Un programme bien écrit se lit comme du pseudo-code
  anglais.
| Son système d'indentation le rend très propre : pas de ; ni de {}...
| Python est facile à apprendre, de plus en plus enseigné (lycée,
  prépa...)
| La communauté pythonienne rédige d'excellentes documentations, claires
  et concises, comme Python !

...utilisé par beaucoup de monde
--------------------------------

Google, Nasa, Youtube, Dropbox, Reddit, Instagram, MIT ...

...gratuit et open source
-------------------------

| Tout le monde peut avoir accès et contribuer à son code source et à
  ses librairies.
| Permet de faire beaucoup de choses que certains logiciels payants ne
  proposent pas (Maple).
| Python est un langage interpreté ce qui le rend très Portable :
  GNU/Linux, Windows, FreeBSD, Macintosh... Un même code source peut
  fonctionner exactement de la même manière sur toutes ces plateformes :
  l'interpréteur se charge de la compilation en fonction de l'OS.

...orienté objet...si on veut
-----------------------------

Python permet de faire de la programmation fonctionnelle et objet.

| En Python, tout est un objet, et peut être manipulé en tant que tel.
| Les fonctions, les classes, les chaînes et même les types sont des
  objets en Python: comme tout objet ils peuvent être passés comme
  arguments de fonction, et ils peuvent avoir des méthodes et
  propriétés.

Cependant, contrairement à Java, Python n’impose pas la programmation
orientée objet comme paradigme de programmation principal. Il est
parfaitement viable pour un projet de Python de ne pas être orienté
objet, à savoir de ne pas utiliser ou très peu de définitions de
classes, d’héritage de classe, ou d’autres mécanismes qui sont
spécifiques à la programmation orientée objet.

La gestion par modules permet aux développeur d'encapsuler naturellement
les couches d'abstractions de leur code.

Les fonctions pures sont des blocs de construction plus efficaces que
les classes et les objets pour certaines architectures parce qu’elles
n’ont pas de contexte ou d’effets de bord. L’orientation objet est utile
et même nécessaire dans de nombreux cas.

...typé dynamiquement
---------------------

| En python les variables sont des "tags" pointant vers des objets.
  L'interpréteur se charge de deviner leur type.
| Pour les variables comme pour beaucoup d'autres choses, on fait
  confiance aux programmeurs pour utiliser un nommage intelligent.

.. code:: ipython3

    a = "Hello world"
    a = 3
    def a():
        print("Finalement je suis une fonction")

...en kit complet
-----------------

**Enormément de librairies standards** : Expression régulières,
génération de doc, test unitaires, threading, database, CGI, FTP, EMail,
XML, HTML, Cryptography, GUI ...

**Encore plus de libraries open source** : Frameworks web, Text
processing, Machine learning, analyse de données, Maths, API, Images,
Son, Geo loc, e-commerce, Dataviz, authentification, scrap ...

Petit tour d'horizon
--------------------

.. code:: ipython3

    import this


.. parsed-literal::

    The Zen of Python, by Tim Peters
    
    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!


Strings
-------

.. code:: ipython3

    # String format
    "Hello my name is {} and I love {}".format("Lucas", "Python")




.. parsed-literal::

    'Hello my name is Lucas and I love Python'



.. code:: ipython3

    # Named string format
    "Hello my name is {name} and I'm {age}".format(name="Lucas",age=26)




.. parsed-literal::

    "Hello my name is Lucas and I'm 26"



.. code:: ipython3

    # String format mini-language
    '{:,}'.format(1234567890)




.. parsed-literal::

    '1,234,567,890'



.. code:: ipython3

    # Strings are iterable. So you can use iterable methods on them...
    print(len("DevStudio"))
    for letter in "abc":
        print(letter)
    print("12th letter of the alphabet is :","abcdefghijklmnopqrstuvwxyz"[12])


.. parsed-literal::

    9
    a
    b
    c
    12th letter of the alphabet is : m


.. code:: ipython3

    "Hello " * 3




.. parsed-literal::

    'Hello Hello Hello '



Lists
-----

| Lists are the most versatile datatype available in Python.
| Lists might contain items of different types, but usually the items
  all have the same type.

.. code:: ipython3

    colors = ["blue","yellow","green"]
    colors.append("purple")
    colors = colors + ["pink"]
    colors.remove("yellow")
    
    for color in colors:
        print(color)


.. parsed-literal::

    blue
    green
    purple
    pink


.. code:: ipython3

    print("green" in colors)
    print("pink is color number {}/{}".format(colors.index('pink'),len(colors)))
    colors[2:4]


.. parsed-literal::

    True
    pink is color number 3/4




.. parsed-literal::

    ['purple', 'pink']



.. code:: ipython3

    # List comprehensions are very powerful
    COLORS = [color.upper() for color in colors]
    print(COLORS)


.. parsed-literal::

    ['BLUE', 'GREEN', 'PURPLE', 'PINK']


.. code:: ipython3

    # enumerate works on any object that supports iteration
    for i,color in enumerate(colors):
        print(i,color)


.. parsed-literal::

    0 blue
    1 green
    2 purple
    3 pink


.. code:: ipython3

    # key specifies a function of one argument that is used to extract a comparison key from each list element
    for color in sorted(colors, key=len):
        print(color)  
    print("--------")
    for color in sorted(["apple","banana","cherry"],key=lambda x:x[-1]):
        print(color)


.. parsed-literal::

    blue
    pink
    green
    purple
    --------
    banana
    apple
    cherry


.. code:: ipython3

    hello = "Bonjour je fais du Python"
    hello2 = hello.split(" ")
    hello3 = "-".join(hello)
    print(hello2)
    print(hello3)



.. parsed-literal::

    ['Bonjour', 'je', 'fais', 'du', 'Python']
    B-o-n-j-o-u-r- -j-e- -f-a-i-s- -d-u- -P-y-t-h-o-n


.. code:: ipython3

    # Zip makes an iterator that aggregates elements from each of the iterables.
    names = ["sky", "sun", "tree"]
    colors = ["blue","yellow","green"]
    for name, color in zip(names, colors):
        print(name,"is",color)  


.. parsed-literal::

    sky is blue
    sun is yellow
    tree is green


Tuples
------

| A tuple is an immutable list.
| Tuples are faster and safer than lists. If you’re defining a constant
  set of values and all you’re ever going to do with it is iterate
  through it, use a tuple instead of a list

.. code:: ipython3

    sites_a_visiter = ("google.com", "stackoverflow.com","lafabriquediy.com")
    sites_a_visiter.remove("google.com")


::


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-19-a531d5a9385b> in <module>()
          1 sites_a_visiter = ("google.com", "stackoverflow.com","lafabriquediy.com")
    ----> 2 sites_a_visiter.remove("google.com")
    

    AttributeError: 'tuple' object has no attribute 'remove'


Dicts
-----

A dictionary is an unordered set of key-value pairs.

.. code:: ipython3

    d = {"sky":"blue","sun":"yellow","tree":"green"}
    del d["sky"]
    
    d.get("sky","black")
    for key in d:
        print(key)


.. parsed-literal::

    sun
    tree


.. code:: ipython3

    len(d)




.. parsed-literal::

    2



.. code:: ipython3

    for key in d:
        print(d[key])


.. parsed-literal::

    yellow
    green


Sets
----

A set is an unordered “bag” of unique values.

.. code:: ipython3

    panier = ['pomme', 'orange', 'pomme', 'banane', 'orange', 'banane']
    panier = set(panier)
    panier.add("pomme")
    print(panier)


.. parsed-literal::

    {'pomme', 'banane', 'orange'}


.. code:: ipython3

    a_set = {2, 4, 5, 9, 12, 21, 30, 51, 76, 127, 195}
    b_set = {1, 2, 3, 5, 6, 8, 9, 12, 15, 17, 18, 21}
    # New set with elements common to the set and all others.
    a_set.intersection(b_set) 
    # new set with elements in the set that are not in the others.
    a_set.difference(b_set) 




.. parsed-literal::

    {4, 30, 51, 76, 127, 195}



Classes
-------

.. code:: ipython3

    import math
    class Complex:
        """Classe représentant un nombre complexe"""
        def __init__(self, realpart, imagpart):
            """Constructeur de notre classe"""
            self.r = realpart
            self.i = imagpart
        def __add__(self, other):
            "Méthode spéciale pour réutiliser le + de python"
            return Complex(self.r + other.i,self.r + other.i)
        
        def __repr__(self):
            """Représentation de notre objet par l'interpréteur"""
            return "{} + i{}".format(self.r,self.i)
        
        @property
        def module(self):
            """Affiche le module du nombre complexe"""
            return (math.sqrt(self.r**2+self.i**2))
    
    x = Complex(3.0, -4.5)
    y = Complex(1.0, 1.0)
    z = x+y
    y.module
    y




.. parsed-literal::

    1.0 + i1.0



.. code:: ipython3

    # Exemple de conteneur
    class Panier:
        nbpanier = 0
        def __init__(self, value=()): # Émulation du constructeur de list
            self.contenu = [element for element in value.split(',')]
            Panier.nbpanier +=1
        def __len__(self): # Sera utile pour les tests
            return len(self.contenu)
        def __getitem__(self, key):
            return self.contenu[key]
        def __setitem__(self, key, value):
            self.contenu[key] = value
        def __delitem__(self, key):
            del self.contenu[key]
        def __contains__(self, value):
            return value in self.contenu
    
    monpanier = Panier("banane,pomme")
    tonpanier = Panier("abricot,fraise")
    
    len(monpanier)
    monpanier[0]
    "banane" in monpanier
    Panier.nbpanier
    dir(Panier)
    monpanier.__dict__





.. parsed-literal::

    {'contenu': ['banane', 'pomme']}



Flow control
------------

If, else, while, try, except ...

.. code:: ipython3

    try:
        3/0
    except Exception as e:
        print(e)


.. parsed-literal::

    division by zero


.. code:: ipython3

    number = 23
    guess = 0
    while guess is not number:
        guess = int(input('Enter an integer : '))
        if guess < number:
            print('No, it is a little higher than that')
        else:
            print('No, it is a little lower than that')
    
    print('Congratulations, you guessed it.')
    print('(but you do not win any prizes!)')


.. parsed-literal::

    Enter an integer : 23
    No, it is a little lower than that
    Congratulations, you guessed it.
    (but you do not win any prizes!)


Decorateurs
-----------

Un moyen simple de modifier le comportement « par défaut » de fonctions.

.. code:: ipython3

    def cache(function):
      memo = {}
      def wrapper(*args):
        if args in memo:
          return memo[args]
        else:
          rv = function(*args)
          memo[args] = rv
          return rv
      return wrapper
    @cache
    def fibonacci(n):
      if n < 2: return n
      return fibonacci(n - 1) + fibonacci(n - 2)
    
    
    fibonacci(35)




.. parsed-literal::

    9227465



Les merveilles de la bibliothèque standard
==========================================

Collections
-----------

| Specialized container datatypes providing alternatives to Python’s
  general purpose built-in containers, dict, list, set, and tuple.
| `Documentation <https://docs.python.org/3.6/library/collections.html>`__

.. code:: ipython3

    import collections
    count = collections.Counter(["banana","apple","apple","orange","cherry","cherry","banana","cherry"])
    print(count)
    print(count.most_common(2))



.. parsed-literal::

    Counter({'cherry': 3, 'banana': 2, 'apple': 2, 'orange': 1})
    [('cherry', 3), ('banana', 2)]


.. code:: ipython3

    d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
    d = collections.OrderedDict(sorted(d.items(), key=lambda t: t[1]))
    print(d)


.. parsed-literal::

    OrderedDict([('pear', 1), ('orange', 2), ('banana', 3), ('apple', 4)])


Regex
-----

Les expressions régulières sont un puissant moyen de rechercher et
d'isoler des expressions d'une chaîne de caractères.

.. code:: ipython3

    import re
    text = "Bonjour je m'appelle Lucas et mon numéro de téléphone lucasberbesson@fabdev.fr est le "
    m = re.findall(r'[\w\.-]+@[\w\.-]+', text)
    m




.. parsed-literal::

    ['lucasberbesson@fabdev.fr']



Time & Datetime
---------------

Contrôler le temps.
`documentation <https://docs.python.org/3/library/datetime.html>`__

.. code:: ipython3

    # datetime(année, mois, jour, heure, minute, seconde, microseconde, fuseau horaire)
    import locale
    locale.setlocale(locale.LC_TIME, "fr_FR")
    
    from datetime import datetime
    maintenant = datetime.now()
    print(maintenant.year, maintenant.month, maintenant.hour, maintenant.minute)
    print('{:%A %d %B %Y %H:%M:%S }'.format(maintenant))



.. parsed-literal::

    2017 4 23 25
    Mardi 25 avril 2017 23:25:17 


.. code:: ipython3

    # Find next friday the 13th
    import datetime
    today = datetime.datetime.today()
    while not (today.day == 13 and today.weekday() == 4):
        today += datetime.timedelta(days=1)
    print(today)


.. parsed-literal::

    2017-10-13 23:25:18.570794


Random
------

Générer de l'aléatoire.
`Documentation <https://docs.python.org/3.6/library/random.html>`__

.. code:: ipython3

    import random
    #un nombre aléatoire entre 
    entier = random.randint(1, 100)
    print(entier)
    cadavre_exquis = 'Bonjour comment ça va'.split()
    random_word = random.choice(cadavre_exquis)
    random.shuffle(cadavre_exquis)
    print(random_word)
    print(cadavre_exquis)


.. parsed-literal::

    26
    ça
    ['Bonjour', 'ça', 'va', 'comment']


Open
----

Open file and return a corresponding file object. If the file cannot be
opened, an OSError is raised.

.. code:: ipython3

    with open('./data/demo.txt') as f:
        print(f.read())


.. parsed-literal::

    Hello world
    


Logs
----

| This module defines functions and classes which implement a flexible
  event logging system for applications and libraries.
| Better than prints for you application events.
  `Documentation <https://docs.python.org/3/library/logging.html>`__

.. code:: ipython3

    import logging
    logging.basicConfig(format='%(asctime)s %(message)s',filename='./logs/example.log',level=logging.DEBUG)
    logging.debug('This message should go to the log file')
    logging.info('So should this')
    logging.warning('And this, too')

OS
--

| This module provides a portable way of using operating system
  dependent functionality.
| If you just want to read or write a file see open(), if you want to
  manipulate paths, see the os.path module, and if you want to read all
  the lines in all the files on the command line see the fileinput
  module.
| For creating temporary files and directories see the tempfile module,
  and for high-level file and directory handling see the shutil module.
  `Documentation <https://docs.python.org/3.6/library/os.html>`__

.. code:: ipython3

    # Remplacer récursivement tous les " " par des "_" dans le dossier courant
    import os
    before = os.listdir(".")
    for path, folders, files in os.walk("."):
        for file in files:
            os.rename(os.path.join(path,file), os.path.join(path, file.replace(' ', '_')))
        for folder in folders:
            new_name = folder.replace(' ', '_')
            os.rename(os.path.join(path, folder), os.path.join(path, new_name))
    
    after = os.listdir(".")
    for before,after in zip(before,after):
        print(before,'-->',after)


.. parsed-literal::

    .DS_Store --> .DS_Store
    .git --> .git
    .gitignore --> .gitignore
    .ipynb_checkpoints --> .ipynb_checkpoints
    data --> data
    Demo_librairies.ipynb --> Demo_librairies.ipynb
    Demo_python.ipynb --> Demo_python.ipynb
    docs --> docs
    example.db --> example.db
    Improve_python.ipynb --> Improve_python.ipynb
    logs --> logs
    passgen.py --> passgen.py
    Play.ipynb --> Play.ipynb
    requests --> requests
    requirements.txt --> requirements.txt
    templates --> templates
    tests --> tests


JSON
----

Easy to use JSON API.
`Documentation <https://docs.python.org/3.6/library/json.html>`__

.. code:: ipython3

    
    import json
    # Json to string
    print(json.dumps({'4': 5, '6': 7}, sort_keys=True, indent=4))


.. parsed-literal::

    {
        "4": 5,
        "6": 7
    }


.. code:: ipython3

    json_string = '{"first_name": "Guido", "last_name":"Rossum"}'
    # String to json
    parsed_json = json.loads(json_string)
    print(parsed_json['first_name'])



.. parsed-literal::

    Guido


CSV
---

The csv module implements classes to read and write tabular data in CSV
format. `Documentation <https://docs.python.org/3/library/csv.html>`__

.. code:: ipython3

    import csv
     
    # write file
    with open('./data/basket.csv', 'w+') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',')
        filewriter.writerow(['Name', 'Quantity'])
        filewriter.writerow(['Bananas', 3])
        filewriter.writerow(['Oranges', 4])
        filewriter.writerow(['Apples', 5])
        
        
    # read file
    with open('./data/basket.csv', 'r+') as f:
        reader = csv.reader(f)
        # read file row by row
        for row in reader:
            print(row)


.. parsed-literal::

    ['Name', 'Quantity']
    ['Bananas', '3']
    ['Oranges', '4']
    ['Apples', '5']


Math
----

For Maths ...

.. code:: ipython3

    import math
    print(math.cos(math.pi))
    print(math.sqrt(25))


.. parsed-literal::

    -1.0
    5.0


smtplib
-------

| The smtplib module defines an SMTP client session object that can be
  used to send mail to any Internet machine with an SMTP or ESMTP
  listener daemon.
| `Documentation <https://docs.python.org/3.6/library/smtplib.html>`__

import smtplib
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("YOUR EMAIL ADDRESS", "YOUR PASSWORD")
 
msg = "YOUR MESSAGE!"
server.sendmail("YOUR EMAIL ADDRESS", "THE EMAIL ADDRESS TO SEND TO", msg)
server.quit()

sqlite3
-------

SQLite is a C library that provides a lightweight disk-based database
that doesn’t require a separate server process and allows accessing the
database using a nonstandard variant of the SQL query language.
`Documentation <https://docs.python.org/3.6/library/sqlite3.html>`__

.. code:: ipython3

    import sqlite3
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    # Create table
    try:
        c.execute('''CREATE TABLE stocks
                     (date text, trans text, symbol text,qty real, price real)''')
        # Insert a row of data
        c.execute("INSERT INTO stocks VALUES ('2017-04-26','BUY','BANANA', 100,35.14)")
    except:
        pass
    # Larger example that inserts many records at a time
    purchases = [('2006-03-28', 'BUY', 'APPLE', 1000, 45.00),
                 ('2006-04-05', 'BUY', 'ORANGE', 1000, 72.00),
                 ('2006-04-06', 'SELL', 'CHERRY', 500, 53.00),
                ]
    c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)
    # Save (commit) the changes
    conn.commit()
    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    conn.close()

.. code:: ipython3

    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    for row in c.execute('SELECT * FROM stocks ORDER BY price'):
        print(row)


.. parsed-literal::

    ('2017-04-26', 'BUY', 'BANANA', 100.0, 35.14)
    ('2006-03-28', 'BUY', 'APPLE', 1000.0, 45.0)
    ('2006-03-28', 'BUY', 'APPLE', 1000.0, 45.0)
    ('2006-04-06', 'SELL', 'CHERRY', 500.0, 53.0)
    ('2006-04-06', 'SELL', 'CHERRY', 500.0, 53.0)
    ('2006-04-05', 'BUY', 'ORANGE', 1000.0, 72.0)
    ('2006-04-05', 'BUY', 'ORANGE', 1000.0, 72.0)

