# Parte 5 - Estruturas de Dados Avançadas

**Curso:** Python Programming - University of Helsinki MOOC  
**Resumo criado por:** Claude (Anthropic)  
**Para:** Eric Alcalai França

---

## Índice

1. [[#Seção 1 - More Lists]]
2. [[#Seção 2 - References]]
3. [[#Seção 3 - Dictionary]]
4. [[#Seção 4 - Tuple]]
5. [[#Conceitos-Chave]]
6. [[#Resumo Rápido]]

---

## Seção 1 - More Lists

### Listas com Diferentes Tipos de Dados

Listas podem armazenar qualquer tipo de valor, não apenas inteiros.

**Lista de strings:**

```python
# Lista de nomes
names = ["Marlyn", "Ruth", "Paul"]
names.append("David")
names.sort()

for name in names:
    print(name)
# David
# Marlyn
# Paul
# Ruth
```

**Lista de floats:**

```python
# Medições de temperatura
measurements = [-2.5, 1.1, 7.5, 14.6, 21.0, 19.2]

# Calcular média
mean = sum(measurements) / len(measurements)
print("A média é:", mean)  # 10.15
```

### ⚠️ Evitar Variáveis Globais em Funções

Usar variáveis globais dentro de funções pode causar bugs difíceis de rastrear.

**Exemplo problemático:**

```python
def print_reversed(names: list):
    # ERRO: usando variável global em vez do parâmetro
    i = len(name_list) - 1
    while i >= 0:
        print(name_list[i])  # sempre usa global!
        i -= 1

name_list = ["Steve", "Jean", "Katherine"]
print_reversed(["Huey", "Dewey", "Louie"])
# Imprime Steve, Jean, Katherine (ERRADO!)
```

**Solução:**

```python
def print_reversed(names: list):
    # Usar apenas o parâmetro
    i = len(names) - 1
    while i >= 0:
        print(names[i])
        i -= 1
```

### ⚠️ Armadilha: Sobrescrever Parâmetros

**Problema 1: Variável de loop sobrescreve parâmetro**

```python
def number_in_list(numbers: list, number: int):
    for number in numbers:  # ❌ Sobrescreve parâmetro!
        if number == number:  # Sempre True
            return True
```

**Solução: Renomear variável do loop**

```python
def number_in_list(numbers: list, searched_number: int):
    for number in numbers:
        if number == searched_number:
            return True
    return False
```

**Problema 2: Retornar muito cedo**

```python
def number_in_list(numbers: list, searched_number: int):
    for number in numbers:
        if number == searched_number:
            return True
        else:
            return False  # ❌ Retorna após 1º item!
```

**Solução: Retornar False APÓS o loop**

```python
def number_in_list(numbers: list, searched_number: int):
    for number in numbers:
        if number == searched_number:
            return True
    
    return False  # ✅ Só depois de verificar todos
```

### Listas Dentro de Listas

Listas podem conter outras listas como elementos.

```python
my_list = [[5, 2, 3], [4, 1], [2, 2, 5, 1]]

print(my_list)        # [[5, 2, 3], [4, 1], [2, 2, 5, 1]]
print(my_list[1])     # [4, 1]
print(my_list[1][0])  # 4
```

**Banco de dados de pessoas (lista de listas):**

```python
persons = [
    ["Betty", 10, 1.37],
    ["Peter", 7, 1.25],
    ["Emily", 32, 1.64]
]

for person in persons:
    name = person[0]
    age = person[1]
    height = person[2]
    print(f"{name}: {age} anos, {height} metros")
```

### Matrizes (Arrays Bidimensionais)

Uma matriz é uma lista de listas, ideal para representar tabelas ou grades.

```python
# Matriz 3x3:
# 1 2 3
# 3 2 1
# 4 5 6

my_matrix = [
    [1, 2, 3],
    [3, 2, 1],
    [4, 5, 6]
]

# Acessar elementos: [linha][coluna]
print(my_matrix[0][1])  # 2 (linha 0, coluna 1)

# Modificar elemento
my_matrix[1][0] = 10
print(my_matrix)  # [[1, 2, 3], [10, 2, 1], [4, 5, 6]]
```

**Percorrer matriz (imprimir cada linha):**

```python
my_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row in my_matrix:
    print(row)
# [1, 2, 3]
# [4, 5, 6]
# [7, 8, 9]
```

**Percorrer cada elemento individualmente:**

```python
for row in my_matrix:
    for element in row:
        print(element)
# 1
# 2
# 3
# 4
# ...
```

### Operações com Matrizes

**Soma de uma linha:**

```python
def sum_of_row(my_matrix, row_no: int):
    # Escolher a linha desejada
    row = my_matrix[row_no]
    return sum(row)

m = [[4, 2, 3, 2], [9, 1, 12, 11]]
print(sum_of_row(m, 1))  # 33 (9+1+12+11)
```

**Soma de uma coluna:**

```python
def sum_of_column(my_matrix, column_no: int):
    column_sum = 0
    for row in my_matrix:
        column_sum += row[column_no]
    return column_sum

m = [[4, 2, 3, 2], [9, 1, 12, 11]]
print(sum_of_column(m, 2))  # 15 (3+12)
```

**Modificar valor específico:**

```python
def change_value(my_matrix, row_no: int, column_no: int, new_value: int):
    my_matrix[row_no][column_no] = new_value

m = [[4, 2, 3], [9, 1, 12]]
change_value(m, 1, 2, 1000)
print(m)  # [[4, 2, 3], [9, 1, 1000]]
```

**Incrementar todos os elementos (usando índices):**

```python
m = [[1, 2, 3], [4, 5, 6]]

for i in range(len(m)):           # Para cada linha
    for j in range(len(m[i])):    # Para cada coluna
        m[i][j] += 1

print(m)  # [[2, 3, 4], [5, 6, 7]]
```

⚠️ **Importante:** Para modificar elementos, precisamos usar índices. Um `for item in list` não funciona porque cria cópias.

### Matrizes em Jogos

Exemplo: grade de Sudoku (9x9, onde 0 = vazio)

```python
sudoku = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [0, 0, 0, 2, 5, 0, 7, 0, 0],
    # ... 7 linhas adicionais
]

def print_grid(sudoku):
    for row in sudoku:
        for square in row:
            if square > 0:
                print(f" {square}", end="")
            else:
                print(" _", end="")
        print()  # Nova linha

print_grid(sudoku)
#  9 _ _ _ 8 _ 3 _ _
#  _ _ _ 2 5 _ 7 _ _
#  ...
```

---

## Seção 2 - References

### O Que São Referências?

Em Python, uma variável não armazena o valor em si, mas uma **referência** (endereço na memória) que aponta para o objeto.

```python
a = [1, 2, 3]
print(id(a))  # 4538357072 (endereço na memória)

b = "Isso também é referência"
print(id(b))  # 4537788912
```

**Visualização:**

```
a  ────►  [1, 2, 3]
          (memória)
```

### Imutabilidade vs Mutabilidade

**Tipos imutáveis:** `int`, `float`, `bool`, `str`, `tuple`
- Não podem ser modificados
- Cada nova atribuição cria novo objeto

```python
number = 1
print(id(number))  # 4535856912

number = 2
print(id(number))  # 4535856944 (DIFERENTE!)

a = 1
print(id(a))       # 4535856912 (IGUAL ao primeiro!)
```

Python reutiliza o objeto `1` na memória. Quando `number = 2`, `number` aponta para um novo objeto.

**Tipos mutáveis:** `list`, `dict`, `set`
- Podem ser modificados diretamente

```python
my_list = [1, 2, 3]
my_list[0] = 10  # Modifica o MESMO objeto
print(id(my_list))  # ID não muda
```

### Múltiplas Referências à Mesma Lista

Atribuir uma lista a outra variável **copia a referência**, não a lista.

```python
a = [1, 2, 3]
b = a  # b aponta para a MESMA lista

b[0] = 10
print(a)  # [10, 2, 3]  ← também mudou!
print(b)  # [10, 2, 3]
```

**Visualização:**

```
a  ────►
         [1, 2, 3]
b  ────►
```

Ambas apontam para a mesma lista na memória!

### Copiando Listas

**Método 1: Loop explícito**

```python
my_list = [1, 2, 3, 3, 5]

new_list = []
for item in my_list:
    new_list.append(item)

new_list[0] = 10
print(my_list)   # [1, 2, 3, 3, 5]   (original intacta)
print(new_list)  # [10, 2, 3, 3, 5]  (cópia modificada)
```

**Método 2: Operador de slice `[:]`**

```python
my_list = [1, 2, 3, 4]
new_list = my_list[:]  # Cria cópia

my_list[0] = 10
new_list[1] = 20

print(my_list)   # [10, 2, 3, 4]
print(new_list)  # [1, 20, 3, 4]
```

### Listas Como Parâmetros de Funções

Quando você passa uma lista para uma função, passa a **referência**. A função pode modificar a lista original.

```python
def add_item(my_list: list):
    my_list.append(10)

a_list = [1, 2, 3]
add_item(a_list)
print(a_list)  # [1, 2, 3, 10] ← modificada!
```

**Alternativa: Retornar nova lista**

```python
def add_item(my_list: list) -> list:
    my_list_copy = my_list[:]  # Cópia
    my_list_copy.append(10)
    return my_list_copy

numbers = [1, 2, 3]
numbers2 = add_item(numbers)

print("original:", numbers)   # [1, 2, 3]
print("nova:", numbers2)      # [1, 2, 3, 10]
```

### ⚠️ Armadilha: Reatribuir Parâmetro Não Afeta Original

```python
def augment_all(my_list: list):
    new_list = []
    for item in my_list:
        new_list.append(item + 10)
    
    my_list = new_list  # ❌ Reatribui apenas localmente!

numbers = [1, 2, 3]
augment_all(numbers)
print(numbers)  # [1, 2, 3] ← não mudou!
```

**Por quê?** `my_list = new_list` faz `my_list` apontar para a nova lista, mas a variável `numbers` na função principal ainda aponta para a lista original.

**Solução 1: Copiar item por item**

```python
def augment_all(my_list: list):
    new_list = []
    for item in my_list:
        new_list.append(item + 10)
    
    # Copiar valores de volta
    for i in range(len(my_list)):
        my_list[i] = new_list[i]
```

**Solução 2: Usar slice assignment**

```python
def augment_all(my_list: list):
    new_list = []
    for item in my_list:
        new_list.append(item + 10)
    
    my_list[:] = new_list  # ✅ Substitui conteúdo
```

**Solução 3: Modificar diretamente**

```python
def augment_all(my_list: list):
    for i in range(len(my_list)):
        my_list[i] += 10
```

### Efeitos Colaterais (Side Effects)

Um efeito colateral ocorre quando uma função modifica objetos acessados por referência de forma não intencional.

**Exemplo problemático:**

```python
def second_smallest(my_list: list) -> int:
    my_list.sort()  # ❌ Ordena a lista original!
    return my_list[1]

numbers = [1, 4, 2, 5, 3]
print(second_smallest(numbers))  # 2
print(numbers)  # [1, 2, 3, 4, 5] ← foi ordenada!
```

**Solução: Usar `sorted()` que retorna cópia**

```python
def second_smallest(my_list: list) -> int:
    list_copy = sorted(my_list)  # ✅ Nova lista ordenada
    return list_copy[1]

numbers = [1, 4, 2, 5, 3]
print(second_smallest(numbers))  # 2
print(numbers)  # [1, 4, 2, 5, 3] ← intacta!
```

**Boas práticas:**
- Evite efeitos colaterais sempre que possível
- Funções "puras" (sem side effects) são mais previsíveis
- Documente claramente se a função modifica seus argumentos

---

## Seção 3 - Dictionary

### O Que É um Dicionário?

Um dicionário armazena pares **chave-valor**. Ao contrário de listas (índices numéricos), dicionários usam chaves para acessar valores.

```python
# Criar dicionário vazio
my_dictionary = {}

# Adicionar pares chave-valor
my_dictionary["apina"] = "monkey"
my_dictionary["banaani"] = "banana"
my_dictionary["cembalo"] = "harpsichord"

print(len(my_dictionary))  # 3
print(my_dictionary["apina"])  # monkey
```

**Verificar se chave existe:**

```python
word = input("Digite uma palavra: ")
if word in my_dictionary:
    print("Tradução:", my_dictionary[word])
else:
    print("Palavra não encontrada")
```

### Tipos de Dados em Dicionários

**Chaves:** Qualquer tipo **imutável** (str, int, float, tuple)  
**Valores:** Qualquer tipo (incluindo listas, dicionários)

```python
# Chaves = strings, Valores = inteiros
results = {}
results["Mary"] = 4
results["Alice"] = 5

# Chaves = inteiros, Valores = listas
lists = {}
lists[5] = [1, 2, 3]
lists[42] = [5, 4, 5, 4, 5]
```

⚠️ **Listas NÃO podem ser chaves:**

```python
my_dict[[1, 2, 3]] = 5  # ❌ TypeError: unhashable type: 'list'
```

**Por quê?** Dicionários usam **hash tables** internamente. Cada chave é convertida em um hash (número). Listas são mutáveis e não podem ser hasheadas.

### Comportamento de Chaves

**Sobrescrever valores:**

```python
my_dict["palavra"] = "grande"
my_dict["palavra"] = "enorme"  # Sobrescreve
print(my_dict["palavra"])  # enorme
```

**Cada chave aparece apenas uma vez**, mas múltiplas chaves podem ter o mesmo valor.

### Percorrer Dicionários

**Método 1: Percorrer chaves**

```python
my_dict = {"apina": "monkey", "banaani": "banana"}

for key in my_dict:
    print("chave:", key)
    print("valor:", my_dict[key])
```

**Método 2: Usar `items()` para pares chave-valor**

```python
for key, value in my_dict.items():
    print("chave:", key)
    print("valor:", value)
```

### Casos de Uso Comuns

**Contar ocorrências:**

```python
def counts(my_list):
    words = {}
    for word in my_list:
        if word not in words:
            words[word] = 0
        words[word] += 1
    return words

word_list = ["banana", "milk", "beer", "cheese", "beer", "beer"]
print(counts(word_list))
# {'banana': 1, 'milk': 1, 'beer': 3, 'cheese': 1}
```

**Categorizar por inicial:**

```python
def categorize_by_initial(my_list):
    groups = {}
    for word in my_list:
        initial = word[0]
        if initial not in groups:
            groups[initial] = []  # Criar lista vazia
        groups[initial].append(word)
    return groups

words = ["banana", "milk", "beer", "cheese"]
groups = categorize_by_initial(words)

for key, value in groups.items():
    print(f"palavras com {key}:")
    for word in value:
        print(word)
# palavras com b:
# banana
# beer
# ...
```

### Remover Itens de Dicionários

**Método 1: `del`**

```python
staff = {"Alan": "lecturer", "Emily": "professor"}
del staff["Alan"]
print(staff)  # {'Emily': 'professor'}
```

⚠️ **Erro se chave não existe:**

```python
del staff["Paul"]  # KeyError: 'Paul'
```

**Solução: Verificar antes**

```python
if "Paul" in staff:
    del staff["Paul"]
else:
    print("Pessoa não encontrada")
```

**Método 2: `pop()`**

```python
staff = {"Alan": "lecturer", "Emily": "professor"}
deleted = staff.pop("Alan")
print(staff)    # {'Emily': 'professor'}
print(deleted)  # lecturer
```

**Pop com valor padrão (evita erro):**

```python
deleted = staff.pop("Paul", None)
if deleted == None:
    print("Pessoa não encontrada")
```

**Limpar dicionário inteiro:**

```python
staff.clear()  # Remove todos os itens
```

### Dados Estruturados com Dicionários

Dicionários são ótimos para organizar informações relacionadas.

```python
# Uma pessoa
person = {
    "name": "Pippa Python",
    "height": 154,
    "weight": 61,
    "age": 44
}

print(person["name"])  # Pippa Python
```

**Lista de pessoas:**

```python
person1 = {"name": "Pippa", "height": 154, "age": 44}
person2 = {"name": "Peter", "height": 174, "age": 31}
people = [person1, person2]

for person in people:
    print(person["name"])

# Média de altura
total_height = sum(p["height"] for p in people)
print("Média:", total_height / len(people))
```

**Banco de dados de filmes:**

```python
def add_movie(database: list, name: str, director: str, year: int, runtime: int):
    movie = {
        "name": name,
        "director": director,
        "year": year,
        "runtime": runtime
    }
    database.append(movie)

movies = []
add_movie(movies, "Gone with Python", "Victor Pything", 2017, 116)
```

---

## Seção 4 - Tuple

### O Que É uma Tupla?

Uma tupla é similar a uma lista, mas **imutável** (não pode ser modificada após criação).

**Diferenças principais:**

| Lista | Tupla |
|-------|-------|
| `[1, 2, 3]` | `(1, 2, 3)` |
| Mutável | Imutável |
| Colchetes `[]` | Parênteses `()` |

```python
# Criar tupla
point = (10, 20)

# Acessar por índice
print(point[0])  # 10
print(point[1])  # 20

# Tentar modificar → ERRO
point[0] = 15  # TypeError: 'tuple' object does not support item assignment
```

### Por Que Usar Tuplas?

**1. Dados relacionados e fixos**

Coordenadas (x, y) são sempre 2 valores:

```python
point = (10, 20)  # ✅ Tupla faz sentido
```

**2. Como chaves de dicionário**

Tuplas (imutáveis) podem ser chaves; listas não.

```python
points = {}
points[(3, 5)] = "monkey"
points[(5, 0)] = "banana"
print(points[(3, 5)])  # monkey

# Listas NÃO funcionam
points[[3, 5]] = "erro"  # TypeError: unhashable type: 'list'
```

**3. Retornar múltiplos valores**

```python
def minmax(my_list):
    return min(my_list), max(my_list)  # Retorna tupla

my_list = [33, 5, 21, 88]
min_value, max_value = minmax(my_list)
print(f"Min: {min_value}, Max: {max_value}")
# Min: 5, Max: 88
```

### Tuplas Sem Parênteses

Parênteses são opcionais em muitos contextos:

```python
numbers = 1, 2, 3  # Equivalente a (1, 2, 3)
```

**Desempacotamento:**

```python
min_value, max_value = minmax(my_list)
# Equivalente a:
(min_value, max_value) = minmax(my_list)
```

**Trocar valores de variáveis:**

```python
# Sem tupla (usando variável auxiliar)
temp = a
a = b
b = temp

# Com tupla (elegante)
a, b = b, a  # Troca valores diretamente!
```

### Tuplas com `items()`

O método `items()` de dicionários retorna tuplas (chave, valor):

```python
my_dict = {"apina": "monkey", "banaani": "banana"}

for key, value in my_dict.items():
    print("chave:", key)
    print("valor:", value)
```

Internamente, `items()` retorna:

```python
[("apina", "monkey"), ("banaani", "banana")]
```

### Exemplos Práticos

**Pessoa mais velha:**

```python
def oldest_person(people: list):
    oldest = people[0]  # Começa com primeira pessoa
    for person in people:
        if person[1] < oldest[1]:  # person[1] = ano nascimento
            oldest = person
    return oldest[0]  # Retorna nome

p1 = ("Adam", 1977)
p2 = ("Mary", 1953)
people = [p1, p2]
print(oldest_person(people))  # Mary
```

**Filtrar por ano:**

```python
def older_people(people: list, year: int):
    result = []
    for person in people:
        if person[1] < year:  # Nasceu antes do ano
            result.append(person[0])  # Adiciona nome
    return result

older = older_people(people, 1979)
print(older)  # ['Adam', 'Mary']
```

---

## Conceitos-Chave

### Tabela de Métodos - Listas

| Método | Função | Retorno |
|--------|--------|---------|
| `list.append(x)` | Adiciona item ao final | None (modifica in-place) |
| `list.insert(i, x)` | Insere item na posição i | None |
| `list.pop()` | Remove e retorna último item | Item removido |
| `list.pop(i)` | Remove e retorna item na posição i | Item removido |
| `list.remove(x)` | Remove primeira ocorrência de x | None |
| `list.sort()` | Ordena lista in-place | None |
| `sorted(list)` | Retorna nova lista ordenada | Nova lista |
| `list.clear()` | Remove todos os itens | None |
| `list[:]` | Cria cópia rasa da lista | Nova lista |

### Tabela de Métodos - Dicionários

| Método | Função | Retorno |
|--------|--------|---------|
| `dict[key]` | Acessa valor da chave | Valor (erro se não existe) |
| `dict[key] = value` | Atribui/sobrescreve valor | None |
| `key in dict` | Verifica se chave existe | True/False |
| `dict.items()` | Retorna pares (chave, valor) | Iterável de tuplas |
| `dict.keys()` | Retorna todas as chaves | Iterável de chaves |
| `dict.values()` | Retorna todos os valores | Iterável de valores |
| `dict.pop(key)` | Remove chave e retorna valor | Valor removido |
| `dict.pop(key, default)` | Pop com valor padrão | Valor ou default |
| `del dict[key]` | Remove chave | None (erro se não existe) |
| `dict.clear()` | Remove todos os itens | None |

### Comparação: Lista vs Tupla vs Dicionário

| Característica | Lista | Tupla | Dicionário |
|----------------|-------|-------|------------|
| Sintaxe | `[1, 2, 3]` | `(1, 2, 3)` | `{"a": 1, "b": 2}` |
| Mutável? | Sim | Não | Sim |
| Ordenado? | Sim (por índice) | Sim (por índice) | Sim (ordem de inserção)* |
| Acesso | Por índice numérico | Por índice numérico | Por chave (qualquer tipo imutável) |
| Pode ser chave? | Não | Sim | Não |
| Uso típico | Coleção ordenada modificável | Dados fixos relacionados | Mapeamento chave-valor |

\* Em Python 3.7+

### Mutabilidade

**Imutável (não pode mudar):**
- `int`, `float`, `bool`, `str`, `tuple`
- Reatribuir variável cria novo objeto

**Mutável (pode mudar):**
- `list`, `dict`, `set`
- Modificações alteram o mesmo objeto

### Referências - Regras Importantes

1. **Atribuir lista = copiar referência**
   ```python
   a = [1, 2]
   b = a  # b aponta para MESMA lista
   ```

2. **Para copiar lista:**
   ```python
   b = a[:]  # ou b = a.copy()
   ```

3. **Parâmetros de função = referências**
   ```python
   def modify(lst):
       lst.append(10)  # Modifica original!
   ```

4. **Evitar efeitos colaterais:**
   - Use `sorted()` em vez de `sort()`
   - Retorne nova lista ou documente modificação

---

## Resumo Rápido

### Programa Exemplo - Banco de Dados de Estudantes

```python
def main():
    # Dicionário de estudantes (chave = nome, valor = dict com cursos)
    students = {}
    
    # Adicionar estudante
    add_student(students, "Peter")
    
    # Adicionar curso (tupla com nome e nota)
    add_course(students, "Peter", ("Programming", 3))
    add_course(students, "Peter", ("Algorithms", 2))
    
    # Imprimir informações
    print_student(students, "Peter")
    # Peter:
    #  2 completed courses:
    #   Programming 3
    #   Algorithms 2
    #  average grade 2.5

def add_student(database: dict, name: str):
    database[name] = []  # Lista vazia de cursos

def add_course(database: dict, name: str, course: tuple):
    # course = (nome_curso, nota)
    if name in database:
        # Verificar se curso já existe
        for completed in database[name]:
            if completed[0] == course[0]:  # Mesmo curso
                # Só atualiza se nota maior
                if course[1] > completed[1]:
                    database[name].remove(completed)
                    database[name].append(course)
                return
        # Curso novo
        if course[1] > 0:  # Ignora nota 0
            database[name].append(course)

def print_student(database: dict, name: str):
    if name not in database:
        print(f"{name}: não encontrado")
        return
    
    courses = database[name]
    print(f"{name}:")
    
    if len(courses) == 0:
        print(" nenhum curso completo")
    else:
        print(f" {len(courses)} cursos completos:")
        for course in courses:
            print(f"  {course[0]} {course[1]}")
        
        # Calcular média
        total = sum(course[1] for course in courses)
        avg = total / len(courses)
        print(f" média {avg:.1f}")

if __name__ == "__main__":
    main()
```

### Checklist de Conceitos

**Listas:**
- [ ] Sei criar listas com diferentes tipos
- [ ] Sei trabalhar com matrizes (listas 2D)
- [ ] Sei acessar elementos com `[linha][coluna]`
- [ ] Sei usar loops aninhados para percorrer matrizes
- [ ] Evito sobrescrever parâmetros em funções
- [ ] Evito retornar muito cedo em buscas

**Referências:**
- [ ] Entendo que variáveis armazenam referências
- [ ] Sei a diferença entre mutável e imutável
- [ ] Sei quando usar `list[:]` para copiar
- [ ] Entendo que funções podem modificar listas
- [ ] Sei evitar efeitos colaterais indesejados
- [ ] Uso `sorted()` em vez de `sort()` quando apropriado

**Dicionários:**
- [ ] Sei criar e usar dicionários
- [ ] Entendo pares chave-valor
- [ ] Sei que chaves devem ser imutáveis
- [ ] Sei usar `in` para verificar chaves
- [ ] Sei percorrer com `items()`, `keys()`, `values()`
- [ ] Sei usar `pop()` e `del` para remover itens
- [ ] Sei quando usar dict vs list para dados estruturados

**Tuplas:**
- [ ] Sei criar tuplas com `()`
- [ ] Entendo que tuplas são imutáveis
- [ ] Sei quando usar tupla vs lista
- [ ] Sei usar tuplas como chaves de dicionário
- [ ] Sei retornar múltiplos valores com tuplas
- [ ] Sei trocar valores com `a, b = b, a`

### Armadilhas Comuns

| Erro | Problema | Solução |
|------|----------|---------|
| `for num in numbers: num += 10` | Loop não modifica lista | Usar índices: `for i in range(len(numbers))` |
| `b = a` (lista) | Copia referência, não lista | `b = a[:]` |
| `def func(lst): lst = [1,2,3]` | Reatribuir não afeta original | Modificar in-place: `lst[:] = [1,2,3]` |
| `my_dict[key]` | KeyError se não existe | Usar `key in my_dict` antes |
| `my_dict[[1,2]]` | Lista como chave | Usar tupla: `my_dict[(1,2)]` |
| `for key in dict: del dict[key]` | Modifica durante iteração | `dict.clear()` ou iterar sobre `list(dict.keys())` |
| `point[0] = 10` (tupla) | Tupla imutável | Criar nova tupla |
| Usar variável global em função | Coupling, bugs difíceis | Usar apenas parâmetros |

### Quando Usar Cada Estrutura?

**Use Lista quando:**
- Ordem importa
- Precisa modificar coleção
- Acesso por posição (índice numérico)
- Ex: histórico de ações, fila de tarefas

**Use Tupla quando:**
- Dados fixos e relacionados
- Quer garantir imutabilidade
- Precisa usar como chave de dict
- Ex: coordenadas (x, y), data (ano, mês, dia)

**Use Dicionário quando:**
- Acesso por chave nomeada
- Relação chave-valor
- Busca rápida por identificador
- Ex: contadores, banco de dados, configurações

**Use Matriz (lista 2D) quando:**
- Dados em grade/tabela
- Jogos de tabuleiro
- Ex: sudoku, imagens, planilhas

---

## Próximos Passos

Na **Parte 6** você aprenderá:

- Leitura e escrita de arquivos
- Tratamento de exceções
- Manipulação de dados CSV

---

**Fonte:** University of Helsinki MOOC - Python Programming  
**Resumo criado por:** Claude (Anthropic)  
**Para:** Eric Alcalai França
