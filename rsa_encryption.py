#!/usr/bin/env python
# -*- coding: utf-8 -*-
from math import sqrt; from itertools import count, islice
import random;
import os;
import time;

"""
Alfabeto basico en espanol (minusculas)
"""
alf ={'a':0,
'b':1,
'c':2,
'd':3,
'e':4,
'f':5,
'g':6,
'h':7,
'i':8,
'j':9,
'k':10,
'l':11,
'm':12,
'n':13,
'o':14,
'p':15,
'q':16,
'r':17,
's':18,
't':19,
'u':20,
'v':21,
'w':22,
'x':23,
'y':24,
'z':25}

alf2 ={0:'a',
1:'b',
2:'c',
3:'d',
4:'e',
5:'f',
6:'g',
7:'h',
8:'i',
9:'j',
10:'k',
11:'l',
12:'m',
13:'n',
14:'o',
15:'p',
16:'q',
17:'r',
18:'s',
19:'t',
20:'u',
21:'v',
22:'w',
23:'x',
24:'y',
25:'z'}

def codificar(texto):
    n = len(alf)
    cod = 0
    j = 0
    for i in range(len(texto)-1,-1,-1):
        'print texto[j],alf[texto[j]],n,i'
        cod = cod + (alf[texto[j]]*n**i)
        j=j+1
    return cod

def decodificar(n):
    lista = numberToBase(n)
    texto = ""
    for element in lista:
        texto = texto + alf2[element]
    return texto

def numberToBase(n):
    b=len(alf)
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n /= b # //= for python 3
    return digits[::-1]

def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))


def randPrime(n):
    for i in count(1):
      x = random.randrange(n)
      if isPrime(x):
        return x

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


class Persona:
   'Clase para crear llave publica y privada de una persona'
   'y pueda intercambiar mensajes'

   def __init__(self, nombre, p, q,e=-1):
      self.nombre = nombre
      self.p = p
      self.q = q
      self.N = p*q
      self.func_euler = ((p-1)*(q-1))
      if e == -1:
         self.e = randPrime(self.func_euler)
      else:
         self.e = e
      if (isPrime(p) == False or isPrime(q) == False ):
         raise Exception('p, q o e no son numeros primos')
      self.d = modinv(self.e,self.func_euler)
      self.Ap = (self.q**(p-1))%self.N
      self.dp = (self.d)%(p-1)
      self.Aq = (self.p**(q-1))%self.N
      self.dq = (self.d)%(q-1)

   def cifrar(self,texto):
      return (codificar(texto)**self.e)%self.N

   def descifrar(self,cripto):
      return (cripto**self.d)%self.N

   def descifrar_resto_chino(self,cripto):
      return (self.Ap*((cripto%self.p)**self.dp) + self.Aq*((cripto%self.q)**self.dq))%self.N
