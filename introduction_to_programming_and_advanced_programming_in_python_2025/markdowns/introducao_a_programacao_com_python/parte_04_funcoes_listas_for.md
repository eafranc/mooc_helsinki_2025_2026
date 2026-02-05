# Parte 4 - Funções, Listas e Loop For

## Índice

- [[#Seção 1 - VS Code, Interpretador e Debugging]]
- [[#Seção 2 - Mais Sobre Funções]]
- [[#Seção 3 - Listas]]
- [[#Seção 4 - Iteração Definida (for)]]
- [[#Seção 5 - Formatação de Print]]
- [[#Seção 6 - Mais Strings e Listas]]
- [[#Conceitos-Chave]]
- [[#Resumo Rápido]]

---

## Seção 1 - VS Code, Interpretador e Debugging

### Objetivos de Aprendizagem

- Usar o editor Visual Studio Code
- Familiarizar-se com o interpretador interativo Python
- Usar a ferramenta de debugging integrada

### Visual Studio Code

- Editor recomendado para o curso
- Instalar extensão Python e plugin TMC
- Executar código: clicar no triângulo no canto superior direito
- Parar execução travada: `Ctrl+C`

### Interpretador Interativo Python

Permite executar código Python linha por linha.

**Iniciar:**
- Linux/Mac: `python3` no terminal
- Windows: `python` no prompt de comando
- VS Code: executar um programa, depois digitar `python3` no terminal

```python
>>> 2 + 3
5
>>> "hello".upper()
'HELLO'
>>> t = [1, 2, 3, 4, 5]
>>> for number in t:
...     print(number)
...
1
2
3
4
5
```

**Função `dir()`** - lista métodos disponíveis:

```python
>>> dir("string")
[..., 'capitalize', 'count', 'find', 'lower', 'replace', 'split', 'upper', ...]

>>> dir([])
[..., 'append', 'clear', 'copy', 'count', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
```

**Sair do interpretador:**
- `quit()` ou `exit()`
- `Ctrl+D` (Linux/Mac) ou `Ctrl+Z` (Windows)

### Debugger Integrado do VS Code

1. **Definir breakpoint:** clicar na margem esquerda da linha
2. **Iniciar:** Menu Run → Start Debugging → Python File
3. **Controles:**
   - Step Into: executa próxima linha
   - Continue: executa até próximo breakpoint
4. **Painel Variables:** mostra valores das variáveis
5. **Debug Console:** permite avaliar expressões

---

## Seção 2 - Mais Sobre Funções

### Objetivos de Aprendizagem

- Conhecer mais sobre argumentos e parâmetros
- Retornar valores de funções
- Adicionar type hints

### Parâmetros vs Argumentos

| Termo | Onde | Exemplo |
|-------|------|---------|
| **Parâmetro** | Na definição da função | `def greet(name):` |
| **Argumento** | Na chamada da função | `greet("Emily")` |

```python
def greet(name):        # 'name' é o parâmetro
    print("Hello", name)

greet("Emily")          # "Emily" é o argumento
```

### Chamando Funções Dentro de Funções

```python
def greet(name):
    print("Hello,", name)

def greet_many_times(name, times):
    while times > 0:
        greet(name)      # Chamando outra função
        times -= 1

greet_many_times("Emily", 3)
```

### Retorno de Valores

A instrução `return` devolve um valor e encerra a função.

```python
def my_sum(a, b):
    return a + b

result = my_sum(2, 3)
print("Sum:", result)  # Sum: 5
```

**Múltiplos returns (saída antecipada):**

```python
def smallest(a, b):
    if a < b:
        return a    # Sai imediatamente se a < b
    return b        # Caso contrário, retorna b

print(smallest(3, 7))  # 3
print(smallest(5, 2))  # 2
```

**Return sem valor (encerrar função):**

```python
def greet(name):
    if name == "":
        print("???")
        return          # Encerra sem retornar valor
    print("Hello,", name)

greet("")       # ???
greet("Emily")  # Hello, Emily
```

### print vs return

```python
# Versão com return - valor pode ser usado depois
def max1(a, b):
    if a > b:
        return a
    return b

result = max1(3, 5)  # result = 5
print(result * 2)    # 10

# Versão com print - apenas exibe, não retorna
def max2(a, b):
    if a > b:
        print(a)
    else:
        print(b)

result = max2(3, 5)  # Imprime 5, mas result = None
```

⚠️ Funções com `return` são mais versáteis - o valor pode ser usado em expressões, atribuições, como argumento de outras funções.

### Usando Valores de Retorno

```python
def my_sum(a, b):
    return a + b

def difference(a, b):
    return a - b

# Retornos como argumentos
result = difference(my_sum(5, 2), my_sum(2, 3))
print(result)  # 7 - 5 = 2
```

### Type Hints

Indicam os tipos esperados (não são obrigatórios, apenas documentação):

```python
def print_many_times(message: str, times: int):
    while times > 0:
        print(message)
        times -= 1

def ask_for_name() -> str:
    name = input("What is your name? ")
    return name
```

- `message: str` → parâmetro deve ser string
- `times: int` → parâmetro deve ser inteiro
- `-> str` → função retorna string

⚠️ Type hints são apenas **dicas** - Python não impede chamadas com tipos errados.

---

## Seção 3 - Listas

### Objetivos de Aprendizagem

- Entender o que são listas em Python
- Acessar itens em uma lista
- Adicionar e remover itens
- Conhecer funções e métodos de lista

### Criando Listas

```python
my_list = []                    # Lista vazia
my_list = [7, 2, 2, 5, 2]       # Lista com 5 itens
```

### Acessando Itens

```python
my_list = [7, 2, 2, 5, 2]

print(my_list[0])   # 7 (primeiro)
print(my_list[1])   # 2 (segundo)
print(my_list[-1])  # 2 (último)
print(my_list)      # [7, 2, 2, 5, 2] (lista inteira)
print(len(my_list)) # 5 (quantidade de itens)
```

### Listas São Mutáveis

Diferente de strings, listas podem ser modificadas:

```python
my_list = [7, 2, 2, 5, 2]
my_list[1] = 3          # Altera segundo item
print(my_list)          # [7, 3, 2, 5, 2]
```

### Adicionando Itens

**`append(item)`** - adiciona no final:

```python
numbers = []
numbers.append(5)
numbers.append(10)
numbers.append(3)
print(numbers)  # [5, 10, 3]
```

**`insert(index, item)`** - adiciona em posição específica:

```python
numbers = [1, 2, 3, 4, 5]
numbers.insert(0, 10)   # Insere 10 no índice 0
print(numbers)          # [10, 1, 2, 3, 4, 5]
numbers.insert(2, 20)   # Insere 20 no índice 2
print(numbers)          # [10, 1, 20, 2, 3, 4, 5]
```

### Removendo Itens

**`pop(index)`** - remove por índice (retorna o item):

```python
my_list = [1, 2, 3, 4, 5, 6]
removed = my_list.pop(2)    # Remove índice 2
print(removed)              # 3
print(my_list)              # [1, 2, 4, 5, 6]
```

**`remove(value)`** - remove por valor (primeira ocorrência):

```python
my_list = [1, 2, 3, 4, 5, 6]
my_list.remove(2)       # Remove o valor 2
print(my_list)          # [1, 3, 4, 5, 6]
```

### Verificando se Item Existe

```python
my_list = [1, 3, 4]

if 1 in my_list:
    print("Found 1")    # Imprime

if 2 in my_list:
    print("Found 2")    # Não imprime
```

### Ordenando Listas

**`sort()`** - modifica a lista original:

```python
my_list = [2, 5, 1, 2, 4]
my_list.sort()
print(my_list)  # [1, 2, 2, 4, 5]
```

**`sorted()`** - retorna nova lista ordenada:

```python
original = [2, 5, 1, 2, 4]
ordered = sorted(original)
print(original)  # [2, 5, 1, 2, 4] (inalterada)
print(ordered)   # [1, 2, 2, 4, 5] (nova lista)
```

### Funções Úteis para Listas

```python
my_list = [5, 2, 3, 1, 4]

print(max(my_list))  # 5 (maior)
print(min(my_list))  # 1 (menor)
print(sum(my_list))  # 15 (soma)
print(len(my_list))  # 5 (quantidade)
```

### Métodos vs Funções

| Tipo | Sintaxe | Exemplo |
|------|---------|---------|
| **Método** | `objeto.método()` | `my_list.append(3)` |
| **Função** | `função(objeto)` | `len(my_list)` |

### Lista como Argumento e Retorno

```python
def median(my_list: list):
    ordered = sorted(my_list)
    middle = len(ordered) // 2
    return ordered[middle]

def input_numbers():
    numbers = []
    while True:
        user_input = input("Number (empty to exit): ")
        if len(user_input) == 0:
            break
        numbers.append(int(user_input))
    return numbers

# Uso
nums = input_numbers()
print("Median:", median(nums))
```

---

## Seção 4 - Iteração Definida (for)

### Objetivos de Aprendizagem

- Conhecer a diferença entre iteração definida e indefinida
- Entender como funciona o loop `for`
- Iterar através de listas e strings

### Iteração Definida vs Indefinida

| Tipo | Loop | Característica |
|------|------|----------------|
| **Indefinida** | `while` | Não sabe quantas iterações |
| **Definida** | `for` | Sabe quantas iterações |

### Estrutura do for

```python
for <variável> in <coleção>:
    <bloco>
```

**Iterando lista:**

```python
my_list = [3, 2, 4, 5, 2]

for item in my_list:
    print(item)
# 3, 2, 4, 5, 2 (cada um em linha separada)
```

**Iterando string:**

```python
name = "Grace"

for character in name:
    print(character)
# G, r, a, c, e (cada um em linha separada)
```

### Função range()

Gera sequência de números.

**Um argumento (0 até n-1):**

```python
for i in range(5):
    print(i)
# 0, 1, 2, 3, 4
```

**Dois argumentos (início até fim-1):**

```python
for i in range(3, 7):
    print(i)
# 3, 4, 5, 6
```

**Três argumentos (início, fim, passo):**

```python
for i in range(1, 9, 2):
    print(i)
# 1, 3, 5, 7

for i in range(6, 2, -1):
    print(i)
# 6, 5, 4, 3
```

### Convertendo range para Lista

```python
numbers = range(2, 7)
print(numbers)        # range(2, 7)

numbers = list(range(2, 7))
print(numbers)        # [2, 3, 4, 5, 6]
```

### Padrão: Encontrar Melhor/Pior Item

```python
def length_of_longest(strings: list):
    best = 0
    for s in strings:
        if len(s) > best:
            best = len(s)
    return best

def shortest(strings: list):
    best = strings[0]
    for s in strings:
        if len(s) < len(best):
            best = s
    return best
```

---

## Seção 5 - Formatação de Print

### Objetivos de Aprendizagem

- Usar argumentos para formatar print
- Usar f-strings para formatação avançada

### Métodos de Formatação

**1. Concatenação com +:**

```python
name = "Mark"
age = 37
print("Hi " + name + " your age is " + str(age))
```

**2. Múltiplos argumentos (separados por vírgula):**

```python
print("Hi", name, "your age is", age)
# Adiciona espaços automaticamente
```

**3. F-strings:**

```python
print(f"Hi {name} your age is {age}")
```

### Argumentos Especiais do print

**`sep`** - separador entre argumentos (padrão: espaço):

```python
print("a", "b", "c", sep="")     # abc
print("a", "b", "c", sep="-")    # a-b-c
print("a", "b", "c", sep="\n")   # Cada um em linha separada
```

**`end`** - final da linha (padrão: `\n`):

```python
print("Hi ", end="")
print("there!")
# Hi there! (mesma linha)
```

### Formatação Avançada com F-strings

**Casas decimais:**

```python
number = 1/3
print(f"Number: {number}")       # 0.333333333...
print(f"Number: {number:.2f}")   # 0.33
print(f"Number: {number:.4f}")   # 0.3333
```

**Largura fixa:**

```python
names = ["Steve", "Jean", "Katherine"]
for name in names:
    print(f"{name:15} done")  # 15 caracteres, alinhado à esquerda
# Steve           done
# Jean            done
# Katherine       done
```

**Alinhamento à direita:**

```python
for name in names:
    print(f"{name:>15}")  # Alinhado à direita
#           Steve
#            Jean
#       Katherine
```

**F-strings fora do print:**

```python
name = "Larry"
age = 48
greeting = f"Hi {name}, you are {age}"
print(greeting)
```

---

## Seção 6 - Mais Strings e Listas

### Objetivos de Aprendizagem

- Conhecer mais métodos de fatiamento
- Entender imutabilidade de strings
- Usar métodos `count` e `replace`

### Fatiamento Avançado

**Com passo:**

```python
my_string = "exemplary"
print(my_string[0:7:2])  # eepa (pula de 2 em 2)

my_list = [1, 2, 3, 4, 5, 6, 7, 8]
print(my_list[6:2:-1])   # [7, 6, 5, 4] (reverso)
```

**Invertendo string/lista:**

```python
my_string = "exemplary"
print(my_string[::-1])   # yralpmexe

my_list = [1, 2, 3]
print(my_list[::-1])     # [3, 2, 1]
```

### Imutabilidade de Strings

**Strings não podem ser modificadas diretamente:**

```python
my_string = "Hey"
my_string[0] = "B"  # ❌ TypeError!
```

**Mas a variável pode receber nova string:**

```python
my_string = "Hey"
my_string = my_string + "!"  # ✅ Cria nova string
print(my_string)  # Hey!
```

**Diferença visual:**

```python
# Lista: modifica o mesmo objeto
my_list = [1, 2, 3]
my_list[0] = 10     # Altera o item

# String: cria novo objeto
my_string = "Hey"
my_string = my_string + "!"  # Nova string
```

### Método count()

Conta ocorrências (funciona em strings e listas):

```python
text = "How much wood would a woodchuck chuck"
print(text.count("ch"))      # 5
print(text.count("wood"))    # 2

my_list = [1, 2, 3, 1, 4, 5, 1, 6]
print(my_list.count(1))      # 3
```

### Método replace()

Cria nova string substituindo ocorrências:

```python
text = "Hi there"
new_text = text.replace("Hi", "Hey")
print(new_text)  # Hey there

# Substitui TODAS as ocorrências
sentence = "she sells seashells"
print(sentence.replace("she", "SHE"))
# SHE sells seaSHElls
```

⚠️ **Erro comum:** Esquecer que `replace` retorna nova string:

```python
my_string = "Python is fun"
my_string.replace("Python", "Java")  # ❌ Não salva!
print(my_string)  # Python is fun

my_string = my_string.replace("Python", "Java")  # ✅ Correto
print(my_string)  # Java is fun
```

### Método split()

Divide string em lista:

```python
sentence = "it was a dark night"
words = sentence.split()  # Divide por espaços
print(words)  # ['it', 'was', 'a', 'dark', 'night']

data = "10,20,30,40"
numbers = data.split(",")  # Divide por vírgula
print(numbers)  # ['10', '20', '30', '40']
```

### Método isupper()

Verifica se string é toda maiúscula:

```python
print("XYZ".isupper())     # True
print("Abc".isupper())     # False
print("abc".isupper())     # False
```

---

## Conceitos-Chave

### Tabela de Referência Rápida

| Conceito | Descrição | Exemplo |
|----------|-----------|---------|
| `return` | Retorna valor da função | `return x + y` |
| Type hint | Indica tipo esperado | `def f(x: int) -> str:` |
| `list[i]` | Acessa item por índice | `my_list[0]` |
| `append()` | Adiciona ao final | `my_list.append(5)` |
| `insert()` | Adiciona em posição | `my_list.insert(0, 5)` |
| `pop()` | Remove por índice | `my_list.pop(2)` |
| `remove()` | Remove por valor | `my_list.remove(5)` |
| `sort()` | Ordena (modifica) | `my_list.sort()` |
| `sorted()` | Ordena (nova lista) | `sorted(my_list)` |
| `for` | Iteração definida | `for x in lista:` |
| `range()` | Gera sequência | `range(1, 10, 2)` |
| `sep` | Separador no print | `print(a, b, sep="-")` |
| `end` | Final no print | `print(a, end="")` |
| `:.2f` | 2 casas decimais | `f"{num:.2f}"` |
| `:>10` | Alinhado à direita | `f"{name:>10}"` |
| `count()` | Conta ocorrências | `text.count("a")` |
| `replace()` | Substitui texto | `text.replace("a", "b")` |
| `split()` | Divide em lista | `text.split(",")` |
| `[::-1]` | Inverte | `text[::-1]` |

### Métodos de Lista

| Método | Descrição | Retorno |
|--------|-----------|---------|
| `append(x)` | Adiciona x no final | None |
| `insert(i, x)` | Adiciona x no índice i | None |
| `pop(i)` | Remove índice i | Item removido |
| `remove(x)` | Remove primeira ocorrência de x | None |
| `sort()` | Ordena a lista | None |
| `reverse()` | Inverte a lista | None |
| `clear()` | Remove todos os itens | None |
| `copy()` | Cria cópia da lista | Nova lista |
| `count(x)` | Conta ocorrências de x | int |
| `index(x)` | Índice de x | int |

### Funções para Listas

| Função | Descrição |
|--------|-----------|
| `len(lista)` | Quantidade de itens |
| `max(lista)` | Maior item |
| `min(lista)` | Menor item |
| `sum(lista)` | Soma dos itens |
| `sorted(lista)` | Nova lista ordenada |
| `list(range(...))` | Converte range em lista |

---

## Resumo Rápido

### Programa Exemplo Completo

```python
def input_numbers() -> list:
    """Lê números do usuário até linha vazia."""
    numbers = []
    while True:
        user_input = input("Number (empty to exit): ")
        if len(user_input) == 0:
            break
        numbers.append(int(user_input))
    return numbers


def statistics(numbers: list) -> str:
    """Retorna estatísticas formatadas."""
    if len(numbers) == 0:
        return "No numbers provided"
    
    total = sum(numbers)
    mean = total / len(numbers)
    
    return f"""Statistics:
  Count: {len(numbers)}
  Sum: {total}
  Mean: {mean:.2f}
  Min: {min(numbers)}
  Max: {max(numbers)}"""


def print_histogram(numbers: list):
    """Imprime histograma visual."""
    for num in numbers:
        print(f"{num:3}: {'*' * num}")


def main():
    print("Enter numbers for analysis")
    nums = input_numbers()
    
    if len(nums) > 0:
        print()
        print(statistics(nums))
        print()
        print("Histogram:")
        print_histogram(nums)
        print()
        print("Sorted:", sorted(nums))
        print("Reversed:", nums[::-1])


if __name__ == "__main__":
    main()
```

### Checklist de Conceitos

- [ ] Sei usar o debugger do VS Code
- [ ] Entendo a diferença entre parâmetro e argumento
- [ ] Sei usar `return` para retornar valores
- [ ] Entendo a diferença entre `print` e `return`
- [ ] Sei usar type hints
- [ ] Sei criar e manipular listas
- [ ] Conheço os métodos `append`, `insert`, `pop`, `remove`
- [ ] Sei a diferença entre `sort()` e `sorted()`
- [ ] Sei usar o loop `for`
- [ ] Sei usar `range()` com 1, 2 ou 3 argumentos
- [ ] Sei formatar números com f-strings (`.2f`, `:>10`)
- [ ] Sei usar `sep` e `end` no print
- [ ] Entendo que strings são imutáveis
- [ ] Sei usar `count`, `replace`, `split`

### Armadilhas Comuns

| Erro | Problema | Solução |
|------|----------|---------|
| `str[0] = "x"` | String imutável | Criar nova string |
| `replace()` sem atribuir | Não salva resultado | `s = s.replace(...)` |
| `sort()` com atribuição | Retorna None | `lista.sort()` ou `nova = sorted(lista)` |
| Variável global em função | Usa variável errada | Usar apenas parâmetros |
| `range(5)` esperando 1-5 | Começa em 0 | `range(1, 6)` |
| `lista[-1]` em lista vazia | IndexError | Verificar `len()` primeiro |

---

## Próximos Passos

Na **Parte 5** você aprenderá:

- Mais sobre listas
- Referências
- Dicionários
- Tuplas

---

**Fonte:** University of Helsinki MOOC - Python Programming  
**Resumo criado por:** Claude (Anthropic)  
**Para:** Eric Alcalai França
