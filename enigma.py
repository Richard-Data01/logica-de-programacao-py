def estado_e_valido(margem):
    # Se o fazendeiro (H) nao esta na margem, verifica se algo e devorado
    if "H" not in margem:
        if "L" in margem and "B" in margem:
            return False  # Lobo come o Bode
        if "B" in margem and "R" in margem:
            return False  # Bode come o Repolho
    return True


def realizar_travessia(origem, destino, item=None):
    if "H" not in origem:
        print("O fazendeiro nao esta nesta margem!")
        return False

    if item and item not in origem:
        print("O item nao esta na margem de origem!")
        return False

    # Mover o fazendeiro
    origem.remove("H")
    destino.append("H")

    # Mover o item (se houver)
    if item:
        origem.remove(item)
        destino.append(item)

    # Se a jogada for invalida, desfaz a travessia (rollback)
    if not estado_e_valido(origem) or not estado_e_valido(destino):
        destino.remove("H")
        origem.append("H")
        if item:
            destino.remove(item)
            origem.append(item)
        print("Jogada invalida! Alguem seria devorado.")
        return False

    return True


def resolver_enigma():
    m_esquerda = ["H", "L", "B", "R"]
    m_direita = []

    print("Iniciando o jogo do Fazendeiro!")
    print("Margem Esquerda:", m_esquerda)
    print("Margem Direita:", m_direita)
    print("---------------------------------------------")

    passos = [
        ("B", "Passo 1: Levar o Bode para a direita"),
        (None, "Passo 2: Fazendeiro volta sozinho"),
        ("L", "Passo 3: Levar o Lobo para a direita"),
        ("B", "Passo 4: Trazer o Bode de volta"),
        ("R", "Passo 5: Levar o Repolho para a direita"),
        (None, "Passo 6: Fazendeiro volta sozinho"),
        ("B", "Passo 7: Levar o Bode para a direita")
    ]

    for item, mensagem in passos:
        print(mensagem)

        if "H" in m_esquerda:
            sucesso = realizar_travessia(m_esquerda, m_direita, item)
        else:
            sucesso = realizar_travessia(m_direita, m_esquerda, item)

        if sucesso:
            print("Margem Esquerda:", m_esquerda)
            print("Margem Direita:", m_direita)
            print("---------------------------------------------")
        else:
            print("Falha na travessia!")
            return False

    print("Parabens! O enigma foi resolvido!")


# Executa a funcao direto no final do script
resolver_enigma()
