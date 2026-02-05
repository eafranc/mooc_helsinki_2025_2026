# Parte 11 - Comprehensions e Recursão

> **Fonte:** University of Helsinki - Python Programming MOOC
> **Resumo criado por:** Claude (Anthropic)
> **Para:** Eric Alcalai França

---

## Índice

- [[#Seção 1 - List Comprehensions]]
- [[#Seção 2 - Mais Sobre Comprehensions]]
- [[#Seção 3 - Recursão]]
- [[#Seção 4 - Mais Exemplos de Recursão]]
- [[#Conceitos-Chave]]
- [[#Resumo Rápido]]

---

## Seção 1 - List Comprehensions

### O Problema: Código Repetitivo

Frequentemente precisamos criar uma nova lista processando cada item de uma lista existente:

```python
# ❌ Abordagem tradicional - verbosa
numbers = [1, 2, 3, 6, 5, 4, 7]

strings = []
for number in numbers:
    strings.append(str(number))

print(strings)  # ['1', '2', '3', '6', '5', '4', '7']
```

### Solução: List Comprehension

Uma forma "pythonica" de criar listas a partir de outras:

```python
# ✅ List comprehension - conciso
numbers = [1, 2, 3, 6, 5, 4, 7]
strings = [str(number) for number in numbers]

print(strings)  # ['1', '2', '3', '6', '5', '4', '7']
```

### Sintaxe Geral

```python
[<expressão> for <item> in <série>]
```

| Parte | Descrição |
|-------|-----------|
| `[ ]` | Indica que o resultado é uma lista |
| `<expressão>` | O que fazer com cada item |
| `for <item> in <série>` | Iteração sobre a série original |

### Exemplos Básicos

```python
# Multiplicar por 10
numbers = list(range(1, 10))
multiplied = [number * 10 for number in numbers]
print(multiplied)  # [10, 20, 30, 40, 50, 60, 70, 80, 90]

# Chamar função personalizada
def factorial(n: int):
    k = 1
    while n >= 2:
        k *= n
        n -= 1
    return k

numbers = [5, 2, 4, 3, 0]
factorials = [factorial(number) for number in numbers]
print(factorials)  # [120, 2, 24, 6, 1]

# Retornar comprehension diretamente de função
def factorials(numbers: list):
    return [factorial(number) for number in numbers]
```

### Filtrando Itens com if

Adicione uma condição para selecionar apenas certos itens:

```python
[<expressão> for <item> in <série> if <condição booleana>]
```

```python
# Filtrar apenas números pares
numbers = [1, 1, 2, 3, 4, 6, 4, 5, 7, 10, 12, 3]
even_items = [item for item in numbers if item % 2 == 0]
print(even_items)  # [2, 4, 6, 4, 10, 12]

# Filtrar E processar
even_times_ten = [item * 10 for item in numbers if item % 2 == 0]
print(even_times_ten)  # [20, 40, 60, 40, 100, 120]

# Filtrar antes de processar (evita erros)
numbers = [-2, 3, -1, 4, -10, 5, 1]
# factorial só funciona para n >= 0
factorials = [factorial(n) for n in numbers if n >= 0]
print(factorials)  # [6, 24, 120, 1]
```

### Criando Tuplas na Comprehension

```python
numbers = [-2, 3, 2, 1, 4, -10, 5, 1, 6]

# Criar tupla (número, fatorial) para positivos pares
factorials = [(n, factorial(n)) for n in numbers if n > 0 and n % 2 == 0]
print(factorials)  # [(2, 2), (4, 24), (6, 720)]
```

### if-else (Operador Ternário)

Quando você quer processar TODOS os itens de formas diferentes:

```python
# ATENÇÃO: sintaxe diferente! if-else vem ANTES do for
[<expressão1> if <condição> else <expressão2> for <item> in <série>]
```

```python
# Valor absoluto: se positivo mantém, se negativo inverte o sinal
numbers = [1, -3, 45, -110, 2, 9, -11]
abs_vals = [number if number >= 0 else -number for number in numbers]
print(abs_vals)  # [1, 3, 45, 110, 2, 9, 11]

# Processar strings, ignorar outros tipos
def string_lengths(my_list: list):
    return [len(item) if type(item) == str else -1 for item in my_list]

test = ["hi", 3, True, "there", -123.344, "toodlepip", 2, False]
print(string_lengths(test))  # [2, -1, -1, 5, -1, 9, -1, -1]
```

### Comparação: if vs if-else

| Situação | Sintaxe | Resultado |
|----------|---------|-----------|
| **Apenas if** (filtrar) | `[x for x in lista if cond]` | Lista menor (só itens que passam) |
| **if-else** (processar todos) | `[a if cond else b for x in lista]` | Lista mesmo tamanho |

```python
numbers = [1, 2, 3, 4, 5]

# Apenas if: FILTRA (lista menor)
pares = [n for n in numbers if n % 2 == 0]
print(pares)  # [2, 4]

# if-else: PROCESSA TODOS (lista mesmo tamanho)
resultado = [n * 2 if n % 2 == 0 else n for n in numbers]
print(resultado)  # [1, 4, 3, 8, 5]
```

---

## Seção 2 - Mais Sobre Comprehensions

### Comprehensions com Strings

Strings são iteráveis, então funcionam com comprehensions:

```python
name = "Peter Python"

# Resultado é uma LISTA de caracteres
uppercased = [char.upper() for char in name]
print(uppercased)  # ['P', 'E', 'T', 'E', 'R', ' ', 'P', 'Y', 'T', 'H', 'O', 'N']
```

### Convertendo Lista para String: join()

```python
name = "Peter"
char_list = list(name)
print(char_list)  # ['P', 'e', 't', 'e', 'r']

# join() une a lista usando a string como "cola"
print("".join(char_list))      # Peter
print(" ".join(char_list))     # P e t e r
print(",".join(char_list))     # P,e,t,e,r
print(" and ".join(char_list)) # P and e and t and e and r
```

### Combinando Comprehension + join()

```python
# Extrair apenas vogais de uma string
test_string = "Hello there, this is a test!"

vowels = [char for char in test_string if char in "aeiou"]
vowel_string = "".join(vowels)
print(vowel_string)  # eoeeiiae

# Tudo em uma linha
vowel_string = "".join([char for char in test_string if char in "aeiou"])
```

### Processando Sentenças

```python
# Remover primeira letra de cada palavra
sentence = "Sheila keeps on selling seashells on the seashore"

# split() → comprehension → join()
result = " ".join([word[1:] for word in sentence.split()])
print(result)  # heila eeps n elling eashells n he eashore
```

**Passo a passo:**
1. `sentence.split()` → divide em palavras
2. `word[1:]` → extrai substring do índice 1 em diante
3. `" ".join()` → une as palavras com espaço

### Comprehensions com Classes Próprias

```python
class Country:
    def __init__(self, name: str, population: int):
        self.name = name
        self.population = population


finland = Country("Finland", 6000000)
malta = Country("Malta", 500000)
sweden = Country("Sweden", 10000000)
iceland = Country("Iceland", 350000)

countries = [finland, malta, sweden, iceland]

# Filtrar países com população > 5 milhões, pegar só o nome
bigger = [country.name for country in countries if country.population > 5000000]
print(bigger)  # ['Finland', 'Sweden']

# Ou manter os objetos para uso posterior
bigger_countries = [c for c in countries if c.population > 5000000]
for country in bigger_countries:
    print(country.name, country.population)
```

### Criando Objetos com Comprehension

```python
class RunningEvent:
    def __init__(self, length: int, name: str = "no name"):
        self.length = length
        self.name = name

    def __repr__(self):
        return f"{self.length} m. ({self.name})"


lengths = [100, 200, 1500, 3000, 42195]

# Criar objetos a partir de uma lista de valores
events = [RunningEvent(length) for length in lengths]
print(events)
# [100 m. (no name), 200 m. (no name), 1500 m. (no name), ...]

# Modificar um objeto
events[-1].name = "Marathon"
print(events[-1])  # 42195 m. (Marathon)
```

### Classes Iteráveis Funcionam com Comprehensions

Se sua classe implementa `__iter__` e `__next__`, pode ser usada em comprehensions:

```python
class Bookshelf:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < len(self._books):
            book = self._books[self.n]
            self.n += 1
            return book
        raise StopIteration


shelf = Bookshelf()
shelf.add_book(Book("Python Life", "Author A", 100))
shelf.add_book(Book("Java Cup", "Author B", 200))

# Funciona porque Bookshelf é iterável!
book_names = [book.name for book in shelf]
print(book_names)  # ['Python Life', 'Java Cup']
```

### Dictionary Comprehensions

Use chaves `{}` em vez de colchetes `[]`:

```python
{<expressão chave> : <expressão valor> for <item> in <série>}
```

```python
# Contar caracteres em uma string
sentence = "hello there"
char_counts = {char: sentence.count(char) for char in sentence}
print(char_counts)
# {'h': 2, 'e': 3, 'l': 2, 'o': 1, ' ': 1, 't': 1, 'r': 1}

# Fatoriais como dicionário
numbers = [-2, 3, 2, 1, 4, -10, 5, 1, 6]
factorials = {n: factorial(n) for n in numbers if n > 0}
print(factorials)
# {3: 6, 2: 2, 1: 1, 4: 24, 5: 120, 6: 720}
```

---

## Seção 3 - Recursão

### O Que É Recursão?

Uma função que **chama a si mesma** com parâmetros diferentes:

```python
# ❌ Recursão infinita - causa erro!
def hello(name: str):
    print("Hello", name)
    hello(name)  # chama a si mesma infinitamente

# RecursionError: maximum recursion depth exceeded
```

### Recursão Correta: Com Condição de Parada

```python
# ✅ Recursão com condição de parada
def fill_list(numbers: list):
    """Adiciona zeros até a lista ter 10 itens"""
    if len(numbers) < 10:  # condição de parada
        numbers.append(0)
        fill_list(numbers)  # chama a si mesma


test_list = [1, 2, 3, 4]
fill_list(test_list)
print(test_list)  # [1, 2, 3, 4, 0, 0, 0, 0, 0, 0]
```

### Iterativo vs Recursivo

| Abordagem | Descrição |
|-----------|-----------|
| **Iterativa** | Usa loops (`for`, `while`) para processar sequencialmente |
| **Recursiva** | Função chama a si mesma com parâmetros modificados |

```python
# Equivalente iterativo
def fill_list_iterative(numbers: list):
    while len(numbers) < 10:
        numbers.append(0)
```

### Recursão com Valor de Retorno

#### Exemplo: Fatorial

```python
def factorial(n: int):
    """Calcula n! para n >= 0"""
    if n < 2:        # condição de parada (base case)
        return 1
    
    # chamada recursiva
    return n * factorial(n - 1)


for i in range(1, 7):
    print(f"Fatorial de {i} é {factorial(i)}")

# Fatorial de 1 é 1
# Fatorial de 2 é 2
# Fatorial de 3 é 6
# Fatorial de 4 é 24
# Fatorial de 5 é 120
# Fatorial de 6 é 720
```

**Como funciona factorial(5):**

```
factorial(5)
  → 5 * factorial(4)
       → 4 * factorial(3)
            → 3 * factorial(2)
                 → 2 * factorial(1)
                      → 1  (base case!)
                 → 2 * 1 = 2
            → 3 * 2 = 6
       → 4 * 6 = 24
  → 5 * 24 = 120
```

#### Exemplo: Fibonacci

```python
def fibonacci(n: int):
    """Retorna o n-ésimo número de Fibonacci"""
    if n <= 2:       # base case: F(1) = F(2) = 1
        return 1
    
    # F(n) = F(n-1) + F(n-2)
    return fibonacci(n - 1) + fibonacci(n - 2)


for i in range(1, 11):
    print(f"Fibonacci({i}) = {fibonacci(i)}")

# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
```

### Binary Search (Busca Binária)

Algoritmo eficiente para buscar em **listas ordenadas**:

```python
def binary_search(target: list, item: int, left: int, right: int):
    """Retorna True se item está na lista, False caso contrário"""
    
    # Base case: área de busca vazia
    if left > right:
        return False
    
    # Calcula o centro
    centre = (left + right) // 2
    
    # Encontrou!
    if target[centre] == item:
        return True
    
    # Item é maior: busca na metade direita
    if target[centre] < item:
        return binary_search(target, item, centre + 1, right)
    
    # Item é menor: busca na metade esquerda
    return binary_search(target, item, left, centre - 1)


# Uso
target = [1, 2, 4, 5, 7, 8, 11, 13, 14, 18]
print(binary_search(target, 2, 0, len(target) - 1))   # True
print(binary_search(target, 13, 0, len(target) - 1))  # True
print(binary_search(target, 6, 0, len(target) - 1))   # False
print(binary_search(target, 15, 0, len(target) - 1))  # False
```

### Eficiência: Linear vs Binária

| Tipo de Busca | Complexidade | 1 milhão de itens |
|---------------|--------------|-------------------|
| **Linear** | O(n) | ~1.000.000 passos |
| **Binária** | O(log n) | ~20 passos |

---

## Seção 4 - Mais Exemplos de Recursão

### Árvores Binárias

Uma estrutura ramificada onde cada nó tem **no máximo 2 filhos**:

```
        2          ← raiz (root)
       / \
      3   4        ← nós filhos
     / \   \
    5   8  11      ← folhas (leaves)
```

### Modelando Árvore em Python

```python
class Node:
    """Representa um nó em uma árvore binária"""
    
    def __init__(self, value, left_child: 'Node' = None, right_child: 'Node' = None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child


# Construindo a árvore do diagrama acima
tree = Node(2)
tree.left_child = Node(3)
tree.left_child.left_child = Node(5)
tree.left_child.right_child = Node(8)
tree.right_child = Node(4)
tree.right_child.right_child = Node(11)
```

### Algoritmo Recursivo: Percorrer Todos os Nós

```python
def print_nodes(root: Node):
    """Imprime todos os nós da árvore"""
    print(root.value)
    
    if root.left_child is not None:
        print_nodes(root.left_child)
    
    if root.right_child is not None:
        print_nodes(root.right_child)


print_nodes(tree)
# 2
# 3
# 5
# 8
# 4
# 11
```

**O algoritmo:**
1. Processa o nó atual
2. Chama recursivamente no filho esquerdo
3. Chama recursivamente no filho direito

### Algoritmo Recursivo: Soma dos Nós

```python
def sum_of_nodes(root: Node):
    """Retorna a soma de todos os valores na árvore"""
    node_sum = root.value
    
    if root.left_child is not None:
        node_sum += sum_of_nodes(root.left_child)
    
    if root.right_child is not None:
        node_sum += sum_of_nodes(root.right_child)
    
    return node_sum


print(sum_of_nodes(tree))  # 2 + 3 + 5 + 8 + 4 + 11 = 33
```

### Árvore Binária Ordenada

Uma árvore onde:
- Filho esquerdo < nó atual
- Filho direito > nó atual

```
        8
       / \
      3   10
     / \    \
    1   6   14
```

### Busca em Árvore Ordenada

```python
def find_node(root: Node, value):
    """Busca um valor em árvore binária ordenada"""
    if root is None:
        return False
    
    if value == root.value:
        return True
    
    if value > root.value:
        return find_node(root.right_child, value)
    
    return find_node(root.left_child, value)
```

### Exemplo: Contando Subordinados

```python
class Employee:
    def __init__(self, name: str):
        self.name = name
        self.subordinates = []
    
    def add_subordinate(self, employee: 'Employee'):
        self.subordinates.append(employee)


def count_subordinates(employee: Employee):
    """Conta recursivamente todos os subordinados"""
    count = len(employee.subordinates)
    
    for subordinate in employee.subordinates:
        count += count_subordinates(subordinate)
    
    return count


# Estrutura hierárquica
t1 = Employee("Sally")      # CEO
t4 = Employee("Emily")      # Gerente
t2 = Employee("Eric")
t3 = Employee("Matthew")
t5 = Employee("Adele")
t6 = Employee("Claire")

t1.add_subordinate(t4)
t1.add_subordinate(t6)
t4.add_subordinate(t2)
t4.add_subordinate(t3)
t4.add_subordinate(t5)

print(count_subordinates(t1))  # 5 (todos abaixo de Sally)
print(count_subordinates(t4))  # 3 (Eric, Matthew, Adele)
print(count_subordinates(t5))  # 0 (sem subordinados)
```

---

## Conceitos-Chave

### List Comprehensions

| Padrão | Sintaxe | Uso |
|--------|---------|-----|
| **Básico** | `[expr for x in lista]` | Transformar todos os itens |
| **Com filtro** | `[expr for x in lista if cond]` | Selecionar alguns itens |
| **Com if-else** | `[a if cond else b for x in lista]` | Processar todos diferentemente |

### Dictionary Comprehensions

```python
{chave: valor for item in série}
{chave: valor for item in série if condição}
```

### Recursão

| Conceito | Descrição |
|----------|-----------|
| **Base Case** | Condição que para a recursão |
| **Recursive Case** | Chamada da função a si mesma |
| **Call Stack** | Pilha de chamadas de função |

### Estruturas de Dados Recursivas

| Estrutura | Descrição |
|-----------|-----------|
| **Árvore Binária** | Cada nó tem 0, 1 ou 2 filhos |
| **Árvore Ordenada** | Esquerda < nó < direita |

---

## Resumo Rápido

### Programa Exemplo: Sistema de Tarefas com Comprehensions e Recursão

```python
# =============================================================
# SISTEMA DE TAREFAS - Demonstração Parte 11
# =============================================================

from datetime import datetime

# ----- CLASSE TAREFA -----
class Task:
    """Representa uma tarefa com prioridade hierárquica"""
    _id_counter = 0
    
    def __init__(self, description: str, priority: int, subtasks: list = None):
        Task._id_counter += 1
        self.id = Task._id_counter
        self.description = description
        self.priority = priority
        self.completed = False
        self.subtasks = subtasks if subtasks else []
    
    def __repr__(self):
        status = "✓" if self.completed else "○"
        return f"[{status}] {self.id}: {self.description} (P{self.priority})"
    
    def add_subtask(self, task: 'Task'):
        self.subtasks.append(task)


# ----- CLASSE LISTA DE TAREFAS -----
class TaskList:
    """Gerenciador de tarefas com comprehensions e recursão"""
    
    def __init__(self):
        self._tasks = []
    
    def add_task(self, task: Task):
        self._tasks.append(task)
    
    # ----- COMPREHENSIONS -----
    
    def get_pending(self) -> list:
        """Retorna tarefas não completadas (comprehension com filtro)"""
        return [t for t in self._tasks if not t.completed]
    
    def get_by_priority(self, min_priority: int) -> list:
        """Filtra por prioridade mínima"""
        return [t for t in self._tasks if t.priority >= min_priority]
    
    def get_descriptions(self) -> list:
        """Extrai apenas descrições"""
        return [t.description for t in self._tasks]
    
    def get_status_report(self) -> list:
        """Gera relatório de status (if-else comprehension)"""
        return [
            f"{t.description}: DONE" if t.completed else f"{t.description}: PENDING"
            for t in self._tasks
        ]
    
    def get_priority_dict(self) -> dict:
        """Cria dicionário id -> prioridade (dict comprehension)"""
        return {t.id: t.priority for t in self._tasks}
    
    def get_high_priority_dict(self) -> dict:
        """Dicionário filtrado por prioridade alta"""
        return {t.id: t.description for t in self._tasks if t.priority >= 3}
    
    # ----- RECURSÃO -----
    
    def count_all_tasks(self, task: Task) -> int:
        """Conta tarefa + todas as subtarefas recursivamente"""
        count = 1  # conta a própria tarefa
        
        for subtask in task.subtasks:
            count += self.count_all_tasks(subtask)
        
        return count
    
    def find_task_recursive(self, tasks: list, task_id: int) -> Task:
        """Busca tarefa por ID em estrutura hierárquica"""
        for task in tasks:
            if task.id == task_id:
                return task
            
            # Busca nas subtarefas
            found = self.find_task_recursive(task.subtasks, task_id)
            if found:
                return found
        
        return None
    
    def get_all_tasks_flat(self, task: Task) -> list:
        """Achata hierarquia em lista (recursão + comprehension)"""
        result = [task]
        
        for subtask in task.subtasks:
            result.extend(self.get_all_tasks_flat(subtask))
        
        return result
    
    def sum_priorities(self, task: Task) -> int:
        """Soma prioridades de toda a hierarquia"""
        total = task.priority
        
        for subtask in task.subtasks:
            total += self.sum_priorities(subtask)
        
        return total
    
    # ----- ITERADOR -----
    
    def __iter__(self):
        self._index = 0
        return self
    
    def __next__(self):
        if self._index < len(self._tasks):
            task = self._tasks[self._index]
            self._index += 1
            return task
        raise StopIteration


# ----- FUNÇÕES AUXILIARES -----

def filter_string(text: str, forbidden: str) -> str:
    """Remove caracteres proibidos usando comprehension + join"""
    return "".join([c for c in text if c not in forbidden])


def word_lengths(words: list) -> dict:
    """Cria dicionário palavra -> comprimento"""
    return {word: len(word) for word in words}


def factorial_recursive(n: int) -> int:
    """Calcula fatorial recursivamente"""
    if n < 2:
        return 1
    return n * factorial_recursive(n - 1)


def fibonacci_recursive(n: int) -> int:
    """Calcula n-ésimo Fibonacci recursivamente"""
    if n <= 2:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


# ----- DEMONSTRAÇÃO -----

if __name__ == "__main__":
    # Criar tarefas
    task_list = TaskList()
    
    # Tarefa principal com subtarefas
    main_task = Task("Desenvolver App", 5)
    main_task.add_subtask(Task("Design UI", 4))
    main_task.add_subtask(Task("Backend API", 5))
    main_task.subtasks[1].add_subtask(Task("Database", 3))
    main_task.subtasks[1].add_subtask(Task("Auth", 4))
    
    task_list.add_task(main_task)
    task_list.add_task(Task("Documentação", 2))
    task_list.add_task(Task("Testes", 4))
    
    # Marcar algumas como completas
    task_list._tasks[1].completed = True
    
    print("=== COMPREHENSIONS ===")
    print("\nTarefas pendentes:")
    for t in task_list.get_pending():
        print(f"  {t}")
    
    print("\nPrioridade >= 4:")
    for t in task_list.get_by_priority(4):
        print(f"  {t}")
    
    print("\nDescrições:", task_list.get_descriptions())
    
    print("\nRelatório de Status:")
    for status in task_list.get_status_report():
        print(f"  {status}")
    
    print("\nDicionário de Prioridades:", task_list.get_priority_dict())
    
    print("\n=== RECURSÃO ===")
    print(f"\nTotal de tarefas (incluindo subtarefas): {task_list.count_all_tasks(main_task)}")
    print(f"Soma de prioridades: {task_list.sum_priorities(main_task)}")
    
    print("\nTodas as tarefas achatadas:")
    for t in task_list.get_all_tasks_flat(main_task):
        print(f"  {t}")
    
    print("\n=== FUNÇÕES AUXILIARES ===")
    print(f"Filtrar 'Hello, World!': {filter_string('Hello, World!', ',!')}")
    print(f"Comprimentos: {word_lengths(['Python', 'Java', 'C'])}")
    print(f"Fatorial(5): {factorial_recursive(5)}")
    print(f"Fibonacci(10): {fibonacci_recursive(10)}")
```

---

### Checklist de Conceitos

- [ ] Criar list comprehension básica
- [ ] Usar filtro com `if` em comprehension
- [ ] Usar `if-else` (ternário) em comprehension
- [ ] Criar dictionary comprehension
- [ ] Combinar comprehension com `join()` para strings
- [ ] Usar comprehension com classes próprias
- [ ] Escrever função recursiva com base case
- [ ] Implementar fatorial recursivo
- [ ] Implementar Fibonacci recursivo
- [ ] Implementar busca binária recursiva
- [ ] Modelar árvore binária com classe Node
- [ ] Percorrer árvore recursivamente

---

### Armadilhas Comuns

| Armadilha | Problema | Solução |
|-----------|----------|---------|
| Recursão sem base case | Loop infinito, `RecursionError` | Sempre definir condição de parada |
| Confundir sintaxe if vs if-else | `[x if cond for...]` dá erro | if sozinho vai no final; if-else no início |
| Modificar lista durante iteração | Comportamento inesperado | Criar nova lista com comprehension |
| Recursão muito profunda | Stack overflow | Usar iteração ou aumentar limite |
| Dict comprehension com chaves duplicadas | Valores sobrescritos | Garantir chaves únicas |

---

### Padrões de Design

```python
# 1. TRANSFORMAR LISTA
novo = [transformar(x) for x in original]

# 2. FILTRAR LISTA
filtrado = [x for x in original if condicao(x)]

# 3. FILTRAR E TRANSFORMAR
resultado = [transformar(x) for x in original if condicao(x)]

# 4. PROCESSAR TODOS DIFERENTEMENTE
resultado = [a(x) if cond(x) else b(x) for x in original]

# 5. CRIAR DICIONÁRIO
d = {chave(x): valor(x) for x in original}

# 6. ACHATAR LISTA DE LISTAS
flat = [item for sublista in lista for item in sublista]

# 7. RECURSÃO PADRÃO
def recursiva(params):
    if base_case:
        return valor_base
    return combinar(recursiva(params_modificados))

# 8. PERCORRER ÁRVORE
def percorrer(node):
    if node is None:
        return
    processar(node)
    percorrer(node.left)
    percorrer(node.right)
```

---

## Próximos Passos

Na **Parte 12** você aprenderá:

- Funções como argumentos
- Generators
- Programação funcional
- Expressões regulares

---

**Fonte:** University of Helsinki MOOC - Python Programming  
**Resumo criado por:** Claude (Anthropic)  
**Para:** Eric Alcalai França
