#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
from math import pi
import sys
sys.path.insert(1, "D:\Python")
from r'c04-ch6-exercices-LEX0RE.exercice' import frequence


# TODO: Définissez vos fonction ici
def ellipsoide(a = 1, b = 1, c = 1, p = 1)->tuple:
    volume = (4/3) * pi * a * b * c
    return (volume, volume * p)

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print(ellipsoide(p = 3, a = 3, b = 45, c = 10))
    #print((lambda sentence: sorted(exercice.frequence(sentence), key=exercice.frequence(sentence).__getitem__)[-1])("Ceci est uuuuuune phrase"))
    #print(exercice.frequence("allo"))
    #print(frequency({3:2, 4:6}))
    pass
