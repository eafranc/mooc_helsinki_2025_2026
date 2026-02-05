# Parte 9 - Programação Orientada a Objetos (Avançado)

**Curso:** Advanced Course in Programming - University of Helsinki MOOC  
**Resumo criado por:** Claude (Anthropic)  
**Para:** Eric Alcalai França

---

## Índice

1. [[#Seção 1 - Objects and References]]
2. [[#Seção 2 - Objects as Attributes]]
3. [[#Seção 3 - Encapsulation]]
4. [[#Seção 4 - Scope of Methods]]
5. [[#Seção 5 - Class Attributes]]
6. [[#Seção 6 - More Examples with Classes]]
7. [[#Conceitos-Chave]]
8. [[#Resumo Rápido]]

---

## Seção 1 - Objects and References

### Objetos em Listas

Todo valor em Python é um objeto. Objetos criados a partir de classes próprias funcionam como qualquer objeto Python - podem ser armazenados em listas, dicionários, etc.

```python
from datetime import date

class CompletedCourse:
    def __init__(self, course_name: str, credits: int, completion_date: date):
        self.name = course_name
        self.credits = credits
        self.completion_date = completion_date

# Criar lista de cursos completados
completed = []

maths1 = CompletedCourse("Mathematics 1", 5, date(2020, 3, 11))
prog1 = CompletedCourse("Programming 1", 6, date(2019, 12, 17))

completed.append(maths1)
completed.append(prog1)

# Adicionar diretamente à lista
completed.append(CompletedCourse("Physics 2", 4, date(2019, 11, 10)))
completed.append(CompletedCourse("Programming 2", 5, date(2020, 5, 19)))

# Iterar e somar créditos
credits = 0
for course in completed:
    print(course.name)
    credits += course.credits

print("Total credits received:", credits)
```

**Saída:**
```
Mathematics 1
Programming 1
Physics 2
Programming 2
Total credits received: 20
```

### Listas Contêm Referências, Não Objetos

**Conceito crucial:** Listas não contêm objetos em si - contêm **referências** a objetos.

O mesmo objeto pode aparecer múltiplas vezes em uma lista:

```python
class Product:
    def __init__(self, name: str, unit: str):
        self.name = name
        self.unit = unit

shopping_list = []
milk = Product("Milk", "litre")

shopping_list.append(milk)
shopping_list.append(milk)  # Mesma referência!
shopping_list.append(Product("Cucumber", "piece"))  # Novo objeto
```

**Visualização:**
```
shopping_list = [ref_to_milk, ref_to_milk, ref_to_cucumber]
                      ↓             ↓
                  [mesmo objeto milk]
```

### Múltiplas Referências ao Mesmo Objeto

Quando há múltiplas referências ao mesmo objeto, qualquer uma delas pode ser usada para modificar o objeto:

```python
class Dog:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return self.name

dogs = []
fluffy = Dog("Fluffy")

dogs.append(fluffy)
dogs.append(fluffy)          # Mesma referência
dogs.append(Dog("Fluffy"))   # Objeto DIFERENTE com mesmo nome

print("Dogs initially:")
for dog in dogs:
    print(dog)

# Mudar nome via índice 0
dogs[0].name = "Pooch"
print("\nAfter renaming dog at index 0:")
for dog in dogs:
    print(dog)

# Mudar nome via índice 2
dogs[2].name = "Fifi"
print("\nAfter renaming dog at index 2:")
for dog in dogs:
    print(dog)
```

**Saída:**
```
Dogs initially:
Fluffy
Fluffy
Fluffy

After renaming dog at index 0:
Pooch
Pooch
Fluffy

After renaming dog at index 2:
Pooch
Pooch
Fifi
```

**Explicação:**
- Índices 0 e 1 → mesma referência → mudança afeta ambos
- Índice 2 → referência diferente → mudança independente

### `is` vs `==`

**`is`** - verifica se são o **mesmo objeto** (mesma referência)  
**`==`** - verifica se têm o **mesmo conteúdo**

```python
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

# Comparar identidade (is)
print(list1 is list2)  # False (objetos diferentes)
print(list1 is list3)  # True (mesma referência)
print(list2 is list3)  # False

print()

# Comparar conteúdo (==)
print(list1 == list2)  # True (mesmo conteúdo)
print(list1 == list3)  # True (mesmo conteúdo)
print(list2 == list3)  # True (mesmo conteúdo)
```

### Objetos em Dicionários

Objetos também podem ser valores (ou até chaves) em dicionários:

```python
class Student:
    def __init__(self, name: str, cr: int):
        self.name = name
        self.cr = cr

# Dicionário: chave = número de matrícula, valor = objeto Student
students = {}
students["12345"] = Student("Saul Student", 10)
students["54321"] = Student("Sally Student", 67)

print(students["12345"].name)  # Saul Student
print(students["54321"].cr)    # 67
```

---

## Seção 2 - Objects as Attributes

### Objetos Como Atributos

Podemos usar instâncias de classes próprias como atributos em outras classes.

**Exemplo com 3 classes:**

```python
# Arquivo: course.py
class Course:
    def __init__(self, name: str, code: str, credits: int):
        self.name = name
        self.code = code
        self.credits = credits

# Arquivo: student.py
class Student:
    def __init__(self, name: str, student_number: str, credits: int):
        self.name = name
        self.student_number = student_number
        self.credits = credits

# Arquivo: completedcourse.py
from course import Course
from student import Student

class CompletedCourse:
    def __init__(self, student: Student, course: Course, grade: int):
        self.student = student  # Objeto Student
        self.course = course    # Objeto Course
        self.grade = grade
```

**Usar as classes:**

```python
from completedcourse import CompletedCourse
from course import Course
from student import Student

# Criar estudantes
students = []
students.append(Student("Ollie", "1234", 10))
students.append(Student("Peter", "3210", 23))
students.append(Student("Lena", "9999", 43))

# Criar curso
itp = Course("Introduction to Programming", "itp1", 5)

# Cursos completados
completed = []
for student in students:
    completed.append(CompletedCourse(student, itp, 3))

# Imprimir nomes
for course in completed:
    print(course.student.name)
```

**Encadeamento com ponto:**

```python
print(course.student.name)
```

- `course` = instância de `CompletedCourse`
- `student` = atributo de `CompletedCourse` (objeto `Student`)
- `name` = atributo do objeto `Student`

### Quando Importar?

**Import é necessário quando:**
- Usar código definido em outro arquivo
- Usar biblioteca padrão Python

**Import NÃO é necessário quando:**
- Todo código está no mesmo arquivo
- Todos exercícios do curso geralmente em arquivo único

```python
# ❌ NÃO faça isso se tudo está no mesmo arquivo!
from person import Person

# ✅ Só use import se Person está em outro arquivo
```

### Listas de Objetos Como Atributo

Muito comum ter coleção de objetos como atributo.

**Exemplo - Time e Jogadores:**

```python
class Player:
    def __init__(self, name: str, goals: int):
        self.name = name
        self.goals = goals
    
    def __str__(self):
        return f"{self.name} ({self.goals} goals)"

class Team:
    def __init__(self, name: str):
        self.name = name
        self.players = []  # Lista de objetos Player
    
    def add_player(self, player: Player):
        self.players.append(player)
    
    def summary(self):
        goals = [player.goals for player in self.players]
        print("Team:", self.name)
        print("Players:", len(self.players))
        print("Goals scored by each player:", goals)

# Usar
ca = Team("Campus Allstars")
ca.add_player(Player("Eric", 10))
ca.add_player(Player("Emily", 22))
ca.add_player(Player("Andy", 1))

ca.summary()
```

**Saída:**
```
Team: Campus Allstars
Players: 3
Goals scored by each player: [10, 22, 1]
```

### None: Referência ao "Nada"

`None` representa objeto "vazio" em Python.

**Quando usar:**
- Retornar quando busca não encontra resultado
- Valor padrão para parâmetro opcional
- Indicar ausência de valor

```python
class Team:
    def __init__(self, name: str):
        self.name = name
        self.players = []
    
    def add_player(self, player: Player):
        self.players.append(player)
    
    def find_player(self, name: str):
        for player in self.players:
            if player.name == name:
                return player
        return None  # Não encontrado

# Testar
ca = Team("Campus Allstars")
ca.add_player(Player("Eric", 10))
ca.add_player(Player("Andy", 1))

player1 = ca.find_player("Andy")
print(player1)  # Andy (1 goals)

player2 = ca.find_player("Charlie")
print(player2)  # None
```

### Cuidado com None!

Tentar acessar atributo/método de `None` causa erro:

```python
ca = Team("Campus Allstars")
ca.add_player(Player("Eric", 10))

player = ca.find_player("Charlie")
print(f"Goals by Charlie: {player.goals}")  # ❌ AttributeError!
```

**Solução: Sempre verificar antes de usar:**

```python
player = ca.find_player("Charlie")
if player is not None:
    print(f"Goals by Charlie: {player.goals}")
else:
    print("Charlie doesn't play in Campus Allstars :(")
```

---

## Seção 3 - Encapsulation

### O Que É Encapsulamento?

**Encapsulamento** = esconder detalhes internos do objeto, oferecendo interface pública apropriada.

**Objetivos:**
1. Facilitar uso da classe
2. Preservar integridade do objeto

**Integridade** = estado do objeto sempre válido (ex: mês nunca 13, créditos nunca negativos)

### Problema Sem Encapsulamento

```python
class Student:
    def __init__(self, name: str, student_number: str):
        self.name = name
        self.student_number = student_number
        self.study_credits = 0
    
    def add_credits(self, study_credits):
        if study_credits > 0:
            self.study_credits += study_credits

sally = Student("Sally Student", "12345")
sally.add_credits(5)
sally.add_credits(10)
print("Study credits:", sally.study_credits)  # 15
```

Parece bom, mas...

```python
# ❌ Podemos burlar validação acessando diretamente!
sally.study_credits = -100
print("Study credits:", sally.study_credits)  # -100 (inválido!)
```

### Atributos Privados: `__`

Prefixo duplo underscore `__` torna atributo **privado**.

```python
class CreditCard:
    def __init__(self, number: str, name: str):
        self.__number = number  # Privado
        self.name = name        # Público
```

**Atributo público pode ser acessado:**

```python
card = CreditCard("123456", "Randy Riches")
print(card.name)  # Randy Riches

card.name = "Charlie Churchmouse"
print(card.name)  # Charlie Churchmouse
```

**Atributo privado NÃO pode:**

```python
card = CreditCard("123456", "Randy Riches")
print(card.__number)  # ❌ AttributeError!
```

### Métodos Para Acessar Atributos Privados

Criar métodos públicos para acessar/modificar dados privados:

```python
class CreditCard:
    def __init__(self, number: str, name: str, balance: float):
        self.__number = number
        self.name = name
        self.__balance = balance
    
    def deposit_money(self, amount: float):
        if amount > 0:
            self.__balance += amount
    
    def withdraw_money(self, amount: float):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
    
    def retrieve_balance(self):
        return self.__balance

card = CreditCard("123456", "Randy Riches", 5000)
print(card.retrieve_balance())  # 5000

card.deposit_money(100)
print(card.retrieve_balance())  # 5100

card.withdraw_money(500)
print(card.retrieve_balance())  # 4600

# Tentar sacar mais que saldo (não funciona)
card.withdraw_money(10000)
print(card.retrieve_balance())  # 4600 (não mudou)
```

### Getters e Setters com `@property`

Forma "pythônica" de criar getters/setters.

**Getter:** `@property`  
**Setter:** `@attribute.setter`

```python
class Wallet:
    def __init__(self):
        self.__money = 0
    
    # Getter
    @property
    def money(self):
        return self.__money
    
    # Setter
    @money.setter
    def money(self, money):
        if money >= 0:
            self.__money = money

# Usar como se fosse atributo (sem parênteses!)
wallet = Wallet()
print(wallet.money)  # 0 (chama getter)

wallet.money = 50    # Chama setter
print(wallet.money)  # 50

wallet.money = -30   # Setter valida e rejeita
print(wallet.money)  # 50 (não mudou)
```

### Lançar Exceção em Setter

Melhor notificar cliente sobre valores inválidos:

```python
class Wallet:
    def __init__(self):
        self.__money = 0
    
    @property
    def money(self):
        return self.__money
    
    @money.setter
    def money(self, money):
        if money >= 0:
            self.__money = money
        else:
            raise ValueError("The amount must not be below zero")

wallet = Wallet()
wallet.money = -30  # ValueError: The amount must not be below zero
```

### Ordem Importante!

⚠️ **Getter (`@property`) DEVE vir antes do Setter!**

```python
class Example:
    def __init__(self):
        self.__value = 0
    
    # ✅ CORRETO: getter primeiro
    @property
    def value(self):
        return self.__value
    
    # Depois setter
    @value.setter
    def value(self, value):
        self.__value = value
```

### Exemplo Completo com Múltiplos Atributos

```python
class Player:
    def __init__(self, name: str, player_number: int):
        self.__name = name
        self.__player_number = player_number
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name: str):
        if name != "":
            self.__name = name
        else:
            raise ValueError("The name may not be an empty string")
    
    @property
    def player_number(self):
        return self.__player_number
    
    @player_number.setter
    def player_number(self, player_number: int):
        if player_number > 0:
            self.__player_number = player_number
        else:
            raise ValueError("The player number must be a positive integer")

player = Player("Betty Ballmer", 10)
print(player.name)           # Betty Ballmer
print(player.player_number)  # 10

player.name = "Buster Ballmer"
player.player_number = 11
print(player.name)           # Buster Ballmer
print(player.player_number)  # 11
```

### Encapsulamento de Estrutura Interna

Cliente não precisa saber implementação interna.

```python
class Diary:
    def __init__(self, owner: str):
        self.__owner = owner
        self.__entries = []  # Cliente não vê estrutura interna
    
    @property
    def owner(self):
        return self.__owner
    
    @owner.setter
    def owner(self, owner):
        if owner != "":
            self.__owner = owner
        else:
            raise ValueError("The owner may not be an empty string")
    
    # Métodos públicos para manipular entradas
    def add_entry(self, entry: str):
        self.__entries.append(entry)
    
    def print_entries(self):
        print("A total of", len(self.__entries), "entries")
        for entry in self.__entries:
            print("- " + entry)

diary = Diary("Peter")
diary.add_entry("Today I ate porridge")
diary.add_entry("Today I learned OOP")
diary.print_entries()
```

**Vantagens:**
- Implementação pode mudar (lista → dict) sem afetar cliente
- Interface pública permanece estável

---

## Seção 4 - Scope of Methods

### Métodos Privados

Métodos também podem ser privados com prefixo `__`.

**Uso:** Métodos auxiliares internos que cliente não precisa conhecer.

```python
class Recipient:
    def __init__(self, name: str, email: str):
        self.__name = name
        if self.__check_email(email):
            self.__email = email
        else:
            raise ValueError("The email address is not valid")
    
    # Método privado auxiliar
    def __check_email(self, email: str):
        # Verificação simples
        return len(email) > 5 and "." in email and "@" in email
```

**Tentar chamar método privado causa erro:**

```python
peter = Recipient("Peter Emailer", "peter@example.com")
peter.__check_email("someone@example.com")  # ❌ AttributeError!
```

### Método Privado com Getters/Setters

```python
class Recipient:
    def __init__(self, name: str, email: str):
        self.__name = name
        if self.__check_email(email):
            self.__email = email
        else:
            raise ValueError("The email address is not valid")
    
    def __check_email(self, email: str):
        return len(email) > 5 and "." in email and "@" in email
    
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, email: str):
        if self.__check_email(email):  # Reusar validação
            self.__email = email
        else:
            raise ValueError("The email address is not valid")
```

### Escopo e Namespace

**Escopo** = seções do programa onde um nome é visível

**Namespace** = nomes disponíveis em unidade Python definida (classe, função)

**Diferentes namespaces:**
- Método tem acesso a: variáveis locais + atributos/métodos da classe
- Classe tem acesso a: seus atributos/métodos (não variáveis locais dos métodos)
- Cliente tem acesso a: apenas membros públicos

**Por que separar?**

Permite usar mesmos nomes em contextos diferentes sem conflito:

```python
class Example:
    def method1(self):
        temp = 10  # Variável local em method1
        return temp
    
    def method2(self):
        temp = "hello"  # Pode reusar nome!
        return temp
```

### Exemplo: Baralho de Cartas

```python
from random import shuffle

class DeckOfCards:
    def __init__(self):
        self.__reset_deck()
    
    # Método privado para resetar baralho
    def __reset_deck(self):
        self.__deck = []
        suits = ["spades", "hearts", "clubs", "diamonds"]
        for suit in suits:
            for number in range(1, 14):
                self.__deck.append((suit, number))
        shuffle(self.__deck)
    
    def deal(self, number_of_cards: int):
        hand = []
        for i in range(number_of_cards):
            hand.append(self.__deck.pop())
        return hand

# Usar
deck = DeckOfCards()
hand1 = deck.deal(5)
print(hand1)
# [('spades', 7), ('hearts', 3), ...]
```

**Por que método privado?**
- Cliente não precisa chamar `__reset_deck` diretamente
- Evita que cliente quebre estado interno do baralho

### Quando Usar Método Privado?

**Use quando:**
- Cliente não precisa acesso direto
- Método é auxiliar interno
- Acesso direto poderia quebrar integridade

**Regra geral:** Oculte tudo que cliente não precisa.

---

## Seção 5 - Class Attributes

### Traits vs Instance Traits

**Traits** (características) de classes incluem:
- Métodos
- Variáveis

**Tipos de traits:**
- **Instance traits:** específicos de cada objeto
- **Static/Class traits:** compartilhados por todos objetos

### Variáveis de Classe (Class Variables)

**Variável de classe** = compartilhada por todas instâncias.

**Declaração:** Sem `self`, fora de métodos, no nível da classe.

```python
class SavingsAccount:
    general_rate = 0.03  # Variável de classe
    
    def __init__(self, account_number: str, balance: float, interest_rate: float):
        self.__account_number = account_number
        self.__balance = balance
        self.__interest_rate = interest_rate
    
    def add_interest(self):
        # Taxa total = taxa geral + taxa da conta
        total_interest = SavingsAccount.general_rate + self.__interest_rate
        self.__balance += self.__balance * total_interest
    
    @property
    def balance(self):
        return self.__balance
```

**Acessar variável de classe:**

```python
# Acessar via nome da classe (sem criar instância)
print("General rate:", SavingsAccount.general_rate)  # 0.03

# Criar instância e usar
account = SavingsAccount("12345", 1000, 0.05)
account.add_interest()
print(account.balance)  # 1080.0
```

**Diferença importante:**
- Variável de classe: `ClassName.variable`
- Variável de instância: `object.variable`

### Mudando Variável de Classe

Mudança afeta todas instâncias:

```python
class SavingsAccount:
    general_rate = 0.03
    
    def __init__(self, account_number: str, balance: float, interest_rate: float):
        self.__account_number = account_number
        self.__balance = balance
        self.__interest_rate = interest_rate
    
    @property
    def total_interest(self):
        return self.__interest_rate + SavingsAccount.general_rate

account1 = SavingsAccount("12345", 100, 0.03)
account2 = SavingsAccount("54321", 200, 0.06)

print("General rate:", SavingsAccount.general_rate)  # 0.03
print(account1.total_interest)  # 0.06
print(account2.total_interest)  # 0.09

# Mudar taxa geral
SavingsAccount.general_rate = 0.10

print("General rate:", SavingsAccount.general_rate)  # 0.10
print(account1.total_interest)  # 0.13 (mudou!)
print(account2.total_interest)  # 0.16 (mudou!)
```

### Exemplo: Códigos de País

```python
class PhoneNumber:
    # Dicionário de classe (compartilhado)
    country_codes = {
        "Finland": "+358",
        "Sweden": "+46",
        "United States": "+1"
    }
    
    def __init__(self, name: str, phone_number: str, country: str):
        self.__name = name
        self.__phone_number = phone_number
        self.__country = country
    
    @property
    def phone_number(self):
        # Adicionar código do país
        code = PhoneNumber.country_codes[self.__country]
        # Remover zero inicial
        return code + " " + self.__phone_number[1:]

paulas_no = PhoneNumber("Paula Pythons", "050 1234 567", "Finland")
print(paulas_no.phone_number)  # +358 50 1234 567
```

### Métodos de Classe (Class Methods)

**Método de classe** = não vinculado a instância específica.

**Características:**
- Pode ser chamado sem criar instância
- Usa decorador `@classmethod`
- Primeiro parâmetro é `cls` (não `self`)

```python
class Registration:
    def __init__(self, owner: str, make: str, year: int, license_plate: str):
        self.__owner = owner
        self.__make = make
        self.__year = year
        self.license_plate = license_plate  # Chama setter
    
    @property
    def license_plate(self):
        return self.__license_plate
    
    @license_plate.setter
    def license_plate(self, plate):
        if Registration.license_plate_valid(plate):
            self.__license_plate = plate
        else:
            raise ValueError("The license plate is not valid")
    
    # Método de classe
    @classmethod
    def license_plate_valid(cls, plate: str):
        if len(plate) < 3 or "-" not in plate:
            return False
        
        letters, numbers = plate.split("-")
        
        # Verificar letras
        for character in letters:
            if character.lower() not in "abcdefghijklmnopqrstuvwxyz":
                return False
        
        # Verificar números
        for character in numbers:
            if character not in "1234567890":
                return False
        
        return True

# Chamar método de classe SEM criar objeto
if Registration.license_plate_valid("xyz-789"):
    print("Valid license plate!")

# Também pode criar objeto
reg = Registration("Mary Motorist", "Volvo", 1992, "abc-123")
```

**Quando usar método de classe:**
- Funcionalidade útil sem precisar criar instância
- Factory methods (métodos que criam instâncias)
- Utilitários relacionados à classe

---

## Seção 6 - More Examples with Classes

### Exemplo: Point e Line

```python
import math

class Point:
    """Representa ponto em espaço 2D."""
    
    def __init__(self, x: float, y: float):
        self.x = x  # Público (qualquer valor aceito)
        self.y = y
    
    # Método de classe: ponto na origem
    @classmethod
    def origo(cls):
        return Point(0, 0)
    
    # Método de classe: espelhar ponto
    @classmethod
    def mirrored(cls, point: "Point", mirror_x: bool, mirror_y: bool):
        x = point.x
        y = point.y
        if mirror_x:
            y = -y
        if mirror_y:
            x = -x
        return Point(x, y)
    
    def __str__(self):
        return f"({self.x}, {self.y})"


class Line:
    """Representa segmento de linha em espaço 2D."""
    
    def __init__(self, beginning: Point, end: Point):
        self.beginning = beginning
        self.end = end
    
    def length(self):
        # Teorema de Pitágoras
        dx = self.end.x - self.beginning.x
        dy = self.end.y - self.beginning.y
        return math.sqrt(dx**2 + dy**2)
    
    def centre_point(self):
        centre_x = (self.beginning.x + self.end.x) / 2
        centre_y = (self.beginning.y + self.end.y) / 2
        return Point(centre_x, centre_y)
    
    def __str__(self):
        return f"{self.beginning} ... {self.end}"

# Usar
point = Point(1, 3)
print(point)  # (1, 3)

origo = Point.origo()
print(origo)  # (0, 0)

point2 = Point.mirrored(point, True, True)
print(point2)  # (-1, -3)

line = Line(point, point2)
print(line.length())         # 6.324...
print(line.centre_point())   # (0.0, 0.0)
print(line)                  # (1, 3) ... (-1, -3)
```

### Valores Padrão de Parâmetros

Parâmetros podem ter valores padrão:

```python
class Student:
    def __init__(self, name: str, student_number: str, 
                 credits: int = 0, notes: str = ""):
        self.name = name
        self.__student_number = student_number
        self.credits = credits
        self.__notes = notes
    
    # ... getters/setters ...
    
    def summary(self):
        print(f"Student {self.name} ({self.__student_number}):")
        print(f"- credits: {self.credits}")
        print(f"- notes: {self.__notes}")

# Apenas nome e número
student1 = Student("Sally Student", "12345")
student1.summary()
# Student Sally Student (12345):
# - credits: 0
# - notes: 

# Com créditos
student2 = Student("Sassy Student", "54321", 25)
student2.summary()
# Student Sassy Student (54321):
# - credits: 25
# - notes: 

# Todos parâmetros
student3 = Student("Saul Student", "99999", 140, "extra time in exam")
student3.summary()

# Pular parâmetro (usar nome)
student4 = Student("Sandy Student", "98765", notes="absent 20-21")
student4.summary()
# Student Sandy Student (98765):
# - credits: 0
# - notes: absent 20-21
```

### Armadilha: Lista Como Valor Padrão

⚠️ **NUNCA use lista mutável como valor padrão!**

```python
# ❌ ERRADO!
class Student:
    def __init__(self, name, completed_courses=[]):
        self.name = name
        self.completed_courses = completed_courses

student1 = Student("Sally")
student2 = Student("Sassy")

student1.add_course("ItP")
student1.add_course("ACiP")

print(student1.completed_courses)  # ['ItP', 'ACiP']
print(student2.completed_courses)  # ['ItP', 'ACiP'] ❌ COMPARTILHADO!
```

**Por que?** Python reutiliza mesma lista para todos objetos!

**Solução: Use None como padrão:**

```python
# ✅ CORRETO!
class Student:
    def __init__(self, name, completed_courses=None):
        self.name = name
        if completed_courses is None:
            self.completed_courses = []
        else:
            self.completed_courses = completed_courses

student1 = Student("Sally")
student2 = Student("Sassy")

student1.add_course("ItP")

print(student1.completed_courses)  # ['ItP']
print(student2.completed_courses)  # [] ✅ Separados!
```

**Regra:** Valor padrão deve ser imutável (`None`, `0`, `""`, etc).

---

## Conceitos-Chave

### Referências vs Valores

| Conceito | Significado |
|----------|-------------|
| Referência | "Endereço" do objeto na memória |
| Valor | Conteúdo do objeto |
| Lista contém | Referências a objetos (não os objetos) |
| Mesma referência | Mudanças afetam "todas cópias" |

### Operadores de Comparação

| Operador | O que compara | Uso |
|----------|---------------|-----|
| `is` | Identidade (mesmo objeto?) | `obj1 is obj2` |
| `==` | Igualdade (mesmo conteúdo?) | `obj1 == obj2` |
| `is not` | Diferentes objetos? | `obj1 is not obj2` |
| `!=` | Conteúdos diferentes? | `obj1 != obj2` |

### None

| Aspecto | Descrição |
|---------|-----------|
| O que é | Objeto especial representando "nada" |
| Quando usar | Busca sem resultado, valor ausente, padrão opcional |
| Verificar | `if value is None:` ou `if value is not None:` |
| Erro comum | Tentar acessar atributo/método de None |

### Encapsulamento

| Elemento | Convenção | Visibilidade |
|----------|-----------|--------------|
| Público | `self.name` | Cliente pode acessar |
| Privado | `self.__name` | Apenas dentro da classe |
| Getter | `@property` | Permite leitura controlada |
| Setter | `@name.setter` | Permite escrita controlada |

### Class vs Instance

| Aspecto | Instance | Class |
|---------|----------|-------|
| **Variáveis** | `self.var` | `ClassName.var` |
| Valor | Específico de cada objeto | Compartilhado por todos |
| Quando usar | Dados únicos por objeto | Dados compartilhados |
| **Métodos** | `def method(self):` | `@classmethod def method(cls):` |
| Acesso a | Atributos da instância | Apenas class variables |
| Chamar | `obj.method()` | `ClassName.method()` |

### Decoradores

| Decorador | Uso | Primeiro Parâmetro |
|-----------|-----|-------------------|
| (nenhum) | Método de instância | `self` |
| `@property` | Getter | `self` |
| `@attr.setter` | Setter | `self` |
| `@classmethod` | Método de classe | `cls` |
| `@staticmethod` | Método estático | (nenhum) |

---

## Resumo Rápido

### Programa Exemplo - Sistema de E-commerce

```python
from datetime import datetime
from typing import Optional

# ============ CLASSE PRODUCT ============
class Product:
    """Produto à venda."""
    
    # Variável de classe: taxa de imposto
    tax_rate = 0.15
    
    def __init__(self, name: str, price: float, stock: int):
        self.__name = name
        self.__price = price
        self.__stock = stock
    
    @property
    def name(self):
        return self.__name
    
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, price: float):
        if price < 0:
            raise ValueError("Price cannot be negative")
        self.__price = price
    
    @property
    def price_with_tax(self):
        """Preço com imposto."""
        return self.__price * (1 + Product.tax_rate)
    
    @property
    def stock(self):
        return self.__stock
    
    def add_stock(self, amount: int):
        """Adiciona ao estoque."""
        if amount > 0:
            self.__stock += amount
    
    def remove_stock(self, amount: int) -> bool:
        """Remove do estoque. Retorna True se bem-sucedido."""
        if 0 < amount <= self.__stock:
            self.__stock -= amount
            return True
        return False
    
    def __str__(self):
        return f"{self.__name} - R$ {self.__price:.2f} ({self.__stock} in stock)"


# ============ CLASSE ORDER ITEM ============
class OrderItem:
    """Item individual em pedido."""
    
    def __init__(self, product: Product, quantity: int):
        self.__product = product
        self.__quantity = quantity
    
    @property
    def product(self):
        return self.__product
    
    @property
    def quantity(self):
        return self.__quantity
    
    @property
    def subtotal(self):
        """Subtotal sem imposto."""
        return self.__product.price * self.__quantity
    
    @property
    def subtotal_with_tax(self):
        """Subtotal com imposto."""
        return self.__product.price_with_tax * self.__quantity
    
    def __str__(self):
        return f"{self.__product.name} x{self.__quantity} = R$ {self.subtotal:.2f}"


# ============ CLASSE ORDER ============
class Order:
    """Pedido de compra."""
    
    # Variável de classe: contador de pedidos
    _next_order_id = 1000
    
    def __init__(self, customer_name: str):
        self.__order_id = Order._next_order_id
        Order._next_order_id += 1
        
        self.__customer_name = customer_name
        self.__items = []
        self.__timestamp = datetime.now()
        self.__is_paid = False
    
    @property
    def order_id(self):
        return self.__order_id
    
    @property
    def customer_name(self):
        return self.__customer_name
    
    def add_item(self, product: Product, quantity: int) -> bool:
        """Adiciona item ao pedido."""
        # Verificar estoque
        if not product.remove_stock(quantity):
            return False
        
        # Verificar se produto já está no pedido
        for item in self.__items:
            if item.product is product:
                # Produto já no pedido - atualizar quantidade
                # (simplificado - normalmente criaria novo OrderItem)
                return True
        
        # Adicionar novo item
        item = OrderItem(product, quantity)
        self.__items.append(item)
        return True
    
    def get_total(self, with_tax: bool = True) -> float:
        """Retorna total do pedido."""
        total = 0
        for item in self.__items:
            if with_tax:
                total += item.subtotal_with_tax
            else:
                total += item.subtotal
        return total
    
    def mark_as_paid(self):
        """Marca pedido como pago."""
        self.__is_paid = True
    
    @property
    def is_paid(self):
        return self.__is_paid
    
    def print_receipt(self):
        """Imprime recibo."""
        print(f"\n{'='*50}")
        print(f"ORDER #{self.__order_id}")
        print(f"Customer: {self.__customer_name}")
        print(f"Date: {self.__timestamp.strftime('%d/%m/%Y %H:%M')}")
        print(f"{'='*50}")
        
        for item in self.__items:
            print(f"  {item}")
        
        print(f"{'-'*50}")
        print(f"Subtotal: R$ {self.get_total(with_tax=False):.2f}")
        print(f"Tax ({Product.tax_rate*100:.0f}%): R$ {self.get_total(with_tax=True) - self.get_total(with_tax=False):.2f}")
        print(f"TOTAL: R$ {self.get_total(with_tax=True):.2f}")
        print(f"Status: {'PAID' if self.__is_paid else 'PENDING'}")
        print(f"{'='*50}\n")
    
    def __str__(self):
        status = "PAID" if self.__is_paid else "PENDING"
        return f"Order #{self.__order_id} - {self.__customer_name} - R$ {self.get_total():.2f} ({status})"


# ============ CLASSE STORE ============
class Store:
    """Loja online."""
    
    def __init__(self, name: str):
        self.__name = name
        self.__products = {}  # SKU -> Product
        self.__orders = []
    
    def add_product(self, sku: str, product: Product):
        """Adiciona produto ao catálogo."""
        self.__products[sku] = product
    
    def get_product(self, sku: str) -> Optional[Product]:
        """Busca produto por SKU."""
        return self.__products.get(sku)
    
    def list_products(self):
        """Lista produtos disponíveis."""
        print(f"\n{self.__name} - Products:")
        print("="*50)
        for sku, product in self.__products.items():
            print(f"[{sku}] {product}")
        print()
    
    def create_order(self, customer_name: str) -> Order:
        """Cria novo pedido."""
        order = Order(customer_name)
        self.__orders.append(order)
        return order
    
    def find_order(self, order_id: int) -> Optional[Order]:
        """Busca pedido por ID."""
        for order in self.__orders:
            if order.order_id == order_id:
                return order
        return None
    
    def get_sales_report(self):
        """Relatório de vendas."""
        total_sales = sum(order.get_total() for order in self.__orders if order.is_paid)
        pending = sum(1 for order in self.__orders if not order.is_paid)
        
        print(f"\n{self.__name} - Sales Report:")
        print("="*50)
        print(f"Total orders: {len(self.__orders)}")
        print(f"Paid orders: {len(self.__orders) - pending}")
        print(f"Pending orders: {pending}")
        print(f"Total revenue: R$ {total_sales:.2f}")
        print("="*50 + "\n")


# ============ PROGRAMA PRINCIPAL ============
def main():
    # Criar loja
    store = Store("TechShop Online")
    
    # Adicionar produtos
    store.add_product("LAPTOP001", Product("Laptop Dell", 3500.00, 5))
    store.add_product("MOUSE001", Product("Wireless Mouse", 85.00, 20))
    store.add_product("KEYB001", Product("Mechanical Keyboard", 450.00, 10))
    store.add_product("MONITOR001", Product("24\" Monitor", 800.00, 8))
    
    # Listar produtos
    store.list_products()
    
    # Criar pedido 1
    order1 = store.create_order("Alice Silva")
    laptop = store.get_product("LAPTOP001")
    mouse = store.get_product("MOUSE001")
    
    if laptop and mouse:
        order1.add_item(laptop, 1)
        order1.add_item(mouse, 2)
    
    order1.print_receipt()
    order1.mark_as_paid()
    
    # Criar pedido 2
    order2 = store.create_order("Bob Santos")
    keyboard = store.get_product("KEYB001")
    monitor = store.get_product("MONITOR001")
    
    if keyboard and monitor:
        order2.add_item(keyboard, 1)
        order2.add_item(monitor, 1)
    
    order2.print_receipt()
    # Este fica pendente
    
    # Mudar taxa de imposto
    print("Changing tax rate from 15% to 18%...")
    Product.tax_rate = 0.18
    
    # Criar pedido 3 (com nova taxa)
    order3 = store.create_order("Carol Lima")
    if laptop:
        order3.add_item(laptop, 1)
    order3.print_receipt()
    order3.mark_as_paid()
    
    # Relatório de vendas
    store.get_sales_report()
    
    # Listar produtos (estoque atualizado)
    store.list_products()

if __name__ == "__main__":
    main()
```

**Saída (parcial):**

```
TechShop Online - Products:
==================================================
[LAPTOP001] Laptop Dell - R$ 3500.00 (5 in stock)
[MOUSE001] Wireless Mouse - R$ 85.00 (20 in stock)
[KEYB001] Mechanical Keyboard - R$ 450.00 (10 in stock)
[MONITOR001] 24" Monitor - R$ 800.00 (8 in stock)

==================================================
ORDER #1000
Customer: Alice Silva
Date: 18/01/2026 15:30
==================================================
  Laptop Dell x1 = R$ 3500.00
  Wireless Mouse x2 = R$ 170.00
--------------------------------------------------
Subtotal: R$ 3670.00
Tax (15%): R$ 550.50
TOTAL: R$ 4220.50
Status: PENDING
==================================================

Changing tax rate from 15% to 18%...

TechShop Online - Sales Report:
==================================================
Total orders: 3
Paid orders: 2
Pending orders: 1
Total revenue: R$ 8394.80
==================================================
```

### Checklist de Conceitos

**Referências:**
- [ ] Entendo que listas contêm referências
- [ ] Sei diferença entre `is` e `==`
- [ ] Sei quando objetos compartilham referência
- [ ] Posso identificar quando mudança afeta múltiplas variáveis

**Objetos como Atributos:**
- [ ] Sei usar objetos como atributos
- [ ] Entendo encadeamento com ponto (obj.attr.subattr)
- [ ] Sei quando usar `import`
- [ ] Sei criar listas de objetos como atributos
- [ ] Uso `None` apropriadamente
- [ ] Sempre verifico None antes de acessar atributos

**Encapsulamento:**
- [ ] Sei criar atributos privados com `__`
- [ ] Entendo por que encapsular
- [ ] Sei criar getters com `@property`
- [ ] Sei criar setters com `@attr.setter`
- [ ] Sempre coloco getter antes de setter
- [ ] Faço validação em setters
- [ ] Levanto exceções para valores inválidos

**Métodos Privados:**
- [ ] Sei criar métodos privados com `__`
- [ ] Entendo quando usar métodos privados
- [ ] Compreendo diferentes namespaces
- [ ] Entendo escopo de variáveis

**Class Attributes:**
- [ ] Sei criar variáveis de classe
- [ ] Acesso via `ClassName.var`
- [ ] Entendo quando usar class vs instance
- [ ] Sei criar métodos de classe com `@classmethod`
- [ ] Uso `cls` em vez de `self` em class methods
- [ ] Chamo class methods via ClassName

**Boas Práticas:**
- [ ] Nunca uso lista mutável como valor padrão
- [ ] Uso `None` como padrão e crio lista no construtor
- [ ] Encapsulo implementação interna
- [ ] Ofereço interface pública clara
- [ ] Valido dados antes de armazenar

### Armadilhas Comuns

| Erro | Problema | Solução |
|------|----------|---------|
| Não verificar None | AttributeError | `if obj is not None:` |
| `obj1 == obj2` para identidade | Compara conteúdo | Use `obj1 is obj2` |
| Modificar objeto pensando ser cópia | Referências compartilhadas | Criar cópia explícita |
| Getter após setter | NameError | Sempre `@property` antes de `.setter` |
| Tentar acessar atributo privado | AttributeError | Usar getter/setter público |
| Lista como padrão | Compartilhada entre objetos | Use `None`, crie lista no `__init__` |
| Esquecer `self` em atributo | NameError | `self.attr` não `attr` |
| `ClassName.var` em instance method | Pode funcionar mas confuso | Use `self.var` ou deixe claro |
| Método privado chamado externamente | AttributeError | Método privado só interno |

### Padrões de Design

**1. Validação Centralizada**

```python
class Person:
    def __init__(self, age: int):
        self.age = age  # Chama setter
    
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age: int):
        if age < 0:
            raise ValueError("Age cannot be negative")
        self.__age = age
```

**2. Factory Method com Class Method**

```python
class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    
    @classmethod
    def origo(cls):
        return cls(0, 0)
    
    @classmethod
    def from_tuple(cls, coords: tuple):
        return cls(coords[0], coords[1])

p1 = Point.origo()
p2 = Point.from_tuple((3, 4))
```

**3. Composição de Objetos**

```python
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.__engine = Engine()  # Composição
    
    def start(self):
        self.__engine.start()
        print("Car ready to drive")
```

**4. Lista como Atributo com Encapsulamento**

```python
class Team:
    def __init__(self, name: str):
        self.__name = name
        self.__players = []
    
    def add_player(self, player):
        self.__players.append(player)
    
    @property
    def player_count(self):
        return len(self.__players)
    
    # NÃO expor lista diretamente
    # Cliente usa métodos add_player, etc
```

**5. None para Busca Sem Resultado**

```python
class Database:
    def __init__(self):
        self.__users = {}
    
    def find_user(self, user_id: int):
        return self.__users.get(user_id)  # Retorna None se não achar
    
    def get_user_or_create(self, user_id: int):
        user = self.find_user(user_id)
        if user is None:
            user = User(user_id)
            self.__users[user_id] = user
        return user
```

---

## Próximos Passos

Na **Parte 10** você aprenderá:

- Herança de classes
- Polimorfismo
- Classes abstratas
- Múltipla herança
- Métodos especiais (dunder methods)

---

**Fonte:** University of Helsinki MOOC - Advanced Course in Programming  
**Resumo criado por:** Claude (Anthropic)  
**Para:** Eric Alcalai França
