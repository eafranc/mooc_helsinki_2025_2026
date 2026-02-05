# Command-Query Separation (CQS)

## Índice
- [[#O Que É CQS]]
- [[#Dois Tipos de Funções]]
- [[#Exemplos Práticos]]
- [[#Fluent Interface]]
- [[#CQS em Bancos de Dados]]
- [[#Quando Quebrar a Regra]]
- [[#Checklist de Boas Práticas]]

---

## O Que É CQS

**Command-Query Separation** é um princípio de design de software proposto por Bertrand Meyer:

> **Uma função deve ser:**
> - **Command (Comando)**: Modifica estado, mas não retorna valor útil
> - **Query (Consulta)**: Retorna valor, mas não modifica estado
> 
> **Nunca os dois ao mesmo tempo!**

### Vantagens

✅ **Código mais previsível** - você sabe se algo vai mudar estado só pelo nome
✅ **Mais fácil de testar** - queries podem ser testadas sem setup complexo
✅ **Menos bugs** - efeitos colaterais ficam explícitos
✅ **Paralelização** - queries são seguras para executar em paralelo

---

## Dois Tipos de Funções

### Commands (Comandos)

**Características:**
- Modificam o estado do sistema
- Têm efeitos colaterais
- Não retornam valor útil (ou retornam `None`)
- Nomes: verbos de ação (add, delete, update, mark, save)

**Exemplos:**

```python
# ✅ Command puro
def mark_finished(self, id: int):
    """Marca uma tarefa como finalizada"""
    for task in self.__tasks:
        if task.id == id:
            task.status = True  # ← modifica estado
            return  # ← não retorna valor útil

# ✅ Command puro
def add_order(self, description: str, programmer: str, workload: int):
    """Adiciona uma nova ordem"""
    order = Task(description, programmer, workload)
    self.__orders.append(order)  # ← modifica estado
    # return implícito (None)

# ✅ Command puro
def save_to_database(self, data: dict):
    """Salva dados no banco"""
    db.insert(data)  # ← modifica banco de dados
    # não retorna nada
```

### Queries (Consultas)

**Características:**
- **NÃO** modificam estado
- **NÃO** têm efeitos colaterais
- **Sempre** retornam um valor
- Nomes: verbos de leitura ou verificação (get, find, list, is, has, can)

**Nomenclatura:**
- Queries usam **verbos de leitura/busca** (não-destrutivos): `get`, `find`, `list`, `fetch`, `search`
- Ou **verbos de verificação** (retornam bool): `is`, `has`, `can`, `should`
- Ou aparecem como **properties** (substantivos): `name`, `count`, `total`, `size`

**Diferença importante:**
- **Commands** = verbos de **ação/modificação** (`add`, `delete`, `update`, `save`)
- **Queries** = verbos de **leitura/verificação** (`get`, `find`, `list`, `is`, `has`)

**Exemplos:**

```python
# ✅ Query pura
def finished_orders(self) -> list:
    """Retorna lista de ordens finalizadas"""
    return [order for order in self.__orders if order.status]
    # ← só lê, não modifica

# ✅ Query pura
def total_workload(self) -> int:
    """Calcula carga de trabalho total"""
    return sum(order.workload for order in self.__orders)
    # ← só calcula, não modifica

# ✅ Query pura
def has_unfinished_tasks(self) -> bool:
    """Verifica se há tarefas não finalizadas"""
    return any(not order.status for order in self.__orders)
    # ← só verifica, não modifica

# ✅ Query pura
def find_by_id(self, id: int) -> Task | None:
    """Busca tarefa por ID"""
    for task in self.__tasks:
        if task.id == id:
            return task
    return None
    # ← só busca, não modifica
```

### ❌ Violações de CQS (Evite!)

```python
# ❌ Faz comando E consulta ao mesmo tempo
def mark_and_count_finished(self, id: int) -> int:
    """Marca como finalizada E retorna total de finalizadas"""
    self.mark_finished(id)  # ← comando
    return len(self.finished_orders())  # ← consulta
    # PROBLEMA: Faz duas coisas diferentes!

# ❌ Query com efeito colateral escondido
def get_next_order(self) -> Task:
    """Retorna próxima ordem E a remove da fila"""
    order = self.__queue[0]
    self.__queue.pop(0)  # ← modifica estado!
    return order
    # PROBLEMA: Parece query mas modifica estado!

# ✅ CORRETO: Separar em dois métodos
def peek_next_order(self) -> Task:
    """Retorna próxima ordem sem remover"""
    return self.__queue[0]  # ← query pura

def remove_next_order(self):
    """Remove próxima ordem da fila"""
    self.__queue.pop(0)  # ← command puro
```

---

## Exemplos Práticos

### Exemplo 1: Sistema de Tarefas

```python
class OrderBook:
    def __init__(self):
        self.__orders = []
        self.__programmers = []
    
    # === COMMANDS ===
    
    def add_order(self, description: str, programmer: str, workload: int):
        """Command: adiciona ordem"""
        order = Task(description, programmer, workload)
        self.__orders.append(order)
        
        if programmer not in self.__programmers:
            self.__programmers.append(programmer)
        # Não retorna valor útil
    
    def mark_finished(self, id: int):
        """Command: marca tarefa como finalizada"""
        for order in self.__orders:
            if order.id == id:
                order.mark_finished()
                return
        raise ValueError(f"Task {id} not found")
    
    # === QUERIES ===
    
    def all_orders(self) -> list:
        """Query: retorna todas as ordens"""
        return self.__orders
    
    def finished_orders(self) -> list:
        """Query: retorna ordens finalizadas"""
        return [o for o in self.__orders if o.status]
    
    def unfinished_orders(self) -> list:
        """Query: retorna ordens não finalizadas"""
        return [o for o in self.__orders if not o.status]
    
    def programmers(self) -> list:
        """Query: retorna lista de programadores"""
        return self.__programmers
    
    def status_of_programmer(self, programmer: str) -> tuple:
        """Query: retorna estatísticas do programador"""
        if programmer not in self.__programmers:
            raise ValueError(f"Programmer not found")
        
        finished = [o.workload for o in self.finished_orders() 
                   if o.programmer == programmer]
        unfinished = [o.workload for o in self.unfinished_orders() 
                     if o.programmer == programmer]
        
        return (len(finished), len(unfinished), 
                sum(finished), sum(unfinished))
```

### Exemplo 2: Sistema Bancário

```python
class BankAccount:
    def __init__(self, balance: float = 0):
        self.__balance = balance
        self.__transactions = []
    
    # === COMMANDS ===
    
    def deposit(self, amount: float):
        """Command: deposita dinheiro"""
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.__balance += amount
        self.__transactions.append(f"Deposit: +{amount}")
    
    def withdraw(self, amount: float):
        """Command: saca dinheiro"""
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount
        self.__transactions.append(f"Withdraw: -{amount}")
    
    # === QUERIES ===
    
    def get_balance(self) -> float:
        """Query: retorna saldo atual"""
        return self.__balance
    
    def get_transactions(self) -> list:
        """Query: retorna histórico de transações"""
        return self.__transactions.copy()  # retorna cópia!
    
    def can_withdraw(self, amount: float) -> bool:
        """Query: verifica se pode sacar"""
        return amount <= self.__balance
```

---

## Fluent Interface

**Fluent Interface** é um padrão onde métodos retornam `self` para permitir **encadeamento de chamadas**.

### Padrão Básico

```python
class OrderBook:
    def add_order(self, description: str, programmer: str, workload: int):
        order = Task(description, programmer, workload)
        self.__orders.append(order)
        return self  # ← retorna self para encadear
    
    def mark_finished(self, id: int):
        for order in self.__orders:
            if order.id == id:
                order.mark_finished()
                return self  # ← retorna self
        raise ValueError(f"Task {id} not found")
```

### Uso

```python
# Sem fluent interface:
book = OrderBook()
book.add_order("task 1", "Eric", 5)
book.add_order("task 2", "Adele", 3)
book.mark_finished(1)

# Com fluent interface:
book = OrderBook()
book.add_order("task 1", "Eric", 5)\
    .add_order("task 2", "Adele", 3)\
    .mark_finished(1)

# Ou em uma linha:
OrderBook().add_order("task 1", "Eric", 5).add_order("task 2", "Adele", 3).mark_finished(1)
```

### CQS + Fluent Interface

**Importante:** Fluent Interface em commands **não viola CQS** porque:
- Retornar `self` **não é retornar informação computada**
- O método **ainda modifica estado** (é um command)
- Apenas facilita encadeamento

```python
# ✅ Command com fluent interface (OK!)
def add_order(self, ...):
    # modifica estado
    self.__orders.append(order)
    return self  # ← facilita encadeamento

# ✅ Query pura (não encadeia)
def finished_orders(self):
    return [...]  # ← retorna informação computada
```

### Exemplos de Fluent Interface

#### String Builder
```python
class StringBuilder:
    def __init__(self):
        self.__parts = []
    
    def append(self, text: str):
        self.__parts.append(text)
        return self
    
    def append_line(self, text: str):
        self.__parts.append(text + "\n")
        return self
    
    def build(self) -> str:
        return "".join(self.__parts)

# Uso:
result = StringBuilder()\
    .append("Hello")\
    .append_line(" World")\
    .append("This is a test")\
    .build()
```

#### Query Builder (SQL-like)
```python
class Query:
    def __init__(self, table: str):
        self.__table = table
        self.__conditions = []
        self.__order = None
    
    def where(self, condition: str):
        self.__conditions.append(condition)
        return self
    
    def order_by(self, field: str):
        self.__order = field
        return self
    
    def execute(self) -> list:
        # executa query no banco
        sql = f"SELECT * FROM {self.__table}"
        if self.__conditions:
            sql += " WHERE " + " AND ".join(self.__conditions)
        if self.__order:
            sql += f" ORDER BY {self.__order}"
        return database.execute(sql)

# Uso:
results = Query("tasks")\
    .where("status = 'finished'")\
    .where("programmer = 'Eric'")\
    .order_by("workload DESC")\
    .execute()
```

---

## CQS em Bancos de Dados

SQL naturalmente segue CQS:

### Commands (DML - Data Manipulation Language)

```sql
-- ✅ Command: Insere dados
INSERT INTO tasks (description, programmer, workload)
VALUES ('Build app', 'Eric', 10);

-- ✅ Command: Atualiza dados
UPDATE tasks
SET status = 'finished'
WHERE id = 1;

-- ✅ Command: Deleta dados
DELETE FROM tasks
WHERE id = 1;
```

### Queries (DQL - Data Query Language)

```sql
-- ✅ Query: Lê dados
SELECT * FROM tasks
WHERE status = 'finished';

-- ✅ Query: Agrega dados
SELECT programmer, COUNT(*) as total
FROM tasks
GROUP BY programmer;

-- ✅ Query: Verifica existência
SELECT EXISTS(
    SELECT 1 FROM tasks 
    WHERE id = 1
) as task_exists;
```

### ORMs Também Seguem CQS

```python
from sqlalchemy import select, update

# ✅ Query: Lê dados
stmt = select(Task).where(Task.status == 'finished')
results = session.execute(stmt).scalars().all()

# ✅ Command: Atualiza dados
stmt = update(Task).where(Task.id == 1).values(status='finished')
session.execute(stmt)
session.commit()  # comando explícito para modificar
```

### CQRS (Command Query Responsibility Segregation)

**Evolução de CQS:** Separar **modelos** diferentes para comandos e consultas.

```python
# Modelo para ESCRITA (Commands)
class TaskWriteModel:
    def add_task(self, ...):
        # Otimizado para escrita
        self.__tasks.append(task)
        self.__event_store.append(TaskAdded(...))
    
    def mark_finished(self, id):
        # Valida e modifica
        task = self.__find(id)
        task.status = 'finished'
        self.__event_store.append(TaskFinished(...))

# Modelo para LEITURA (Queries)
class TaskReadModel:
    def get_finished_tasks(self):
        # Otimizado para leitura (pode usar cache, views, etc)
        return self.__cache.get('finished_tasks')
    
    def get_dashboard_stats(self):
        # View materializada, super rápida
        return self.__stats_view.get()
```

**Vantagens do CQRS:**
- Escala escrita e leitura independentemente
- Otimiza cada lado para seu propósito
- Queries podem usar caches, réplicas, views materializadas
- Commands podem usar event sourcing

---

## Quando Quebrar a Regra

### Caso 1: Stack.pop() - Convenção Estabelecida

```python
# ❌ Tecnicamente viola CQS
def pop(self) -> T:
    """Remove E retorna último elemento"""
    return self.__items.pop()

# ✅ Mas é convenção aceita em estruturas de dados
stack = Stack()
item = stack.pop()  # todos esperam esse comportamento
```

**Por quê é aceitável?**
- Convenção universal em todas as linguagens
- Nome `pop` deixa claro que modifica estado
- Estruturas de dados têm semântica específica

### Caso 2: Builders com Validação

```python
# ❌ Tecnicamente viola CQS
def build(self) -> Product:
    """Valida estado interno E retorna produto"""
    if not self.__is_valid():
        raise ValueError("Invalid state")
    
    product = Product(self.__name, self.__price)
    self.__reset()  # ← modifica estado
    return product  # ← E retorna

# Uso do Builder:
builder = ProductBuilder()
product = builder.set_name("Widget")\
                .set_price(9.99)\
                .build()  # ← reseta builder internamente
```

**Por quê é aceitável?**
- Padrão Builder reconhecido
- Reset interno é esperado
- Facilita reuso do builder

### Caso 3: Lazy Loading

```python
# ❌ Tecnicamente viola CQS
def get_data(self) -> list:
    """Retorna dados, carregando-os se necessário"""
    if self.__cache is None:
        self.__cache = self.__load_from_db()  # ← modifica cache
    return self.__cache  # ← retorna dados

# Uso:
data = obj.get_data()  # primeira vez carrega, depois usa cache
```

**Por quê é aceitável?**
- Cache interno é detalhe de implementação
- Do ponto de vista externo, parece query pura
- Não afeta comportamento observável

### Regra Geral

> **Quebre CQS apenas quando:**
> 1. É convenção universal (como `pop()`)
> 2. O efeito colateral é **detalhe de implementação** (como cache)
> 3. A semântica do método deixa **explícito** que modifica (como `pop`, `dequeue`)

---

## Checklist de Boas Práticas

### ✅ Ao Escrever Commands

- [ ] Nome é verbo de ação? (add, delete, update, mark, save)
- [ ] Modifica estado do objeto/sistema?
- [ ] **NÃO** retorna valor calculado?
- [ ] Pode lançar exceção em caso de erro?
- [ ] Documentação menciona que modifica estado?

**Exemplo:**
```python
def mark_finished(self, id: int):
    """
    Marca uma tarefa como finalizada.
    
    Args:
        id: ID da tarefa
    
    Raises:
        ValueError: Se tarefa não existe
    """
    # implementação...
```

### ✅ Ao Escrever Queries

- [ ] Nome é verbo de leitura/verificação ou property? (get, find, list, is, has, name, count)
- [ ] **NÃO** modifica estado observável?
- [ ] **Sempre** retorna valor?
- [ ] Tipo de retorno está anotado?
- [ ] Pode ser chamada múltiplas vezes sem efeito?
- [ ] É segura para paralelização?

**Exemplo:**
```python
def finished_orders(self) -> list[Task]:
    """
    Retorna lista de tarefas finalizadas.
    
    Returns:
        Lista de objetos Task com status=True
    """
    return [order for order in self.__orders if order.status]
```

### ✅ Ao Revisar Código

- [ ] Funções fazem **uma coisa só**?
- [ ] Commands não retornam valores computados?
- [ ] Queries não modificam estado?
- [ ] Nomes refletem intenção (comando vs consulta)?
- [ ] Exceções são usadas para erros (não retornos especiais)?

### ❌ Code Smells (Sinais de Problema)

```python
# ❌ Nome não deixa claro que modifica
def task(self, id: int):  # faz o quê? command ou query?
    self.__mark_finished(id)

# ❌ Query com efeito colateral escondido
def get_next_id(self) -> int:
    self.__counter += 1  # ← modifica!
    return self.__counter

# ❌ Command retornando valor computado
def save_user(self, user: User) -> int:
    db.save(user)
    return db.count_users()  # ← não deveria retornar isso!

# ❌ Função faz duas coisas
def update_and_notify(self, id: int, data: dict) -> bool:
    self.update(id, data)  # comando
    return self.send_notification()  # outro comando + retorna bool
```

### ✅ Refatorações Comuns

**Antes (viola CQS):**
```python
def remove_first(self) -> Task:
    """Remove E retorna primeiro elemento"""
    return self.__tasks.pop(0)
```

**Depois (segue CQS):**
```python
def first(self) -> Task:
    """Retorna primeiro elemento sem remover"""
    return self.__tasks[0]

def remove_first(self):
    """Remove primeiro elemento"""
    self.__tasks.pop(0)

# Uso:
task = queue.first()  # query
queue.remove_first()  # command
```

---

## Resumo

### Princípio CQS

```
┌─────────────────────────────────────┐
│  COMMAND (Comando)                  │
│  - Modifica estado                  │
│  - Não retorna valor útil           │
│  - Verbos de ação: add, delete,     │
│    update, save, mark, create       │
└─────────────────────────────────────┘

┌─────────────────────────────────────┐
│  QUERY (Consulta)                   │
│  - NÃO modifica estado              │
│  - Sempre retorna valor             │
│  - Verbos de leitura: get, find,    │
│    list, fetch, search              │
│  - Verbos de verificação: is, has,  │
│    can, should                      │
│  - Properties: name, count, total   │
└─────────────────────────────────────┘
```

### Benefícios

✅ **Previsibilidade** - nome indica se modifica estado
✅ **Testabilidade** - queries fáceis de testar
✅ **Paralelização** - queries seguras para threads
✅ **Manutenibilidade** - efeitos colaterais explícitos
✅ **Debugging** - mais fácil rastrear mudanças de estado

### Quando Aplicar

**Sempre que possível!** Especialmente em:
- 📚 Bibliotecas e APIs públicas
- 🏢 Código corporativo de longa vida
- 🧪 Código com testes automatizados
- 👥 Projetos com múltiplos desenvolvedores

### Lembre-se

> "Perguntas devem receber respostas, não mudar o mundo."
> "Comandos devem mudar o mundo, não dar respostas."

---

**Referências:**
- Meyer, Bertrand. "Object-Oriented Software Construction" (1988)
- Martin Fowler. "CommandQuerySeparation"
- Greg Young. "CQRS Documents"
