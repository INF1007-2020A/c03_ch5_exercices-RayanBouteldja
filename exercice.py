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
    num_premier=0
    nombre=2
    somme=0
    while num_premier<100:
        estpremier=True
        for i in range(1,nombre+1):
            if nombre%i==0 and i!=1 and i!=nombre:
               estpremier=False
               break
        if estpremier:
            somme+=nombre
            num_premier += 1
        nombre+=1                 
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
        print(numero)


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
