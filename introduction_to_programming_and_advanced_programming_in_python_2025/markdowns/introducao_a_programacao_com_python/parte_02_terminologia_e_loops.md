# Parte 2 - Terminologia de Programação e Loops

## Índice

- [[#Seção 1 - Terminologia de Programação]]
- [[#Seção 2 - Mais Sobre Condicionais]]
- [[#Seção 3 - Combinando Condições]]
- [[#Seção 4 - Loops Simples]]
- [[#Conceitos-Chave]]
- [[#Resumo Rápido]]

---

## Seção 1 - Terminologia de Programação

### Objetivos de Aprendizagem

- Familiarizar-se com a terminologia essencial de programação
- Entender a diferença entre statement e expression
- Descobrir o tipo de dado de uma expressão avaliada
- Usar métodos de debugging para encontrar erros no código

### Conceitos Fundamentais

#### Statement (Declaração/Instrução)

Uma **statement** é uma parte do programa que executa algo. Geralmente se refere a um único comando.

```python
print("Hi!")      # statement de print
number = 2        # statement de atribuição
```

Statements podem conter outras statements:

```python
if name == "Anna":       # statement condicional
    print("Hi!")         # statement dentro do if
    number = 2           # outra statement dentro do if
```

#### Block (Bloco)

Um **block** é um grupo de statements consecutivas no mesmo nível da estrutura do programa.

```python
if age > 17:
    # início do bloco condicional
    print("You are of age!")
    age = age + 1
    print("You are now one year older...")
    # fim do bloco condicional

print("This here belongs to another block")
```

**Em Python:** Blocos são definidos pela **indentação** (espaços/tabs no início da linha).

⚠️ **Importante:** O bloco principal de um programa Python deve estar sempre na borda esquerda, sem indentação.

#### Expression (Expressão)

Uma **expression** é um trecho de código que resulta em um valor com tipo de dado determinado.

| Expressão | Valor | Tipo | Tipo Python |
|-----------|-------|------|-------------|
| `2 + 4 + 3` | 9 | inteiro | `int` |
| `"abc" + "de"` | "abcde" | string | `str` |
| `11 / 2` | 5.5 | ponto flutuante | `float` |
| `2 * 5 > 9` | True | booleano | `bool` |

Expressões podem ser atribuídas a variáveis:

```python
x = 1 + 2           # x recebe o valor da expressão
y = 3 * x + x**2    # expressões podem ser combinadas
```

#### Function (Função)

Uma **function** executa alguma funcionalidade. Pode receber **argumentos** (dados para processar).

```python
print("this is an argument")   # função com argumento

name = input("Please type in your name: ")  # função que retorna valor
```

- **Argumento/Parâmetro:** Dados passados para a função
- **Retorno:** Valor que a função devolve após execução

#### Data Type (Tipo de Dado)

Características de qualquer valor no programa.

```python
name = "Anna"       # tipo: str (string)
result = 100        # tipo: int (integer)

print(type("Anna")) # <class 'str'>
print(type(100))    # <class 'int'>
```

A função `type()` revela o tipo de dado de qualquer expressão.

#### Syntax (Sintaxe)

Regras que determinam como o código deve ser escrito.

```python
# ✅ Sintaxe correta
if name == "Anna":
    print("Hi!")

# ❌ Sintaxe incorreta (falta ":")
if name == "Anna"
    print("Hi!")
# SyntaxError: invalid syntax
```

### Debugging (Depuração)

**Debugging** é o processo de encontrar e corrigir bugs (erros) no programa.

#### Tipos de Bugs

1. **Erros de execução** - Programa para com mensagem de erro
2. **Erros de lógica** - Programa roda mas resultado está errado

#### Técnica: Print Statements para Debugging

```python
# Problema: domingo não está dobrando o salário
hourly_wage = 20.0
hours = 6
day = "Sunday"

daily_wages = hourly_wage * hours

# Debugging: verificar se a condição é verdadeira
print("condition:", day == "sunday")  # False! (S maiúsculo vs minúsculo)

if day == "sunday":
    print("wages before:", daily_wages)
    daily_wages * 2  # Bug: não está atribuindo!
    print("wages after:", daily_wages)
```

**Bugs encontrados:**
1. `"Sunday"` ≠ `"sunday"` (case-sensitive)
2. `daily_wages * 2` calcula mas não armazena → usar `daily_wages *= 2`

#### Dica: Hard-coding para Testes

```python
# Ao invés de pedir input toda vez:
# hourly_wage = float(input("Hourly wage: "))

# Temporariamente fixar valores para testar:
hourly_wage = 20.0
hours = 6
day = "Sunday"
```

---

## Seção 2 - Mais Sobre Condicionais

### Objetivos de Aprendizagem

- Criar múltiplos branches em statements condicionais
- Entender o propósito de `if`, `elif` e `else`
- Usar operação módulo `%` em expressões booleanas

### Estrutura if-else

Quando há apenas duas alternativas mutuamente exclusivas:

```python
number = int(input("Please type in a number: "))

if number < 0:
    print("The number is negative")
else:
    print("The number is positive or zero")
```

**Regra:** Exatamente um dos branches será executado.

⚠️ **Importante:** Não pode haver `else` sem um `if` antes dele.

### Operador Módulo (%)

Retorna o **resto** da divisão inteira.

```python
# Verificar se número é par ou ímpar
if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")
```

Exemplos:
- `10 % 2` → `0` (par)
- `7 % 2` → `1` (ímpar)
- `17 % 5` → `2`

### Estrutura if-elif-else

Quando há **mais de duas** alternativas:

```python
goals_home = int(input("Home goals scored: "))
goals_away = int(input("Away goals scored: "))

if goals_home > goals_away:
    print("The home team won!")
elif goals_away > goals_home:
    print("The away team won!")
else:
    print("It's a tie!")
```

**Características:**
- Pode haver múltiplos `elif`
- O `else` é opcional
- Apenas **um** branch é executado
- Branches são avaliados em ordem (primeiro `if`, depois `elif`s, por fim `else`)

### Exemplo: Calendário de Feriados

```python
print("Holiday calendar")
date = input("What is the date today? ")

if date == "Dec 26":
    print("It's Boxing Day")
elif date == "Dec 31":
    print("It's Hogmanay")
elif date == "Jan 1":
    print("It's New Year's Day")

print("Thanks and bye.")
```

Se nenhuma condição for verdadeira e não houver `else`, nenhum branch é executado.

---

## Seção 3 - Combinando Condições

### Objetivos de Aprendizagem

- Usar operadores `and`, `or` e `not` em condições
- Escrever condicionais aninhados

### Operadores Lógicos

#### Operador `and`

**Todas** as condições devem ser verdadeiras.

```python
if number >= 5 and number <= 8:
    print("The number is between 5 and 8")
```

#### Operador `or`

**Pelo menos uma** condição deve ser verdadeira.

```python
if number < 5 or number > 8:
    print("The number is not within the range of 5 to 8")
```

#### Operador `not`

**Nega** (inverte) a condição.

```python
if not (number >= 5 and number <= 8):
    print("The number is not within the range of 5 to 8")
```

### Tabela-Verdade

| a | b | a and b | a or b |
|---|---|---------|--------|
| False | False | False | False |
| True | False | False | True |
| False | True | False | True |
| True | True | True | True |

| a | not a |
|---|-------|
| True | False |
| False | True |

### Notação Simplificada do Python

Python permite uma forma mais curta para verificar intervalos:

```python
# Forma longa
if x >= a and x <= b:

# Forma curta (Python permite!)
if a <= x <= b:
```

⚠️ Esta notação é exclusiva do Python e não funciona na maioria das outras linguagens.

### Combinando Múltiplas Condições

```python
n1 = int(input("Number 1: "))
n2 = int(input("Number 2: "))
n3 = int(input("Number 3: "))
n4 = int(input("Number 4: "))

if n1 > n2 and n1 > n3 and n1 > n4:
    greatest = n1
elif n2 > n3 and n2 > n4:
    greatest = n2
elif n3 > n4:
    greatest = n3
else:
    greatest = n4

print(f"{greatest} is the greatest of the numbers.")
```

### Condicionais Aninhados

Um `if` dentro de outro `if`:

```python
number = int(input("Please type in a number: "))

if number > 0:
    if number % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")
else:
    print("The number is negative or zero")
```

**Equivalente com operadores lógicos:**

```python
if number > 0 and number % 2 == 0:
    print("The number is even")
elif number > 0 and number % 2 != 0:
    print("The number is odd")
else:
    print("The number is negative or zero")
```

Ambas as abordagens funcionam. A escolha depende de qual é mais legível no contexto.

### Exemplo Clássico: FizzBuzz

```python
num = int(input("Number:"))
result = ""

if num % 3 == 0:
    result += "Fizz"
if num % 5 == 0:
    result += "Buzz"

print(result)
```

**Lógica:**
- Divisível por 3 → "Fizz"
- Divisível por 5 → "Buzz"
- Divisível por ambos → "FizzBuzz"

---

## Seção 4 - Loops Simples

### Objetivos de Aprendizagem

- Entender o que significa loop em programação
- Usar `while True` em programas
- Usar o comando `break` para sair de um loop

### Estruturas de Controle

| Tipo | Função |
|------|--------|
| **Condicional** | Escolher entre seções de código |
| **Iteração** (loop) | Repetir seções de código |

Uma **iteração** é uma execução do bloco do loop.

### Loop while True

```python
while True:
    number = int(input("Please type in a number, -1 to quit: "))

    if number == -1:
        break

    print(number ** 2)

print("Thanks and bye!")
```

**Saída:**
```
Please type in a number, -1 to quit: 2
4
Please type in a number, -1 to quit: 4
16
Please type in a number, -1 to quit: -1
Thanks and bye!
```

### Comando break

O `break` **sai imediatamente** do loop e continua na primeira linha após o bloco `while`.

⚠️ **Loop infinito:** Se não houver forma de executar `break`, o loop roda para sempre!

```python
# ❌ Loop infinito - input está FORA do loop
number = int(input("Please type in a number, -1 to quit: "))
while True:
    if number == -1:
        break
    print(number ** 2)  # Imprime para sempre!
```

### Exemplo: Verificação de PIN

```python
while True:
    code = input("Please type in your PIN: ")
    if code == "1234":
        break
    print("Incorrect...try again")

print("Correct PIN entered!")
```

### Variáveis Auxiliares em Loops

#### Contador de tentativas

```python
attempts = 0

while True:
    code = input("Please type in your PIN: ")
    attempts += 1

    if code == "1234":
        success = True
        break

    if attempts == 3:
        success = False
        break

    print("Incorrect...try again")

if success:
    print("Correct PIN entered!")
else:
    print("Too many attempts...")
```

**Padrão:**
1. Inicializar variável antes do loop
2. Modificar dentro do loop
3. Usar após o loop

#### Concatenação de strings

```python
codes = ""       # string vazia
attempts = 0

while True:
    code = input("Please type in your PIN: ")
    attempts += 1
    codes += code + ", "   # acumula todos os códigos
    # ...
```

### Debugging em Loops

A **ordem das condições** é crucial:

```python
# ❌ Bug: verifica tentativas ANTES de verificar código
while True:
    code = input("PIN: ")
    attempts += 1

    if attempts == 3:      # Executado primeiro!
        success = False
        break

    if code == "1234":     # Nunca alcançado na 3ª tentativa
        success = True
        break
```

**Solução:** Verificar código correto ANTES de verificar tentativas.

### Print Statements em Loops

```python
while True:
    print("beginning of the while block:")
    code = input("PIN: ")
    attempts += 1

    print("attempts:", attempts)
    print("condition1:", attempts == 3)

    if attempts == 3:
        success = False
        break

    print("code:", code)
    print("condition2:", code == "1234")
    # ...
```

---

## Conceitos-Chave

### Tabela de Referência Rápida

| Conceito | Descrição | Exemplo |
|----------|-----------|---------|
| **Statement** | Comando que executa algo | `print("Hi")` |
| **Block** | Grupo de statements no mesmo nível | Código dentro do `if` |
| **Expression** | Código que resulta em valor | `2 + 3`, `x > 5` |
| **Function** | Executa funcionalidade, pode retornar valor | `input()`, `print()` |
| **Data type** | Tipo do valor | `int`, `str`, `float`, `bool` |
| **Syntax** | Regras de escrita do código | `:` após `if` |
| **Debugging** | Encontrar e corrigir bugs | Print statements |
| **if-elif-else** | Múltiplos branches condicionais | Ver seção 2 |
| **and** | Todas condições verdadeiras | `x > 0 and x < 10` |
| **or** | Pelo menos uma verdadeira | `x < 0 or x > 10` |
| **not** | Inverte a condição | `not (x > 5)` |
| **while True** | Loop infinito (até `break`) | Ver seção 4 |
| **break** | Sai do loop | `if x == 0: break` |
| **%** (módulo) | Resto da divisão | `7 % 3` → `1` |

### Operadores de Comparação

| Operador | Significado |
|----------|-------------|
| `==` | Igual a |
| `!=` | Diferente de |
| `>` | Maior que |
| `<` | Menor que |
| `>=` | Maior ou igual a |
| `<=` | Menor ou igual a |

---

## Resumo Rápido

### Programa Exemplo Completo

```python
# Jogo de adivinhação com limite de tentativas
import random

secret = random.randint(1, 10)
attempts = 0
max_attempts = 3

print("Guess the number (1-10)")

while True:
    guess = int(input("Your guess: "))
    attempts += 1

    if guess == secret:
        print(f"Correct! You got it in {attempts} attempts!")
        break

    if attempts == max_attempts:
        print(f"Game over! The number was {secret}")
        break

    if guess < secret:
        print("Too low!")
    else:
        print("Too high!")

    remaining = max_attempts - attempts
    print(f"Attempts remaining: {remaining}")

print("Thanks for playing!")
```

### Checklist de Conceitos

- [ ] Entendo a diferença entre statement e expression
- [ ] Sei usar `type()` para verificar tipos de dados
- [ ] Domino a estrutura `if-elif-else`
- [ ] Sei usar operadores lógicos: `and`, `or`, `not`
- [ ] Entendo a tabela-verdade
- [ ] Sei usar a notação simplificada `a <= x <= b`
- [ ] Consigo criar condicionais aninhados
- [ ] Entendo como funciona `while True` com `break`
- [ ] Sei usar variáveis auxiliares (contadores, acumuladores)
- [ ] Sei adicionar print statements para debugging

### Armadilhas Comuns

| Erro | Problema | Solução |
|------|----------|---------|
| `if x = 5` | `=` ao invés de `==` | `if x == 5` |
| `"Sunday" == "sunday"` | Case-sensitive | Padronizar ou usar `.lower()` |
| `x * 2` sem atribuir | Não armazena resultado | `x *= 2` ou `x = x * 2` |
| Loop infinito | Sem condição de saída | Garantir que `break` seja alcançável |
| Ordem errada no loop | Verifica limite antes do sucesso | Reorganizar condições |
| `else` sem `if` | Sintaxe inválida | `else` sempre após `if` ou `elif` |

---

## Próximos Passos

Na **Parte 3** você aprenderá:

- Loops `while` com condições (não apenas `True`)
- Loops `for` para iteração
- Strings em mais detalhes
- Operações com strings

---

**Fonte:** University of Helsinki MOOC - Python Programming  
**Resumo criado por:** Claude (Anthropic)  
**Para:** Eric Alcalai França
