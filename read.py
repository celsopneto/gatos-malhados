# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 22:14:14 2019

@author: Celso Pereira Neto
"""
import json
from write import Gato

with open("gatos.json","r") as file:
    from_json_cats = json.load(file)

gatos_recriados = [Gato(c['nome'],
                     c['cor_olhos'],
                     c['padrao_pelagem'],
                     c['cumprimento']) for c in from_json_cats]
tstcats = (('{} diz {}'.format(
        c.nome, c.cumprimento()) for c in gatos_recriados))
for t in tstcats:
    print(t)
