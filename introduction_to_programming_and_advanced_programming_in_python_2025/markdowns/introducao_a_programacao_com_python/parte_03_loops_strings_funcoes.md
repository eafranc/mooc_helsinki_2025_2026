# Parte 3 - Loops Avançados, Strings e Funções

## Índice

- [[#Seção 1 - Loops com Condições]]
- [[#Seção 2 - Trabalhando com Strings]]
- [[#Seção 3 - Mais Sobre Loops]]
- [[#Seção 4 - Definindo Funções]]
- [[#Conceitos-Chave]]
- [[#Resumo Rápido]]

---

## Seção 1 - Loops com Condições

### Objetivos de Aprendizagem

- Criar loops `while` com condições
- Entender os papéis de inicialização, condição e atualização
- Criar loops com diferentes tipos de condições

### Estrutura Geral do while

```python
while <condição>:
    <bloco>
```

**Funcionamento:**
1. Verifica a condição
2. Se `True`, executa o bloco
3. Volta ao passo 1
4. Se `False`, sai do loop e continua o programa

### Exemplo Básico

```python
number = int(input("Please type in a number: "))

while number < 10:
    print(number)
    number += 1

print("Execution finished.")
```

**Saída com input 4:**
```
4
5
6
7
8
9
Execution finished.
```

**Saída com input 12:**
```
Execution finished.
```

⚠️ A condição é verificada **antes** de executar o bloco. Se já for `False` no início, o bloco nunca executa.

### Os Três Componentes de um Loop

| Componente | Descrição | Quando |
|------------|-----------|--------|
| **Inicialização** | Definir valor inicial da variável | Antes do loop |
| **Condição** | Definir quando o loop continua | No início do `while` |
| **Atualização** | Modificar a variável de iteração | Dentro do loop |

```python
# Inicialização
number = 1

# Condição
while number < 10:
    print(number)
    # Atualização
    number += 1
```

⚠️ **Erro comum:** Esquecer a atualização causa loop infinito!

```python
# ❌ Loop infinito - falta atualização
number = 1
while number < 10:
    print(number)  # Imprime 1 para sempre!
```

### Condições Compostas

```python
number = int(input("Please type in a number: "))

# Loop continua enquanto AMBAS condições forem verdadeiras
while number < 100 and number % 5 != 0:
    print(number)
    number += 3
```

### Cuidado com Loops Infinitos

```python
number = int(input("Please type in a number: "))

while number != 10:
    print(number)
    number += 2
```

Este loop:
- ✅ Termina se input for par e ≤ 10 (ex: 4 → 6 → 8 → 10)
- ❌ Loop infinito se input for ímpar (ex: 3 → 5 → 7 → 9 → 11 → ...)
- ❌ Loop infinito se input for > 10 (ex: 12 → 14 → 16 → ...)

### Dicas de Debugging

#### Hard-coding para Testes

```python
# Durante testes, fixar o valor ao invés de pedir input:
limit = 8  # int(input("Upper limit: "))
number = 1

while number <= limit:
    print(number)
    number *= 2
```

#### Python Tutor

Ferramenta visual para acompanhar execução linha por linha: https://pythontutor.com

### Construindo Strings em Loops

```python
words = "pride"
words += ", prejudice"    # Concatenação com +=
words += " and python"

print(words)  # pride, prejudice and python
```

**Com f-strings:**

```python
course = "Introduction to Programming"
grade = 4

verdict = "You have received "
verdict += f"the grade {grade} "
verdict += f"from the course {course}"

print(verdict)
```

**Acumulando em loop:**

```python
limit = int(input("Limit: "))
count = 1
total = 1
calculation = "1"

while total < limit:
    count += 1
    total += count
    calculation += f" + {count}"

calculation += f" = {total}"
print(f"The consecutive sum: {calculation}")
# Ex: The consecutive sum: 1 + 2 + 3 + 4 = 10
```

---

## Seção 2 - Trabalhando com Strings

### Objetivos de Aprendizagem

- Usar operadores `+` e `*` com strings
- Descobrir o comprimento de uma string
- Entender indexação de strings
- Buscar substrings dentro de strings

### Operações com Strings

#### Concatenação (+)

```python
begin = "ex"
end = "ample"
word = begin + end
print(word)  # example
```

#### Repetição (*)

```python
word = "banana"
print(word * 3)  # bananabananabanana
```

#### Exemplo: Pirâmide de Asteriscos

```python
n = 5
row = "*"

while n > 0:
    print(" " * n + row)
    row += "**"
    n -= 1
```

**Saída:**
```
     *
    ***
   *****
  *******
 *********
```

### Comprimento de String: len()

```python
print(len("hey"))      # 3
print(len("bye bye"))  # 7 (espaço conta!)
print(len(""))         # 0 (string vazia)
```

**Exemplo: Sublinhando texto**

```python
text = input("Please type in a string: ")
print(text)
print("-" * len(text))
```

### Indexação de Strings

Cada caractere tem um **índice** (posição), começando em 0.

```
String:  m  o  n  k  e  y
Índice:  0  1  2  3  4  5
```

```python
word = "monkey"
print(word[0])   # m (primeiro)
print(word[1])   # o (segundo)
print(word[5])   # y (último)
print(word[-1])  # y (último, índice negativo)
print(word[-2])  # e (penúltimo)
```

#### Índices Negativos

```
String:  m  o  n  k  e  y
Índice: -6 -5 -4 -3 -2 -1
```

```python
word = "testing"
print(word[0])   # t (primeiro)
print(word[-1])  # g (último)
print(word[len(word) - 1])  # g (equivalente a -1)
```

#### Percorrendo uma String

```python
text = "test"
index = 0

while index < len(text):
    print(text[index])
    index += 1
```

### IndexError

```python
word = "python"
print(word[10])  # IndexError: string index out of range
```

**Prevenindo erros:**

```python
text = input("Please type in a string: ")

if len(text) > 0:
    print("First character:", text[0])
else:
    print("The string is empty.")
```

### Substrings e Fatiamento (Slicing)

**Sintaxe:** `string[início:fim]`

- Inclui o caractere no índice `início`
- **Exclui** o caractere no índice `fim`

```python
word = "presumptious"

print(word[0:3])   # pre
print(word[4:10])  # umptio
print(word[:3])    # pre (início omitido = 0)
print(word[4:])    # umptious (fim omitido = len)
```

**Calculando o tamanho do slice:** `fim - início`

### Operador in

Verifica se uma substring existe dentro de uma string.

```python
text = "test"

print("t" in text)    # True
print("x" in text)    # False
print("es" in text)   # True
print("ets" in text)  # False
```

**Uso prático:**

```python
word = "perpendicular"
substring = input("What are you looking for? ")

if substring in word:
    print("Found it")
else:
    print("Not found")
```

### Método find()

Retorna o **índice** da primeira ocorrência da substring, ou **-1** se não encontrar.

```python
text = "test"

print(text.find("t"))    # 0 (primeira ocorrência)
print(text.find("x"))    # -1 (não encontrado)
print(text.find("es"))   # 1
print(text.find("ets"))  # -1
```

**Uso prático:**

```python
word = "perpendicular"
substring = input("What are you looking for? ")
index = word.find(substring)

if index >= 0:
    print(f"Found it at index {index}")
else:
    print("Not found")
```

### Métodos vs Funções

| Função | Método |
|--------|--------|
| `len(text)` | `text.find("x")` |
| Chamada independente | Chamada no objeto |
| `função(objeto)` | `objeto.método()` |

---

## Seção 3 - Mais Sobre Loops

### Objetivos de Aprendizagem

- Entender quando usar `break`
- Usar `continue` para pular iterações
- Entender loops aninhados

### Comando break

Termina o loop imediatamente.

**Versão com break:**

```python
sum = 0

while True:
    number = int(input("Number (-1 to exit): "))
    if number == -1:
        break
    sum += number

print(f"The sum is {sum}")
```

**Versão equivalente sem break:**

```python
sum = 0
number = 0

while number != -1:
    number = int(input("Number (-1 to exit): "))
    if number != -1:
        sum += number

print(f"The sum is {sum}")
```

A versão com `break` é geralmente mais limpa.

#### Combinando Condição e break

```python
sum = 0

while sum <= 100:  # Condição principal
    number = int(input("Number (-1 to exit): "))
    if number == -1:  # Condição de saída antecipada
        break
    sum += number

print(f"The sum is {sum}")
```

O loop termina quando:
1. `sum > 100` (condição do while), OU
2. Usuário digita `-1` (break)

### Comando continue

Pula para a **próxima iteração** do loop, ignorando o resto do bloco.

```python
sum = 0

while True:
    number = int(input("Number (-1 to exit): "))
    if number == -1:
        break
    if number >= 10:
        continue  # Ignora números >= 10
    sum += number

print(f"The sum is {sum}")
```

**Saída exemplo:**
```
Number: 4
Number: 7
Number: 99    ← ignorado pelo continue
Number: 5
Number: -1
The sum is 16  (4 + 7 + 5)
```

### Loops Aninhados

Um loop dentro de outro.

```python
while True:
    number = int(input("Please type in a number: "))
    if number == -1:
        break
    
    # Loop interno: conta regressiva
    while number > 0:
        print(number)
        number -= 1
```

**Saída:**
```
Please type in a number: 3
3
2
1
Please type in a number: -1
```

⚠️ **Importante:** `break` e `continue` afetam apenas o loop **mais interno**.

### Variáveis Auxiliares em Loops Aninhados

```python
number = int(input("Please type in a number: "))

while number > 0:
    i = 0  # Reinicializa a cada iteração do loop externo
    
    while i < number:
        print(f"{i} ", end="")
        i += 1
    
    print()  # Nova linha
    number -= 1
```

**Saída com input 5:**
```
0 1 2 3 4
0 1 2 3
0 1 2
0 1
0
```

### Exemplo: Tabuada

```python
num = int(input("Please type in a number: "))
i = 1

while i <= num:
    j = 1
    while j <= num:
        print(f"{i} x {j} = {i * j}")
        j += 1
    i += 1
```

---

## Seção 4 - Definindo Funções

### Objetivos de Aprendizagem

- Escrever e chamar suas próprias funções
- Entender argumentos e parâmetros
- Definir parâmetros em funções

### Estrutura de uma Função

```python
def nome_da_funcao():
    # corpo da função (indentado)
    print("Hello!")
```

**Partes:**
1. `def` - palavra-chave para definir função
2. `nome_da_funcao` - nome escolhido
3. `()` - parênteses (podem conter parâmetros)
4. `:` - dois-pontos
5. Bloco indentado - corpo da função

### Chamando uma Função

```python
def message():
    print("This is my very own function!")

# Chamando a função
message()
message()
message()
```

**Saída:**
```
This is my very own function!
This is my very own function!
This is my very own function!
```

⚠️ Definir a função não executa seu código. É preciso **chamá-la**.

### Funções com Parâmetros

```python
def hello(target):
    print("Hello", target)

hello("Emily")   # Hello Emily
hello("world!")  # Hello world!
```

- **Argumento:** valor passado na chamada (`"Emily"`)
- **Parâmetro:** variável que recebe o valor na definição (`target`)

### Múltiplos Parâmetros

```python
def sum(x, y):
    result = x + y
    print(f"The sum of {x} and {y} is {result}")

sum(1, 2)    # The sum of 1 and 2 is 3
sum(5, 24)   # The sum of 5 and 24 is 29
```

### Parâmetros são Locais

Os nomes dos parâmetros são independentes de variáveis externas:

```python
def sum(x, y):
    print(f"x = {x}, y = {y}")

x = 100
y = 30
sum(1, 2)        # x = 1, y = 2
sum(x + y, 10)   # x = 130, y = 10
```

### Estrutura para Testes

```python
def greet():
    print("Hi!")

# Código de teste dentro deste bloco:
if __name__ == "__main__":
    greet()
```

O bloco `if __name__ == "__main__":` não é executado pelos testes automáticos do curso.

### Exemplo: Função com Condição

```python
def hello(name):
    if name == "Emily":
        print("Hello", name)
    else:
        print("Hi", name)

hello("Emily")  # Hello Emily
hello("Mark")   # Hi Mark
```

### Exemplo: Função com Loop

```python
def hash_square(length):
    row = 1
    while row <= length:
        print("#" * length)
        row += 1

hash_square(3)
# ###
# ###
# ###
```

### ⚠️ Evite Variáveis Globais

```python
# ❌ ERRADO - usa variável global por engano
name = "Betty"

def hello(given_name):
    print("Hello", name)  # Usa 'name' global, não 'given_name'!

hello("Steve")  # Hello Betty (errado!)
hello("Betty")  # Hello Betty
```

**Sempre use os parâmetros dentro da função!**

---

## Conceitos-Chave

### Tabela de Referência Rápida

| Conceito | Descrição | Exemplo |
|----------|-----------|---------|
| `while condição` | Loop com condição | `while x < 10:` |
| Inicialização | Valor inicial da variável | `x = 0` |
| Atualização | Modificar variável no loop | `x += 1` |
| `len(s)` | Comprimento da string | `len("abc")` → 3 |
| `s[i]` | Caractere no índice i | `"abc"[1]` → "b" |
| `s[-1]` | Último caractere | `"abc"[-1]` → "c" |
| `s[a:b]` | Slice de a até b-1 | `"abcde"[1:4]` → "bcd" |
| `x in s` | Substring existe? | `"bc" in "abcd"` → True |
| `s.find(x)` | Índice da substring | `"abc".find("b")` → 1 |
| `break` | Sai do loop | Ver seção 3 |
| `continue` | Pula para próxima iteração | Ver seção 3 |
| `def` | Define função | `def func():` |
| Argumento | Valor passado na chamada | `func(5)` |
| Parâmetro | Variável na definição | `def func(x):` |

### Operadores de String

| Operador | Descrição | Exemplo |
|----------|-----------|---------|
| `+` | Concatenação | `"a" + "b"` → `"ab"` |
| `*` | Repetição | `"a" * 3` → `"aaa"` |
| `in` | Pertence | `"a" in "abc"` → `True` |
| `[]` | Indexação | `"abc"[0]` → `"a"` |
| `[:]` | Fatiamento | `"abc"[0:2]` → `"ab"` |

---

## Resumo Rápido

### Programa Exemplo Completo

```python
def analyze_word(word):
    """Analisa uma palavra e imprime estatísticas."""
    print(f"\nAnalyzing: {word}")
    print("-" * 20)
    
    # Comprimento
    print(f"Length: {len(word)}")
    
    # Primeiro e último
    if len(word) > 0:
        print(f"First char: {word[0]}")
        print(f"Last char: {word[-1]}")
    
    # Contar vogais
    vowels = "aeiou"
    count = 0
    i = 0
    while i < len(word):
        if word[i].lower() in vowels:
            count += 1
        i += 1
    print(f"Vowels: {count}")


def main():
    while True:
        word = input("\nType a word (empty to quit): ")
        
        if len(word) == 0:
            break
        
        if len(word) < 2:
            print("Word too short, skipping...")
            continue
        
        analyze_word(word)
    
    print("\nGoodbye!")


if __name__ == "__main__":
    main()
```

### Checklist de Conceitos

- [ ] Sei criar `while` com condições (não apenas `True`)
- [ ] Entendo inicialização, condição e atualização
- [ ] Sei usar `len()` para obter comprimento de string
- [ ] Entendo indexação positiva e negativa
- [ ] Sei fazer slicing com `[início:fim]`
- [ ] Sei usar `in` para verificar substring
- [ ] Sei usar `find()` para localizar substring
- [ ] Entendo a diferença entre `break` e `continue`
- [ ] Sei criar loops aninhados
- [ ] Sei definir funções com `def`
- [ ] Entendo a diferença entre argumento e parâmetro
- [ ] Sei usar o bloco `if __name__ == "__main__":`

### Armadilhas Comuns

| Erro | Problema | Solução |
|------|----------|---------|
| Loop infinito | Esqueceu atualização | Sempre atualizar variável |
| `IndexError` | Índice fora do range | Verificar `len()` antes |
| `s[len(s)]` | Índice inválido | Usar `s[len(s)-1]` ou `s[-1]` |
| Variável global | Usar variável externa na função | Usar apenas parâmetros |
| `break` em loop aninhado | Sai só do interno | Usar flag ou reestruturar |

---

## Próximos Passos

Na **Parte 4** você aprenderá:

- Mais sobre funções (retorno de valores)
- Listas
- Mais sobre strings
- O loop `for`

---

**Fonte:** University of Helsinki MOOC - Python Programming  
**Resumo criado por:** Claude (Anthropic)  
**Para:** Eric Alcalai França
