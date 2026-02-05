# Parte 12 - Programação Funcional e Expressões Regulares

> **Fonte:** University of Helsinki - Python Programming MOOC
> **Resumo criado por:** Claude (Anthropic)
> **Para:** Eric Alcalai França

---

## Índice

- [[#Seção 1 - Funções como Argumentos]]
- [[#Seção 2 - Generators]]
- [[#Seção 3 - Programação Funcional]]
- [[#Seção 4 - Expressões Regulares]]
- [[#Conceitos-Chave]]
- [[#Resumo Rápido]]

---

## Seção 1 - Funções como Argumentos

### O Problema: Ordenação Customizada

Por padrão, listas de tuplas são ordenadas pelo primeiro elemento:

```python
products = [("banana", 5.95), ("apple", 3.95), ("orange", 4.50), ("watermelon", 4.95)]

products.sort()

for product in products:
    print(product)

# ('apple', 3.95)
# ('banana', 5.95)
# ('orange', 4.5)
# ('watermelon', 4.95)
```

E se quisermos ordenar por preço (segundo elemento)?

### Solução: Parâmetro key

O parâmetro `key` aceita uma **função** que define o critério de ordenação:

```python
def order_by_price(item: tuple):
    """Retorna o preço (segundo item da tupla)"""
    return item[1]


products = [("banana", 5.95), ("apple", 3.95), ("orange", 4.50), ("watermelon", 4.95)]

# Passa a FUNÇÃO (não o resultado!) como argumento
products.sort(key=order_by_price)

for product in products:
    print(product)

# ('apple', 3.95)
# ('orange', 4.5)
# ('watermelon', 4.95)
# ('banana', 5.95)
```

### Como Funciona

Python chama a função `key` para **cada item** da lista para determinar seu "valor de ordenação":

```python
def order_by_price(item: tuple):
    print(f"Chamada: order_by_price({item})")
    return item[1]


products.sort(key=order_by_price)

# Chamada: order_by_price(('banana', 5.95))
# Chamada: order_by_price(('apple', 3.95))
# Chamada: order_by_price(('orange', 4.5))
# Chamada: order_by_price(('watermelon', 4.95))
```

### Ordenação Reversa

Use `reverse=True` para ordem decrescente:

```python
products.sort(key=order_by_price, reverse=True)

# Ou com sorted():
sorted_products = sorted(products, key=order_by_price, reverse=True)
```

### Função Auxiliar Interna

Você pode definir a função auxiliar dentro de outra função:

```python
def sort_by_price(items: list):
    # Função auxiliar definida internamente
    def order_by_price(item: tuple):
        return item[1]
    
    return sorted(items, key=order_by_price)
```

### Ordenando Objetos de Classes Próprias

```python
class Student:
    def __init__(self, name: str, id: str, credits: int):
        self.name = name
        self.id = id
        self.credits = credits

    def __str__(self):
        return f"{self.name} ({self.id}), {self.credits} cr."


def by_id(item: Student):
    return item.id

def by_credits(item: Student):
    return item.credits


students = [
    Student("Archie", "a123", 220),
    Student("Marvin", "m321", 210),
    Student("Anna", "a999", 131)
]

print("Por ID:")
for s in sorted(students, key=by_id):
    print(s)

# Archie (a123), 220 cr.
# Anna (a999), 131 cr.
# Marvin (m321), 210 cr.

print("\nPor créditos:")
for s in sorted(students, key=by_credits):
    print(s)

# Anna (a999), 131 cr.
# Marvin (m321), 210 cr.
# Archie (a123), 220 cr.
```

### Lambda Expressions

Funções anônimas criadas "on the fly":

```python
lambda <parâmetros> : <expressão>
```

```python
# Em vez de definir uma função separada...
def order_by_price(item):
    return item[1]

products.sort(key=order_by_price)

# ...use lambda:
products.sort(key=lambda item: item[1])
```

### Exemplos de Lambda

```python
# Ordenar strings pelo último caractere
strings = ["Mickey", "Mack", "Marvin", "Minnie", "Merl"]
sorted_strings = sorted(strings, key=lambda word: word[-1])
# ['Minnie', 'Mack', 'Merl', 'Marvin', 'Mickey']

# Ordenar strings pelas vogais
sorted_vowels = sorted(strings, key=lambda word: "".join([c for c in word if c in "aeiou"]))
# ['Mack', 'Marvin', 'Merl', 'Mickey', 'Minnie']
```

### Lambda com min() e max()

```python
class Recording:
    def __init__(self, name: str, performer: str, year: int, runtime: int):
        self.name = name
        self.performer = performer
        self.year = year
        self.runtime = runtime

    def __str__(self):
        return f"{self.name} ({self.performer}), {self.year}. {self.runtime} min."


recordings = [
    Recording("Nevermind", "Nirvana", 1991, 43),
    Recording("Let It Be", "Beatles", 1969, 35),
    Recording("Joshua Tree", "U2", 1986, 50)
]

# Mais antigo
oldest = min(recordings, key=lambda rec: rec.year)
print(oldest)  # Let It Be (Beatles), 1969. 35 min.

# Mais longo
longest = max(recordings, key=lambda rec: rec.runtime)
print(longest)  # Joshua Tree (U2), 1986. 50 min.
```

### Funções como Argumentos em Funções Próprias

```python
# Type hint "callable" indica uma função
def perform_operation(operation: callable):
    return operation(10, 5)

def my_sum(a: int, b: int):
    return a + b

def my_product(a: int, b: int):
    return a * b


print(perform_operation(my_sum))       # 15
print(perform_operation(my_product))   # 50
print(perform_operation(lambda x, y: x - y))  # 5
```

### Exemplo Prático: Copiar Linhas com Critério

```python
def copy_lines(source_file: str, target_file: str, criterion=lambda x: True):
    """Copia linhas que satisfazem o critério"""
    with open(source_file) as source, open(target_file, "w") as target:
        for line in source:
            line = line.strip()
            if criterion(line):
                target.write(line + "\n")


# Copiar todas as linhas (default)
copy_lines("first.txt", "second.txt")

# Copiar apenas linhas não vazias
copy_lines("first.txt", "second.txt", lambda line: len(line) > 0)

# Copiar linhas que contêm "Python"
copy_lines("first.txt", "second.txt", lambda line: "Python" in line)

# Copiar linhas que não terminam com ponto
copy_lines("first.txt", "second.txt", lambda line: line[-1] != ".")
```

---

## Seção 2 - Generators

### O Problema

Gerar séries (como Fibonacci) recursivamente recalcula tudo a cada chamada. Queremos gerar o **próximo item** sob demanda.

### Solução: Generators

Generators são funções que usam `yield` em vez de `return`:

```python
def counter(max_value: int):
    number = 0
    while number <= max_value:
        yield number  # "retorna" e PAUSA
        number += 1   # continua daqui na próxima chamada
```

### Usando Generators com next()

```python
numbers = counter(10)

print(next(numbers))  # 0
print(next(numbers))  # 1
print(next(numbers))  # 2
# ...
```

### yield vs return

| `return` | `yield` |
|----------|---------|
| Encerra a função | Pausa a função |
| Retorna valor único | Retorna série de valores |
| Função "esquece" estado | Função "lembra" estado |

### StopIteration

Quando o generator se esgota:

```python
numbers = counter(1)

print(next(numbers))  # 0
print(next(numbers))  # 1
print(next(numbers))  # StopIteration exception!
```

### Tratando StopIteration

```python
numbers = counter(1)

try:
    print(next(numbers))
    print(next(numbers))
    print(next(numbers))
except StopIteration:
    print("Acabaram os números!")
```

### Iterando com for

```python
numbers = counter(5)

for number in numbers:
    print(number)

# 0, 1, 2, 3, 4, 5
```

> ⚠️ **Cuidado:** Se o generator não tiver limite, o `for` loop será infinito!

### Generator Infinito

```python
def infinite_counter():
    number = 0
    while True:  # nunca termina
        yield number
        number += 1


# Uso controlado com next()
counter = infinite_counter()
for _ in range(5):
    print(next(counter))
# 0, 1, 2, 3, 4
```

### Generator Comprehensions

Use parênteses `()` em vez de colchetes `[]`:

```python
# List comprehension - cria lista na memória
squares_list = [x ** 2 for x in range(1, 64)]

# Generator comprehension - cria generator (lazy)
squares_gen = (x ** 2 for x in range(1, 64))

print(squares_gen)  # <generator object <genexpr> at 0x...>

for i in range(5):
    print(next(squares_gen))  # 1, 4, 9, 16, 25
```

### Exemplo: Substrings do Alfabeto

```python
substrings = ("abcdefghijklmnopqrstuvwxyz"[i:i+3] for i in range(24))

for i in range(10):
    print(next(substrings))

# abc, bcd, cde, def, efg, fgh, ghi, hij, ijk, jkl
```

### Vantagens de Generators

| Aspecto | Lista | Generator |
|---------|-------|-----------|
| Memória | Toda na RAM | Um item por vez |
| Criação | Imediata | Lazy (sob demanda) |
| Reutilização | Múltiplas vezes | Uma vez só |
| Tamanho | Limitado pela RAM | Pode ser infinito |

---

## Seção 3 - Programação Funcional

### Paradigmas de Programação

| Paradigma | Descrição |
|-----------|-----------|
| **Imperativo** | Sequência de comandos |
| **Procedural** | Agrupado em procedures/funções |
| **Orientado a Objetos** | Estado em objetos/classes |
| **Funcional** | Evita estado; cadeias de funções |

Python permite misturar paradigmas!

### map()

Aplica uma função a **cada item** de uma série:

```python
map(<função>, <série>)
```

```python
str_list = ["123", "-10", "23", "98", "0", "-110"]

# Converter cada string para int
integers = map(lambda x: int(x), str_list)

print(list(integers))  # [123, -10, 23, 98, 0, -110]
```

### map() com Função Nomeada

```python
def capitalize(my_string: str):
    return my_string[0].upper() + my_string[1:]


test_list = ["first", "second", "third", "fourth"]

capitalized = map(capitalize, test_list)
print(list(capitalized))  # ['First', 'Second', 'Third', 'Fourth']
```

### map() Retorna Iterator

```python
capitalized = map(capitalize, test_list)

for word in capitalized:
    print(word)  # First, Second, Third, Fourth

print("De novo:")
for word in capitalized:
    print(word)  # NADA! Iterator esgotado!

# Solução: converter para lista primeiro
capitalized = list(map(capitalize, test_list))
```

### map() com Classes Próprias

```python
class BankAccount:
    def __init__(self, account_number: str, name: str, balance: float):
        self.__account_number = account_number
        self.name = name
        self.__balance = balance

    def get_balance(self):
        return self.__balance


accounts = [
    BankAccount("123456", "Randy Riches", 5000),
    BankAccount("12321", "Paul Pauper", 1),
    BankAccount("223344", "Mary Millionaire", 1000000)
]

# Extrair nomes
clients = map(lambda t: t.name, accounts)
print(list(clients))  # ['Randy Riches', 'Paul Pauper', 'Mary Millionaire']

# Extrair saldos
balances = map(lambda t: t.get_balance(), accounts)
print(list(balances))  # [5000, 1, 1000000]
```

### filter()

Seleciona itens que satisfazem uma condição:

```python
filter(<função_booleana>, <série>)
```

```python
integers = [1, 2, 3, 5, 6, 4, 9, 10, 14, 15]

# Filtrar pares
even_numbers = filter(lambda n: n % 2 == 0, integers)
print(list(even_numbers))  # [2, 6, 4, 10, 14]
```

### filter() com Classes

```python
class Fish:
    def __init__(self, species: str, weight: int):
        self.species = species
        self.weight = weight

    def __repr__(self):
        return f"{self.species} ({self.weight} g.)"


fishes = [
    Fish("Pike", 1870),
    Fish("Perch", 763),
    Fish("Pike", 3410),
    Fish("Cod", 2449),
    Fish("Roach", 210)
]

# Filtrar peixes com peso >= 1000g
over_a_kilo = filter(lambda fish: fish.weight >= 1000, fishes)
print(list(over_a_kilo))
# [Pike (1870 g.), Pike (3410 g.), Cod (2449 g.)]
```

### filter() Também Retorna Iterator

```python
over_a_kilo = filter(lambda fish: fish.weight >= 1000, fishes)

for fish in over_a_kilo:
    print(fish)

# Segunda iteração não funciona!
for fish in over_a_kilo:
    print(fish)  # NADA!

# Solução: converter para lista
over_a_kilo = list(filter(lambda fish: fish.weight >= 1000, fishes))
```

### reduce()

Reduz uma série a um **único valor**:

```python
from functools import reduce

reduce(<função>, <série>, <valor_inicial>)
```

```python
from functools import reduce

my_list = [2, 3, 1, 5]

# Soma: 0 + 2 + 3 + 1 + 5 = 11
sum_of_numbers = reduce(lambda acc, item: acc + item, my_list, 0)
print(sum_of_numbers)  # 11
```

### Como reduce() Funciona

```python
from functools import reduce

def sum_helper(acc, item):
    print(f"acc = {acc}, item = {item}")
    return acc + item


my_list = [2, 3, 1, 5]
result = reduce(sum_helper, my_list, 0)

# acc = 0, item = 2
# acc = 2, item = 3
# acc = 5, item = 1
# acc = 6, item = 5
# result = 11
```

### reduce() para Multiplicação

```python
from functools import reduce

my_list = [2, 2, 4, 3, 5, 2]

# Produto: 1 * 2 * 2 * 4 * 3 * 5 * 2 = 480
product = reduce(lambda prod, item: prod * item, my_list, 1)
print(product)  # 480
```

### reduce() com Objetos

```python
from functools import reduce

# Soma de saldos bancários
def balance_sum_helper(total, account):
    return total + account.get_balance()

accounts = [a1, a2, a3]  # objetos BankAccount
total_balance = reduce(balance_sum_helper, accounts, 0)
print(total_balance)  # 1005001
```

### reduce() Sem Valor Inicial

Se omitido, o primeiro item vira valor inicial:

```python
my_list = [2, 3, 1, 5]

# Funciona (começa com 2)
sum_result = reduce(lambda acc, item: acc + item, my_list)

# ERRO se tipos diferentes!
# reduce(balance_sum_helper, accounts)  # TypeError
```

### Comparação: map vs filter vs reduce

| Função | Entrada | Saída | Uso |
|--------|---------|-------|-----|
| `map` | n itens | n itens | Transformar cada item |
| `filter` | n itens | ≤n itens | Selecionar itens |
| `reduce` | n itens | 1 valor | Agregar/acumular |

---

## Seção 4 - Expressões Regulares

### O Que São Regex?

Padrões para buscar/validar strings. Uma "mini-linguagem" dentro de Python.

```python
import re

words = ["Python", "Pantone", "Pontoon", "Pollute", "Pantheon"]

for word in words:
    # Padrão: começa com "P" e termina com "on"
    if re.search("^P.*on$", word):
        print(word, "encontrado!")

# Python encontrado!
# Pontoon encontrado!
# Pantheon encontrado!
```

### Funções Principais do Módulo re

| Função | Descrição |
|--------|-----------|
| `re.search(pattern, string)` | Retorna match ou None |
| `re.findall(pattern, string)` | Lista de todas as ocorrências |
| `re.match(pattern, string)` | Match apenas no início |
| `re.sub(pattern, repl, string)` | Substitui ocorrências |

### findall() Exemplo

```python
import re

sentence = "First, 2 !#third 44 five 678xyz962"

numbers = re.findall(r"\d+", sentence)
print(numbers)  # ['2', '44', '678', '962']
```

### Sintaxe de Regex

#### Alternativas (OR)

```python
# Matches "911" OU "112"
pattern = "911|112"

re.search("aa|ee|ii", "aardvark")  # Match!
re.search("aa|ee|ii", "feelings")  # Match!
re.search("aa|ee|ii", "smooch")    # No match
```

#### Classes de Caracteres

```python
# [aeio] = qualquer um desses caracteres
re.search("[aeio]", "hello")  # Match!

# [0-9] = dígitos de 0 a 9
re.search("[0-9]", "abc123")  # Match!

# [a-zA-Z] = letras maiúsculas e minúsculas
re.search("[a-zA-Z]", "123abc")  # Match!

# [0-68a-d] = 0-6, ou 8, ou a-d
```

#### Consecutivos

```python
# [1-3][0-9] = número de 10 a 39
re.search("[1-3][0-9]", "25")  # Match!
re.search("[1-3][0-9]", "42")  # No match
```

### Quantificadores

| Símbolo | Significado |
|---------|-------------|
| `*` | 0 ou mais vezes |
| `+` | 1 ou mais vezes |
| `?` | 0 ou 1 vez |
| `{m}` | Exatamente m vezes |
| `{m,n}` | De m a n vezes |

```python
# ba+b = "b", um ou mais "a", "b"
re.search("ba+b", "bab")      # Match!
re.search("ba+b", "baaaaab")  # Match!
re.search("ba+b", "bb")       # No match

# A[BCDE]*Z = "A", zero ou mais de BCDE, "Z"
re.search("A[BCDE]*Z", "AZ")        # Match!
re.search("A[BCDE]*Z", "ABCDEZ")    # Match!
```

### Caracteres Especiais

| Símbolo | Significado |
|---------|-------------|
| `.` | Qualquer caractere (exceto \n) |
| `^` | Início da string |
| `$` | Fim da string |
| `\d` | Dígito [0-9] |
| `\w` | Alfanumérico [a-zA-Z0-9_] |
| `\s` | Espaço em branco |
| `\` | Escape de caractere especial |

```python
# c...o = "c", 3 caracteres quaisquer, "o"
re.search("c...o", "c-3po")  # Match!
re.search("c...o", "cello")  # Match!

# ^[123]*$ = string contendo APENAS 1, 2, 3
re.search("^[123]*$", "1221")  # Match!
re.search("^[123]*$", "1234")  # No match (tem 4)

# 1\+ = literalmente "1+"
re.search(r"1\+", "1+2")  # Match!
```

### Grupos com Parênteses

```python
# (ab)+c = "ab" uma ou mais vezes, seguido de "c"
re.search("(ab)+c", "abc")       # Match!
re.search("(ab)+c", "ababc")     # Match!
re.search("(ab)+c", "ac")        # No match

# ^(jabba).*(hut)$ = começa com "jabba", termina com "hut"
re.search("^(jabba).*(hut)$", "jabba the hut")  # Match!
```

### Exemplos Práticos

```python
import re

# Validar email simples
def is_email(s):
    return bool(re.search(r"^[\w.]+@[\w.]+\.\w+$", s))

print(is_email("user@example.com"))  # True
print(is_email("invalid"))           # False

# Validar horário HH:MM:SS
def is_time(s):
    return bool(re.search(r"^[0-2][0-9]:[0-5][0-9]:[0-5][0-9]$", s))

print(is_time("12:43:01"))  # True
print(is_time("33:66:77"))  # False

# Extrair números de telefone
text = "Ligue para 555-1234 ou 555-5678"
phones = re.findall(r"\d{3}-\d{4}", text)
print(phones)  # ['555-1234', '555-5678']
```

### Tabela de Referência Rápida

| Padrão | Descrição | Exemplo |
|--------|-----------|---------|
| `abc` | Literal | "abc" |
| `a\|b` | a ou b | "cat\|dog" |
| `[abc]` | Um de a, b, c | "[aeiou]" |
| `[^abc]` | Não a, b, c | "[^0-9]" |
| `[a-z]` | Range | "[A-Za-z]" |
| `.` | Qualquer char | "c.t" |
| `^` | Início | "^Hello" |
| `$` | Fim | "bye$" |
| `*` | 0+ vezes | "ab*c" |
| `+` | 1+ vezes | "ab+c" |
| `?` | 0 ou 1 vez | "colou?r" |
| `{n}` | n vezes | "a{3}" |
| `\d` | Dígito | "\d+" |
| `\w` | Alfanum | "\w+" |
| `\s` | Espaço | "\s+" |
| `()` | Grupo | "(ab)+" |

---

## Conceitos-Chave

### Funções como Argumentos

| Conceito | Descrição |
|----------|-----------|
| `key=` | Função que define critério de ordenação |
| `lambda` | Função anônima inline |
| `callable` | Type hint para funções |

### Generators

| Conceito | Descrição |
|----------|-----------|
| `yield` | Retorna valor e pausa função |
| `next()` | Obtém próximo valor |
| `StopIteration` | Exceção quando esgota |
| Generator comprehension | `(expr for x in seq)` |

### Programação Funcional

| Função | Assinatura | Retorno |
|--------|------------|---------|
| `map` | `map(func, seq)` | Iterator transformado |
| `filter` | `filter(func, seq)` | Iterator filtrado |
| `reduce` | `reduce(func, seq, init)` | Valor único |

### Regex

| Função | Uso |
|--------|-----|
| `re.search()` | Busca padrão |
| `re.findall()` | Lista todas ocorrências |
| `re.match()` | Match no início |
| `re.sub()` | Substituição |

---

## Resumo Rápido

### Programa Exemplo: Processador de Dados com Funcional

```python
# =============================================================
# PROCESSADOR DE DADOS - Demonstração Parte 12
# =============================================================

import re
from functools import reduce

# ----- CLASSE DE DADOS -----
class Product:
    def __init__(self, name: str, price: float, stock: int, category: str):
        self.name = name
        self.price = price
        self.stock = stock
        self.category = category

    def __repr__(self):
        return f"{self.name} (R${self.price:.2f}, {self.stock}un)"


# ----- GENERATORS -----
def product_generator(data: list):
    """Generator que cria Products sob demanda"""
    for item in data:
        yield Product(
            item["name"],
            item["price"],
            item["stock"],
            item["category"]
        )


def infinite_ids():
    """Generator infinito de IDs"""
    id_num = 1
    while True:
        yield f"PROD-{id_num:04d}"
        id_num += 1


# ----- FUNÇÕES DE ORDENAÇÃO -----
def sort_by_price(products: list, descending: bool = False):
    """Ordena por preço usando key="""
    return sorted(products, key=lambda p: p.price, reverse=descending)


def sort_by_stock(products: list):
    """Ordena por estoque (menor primeiro)"""
    return sorted(products, key=lambda p: p.stock)


def sort_by_name(products: list):
    """Ordena alfabeticamente"""
    return sorted(products, key=lambda p: p.name.lower())


# ----- MAP, FILTER, REDUCE -----
def get_names(products: list) -> list:
    """Extrai nomes com map"""
    return list(map(lambda p: p.name, products))


def get_total_value(products: list) -> float:
    """Calcula valor total do estoque com map + reduce"""
    values = map(lambda p: p.price * p.stock, products)
    return reduce(lambda acc, v: acc + v, values, 0)


def filter_by_category(products: list, category: str) -> list:
    """Filtra por categoria"""
    return list(filter(lambda p: p.category == category, products))


def filter_low_stock(products: list, threshold: int = 10) -> list:
    """Filtra produtos com estoque baixo"""
    return list(filter(lambda p: p.stock < threshold, products))


def filter_by_price_range(products: list, min_price: float, max_price: float) -> list:
    """Filtra por faixa de preço"""
    return list(filter(
        lambda p: min_price <= p.price <= max_price,
        products
    ))


def get_average_price(products: list) -> float:
    """Calcula preço médio com filter + reduce"""
    if not products:
        return 0
    total = reduce(lambda acc, p: acc + p.price, products, 0)
    return total / len(products)


# ----- REGEX VALIDATION -----
def is_valid_product_code(code: str) -> bool:
    """Valida código: PROD-NNNN"""
    return bool(re.match(r"^PROD-\d{4}$", code))


def is_valid_email(email: str) -> bool:
    """Valida email básico"""
    pattern = r"^[\w.+-]+@[\w-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))


def extract_numbers(text: str) -> list:
    """Extrai todos os números de um texto"""
    return re.findall(r"\d+", text)


def clean_product_name(name: str) -> str:
    """Remove caracteres especiais do nome"""
    return re.sub(r"[^a-zA-Z0-9\s]", "", name)


# ----- PROCESSAMENTO COMBINADO -----
def process_expensive_electronics(products: list) -> dict:
    """
    Pipeline funcional:
    1. filter por categoria
    2. filter por preço
    3. map para extrair dados
    4. reduce para estatísticas
    """
    # Step 1: Filter electronics
    electronics = filter(lambda p: p.category == "Electronics", products)
    
    # Step 2: Filter expensive (> R$100)
    expensive = filter(lambda p: p.price > 100, electronics)
    
    # Convert to list (iterators são consumidos uma vez)
    expensive_list = list(expensive)
    
    if not expensive_list:
        return {"count": 0, "total": 0, "names": []}
    
    # Step 3: Map to get names
    names = list(map(lambda p: p.name, expensive_list))
    
    # Step 4: Reduce to get total
    total = reduce(lambda acc, p: acc + p.price, expensive_list, 0)
    
    return {
        "count": len(expensive_list),
        "total": total,
        "names": names
    }


# ----- DEMONSTRAÇÃO -----
if __name__ == "__main__":
    # Dados de exemplo
    raw_data = [
        {"name": "Laptop", "price": 2500.00, "stock": 15, "category": "Electronics"},
        {"name": "Mouse", "price": 89.90, "stock": 50, "category": "Electronics"},
        {"name": "Teclado", "price": 199.90, "stock": 8, "category": "Electronics"},
        {"name": "Cadeira", "price": 599.00, "stock": 5, "category": "Furniture"},
        {"name": "Mesa", "price": 450.00, "stock": 3, "category": "Furniture"},
        {"name": "Caneta", "price": 2.50, "stock": 200, "category": "Office"},
        {"name": "Papel A4", "price": 25.00, "stock": 100, "category": "Office"},
    ]
    
    # Criar produtos com generator
    products = list(product_generator(raw_data))
    
    print("=== ORDENAÇÃO ===")
    print("\nPor preço (crescente):")
    for p in sort_by_price(products)[:3]:
        print(f"  {p}")
    
    print("\nPor estoque (baixo primeiro):")
    for p in sort_by_stock(products)[:3]:
        print(f"  {p}")
    
    print("\n=== MAP ===")
    print("Nomes:", get_names(products))
    
    print("\n=== FILTER ===")
    print("Eletrônicos:")
    for p in filter_by_category(products, "Electronics"):
        print(f"  {p}")
    
    print("\nEstoque baixo (<10):")
    for p in filter_low_stock(products):
        print(f"  {p}")
    
    print("\n=== REDUCE ===")
    print(f"Valor total do estoque: R${get_total_value(products):,.2f}")
    print(f"Preço médio: R${get_average_price(products):.2f}")
    
    print("\n=== PIPELINE FUNCIONAL ===")
    result = process_expensive_electronics(products)
    print(f"Eletrônicos caros: {result['count']} produtos")
    print(f"Total: R${result['total']:,.2f}")
    print(f"Nomes: {result['names']}")
    
    print("\n=== GENERATORS ===")
    id_gen = infinite_ids()
    print("Primeiros 5 IDs:")
    for _ in range(5):
        print(f"  {next(id_gen)}")
    
    print("\n=== REGEX ===")
    print(f"PROD-0001 válido? {is_valid_product_code('PROD-0001')}")
    print(f"PROD-ABC válido? {is_valid_product_code('PROD-ABC')}")
    print(f"user@example.com válido? {is_valid_email('user@example.com')}")
    
    text = "Pedido 12345 com 3 itens no valor de R$150"
    print(f"Números em '{text}': {extract_numbers(text)}")
```

---

### Checklist de Conceitos

- [ ] Usar `key=` para ordenação customizada
- [ ] Criar lambda expressions
- [ ] Definir função dentro de outra função
- [ ] Criar generator com `yield`
- [ ] Usar `next()` com generators
- [ ] Criar generator comprehension `()`
- [ ] Usar `map()` para transformar dados
- [ ] Usar `filter()` para selecionar dados
- [ ] Usar `reduce()` para agregar dados
- [ ] Importar `reduce` de `functools`
- [ ] Escrever regex básico
- [ ] Usar `re.search()` e `re.findall()`
- [ ] Validar strings com regex

---

### Armadilhas Comuns

| Armadilha | Problema | Solução |
|-----------|----------|---------|
| Iterator esgotado | map/filter só iteram uma vez | Converter para `list()` |
| Esquecer `import re` | NameError | Importar no início |
| Regex sem raw string | `\d` interpretado errado | Usar `r"\d"` |
| reduce sem valor inicial | Erro se tipos diferentes | Sempre passar 3º argumento |
| Generator em for infinito | Loop eterno | Adicionar condição de parada |
| Lambda complexa demais | Difícil de ler | Usar função nomeada |

---

### Padrões de Design

```python
# 1. ORDENAÇÃO COM LAMBDA
sorted(lista, key=lambda x: x.atributo)
sorted(lista, key=lambda x: x.atributo, reverse=True)

# 2. GENERATOR SIMPLES
def meu_generator(n):
    for i in range(n):
        yield i * 2

# 3. GENERATOR COMPREHENSION
gen = (x**2 for x in range(10))

# 4. MAP PATTERN
nomes = list(map(lambda obj: obj.nome, objetos))

# 5. FILTER PATTERN
ativos = list(filter(lambda obj: obj.ativo, objetos))

# 6. REDUCE PATTERN
from functools import reduce
total = reduce(lambda acc, x: acc + x.valor, objetos, 0)

# 7. PIPELINE FUNCIONAL
resultado = reduce(
    agregar,
    filter(filtrar, map(transformar, dados)),
    valor_inicial
)

# 8. REGEX VALIDATION
import re
valido = bool(re.match(r"^padrão$", string))

# 9. REGEX EXTRACTION
matches = re.findall(r"padrão", string)
```

---

## Próximos Passos

Na **Parte 13** você aprenderá:

- Pygame e gráficos
- Animações
- Eventos e interação
- Jogos simples

---

**Fonte:** University of Helsinki MOOC - Python Programming  
**Resumo criado por:** Claude (Anthropic)  
**Para:** Eric Alcalai França
