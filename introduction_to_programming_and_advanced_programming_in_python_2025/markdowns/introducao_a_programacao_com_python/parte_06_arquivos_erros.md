# Parte 6 - Arquivos e Tratamento de Erros

**Curso:** Python Programming - University of Helsinki MOOC  
**Resumo criado por:** Claude (Anthropic)  
**Para:** Eric Alcalai França

---

## Índice

1. [[#Seção 1 - Reading Files]]
2. [[#Seção 2 - Writing Files]]
3. [[#Seção 3 - Handling Errors]]
4. [[#Seção 4 - Local and Global Variables]]
5. [[#Conceitos-Chave]]
6. [[#Resumo Rápido]]

---

## Seção 1 - Reading Files

### Abrindo e Lendo Arquivos

Use o statement `with` para abrir arquivos. O arquivo é automaticamente fechado após o bloco.

**Ler arquivo inteiro:**

```python
# Arquivo: example.txt
# Hello there!
# This example file contains three lines of text.
# This is the last line.

with open("example.txt") as new_file:
    contents = new_file.read()
    print(contents)

# Hello there!
# This example file contains three lines of text.
# This is the last line.
```

O método `read()` retorna todo o conteúdo como string única, incluindo `\n` (quebras de linha).

### Percorrendo Arquivo Linha por Linha

Arquivos de texto podem ser tratados como listas de strings.

```python
with open("example.txt") as new_file:
    count = 0
    total_length = 0
    
    for line in new_file:
        line = line.replace("\n", "")  # Remove quebra de linha
        count += 1
        print("Linha", count, line)
        total_length += len(line)

print("Comprimento total:", total_length)
```

**Por que remover `\n`?**
- Cada linha no arquivo termina com `\n`
- `print()` já adiciona quebra de linha
- Sem `replace()`, teríamos linhas duplas
- Remove `\n` para calcular comprimento correto

### Arquivos CSV (Comma-Separated Values)

CSV armazena dados separados por delimitador (`,`, `;`, etc.).

**Método `split()`:**

```python
text = "monkey,banana,harpsichord"
words = text.split(",")
# ['monkey', 'banana', 'harpsichord']

for word in words:
    print(word)
# monkey
# banana
# harpsichord
```

**Exemplo: Arquivo de notas**

```python
# grades.csv:
# Paul;5;4;5;3;4
# Beth;3;4;2;4;4

with open("grades.csv") as new_file:
    for line in new_file:
        line = line.replace("\n", "")
        parts = line.split(";")
        name = parts[0]
        grades = parts[1:]  # Slice: todos exceto primeiro
        print("Nome:", name)
        print("Notas:", grades)

# Nome: Paul
# Notas: ['5', '4', '5', '3', '4']
```

⚠️ **Importante:** `split()` retorna strings! Para números, use `int()`:

```python
grades = [int(grade) for grade in parts[1:]]
```

### Ler Arquivo Múltiplas Vezes

**Problema:** Arquivo só pode ser lido uma vez por abertura.

```python
with open("people.csv") as new_file:
    # Primeira leitura
    for line in new_file:
        print(line)
    
    # Segunda leitura NÃO funciona (arquivo já no final)
    for line in new_file:
        print(line)  # Nunca executa!
```

**Solução 1: Abrir novamente**

```python
with open("people.csv") as new_file:
    for line in new_file:
        print(line)

with open("people.csv") as new_file:  # Abre de novo
    for line in new_file:
        print(line)
```

**Solução 2 (MELHOR): Armazenar em lista**

```python
people = []

# Ler uma vez e armazenar
with open("people.csv") as new_file:
    for line in new_file:
        parts = line.split(";")
        people.append((parts[0], int(parts[1])))

# Agora pode usar quantas vezes quiser
for person in people:
    print(person[0])

oldest_age = max(person[1] for person in people)
```

### Processamento Avançado de CSV

**Criar dicionário a partir de CSV:**

```python
# grades.csv:
# Paul;5;4;5;3
# Beth;3;4;2;4

grades = {}

with open("grades.csv") as new_file:
    for line in new_file:
        line = line.replace("\n", "")
        parts = line.split(";")
        name = parts[0]
        grades[name] = []
        
        for grade in parts[1:]:
            grades[name].append(int(grade))

print(grades)
# {'Paul': [5, 4, 5, 3], 'Beth': [3, 4, 2, 4]}

# Calcular estatísticas
for name, grade_list in grades.items():
    best = max(grade_list)
    average = sum(grade_list) / len(grade_list)
    print(f"{name}: melhor {best}, média {average:.2f}")
```

### Limpando Linhas: `strip()`, `lstrip()`, `rstrip()`

**Problema:** Espaços extras e quebras de linha.

```python
# people.csv:
# first; last
# Paul; Python
# Jean; Java

last_names = []

with open("people.csv") as new_file:
    for line in new_file:
        parts = line.split(';')
        
        if parts[0] == "first":
            continue  # Pula cabeçalho
        
        last_names.append(parts[1])

print(last_names)
# [' Python\n', ' Java\n']  ← espaços e \n!
```

**Solução: `strip()`**

Remove espaços, tabs, `\n` do início e fim da string.

```python
last_names = []

with open("people.csv") as new_file:
    for line in new_file:
        parts = line.split(';')
        
        if parts[0] == "first":
            continue
        
        last_names.append(parts[1].strip())  # ✅

print(last_names)
# ['Python', 'Java']  ← limpo!
```

**Variantes:**

```python
# strip() - remove dos dois lados
"  teste  ".strip()      # 'teste'

# lstrip() - remove só da esquerda (left)
"  teste  ".lstrip()     # 'teste  '

# rstrip() - remove só da direita (right)
"  teste  ".rstrip()     # '  teste'
```

### Combinando Dados de Múltiplos Arquivos

Usar dicionários com chave comum (ex: ID).

**Exemplo: Funcionários e Salários**

```python
# employees.csv:
# pic;name;address
# 080488-123X;Pekka Mikkola;Vilppulantie 7

# salaries.csv:
# pic;salary;bonus
# 080488-123X;3300;0

# Ler nomes
names = {}
with open("employees.csv") as new_file:
    for line in new_file:
        parts = line.split(';')
        if parts[0] == "pic":
            continue  # Pula cabeçalho
        names[parts[0]] = parts[1]

# Ler salários
salaries = {}
with open("salaries.csv") as new_file:
    for line in new_file:
        parts = line.split(';')
        if parts[0] == "pic":
            continue
        # Salário + bônus
        salaries[parts[0]] = int(parts[1]) + int(parts[2])

# Combinar
print("Rendas:")
for pic, name in names.items():
    if pic in salaries:
        salary = salaries[pic]
        print(f"{name:16} {salary} euros")
    else:
        print(f"{name:16} 0 euros")
```

**Estrutura dos dicionários:**

```python
names = {
    '080488-123X': 'Pekka Mikkola',
    '290274-044S': 'Liisa Marttinen'
}

salaries = {
    '080488-123X': 3300,
    '290274-044S': 4350
}
```

### ⚠️ Problemas Comuns ao Ler Arquivos

**Visual Studio Code não encontra arquivo:**

1. Verifique ortografia do nome
2. Configure: File → Preferences → Settings
3. Busque "executeinfile"
4. Ative: Python → Terminal → Execute In File Dir
5. Ou copie arquivo para raiz do diretório do exercício

**Debugger e arquivos:**
- Debugger sempre procura na raiz
- Execute In File Dir não afeta debugger
- Solução: copiar arquivo para raiz

---

## Seção 2 - Writing Files

### Criando Novo Arquivo

Use `open()` com modo `"w"` (write).

```python
with open("new_file.txt", "w") as my_file:
    my_file.write("Hello there!")
```

⚠️ **ATENÇÃO:** Modo `"w"` **sobrescreve** arquivo se já existir!

**Resultado (new_file.txt):**

```
Hello there!
```

### Quebras de Linha Manuais

`write()` **NÃO** adiciona quebras de linha automaticamente (diferente de `print()`).

**Sem `\n`:**

```python
with open("new_file.txt", "w") as my_file:
    my_file.write("Hello there!")
    my_file.write("This is the second line")
    my_file.write("This is the last line")

# Resultado:
# Hello there!This is the second lineThis is the last line
```

**Com `\n`:**

```python
with open("new_file.txt", "w") as my_file:
    my_file.write("Hello there!\n")
    my_file.write("This is the second line\n")
    my_file.write("This is the last line\n")

# Resultado:
# Hello there!
# This is the second line
# This is the last line
```

### Modo Append (Adicionar ao Final)

Use `"a"` (append) para adicionar sem apagar conteúdo existente.

```python
with open("new_file.txt", "a") as my_file:
    my_file.write("This is the 4th line\n")
    my_file.write("And yet another line.\n")

# Resultado (adicionado ao final):
# Hello there!
# This is the second line
# This is the last line
# This is the 4th line
# And yet another line.
```

**Se arquivo não existe:** `"a"` funciona igual a `"w"`.

### Escrevendo CSV

**Escrita manual:**

```python
with open("coders.csv", "w") as my_file:
    my_file.write("Eric;Windows;Pascal;10\n")
    my_file.write("Matt;Linux;PHP;2\n")
    my_file.write("Alan;Linux;Java;17\n")

# Resultado (coders.csv):
# Eric;Windows;Pascal;10
# Matt;Linux;PHP;2
# Alan;Linux;Java;17
```

**De lista para CSV:**

```python
coders = []
coders.append(["Eric", "Windows", "Pascal", 10])
coders.append(["Matt", "Linux", "PHP", 2])

# Método 1: F-string
with open("coders.csv", "w") as my_file:
    for coder in coders:
        line = f"{coder[0]};{coder[1]};{coder[2]};{coder[3]}"
        my_file.write(line + "\n")

# Método 2: Loop para construir string
with open("coders.csv", "w") as my_file:
    for coder in coders:
        line = ""
        for value in coder:
            line += f"{value};"
        line = line[:-1]  # Remove último ";"
        my_file.write(line + "\n")
```

### Limpar Conteúdo de Arquivo

Abrir em modo `"w"` e fechar imediatamente.

```python
# Método 1: Com with
with open("file_to_be_cleared.txt", "w") as my_file:
    pass  # Não faz nada (mas necessário em Python)

# Método 2: Oneliner
open('file_to_be_cleared.txt', 'w').close()
```

### Deletar Arquivo

Usar módulo `os`:

```python
import os

os.remove("unnecessary_file.csv")
```

⚠️ **Nota:** Não funciona nos testes automáticos do curso (limitação técnica).

### Estrutura de Programa com Arquivos

**Exemplo: Sistema de Notas**

```python
# 1. LER arquivo
def read_weekly_points(filename):
    weekly_points = {}
    with open(filename) as my_file:
        for line in my_file:
            parts = line.split(";")
            point_list = [int(p) for p in parts[1:]]
            weekly_points[parts[0]] = point_list
    return weekly_points

# 2. PROCESSAR dados
def grade(points):
    if points < 20:
        return 0
    elif points < 25:
        return 1
    elif points < 30:
        return 2
    elif points < 35:
        return 3
    elif points < 40:
        return 4
    else:
        return 5

# 3. ESCREVER resultado
def save_results(filename, weekly_points):
    with open(filename, "w") as my_file:
        for name, point_list in weekly_points.items():
            point_sum = sum(point_list)
            my_file.write(f"{name};{point_sum};{grade(point_sum)}\n")

# 4. MAIN function
weekly_points = read_weekly_points("weekly_points.csv")
save_results("results.csv", weekly_points)
```

**Princípios de design:**
- Cada função tem **responsabilidade única**
- Entrada via argumentos, saída via return
- Facilita testes e manutenção
- Fácil adicionar novas funcionalidades

---

## Seção 3 - Handling Errors

### Tipos de Erros

**1. Erros de sintaxe**
- Impedem execução
- Python aponta localização
- Ex: `:` faltando, `"` sem fechar

**2. Erros de runtime (exceções)**
- Ocorrem durante execução
- Podem ser tratados com try-except
- Ex: input inválido, divisão por zero

### Validação de Input

**Problema:** Input inválido causa erro.

```python
age = int(input("Digite sua idade: "))
if age >= 0 and age <= 150:
    print("Idade válida")
else:
    print("Idade inválida")

# Input: "vinte e três"
# ValueError: invalid literal for int() with base 10: 'vinte e três'
```

### Try-Except

Permite **capturar** e **tratar** exceções.

```python
try:
    age = int(input("Digite sua idade: "))
except ValueError:
    age = -1  # Valor inválido padrão

if age >= 0 and age <= 150:
    print("Idade válida")
else:
    print("Idade inválida")

# Input: "vinte e três"
# Idade inválida  ← programa continua!
```

**Estrutura:**

```python
try:
    # Código que pode causar erro
    resultado = operacao_perigosa()
except TipoDeErro:
    # O que fazer se erro ocorrer
    resultado = valor_padrao
```

### Loop com Try-Except

**Pedir input até ser válido:**

```python
def read_integer():
    while True:
        try:
            input_str = input("Digite um inteiro: ")
            return int(input_str)
        except ValueError:
            print("Input inválido")

number = read_integer()
print("Obrigado!")
print(number, "ao cubo é", number**3)

# Digite um inteiro: três
# Input inválido
# Digite um inteiro: abc
# Input inválido
# Digite um inteiro: 5
# Obrigado!
# 5 ao cubo é 125
```

### Pass Statement

Bloco vazio não é permitido em Python. Use `pass` quando não quiser fazer nada.

```python
def read_small_integer():
    while True:
        try:
            number = int(input("Digite um inteiro: "))
            if number < 100:
                return number
        except ValueError:
            pass  # Não faz nada

        print("Input inválido")

# Digite um inteiro: três
# Input inválido
# Digite um inteiro: 1000
# Input inválido
# Digite um inteiro: 5
```

### Exceções Comuns

| Exceção | Causa | Exemplo |
|---------|-------|---------|
| `ValueError` | Argumento com valor inválido | `float("1,23")` (vírgula) |
| `TypeError` | Tipo errado | `len(10)` (int não tem len) |
| `IndexError` | Índice fora do alcance | `"abc"[5]` |
| `ZeroDivisionError` | Divisão por zero | `10 / 0` |
| `FileNotFoundError` | Arquivo não existe | `open("inexistente.txt")` |
| `PermissionError` | Sem permissão | Acesso negado a arquivo |
| `UnboundLocalError` | Variável local não definida | Uso antes de atribuir |

### Múltiplos Except

Tratar diferentes erros de formas diferentes.

```python
try:
    with open("example.txt") as my_file:
        for line in my_file:
            print(line)
except FileNotFoundError:
    print("Arquivo example.txt não encontrado")
except PermissionError:
    print("Sem permissão para acessar example.txt")
```

### Except Genérico

Captura **QUALQUER** exceção (exceto erros de sintaxe).

```python
try:
    with open("example.txt") as my_file:
        for line in my_file:
            print(line)
except:
    print("Erro ao ler arquivo")
```

⚠️ **CUIDADO:** Except genérico pode esconder erros de programação!

```python
# BUG: "myfile" deveria ser "my_file"
try:
    with open("example.txt") as my_file:
        for line in myfile:  # NameError (variável errada)
            print(line)
except:
    print("Erro ao ler arquivo")  # Esconde o bug!
```

**Boa prática:** Especifique o tipo de erro sempre que possível.

### Propagação de Exceções

Se exceção não é tratada em função, ela "sobe" para quem chamou a função.

```python
def testing(x):
    print(int(x) + 1)  # Pode causar ValueError

# Tratamento na chamada
try:
    number = input("Digite um número: ")
    testing(number)
except:
    print("Algo deu errado")

# Digite um número: três
# Algo deu errado
```

### Raising Exceptions (Lançar Erros)

Use `raise` para criar exceções intencionalmente.

**Por quê?**
- Validar parâmetros
- Sinalizar condições inválidas
- Facilitar debugging

```python
def factorial(n):
    if n < 0:
        raise ValueError("Input foi negativo: " + str(n))
    
    k = 1
    for i in range(2, n + 1):
        k *= i
    return k

print(factorial(3))   # 6
print(factorial(6))   # 720
print(factorial(-1))  # ValueError: Input foi negativo: -1
```

**Quando usar:**
- Input inválido em funções
- Condições que não deveriam acontecer
- Ajudar outros desenvolvedores a encontrar bugs

---

## Seção 4 - Local and Global Variables

### Escopo de Variáveis

**Escopo:** Seções do programa onde variável está acessível.

- **Local:** Acessível apenas dentro de função
- **Global:** Acessível em todo o programa

### Variáveis Locais

Variáveis definidas **dentro** de função são locais.

```python
def testing():
    x = 5
    print(x)

testing()  # 5
print(x)   # NameError: name 'x' is not defined
```

`x` só existe durante execução de `testing()`.

**Parâmetros também são locais:**

```python
def greeting(name):
    print("Olá", name)

greeting("Ana")  # Olá Ana
print(name)      # NameError: name 'name' is not defined
```

### Variáveis Globais

Variáveis definidas **fora** de funções são globais.

```python
def testing():
    print(x)  # Pode ler global

x = 3
testing()  # 3
```

**Leitura OK, modificação NÃO:**

```python
def testing():
    x = 5  # Cria nova variável LOCAL
    print(x)

x = 3
testing()  # 5 (local)
print(x)   # 3 (global não mudou)
```

### Mascaramento (Shadowing)

Local "esconde" global com mesmo nome.

```python
x = 10  # Global

def testing():
    x = 5  # Local (mascara global)
    print(x)

testing()  # 5 (local)
print(x)   # 10 (global intacta)
```

### ⚠️ Erro: Referenciar Antes de Atribuir

```python
def testing():
    print(x)  # Tenta usar x
    x = 5     # Mas atribui depois

x = 3
testing()
# UnboundLocalError: local variable 'x' referenced before assignment
```

Python vê `x = 5`, então interpreta `x` como local. Mas tenta usar antes de definir!

### Keyword `global`

Permite modificar variável global **dentro** de função.

```python
def testing():
    global x
    x = 3
    print(x)

x = 5
testing()  # 3
print(x)   # 3 (global foi alterada!)
```

### Quando Usar Global?

❌ **NÃO use para:**
- Substituir parâmetros
- Substituir return values

```python
# ❌ RUIM
def calculate_sum(a, b):
    global result
    result = a + b

calculate_sum(2, 3)
print(result)

# ✅ BOM
def calculate_sum(a, b):
    return a + b

result = calculate_sum(2, 3)
print(result)
```

✅ **Use global quando:**
- Precisar de informação comum a múltiplas funções
- Ex: contador de chamadas

```python
def calculate_sum(a, b):
    global count
    count += 1
    return a + b

def calculate_difference(a, b):
    global count
    count += 1
    return a - b

count = 0
print(calculate_sum(2, 3))         # 5
print(calculate_difference(5, 2))  # 3
print("Chamadas:", count)          # 2
```

### Passando Dados Entre Funções

**Princípio:** Use argumentos e return, não global.

```python
def input_from_user(how_many: int):
    numbers = []
    for i in range(how_many):
        number = int(input(f"Número {i+1}: "))
        numbers.append(number)
    return numbers

def analyze(numbers: list):
    mean = sum(numbers) / len(numbers)
    return f"Média: {mean}, Min: {min(numbers)}, Max: {max(numbers)}"

# Main function armazena dados
inputs = input_from_user(5)
result = analyze(inputs)
print(result)
```

**Por quê?**
- Funções são independentes
- Fácil testar individualmente
- Fácil manter e modificar
- Evita estado global confuso

### Main Function Explícita

Transformar código principal em função main().

```python
def main():
    inputs = input_from_user(5)
    result = analyze(inputs)
    print(result)

# Executar main
main()
```

Agora `inputs` é local a `main()`, não global!

---

## Conceitos-Chave

### Modos de Abertura de Arquivo

| Modo | Nome | Função | Se arquivo existe | Se não existe |
|------|------|--------|-------------------|---------------|
| `"r"` | Read | Leitura | Abre | Erro |
| `"w"` | Write | Escrita | **Sobrescreve** | Cria |
| `"a"` | Append | Adicionar | Adiciona ao final | Cria |

### Métodos de Arquivo

| Método | Função | Retorno |
|--------|--------|---------|
| `read()` | Lê arquivo inteiro | String |
| `readline()` | Lê uma linha | String |
| `readlines()` | Lê todas as linhas | Lista de strings |
| `write(text)` | Escreve string | None |
| `close()` | Fecha arquivo | None |

### Métodos de String para Limpeza

| Método | Função | Exemplo |
|--------|--------|---------|
| `strip()` | Remove espaços/\n de ambos lados | `"  hi\n".strip()` → `"hi"` |
| `lstrip()` | Remove só da esquerda | `"  hi  ".lstrip()` → `"hi  "` |
| `rstrip()` | Remove só da direita | `"  hi  ".rstrip()` → `"  hi"` |
| `replace(old, new)` | Substitui substring | `"hi\n".replace("\n", "")` → `"hi"` |
| `split(sep)` | Divide em lista | `"a;b;c".split(";")` → `['a','b','c']` |

### Exceções - Quando Usar

| Situação | Usar try-except? |
|----------|------------------|
| Input do usuário | ✅ Sim (pode ser inválido) |
| Leitura de arquivo | ✅ Sim (arquivo pode não existir) |
| Cálculos matemáticos | ✅ Sim (divisão por zero possível) |
| Código sem input externo | ❌ Não (corrigir bug em vez de tratar) |

### Escopo - Regras de Ouro

| Tipo | Onde definida | Onde acessível | Modificável de função? |
|------|---------------|----------------|------------------------|
| Local | Dentro de função | Só na função | N/A |
| Global | Fora de funções | Todo o programa | Só com `global` |

**Quando usar global:**
- ✅ Contadores compartilhados
- ✅ Configurações de programa
- ❌ Passar dados entre funções (use argumentos)
- ❌ Retornar resultados (use return)

---

## Resumo Rápido

### Programa Exemplo - Sistema de Análise de Curso

```python
# ============ LEITURA ============
def read_student_info(filename):
    """Lê informações dos alunos de CSV."""
    students = {}
    with open(filename) as file:
        for line in file:
            parts = line.strip().split(';')
            if parts[0] == "id":  # Pula cabeçalho
                continue
            student_id = parts[0]
            name = f"{parts[1]} {parts[2]}"
            students[student_id] = name
    return students

def read_exercise_data(filename):
    """Lê dados de exercícios de CSV."""
    exercises = {}
    with open(filename) as file:
        for line in file:
            parts = line.strip().split(';')
            if parts[0] == "id":
                continue
            student_id = parts[0]
            # Converter para inteiros
            exercise_list = [int(x) for x in parts[1:]]
            exercises[student_id] = exercise_list
    return exercises

# ============ PROCESSAMENTO ============
def calculate_grade(points):
    """Determina nota baseada em pontos."""
    if points < 15:
        return 0
    elif points < 18:
        return 1
    elif points < 21:
        return 2
    elif points < 24:
        return 3
    elif points < 28:
        return 4
    else:
        return 5

def process_results(students, exercises):
    """Combina dados e calcula resultados."""
    results = {}
    
    for student_id, name in students.items():
        if student_id not in exercises:
            continue
        
        exercise_points = sum(exercises[student_id]) // 10
        # Aqui poderia adicionar pontos de prova
        total_points = exercise_points
        grade = calculate_grade(total_points)
        
        results[student_id] = {
            'name': name,
            'exercises': sum(exercises[student_id]),
            'points': total_points,
            'grade': grade
        }
    
    return results

# ============ ESCRITA ============
def save_results_txt(filename, results):
    """Salva resultados formatados em TXT."""
    with open(filename, "w") as file:
        file.write("Resultados do Curso\n")
        file.write("=" * 50 + "\n")
        
        for student_id, data in results.items():
            line = f"{data['name']:20} Exercícios: {data['exercises']:3} "
            line += f"Pontos: {data['points']:2} Nota: {data['grade']}\n"
            file.write(line)

def save_results_csv(filename, results):
    """Salva resultados em CSV."""
    with open(filename, "w") as file:
        for student_id, data in results.items():
            file.write(f"{student_id};{data['name']};{data['grade']}\n")

# ============ TRATAMENTO DE ERROS ============
def safe_file_read(filename, reader_function):
    """Wrapper com tratamento de erros para leitura."""
    try:
        return reader_function(filename)
    except FileNotFoundError:
        print(f"Erro: Arquivo '{filename}' não encontrado")
        return None
    except PermissionError:
        print(f"Erro: Sem permissão para ler '{filename}'")
        return None
    except Exception as e:
        print(f"Erro inesperado: {e}")
        return None

# ============ MAIN ============
def main():
    # Ler dados
    students = safe_file_read("students.csv", read_student_info)
    exercises = safe_file_read("exercises.csv", read_exercise_data)
    
    if students is None or exercises is None:
        print("Não foi possível ler os arquivos necessários")
        return
    
    # Processar
    results = process_results(students, exercises)
    
    # Salvar
    save_results_txt("results.txt", results)
    save_results_csv("results.csv", results)
    
    print("Resultados salvos com sucesso!")

# Executar programa
if __name__ == "__main__":
    main()
```

### Checklist de Conceitos

**Leitura de Arquivos:**
- [ ] Sei usar `with open()` para abrir arquivos
- [ ] Sei ler arquivo inteiro com `read()`
- [ ] Sei percorrer linha por linha com for loop
- [ ] Sei usar `strip()` para limpar linhas
- [ ] Sei processar CSV com `split()`
- [ ] Sei converter strings para números com `int()`/`float()`
- [ ] Entendo que arquivo só pode ser lido uma vez por abertura
- [ ] Sei quando armazenar dados em lista/dicionário

**Escrita de Arquivos:**
- [ ] Sei criar arquivo novo com modo `"w"`
- [ ] Sei adicionar ao final com modo `"a"`
- [ ] Lembro de adicionar `\n` manualmente
- [ ] Sei escrever CSV formatado
- [ ] Sei limpar conteúdo de arquivo

**Tratamento de Erros:**
- [ ] Sei usar try-except para capturar exceções
- [ ] Conheço exceções comuns (ValueError, TypeError, etc.)
- [ ] Sei tratar múltiplas exceções
- [ ] Sei quando usar except genérico vs específico
- [ ] Sei usar `pass` em blocos vazios
- [ ] Sei lançar exceções com `raise`
- [ ] Entendo propagação de exceções

**Escopo de Variáveis:**
- [ ] Entendo diferença entre local e global
- [ ] Sei que parâmetros são locais
- [ ] Sei usar keyword `global` quando necessário
- [ ] Evito usar global para passar dados entre funções
- [ ] Uso argumentos e return para comunicação entre funções

### Armadilhas Comuns

| Erro | Problema | Solução |
|------|----------|---------|
| Esquecer `\n` ao escrever | Linhas juntas | Sempre adicionar `\n` com `write()` |
| Modo "w" apaga arquivo | Dados perdidos | Verificar se arquivo existe ou usar "a" |
| `for line in file:` duas vezes | Segunda não executa | Abrir arquivo novamente ou armazenar em lista |
| Não usar `strip()` em CSV | Espaços extras | Sempre `strip()` antes de `split()` |
| Except genérico esconde bugs | Erro real não aparece | Especificar tipo de exceção |
| Modificar global sem `global` | Cria local em vez de modificar | Usar keyword `global` |
| Usar global em vez de return | Código confuso | Usar return para resultados |
| Esquecer `int()` em CSV numérico | Strings em vez de números | Converter com `int()` ou `float()` |

### Padrões de Design

**1. Separação de Responsabilidades**

```python
# ✅ BOM: Cada função faz uma coisa
def read_data(filename):
    """Apenas lê."""
    pass

def process_data(data):
    """Apenas processa."""
    pass

def save_data(filename, data):
    """Apenas salva."""
    pass

# ❌ RUIM: Função faz tudo
def do_everything():
    # ler, processar, salvar tudo junto
    pass
```

**2. Tratamento de Erros Centralizado**

```python
# ✅ BOM: Wrapper reutilizável
def safe_read(filename, reader):
    try:
        return reader(filename)
    except Exception as e:
        print(f"Erro: {e}")
        return None

# ❌ RUIM: Try-except repetido em todo lugar
```

**3. Main Function Explícita**

```python
# ✅ BOM: Fluxo claro
def main():
    data = read_data("input.csv")
    results = process(data)
    save_data("output.csv", results)

if __name__ == "__main__":
    main()

# ❌ RUIM: Código solto no nível global
```

---

## Próximos Passos

Na **Parte 7** você aprenderá:

- Módulos e bibliotecas
- Números aleatórios
- Datas e horários
- Funções de ordem superior

---

**Fonte:** University of Helsinki MOOC - Python Programming  
**Resumo criado por:** Claude (Anthropic)  
**Para:** Eric Alcalai França
