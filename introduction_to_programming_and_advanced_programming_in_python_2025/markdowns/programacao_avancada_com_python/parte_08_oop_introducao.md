# Parte 8 - Programação Orientada a Objetos (Introdução)

**Curso:** Advanced Course in Programming - University of Helsinki MOOC  
**Resumo criado por:** Claude (Anthropic)  
**Para:** Eric Alcalai França

---

## Índice

1. [[#Seção 1 - Objects and Methods]]
2. [[#Seção 2 - Classes and Objects]]
3. [[#Seção 3 - Defining Classes]]
4. [[#Seção 4 - Defining Methods]]
5. [[#Seção 5 - More Examples of Classes]]
6. [[#Conceitos-Chave]]
7. [[#Resumo Rápido]]

---

## Seção 1 - Objects and Methods

### O Que São Objetos?

Em programação, **objeto** significa uma entidade independente que contém dados relacionados entre si.

**Exemplo com tupla:**

```python
name = "In Search of Lost Typing"
author = "Marcel Pythons"
year = 1992

# Combinar em tupla
book = (name, author, year)

# Acessar nome do livro
print(book[0])  # In Search of Lost Typing
```

**Exemplo com dicionário (melhor):**

```python
book = {
    "name": "In Search of Lost Typing",
    "author": "Marcel Pythons",
    "year": 1992
}

# Acessar com chave descritiva
print(book["name"])  # In Search of Lost Typing
```

### Independência dos Objetos

Objetos são **independentes**: mudanças em um objeto não afetam outros.

```python
book1 = {"name": "The Old Man and the Pythons", "author": "Ernest Pythons", "year": 1952}
book2 = {"name": "Seven Pythons", "author": "Aleksis Python", "year": 1894}

print(book1["name"])  # The Old Man and the Pythons
print(book2["name"])  # Seven Pythons

book1["name"] = "A Farewell to ARM Processors"

print(book1["name"])  # A Farewell to ARM Processors
print(book2["name"])  # Seven Pythons (não mudou!)
```

### Tudo em Python é Objeto

Internamente, **todo valor** em Python é um objeto. Variáveis armazenam **referências** a objetos, não os valores diretamente.

```python
a = 3  # 'a' contém referência a objeto que contém 3
```

**Tipos básicos são imutáveis:**
- `int`, `float`, `bool`, `str`, `tuple`
- Não podem ser modificados na memória
- Mudanças criam novos objetos

**Outros tipos são mutáveis:**
- `list`, `dict`, `set`
- Podem ser modificados diretamente

### Métodos

**Método** = função que opera em objeto específico.

**Sintaxe:** `objeto.método(argumentos)`

**Exemplo com dicionário:**

```python
book = {
    "name": "The Old Man and the Pythons",
    "author": "Ernest Pythons",
    "year": 1952
}

# Método values() retorna valores do dicionário
for value in book.values():
    print(value)
# The Old Man and the Pythons
# Ernest Pythons
# 1952
```

**Exemplo com strings:**

```python
name = "Imaginary Irene"

# Contar ocorrências de letra
print(name.count("I"))  # 2

# Encontrar substring
print(name.find("Irene"))  # 10
print("Another string".find("Irene"))  # -1 (não encontrado)
```

### Métodos que Modificam vs Não Modificam

**Strings são imutáveis:** Métodos não alteram string original.

```python
text = "hello"
text.upper()  # Retorna "HELLO" mas não modifica 'text'
print(text)   # hello (original intacta)

# Para modificar, precisa reatribuir
text = text.upper()
print(text)   # HELLO
```

**Listas são mutáveis:** Métodos podem alterar lista.

```python
my_list = [1, 2, 3]

my_list.append(5)  # Modifica lista original
print(my_list)     # [1, 2, 3, 5]

my_list.pop(0)     # Remove primeiro item
print(my_list)     # [2, 3, 5]
```

---

## Seção 2 - Classes and Objects

### Declaração Especial de Tipos Básicos

Python tem sintaxe única para tipos básicos:

```python
# Listas → colchetes
my_list = [1, 2, 3]

# Strings → aspas
my_string = "Hi there!"

# Dicionários → chaves
my_dict = {"one": 1, "two": 2}

# Tuplas → parênteses
my_tuple = (1, 2, 3)
```

### Outros Tipos: Construtores

Para outros tipos, chamamos função **construtor**.

```python
from fractions import Fraction

# Criar frações
half = Fraction(1, 2)      # 1/2
third = Fraction(1, 3)     # 1/3
another = Fraction(3, 11)  # 3/11

print(half)         # 1/2
print(half + third) # 5/6
```

**Características de construtores:**
- Não usam notação de ponto (criam objeto)
- Começam com letra maiúscula: `Fraction(1, 2)`

### Classe: Blueprint de Objetos

**Classe** = definição que contém:
- Estrutura dos dados (atributos)
- Funcionalidades (métodos)

**Analogia:**
- **Classe** = planta arquitetônica
- **Objeto** = casa construída a partir da planta

**Relação classe-objeto simplificada:**
- Classe define as variáveis
- Objeto atribui valores a essas variáveis

**Exemplo com Fraction:**

```python
from fractions import Fraction

number = Fraction(2, 5)

# Acessar atributos do objeto
print(number.numerator)    # 2
print(number.denominator)  # 5
```

A classe `Fraction` define `numerator` e `denominator`. Cada objeto tem seus próprios valores.

**Exemplo com date:**

```python
from datetime import date

xmas_eve = date(2020, 12, 24)
midsummer = date(2020, 6, 20)

# Cada objeto tem seus próprios valores
print(xmas_eve.month)   # 12
print(midsummer.month)  # 6
```

### Funções que Trabalham com Objetos

```python
from datetime import date

def is_it_weekend(my_date: date):
    weekday = my_date.isoweekday()  # 1=segunda, 7=domingo
    return weekday == 6 or weekday == 7

xmas_eve = date(2020, 12, 24)
midsummer = date(2020, 6, 20)

print(is_it_weekend(xmas_eve))   # False
print(is_it_weekend(midsummer))  # True
```

### Métodos vs Variáveis (Atributos)

**Diferença sutil mas importante:**

```python
from datetime import date

my_date = date(2020, 12, 24)

# MÉTODO - usa parênteses
weekday = my_date.isoweekday()  # ✅ Correto

# VARIÁVEL - sem parênteses
my_month = my_date.month  # ✅ Correto
```

**Erros comuns:**

```python
# ❌ Esquecer parênteses em método
weekday = my_date.isoweekday
print(weekday)
# <built-in method isoweekday of datetime.date object at 0x...>

# ❌ Colocar parênteses em variável
my_month = my_date.month()
# TypeError: 'int' object is not callable
```

---

## Seção 3 - Defining Classes

### Sintaxe Básica

```python
class NameOfClass:
    # definição da classe
```

**Convenção de nomes: PascalCase (UpperCamelCase)**
- Todas palavras juntas, sem espaços
- Cada palavra com maiúscula inicial

```python
Weekday
BankAccount
LibraryDatabase
PythonCourseGrades
```

### Classe Vazia (Skeleton)

```python
class BankAccount:
    pass  # Necessário pois bloco não pode ser vazio
```

### Adicionando Atributos

Atributos = variáveis anexadas ao objeto.

```python
class BankAccount:
    pass

# Criar objeto
peters_account = BankAccount()

# Adicionar atributos
peters_account.owner = "Peter Python"
peters_account.balance = 5.0

print(peters_account.owner)    # Peter Python
print(peters_account.balance)  # 5.0
```

**Problema:** Objetos diferentes podem ter atributos diferentes!

```python
peters_account = BankAccount()
peters_account.owner = "Peter"
peters_account.balance = 1400

paulas_account = BankAccount()
paulas_account.owner = "Paula"
# paulas_account NÃO tem balance!

print(peters_account.balance)  # 1400
print(paulas_account.balance)  # ❌ AttributeError!
```

### Construtor: `__init__`

**Solução:** Inicializar atributos no construtor.

```python
class BankAccount:
    
    def __init__(self, balance: float, owner: str):
        self.balance = balance
        self.owner = owner
```

**Componentes:**
- Nome: sempre `__init__` (2 underscores de cada lado)
- Primeiro parâmetro: sempre `self`
- Outros parâmetros: valores iniciais

### O Parâmetro `self`

`self` = referência ao próprio objeto.

**Diferença importante:**

```python
def __init__(self, balance: float, owner: str):
    self.balance = balance
    self.owner = owner
```

- `self.balance` = atributo do objeto (persiste)
- `balance` = parâmetro da função (temporário)

**Usando construtor:**

```python
class BankAccount:
    def __init__(self, balance: float, owner: str):
        self.balance = balance
        self.owner = owner

# Python passa 'self' automaticamente
peters_account = BankAccount(100, "Peter Python")
paulas_account = BankAccount(20000, "Paula Pythons")

print(peters_account.balance)  # 100
print(paulas_account.balance)  # 20000
```

### Modificando Atributos

Mesmo com construtor, ainda podemos modificar depois:

```python
class BankAccount:
    def __init__(self, balance: float, owner: str):
        self.balance = balance
        self.owner = owner

peters_account = BankAccount(100, "Peter Python")
print(peters_account.balance)  # 100

# Modificar diretamente
peters_account.balance = 1500
print(peters_account.balance)  # 1500

# Incrementar
peters_account.balance += 2000
print(peters_account.balance)  # 3500
```

### Atributos de Tipos Diversos

Atributos podem ser de qualquer tipo.

```python
from datetime import date

class LotteryDraw:
    def __init__(self, round_week: int, round_date: date, numbers: list):
        self.round_week = round_week
        self.round_date = round_date
        self.numbers = numbers

round1 = LotteryDraw(1, date(2021, 1, 2), [1, 4, 8, 12, 13, 14, 33])

print(round1.round_week)   # 1
print(round1.round_date)   # 2021-01-02

for number in round1.numbers:
    print(number)
# 1
# 4
# 8
# ...
```

### Usando Objetos de Classes Próprias

Objetos de classes próprias funcionam igual a qualquer objeto Python.

```python
class BankAccount:
    def __init__(self, balance: float, owner: str):
        self.balance = balance
        self.owner = owner

# Função que cria e retorna objeto
def open_account(name: str):
    new_account = BankAccount(0, name)
    return new_account

# Função que modifica objeto
def deposit_money_on_account(account: BankAccount, amount: int):
    account.balance += amount

peters_account = open_account("Peter Python")
print(peters_account.balance)  # 0

deposit_money_on_account(peters_account, 500)
print(peters_account.balance)  # 500
```

---

## Seção 4 - Defining Methods

### Classe com Apenas Dados vs Dicionário

**Com classe:**

```python
class BankAccount:
    def __init__(self, account_number: str, owner: str, balance: float, annual_interest: float):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
        self.annual_interest = annual_interest

peters_account = BankAccount("12345-678", "Peter Python", 1500.0, 0.015)
```

**Com dicionário:**

```python
peters_account = {
    "account_number": "12345-678",
    "owner": "Peter Python",
    "balance": 1500.0,
    "annual_interest": 0.015
}
```

**Vantagens da classe:**
- Estrutura "amarrada" (todos objetos iguais)
- Nome significativo (`BankAccount` vs `dict`)
- Pode conter **funcionalidade** (métodos)

### Adicionando Métodos

**Princípio OOP:** Objeto contém dados E funcionalidade para processá-los.

```python
class BankAccount:
    def __init__(self, account_number: str, owner: str, balance: float, annual_interest: float):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
        self.annual_interest = annual_interest
    
    # Método para adicionar juros
    def add_interest(self):
        self.balance += self.balance * self.annual_interest

peters_account = BankAccount("12345-678", "Peter Python", 1500.0, 0.015)
peters_account.add_interest()
print(peters_account.balance)  # 1522.5
```

**Método afeta apenas o objeto em que é chamado:**

```python
peters_account = BankAccount("12345-678", "Peter Python", 1500.0, 0.015)
paulas_account = BankAccount("99999-999", "Paula Pythonen", 1500.0, 0.05)
pippas_account = BankAccount("1111-222", "Pippa Programmer", 1500.0, 0.001)

# Adicionar juros apenas em Peter e Paula
peters_account.add_interest()
paulas_account.add_interest()

print(peters_account.balance)  # 1522.5
print(paulas_account.balance)  # 1575.0
print(pippas_account.balance)  # 1500.0 (não mudou)
```

### Encapsulamento

**Client** = código que cria objeto e usa seus métodos.

**Encapsulamento** = garantir integridade interna do objeto.
- Dados acessados apenas através de métodos
- Métodos verificam validade das operações

```python
class BankAccount:
    def __init__(self, account_number: str, owner: str, balance: float, annual_interest: float):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
        self.annual_interest = annual_interest
    
    def add_interest(self):
        self.balance += self.balance * self.annual_interest
    
    # Método para sacar - verifica se há saldo
    def withdraw(self, amount: float):
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False

peters_account = BankAccount("12345-678", "Peter Python", 1500.0, 0.015)

if peters_account.withdraw(1000):
    print("Saque bem-sucedido, saldo:", peters_account.balance)
else:
    print("Saque malsucedido, saldo insuficiente")
# Saque bem-sucedido, saldo: 500.0

if peters_account.withdraw(1000):
    print("Saque bem-sucedido, saldo:", peters_account.balance)
else:
    print("Saque malsucedido, saldo insuficiente")
# Saque malsucedido, saldo insuficiente
```

**Problema:** Ainda é possível modificar atributo diretamente!

```python
peters_account = BankAccount("12345-678", "Peter Python", 1500.0, 0.015)

if peters_account.withdraw(2000):
    print("Saque bem-sucedido")
else:
    print("Saque malsucedido")
    # "Forçar" saque
    peters_account.balance -= 2000  # ❌ Burla validação!

print("Saldo:", peters_account.balance)  # -500.0 (negativo!)
```

**Solução:** Esconder atributos do client (próxima parte do curso).

### Validação no Construtor

Podemos validar dados já no construtor.

```python
from datetime import date

class PersonalBest:
    def __init__(self, player: str, day: int, month: int, year: int, points: int):
        # Valores padrão
        self.player = ""
        self.date_of_pb = date(1900, 1, 1)
        self.points = 0
        
        # Validar e atribuir
        if self.name_ok(player):
            self.player = player
        
        if self.date_ok(day, month, year):
            self.date_of_pb = date(year, month, day)
        
        if self.points_ok(points):
            self.points = points
    
    # Métodos auxiliares de validação
    def name_ok(self, name: str):
        return len(name) >= 2
    
    def date_ok(self, day, month, year):
        try:
            date(year, month, day)
            return True
        except:
            return False
    
    def points_ok(self, points):
        return points >= 0

result1 = PersonalBest("Peter", 1, 11, 2020, 235)
print(result1.points)      # 235
print(result1.player)      # Peter
print(result1.date_of_pb)  # 2020-11-01

# Data inválida
result2 = PersonalBest("Paula", 4, 13, 2019, 4555)
print(result2.points)      # 4555
print(result2.player)      # Paula
print(result2.date_of_pb)  # 1900-01-01 (valor padrão)
```

### Variáveis Locais em Métodos

Nem todas variáveis em métodos precisam de `self`.

**Use `self` quando:**
- Variável é atributo do objeto
- Precisa ser acessada fora do método

**Não use `self` quando:**
- Variável é auxiliar/temporária
- Só usada dentro do método

```python
class BonusCard:
    def __init__(self, name: str, balance: float):
        self.name = name         # ✅ Atributo
        self.balance = balance   # ✅ Atributo
    
    def add_bonus(self):
        # Variável LOCAL (sem self)
        bonus = self.balance * 0.25  # ✅ Auxiliar
        self.balance += bonus
    
    def add_superbonus(self):
        # Outra variável LOCAL
        superbonus = self.balance * 0.5  # ✅ Auxiliar
        self.balance += superbonus
```

---

## Seção 5 - More Examples of Classes

### Exemplo 1: Classe Rectangle

```python
class Rectangle:
    def __init__(self, left_upper: tuple, right_lower: tuple):
        self.left_upper = left_upper
        self.right_lower = right_lower
        self.width = right_lower[0] - left_upper[0]
        self.height = right_lower[1] - left_upper[1]
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return self.width * 2 + self.height * 2
    
    def move(self, x_change: int, y_change: int):
        # Mover canto superior esquerdo
        corner = self.left_upper
        self.left_upper = (corner[0] + x_change, corner[1] + y_change)
        
        # Mover canto inferior direito
        corner = self.right_lower
        self.right_lower = (corner[0] + x_change, corner[1] + y_change)

# Usar classe
rectangle = Rectangle((1, 1), (4, 3))
print(rectangle.left_upper)   # (1, 1)
print(rectangle.width)        # 3
print(rectangle.height)       # 2
print(rectangle.perimeter())  # 10
print(rectangle.area())       # 6

rectangle.move(3, 3)
print(rectangle.left_upper)   # (4, 4)
print(rectangle.right_lower)  # (7, 6)
```

**Sistema de coordenadas:**
- x aumenta da esquerda para direita
- y aumenta de cima para baixo
- (0, 0) = canto superior esquerdo da tela

### Imprimindo Objetos

**Comportamento padrão:**

```python
rectangle = Rectangle((1, 1), (4, 3))
print(rectangle)
# <__main__.Rectangle object at 0x000002D7BF148A90>
```

Nada informativo!

### Método `__str__`

Define representação em string do objeto.

```python
class Rectangle:
    def __init__(self, left_upper: tuple, right_lower: tuple):
        self.left_upper = left_upper
        self.right_lower = right_lower
        self.width = right_lower[0] - left_upper[0]
        self.height = right_lower[1] - left_upper[1]
    
    # ... outros métodos ...
    
    def __str__(self):
        return f"rectangle {self.left_upper} ... {self.right_lower}"

rectangle = Rectangle((1, 1), (4, 3))
print(rectangle)
# rectangle (1, 1) ... (4, 3)

# Ou com str()
str_rep = str(rectangle)
print(str_rep)
# rectangle (1, 1) ... (4, 3)
```

**Métodos especiais com underscores:**
- `__str__`: Representação user-friendly
- `__repr__`: Representação técnica
- `__init__`: Construtor
- Muitos outros (veremos depois)

### Exemplo 2: TaskList

```python
class TaskList:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, name: str, priority: int):
        # Armazenar como tupla (prioridade, nome)
        self.tasks.append((priority, name))
    
    def get_next(self):
        # Ordenar por prioridade
        self.tasks.sort()
        # Remover e retornar última (maior prioridade)
        task = self.tasks.pop()
        # Retornar apenas o nome
        return task[1]
    
    def number_of_tasks(self):
        return len(self.tasks)
    
    def clear_tasks(self):
        self.tasks = []

# Usar classe
tasks = TaskList()
tasks.add_task("studying", 50)
tasks.add_task("exercise", 60)
tasks.add_task("cleaning", 10)

print(tasks.number_of_tasks())  # 3
print(tasks.get_next())         # exercise (prioridade 60)
print(tasks.number_of_tasks())  # 2

tasks.add_task("date", 100)
print(tasks.number_of_tasks())  # 3
print(tasks.get_next())         # date (prioridade 100)
print(tasks.get_next())         # studying (prioridade 50)
print(tasks.number_of_tasks())  # 1

tasks.clear_tasks()
print(tasks.number_of_tasks())  # 0
```

**Por que funciona?**
- Tupla `(prioridade, nome)` → prioridade vem primeiro
- `sort()` ordena por primeiro elemento
- Maior prioridade fica no final
- `pop()` remove e retorna último

---

## Conceitos-Chave

### Terminologia OOP

| Termo | Significado |
|-------|-------------|
| **Classe** | Blueprint/molde que define estrutura e comportamento |
| **Objeto** | Instância de uma classe com valores específicos |
| **Atributo** | Variável anexada a objeto (também chamado *data attribute*) |
| **Método** | Função anexada a classe/objeto |
| **Construtor** | Método `__init__` que inicializa objeto |
| **self** | Referência ao próprio objeto dentro da classe |
| **Encapsulamento** | Garantir integridade interna ocultando detalhes |
| **Client** | Código que usa objetos de uma classe |

### Convenções de Nomenclatura

| Tipo | Convenção | Exemplo |
|------|-----------|---------|
| Classe | PascalCase | `BankAccount`, `TaskList` |
| Método | snake_case | `add_interest`, `get_next` |
| Atributo | snake_case | `balance`, `annual_interest` |
| Variável local | snake_case | `bonus`, `total` |

### Métodos Especiais (Magic Methods)

| Método | Quando chamado | Propósito |
|--------|----------------|-----------|
| `__init__(self, ...)` | Ao criar objeto | Inicializar atributos |
| `__str__(self)` | `print(obj)` ou `str(obj)` | Representação legível |
| `__repr__(self)` | Console interativo | Representação técnica |

### self vs Parâmetros Normais

```python
def __init__(self, balance: float, owner: str):
    self.balance = balance
    self.owner = owner
```

| Variável | Tipo | Escopo | Persiste? |
|----------|------|--------|-----------|
| `self.balance` | Atributo | Todo objeto | ✅ Sim |
| `balance` | Parâmetro | Só método | ❌ Não |

### Mutabilidade

| Tipo | Mutável? | Exemplo |
|------|----------|---------|
| `int`, `float`, `bool` | ❌ Não | Reatribuir cria novo objeto |
| `str`, `tuple` | ❌ Não | Métodos retornam novas cópias |
| `list`, `dict`, `set` | ✅ Sim | Métodos modificam in-place |
| Objetos de classes | Depende | Define no método |

---

## Resumo Rápido

### Programa Exemplo - Sistema Bancário Completo

```python
from datetime import datetime

class Transaction:
    """Representa uma transação bancária."""
    
    def __init__(self, amount: float, transaction_type: str, timestamp: datetime = None):
        self.amount = amount
        self.transaction_type = transaction_type
        self.timestamp = timestamp if timestamp else datetime.now()
    
    def __str__(self):
        date_str = self.timestamp.strftime("%d/%m/%Y %H:%M")
        return f"{date_str}: {self.transaction_type} R$ {self.amount:.2f}"


class BankAccount:
    """Conta bancária com histórico de transações."""
    
    # Contador de contas (variável de classe - veremos depois)
    _next_account_number = 1000
    
    def __init__(self, owner: str, initial_balance: float = 0.0):
        # Atributos públicos
        self.account_number = BankAccount._next_account_number
        BankAccount._next_account_number += 1
        
        self.owner = owner
        self.balance = initial_balance
        self.transactions = []
        
        # Registrar depósito inicial se houver
        if initial_balance > 0:
            self._record_transaction(initial_balance, "Depósito inicial")
    
    def deposit(self, amount: float):
        """Deposita valor na conta."""
        if amount <= 0:
            raise ValueError("Valor deve ser positivo")
        
        self.balance += amount
        self._record_transaction(amount, "Depósito")
    
    def withdraw(self, amount: float) -> bool:
        """Saca valor da conta. Retorna True se bem-sucedido."""
        if amount <= 0:
            raise ValueError("Valor deve ser positivo")
        
        if amount > self.balance:
            return False
        
        self.balance -= amount
        self._record_transaction(-amount, "Saque")
        return True
    
    def transfer(self, target_account, amount: float) -> bool:
        """Transfere valor para outra conta."""
        if amount <= 0:
            raise ValueError("Valor deve ser positivo")
        
        if amount > self.balance:
            return False
        
        # Realizar transferência
        self.balance -= amount
        target_account.balance += amount
        
        # Registrar em ambas contas
        self._record_transaction(-amount, f"Transferência para {target_account.owner}")
        target_account._record_transaction(amount, f"Transferência de {self.owner}")
        
        return True
    
    def get_statement(self, last_n: int = 10) -> str:
        """Retorna extrato com últimas N transações."""
        if not self.transactions:
            return "Nenhuma transação registrada"
        
        # Pegar últimas N transações
        recent = self.transactions[-last_n:]
        
        lines = [f"Extrato - Conta {self.account_number} ({self.owner})"]
        lines.append("=" * 50)
        
        for transaction in recent:
            lines.append(str(transaction))
        
        lines.append("=" * 50)
        lines.append(f"Saldo atual: R$ {self.balance:.2f}")
        
        return "\n".join(lines)
    
    def _record_transaction(self, amount: float, transaction_type: str):
        """Método auxiliar privado para registrar transação."""
        transaction = Transaction(abs(amount), transaction_type)
        self.transactions.append(transaction)
    
    def __str__(self):
        return f"Conta {self.account_number} - {self.owner} (R$ {self.balance:.2f})"


class Bank:
    """Sistema bancário com múltiplas contas."""
    
    def __init__(self, name: str):
        self.name = name
        self.accounts = {}  # account_number -> BankAccount
    
    def create_account(self, owner: str, initial_balance: float = 0.0) -> BankAccount:
        """Cria nova conta bancária."""
        account = BankAccount(owner, initial_balance)
        self.accounts[account.account_number] = account
        return account
    
    def find_account(self, account_number: int) -> BankAccount:
        """Busca conta por número."""
        return self.accounts.get(account_number)
    
    def find_accounts_by_owner(self, owner: str) -> list:
        """Busca todas as contas de um proprietário."""
        return [acc for acc in self.accounts.values() if acc.owner == owner]
    
    def total_deposits(self) -> float:
        """Retorna soma de todos os saldos."""
        return sum(acc.balance for acc in self.accounts.values())
    
    def list_accounts(self):
        """Lista todas as contas."""
        if not self.accounts:
            print("Nenhuma conta cadastrada")
            return
        
        print(f"\n{self.name} - Contas cadastradas:")
        print("=" * 50)
        for account in self.accounts.values():
            print(account)
    
    def __str__(self):
        return f"{self.name} ({len(self.accounts)} contas)"


# ============ USANDO O SISTEMA ============
def main():
    # Criar banco
    bank = Bank("Banco Python")
    
    # Criar contas
    john_account = bank.create_account("John Smith", 1000)
    mary_account = bank.create_account("Mary Johnson", 500)
    peter_account = bank.create_account("Peter Parker")
    
    print(bank)
    bank.list_accounts()
    
    # Operações
    print("\n--- Operações ---")
    
    john_account.withdraw(200)
    print(f"John sacou R$ 200: {john_account}")
    
    mary_account.deposit(300)
    print(f"Mary depositou R$ 300: {mary_account}")
    
    if john_account.transfer(peter_account, 150):
        print(f"John transferiu R$ 150 para Peter")
    
    # Tentar saque além do saldo
    if not mary_account.withdraw(1000):
        print("Mary tentou sacar R$ 1000 - saldo insuficiente")
    
    # Extratos
    print("\n--- Extrato de John ---")
    print(john_account.get_statement())
    
    print("\n--- Extrato de Peter ---")
    print(peter_account.get_statement())
    
    # Estatísticas do banco
    print(f"\nTotal depositado no banco: R$ {bank.total_deposits():.2f}")

if __name__ == "__main__":
    main()
```

**Saída:**

```
Banco Python (3 contas)

Banco Python - Contas cadastradas:
==================================================
Conta 1000 - John Smith (R$ 1000.00)
Conta 1001 - Mary Johnson (R$ 500.00)
Conta 1002 - Peter Parker (R$ 0.00)

--- Operações ---
John sacou R$ 200: Conta 1000 - John Smith (R$ 800.00)
Mary depositou R$ 300: Conta 1001 - Mary Johnson (R$ 800.00)
John transferiu R$ 150 para Peter
Mary tentou sacar R$ 1000 - saldo insuficiente

--- Extrato de John ---
Extrato - Conta 1000 (John Smith)
==================================================
18/01/2026 14:30: Depósito inicial R$ 1000.00
18/01/2026 14:30: Saque R$ 200.00
18/01/2026 14:30: Transferência para Peter Parker R$ 150.00
==================================================
Saldo atual: R$ 650.00

--- Extrato de Peter ---
Extrato - Conta 1002 (Peter Parker)
==================================================
18/01/2026 14:30: Transferência de John Smith R$ 150.00
==================================================
Saldo atual: R$ 150.00

Total depositado no banco: R$ 1600.00
```

### Checklist de Conceitos

**Fundamentos:**
- [ ] Entendo o que é um objeto
- [ ] Entendo que objetos são independentes
- [ ] Sei a diferença entre método e função
- [ ] Sei quando usar método vs atributo

**Classes:**
- [ ] Sei definir classe com `class NomeDaClasse:`
- [ ] Uso PascalCase para nomes de classes
- [ ] Entendo que classe é blueprint de objetos
- [ ] Sei criar objetos chamando construtor

**Atributos:**
- [ ] Sei definir atributos com `self.nome_atributo`
- [ ] Entendo diferença entre `self.x` e `x`
- [ ] Sei acessar atributos com `objeto.atributo`
- [ ] Sei quando usar variável local vs atributo

**Construtor:**
- [ ] Sei escrever `__init__(self, ...)`
- [ ] Sempre coloco `self` como primeiro parâmetro
- [ ] Inicializo todos os atributos no construtor
- [ ] Posso fazer validação no construtor

**Métodos:**
- [ ] Sei definir métodos com `def nome(self, ...):`
- [ ] Sempre coloco `self` como primeiro parâmetro
- [ ] Acesso atributos com `self.atributo`
- [ ] Chamo métodos com `objeto.metodo()`
- [ ] Entendo encapsulamento

**Métodos Especiais:**
- [ ] Sei implementar `__str__` para impressão
- [ ] Entendo diferença entre `__str__` e `__repr__`

### Armadilhas Comuns

| Erro | Problema | Solução |
|------|----------|---------|
| Esquecer `self` no método | `def metodo():` | `def metodo(self):` |
| Esquecer `self.` ao acessar atributo | `balance += 10` | `self.balance += 10` |
| Usar `__init` em vez de `__init__` | Um underscore | Dois underscores de cada lado |
| Parênteses em atributo | `obj.month()` | `obj.month` (sem parênteses) |
| Sem parênteses em método | `obj.isoweekday` | `obj.isoweekday()` |
| Modificar atributo diretamente | Burla validação | Usar métodos (encapsulamento) |
| Não retornar em `__str__` | Esquece `return` | Sempre retornar string |
| `self` em variável local | `self.temp = x` | `temp = x` (sem self) |

### Padrões de Design

**1. Construtor com Validação**

```python
class Person:
    def __init__(self, name: str, age: int):
        if not name:
            raise ValueError("Nome não pode ser vazio")
        if age < 0:
            raise ValueError("Idade não pode ser negativa")
        
        self.name = name
        self.age = age
```

**2. Métodos que Retornam vs Modificam**

```python
class Numbers:
    def __init__(self):
        self.values = []
    
    # Modifica objeto (retorna None ou bool)
    def add(self, value):
        self.values.append(value)
    
    # Não modifica (retorna novo valor)
    def get_sum(self):
        return sum(self.values)
```

**3. Método Auxiliar Privado**

```python
class Account:
    def withdraw(self, amount):
        if self._validate_amount(amount):
            self.balance -= amount
    
    # Método privado (convenção: prefixo _)
    def _validate_amount(self, amount):
        return 0 < amount <= self.balance
```

**4. `__str__` Informativo**

```python
class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price
    
    def __str__(self):
        return f"{self.name} - R$ {self.price:.2f}"
```

---

## Próximos Passos

Na **Parte 9** você aprenderá:

- Visibilidade de atributos (público vs privado)
- Properties e getters/setters
- Métodos de classe e estáticos
- Herança

---

**Fonte:** University of Helsinki MOOC - Advanced Course in Programming  
**Resumo criado por:** Claude (Anthropic)  
**Para:** Eric Alcalai França
