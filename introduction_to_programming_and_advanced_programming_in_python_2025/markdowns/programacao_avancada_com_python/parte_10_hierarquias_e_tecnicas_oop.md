# Parte 10 - Hierarquias de Classes e Técnicas OOP

> **Fonte:** University of Helsinki - Python Programming MOOC
> **Resumo criado por:** Claude (Anthropic)
> **Para:** Eric Alcalai França

---

## Índice

- [[#Seção 1 - Hierarquias de Classes (Herança)]]
- [[#Seção 2 - Modificadores de Acesso]]
- [[#Seção 3 - Técnicas de Programação Orientada a Objetos]]
- [[#Seção 4 - Desenvolvendo uma Aplicação Maior]]
- [[#Conceitos-Chave]]
- [[#Resumo Rápido]]

---

## Seção 1 - Hierarquias de Classes (Herança)

### O Problema da Repetição

Quando temos classes similares com atributos em comum, acabamos repetindo código:

```python
# ❌ Código repetido - name e email aparecem nas duas classes
class Student:
    def __init__(self, name: str, id: str, email: str, credits: int):
        self.name = name      # repetido
        self.id = id
        self.email = email    # repetido
        self.credits = credits

class Teacher:
    def __init__(self, name: str, email: str, room: str, teaching_years: int):
        self.name = name      # repetido
        self.email = email    # repetido
        self.room = room
        self.teaching_years = teaching_years
```

### Solução: Herança (Inheritance)

Uma classe pode **herdar** traits (atributos e métodos) de outra classe:

```python
# ✅ Classe base com atributos comuns
class Person:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    def update_email_domain(self, new_domain: str):
        old_domain = self.email.split("@")[1]
        self.email = self.email.replace(old_domain, new_domain)


# Classes derivadas herdam de Person
class Student(Person):  # Sintaxe: classe base entre parênteses
    def __init__(self, name: str, id: str, email: str, credits: int):
        self.name = name
        self.id = id
        self.email = email
        self.credits = credits


class Teacher(Person):
    def __init__(self, name: str, email: str, room: str, teaching_years: int):
        self.name = name
        self.email = email
        self.room = room
        self.teaching_years = teaching_years


# Teste - ambas as classes têm acesso ao método herdado
saul = Student("Saul Student", "1234", "saul@example.com", 0)
saul.update_email_domain("example.edu")  # método herdado!
print(saul.email)  # saul@example.edu

tara = Teacher("Tara Teacher", "tara@example.fi", "A123", 2)
tara.update_email_domain("example.ex")
print(tara.email)  # tara@example.ex
```

### Terminologia

| Termo | Sinônimos | Descrição |
|-------|-----------|-----------|
| **Classe Base** | Parent class, Superclass | Classe da qual se herda |
| **Classe Derivada** | Child class, Subclass | Classe que herda |
| **Herança** | Inheritance | Mecanismo de reutilização |

### Overriding (Sobrescrita de Métodos)

A classe derivada pode **redefinir** um método da classe base:

```python
class Book:
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author


class BookContainer:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)  # adiciona no final

    def list_books(self):
        for book in self.books:
            print(f"{book.name} ({book.author})")


class Bookshelf(BookContainer):
    def __init__(self):
        super().__init__()  # chama construtor da classe base

    # OVERRIDE: redefine add_book com parâmetro extra
    def add_book(self, book: Book, location: int):
        self.books.insert(location, book)  # insere em posição específica


# Teste
b1 = Book("O Velho e o Mar", "Hemingway")
b2 = Book("Primavera Silenciosa", "Rachel Carson")
b3 = Book("Orgulho e Preconceito", "Jane Austen")

container = BookContainer()
container.add_book(b1)
container.add_book(b2)
container.add_book(b3)

shelf = Bookshelf()
shelf.add_book(b1, 0)  # sempre no início
shelf.add_book(b2, 0)
shelf.add_book(b3, 0)

print("Container:")
container.list_books()
# O Velho e o Mar, Primavera Silenciosa, Orgulho e Preconceito

print("\nShelf:")
shelf.list_books()
# Orgulho e Preconceito, Primavera Silenciosa, O Velho e o Mar (ordem inversa!)
```

### A Função super()

`super()` acessa métodos e atributos da classe base:

```python
class Book:
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author


class Thesis(Book):
    def __init__(self, name: str, author: str, grade: int):
        # Chama o construtor da classe base
        super().__init__(name, author)  # sem self!
        # Adiciona atributo específico da classe derivada
        self.grade = grade


thesis = Thesis("Python e o Universo", "Peter Pythons", 3)
print(thesis.name)   # Python e o Universo (herdado)
print(thesis.author) # Peter Pythons (herdado)
print(thesis.grade)  # 3 (específico)
```

### Chamando Método Sobrescrito da Base

Mesmo após override, ainda podemos chamar o método original:

```python
class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price


class BonusCard:
    def __init__(self):
        self.products_bought = []

    def add_product(self, product: Product):
        self.products_bought.append(product)

    def calculate_bonus(self):
        bonus = 0
        for product in self.products_bought:
            bonus += product.price * 0.05  # 5% de bônus
        return bonus


class PlatinumCard(BonusCard):
    def __init__(self):
        super().__init__()

    def calculate_bonus(self):
        # Chama o método da classe base
        bonus = super().calculate_bonus()
        # Adiciona 5% extra ao resultado
        bonus = bonus * 1.05
        return bonus


# Teste
card = BonusCard()
card.add_product(Product("Bananas", 6.50))
card.add_product(Product("Tangerinas", 7.95))
print(card.calculate_bonus())  # 0.7225

platinum = PlatinumCard()
platinum.add_product(Product("Bananas", 6.50))
platinum.add_product(Product("Tangerinas", 7.95))
print(platinum.calculate_bonus())  # 0.7586... (5% a mais)
```

---

## Seção 2 - Modificadores de Acesso

### O Problema com Atributos Privados

Atributos privados (`__nome`) não são acessíveis em classes derivadas:

```python
class Notebook:
    def __init__(self):
        self.__notes = []  # PRIVADO

    def add_note(self, note):
        self.__notes.append(note)


class NotebookPro(Notebook):
    def __init__(self):
        super().__init__()

    def find_notes(self, search_term):
        found = []
        # ❌ ERRO! __notes é privado
        for note in self.__notes:
            if search_term in note:
                found.append(note)
        return found

# AttributeError: 'NotebookPro' object has no attribute '_NotebookPro__notes'
```

### Solução: Atributos Protegidos

Use **um único underscore** para indicar atributo protegido:

```python
class Notebook:
    def __init__(self):
        self._notes = []  # PROTEGIDO (convenção)

    def add_note(self, note):
        self._notes.append(note)

    def retrieve_note(self, index):
        return self._notes[index]

    def all_notes(self):
        return ",".join(self._notes)


class NotebookPro(Notebook):
    def __init__(self):
        super().__init__()

    def find_notes(self, search_term):
        found = []
        # ✅ Funciona! _notes é protegido, acessível na derivada
        for note in self._notes:
            if search_term in note:
                found.append(note)
        return found
```

### Tabela de Visibilidade

| Modificador | Sintaxe | Cliente Externo | Classe Derivada |
|-------------|---------|-----------------|-----------------|
| **Public** | `self.name` | ✅ Sim | ✅ Sim |
| **Protected** | `self._name` | ❌ Não* | ✅ Sim |
| **Private** | `self.__name` | ❌ Não | ❌ Não |

> *Tecnicamente acessível, mas convenção diz para não usar externamente.

### Métodos Também Podem Ser Protegidos

```python
class Person:
    def __init__(self, name: str):
        self._name = self._capitalize_initials(name)

    def _capitalize_initials(self, name):  # PROTEGIDO
        name_capitalized = []
        for n in name.split(" "):
            name_capitalized.append(n.capitalize())
        return " ".join(name_capitalized)


class Footballer(Person):
    def __init__(self, name: str, nickname: str, position: str):
        super().__init__(name)
        # ✅ Método protegido acessível na derivada
        self.__nickname = self._capitalize_initials(nickname)
        self.__position = position

    def __repr__(self):
        return f"Footballer - name: {self._name}, nickname: {self.__nickname}, position: {self.__position}"


jp = Footballer("peter pythons", "pyper", "forward")
print(jp)
# Footballer - name: Peter Pythons, nickname: Pyper, position: forward
```

---

## Seção 3 - Técnicas de Programação Orientada a Objetos

### self Como Referência ao Próprio Objeto

Um método pode retornar o próprio objeto ou um novo objeto da mesma classe:

```python
class Product:
    def __init__(self, name: str, price: float):
        self.__name = name
        self.__price = price

    def __str__(self):
        return f"{self.__name} (price {self.__price})"

    @property
    def price(self):
        return self.__price

    # Retorna NOVO objeto da mesma classe
    def product_on_sale(self):
        on_sale = Product(self.__name, self.__price * 0.75)
        return on_sale

    # Retorna self ou outro objeto
    def cheaper(self, other):
        if self.__price < other.price:
            return self  # retorna o próprio objeto
        else:
            return other


apple = Product("Apple", 2.99)
apple_sale = apple.product_on_sale()
print(apple)       # Apple (price 2.99)
print(apple_sale)  # Apple (price 2.2425)

orange = Product("Orange", 3.95)
print(orange.cheaper(apple))  # Apple (price 2.99)
```

### Overloading de Operadores

Você pode definir como operadores funcionam com seus objetos:

```python
class Product:
    def __init__(self, name: str, price: float):
        self.__name = name
        self.__price = price

    @property
    def price(self):
        return self.__price

    # Define o operador >
    def __gt__(self, another_product):
        return self.price > another_product.price

    # Define o operador ==
    def __eq__(self, another_product):
        return self.price == another_product.price


orange = Product("Orange", 2.90)
apple = Product("Apple", 3.95)

if orange > apple:  # usa __gt__
    print("Orange é maior")
else:
    print("Apple é maior")  # imprime isso
```

### Tabela de Operadores de Comparação

| Operador | Significado | Método |
|----------|-------------|--------|
| `<` | Menor que | `__lt__(self, another)` |
| `>` | Maior que | `__gt__(self, another)` |
| `==` | Igual a | `__eq__(self, another)` |
| `!=` | Diferente de | `__ne__(self, another)` |
| `<=` | Menor ou igual | `__le__(self, another)` |
| `>=` | Maior ou igual | `__ge__(self, another)` |

### Tabela de Operadores Aritméticos

| Operador | Significado | Método |
|----------|-------------|--------|
| `+` | Adição | `__add__(self, another)` |
| `-` | Subtração | `__sub__(self, another)` |
| `*` | Multiplicação | `__mul__(self, another)` |
| `/` | Divisão (float) | `__truediv__(self, another)` |
| `//` | Divisão (int) | `__floordiv__(self, another)` |

### Exemplo: Operador de Adição

```python
from datetime import datetime

class Note:
    def __init__(self, entry_date: datetime, entry: str):
        self.entry_date = entry_date
        self.entry = entry

    def __str__(self):
        return f"{self.entry_date}: {self.entry}"

    def __add__(self, another):
        # Cria nova nota combinando duas
        new_note = Note(datetime.now(), "")
        new_note.entry = self.entry + " and " + another.entry
        return new_note


entry1 = Note(datetime(2016, 12, 17), "Comprar presentes")
entry2 = Note(datetime(2016, 12, 23), "Buscar árvore")

# Usando o operador +
both = entry1 + entry2
print(both)
# 2024-01-18 14:30:00: Comprar presentes and Buscar árvore
```

### \_\_repr\_\_ vs \_\_str\_\_

| Método | Propósito | Público-alvo |
|--------|-----------|--------------|
| `__str__` | Representação legível | Usuário final |
| `__repr__` | Representação técnica | Desenvolvedor |

```python
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __repr__(self):
        # Representação técnica - código que recria o objeto
        return f"Person({repr(self.name)}, {self.age})"

    def __str__(self):
        # Representação amigável
        return f"{self.name} ({self.age} anos)"


person = Person("Anna", 25)
print(person)        # Anna (25 anos)        <- usa __str__
print(repr(person))  # Person('Anna', 25)    <- usa __repr__

# Em listas, Python usa __repr__!
persons = [Person("Anna", 25), Person("Peter", 99)]
print(persons)  # [Person('Anna', 25), Person('Peter', 99)]
```

### Iteradores: \_\_iter\_\_ e \_\_next\_\_

Torne sua classe iterável para usar em `for` loops:

```python
class Book:
    def __init__(self, name: str, author: str, page_count: int):
        self.name = name
        self.author = author
        self.page_count = page_count


class Bookshelf:
    def __init__(self):
        self._books = []

    def add_book(self, book: Book):
        self._books.append(book)

    # Inicializa a iteração
    def __iter__(self):
        self.n = 0  # contador
        return self  # retorna o próprio objeto

    # Retorna o próximo item
    def __next__(self):
        if self.n < len(self._books):
            book = self._books[self.n]
            self.n += 1
            return book
        else:
            raise StopIteration  # sinaliza fim da iteração


# Uso
shelf = Bookshelf()
shelf.add_book(Book("A Vida de Python", "Montague Python", 123))
shelf.add_book(Book("O Velho e o C", "Ernest Hemingjavay", 204))
shelf.add_book(Book("Uma Boa Xícara de Java", "Caffee Coder", 997))

# Agora podemos usar for!
for book in shelf:
    print(book.name)

# A Vida de Python
# O Velho e o C
# Uma Boa Xícara de Java
```

---

## Seção 4 - Desenvolvendo uma Aplicação Maior

### Princípio: Separation of Concerns

> "Separation of concerns é um princípio de design para separar um programa em seções distintas, de modo que cada seção trate de uma preocupação separada."

### Single-Responsibility Principle

Cada classe deve ter **uma única responsabilidade**:

| Responsabilidade | Classe |
|------------------|--------|
| Lógica da aplicação | `PhoneBook` |
| Interface com usuário | `PhoneBookApplication` |
| Manipulação de arquivos | `FileHandler` |

### Estrutura de uma Aplicação

```
┌─────────────────────────────────────┐
│     PhoneBookApplication (UI)       │
│  - Interage com o usuário           │
│  - Delega comandos para outras      │
│    classes                          │
└──────────────┬──────────────────────┘
               │
    ┌──────────┴──────────┐
    │                     │
    ▼                     ▼
┌─────────────┐   ┌─────────────────┐
│  PhoneBook  │   │   FileHandler   │
│  (Lógica)   │   │   (Arquivo)     │
└─────────────┘   └─────────────────┘
```

### Exemplo Completo: PhoneBook

#### 1. Classe de Lógica

```python
class PhoneBook:
    def __init__(self):
        self.__persons = {}

    def add_number(self, name: str, number: str):
        if name not in self.__persons:
            self.__persons[name] = []
        self.__persons[name].append(number)

    def get_numbers(self, name: str):
        if name not in self.__persons:
            return None
        return self.__persons[name]

    def all_entries(self):
        return self.__persons
```

#### 2. Classe de Manipulação de Arquivos

```python
class FileHandler:
    def __init__(self, filename):
        self.__filename = filename

    def load_file(self):
        names = {}
        with open(self.__filename) as f:
            for line in f:
                parts = line.strip().split(';')
                name, *numbers = parts  # unpacking com *
                names[name] = numbers
        return names

    def save_file(self, phonebook: dict):
        with open(self.__filename, "w") as f:
            for name, numbers in phonebook.items():
                line = [name] + numbers
                f.write(";".join(line) + "\n")
```

#### 3. Classe de Interface

```python
class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()
        self.__filehandler = FileHandler("phonebook.txt")

        # Carrega dados do arquivo ao iniciar
        for name, numbers in self.__filehandler.load_file().items():
            for number in numbers:
                self.__phonebook.add_number(name, number)

    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add entry")
        print("2 search")

    def add_entry(self):
        name = input("name: ")
        number = input("number: ")
        self.__phonebook.add_number(name, number)

    def search(self):
        name = input("name: ")
        numbers = self.__phonebook.get_numbers(name)
        if numbers is None:
            print("number unknown")
            return
        for number in numbers:
            print(number)

    def exit(self):
        self.__filehandler.save_file(self.__phonebook.all_entries())

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                self.exit()
                break
            elif command == "1":
                self.add_entry()
            elif command == "2":
                self.search()
            else:
                self.help()


# Execução
application = PhoneBookApplication()
application.execute()
```

### Dependency Injection

Passar dependências de fora, em vez de criá-las dentro da classe:

```python
# ❌ Dependência hardcoded
class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()
        self.__filehandler = FileHandler("phonebook.txt")  # fixo!


# ✅ Dependency Injection
class PhoneBookApplication:
    def __init__(self, storage_service):
        self.__phonebook = PhoneBook()
        self.__storage_service = storage_service  # passado de fora


# Uso - fácil trocar implementação
storage_service = FileHandler("phonebook.txt")
application = PhoneBookApplication(storage_service)

# Ou usar outro tipo de storage sem mudar PhoneBookApplication!
cloud_service = CloudHandler("amazon-cloud", "user", "pass")
application = PhoneBookApplication(cloud_service)
```

### Benefícios da Modularidade

| Benefício | Descrição |
|-----------|-----------|
| **Testabilidade** | Testar cada classe isoladamente |
| **Manutenção** | Fácil localizar e corrigir bugs |
| **Expansão** | Adicionar features sem quebrar código existente |
| **Reutilização** | Usar classes em outros projetos |

---

## Conceitos-Chave

### Herança

| Conceito | Descrição |
|----------|-----------|
| **Herança** | Classe derivada herda traits da base |
| **Sintaxe** | `class Derived(Base):` |
| **super()** | Acessa métodos/atributos da base |
| **Override** | Redefinir método herdado na derivada |

### Modificadores de Acesso

| Modificador | Sintaxe | Visibilidade |
|-------------|---------|--------------|
| Public | `self.attr` | Todos |
| Protected | `self._attr` | Classe + derivadas |
| Private | `self.__attr` | Apenas a própria classe |

### Operadores Especiais

| Categoria | Métodos |
|-----------|---------|
| Comparação | `__lt__`, `__gt__`, `__eq__`, `__ne__`, `__le__`, `__ge__` |
| Aritmética | `__add__`, `__sub__`, `__mul__`, `__truediv__` |
| Representação | `__str__` (usuário), `__repr__` (técnico) |
| Iteração | `__iter__` (inicializa), `__next__` (próximo item) |

### Arquitetura de Software

| Princípio | Descrição |
|-----------|-----------|
| **Separation of Concerns** | Dividir programa em seções distintas |
| **Single Responsibility** | Uma classe = uma responsabilidade |
| **Dependency Injection** | Passar dependências de fora |

---

## Resumo Rápido

### Programa Exemplo: Sistema de Biblioteca

```python
# =============================================================
# SISTEMA DE BIBLIOTECA - Demonstração Parte 10
# =============================================================

from datetime import datetime

# ----- CLASSE BASE -----
class Item:
    """Classe base para itens da biblioteca"""
    
    def __init__(self, title: str, year: int):
        self._title = title      # protegido
        self._year = year        # protegido
        self._borrowed = False
    
    @property
    def title(self):
        return self._title
    
    @property
    def year(self):
        return self._year
    
    def borrow(self):
        if self._borrowed:
            return False
        self._borrowed = True
        return True
    
    def return_item(self):
        self._borrowed = False
    
    def __str__(self):
        status = "emprestado" if self._borrowed else "disponível"
        return f"{self._title} ({self._year}) - {status}"
    
    def __repr__(self):
        return f"Item({repr(self._title)}, {self._year})"
    
    # Comparação por ano
    def __lt__(self, other):
        return self._year < other.year
    
    def __eq__(self, other):
        return self._title == other.title and self._year == other.year


# ----- CLASSES DERIVADAS -----
class Book(Item):
    """Livro - herda de Item"""
    
    def __init__(self, title: str, author: str, year: int, pages: int):
        super().__init__(title, year)  # chama construtor base
        self.__author = author
        self.__pages = pages
    
    @property
    def author(self):
        return self.__author
    
    def __str__(self):
        base = super().__str__()  # usa __str__ da base
        return f"📖 {base} - {self.__author}, {self.__pages}p"
    
    def __repr__(self):
        return f"Book({repr(self._title)}, {repr(self.__author)}, {self._year}, {self.__pages})"


class DVD(Item):
    """DVD - herda de Item"""
    
    def __init__(self, title: str, director: str, year: int, duration: int):
        super().__init__(title, year)
        self.__director = director
        self.__duration = duration
    
    @property
    def director(self):
        return self.__director
    
    def __str__(self):
        base = super().__str__()
        return f"📀 {base} - Dir: {self.__director}, {self.__duration}min"


# ----- CLASSE ITERÁVEL -----
class Library:
    """Biblioteca - coleção iterável de itens"""
    
    def __init__(self, name: str):
        self._name = name
        self._items = []
    
    def add_item(self, item: Item):
        self._items.append(item)
    
    def find_by_title(self, title: str):
        for item in self._items:
            if title.lower() in item.title.lower():
                return item
        return None
    
    def available_items(self):
        return [item for item in self._items if not item._borrowed]
    
    # Torna a classe iterável
    def __iter__(self):
        self._index = 0
        return self
    
    def __next__(self):
        if self._index < len(self._items):
            item = self._items[self._index]
            self._index += 1
            return item
        raise StopIteration
    
    # Operador + para combinar bibliotecas
    def __add__(self, other):
        new_lib = Library(f"{self._name} + {other._name}")
        new_lib._items = self._items + other._items
        return new_lib
    
    def __len__(self):
        return len(self._items)


# ----- MANIPULADOR DE ARQUIVOS -----
class LibraryFileHandler:
    """Responsável por salvar/carregar dados"""
    
    def __init__(self, filename: str):
        self.__filename = filename
    
    def save(self, library: Library):
        with open(self.__filename, "w") as f:
            for item in library:
                if isinstance(item, Book):
                    f.write(f"BOOK;{item.title};{item.author};{item.year}\n")
                elif isinstance(item, DVD):
                    f.write(f"DVD;{item.title};{item.director};{item.year}\n")
    
    def load(self):
        items = []
        try:
            with open(self.__filename) as f:
                for line in f:
                    parts = line.strip().split(";")
                    item_type, title, creator, year = parts
                    if item_type == "BOOK":
                        items.append(Book(title, creator, int(year), 0))
                    elif item_type == "DVD":
                        items.append(DVD(title, creator, int(year), 0))
        except FileNotFoundError:
            pass
        return items


# ----- INTERFACE DO USUÁRIO -----
class LibraryApp:
    """Interface de usuário - responsabilidade única"""
    
    def __init__(self, file_handler: LibraryFileHandler):
        self.__library = Library("Minha Biblioteca")
        self.__file_handler = file_handler
        
        # Carrega dados salvos
        for item in self.__file_handler.load():
            self.__library.add_item(item)
    
    def run(self):
        while True:
            print("\n--- BIBLIOTECA ---")
            print("1. Adicionar livro")
            print("2. Listar itens")
            print("3. Emprestar")
            print("4. Devolver")
            print("0. Sair")
            
            cmd = input("Opção: ")
            
            if cmd == "0":
                self.__file_handler.save(self.__library)
                print("Dados salvos. Até logo!")
                break
            elif cmd == "1":
                self.__add_book()
            elif cmd == "2":
                self.__list_items()
            elif cmd == "3":
                self.__borrow_item()
            elif cmd == "4":
                self.__return_item()
    
    def __add_book(self):
        title = input("Título: ")
        author = input("Autor: ")
        year = int(input("Ano: "))
        pages = int(input("Páginas: "))
        self.__library.add_item(Book(title, author, year, pages))
        print("Livro adicionado!")
    
    def __list_items(self):
        if len(self.__library) == 0:
            print("Biblioteca vazia.")
            return
        
        print("\n--- ACERVO ---")
        for item in self.__library:  # usando __iter__
            print(item)
    
    def __borrow_item(self):
        title = input("Título para emprestar: ")
        item = self.__library.find_by_title(title)
        if item and item.borrow():
            print(f"'{item.title}' emprestado!")
        else:
            print("Item não encontrado ou já emprestado.")
    
    def __return_item(self):
        title = input("Título para devolver: ")
        item = self.__library.find_by_title(title)
        if item:
            item.return_item()
            print(f"'{item.title}' devolvido!")
        else:
            print("Item não encontrado.")


# ----- EXECUÇÃO -----
if __name__ == "__main__":
    # Dependency Injection - passamos o handler de fora
    handler = LibraryFileHandler("library.txt")
    app = LibraryApp(handler)
    app.run()
```

---

### Checklist de Conceitos

- [ ] Criar classe que herda de outra (`class Derived(Base)`)
- [ ] Usar `super().__init__()` para chamar construtor da base
- [ ] Fazer override de método da classe base
- [ ] Chamar método da base com `super().method()`
- [ ] Usar atributos protegidos (`_attr`) para herança
- [ ] Implementar `__lt__`, `__gt__`, `__eq__` para comparações
- [ ] Implementar `__add__`, `__sub__` para aritmética
- [ ] Diferenciar `__str__` (usuário) de `__repr__` (técnico)
- [ ] Implementar `__iter__` e `__next__` para iteração
- [ ] Separar responsabilidades em classes distintas
- [ ] Aplicar Dependency Injection

---

### Armadilhas Comuns

| Armadilha | Problema | Solução |
|-----------|----------|---------|
| `__attr` em herança | Atributo privado inacessível na derivada | Usar `_attr` (protegido) |
| Esquecer `super().__init__()` | Atributos da base não inicializados | Sempre chamar no construtor |
| `self` em `super()` | `super().__init__(self, x)` está errado | `super().__init__(x)` sem self |
| Override sem chamar base | Perde funcionalidade original | Usar `super().method()` se necessário |
| `__iter__` sem `StopIteration` | Loop infinito | Sempre levantar no final |
| Classe fazendo tudo | Difícil manter e testar | Separar responsabilidades |

---

### Padrões de Design

```python
# 1. HERANÇA BÁSICA
class Derived(Base):
    def __init__(self, base_arg, derived_arg):
        super().__init__(base_arg)
        self._derived_attr = derived_arg

# 2. OVERRIDE COM EXTENSÃO
def method(self):
    result = super().method()  # chama original
    # adiciona funcionalidade
    return result * 1.1

# 3. ITERADOR PADRÃO
def __iter__(self):
    self._index = 0
    return self

def __next__(self):
    if self._index < len(self._items):
        item = self._items[self._index]
        self._index += 1
        return item
    raise StopIteration

# 4. COMPARAÇÃO COMPLETA
def __lt__(self, other): return self.value < other.value
def __le__(self, other): return self.value <= other.value
def __gt__(self, other): return self.value > other.value
def __ge__(self, other): return self.value >= other.value
def __eq__(self, other): return self.value == other.value
def __ne__(self, other): return self.value != other.value

# 5. DEPENDENCY INJECTION
class App:
    def __init__(self, storage):  # recebe dependência
        self._storage = storage

storage = FileStorage("data.txt")  # cria fora
app = App(storage)                 # injeta
```

---

## Próximos Passos

Na **Parte 11** você aprenderá:

- List comprehensions avançadas
- Recursão
- Mais sobre funções e closures

---

**Fonte:** University of Helsinki MOOC - Python Programming  
**Resumo criado por:** Claude (Anthropic)  
**Para:** Eric Alcalai França
