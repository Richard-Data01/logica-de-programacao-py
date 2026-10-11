# Versão 1: Abordagem Inicial (Sem validação ou tratamento de exceções)

print("Olá! Vamos calcular o frete e o preço total da Nota Fiscal.")

# Entrada de dados
peso_produto = int(input("Digite o peso do produto (em kg): ").strip())

# Processamento
valor_frete = peso_produto * 15.50
print(f"O valor do frete é: R$ {valor_frete:.2f}")

preco_produto = float(input("Digite o PREÇO TOTAL do produto: ").strip())
valor_total_nota = preco_produto + valor_frete

# Saída
print(f"Valor Total da Nota Fiscal: R$ {valor_total_nota:.2f}")
