# Parte 1 - Introdução ao Python

## Índice
- [[#Seção 1 - Primeiros Passos]]
- [[#Seção 2 - Entrada de Dados do Usuário]]
- [[#Seção 3 - Mais Sobre Variáveis]]
- [[#Seção 4 - Operações Aritméticas]]
- [[#Seção 5 - Declarações Condicionais]]
- [[#Conceitos-Chave]]
- [[#Resumo Rápido]]

---

## Seção 1 - Primeiros Passos

### Objetivos de Aprendizagem
- Escrever e executar o primeiro programa Python
- Usar o comando `print()`
- Realizar operações aritméticas básicas

### Conceito: Comando `print()`

**Imprime texto ou valores na tela**

```python
# Imprimindo texto (strings)
print("Hi there!")  # Output: Hi there!

# Múltiplas linhas
print("Linha 1")
print("Linha 2")
print("Linha 3")
```

### Strings vs Operações Aritméticas

```python
# COM aspas = string (texto literal)
print("2 + 5")        # Output: 2 + 5

# SEM aspas = operação (calcula)
print(2 + 5)          # Output: 7
```

### Operações Aritméticas Básicas

```python
print(2 + 5)          # 7 (adição)
print(3 * 3)          # 9 (multiplicação)
print(2 + 2 * 10)     # 22 (multiplicação primeiro!)
```

**Ordem de operações:** `*` e `/` antes de `+` e `-`

### Comentários

```python
# Isso é um comentário - Python ignora
print(365 * 24)  # Comentário no final da linha
```

- Começam com `#`
- Python ignora tudo após `#`
- Usados para explicar o código

### Aspas Simples vs Duplas

```python
print("Hello")              # funciona
print('Hello')              # também funciona
print('"Hi!", he said.')    # aspas simples fora, duplas dentro
```

### ⚠️ Armadilhas Comuns

❌ **Esquecer aspas:**
```python
print(Hi there!)  # ERRO! SyntaxError
```

✅ **Correto:**
```python
print("Hi there!")
```

---

## Seção 2 - Entrada de Dados do Usuário

### Objetivos de Aprendizagem
- Usar `input()` para ler dados do usuário
- Armazenar dados em variáveis
- Combinar strings com `+`

### Comando `input()`

```python
# Lê entrada do usuário
name = input("What is your name? ")
print("Hi there, " + name)
```

**Execução:**
```
What is your name? Paul
Hi there, Paul
```

### Variáveis

**Variável** = local para armazenar um valor (string, número, etc)

```python
name = input("What is your name? ")  # armazena na variável 'name'
print(name)  # usa a variável
```

### Concatenação de Strings

Operador `+` combina strings:

```python
name = "Paul"
print("Hi " + name + "! Nice to meet you.")
# Output: Hi Paul! Nice to meet you.
```

### Múltiplas Entradas

```python
name = input("What is your name? ")
email = input("What is your email? ")
nickname = input("What is your nickname? ")

print("Your name: " + name)
print("Your email: " + email)
print("Your nickname: " + nickname)
```

### Reutilizando Variáveis

**Novo valor substitui o antigo:**

```python
address = input("What is your address? ")
print("You live at: " + address)

address = input("New address: ")  # substitui o valor
print("Your address is now: " + address)  # valor antigo perdido!
```

### Nomenclatura de Variáveis

**Regras:**
- Começar com letra
- Conter apenas letras, números e `_` (underscore)
- Lowercase é convenção em Python
- Nomes em inglês (convenção internacional)
- Nomes descritivos (ex: `name` melhor que `n`)

```python
# ✅ Bom
user_name = "Paul"
age = 25

# ❌ Ruim
n = "Paul"
a = 25
```

---

## Seção 3 - Mais Sobre Variáveis

### Objetivos de Aprendizagem
- Entender tipos de dados (strings, int, float)
- Diferenciar strings de números
- Usar variáveis em diferentes contextos

### Tipos de Dados

Python tem três tipos fundamentais:

| Tipo | Descrição | Exemplo |
|------|-----------|---------|
| `str` | String (texto) | `"Hello"`, `"123"` |
| `int` | Inteiro | `42`, `-5`, `0` |
| `float` | Ponto flutuante | `3.14`, `-0.5` |

### Inteiros (`int`)

```python
age = 24  # sem aspas = número
print(age)  # Output: 24

# COM aspas = string!
age = "24"  # isso é texto, não número
```

### Diferença: Número vs String

```python
number1 = 100      # int
number2 = "100"    # str

print(number1 + number1)  # 200 (adição)
print(number2 + number2)  # 100100 (concatenação!)
```

**Operador `+`:**
- Com números → adição
- Com strings → concatenação

### Operações Inválidas

```python
number = "100"
print(number / 2)  # ❌ ERRO! TypeError
# Não pode dividir string por número
```

### Combinando Tipos ao Imprimir

❌ **Não funciona:**
```python
result = 250
print("The result is " + result)  # ERRO! str + int
```

✅ **Solução 1: Converter com `str()`**
```python
result = 250
print("The result is " + str(result))
```

✅ **Solução 2: Vírgula no print**
```python
result = 250
print("The result is", result)  # espaço automático
```

✅ **Solução 3: F-strings** (Melhor!)
```python
result = 250
print(f"The result is {result}")
```

### F-strings (Formatação)

```python
name = "Mark"
age = 37
city = "Palo Alto"

print(f"Hi {name}, you are {age} years old. You live in {city}.")
# Output: Hi Mark, you are 37 years old. You live in Palo Alto.
```

**Vantagens:**
- Mais limpo que concatenação
- Não adiciona espaços indesejados
- Mais fácil de ler

**Sintaxe:**
- `f` antes das aspas
- Variáveis dentro de `{}`

### Números de Ponto Flutuante (`float`)

```python
number1 = 2.5
number2 = -1.25
number3 = 3.62

mean = (number1 + number2 + number3) / 3
print(f"Mean: {mean}")
# Output: Mean: 1.6233333333333333
```

### Parâmetro `end` do print

Por padrão, `print()` adiciona quebra de linha. Use `end=""` para evitar:

```python
print("Hi ", end="")
print("there!")
# Output: Hi there! (mesma linha)
```

### ⚠️ Compatibilidade: F-strings

F-strings funcionam apenas no **Python 3.6+**. Se usar versão antiga, use concatenação ou vírgulas.

---

## Seção 4 - Operações Aritméticas

### Objetivos de Aprendizagem
- Usar variáveis em operações aritméticas
- Lidar com números do usuário
- Converter entre tipos de dados

### Operadores Aritméticos

| Operador | Operação | Exemplo | Resultado |
|----------|----------|---------|-----------|
| `+` | Adição | `2 + 4` | `6` |
| `-` | Subtração | `10 - 2.5` | `7.5` |
| `*` | Multiplicação | `-2 * 123` | `-246` |
| `/` | Divisão (float) | `9 / 2` | `4.5` |
| `//` | Divisão inteira | `9 // 2` | `4` |
| `%` | Módulo (resto) | `9 % 2` | `1` |
| `**` | Exponenciação | `2 ** 3` | `8` |

### Ordem de Operações

```python
print(2 + 3 * 3)    # 11 (multiplicação primeiro)
print((2 + 3) * 3)  # 15 (parênteses alteram ordem)
```

**Prioridade:**
1. `**` (exponenciação)
2. `*`, `/`, `//`, `%`
3. `+`, `-`
4. Parênteses `()` alteram a ordem

### Divisão: `/` vs `//`

```python
x = 3
y = 2

print(x / y)   # 1.5 (sempre retorna float)
print(x // y)  # 1 (divisão inteira, arredonda para baixo)
```

### Tipo do Resultado

**Regra:** Se **qualquer** operando é `float`, resultado é `float`

```python
print(5 + 3)      # 8 (int + int = int)
print(5.0 + 3)    # 8.0 (float + int = float)
print(1 / 5)      # 0.2 (divisão sempre retorna float!)
```

### Convertendo Entrada do Usuário

`input()` **sempre** retorna string. Para usar como número, converta:

```python
# ❌ Errado
year = input("Year: ")
age = 2021 - year  # ERRO! str - int

# ✅ Correto
year = int(input("Year: "))
age = 2021 - year  # funciona!
```

### Funções de Conversão

```python
int(input("Number: "))     # converte para inteiro
float(input("Number: "))   # converte para float
str(42)                    # converte para string
```

**Exemplo completo:**
```python
height = float(input("Height (cm): "))
weight = float(input("Weight (kg): "))

height = height / 100  # converte cm para metros
bmi = weight / height ** 2

print(f"BMI: {bmi}")
```

### Reutilizando Variáveis

```python
# Calculando soma de 3 números
sum = 0

sum += int(input("First: "))
sum += int(input("Second: "))
sum += int(input("Third: "))

print(f"Sum: {sum}")
```

### Operadores de Atribuição Compostos

```python
sum = 0
sum += 5    # equivale a: sum = sum + 5
sum -= 2    # equivale a: sum = sum - 2
sum *= 3    # equivale a: sum = sum * 3
sum /= 4    # equivale a: sum = sum / 4
```

### Quando Usar Múltiplas Variáveis

✅ **Use variáveis separadas quando precisar dos valores depois:**
```python
num1 = int(input("First: "))
num2 = int(input("Second: "))
print(f"{num1} + {num2} = {num1 + num2}")
```

✅ **Reutilize variáveis quando só precisar do resultado final:**
```python
sum = 0
sum += int(input("First: "))
sum += int(input("Second: "))
print(f"Sum: {sum}")
```

---

## Seção 5 - Declarações Condicionais

### Objetivos de Aprendizagem
- Usar declarações condicionais (`if`)
- Entender valores booleanos
- Usar operadores de comparação

### Estrutura Condicional `if`

```python
age = int(input("How old are you? "))

if age > 17:
    print("You are of age!")
    print("Here's your copy of GTA6.")

print("Next customer, please!")
```

**Execução:**
- Se `age > 17` é **True**: executa bloco indentado
- Se `age > 17` é **False**: pula o bloco

### Sintaxe do `if`

```
if condição:
    código indentado
    mais código indentado
código não indentado (sempre executa)
```

**Importante:**
- `:` (dois pontos) após a condição
- Indentação (Tab ou 4 espaços) define o bloco
- Sem indentação = fora do `if`

### Operadores de Comparação

| Operador | Significado | Exemplo | Resultado |
|----------|-------------|---------|-----------|
| `==` | Igual a | `a == b` | True se iguais |
| `!=` | Diferente de | `a != b` | True se diferentes |
| `>` | Maior que | `a > b` | True se a > b |
| `>=` | Maior ou igual | `a >= b` | True se a ≥ b |
| `<` | Menor que | `a < b` | True se a < b |
| `<=` | Menor ou igual | `a <= b` | True se a ≤ b |

### Múltiplas Condições

```python
number = int(input("Number: "))

if number < 0:
    print("Negative")

if number > 0:
    print("Positive")

if number == 0:
    print("Zero")
```

### Indentação

**Crucial em Python!** Define blocos de código.

```python
# ✅ Correto
if password == "secret":
    print("Access granted")
    print("Welcome!")
print("Program ended")

# ❌ Errado (indentação inconsistente)
if password == "secret":
    print("Access granted")
  print("Welcome!")  # erro de indentação!
```

**Dicas:**
- Use Tab para indentar
- Backspace para desindentar
- Todas as linhas do bloco devem ter mesma indentação

### Valores Booleanos

Tipo `bool` - apenas dois valores possíveis:

```python
True   # verdadeiro
False  # falso
```

**Expressões booleanas** retornam `True` ou `False`:

```python
a = 3
print(a < 5)  # True
print(a > 10) # False
```

### Armazenando Condições

```python
a = 3
condition = a < 5  # armazena True ou False

print(condition)   # True

if condition:
    print("a is less than 5")
```

### Usando `True` e `False` Diretamente

```python
condition = True

if condition:
    print("This always executes")
```

Não muito útil sozinho, mas útil em programas mais complexos.

### ⚠️ Erros Comuns

❌ **Esquecer os dois pontos:**
```python
if age > 17  # ERRO! SyntaxError
    print("Adult")
```

❌ **Confundir `=` com `==`:**
```python
if age = 18:  # ERRO! = é atribuição, == é comparação
```

❌ **Indentação errada:**
```python
if age > 17:
print("Adult")  # ERRO! Precisa estar indentado
```

---

## Conceitos-Chave

### Comandos Básicos

| Comando | Uso | Exemplo |
|---------|-----|---------|
| `print()` | Exibe na tela | `print("Hello")` |
| `input()` | Lê do usuário | `name = input("Name: ")` |
| `int()` | Converte para inteiro | `age = int("25")` |
| `float()` | Converte para float | `price = float("9.99")` |
| `str()` | Converte para string | `text = str(42)` |

### Tipos de Dados

```python
# String (texto)
name = "Paul"
number_str = "123"

# Integer (inteiro)
age = 25
count = -5

# Float (ponto flutuante)
price = 9.99
temperature = -3.5

# Boolean (booleano)
is_adult = True
is_raining = False
```

### Operadores

**Aritméticos:**
```python
+   # adição
-   # subtração
*   # multiplicação
/   # divisão (float)
//  # divisão inteira
%   # módulo (resto)
**  # exponenciação
```

**Atribuição composta:**
```python
+=  # x += 5  →  x = x + 5
-=  # x -= 3  →  x = x - 3
*=  # x *= 2  →  x = x * 2
/=  # x /= 4  →  x = x / 4
```

**Comparação:**
```python
==  # igual
!=  # diferente
>   # maior
>=  # maior ou igual
<   # menor
<=  # menor ou igual
```

### F-strings

```python
name = "Alice"
age = 30

# Formato antigo (evite)
print("Name: " + name + ", Age: " + str(age))

# F-string (preferido!)
print(f"Name: {name}, Age: {age}")

# Com expressões
print(f"Next year: {age + 1}")
```

### Estrutura Condicional

```python
if condição:
    # bloco executado se True
    código
    mais código
# código fora do if (sempre executa)
```

---

## Resumo Rápido

### Programa Completo Exemplo

```python
# Entrada
name = input("What is your name? ")
age = int(input("How old are you? "))

# Processamento
years_to_adult = 18 - age

# Saída com condição
print(f"Hi {name}!")

if age >= 18:
    print("You are an adult.")
else:
    print(f"You will be an adult in {years_to_adult} years.")
```

### Checklist de Conceitos

- [ ] `print()` para exibir texto e números
- [ ] `input()` para ler dados do usuário
- [ ] Variáveis armazenam valores
- [ ] Strings usam aspas (`"` ou `'`)
- [ ] Comentários começam com `#`
- [ ] Operações aritméticas: `+`, `-`, `*`, `/`, `//`, `%`, `**`
- [ ] Converter tipos: `int()`, `float()`, `str()`
- [ ] F-strings: `f"texto {variavel}"`
- [ ] Condicionais: `if condição:`
- [ ] Indentação define blocos
- [ ] Operadores: `==`, `!=`, `>`, `<`, `>=`, `<=`
- [ ] Valores booleanos: `True`, `False`

### Armadilhas Comuns

| Erro | Problema | Solução |
|------|----------|---------|
| `print(texto)` | Sem aspas | `print("texto")` |
| `if x = 5:` | `=` ao invés de `==` | `if x == 5:` |
| `if x > 5` | Sem `:` | `if x > 5:` |
| `"5" + 3` | String + int | `int("5") + 3` ou `"5" + str(3)` |
| Indentação errada | Bloco mal definido | Use Tab consistentemente |

---

## Próximos Passos

Na **Parte 2** você aprenderá:
- Estruturas condicionais mais complexas (`elif`, `else`)
- Loops (`while`, `for`)
- Mais sobre strings
- Funções básicas

---

**Dica de Estudo:** Pratique escrevendo pequenos programas que combinam todos estes conceitos. Por exemplo, uma calculadora simples que pede dois números e uma operação, ou um programa que calcula IMC e dá feedback baseado no resultado.

---

**Fonte:** University of Helsinki MOOC - Python Programming  
**Resumo criado por:** Claude (Anthropic)  
**Para:** Eric Alcalai França