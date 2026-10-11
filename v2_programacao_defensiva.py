# Versão 2: Programação Defensiva (Com try/except e def)

# 1. Regra de Negócio
def calcular_frete(peso_kg):
    return peso_kg * 15.50


# 2. Entrada do Peso
while True:
    try:
        entrada_peso = input("Digite o peso em kg (ex: 10): ").strip()
        peso_produto = int(entrada_peso)
        break
    except ValueError:
        print("[!] Entrada inválida. Digite apenas inteiros.")

# 3. Entrada do Preço
while True:
    try:
        entrada_preco = input("Digite o preço (ex: 500.00): ").strip()
        preco_produto = float(entrada_preco.replace(",", "."))
        break
    except ValueError:
        print("[!] Preço incorreto. Digite apenas números.")

# 4. Processamento
custo_frete = calcular_frete(peso_produto)
valor_total_nota = preco_produto + custo_frete

# 5. Saída de Dados
print(f"Valor do Frete: R$ {custo_frete:.2f}")
print(f"Valor Total da Nota Fiscal: R$ {valor_total_nota:.2f}")
