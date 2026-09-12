print('Enigma do Fazendeiro')
lado_0 = ['H', 'L', 'B', 'R']
lado_1 = []

print(lado_0)
print(lado_1)

# 1a Viagem: Homem e Bode vão para o lado 1
lado_0.remove('H')
lado_0.remove('B')

lado_1.append('H')
lado_1.append('B')

print('--- Após a 1a viagem ---')
print(lado_0)
print(lado_1)

# 2a Viagem: Homem volta sozinho para o lado 0
lado_1.remove('H')
lado_0.append('H')

print('--- Após a 2a viagem ---')
print(lado_0)
print(lado_1)

# 3a Viagem: Homem leva o Repolho para o lado 1
lado_0.remove('H')
lado_0.remove('R')
lado_1.append('H')
lado_1.append('R')

print("--- 3a Viagem (Leva Repolho) ---")
print(lado_0)
print(lado_1)

# 4a Viagem: Homem e o Bode voltam para o lado 0
lado_1.remove('H')
lado_1.remove('B')
lado_0.append('H')
lado_0.append('B')

print("--- 4a Viagem (Volta Bode) ---")
print(lado_0)
print(lado_1)

# 5a Viagem: Homem leva o Lobo para o lado 1
lado_0.remove('H')
lado_0.remove('L')
lado_1.append('H')
lado_1.append('L')

print("--- 5a Viagem (Leva Lobo) ---")
print(lado_0)
print(lado_1)

# 6a Viagem: Homem vai para o lado 0
lado_1.remove('H')
lado_0.append('H')

print("--- 6a Viagem (Volta Vazio) ---")
print(lado_0)
print(lado_1)

# 7a Viagem: Homem e Bode vao para o lado 1
lado_0.remove('H')
lado_0.remove('B')
lado_1.append('H')
lado_1.append('B')

print("--- 7a Viagem (Leva Bode - Fim) ---")
print(lado_0)
print(lado_1)


