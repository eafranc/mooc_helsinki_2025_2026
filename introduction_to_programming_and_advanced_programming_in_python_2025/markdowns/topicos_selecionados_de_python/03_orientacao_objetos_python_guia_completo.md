# Orientação a Objetos em Python - Guia Completo

## Índice
1. [[## 1. Classes e Objetos - Conceitos Básicos|Classes e Objetos - Conceitos Básicos]]
2. [[## 2. Objects and References|Objects and References]]
3. [[## 3. Objetos como Atributos|Objetos como Atributos]]
4. [[##4. Encapsulamento|Encapsulamento]]
5. [[##5. Scope de Métodos|Scope de Métodos]]
6. [[##6. Atributos de Classe|Atributos de Classe]]
7. [[#7. Métodos Especiais (__repr__, __eq__, etc)|Métodos Especiais]]
8. [[##8. Exemplo Completo Integrando Tudo|Exemplo Completo Integrando Tudo]]
9. [[##9. Perguntas e Respostas Importantes|Perguntas e Respostas Importantes]]
10. [[##10. Conceitos Fundamentais: Client, Escopo e Namespace|Conceitos Fundamentais]]
---

## 1. Classes e Objetos - Conceitos Básicos

### Definindo uma Classe Simples

```python
class Dog:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    def bark(self):
        print(f"{self.name} says: Woof!")
    
    def __str__(self):
        return f"{self.name}, {self.age} years old"

# Criando objetos (instâncias)
rex = Dog("Rex", 5)
bella = Dog("Bella", 3)

rex.bark()  # Rex says: Woof!
print(bella)  # Bella, 3 years old
```

**Conceitos:**
- `class` - define o "molde" para criar objetos
- `__init__` - construtor, executado quando criamos um objeto
- `self` - referência ao próprio objeto
- `__str__` - define como o objeto é representado como string

### Métodos vs Funções

```python
class Calculator:
    def __init__(self, initial_value: int = 0):
        self.value = initial_value
    
    def add(self, number: int):
        self.value += number
    
    def get_value(self):
        return self.value

calc = Calculator(10)
calc.add(5)  # método - trabalha com os dados do objeto
print(calc.get_value())  # 15
```

**Métodos** têm acesso aos atributos do objeto via `self`. **Funções** são independentes.

---

## 2. Objects and References

### Objetos são Referências

```python
class BankAccount:
    def __init__(self, owner: str, balance: float):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount: float):
        self.balance += amount

# Duas variáveis, MESMO objeto
account1 = BankAccount("Eric", 1000)
account2 = account1  # não cria cópia, aponta para o mesmo objeto!

account2.deposit(500)
print(account1.balance)  # 1500 (afeta o mesmo objeto!)

# Para criar cópia independente
account3 = BankAccount("Eric", 1000)  # novo objeto
```

### Objetos como Parâmetros

```python
class Player:
    def __init__(self, name: str, goals: int):
        self.name = name
        self.goals = goals

def award_bonus(player: Player, bonus_goals: int):
    player.goals += bonus_goals  # modifica o objeto original!

messi = Player("Messi", 30)
award_bonus(messi, 5)
print(messi.goals)  # 35
```

**Importante:** Quando passamos objetos para funções, passamos a **referência**, não uma cópia.

---

## 3. Objetos como Atributos

### Composição de Objetos

```python
class Course:
    def __init__(self, name: str, credits: int):
        self.name = name
        self.credits = credits

class Student:
    def __init__(self, name: str):
        self.name = name
        self.courses = []  # lista de objetos Course
    
    def enroll(self, course: Course):
        self.courses.append(course)
    
    def total_credits(self):
        total = 0
        for course in self.courses:
            total += course.credits
        return total
    
    def __str__(self):
        courses_str = ", ".join([c.name for c in self.courses])
        return f"{self.name}: {courses_str}"

# Usando
eric = Student("Eric")
python_course = Course("Python Programming", 5)
databases = Course("Databases", 4)

eric.enroll(python_course)
eric.enroll(databases)

print(eric)  # Eric: Python Programming, Databases
print(eric.total_credits())  # 9
```

### Exemplo Mais Complexo

```python
class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

class Library:
    def __init__(self, name: str):
        self.name = name
        self.books = []
    
    def add_book(self, book: Book):
        self.books.append(book)
    
    def search_by_author(self, author: str):
        found = []
        for book in self.books:
            if book.author == author:
                found.append(book)
        return found

# Usando
library = Library("City Library")
library.add_book(Book("The Metamorphosis", "Kafka"))
library.add_book(Book("The Trial", "Kafka"))
library.add_book(Book("Crime and Punishment", "Dostoevsky"))

kafka_books = library.search_by_author("Kafka")
for book in kafka_books:
    print(book.title)
```

---

## 4. Encapsulamento

### Atributos Privados

```python
class BankAccount:
    def __init__(self, owner: str, balance: float):
        self.__owner = owner      # privado
        self.__balance = balance  # privado
    
    def deposit(self, amount: float):
        if amount > 0:
            self.__balance += amount
    
    def withdraw(self, amount: float):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            raise ValueError("Invalid amount")
    
    def get_balance(self):
        return self.__balance

account = BankAccount("Eric", 1000)
# account.__balance = 999999  # Não funciona diretamente
account.deposit(500)
print(account.get_balance())  # 1500
```

### Properties (Getters e Setters)

```python
class Temperature:
    def __init__(self, celsius: float):
        self.__celsius = celsius
    
    # Getter
    @property
    def celsius(self):
        return self.__celsius
    
    # Setter
    @celsius.setter
    def celsius(self, value: float):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self.__celsius = value
    
    # Propriedade computada (só getter)
    @property
    def fahrenheit(self):
        return self.__celsius * 9/5 + 32

# Usando
temp = Temperature(25)
print(temp.celsius)      # 25 (usa o getter)
print(temp.fahrenheit)   # 77.0
temp.celsius = 30        # usa o setter
# temp.celsius = -300    # ValueError!
```

### Exemplo Completo de Encapsulamento

```python
class CreditCard:
    def __init__(self, number: str, holder: str, limit: float):
        self.__number = number
        self.__holder = holder
        self.__limit = limit
        self.__balance = 0.0
    
    @property
    def balance(self):
        return self.__balance
    
    @property
    def available_credit(self):
        return self.__limit - self.__balance
    
    def charge(self, amount: float):
        if amount > self.available_credit:
            raise ValueError("Credit limit exceeded")
        self.__balance += amount
    
    def pay(self, amount: float):
        if amount > 0:
            self.__balance -= amount
    
    def __str__(self):
        # Mascara o número do cartão
        masked = "**** **** **** " + self.__number[-4:]
        return f"{masked} - {self.__holder}"

card = CreditCard("1234567890123456", "Eric Silva", 5000)
card.charge(1000)
print(card.balance)  # 1000
print(card.available_credit)  # 4000
print(card)  # **** **** **** 3456 - Eric Silva
```

---

## 5. Scope de Métodos

### Métodos Chamando Outros Métodos

```python
class ShoppingCart:
    def __init__(self):
        self.__items = []
    
    def add_item(self, name: str, price: float):
        self.__items.append({"name": name, "price": price})
    
    def __calculate_total(self):  # método privado
        total = 0
        for item in self.__items:
            total += item["price"]
        return total
    
    def __calculate_discount(self, total: float):  # método privado
        if total > 100:
            return total * 0.1
        return 0
    
    def get_final_price(self):  # método público que usa os privados
        total = self.__calculate_total()
        discount = self.__calculate_discount(total)
        return total - discount

cart = ShoppingCart()
cart.add_item("Book", 50)
cart.add_item("Headphones", 80)
print(cart.get_final_price())  # 117.0 (130 - 10% desconto)
```

### Métodos Auxiliares

```python
class TextAnalyzer:
    def __init__(self, text: str):
        self.__text = text
    
    def __clean_text(self):
        return self.__text.lower().strip()
    
    def __split_words(self):
        cleaned = self.__clean_text()
        return cleaned.split()
    
    def word_count(self):
        words = self.__split_words()
        return len(words)
    
    def most_common_word(self):
        words = self.__split_words()
        word_freq = {}
        for word in words:
            word_freq[word] = word_freq.get(word, 0) + 1
        
        max_count = 0
        most_common = ""
        for word, count in word_freq.items():
            if count > max_count:
                max_count = count
                most_common = word
        return most_common

analyzer = TextAnalyzer("  Python is great Python is fun  ")
print(analyzer.word_count())  # 6
print(analyzer.most_common_word())  # python
```

---

## 6. Atributos de Classe

### Diferença: Atributos de Instância vs Classe

```python
class Player:
    # Atributo de CLASSE (compartilhado por todos)
    total_players = 0
    
    def __init__(self, name: str):
        # Atributo de INSTÂNCIA (único para cada objeto)
        self.name = name
        Player.total_players += 1  # acessa atributo de classe
    
    @classmethod
    def get_total_players(cls):
        return cls.total_players

# Criando jogadores
p1 = Player("Messi")
p2 = Player("Ronaldo")
p3 = Player("Neymar")

print(Player.total_players)  # 3
print(Player.get_total_players())  # 3
```

### Exemplo Prático: Contador de IDs

```python
class Task:
    next_id = 1  # atributo de classe
    
    def __init__(self, description: str):
        self.id = Task.next_id
        self.description = description
        self.completed = False
        Task.next_id += 1  # incrementa para próxima task
    
    def complete(self):
        self.completed = True
    
    def __str__(self):
        status = "✓" if self.completed else "○"
        return f"[{self.id}] {status} {self.description}"

# Usando
task1 = Task("Study Python")
task2 = Task("Practice exercises")
task3 = Task("Review code")

task1.complete()

print(task1)  # [1] ✓ Study Python
print(task2)  # [2] ○ Practice exercises
print(task3)  # [3] ○ Review code
```

### Constantes de Classe

```python
class Configuration:
    # Constantes (convenção: MAIÚSCULAS)
    MAX_LOGIN_ATTEMPTS = 3
    SESSION_TIMEOUT = 1800  # segundos
    DEFAULT_LANGUAGE = "pt-BR"
    
    def __init__(self, username: str):
        self.username = username
        self.login_attempts = 0
    
    def try_login(self, password: str):
        if self.login_attempts >= Configuration.MAX_LOGIN_ATTEMPTS:
            raise Exception("Account locked")
        
        # lógica de verificação de senha aqui
        self.login_attempts += 1

user = Configuration("eric")
print(Configuration.MAX_LOGIN_ATTEMPTS)  # 3
```

---

## 7. Métodos Especiais (__repr__, __eq__, etc)

### __repr__ vs __str__

```python
class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year
    
    def __str__(self):
        # Para usuários finais
        return f'"{self.title}" by {self.author}'
    
    def __repr__(self):
        # Para desenvolvedores (deve permitir recriar objeto)
        return f'Book("{self.title}", "{self.author}", {self.year})'

book = Book("The Metamorphosis", "Kafka", 1915)
print(str(book))   # "The Metamorphosis" by Kafka
print(repr(book))  # Book("The Metamorphosis", "Kafka", 1915)
```

### Comparação de Objetos

```python
class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price
    
    def __eq__(self, other):
        # Define igualdade
        return self.name == other.name and self.price == other.price
    
    def __lt__(self, other):
        # Define "menor que" (para ordenação)
        return self.price < other.price
    
    def __str__(self):
        return f"{self.name}: R$ {self.price:.2f}"

p1 = Product("Mouse", 50.00)
p2 = Product("Keyboard", 150.00)
p3 = Product("Mouse", 50.00)

print(p1 == p3)  # True (mesmo nome e preço)
print(p1 == p2)  # False
print(p1 < p2)   # True (50 < 150)

# Agora podemos ordenar!
products = [p2, p1, Product("Monitor", 800)]
products.sort()
for p in products:
    print(p)
```

---

## 8. Exemplo Completo Integrando Tudo

```python
class Transaction:
    next_id = 1
    
    def __init__(self, amount: float, description: str):
        self.id = Transaction.next_id
        self.amount = amount
        self.description = description
        Transaction.next_id += 1
    
    def __str__(self):
        return f"#{self.id}: {self.description} - R$ {self.amount:.2f}"

class BankAccount:
    def __init__(self, owner: str, initial_balance: float = 0):
        self.__owner = owner
        self.__balance = initial_balance
        self.__transactions = []
    
    @property
    def owner(self):
        return self.__owner
    
    @property
    def balance(self):
        return self.__balance
    
    def __validate_amount(self, amount: float):
        if amount <= 0:
            raise ValueError("Amount must be positive")
    
    def deposit(self, amount: float, description: str = "Deposit"):
        self.__validate_amount(amount)
        self.__balance += amount
        transaction = Transaction(amount, description)
        self.__transactions.append(transaction)
    
    def withdraw(self, amount: float, description: str = "Withdrawal"):
        self.__validate_amount(amount)
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount
        transaction = Transaction(-amount, description)
        self.__transactions.append(transaction)
    
    def get_statement(self):
        print(f"Account Statement - {self.__owner}")
        print("=" * 50)
        for transaction in self.__transactions:
            print(transaction)
        print("=" * 50)
        print(f"Current Balance: R$ {self.__balance:.2f}")
    
    def __str__(self):
        return f"Account of {self.__owner}: R$ {self.__balance:.2f}"

# Usando
account = BankAccount("Eric Silva", 1000)
account.deposit(500, "Salary")
account.withdraw(200, "Grocery shopping")
account.deposit(100, "Freelance work")

print(account)
account.get_statement()
```

**Output:**
```
Account of Eric Silva: R$ 1400.00
Account Statement - Eric Silva
==================================================
#1: Salary - R$ 500.00
#2: Grocery shopping - R$ -200.00
#3: Freelance work - R$ 100.00
==================================================
Current Balance: R$ 1400.00
```

---

## 9. Perguntas e Respostas Importantes

### 9.1 Type Hints em Métodos Especiais (`__eq__`, etc)

**Pergunta:** Preciso colocar type hint no parâmetro `other` do método `__eq__`?

**Resposta:** Sim! Você deveria adicionar o type hint. Ficaria assim:

```python
def __eq__(self, other: "Product") -> bool:
    return self.name == other.name and self.price == other.price
```

**Por que as aspas?** Porque quando você está **dentro** da definição da classe `Product`, o nome `Product` ainda não está completamente definido. As aspas fazem uma "forward reference" (referência futura).

**Alternativa moderna (Python 3.10+):**
```python
from __future__ import annotations

class Product:
    def __eq__(self, other: Product) -> bool:  # sem aspas!
        return self.name == other.name and self.price == other.price
```

---

### 9.2 Getter/Setter para Listas e Dicionários

**Pergunta:** Faz sentido criar getter e setter para atributos que são listas ou dicionários?

**Resposta:** Depende do que você quer permitir. Vejamos as opções:

#### Opção 1: Não expor a lista (mais restritivo)

```python
class ShoppingCart:
    def __init__(self):
        self.__items = []
    
    def add_item(self, name: str, price: float):
        self.__items.append({"name": name, "price": price})
    
    def remove_item(self, name: str):
        self.__items = [item for item in self.__items if item["name"] != name]
    
    def get_items_count(self):
        return len(self.__items)
    
    def get_total(self):
        return sum(item["price"] for item in self.__items)
```

**Vantagem:** Controle total. Ninguém pode estragar sua lista.

#### Opção 2: Getter que retorna cópia (seguro)

```python
class ShoppingCart:
    def __init__(self):
        self.__items = []
    
    @property
    def items(self):
        # Retorna CÓPIA, não a lista original
        return self.__items.copy()
    
    def add_item(self, name: str, price: float):
        self.__items.append({"name": name, "price": price})

cart = ShoppingCart()
cart.add_item("Book", 50)

# Isso NÃO afeta a lista interna (é uma cópia)
items_copy = cart.items
items_copy.append({"name": "Hacked!", "price": 0})

print(len(cart.items))  # 1 (não foi afetado)
```

**Vantagem:** Permite leitura segura sem expor a lista original.

#### Opção 3: Getter sem setter (somente leitura) - PERIGOSO

```python
class Student:
    def __init__(self, name: str):
        self.__name = name
        self.__grades = []
    
    @property
    def grades(self):
        # CUIDADO: retorna a lista original (perigoso!)
        return self.__grades
    
    def add_grade(self, grade: float):
        if 0 <= grade <= 10:
            self.__grades.append(grade)

student = Student("Eric")
student.add_grade(9.5)

# Isso é PERIGOSO e funciona:
student.grades.append(15)  # bypassa a validação!
print(student.grades)  # [9.5, 15] - valor inválido entrou!
```

**Problema:** Se você retorna a lista original, o usuário pode modificá-la diretamente.

#### Opção 4: Property com validação (mais usado na prática)

```python
class Configuration:
    def __init__(self):
        self.__allowed_ips = []
    
    @property
    def allowed_ips(self):
        return self.__allowed_ips.copy()  # retorna cópia
    
    @allowed_ips.setter
    def allowed_ips(self, ip_list: list):
        # Valida cada IP antes de aceitar
        for ip in ip_list:
            if not self.__validate_ip(ip):
                raise ValueError(f"Invalid IP: {ip}")
        self.__allowed_ips = ip_list.copy()
    
    def __validate_ip(self, ip: str):
        parts = ip.split(".")
        if len(parts) != 4:
            return False
        try:
            return all(0 <= int(part) <= 255 for part in parts)
        except ValueError:
            return False

config = Configuration()
config.allowed_ips = ["192.168.1.1", "10.0.0.1"]  # OK
# config.allowed_ips = ["999.999.999.999"]  # ValueError!
```

#### Resposta Prática:

Na prática, você geralmente:
- **Não cria setter** para listas/dicionários complexos
- **Cria métodos específicos** (`add_item`, `remove_item`) para controlar modificações
- **Se criar getter, retorna cópia** para evitar modificação acidental

---

### 9.3 Acessando Atributos de Classe

**Pergunta:** Como acessar atributos de classe?

**Resposta:** Atributos de classe são acessados de **duas formas**:

#### Forma 1: Pelo nome da classe

```python
class Player:
    total_players = 0  # atributo de classe
    
    def __init__(self, name: str):
        self.name = name  # atributo de instância
        Player.total_players += 1

# Acessando ANTES de criar qualquer objeto
print(Player.total_players)  # 0

p1 = Player("Messi")
p2 = Player("Ronaldo")

print(Player.total_players)  # 2
```

#### Forma 2: Por uma instância (mas cuidado!)

```python
class Dog:
    species = "Canis familiaris"  # atributo de classe
    
    def __init__(self, name: str):
        self.name = name

rex = Dog("Rex")

# Acesso por instância
print(rex.species)  # "Canis familiaris"

# Acesso pela classe
print(Dog.species)  # "Canis familiaris"

# CUIDADO: isso cria atributo de INSTÂNCIA, não modifica o de classe!
rex.species = "Canis lupus"

print(rex.species)     # "Canis lupus" (atributo de instância)
print(Dog.species)     # "Canis familiaris" (atributo de classe não mudou!)

bella = Dog("Bella")
print(bella.species)   # "Canis familiaris" (usa o da classe)
```

#### Modificando Atributo de Classe

```python
class Configuration:
    debug_mode = False  # atributo de classe
    
    @classmethod
    def enable_debug(cls):
        cls.debug_mode = True

# Modificando pela classe
Configuration.debug_mode = True

# Ou por método de classe
Configuration.enable_debug()
```

---

### 9.4 Métodos servem APENAS para manipular atributos?

**Pergunta:** Métodos só servem para manipular os atributos da classe?

**Resposta:** Não! Métodos podem fazer muito mais:

#### Exemplo 1: Cálculos sem modificar estado

```python
class Calculator:
    @staticmethod
    def add(a: int, b: int) -> int:
        return a + b  # não usa self, não acessa atributos
    
    @staticmethod
    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

# Uso sem criar objeto
print(Calculator.add(5, 3))      # 8
print(Calculator.is_prime(17))   # True
```

#### Exemplo 2: Factory Methods (criar objetos)

```python
from datetime import datetime

class Person:
    def __init__(self, name: str, birth_year: int):
        self.name = name
        self.birth_year = birth_year
    
    @classmethod
    def from_birth_date(cls, name: str, birth_date: str):
        # Método que cria objeto de forma alternativa
        year = int(birth_date.split("-")[0])
        return cls(name, year)
    
    def get_age(self):
        return datetime.now().year - self.birth_year

# Duas formas de criar
person1 = Person("Eric", 1990)
person2 = Person.from_birth_date("Ana", "1985-05-20")

print(person1.get_age())
print(person2.get_age())
```

#### Exemplo 3: Validações e Formatações

```python
class EmailValidator:
    @staticmethod
    def is_valid(email: str) -> bool:
        return "@" in email and "." in email.split("@")[1]
    
    @staticmethod
    def normalize(email: str) -> str:
        return email.lower().strip()

print(EmailValidator.is_valid("eric@example.com"))  # True
print(EmailValidator.normalize("  ERIC@Example.COM  "))  # eric@example.com
```

#### Resumo:

Métodos podem:
1. ✅ Manipular atributos de instância (`self.attribute`)
2. ✅ Acessar/modificar atributos de classe (`cls.attribute` ou `ClassName.attribute`)
3. ✅ Fazer cálculos e retornar valores sem tocar em atributos
4. ✅ Criar novos objetos (factory methods)
5. ✅ Validar dados
6. ✅ Formatar outputs
7. ✅ Interagir com outros objetos

O importante é que métodos **pertencem semanticamente** à classe, mesmo que não necessariamente usem seus atributos.

---

## 10. Conceitos Fundamentais: Client, Escopo e Namespace

### 10.1 Client (Cliente) no contexto de OOP

**Client** é o código que **usa** uma classe, não o código que **define** a classe.

#### Exemplo Simples:

```python
# Esta é a CLASSE (o "servidor" de funcionalidades)
class BankAccount:
    def __init__(self, owner: str, balance: float):
        self.__balance = balance
        self.owner = owner
    
    def deposit(self, amount: float):
        self.__balance += amount
    
    def get_balance(self):
        return self.__balance

# Este é o CLIENT (quem USA a classe)
account = BankAccount("Eric", 1000)  # cliente criando objeto
account.deposit(500)                  # cliente usando método
print(account.get_balance())          # cliente consultando saldo
```

O **client** (cliente) é simplesmente qualquer código que instancia e interage com objetos de uma classe.

#### Por que o termo "client"?

A analogia vem da relação cliente-servidor:
- A **classe** oferece serviços (métodos)
- O **client** consome esses serviços

#### Perspectiva do Encapsulamento:

```python
class EmailSender:
    def __init__(self, smtp_server: str):
        self.__server = smtp_server
        self.__connection = None
    
    def __connect(self):  # método PRIVADO
        # lógica complexa de conexão
        print(f"Connecting to {self.__server}")
        self.__connection = "connected"
    
    def __disconnect(self):  # método PRIVADO
        print("Disconnecting...")
        self.__connection = None
    
    def send_email(self, to: str, subject: str, body: str):  # método PÚBLICO
        # O CLIENT só vê este método simples
        self.__connect()
        print(f"Sending email to {to}: {subject}")
        self.__disconnect()

# CLIENT CODE (código cliente)
# O cliente não precisa saber sobre conexões, só usa o serviço
mailer = EmailSender("smtp.gmail.com")
mailer.send_email("eric@example.com", "Hello", "Test message")
# O cliente NÃO pode (e não deve) chamar __connect() diretamente
```

**Ponto importante:** Quando você projeta uma classe, pensa em duas perspectivas:
1. **Implementação interna** - como a classe funciona por dentro
2. **Interface pública (API)** - o que o **client** pode/deve usar

#### Exemplo Prático:

```python
class ShoppingCart:
    def __init__(self):
        self.__items = []
        self.__discount_rate = 0
    
    # Métodos PÚBLICOS (interface para o client)
    def add_item(self, name: str, price: float):
        self.__items.append({"name": name, "price": price})
    
    def apply_discount(self, rate: float):
        if 0 <= rate <= 0.5:  # máximo 50% desconto
            self.__discount_rate = rate
    
    def get_total(self):
        subtotal = self.__calculate_subtotal()
        return subtotal * (1 - self.__discount_rate)
    
    # Método PRIVADO (implementação interna, cliente não vê)
    def __calculate_subtotal(self):
        return sum(item["price"] for item in self.__items)

# ===== CLIENT CODE (usuário da classe) =====
cart = ShoppingCart()
cart.add_item("Book", 50)
cart.add_item("Pen", 5)
cart.apply_discount(0.1)  # 10% desconto
print(f"Total: ${cart.get_total()}")

# O cliente SÓ usa a interface pública
# Não precisa saber que existe __calculate_subtotal()
```

---

### 10.2 Escopo (Scope) no contexto de OOP

**Escopo** define **onde** uma variável ou método pode ser acessado.

#### Tipos de Escopo em Python OOP:

##### 1. Escopo Local (dentro de um método)

```python
class Calculator:
    def add(self, a: int, b: int):
        result = a + b  # 'result' tem escopo LOCAL
        return result
    
    def multiply(self, a: int, b: int):
        # 'result' do método add() NÃO existe aqui
        # print(result)  # ERRO! NameError
        product = a * b
        return product

calc = Calculator()
# print(result)  # ERRO! 'result' só existe dentro do método
```

##### 2. Escopo de Instância (atributos do objeto)

```python
class Person:
    def __init__(self, name: str, age: int):
        self.name = name  # escopo de INSTÂNCIA
        self.age = age    # escopo de INSTÂNCIA
    
    def greet(self):
        # Dentro dos métodos, acesso via 'self'
        print(f"Hi, I'm {self.name}")
    
    def birthday(self):
        self.age += 1  # modificando atributo de instância

person = Person("Eric", 30)
# Fora da classe, acesso via objeto
print(person.name)  # OK
person.greet()      # OK
```

##### 3. Escopo de Classe (atributos compartilhados)

```python
class Employee:
    company_name = "TechCorp"  # escopo de CLASSE
    total_employees = 0        # escopo de CLASSE
    
    def __init__(self, name: str):
        self.name = name  # escopo de INSTÂNCIA
        Employee.total_employees += 1
    
    def show_company(self):
        # Acesso ao atributo de classe
        print(f"I work at {Employee.company_name}")

# Acesso ao escopo de classe SEM criar instância
print(Employee.company_name)  # "TechCorp"
print(Employee.total_employees)  # 0

emp1 = Employee("Eric")
emp2 = Employee("Ana")

print(Employee.total_employees)  # 2
```

##### 4. Escopo Privado (atributos/métodos com `__`)

```python
class BankAccount:
    def __init__(self, balance: float):
        self.__balance = balance  # escopo PRIVADO
        self.account_type = "Savings"  # escopo PÚBLICO
    
    def __validate(self, amount):  # método PRIVADO
        return amount > 0
    
    def deposit(self, amount: float):
        if self.__validate(amount):  # OK dentro da classe
            self.__balance += amount

account = BankAccount(1000)
# print(account.__balance)  # ERRO! AttributeError
print(account.account_type)  # OK (público)
```

#### Regras de Resolução de Escopo (LEGB Rule):

Python procura variáveis nesta ordem:
1. **L**ocal - dentro da função/método atual
2. **E**nclosing - funções externas (closures)
3. **G**lobal - nível do módulo
4. **B**uilt-in - funções Python embutidas

```python
company = "Global Corp"  # escopo GLOBAL

class Employee:
    company = "Class Corp"  # escopo de CLASSE
    
    def __init__(self, name):
        self.name = name
    
    def show_company(self):
        company = "Local Corp"  # escopo LOCAL
        print(company)  # usa LOCAL
    
    def show_class_company(self):
        print(Employee.company)  # usa CLASSE
    
    def show_global_company(self):
        print(globals()['company'])  # força GLOBAL

emp = Employee("Eric")
emp.show_company()         # "Local Corp"
emp.show_class_company()   # "Class Corp"
emp.show_global_company()  # "Global Corp"
```

---

### 10.3 Namespace no contexto de OOP

**Namespace** é um "container" que mapeia nomes para objetos. Pense nele como um **dicionário de nomes**.

#### Namespaces em OOP:

##### 1. Namespace de Classe

```python
class Car:
    wheels = 4  # no namespace da CLASSE
    
    def __init__(self, model: str):
        self.model = model  # no namespace da INSTÂNCIA
    
    def honk(self):  # no namespace da CLASSE
        print("Beep!")

# Visualizando namespaces
print(Car.__dict__)
# {'wheels': 4, 'honk': <function>, '__init__': <function>, ...}
```

##### 2. Namespace de Instância

```python
class Person:
    species = "Homo sapiens"  # namespace de CLASSE
    
    def __init__(self, name: str, age: int):
        self.name = name  # namespace de INSTÂNCIA
        self.age = age    # namespace de INSTÂNCIA

eric = Person("Eric", 30)
ana = Person("Ana", 25)

# Cada instância tem seu próprio namespace
print(eric.__dict__)  # {'name': 'Eric', 'age': 30}
print(ana.__dict__)   # {'name': 'Ana', 'age': 25}

# Mas compartilham o namespace de classe
print(Person.__dict__)  # {'species': 'Homo sapiens', ...}
```

##### 3. Namespaces Separados Evitam Conflitos

```python
class Student:
    def __init__(self, name: str):
        self.name = name
        self.grade = None
    
    def grade(self):  # ERRO! Conflito de nomes
        return self.grade

# Isso dá erro porque 'grade' é tanto atributo quanto método
# Python não sabe se você quer o atributo ou o método
```

**Solução:** Use nomes diferentes!

```python
class Student:
    def __init__(self, name: str):
        self.name = name
        self.__grade = None  # atributo privado
    
    def get_grade(self):  # método com nome diferente
        return self.__grade
    
    def set_grade(self, grade: float):
        self.__grade = grade
```

#### Exemplo Completo: Namespaces em Ação

```python
class University:
    # Namespace de CLASSE
    name = "USP"
    total_students = 0
    
    def __init__(self, campus: str):
        # Namespace de INSTÂNCIA
        self.campus = campus
        self.students = []
        University.total_students += 1
    
    def add_student(self, student_name: str):
        # Namespace LOCAL (variável temporária)
        new_student = {"name": student_name, "enrolled": True}
        self.students.append(new_student)

# Criando instâncias
sao_carlos = University("São Carlos")
sao_paulo = University("São Paulo")

# Namespaces diferentes para cada instância
print(sao_carlos.__dict__)
# {'campus': 'São Carlos', 'students': []}

print(sao_paulo.__dict__)
# {'campus': 'São Paulo', 'students': []}

# Namespace de classe é compartilhado
print(University.__dict__['name'])  # "USP"
print(University.total_students)    # 2
```

#### Importância dos Namespaces:

**1. Evitam conflitos de nomes:**
```python
class MathUtils:
    @staticmethod
    def max(a, b):  # não conflita com built-in max()
        return a if a > b else b

print(max([1, 2, 3]))        # built-in max
print(MathUtils.max(5, 10))  # nosso max
```

**2. Organizam código:**
```python
class Database:
    class Connection:  # namespace aninhado
        def __init__(self, host: str):
            self.host = host
    
    class Query:  # namespace aninhado
        def __init__(self, sql: str):
            self.sql = sql

# Acesso via namespace hierárquico
conn = Database.Connection("localhost")
query = Database.Query("SELECT * FROM users")
```

---

### 10.4 Resumo Visual

```
┌─────────────────────────────────────────────┐
│            NAMESPACE DE CLASSE              │
│  • Atributos de classe                      │
│  • Métodos                                  │
│  • Constantes                               │
│  (compartilhado por todas as instâncias)    │
└─────────────────────────────────────────────┘
                    ▲
                    │
        ┌───────────┴───────────┐
        │                       │
┌───────▼─────────┐    ┌────────▼────────┐
│  NAMESPACE      │    │  NAMESPACE      │
│  INSTÂNCIA 1    │    │  INSTÂNCIA 2    │
│  • self.attr1   │    │  • self.attr1   │
│  • self.attr2   │    │  • self.attr2   │
└─────────────────┘    └─────────────────┘

CLIENT CODE (fora da classe)
• Usa interface pública
• Não vê implementação privada
• Acessa via objetos ou nome da classe
```

**Pontos-chave:**
- **Client**: código que usa a classe
- **Escopo**: onde variáveis/métodos podem ser acessados
- **Namespace**: mapeamento de nomes para valores
- Cada instância tem seu próprio namespace
- A classe tem um namespace compartilhado
- Escopos privados (`__`) limitam acesso do client

---

## Resumo dos Conceitos-Chave

1. **Classes** definem o molde, **objetos** são instâncias concretas
2. **`self`** refere-se ao próprio objeto
3. **`__init__`** inicializa o objeto
4. **Atributos privados** (`__attribute`) protegem dados
5. **Properties** (`@property`) criam getters/setters elegantes
6. **Atributos de classe** são compartilhados entre todas as instâncias
7. **Métodos especiais** (`__str__`, `__repr__`, `__eq__`) customizam comportamento
8. **Composição** permite objetos conterem outros objetos
9. **Encapsulamento** esconde detalhes de implementação
10. **Type hints** melhoram legibilidade e ajudam ferramentas de análise
11. **Client** é o código que usa a classe (perspectiva externa)
12. **Escopo** define onde variáveis/métodos podem ser acessados
13. **Namespace** organiza nomes e evita conflitos

---

## Boas Práticas

### Nomenclatura
- Classes: `PascalCase` (ex: `BankAccount`, `ShoppingCart`)
- Métodos e atributos: `snake_case` (ex: `add_item`, `get_balance`)
- Constantes de classe: `UPPER_CASE` (ex: `MAX_ATTEMPTS`)
- Atributos/métodos privados: prefixo `__` (ex: `__balance`)
- Atributos/métodos "internos": prefixo `_` (ex: `_helper_method`)

### Encapsulamento
- Use atributos privados (`__attribute`) para dados sensíveis
- Forneça properties quando precisar de validação
- Retorne cópias de listas/dicionários em getters
- Crie métodos específicos em vez de setters para coleções

### Documentação
```python
class BankAccount:
    """
    Representa uma conta bancária com operações básicas.
    
    Attributes:
        owner (str): Nome do titular da conta
        balance (float): Saldo atual da conta
    """
    
    def __init__(self, owner: str, initial_balance: float = 0):
        """
        Inicializa uma nova conta bancária.
        
        Args:
            owner: Nome do titular
            initial_balance: Saldo inicial (padrão: 0)
        
        Raises:
            ValueError: Se o saldo inicial for negativo
        """
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative")
        self.__owner = owner
        self.__balance = initial_balance
```

---

**Criado por:** Claude (Anthropic)  
**Baseado em:** Conversa com Eric Alcalai França  
**Data:** Dezembro 2024  
**Fonte:** University of Helsinki MOOC - Advanced Programming in Python (Partes 8-9)
