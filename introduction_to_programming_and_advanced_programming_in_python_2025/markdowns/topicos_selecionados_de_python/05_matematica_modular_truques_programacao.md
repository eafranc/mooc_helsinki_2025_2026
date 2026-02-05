# Matemática Modular em Programação - Guia de Truques

## Índice
- [[#O que é Matemática Modular?]]
- [[#Operadores Básicos: // e %]]
- [[#Truque 1: Divisão Ceiling (Arredondamento para Cima)]]
- [[#Truque 2: Conversão Base-0 ↔ Base-1]]
- [[#Truque 3: Ciclos e Wrap-around]]
- [[#Truque 4: Detectar Múltiplos]]
- [[#Truque 5: Distribuir Itens Uniformemente]]
- [[#Truque 6: Conversão entre Unidades]]
- [[#Truque 7: Índices Circulares]]
- [[#Truque 8: Paridade (Par/Ímpar)]]
- [[#Problemas Práticos Comuns]]
- [[#Referência Rápida]]

---

## O que é Matemática Modular?

**Matemática modular** trabalha com **restos de divisão**. É como um relógio: depois das 12 horas, volta para 1.

### Conceitos Básicos

```python
# Divisão inteira (//): quantas vezes cabe?
17 // 5 = 3  # 5 cabe 3 vezes em 17

# Módulo (%): qual o resto?
17 % 5 = 2   # sobram 2 (porque 3 × 5 = 15, faltam 2 para 17)

# Relação fundamental:
dividendo = divisor × quociente + resto
17 = 5 × 3 + 2
```

### Analogia do Relógio

```python
# Relógio de 12 horas
hora_atual = 10
horas_depois = 5

nova_hora = (10 + 5) % 12 = 15 % 12 = 3
# 10h + 5h = 3h (15h no formato 12h)
```

---

## Operadores Básicos: // e %

### Divisão Inteira `//` (Floor Division)

Retorna **quantas vezes** o divisor cabe no dividendo (arredonda para baixo).

```python
# Exemplos positivos
10 // 3 = 3   # 3 cabe 3 vezes em 10
15 // 4 = 3   # 4 cabe 3 vezes em 15
30 // 30 = 1  # 30 cabe 1 vez em 30

# Casos especiais
5 // 10 = 0   # 10 não cabe em 5 (0 vezes)
0 // 5 = 0    # 0 dividido por qualquer coisa é 0
```

### Módulo `%` (Remainder)

Retorna o **resto** da divisão.

```python
# Exemplos básicos
10 % 3 = 1    # 10 = 3×3 + 1 (resto 1)
15 % 4 = 3    # 15 = 4×3 + 3 (resto 3)
30 % 30 = 0   # 30 = 30×1 + 0 (sem resto)

# Casos especiais
5 % 10 = 5    # 5 = 10×0 + 5 (resto é o próprio número)
0 % 5 = 0     # sem resto
```

### Propriedades Importantes

```python
# 1. O resto é sempre menor que o divisor
a % b < b  # sempre verdadeiro (para b > 0)

17 % 5 = 2  # 2 < 5 ✓
100 % 7 = 2 # 2 < 7 ✓

# 2. Se dividendo < divisor, o resto é o próprio dividendo
3 % 10 = 3
7 % 100 = 7

# 3. Múltiplos sempre dão resto 0
30 % 30 = 0
60 % 30 = 0
90 % 30 = 0
```

---

## Truque 1: Divisão Ceiling (Arredondamento para Cima)

**Problema:** Python's `//` arredonda para baixo. E se precisarmos arredondar para cima?

### Fórmula Mágica

```python
# Arredondar A ÷ B para CIMA:
resultado = (A + B - 1) // B

# Ou equivalente:
resultado = (A - 1) // B + 1  # se A > 0
```

### Exemplos Práticos

#### Exemplo 1: Páginas necessárias

```python
# 100 itens, 25 por página. Quantas páginas?
total_itens = 100
por_pagina = 25

# Errado (floor):
paginas = total_itens // por_pagina  # 100 // 25 = 4

# Certo (ceiling):
paginas = (total_itens + por_pagina - 1) // por_pagina
paginas = (100 + 24) // 25 = 124 // 25 = 4  ✓

# Testando com 101 itens:
paginas = (101 + 24) // 25 = 125 // 25 = 5  ✓ (precisa de 5!)
```

#### Exemplo 2: Blocos de memória

```python
# Preciso de 1000 bytes, blocos de 512 bytes
bytes_needed = 1000
block_size = 512

blocos = (bytes_needed + block_size - 1) // block_size
blocos = (1000 + 511) // 512 = 1511 // 512 = 2  ✓
```

#### Exemplo 3: Threads para processar tarefas

```python
# 100 tarefas, 8 threads disponíveis
# Quantas tarefas por thread?
tarefas = 100
threads = 8

por_thread = (tarefas + threads - 1) // threads
por_thread = (100 + 7) // 8 = 107 // 8 = 13  ✓
# Cada thread pega 13 tarefas (última thread pega menos)
```

### Por Que Funciona?

```python
# Adicionar (divisor - 1) "empurra" não-múltiplos para cima
# Mas não afeta múltiplos exatos

# Múltiplo exato:
(30 + 29) // 30 = 59 // 30 = 1  ✓ (não vira 2)

# Não-múltiplo:
(31 + 29) // 30 = 60 // 30 = 2  ✓ (arredonda para cima)
```

---

## Truque 2: Conversão Base-0 ↔ Base-1

**Problema:** Computadores usam base-0 (0, 1, 2, ...), mas humanos usam base-1 (1, 2, 3, ...).

### Contexto

```python
# Arrays/listas em programação (base-0):
lista = ['a', 'b', 'c']
lista[0]  # primeiro elemento

# Dias, meses, andares (base-1):
# Dias: 1, 2, 3, ..., 30 (não existe dia 0)
# Meses: 1, 2, 3, ..., 12 (não existe mês 0)
# Andares: 1, 2, 3, ... (térreo = 1º andar)
```

### Fórmula de Conversão

```python
# BASE-1 → BASE-0: subtrair 1
indice_base0 = valor_base1 - 1

# BASE-0 → BASE-1: somar 1
valor_base1 = indice_base0 + 1

# Para operações com divisão/módulo:
# Converter para base-0, operar, converter de volta
resultado_base1 = (valor_base1 - 1) operacao tamanho + 1
```

### Exemplo: Calendário Simplificado

```python
# Dado total de dias, encontrar mês e dia
# (meses de 30 dias, começando em 1)

total_dias = 65  # 65 dias desde o início do ano

# ERRADO (sem conversão):
mes = total_dias // 30 = 65 // 30 = 2  # ❌ (deveria ser 3)
dia = total_dias % 30 = 65 % 30 = 5    # ✓

# CERTO (com conversão base-1):
mes = (total_dias - 1) // 30 + 1
mes = (65 - 1) // 30 + 1 = 64 // 30 + 1 = 2 + 1 = 3  ✓

dia = (total_dias - 1) % 30 + 1
dia = (65 - 1) % 30 + 1 = 64 % 30 + 1 = 4 + 1 = 5   ✓

# Resultado: dia 5 do mês 3 (Março)
```

### Casos Críticos (Múltiplos)

```python
# Dia 30 (último do mês):
total_dias = 30

# SEM conversão:
mes = 30 // 30 = 1       # ✓
dia = 30 % 30 = 0        # ❌ dia 0 não existe!

# COM conversão:
mes = (30 - 1) // 30 + 1 = 29 // 30 + 1 = 0 + 1 = 1  ✓
dia = (30 - 1) % 30 + 1 = 29 % 30 + 1 = 29 + 1 = 30 ✓

# Resultado: dia 30 do mês 1 ✓
```

### Exemplo: Andares de Prédio

```python
# Subiu 33 degraus, 10 degraus por andar
# Andares começam em 1 (térreo = 1º andar)

degraus = 33

# SEM conversão:
andar = degraus // 10 = 33 // 10 = 3  # ❌ (está no 4º andar!)

# COM conversão:
andar = (degraus - 1) // 10 + 1
andar = (33 - 1) // 10 + 1 = 32 // 10 + 1 = 3 + 1 = 4  ✓

# Porque: degraus 1-10 = andar 1
#         degraus 11-20 = andar 2
#         degraus 21-30 = andar 3
#         degraus 31-40 = andar 4 ← 33 está aqui!
```

---

## Truque 3: Ciclos e Wrap-around

**Problema:** Fazer valores "darem a volta" quando atingem um limite.

### Relógio / Dias da Semana

```python
# Que dia da semana será daqui a 10 dias?
# Hoje é segunda (0), semana tem 7 dias

hoje = 0  # 0=seg, 1=ter, 2=qua, ..., 6=dom
dias_depois = 10

dia_futuro = (hoje + dias_depois) % 7
dia_futuro = (0 + 10) % 7 = 10 % 7 = 3  # quarta-feira

# Generalização:
novo_valor = (valor_atual + incremento) % tamanho_ciclo
```

### Índices Circulares (Lista Circular)

```python
# Acessar próximo elemento, voltando ao início se necessário
lista = ['A', 'B', 'C', 'D', 'E']
indice_atual = 4  # último elemento ('E')

# Próximo (volta para 0):
proximo = (indice_atual + 1) % len(lista)
proximo = (4 + 1) % 5 = 0  # volta para 'A'

# Anterior (volta para o final):
anterior = (indice_atual - 1) % len(lista)
anterior = (0 - 1) % 5 = -1 % 5 = 4  # vai para 'E'
```

### Rotação de Array

```python
def rotacionar(lista, k):
    """Rotaciona lista k posições para a direita"""
    n = len(lista)
    k = k % n  # normaliza k (caso k > n)
    
    rotacionada = []
    for i in range(n):
        novo_indice = (i + k) % n
        rotacionada.append(lista[novo_indice])
    
    return rotacionada

# Exemplo:
nums = [1, 2, 3, 4, 5]
rotacionar(nums, 2)  # [4, 5, 1, 2, 3]
```

### Caesar Cipher (Cifra de César)

```python
def cifrar(texto, shift):
    """Cifra de César: desloca letras"""
    resultado = ""
    
    for char in texto:
        if char.isalpha():
            # Converter para 0-25
            base = ord('A') if char.isupper() else ord('a')
            pos = ord(char) - base
            
            # Aplicar shift com wrap-around
            nova_pos = (pos + shift) % 26
            
            # Converter de volta
            novo_char = chr(base + nova_pos)
            resultado += novo_char
        else:
            resultado += char
    
    return resultado

# Exemplo:
cifrar("HELLO", 3)  # "KHOOR"
# H(7) → K(10), E(4) → H(7), L(11) → O(14), ...
```

---

## Truque 4: Detectar Múltiplos

**Problema:** Verificar se um número é múltiplo de outro.

### Fórmula Básica

```python
# N é múltiplo de M se:
N % M == 0

# Exemplos:
30 % 10 == 0  # True (30 é múltiplo de 10)
33 % 10 == 0  # False (33 não é múltiplo de 10)
```

### Aplicações Práticas

#### Exemplo 1: Exibir a cada N linhas

```python
# Exibir cabeçalho a cada 10 linhas
for i in range(1, 101):
    if i % 10 == 1:  # linhas 1, 11, 21, 31, ...
        print("=== CABEÇALHO ===")
    print(f"Linha {i}")
```

#### Exemplo 2: Alternar cores (zebra)

```python
# Linhas pares em branco, ímpares em cinza
for i in range(20):
    cor = "branco" if i % 2 == 0 else "cinza"
    print(f"Linha {i}: {cor}")
```

#### Exemplo 3: Processar em lotes

```python
# Processar dados em lotes de 100
dados = list(range(1, 1000))
batch_size = 100

for i, item in enumerate(dados):
    processar(item)
    
    # A cada 100 itens, salvar progresso
    if (i + 1) % batch_size == 0:
        salvar_checkpoint()
        print(f"Processados {i + 1} itens")
```

#### Exemplo 4: Ano bissexto

```python
def eh_bissexto(ano):
    """Verifica se ano é bissexto"""
    # Divisível por 4 E
    # (não divisível por 100 OU divisível por 400)
    return ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)

# Testes:
eh_bissexto(2000)  # True (divisível por 400)
eh_bissexto(1900)  # False (divisível por 100 mas não por 400)
eh_bissexto(2024)  # True (divisível por 4, não por 100)
```

---

## Truque 5: Distribuir Itens Uniformemente

**Problema:** Distribuir N itens entre M containers o mais uniformemente possível.

### Fórmula

```python
# Itens por container (mínimo):
itens_por_container = total_itens // num_containers

# Containers que recebem 1 item extra:
containers_extras = total_itens % num_containers
```

### Exemplo Prático

```python
# Distribuir 100 tarefas entre 8 workers
tarefas = 100
workers = 8

base = tarefas // workers  # 100 // 8 = 12
extras = tarefas % workers  # 100 % 8 = 4

# Resultado:
# 4 workers recebem 13 tarefas (12 + 1)
# 4 workers recebem 12 tarefas
# Total: 4×13 + 4×12 = 52 + 48 = 100 ✓

def distribuir_tarefas(total, num_workers):
    base = total // num_workers
    extras = total % num_workers
    
    distribuicao = []
    for i in range(num_workers):
        if i < extras:
            distribuicao.append(base + 1)
        else:
            distribuicao.append(base)
    
    return distribuicao

print(distribuir_tarefas(100, 8))
# [13, 13, 13, 13, 12, 12, 12, 12]
```

---

## Truque 6: Conversão entre Unidades

**Problema:** Converter entre unidades (segundos ↔ horas/minutos/segundos, etc).

### Tempo: Segundos → Horas:Minutos:Segundos

```python
def segundos_para_hms(total_segundos):
    horas = total_segundos // 3600
    resto = total_segundos % 3600
    
    minutos = resto // 60
    segundos = resto % 60
    
    return horas, minutos, segundos

# Exemplo:
segundos_para_hms(3725)  # (1, 2, 5) = 1h 2min 5s
# 3725 = 1×3600 + 2×60 + 5
```

### Tempo: HH:MM:SS → Segundos

```python
def hms_para_segundos(horas, minutos, segundos):
    return horas * 3600 + minutos * 60 + segundos

# Exemplo:
hms_para_segundos(1, 2, 5)  # 3725 segundos
```

### Calendário Simplificado: Dias → Anos:Meses:Dias

```python
# Assumindo 360 dias/ano, 30 dias/mês

def dias_para_data(total_dias):
    anos = total_dias // 360
    resto = total_dias % 360
    
    meses = (resto - 1) // 30 + 1
    dias = (resto - 1) % 30 + 1
    
    return anos, meses, dias

# Exemplo:
dias_para_data(715358)
# 715358 dias = 1987 anos + 38 dias restantes
# 38 dias = mês 2, dia 8
# Resultado: (1987, 2, 8)
```

### Bytes → KB/MB/GB

```python
def formatar_bytes(bytes_total):
    if bytes_total < 1024:
        return f"{bytes_total} B"
    elif bytes_total < 1024**2:
        kb = bytes_total / 1024
        return f"{kb:.2f} KB"
    elif bytes_total < 1024**3:
        mb = bytes_total / (1024**2)
        return f"{mb:.2f} MB"
    else:
        gb = bytes_total / (1024**3)
        return f"{gb:.2f} GB"

# Exemplos:
formatar_bytes(512)        # "512 B"
formatar_bytes(2048)       # "2.00 KB"
formatar_bytes(5242880)    # "5.00 MB"
formatar_bytes(1073741824) # "1.00 GB"
```

---

## Truque 7: Índices Circulares

**Problema:** Acessar elementos antes/depois em estruturas circulares.

### Buffer Circular (Ring Buffer)

```python
class RingBuffer:
    def __init__(self, tamanho):
        self.buffer = [None] * tamanho
        self.tamanho = tamanho
        self.indice = 0
    
    def adicionar(self, item):
        self.buffer[self.indice] = item
        self.indice = (self.indice + 1) % self.tamanho  # wrap-around
    
    def obter_ultimos(self, n):
        """Retorna últimos n itens"""
        resultado = []
        for i in range(n):
            pos = (self.indice - 1 - i) % self.tamanho
            resultado.append(self.buffer[pos])
        return resultado

# Uso:
rb = RingBuffer(5)
for i in range(1, 8):
    rb.adicionar(i)

print(rb.buffer)  # [6, 7, 3, 4, 5]
# Elementos 1 e 2 foram sobrescritos
```

### Carrossel de Imagens

```python
class Carrossel:
    def __init__(self, imagens):
        self.imagens = imagens
        self.atual = 0
    
    def proxima(self):
        self.atual = (self.atual + 1) % len(self.imagens)
        return self.imagens[self.atual]
    
    def anterior(self):
        self.atual = (self.atual - 1) % len(self.imagens)
        return self.imagens[self.atual]
    
    def ir_para(self, indice):
        self.atual = indice % len(self.imagens)
        return self.imagens[self.atual]

# Uso:
c = Carrossel(['img1.jpg', 'img2.jpg', 'img3.jpg'])
c.proxima()   # img2.jpg
c.proxima()   # img3.jpg
c.proxima()   # img1.jpg (volta ao início)
c.anterior()  # img3.jpg
```

---

## Truque 8: Paridade (Par/Ímpar)

**Problema:** Determinar se número é par ou ímpar.

### Básico

```python
# Par: divisível por 2 (resto 0)
n % 2 == 0  # True se par

# Ímpar: resto 1
n % 2 == 1  # True se ímpar
# ou
n % 2 != 0  # True se ímpar
```

### Aplicações

#### Alternar comportamento

```python
# Zebra: cores alternadas
for i in range(10):
    cor = "branco" if i % 2 == 0 else "cinza"
    print(f"{i}: {cor}")
```

#### Xadrez: casas pretas/brancas

```python
def cor_casa_xadrez(linha, coluna):
    """Casa é preta se (linha + coluna) é par"""
    return "preta" if (linha + coluna) % 2 == 0 else "branca"

# Exemplos:
cor_casa_xadrez(0, 0)  # "preta" (a1)
cor_casa_xadrez(0, 1)  # "branca" (b1)
cor_casa_xadrez(7, 7)  # "preta" (h8)
```

#### Número de bits setados

```python
def contar_bits_pares(n):
    """Retorna True se número de bits 1 é par"""
    count = bin(n).count('1')
    return count % 2 == 0

contar_bits_pares(7)   # False (111 = 3 bits, ímpar)
contar_bits_pares(15)  # False (1111 = 4 bits, par)
```

---

## Problemas Práticos Comuns

### Problema 1: Calendário Perpétuo

```python
class CalendarioSimples:
    """Calendário com meses de 30 dias"""
    
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
    
    def para_dias_totais(self):
        """Converte data para dias totais desde ano 0"""
        return self.ano * 360 + (self.mes - 1) * 30 + self.dia
    
    @classmethod
    def de_dias_totais(cls, total):
        """Converte dias totais para data"""
        ano = total // 360
        resto = total % 360
        
        mes = (resto - 1) // 30 + 1
        dia = (resto - 1) % 30 + 1
        
        return cls(dia, mes, ano)
    
    def adicionar_dias(self, n):
        """Retorna nova data após adicionar n dias"""
        total = self.para_dias_totais()
        return CalendarioSimples.de_dias_totais(total + n)
    
    def diferenca(self, outra_data):
        """Diferença em dias entre duas datas"""
        return abs(self.para_dias_totais() - outra_data.para_dias_totais())
    
    def __str__(self):
        return f"{self.dia:02d}/{self.mes:02d}/{self.ano:04d}"

# Uso:
d1 = CalendarioSimples(28, 12, 1985)
d2 = d1.adicionar_dias(400)
print(d1)  # 28/12/1985
print(d2)  # 08/02/1987
print(d1.diferenca(d2))  # 400 dias
```

### Problema 2: Horário em Formato 24h

```python
class Horario:
    def __init__(self, hora, minuto, segundo):
        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo
    
    def para_segundos(self):
        """Converte para segundos desde meia-noite"""
        return self.hora * 3600 + self.minuto * 60 + self.segundo
    
    @classmethod
    def de_segundos(cls, total_segundos):
        """Converte segundos para horário"""
        # Normaliza para 24h (86400 segundos/dia)
        total_segundos = total_segundos % 86400
        
        hora = total_segundos // 3600
        resto = total_segundos % 3600
        
        minuto = resto // 60
        segundo = resto % 60
        
        return cls(hora, minuto, segundo)
    
    def adicionar(self, horas=0, minutos=0, segundos=0):
        """Adiciona tempo e retorna novo horário"""
        total = self.para_segundos()
        total += horas * 3600 + minutos * 60 + segundos
        return Horario.de_segundos(total)
    
    def __str__(self):
        return f"{self.hora:02d}:{self.minuto:02d}:{self.segundo:02d}"

# Uso:
h1 = Horario(22, 30, 0)
h2 = h1.adicionar(horas=3, minutos=45)  # passa da meia-noite
print(h1)  # 22:30:00
print(h2)  # 02:15:00 (dia seguinte)
```

### Problema 3: Coordenadas em Grid Circular

```python
class GridCircular:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    
    def normalizar(self, x, y):
        """Normaliza coordenadas com wrap-around"""
        x_norm = x % self.largura
        y_norm = y % self.altura
        return x_norm, y_norm
    
    def vizinhos(self, x, y):
        """Retorna 8 vizinhos (incluindo diagonais)"""
        deltas = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]
        
        vizinhos = []
        for dx, dy in deltas:
            nx, ny = self.normalizar(x + dx, y + dy)
            vizinhos.append((nx, ny))
        
        return vizinhos

# Uso: Jogo da Vida (Conway's Game of Life)
grid = GridCircular(10, 10)

# Célula no canto (9, 9)
vizinhos = grid.vizinhos(9, 9)
print(vizinhos)
# Inclui (0, 0) devido ao wrap-around!
```

### Problema 4: Distribuição Round-Robin

```python
def round_robin(tarefas, num_workers):
    """Distribui tarefas entre workers em round-robin"""
    distribuicao = [[] for _ in range(num_workers)]
    
    for i, tarefa in enumerate(tarefas):
        worker_id = i % num_workers
        distribuicao[worker_id].append(tarefa)
    
    return distribuicao

# Uso:
tarefas = list(range(1, 21))  # 20 tarefas
workers = 3

resultado = round_robin(tarefas, workers)
for i, worker_tarefas in enumerate(resultado):
    print(f"Worker {i}: {worker_tarefas}")

# Output:
# Worker 0: [1, 4, 7, 10, 13, 16, 19]
# Worker 1: [2, 5, 8, 11, 14, 17, 20]
# Worker 2: [3, 6, 9, 12, 15, 18]
```

---

## Referência Rápida

### Fórmulas Essenciais

```python
# 1. Divisão ceiling (arredondar para cima)
resultado = (a + b - 1) // b
# ou
resultado = (a - 1) // b + 1  # se a > 0

# 2. Conversão base-0 ↔ base-1
valor_base1 = (valor_base1 - 1) // tamanho + 1  # para índice
valor_base1 = (valor_base1 - 1) % tamanho + 1   # para resto

# 3. Wrap-around (circular)
novo_indice = (indice_atual + offset) % tamanho

# 4. Detectar múltiplo
if n % m == 0:  # n é múltiplo de m

# 5. Par/Ímpar
if n % 2 == 0:  # par
if n % 2 == 1:  # ímpar

# 6. Distribuir uniformemente
por_container = total // num_containers
extras = total % num_containers
# Primeiros 'extras' containers recebem +1

# 7. Conversão de unidades
# Para converter A em unidades de B:
quantidade_B = A // tamanho_B
resto = A % tamanho_B
```

### Casos Especiais para Testar

Sempre teste esses casos ao usar módulo/divisão:

```python
# 1. Zero
0 // n  # sempre 0
0 % n   # sempre 0

# 2. Valores menores que divisor
a // b quando a < b  # sempre 0
a % b quando a < b   # sempre a

# 3. Múltiplos exatos
30 // 30  # 1
30 % 30   # 0 ← CUIDADO! Pode causar bugs

# 4. Negativos (comportamento pode surpreender)
-17 % 5   # 3 em Python (não -2!)
-17 // 5  # -4 em Python (não -3!)
```

### Padrões Comuns

| Objetivo | Código |
|----------|--------|
| Alternar entre 0 e 1 | `i % 2` |
| Alternar entre A e B | `valores[i % 2]` |
| Processar a cada N | `if i % N == 0:` |
| Último de cada grupo | `if (i+1) % N == 0:` |
| Ciclo de 0 a N-1 | `(atual + 1) % N` |
| Dividir em N grupos | `item_id % N` |
| Obter dígito das unidades | `numero % 10` |
| Remover último dígito | `numero // 10` |

---

## Dicas Finais

1. **Sempre teste casos de borda:**
   - Zero
   - Um
   - Múltiplos exatos
   - Valores menores que o divisor

2. **Lembre-se das indexações:**
   - Arrays/listas: base-0
   - Dias/meses/andares: base-1
   - Use `-1` e `+1` para converter

3. **Módulo com negativos:**
   - Python garante: `a % b` tem mesmo sinal de `b`
   - Diferentes de C/Java!

4. **Performance:**
   - `%` e `//` são operações rápidas
   - Evite loops quando possível

5. **Debugging:**
   - Print intermediário: `print(f"{a} // {b} = {a//b}, {a} % {b} = {a%b}")`
   - Teste com valores pequenos primeiro

---

**Criado por:** Claude (Anthropic)  
**Para:** Eric Alcalai França  
**Data:** Dezembro 2024  
**Contexto:** Estudos de Python - Matemática Modular em Programação
