# Parte 7 - Módulos e Recursos Avançados

**Curso:** Python Programming - University of Helsinki MOOC  
**Resumo criado por:** Claude (Anthropic)  
**Para:** Eric Alcalai França

---

## Índice

1. [[#Seção 1 - Modules]]
2. [[#Seção 2 - Randomness]]
3. [[#Seção 3 - Times and Dates]]
4. [[#Seção 4 - Data Processing]]
5. [[#Seção 5 - Creating Your Own Modules]]
6. [[#Seção 6 - More Python Features]]
7. [[#Conceitos-Chave]]
8. [[#Resumo Rápido]]

---

## Seção 1 - Modules

### Debugging com Breakpoint

Python 3.7+ introduziu o comando `breakpoint()` para debugging interativo.

```python
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        breakpoint()  # Pausa execução aqui
        result *= i
    return result

print(factorial(5))
```

**Console de debug:**
- Execução pausa no breakpoint
- Console interativo abre
- Pode testar código naquele ponto exato
- Comandos úteis:
  - `c` ou `continue`: Continua até próximo breakpoint
  - `help`: Mostra comandos disponíveis
  - `exit`: Finaliza execução

⚠️ **Lembre-se:** Remover breakpoints antes de finalizar código!

### O Que São Módulos?

Módulos são arquivos Python que contêm funções, classes e variáveis agrupadas por tema. A biblioteca padrão do Python contém dezenas de módulos úteis.

### Importando Módulos

**Sintaxe básica:**

```python
import math

# Usar funções do módulo
print(math.sqrt(5))      # 2.236...
print(math.log(8, 2))    # 3.0
```

Funções devem ser prefixadas: `math.sqrt`, `math.log`

### Importar Funções Específicas

```python
from math import sqrt, log

print(sqrt(5))    # Sem prefixo!
print(log(5, 2))
```

### Importar Tudo (Star Import)

```python
from math import *

print(sqrt(5))
print(log(5, 2))
```

⚠️ **Cuidado:** Star imports podem causar conflitos de nomes. Útil para testes, mas evite em projetos grandes.

### Explorando Módulos

**Função `dir()`:**

```python
import math

print(dir(math))
# ['acos', 'asin', 'atan', 'ceil', 'cos', 'e', 'exp', 
#  'floor', 'log', 'pi', 'sin', 'sqrt', 'tan', ...]
```

**Documentação oficial:**

https://docs.python.org/3/library/

Cada módulo tem documentação detalhada com exemplos.

### Módulos Úteis da Biblioteca Padrão

**`string`** - Constantes de strings

```python
import string

# Constantes disponíveis
print(string.ascii_letters)  # 'abcdefg...XYZ'
print(string.digits)         # '0123456789'
print(string.punctuation)    # '!"#$%&...'
```

**`fractions`** - Números racionais

```python
from fractions import Fraction

# Criar frações
f1 = Fraction(1, 3)  # 1/3
f2 = Fraction(1, 2)  # 1/2

print(f1 + f2)  # 5/6
```

---

## Seção 2 - Randomness

### Módulo `random`

Fornece funções para gerar números aleatórios e aleatorizar dados.

### Número Aleatório em Intervalo

**`randint(a, b)`** - Inteiro aleatório entre a e b (inclusive)

```python
from random import randint

# Simular dado (1 a 6)
print(randint(1, 6))  # 4

# Jogar dado 10 vezes
for i in range(10):
    print(randint(1, 6), end=" ")
# 5 4 3 2 3 4 6 4 4 3
```

⚠️ **Diferente de `range()`:**
- `randint(1, 6)` → 1, 2, 3, 4, 5, **6** (inclusive)
- `range(1, 6)` → 1, 2, 3, 4, 5 (exclusive)

### Embaralhar Lista

**`shuffle(lista)`** - Embaralha in-place (modifica original)

```python
from random import shuffle

words = ["atlas", "banana", "carrot"]
shuffle(words)
print(words)
# ['banana', 'atlas', 'carrot']
```

### Escolher Item Aleatório

**`choice(sequencia)`** - Retorna item aleatório

```python
from random import choice

words = ["atlas", "banana", "carrot"]
print(choice(words))
# 'carrot'
```

### Amostra Aleatória (Sem Repetição)

**`sample(sequencia, k)`** - k itens aleatórios únicos

```python
from random import sample

# Números de loteria (7 de 40)
number_pool = list(range(1, 41))
weekly_draw = sample(number_pool, 7)
print(sorted(weekly_draw))
# [4, 7, 11, 16, 22, 29, 38]
```

### Comparação: Garantir Unicidade

**Método 1: Loop com verificação**

```python
from random import randint

weekly_draw = []
while len(weekly_draw) < 7:
    new_rnd = randint(1, 40)
    if new_rnd not in weekly_draw:
        weekly_draw.append(new_rnd)
```

**Método 2: Shuffle**

```python
from random import shuffle

number_pool = list(range(1, 41))
shuffle(number_pool)
weekly_draw = number_pool[0:7]
```

**Método 3 (MELHOR): Sample**

```python
from random import sample

number_pool = list(range(1, 41))
weekly_draw = sample(number_pool, 7)
```

### Seed (Valor de Inicialização)

Permite reproduzir mesma sequência "aleatória".

```python
from random import randint, seed

seed(1337)
print(randint(1, 100))  # Sempre mesmo número
```

**Quando usar:**
- ✅ Testes (resultados previsíveis)
- ✅ Debugging
- ❌ Aplicações que precisam de aleatoriedade real

### Aleatoriedade Real vs Pseudoaleatória

- **Pseudoaleatória:** Algoritmo determinístico (random module)
- **Verdadeiramente aleatória:** Fonte externa (radiação, ruído, lava lamps)

Para maioria das aplicações, pseudoaleatória é suficiente.

---

## Seção 3 - Times and Dates

### Objeto `datetime`

Representa data e hora.

**Criar datetime com data/hora atual:**

```python
from datetime import datetime

my_time = datetime.now()
print(my_time)
# 2021-10-19 08:46:49.311393
```

**Criar datetime manualmente:**

```python
from datetime import datetime

# Data apenas (meia-noite por padrão)
my_time = datetime(1952, 12, 24)
print(my_time)
# 1952-12-24 00:00:00

# Com hora
my_time = datetime(2021, 6, 30, 13)        # 13:00
my_time = datetime(2021, 6, 30, 18, 45)    # 18:45
```

### Acessar Elementos de datetime

```python
from datetime import datetime

my_time = datetime(1952, 12, 24)

print("Dia:", my_time.day)      # 24
print("Mês:", my_time.month)    # 12
print("Ano:", my_time.year)     # 1952
print("Hora:", my_time.hour)    # 0
print("Minuto:", my_time.minute) # 0
```

### Comparar Datas

Operadores de comparação funcionam normalmente.

```python
from datetime import datetime

time_now = datetime.now()
midsummer = datetime(2021, 6, 26)

if time_now < midsummer:
    print("Ainda não é verão")
elif time_now == midsummer:
    print("É verão!")
elif time_now > midsummer:
    print("Verão já passou")
```

### Calcular Diferenças (timedelta)

Subtração entre datetime retorna objeto `timedelta`.

```python
from datetime import datetime

time_now = datetime.now()
midsummer = datetime(2021, 6, 26)

difference = midsummer - time_now
print("Verão em", difference.days, "dias")
# Verão em -116 dias (negativo = passou)
```

**Atributos de timedelta:**
- `days`: Número de dias
- `seconds`: Número de segundos (dentro de um dia)
- `microseconds`: Microssegundos

⚠️ **Limitações:**
- Não tem atributo `years` (anos variam em duração)
- Outros valores (weeks, hours) são convertidos para days/seconds

### Adicionar Tempo (datetime + timedelta)

```python
from datetime import datetime, timedelta

midsummer = datetime(2021, 6, 26)

# Adicionar 1 semana
one_week = timedelta(days=7)
week_from_date = midsummer + one_week
print(week_from_date)
# 2021-07-03 00:00:00

# Adicionar múltiplas unidades
long_time = timedelta(weeks=32, days=15)
print(midsummer + long_time)
# 2022-02-20 00:00:00
```

### Precisão em Segundos

```python
from datetime import datetime

time_now = datetime.now()
midnight = datetime(2021, 6, 30)

difference = midnight - time_now
print(f"Meia-noite em {difference.seconds} segundos")
# Meia-noite em 8188 segundos
```

### Formatação de Datas: `strftime()`

Converte datetime para string formatada.

```python
from datetime import datetime

my_time = datetime.now()

print(my_time.strftime("%d.%m.%Y"))
# 19.10.2021

print(my_time.strftime("%d/%m/%Y %H:%M"))
# 19/10/2021 09:31
```

**Códigos de formatação comuns:**

| Código | Significado | Exemplo |
|--------|-------------|---------|
| `%d` | Dia (01-31) | 19 |
| `%m` | Mês (01-12) | 10 |
| `%Y` | Ano (4 dígitos) | 2021 |
| `%y` | Ano (2 dígitos) | 21 |
| `%H` | Hora 24h (00-23) | 09 |
| `%I` | Hora 12h (01-12) | 09 |
| `%M` | Minutos (00-59) | 31 |
| `%S` | Segundos (00-59) | 45 |
| `%p` | AM/PM | AM |

### Parse de Strings: `strptime()`

Converte string formatada para datetime.

```python
from datetime import datetime

birthday = input("Digite sua data de nascimento (dd.mm.yyyy): ")
my_time = datetime.strptime(birthday, "%d.%m.%Y")

if my_time < datetime(2000, 1, 1):
    print("Nasceu no milênio passado")
else:
    print("Nasceu neste milênio")

# Digite sua data de nascimento (dd.mm.yyyy): 5.11.1986
# Nasceu no milênio passado
```

---

## Seção 4 - Data Processing

### Módulo `csv`

Processa arquivos CSV de forma robusta.

**Problema com `split()`:**

```python
# Se CSV contém strings com delimitador:
# "aaa;bbb";"ccc;ddd"

line.split(";")  # ❌ Divide dentro das strings!
```

**Solução: Módulo csv**

```python
import csv

with open("test.csv") as my_file:
    for line in csv.reader(my_file, delimiter=";"):
        print(line)

# ['012121212', '5']
# ['012345678', '2']
```

O módulo csv trata corretamente strings que contêm o delimitador.

### Módulo `json`

JSON (JavaScript Object Notation) é formato popular para troca de dados.

**Exemplo de arquivo JSON (courses.json):**

```json
[
    {
        "name": "Introduction to Programming",
        "abbreviation": "ItP",
        "periods": [1, 3]
    },
    {
        "name": "Advanced Course in Programming",
        "abbreviation": "ACiP",
        "periods": [2, 4]
    }
]
```

**Ler JSON:**

```python
import json

with open("courses.json") as my_file:
    data = my_file.read()

courses = json.loads(data)  # Converte para Python
print(courses)
# [{'name': 'Introduction to Programming', ...}, ...]

# Acessar dados
for course in courses:
    print(course["name"])
# Introduction to Programming
# Advanced Course in Programming
```

**Estrutura JSON → Python:**
- JSON array `[]` → Python `list`
- JSON object `{}` → Python `dict`
- JSON string → Python `str`
- JSON number → Python `int`/`float`
- JSON true/false → Python `True`/`False`
- JSON null → Python `None`

### Recuperar Dados da Internet

Módulo `urllib.request` permite buscar conteúdo online.

**Exemplo básico:**

```python
import urllib.request

my_request = urllib.request.urlopen("https://helsinki.fi")
print(my_request.read())
```

**Exemplo prático: API JSON**

```python
import urllib.request
import json

def retrieve_all():
    address = "https://studies.cs.helsinki.fi/stats-mock/api/courses"
    request = urllib.request.urlopen(address)
    data = request.read()
    
    courses = json.loads(data)
    
    # Filtrar cursos ativos
    active = []
    for course in courses:
        if course["enabled"]:
            name = course["fullName"]
            exercises = sum(course["exercises"])
            active.append((name, course["name"], course["year"], exercises))
    
    return active
```

⚠️ **Problema SSL no Mac:**

Se encontrar erro de certificado SSL:

```python
import ssl

def retrieve_all():
    context = ssl._create_unverified_context()
    # ou use certifi
```

---

## Seção 5 - Creating Your Own Modules

### Criando Módulo Próprio

Qualquer arquivo `.py` pode ser módulo!

**Arquivo: `words.py`**

```python
def first_word(my_string: str):
    parts = my_string.split(" ")
    return parts[0]

def last_word(my_string: str):
    parts = my_string.split(" ")
    return parts[-1]

def number_of_words(my_string: str):
    parts = my_string.split(" ")
    return len(parts)
```

**Usar o módulo:**

```python
import words

sentence = "Sheila sells seashells by the seashore"

print(words.first_word(sentence))   # Sheila
print(words.last_word(sentence))    # seashore
print(words.number_of_words(sentence))  # 6
```

⚠️ **Importante:** Arquivo do módulo deve estar:
- No mesmo diretório do programa, OU
- Em diretório padrão do Python

### Importar Funções Específicas

```python
from words import first_word, last_word

sentence = input("Digite uma frase: ")

print("Primeira palavra:", first_word(sentence))
print("Última palavra:", last_word(sentence))
```

### Type Hints em Módulos

Type hints são especialmente úteis em módulos!

```python
# words.py
def first_word(my_string: str) -> str:
    parts = my_string.split(" ")
    return parts[0]
```

Editores como VSCode mostram type hints automaticamente ao usar o módulo.

### Problema: Código no Nível do Módulo

**Se módulo contém código fora de funções:**

```python
# words.py
def first_word(my_string: str):
    # ...

# Código de teste
print(first_word("This is a test"))  # Executado ao importar!
```

**Ao importar, testes são executados:**

```python
import words  # Imprime "This"!

my_string = "Sheila sells seashells"
print(words.first_word(my_string))
```

Resultado:

```
This          ← do módulo
Sheila        ← do programa
```

### Solução: `__name__` e `__main__`

Python tem variável especial `__name__`:
- Se programa executado diretamente: `__name__ == "__main__"`
- Se importado: `__name__ == "nome_do_modulo"`

**Isolar testes:**

```python
# words.py
def first_word(my_string: str) -> str:
    parts = my_string.split(" ")
    return parts[0]

def last_word(my_string: str) -> str:
    parts = my_string.split(" ")
    return parts[-1]

if __name__ == "__main__":
    # Testes só executados se módulo rodado diretamente
    print(first_word("This is a test"))
    print(last_word("Here we are testing"))
```

**Executar módulo diretamente:**

```bash
python words.py
```

Resultado:

```
This
testing
```

**Importar em outro programa:**

```python
import words

print(words.first_word("Hello world"))
# Hello
# (sem executar testes!)
```

**Por isso usamos `if __name__ == "__main__":` nos exercícios!**

---

## Seção 6 - More Python Features

### Expressões Condicionais (Ternary Operator)

Condicional em uma linha: `a if condição else b`

```python
# Tradicional
if x % 2 == 0:
    print("par")
else:
    print("ímpar")

# Ternary
print("par" if x % 2 == 0 else "ímpar")
```

**Útil para atribuições condicionais:**

```python
# Tradicional
if x % 2 == 0:
    y += 1
else:
    y = 0

# Ternary
y = y + 1 if x % 2 == 0 else 0
```

### Comando `pass`

Python não permite blocos vazios. Use `pass` quando não quiser fazer nada.

```python
# Função que não faz nada (para testes)
def testing():
    pass

# Sem pass → ERRO
def testing():  # SyntaxError!
```

**Útil em:**
- Funções placeholder
- Blocos except vazios
- Classes ainda não implementadas

### Loops com `else`

Bloco `else` em loop executa se loop terminar normalmente (sem `break`).

```python
my_list = [3, 5, 2, 8, 1]

for x in my_list:
    if x % 2 == 0:
        print("Encontrou número par:", x)
        break
else:
    print("Não há números pares")

# Encontrou número par: 2
```

**Equivalente tradicional:**

```python
my_list = [3, 5, 2, 8, 1]
found = False

for x in my_list:
    if x % 2 == 0:
        print("Encontrou número par:", x)
        found = True
        break

if not found:
    print("Não há números pares")
```

### Parâmetros com Valor Padrão

```python
def say_hello(name="Emily"):
    print("Olá,", name)

say_hello()          # Olá, Emily (usa padrão)
say_hello("Eric")    # Olá, Eric
say_hello("Matthew") # Olá, Matthew
say_hello("")        # Olá,  (string vazia ≠ sem argumento)
```

⚠️ **String vazia ainda é argumento!**

### Número Variável de Parâmetros (`*args`)

Asterisco antes do parâmetro captura argumentos restantes em tupla.

```python
def testing(*my_args):
    print("Você passou", len(my_args), "argumentos")
    print("Soma:", sum(my_args))

testing(1, 2, 3, 4, 5)
# Você passou 5 argumentos
# Soma: 15
```

**Útil para:**
- Funções que aceitam quantidade variável de argumentos
- Wrappers de funções
- APIs flexíveis

---

## Conceitos-Chave

### Módulos da Biblioteca Padrão

| Módulo | Uso | Exemplo |
|--------|-----|---------|
| `math` | Funções matemáticas | `sqrt()`, `log()`, `sin()` |
| `random` | Números aleatórios | `randint()`, `choice()`, `shuffle()` |
| `datetime` | Datas e horas | `datetime.now()`, `timedelta()` |
| `string` | Constantes de strings | `ascii_letters`, `digits` |
| `fractions` | Frações | `Fraction(1, 3)` |
| `csv` | Arquivos CSV | `csv.reader()` |
| `json` | Arquivos JSON | `json.loads()`, `json.dumps()` |
| `urllib.request` | Conteúdo web | `urlopen()` |

### Funções do Módulo `random`

| Função | Descrição | Exemplo |
|--------|-----------|---------|
| `randint(a, b)` | Inteiro entre a e b (inclusive) | `randint(1, 6)` → 4 |
| `choice(seq)` | Item aleatório | `choice(['a','b'])` → 'b' |
| `shuffle(list)` | Embaralha in-place | `shuffle(my_list)` |
| `sample(seq, k)` | k itens únicos | `sample(range(100), 5)` |
| `seed(x)` | Define seed | `seed(1337)` |

### Formatação de datetime

| Código | Significado | Exemplo |
|--------|-------------|---------|
| `%d` | Dia (01-31) | 19 |
| `%m` | Mês (01-12) | 10 |
| `%Y` | Ano (4 dígitos) | 2021 |
| `%y` | Ano (2 dígitos) | 21 |
| `%H` | Hora 24h | 09 |
| `%I` | Hora 12h | 09 |
| `%M` | Minutos | 31 |
| `%S` | Segundos | 45 |
| `%p` | AM/PM | AM |

**Exemplo:**

```python
dt.strftime("%d/%m/%Y %H:%M")  # 19/10/2021 09:31
```

### JSON ↔ Python

| JSON | Python |
|------|--------|
| array `[]` | list |
| object `{}` | dict |
| string | str |
| number | int/float |
| true/false | True/False |
| null | None |

---

## Resumo Rápido

### Programa Exemplo - Sistema de Gerenciamento de Tarefas

```python
# ============ MÓDULO: tasks.py ============
"""Módulo para gerenciamento de tarefas."""

from datetime import datetime, timedelta
import json
import random

def load_tasks(filename: str) -> list:
    """Carrega tarefas de arquivo JSON."""
    try:
        with open(filename) as f:
            data = f.read()
        return json.loads(data)
    except FileNotFoundError:
        return []

def save_tasks(filename: str, tasks: list):
    """Salva tarefas em arquivo JSON."""
    with open(filename, "w") as f:
        f.write(json.dumps(tasks, indent=2))

def add_task(tasks: list, description: str, days_until_due: int = 7):
    """Adiciona nova tarefa."""
    due_date = datetime.now() + timedelta(days=days_until_due)
    
    task = {
        "id": random.randint(1000, 9999),
        "description": description,
        "due_date": due_date.strftime("%Y-%m-%d"),
        "completed": False
    }
    
    tasks.append(task)
    return task

def get_overdue_tasks(tasks: list) -> list:
    """Retorna tarefas atrasadas."""
    today = datetime.now()
    overdue = []
    
    for task in tasks:
        if task["completed"]:
            continue
        
        due = datetime.strptime(task["due_date"], "%Y-%m-%d")
        if due < today:
            overdue.append(task)
    
    return overdue

def format_task(task: dict) -> str:
    """Formata tarefa para exibição."""
    status = "✓" if task["completed"] else " "
    return f"[{status}] {task['id']}: {task['description']} (até {task['due_date']})"

def get_random_encouragement() -> str:
    """Mensagem motivacional aleatória."""
    messages = [
        "Você consegue!",
        "Continue assim!",
        "Ótimo trabalho!",
        "Está indo bem!"
    ]
    return random.choice(messages)

# Testes (só executam se módulo rodado diretamente)
if __name__ == "__main__":
    # Teste básico
    tasks = []
    add_task(tasks, "Estudar Python", 3)
    add_task(tasks, "Fazer exercícios", 7)
    
    print("Tarefas criadas:")
    for task in tasks:
        print(format_task(task))
    
    print("\n" + get_random_encouragement())

# ============ PROGRAMA PRINCIPAL: main.py ============
import tasks

def main():
    # Carregar tarefas existentes
    task_list = tasks.load_tasks("tasks.json")
    
    while True:
        print("\n=== Gerenciador de Tarefas ===")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Ver tarefas atrasadas")
        print("4. Marcar como concluída")
        print("5. Sair")
        
        choice = input("\nEscolha: ")
        
        if choice == "1":
            desc = input("Descrição: ")
            days = input("Dias até vencimento (7): ")
            days = int(days) if days else 7
            
            task = tasks.add_task(task_list, desc, days)
            print(f"\nTarefa #{task['id']} criada!")
            print(tasks.get_random_encouragement())
        
        elif choice == "2":
            if not task_list:
                print("\nNenhuma tarefa cadastrada")
            else:
                print("\nTarefas:")
                for task in task_list:
                    print(tasks.format_task(task))
        
        elif choice == "3":
            overdue = tasks.get_overdue_tasks(task_list)
            
            if not overdue:
                print("\nNenhuma tarefa atrasada! 🎉")
            else:
                print(f"\n{len(overdue)} tarefa(s) atrasada(s):")
                for task in overdue:
                    print(tasks.format_task(task))
        
        elif choice == "4":
            task_id = int(input("ID da tarefa: "))
            
            for task in task_list:
                if task["id"] == task_id:
                    task["completed"] = True
                    print(f"\n✓ Tarefa #{task_id} concluída!")
                    print(tasks.get_random_encouragement())
                    break
            else:
                print(f"\nTarefa #{task_id} não encontrada")
        
        elif choice == "5":
            # Salvar antes de sair
            tasks.save_tasks("tasks.json", task_list)
            print("\nTarefas salvas. Até logo!")
            break

if __name__ == "__main__":
    main()
```

### Checklist de Conceitos

**Módulos:**
- [ ] Sei usar `import module`
- [ ] Sei usar `from module import function`
- [ ] Sei usar `dir()` para explorar módulos
- [ ] Conheço módulos úteis (math, random, datetime, etc.)
- [ ] Sei criar meus próprios módulos
- [ ] Uso `if __name__ == "__main__":` corretamente

**Random:**
- [ ] Sei gerar números aleatórios com `randint()`
- [ ] Sei embaralhar listas com `shuffle()`
- [ ] Sei escolher item aleatório com `choice()`
- [ ] Sei gerar amostras únicas com `sample()`
- [ ] Entendo diferença entre aleatório e pseudoaleatório

**Datetime:**
- [ ] Sei criar objetos datetime
- [ ] Sei acessar dia, mês, ano, hora
- [ ] Sei comparar datas
- [ ] Sei calcular diferenças com timedelta
- [ ] Sei adicionar tempo a datas
- [ ] Sei formatar com `strftime()`
- [ ] Sei fazer parse com `strptime()`

**Data Processing:**
- [ ] Sei processar CSV com módulo csv
- [ ] Sei ler JSON com `json.loads()`
- [ ] Sei buscar dados online com urllib.request
- [ ] Entendo estrutura JSON → Python

**Features Avançadas:**
- [ ] Sei usar expressões ternárias
- [ ] Sei quando usar `pass`
- [ ] Sei usar for-else
- [ ] Sei definir parâmetros com valor padrão
- [ ] Sei usar `*args` para parâmetros variáveis

### Armadilhas Comuns

| Erro | Problema | Solução |
|------|----------|---------|
| `randint(1, 6)` vs `range(1, 6)` | randint é inclusive | `randint(1, 6)` → 1-6, `range(1, 6)` → 1-5 |
| Esquecer seed em testes | Resultados diferentes | Use `seed()` para reproduzibilidade |
| `datetime - datetime` | Esquece que retorna timedelta | Acessar `.days`, `.seconds` |
| Comparar string com datetime | TypeError | Converter string com `strptime()` |
| JSON com datetime | datetime não é serializável | Converter para string antes |
| Código fora de `if __name__` | Executa ao importar | Sempre usar `if __name__ == "__main__":` |
| Bloco vazio sem `pass` | SyntaxError | Adicionar `pass` |
| String vazia como padrão | Usa valor padrão? | Não! String vazia ≠ sem argumento |

### Padrões de Design com Módulos

**1. Estrutura de Módulo Típica**

```python
"""Docstring do módulo."""

# Imports
import math
from datetime import datetime

# Constantes
DEFAULT_TIMEOUT = 30
MAX_RETRIES = 3

# Funções
def public_function():
    """Função pública."""
    pass

def _private_function():
    """Função privada (convenção: prefixo _)."""
    pass

# Testes
if __name__ == "__main__":
    # Código de teste
    pass
```

**2. Separação de Concerns**

```python
# data.py - Camada de dados
def load_from_file(filename):
    pass

# business.py - Lógica de negócio
import data

def process_data():
    raw = data.load_from_file("data.json")
    # processar...

# ui.py - Interface
import business

def main():
    business.process_data()
    # exibir...
```

**3. Type Hints para Documentação Automática**

```python
# mymodule.py
from typing import List, Dict, Optional

def process_users(users: List[Dict[str, str]]) -> Optional[str]:
    """Processa lista de usuários.
    
    Args:
        users: Lista de dicionários com dados de usuários
        
    Returns:
        Relatório formatado ou None se lista vazia
    """
    pass
```

---

## Parabéns! 🎓

Você completou o curso **Python Programming** da Universidade de Helsinki!

### O Que Você Aprendeu

**Fundamentos:**
- Variáveis, tipos, operadores
- Condicionais, loops
- Funções, parâmetros, return

**Estruturas de Dados:**
- Listas, tuplas, sets
- Dicionários
- Matrizes (listas 2D)

**Programação Avançada:**
- Arquivos (leitura/escrita)
- Tratamento de erros (try-except)
- Módulos próprios

**Bibliotecas Padrão:**
- random, datetime
- csv, json
- urllib.request

**Boas Práticas:**
- Type hints
- Escopo de variáveis
- Separação de responsabilidades
- Documentação

### Próximos Passos

1. **Pratique:** Crie projetos próprios
2. **Advanced Course in Programming:** Continue sua jornada
3. **Bibliotecas populares:** pandas, numpy, requests, flask
4. **Especialização:** Data Science, Web Dev, Automation

---

**Fonte:** University of Helsinki MOOC - Python Programming  
**Resumo criado por:** Claude (Anthropic)  
**Para:** Eric Alcalai França

**Parabéns pela conclusão do curso!** 🎉
