#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' Challenge Python Onbound
    Jogo: Banco Imobiliário
    Author: Marcos Lopes Martins
    Github: gatosimba
    Data: 15-Maio-2020'''

import random

#------------------
def joga_dados(qtd):

    if qtd == 1:
        dado = random.randint(1,6)
    else:
        dado = random.randint(1,12)
    return dado

#-------------------------------
def get_jogador(jogadores, vez):

    for jog in jogadores:
        if jog['vez'] == vez:
            return jog['jogador']

#---------------------------------
def get_proprietario(casas, casa):

    for j in casas:
        if j['casa'] == casa:
            return j['comprador']

#------------------------
def check_fim(jogadores):

    qtd = 0
    for jog in jogadores:
        if jog['gameover']:
            qtd += 1
    return qtd

#-----------------------------
def setar_vencedor(jogadores):

    jogadores = sorted(jogadores, key=lambda k: (k['saldo'], k['vez']), reverse=True) 
    qtv = 0
    
    for jog in jogadores:
        if jog['gameover']:
            continue                
        qtv +=1

    if qtv > 1: # Por critério de desempate
        for jog in jogadores:
            jog['winner'] = True
            jog['vitorias'] += 1
            break
    else: # por critério de desempenho
        for jog in jogadores:
            jog['winner'] = True
            jog['vitorias'] += 1
            break

    return jogadores

#---------------------------
def get_vencedor(jogadores):

    for jog in jogadores:
        if not jog['gameover']:
            return jog['jogador']
