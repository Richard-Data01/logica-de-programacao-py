# 🐍 Lógica de Programação em Python

Repositório dedicado aos exercícios e projetos práticos do curso de **Sistemas de Informação (SI) na Faculdade Impacta**.

---

## 🌾 Enigma do Fazendeiro (Lobo, Bode e Repolho)

Implementação em Python para solucionar o clássico problema de travessia de rio, garantindo que nenhum item seja devorado ao longo do trajeto.
![Fluxograma da Resolução](Untitled%20Diagram.drawio.png)

### 🧠 Regras do Problema:
* O Homem possui um barco com capacidade para levar apenas ele e **um** item por vez.
* O **Lobo e o Bode** não podem ficar sozinhos na mesma margem.
* O **Bode e o Repolho** não podem ficar sozinhos na mesma margem.

### 💻 Como foi implementado:
* **Margens do Rio:** Duas listas dinâmicas (`lado_0` e `lado_1`).
* **Movimentação:** Uso dos métodos `.remove()` para retirada da margem de origem e `.append()` para chegada na margem de destino.
* **Resolução:** 7 etapas sequenciais de transporte garantindo a integridade dos itens.

### 🚀 Como executar:
Basta rodar o arquivo `enigma.py` em qualquer ambiente Python (IDLE, VS Code ou terminal):

```bash
python enigma.py
```

---

## 🛡️ Quiz Interativo: Operadores Relacionais (Star Wars & The Mandalorian)

Aplicação interativa desenvolvida em Python para fixação e validação prática de operadores relacionais (`==`, `!=`, `<`, `>`, `<=`, `>=`) com fluxo didático e narrativa temática inspirada no universo de Star Wars.

### 🧠 Decisões de Lógica e Controle de Fluxo:
* **Loop Didático (`while True` + `break`):** O usuário não avança ao errar; o laço força a reflexão e repete a pergunta até que a resposta correta seja inserida.
* **Sanitização de Inputs:** Tratamento da entrada com `.strip().capitalize()`, eliminando espaços acidentais e padronizando digitações em letras minúsculas (`true`/`false`).
* **Tratamento de Comandos Inválidos:** Estrutura condicional (`if/elif/else`) preparada para capturar entradas fora do padrão e emitir alertas contextuais sem interromper a execução do programa.

### 🖥️ Simulação de Execução no Terminal:
```text
É correto afirmar que a == a?
Você considera True ou False? false
Errado! Paciência e tente novamente

É correto afirmar que a == a?
Você considera True ou False? true
Muito bem, caro padawan! A força está com você. Avançando...

A expressão a != b está correta?
Podemos considerar True ou False? 1234
Comando inválido! Digite apenas "True" ou "False".
'''
### 🚀 Como Executar:
1. Certifique-se de que tem o Python instalado no computador.
2. Clone ou descarregue este repositório.
3. No terminal ou linha de comandos, navegue até à pasta do projeto e execute:
   ```bash
   python quiz_operadores_relacionais.py
'''
