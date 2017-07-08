#!/usr/bin/env pypy
# -*- coding: utf-8 -*-
import random
import itertools
from bolsa import Bolsa
from poblacion import Poblacion
from mochila import Mochila

if __name__ == '__main__':
    cant_productos = 200
    capacidad = 3570
    generaciones = 1000
    n = 60 #Tamanio de poblacion
    rnd = random.Random(6352920)

    productos = tuple(Bolsa(i, rnd) for i in range(cant_productos)) # Lista de productos generados aleatoriamente
    pob = Poblacion(productos, rnd, capacidad, n)
    print '-' * 50
    print "Mejor mochila poblacion inicial:"
    print pob
    print '-' * 50
    print

    for i in range(generaciones):
        if (i-1)%100 == 0:
            print '-' * 50
            print "Mejor mochila despues de {0} años ".format(i)
            print pob
            print '-' * 50
        pob.newGeneration()

    print '-' * 50
    print "Mejor mochila despues de {0} años ".format(generaciones)
    print pob
    print '-' * 50
    print pob.mejorWilson()

    mejol = Mochila(0, productos, capacidad, rnd)
