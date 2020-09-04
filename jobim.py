#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' Challenge Python Onbound
    Jogo: Banco Imobiliário
    Author: Marcos Lopes Martins
    Data: 15-Maio-2020'''

#-> Import de bibliotecas necessárias para o Jogo

import random
import datetime
import time
import sys

from operator import itemgetter

#-> Import de funções e utilitários do Jogo

from funcoes import *

#-> Variáveis globais necessárias ao Jogo

qtd_turnos = by_timeout = 0

teste = True

#----------    
def main():
#----------
    
    try:


        startgame = datetime.datetime.now()

#-> Step 1 - Configurar o Jogo (Simulações e Timeout)

        print()
        print("1. Vamos configurar a Quantidade de Simulações do Jogo!")
        print()
        qts = 1
        while qts == 1:
            qts = input("Informe o número de Simulações do Jogo (Sugestão: Mínimo=300 Máximo: 600): ")
        if len(qts) == 0:
            print("Ops! Quantidade de Simulações não informada. Vamos assumir 300.")
            print()
            qts = 300
        qts = int(qts)
        if qts < 300:
            print("Ops! Quantidade de Simulações abaixo do mínimo. Vamos assumir 300.")
            print()
            qts = 300
        if qts > 600:
            print("Ops! Quantidade de Simulações acima do máximo. Vamos assumir 600.")
            print()
            qts = 600

        print()
        print("2. Vamos configurar o Timeout do Jogo!")
        print()
        qtt = 1
        while qtt == 1:
            qtt = input("Informe o número de Rodadas para Timeout (Sugestão: Mínimo=1.000 Máximo: 2.000): ")
        if len(qtt) == 0:
            print("Ops! Rodadas para Timeout não informada. Vamos assumir 1.000.")
            print()
            qtt = 1000
        qtt = int(qtt)
        if qtt < 1000:
            print("Ops! Rodadas para Timeout abaixo do mínimo. Vamos assumir 1.000.")
            print()
            qtt = 1000
        if qtt > 2000:
            print("Ops! Rodadas para Timeout acima do máximo. Vamos assumir 2.000.")
            print()
            qtt = 2000

        #-> Configurar o tabuleiro (board)
        print()
        print("3. Agora vamos configurar o Tabuleiro!")
        print()
        qtp = 1
        while qtp == 1:
            qtp = input("Informe o número de Propriedades (Minímo=20 e Máximo=40): ")
        if len(qtp) == 0:
            print("Ops! Propriedades não informadas. Vamos assumir 20.")
            print()
            qtp = 20
        qtp = int(qtp)
        if qtp < 20:
            print("Ops! Propriedades abaixo do mínimo. Vamos assumir 20.")
            print()
            qtp = 20
        if qtp > 40:
            print("Ops! Propriedades acima do máximo. Vamos assumir 40.")
            print()
            qtp = 40

        casas = []
        lin = {}
        for i in range(qtp):
            lin['casa'] = i + 1
            if (i%2): # casa ímpar
                lin['venda'] = 99 + i
                lin['aluguel'] = 33 + i
            else: # casa par
                lin['venda'] = 88 + i
                lin['aluguel'] = 30 + i
            lin['vazia'] = True
            lin['comprador'] = ''    
            casas.append(lin)
            lin = {}

        qtd_dados = 3
        while qtd_dados == 3:
            qtd_dados = input("Informe o número de Dados (Minímo=1 e Máximo=2): ")
        if len(qtd_dados) == 0:
            print("Ops! Quantidade de Dados não informada. Vamos assumir 1.")
            print()
            qtd_dados = 1
        qtd_dados = int(qtd_dados)
        if qtd_dados < 1:
            print("Ops! Quantidade de Dados abaixo do mínimo. Vamos assumir 1.")
            print()
            qtd_dados = 1
        if qtd_dados > 2:
            print("Ops! Quantidade de Dados acima do máximo. Vamos assumir 2.")
            print()
            qtd_dados = 2

        #-> Configurar os valores em moeda
        print()
        print("4. Agora vamos configurar a grana R$ do Jogo!")
        print()
        vlr_saldo = vlr_premio = 1
        while vlr_saldo == 1:
            vlr_saldo = input("Informe o Valor do Saldo Inicial (Minímo 300,00): ")
        if len(vlr_saldo) == 0:
            print("Ops! Valor do Saldo não informado. Vamos assumir 300,00.")
            print()
            vlr_saldo = 300
        vlr_saldo = int(vlr_saldo)
        if vlr_saldo < 1:
            print("Ops! Valor do Saldo abaixo do mínimo. Vamos assumir 300,00.")
            print()
            vlr_saldo = 300

        while vlr_premio == 1:
            vlr_premio = input("Informe o Valor do Premio ao completar uma volta (Minímo 100,00): ")
        if len(vlr_premio) == 0:
            print("Ops! Valor do Premio não informado. Vamos assumir 100,00.")
            print()
            vlr_premio = 100
        vlr_premio = int(vlr_premio)
        if vlr_premio < 1:
            print("Ops! Valor do Premio abaixo do mínimo. Vamos assumir 100,00.")
            print()
            vlr_premio = 100

        #-> Configurar os jogadores
        print()
        print("5. Vamos configurar o número de Jogadores participantes!")
        print()
        qtj = 1
        while qtj == 1:
            qtj = input("Informe o número de Jogadores (Minímo=2 e Máximo=4): ")
        if len(qtj) == 0:
            print("Ops! Jogadores não informados. Vamos assumir 2.")
            print()
            qtj = 2
        qtj = int(qtj)
        if qtj < 2:
            print("Ops! Jogadores abaixo do mínimo. Vamos assumir 2.")
            print()
            qtj = 2
        if qtj > 4:
            print("Ops! Jogadores acima do máximo. Vamos assumir 4.")
            print()
            qtj = 4

        print()
        print("6. Finalmente, vamos configurar o Nome e Perfil dos Jogadores!")
        print()

        jogadores = ltipo = []
        jog = {}
        xi = 0

        vezes = random.sample(range(1,qtj+1), qtj)
        ltipo = ['I','E','C','A']
        xtipo = []
    
        for i in range(qtj):
            xi += 1
            jnome = input("Informe o Nome do(a) Jogador(a) %s: " % str(xi))
            if len(jnome) < 1:
                jnome = "Jogador"+str(xi)
                print("Ops! Nome não informado. Vamos assumir: %s" % jnome)
                print()
            
            faz = True
            while faz:
                jtipo = input("Informe o Perfil do(a) Jogador(a) %s %s: " % (jnome, ltipo))
                jtipo = jtipo.upper()
                if jtipo in xtipo:
                    print()
                    print("Ops! Perfil do Jogador já foi escolhido: %s" % xtipo)
                    print("Ops! Escolha outro Perfil .............: %s" % ltipo)
                    print()
                elif jtipo not in ltipo:
                    print()
                    print("Ops! Perfil do Jogador não é válido: %s" % ltipo)
                    print()
                else:
                    faz = False
            xtipo.append(jtipo)
            ltipo.remove(jtipo)
        
#-----> Guardar em memória dados do Jogador
            jog['vez']     = vezes[xi-1]
            jog['jogador'] = jnome.upper()
            jog['tipo']    = jtipo # comportamento do jogador            
            jog['credito']  = 0.00
            jog['debito']   = 0.00
            jog['saldo']    = vlr_saldo
            jog['premios']  = 0
            jog['partidas'] = 0
            jog['vitorias'] = 0
            jog['casa']     = 0
            jog['winner']   = False
            jog['gameover'] = False
            jog['var_alug']  = 0
            jog['var_saldo'] = 0
            jog['var_prob']  = 0

            if jtipo.upper() == 'I':
                jog['perfil'] = 'Impulsivo'
            elif jtipo.upper() == 'E':
                jog['perfil'] = 'Exigente'
                jog['var_alug'] = 50
            elif jtipo.upper() == 'C':
                jog['perfil'] = 'Cauteloso'
                jog['var_saldo'] = 80
            elif jtipo.upper() == 'A':
                jog['perfil'] = 'Aleatório'
                jog['var_prob']  = 50.0

            jogadores.append(jog)
            jog = {}

        jogadores = sorted(jogadores, key=lambda k: k['vez']) 

#-----------------------------------------
#-> Step 2 - Lógica do jogo. Let's play...
#-----------------------------------------
        
        print()
        print("Ok, Configuração completa. Aguarde!!! Agora o computador vai jogar...")
        print()

        qtimeout = qtr = qturnos = qtjogadas = qtrodadas= 0
        startgame = datetime.datetime.now()
        
        for s in range(qts): # range(qts) número de partidas (simulações)
            
            # Inicializar as variáveis do jogador para uma nova partida

            setar_vencedor(jogadores)

            for casa in casas:
                casa['vazia'] = True
                casa['comprador'] = ''

            vezes = random.sample(range(1,qtj+1), qtj)
            qtoff = xi = 0
            for jog in jogadores:
                jog['vez']     = vezes[xi]
                jog['casa']    = 0
                jog['winner']  = False
                jog['gameover'] = False
                jog['partidas'] += 1
                jog['premios'] = 0.00
                jog['credito'] = vlr_saldo
                jog['debito']  = 0.00
                jog['saldo']   = vlr_saldo
                xi += 1

            jogadores = sorted(jogadores, key=lambda k: k['vez']) 

            #print("Quantidade de rodadas dentro do turno: %s %s" % (s, qtr))

            if qtr > qtt - 1:
                qtimeout + 1
                
            qtrodadas += qtr
            qtr = 0

            for t in range(qtt): # range(qtt) número de turnos, rodadas

                qtv = 0
                for jog in jogadores:
                    if jog['gameover']:
                        qtv += 1
                if qtv >= qtj - 1:
                    break
                    
                qtr += 1
                startturno = datetime.datetime.now()

                #-> Iniciar uma rodada
                for jog in jogadores:
                    if jog['gameover']:
                        continue
                    
                    passos = joga_dados(qtd_dados)
                    jog['casa'] += passos
                    nomej = jog['jogador']    

                    for casa in casas:

                        if jog['casa'] > qtp:
                            jog['premios'] += vlr_premio
                            jog['credito'] += vlr_premio
                            jog['saldo'] = jog['credito'] - jog['debito']
                            jog['casa'] -= qtp
                        
                        if casa['casa'] == jog['casa']:
                            if casa['vazia']:
                                if jog['tipo'] == 'E' and casa['aluguel'] <= jog['var_alug']:
                                    break
                                if jog['tipo'] == 'C' and jog['saldo'] < jog['var_saldo']:
                                    break
                                if jog['tipo'] == 'A' and (jog['saldo'] < (casa['venda'] * jog['var_prob'] / 100.0)):
                                    break
                                casa['vazia'] = False
                                casa['comprador'] = jog['jogador']
                                jog['debito'] += casa['venda']
                                jog['saldo'] = jog['credito'] - jog['debito']
                                if jog['saldo'] < 0:
                                    jog['gameover'] = True
                                    break
                            else:
                                #-> Pagar aluguel
                                if jog['jogador'] != casa['comprador']:
                                    for j in jogadores:
                                        if j["jogador"] == casa['comprador']: 
                                            j['credito'] += casa['aluguel']
                                            j['saldo'] = j['credito'] - j['debito']
                                            jog['debito'] += casa['aluguel']
                                            jog['saldo'] = jog['credito'] - jog['debito']
                                            if jog['saldo'] < 0:
                                                jog['gameover'] = True
                                                break

                    #-> Fim da busca de uma casa de um jogador
                    pass
                
                #-> Fim da rodada de jogador
                pass                                                

            #-> Fim de uma de 1.000 rodadas
            pass            
            
            #print(msg)
                                            
        #-> Fim de uma de 300 simulações
        #setar_vencedor(jogadores)
        pass
    
#-------------
#-> Show error
#-------------
                
    except Exception as e:
        print(sys.exc_info()[0])


#----------------------------------------------------------------
#-> Step 3 - Mostrar o resumo do jogo e performance dos jogadores
#----------------------------------------------------------------
        
    finally:

        print()
        print("---------------------------------------------------")
        print("Ufa!!! Fim do jogo. Vamos ao Resumo das partidas...")
        print("---------------------------------------------------")

        jogadores = sorted(jogadores, key=lambda k: (k['vitorias'], k['vez']), reverse=True) 

        qtv = 0

        print()
        print("Performance dos jogadores:")

        for jog in jogadores:
            print()
            print("Jogador.................: %s" % (jog['jogador']))
            print("Vitórias................: %s " % jog['vitorias'])

            pvit = round((jog['vitorias'] / qts * 100.0), 2)
            print("Porcentagem de Vitórias.: %s " % pvit)

            print("Comportamento (Perfil)..: %s " % jog['perfil'])

            if jog['gameover']:
                continue                
            qtv +=1

        if qtv > 1: # Por critério de desempate
            for jog in jogadores:
                nomej = jog['jogador']
                saldoj = jog['saldo']
                msg = ("Parabéns %s!!! Venceu por critério de desempate." % nomej)
                break
        else: # por critério de desempenho
            for jog in jogadores:
                nomej = jog['jogador']
                saldoj = jog['saldo']
                msg = ("Parabéns %s!!! Venceu por critério de desempenho." % nomej)
                break

        print()
        print()
        print("----------------------")
        print('So, the Oscar goes to: %s' % nomej)
        print("----------------------")

        print()
        print(msg)
        
        print()
        print("Número de partidas encerradas por timeout..: %s" % qtimeout)

        print()
        print("Número total de turnos.....................: %s" % qtrodadas)

        print()
        print("Quantos turnos em média demora uma partida.: %s" % int(qtrodadas / qts))

        print()
        print("Duração Total da Simulação: %s " % (datetime.datetime.now() - startgame))

'''
        print()
        print("-------------------------")
        print("Propriedades atualizadas: %s" % casas)    
        print()
        print("-------------------------")
        jogadores = sorted(jogadores, key=lambda k: k['vez'], reverse=False) 
        print("Jogadores atualizados...: %s" % jogadores)
'''

#-------------------------
if __name__ == "__main__":
#-------------------------
    
    jogo = input("Deseja iniciar o jogo? (s/n): ")
    if jogo == "s":
        print("Ok, Vamos começar configurando o Jogo...")
        print()
        time.sleep(1)
        main()
    else:
        print ("Ok, bye bye my friend :-)")
        sys.exit()
