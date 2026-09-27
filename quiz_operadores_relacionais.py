
# APRESENTAÇÃO

print('Boas vindas, camarada! É uma longa jornada até chegar ao topo do rock, já dizia AC/DC. Sabendo disso, iremos praticar!')
print('Veja as variáveis abaixo, e depois responda com base na aula anterior. Que a força esteja com você!')

print('a = 3')
print('b = 4')
print('c = 0.25')
print('d = -158')


# VARIÁVEIS DOS EXERCÍCIOS

a = 3
b = 4
c = 0.25
d = -158

# Aqui ficarão salvas as expressões relacionais do quizz

# ---------------------------------------------------------------------
# GABARITO A (True)
# Pergunta 1
gabarito_1 = a == a
while True:
    print('É correto afirmar que a == a?')
    resposta_user = input('Você considera True ou False? ').strip().capitalize()
    if resposta_user == 'True':
        print('Muito bem, caro padawan! A força está com você. Avançando...')
        break
    elif resposta_user == 'False':
        print('Errado! Paciência e tente novamente')
    else:
        print('Comando inválido! Digite apenas "True" ou "False".')

# Pergunta 2
gabarito_2 = a != b
while True:
    print('A expressão a != b está correta?')
    resposta_user = input('Podemos considerar True ou False? ').strip().capitalize()
    if resposta_user == 'True':
        print('Muito bem! Podemos avançar esse treinamento então.')
        break
    elif resposta_user == 'False':
        print('Sabemos que você pode mais, vamos lá! Tente novamente.')
    else:
        print('Comando inválido! Digite apenas "True" ou "False".')

# ---------------------------------------------------------------------
# GABARITO B (False)
# Pergunta 3
gabarito_3 = b <= c
while True:
    print('Podemos afirmar que b<= c?')
    resposta_user = input('True ou False? ').strip().capitalize()
    if resposta_user == 'False':
        print('Exato! Mandou bem.')
        break
    elif resposta_user == 'True':
        print('Mantenha a atenção! Tente novamente.')
    else:
        print('Comando inválido! Digite apenas "True" ou "False".')

# Pergunta 4
gabarito_4 = b != b
while True:
    print('A expressão b != b é verdadeira?')
    resposta_user = input('True ou False? ').strip().capitalize()
    if resposta_user == 'False':
        print('Correto! This is the way.')
        break
    elif resposta_user == 'True':
        print('Mais atenção, vamos lá! Tente novamente.')
    else:
        print('Comando inválido! Digite apenas "True" ou "False".')

# ---------------------------------------------------------------------
# GABARITO C (True)
# Pergunta 5
gabarito_5 = c >= d
while True:
    print('A relação c >= d é verdadeira?')
    resposta_user = input('True ou False? ').strip().capitalize()
    if resposta_user == 'True':
        print('Excelente! Alvo abatido com sucesso.')
        break
    elif resposta_user == 'False':
        print('Ops! Não se distraia, aprendiz.')
    else:
        print('Comando inválido! Digite apenas "True" ou "False".')

# Pergunta 6
gabarito_6 = c < a
while True:
    print('Podemos afirmar que c < a?')
    resposta_user = input('True ou False? ').strip().capitalize()
    if resposta_user == 'True':
        print('Muito bem! Não esperava menos de você.')
        break
    elif resposta_user == 'False':
        print('Atenção aos detalhes. Recomponha-se e tente novamente.')
    else:
        print('Comando inválido! Digite apenas "True" ou "False".')

# ---------------------------------------------------------------------
# GABARITO D (True)
# Pergunta 7
gabarito_7 = d <= c
while True:
    print('A expressão d <= c está correta?')
    resposta_user = input('True ou False? ').strip().capitalize()
    if resposta_user == 'True':
        print('Perfeito! Mas permaneça em guarda.')
        break
    elif resposta_user == 'False':
        print('Eu avisei pra permanecer em guarda. Vamos novamente.')
    else:
        print('Comando inválido! Digite apenas "True" ou "False".')

# Pergunta 8
gabarito_8 = d <= d
while True:
    print('Por fim, podemos afirmar que d <= d?')
    resposta_user = input('True ou False? ').strip().capitalize()
    if resposta_user == 'True':
        print('Parabéns, jovem Padawan! Treinamento concluído com maestria!')
        break
    elif resposta_user == 'False':
        print('Lembre-se das palavras de seu mestre.')
    else:
        print('Comando inválido! Digite apenas "True" ou "False".')
