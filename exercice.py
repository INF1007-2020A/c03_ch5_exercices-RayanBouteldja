#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List
from math import sqrt

def convert_to_absolute() -> float:
    nombre = float(input("Écrire un nombre: "))
    if nombre<0:
        nombre = -nombre
    return nombre

def use_prefixes() -> List[str]:
    resultat=[]
    prefixes, suffixes = 'JKLMNOP', 'ack'
    for lettre in prefixes:
        mot=lettre+suffixes
        resultat.append(mot)    
    return resultat


def prime_integer_summation() -> int:
    somme=0                  
    return somme


def factorial(number: int) -> int:
    factorielle = 1
    n=0
    while n<number:
        factorielle*=(n+1)
        n+=1
    return factorielle



def use_continue() -> None:
    for numero in range(1,11):
        if numero==5:
           continue
        else:
           print(numero)
    pass


def main() -> None:
    print(f"La valeur absolue du nombre est {convert_to_absolute()}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des nombres de 0 à 100 est: {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()


if __name__ == '__main__':
    main()
