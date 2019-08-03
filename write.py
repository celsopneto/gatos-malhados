# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 20:46:56 2019

@author: Celso Pereira Neto
"""

import json

class Animal:
    def __init__(self, nome, specie):
        self.nome = nome
        self.specie = specie
    def __str__(self):
        return "{} diz oi. {}".format(self.nome, self.cumprimento())


    def cumprimento(self):
        """

        """
        if hasattr(self, "cumprimento"):
            print(self)
        else:
            print("Esse animal prefere manter um mistério sobre si mesmo")



class Gato(Animal):
    def __init__(self, nome, cor_olhos, padrao_pelagem, cor_pelagem):
        Animal.__init__(self, nome=nome, specie="Felis Gatous")
        self.cor_olhos = cor_olhos
        self.padrao_pelagem = padrao_pelagem
        self.cor_pelagem = cor_pelagem

    def cumprimento(self):
        if self.padrao_pelagem != "tortoise":
            return "Meow"
        else:
            return "Meooow"


    def toJSON(self):
        return {"nome": self.nome,
                "specie": self.specie,
                "cor_olhos": self.cor_olhos,
                "padrao_pelagem" : self.padrao_pelagem,
                "cor_pelagem": self.cor_pelagem,
                "cumprimento": self.cumprimento()
                }



def main():
    gatos = [Gato("Mel", "blue", "tabby", ["white, black"]),
             Gato("Sunshine", "green", "tortoise", ["yellow, black, white"]),
             Gato("Ramona", "green", "black smoke", ["black, white"])
            ]
    json_gatos = [gato.toJSON() for gato in gatos]


    with open("gatos.json", "w") as file:
        json.dump(json_gatos, file)

if __name__ == '__main__':
    main()

