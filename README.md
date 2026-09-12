# 🐍 Lógica de Programação em Python

Repositório dedicado aos exercícios e projetos práticos do curso de **Sistemas de Informação (SI) na Faculdade Impacta**.

---

## 🌾 Enigma do Fazendeiro (Lobo, Bode e Repolho)

Implementação em Python para solucionar o clássico problema de travessia de rio, garantindo que nenhum item seja devorado ao longo do trajeto.

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
