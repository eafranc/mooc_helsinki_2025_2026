# Python: Referências vs Cópias

**Guia Completo sobre Como Python Gerencia Objetos**

---

## Índice

1. [[# Conceito Fundamental]]
2. [[# Tipos de Atribuição]]
3. [[# Comparação com C]]
4. [[# Armadilhas Clássicas]]
5. [[# Quando Modificar vs Criar Novo]]
6. [[# Testando Referências]]

---

## Conceito Fundamental

**Em Python, toda variável é uma REFERÊNCIA a um objeto.**

Isso significa que quando você faz `b = a`, você NÃO está copiando o valor - está criando uma nova referência ao MESMO objeto!

### Exemplo Básico

```python
lista1 = [1, 2, 3]
lista2 = lista1  # Referência (não cópia!)

lista2.append(4)

print(lista1)  # [1, 2, 3, 4] ← modificou!
print(lista2)  # [1, 2, 3, 4]

# São o MESMO objeto:
print(id(lista1) == id(lista2))  # True
```

**O que aconteceu:**
- `lista2` não é uma cópia
- `lista2` APONTA para o mesmo objeto que `lista1`
- Modificar via `lista2` afeta `lista1`

---

## Tipos de Atribuição

### 1. Referência (Default)

**Sintaxe:** `b = a`

```python
original = [1, 2, 3]
referencia = original  # Só cria nova "etiqueta" pro mesmo objeto

referencia.append(4)

print(original)     # [1, 2, 3, 4] ← modificou!
print(referencia)   # [1, 2, 3, 4]

# Verificar:
print(id(original) == id(referencia))  # True
print(original is referencia)          # True
```

**Quando acontece:**
- Atribuição simples: `b = a`
- Passar para função: `func(lista)`
- Retornar de função: `return lista`
- Loop: `for item in lista` (item é referência!)

---

### 2. Cópia Superficial (Shallow Copy)

**Sintaxe:** `b = a.copy()` ou `b = a[:]` ou `b = list(a)`

```python
original = [1, 2, 3]
copia = original.copy()  # Cria NOVA lista

copia.append(4)

print(original)  # [1, 2, 3] ← NÃO modificou!
print(copia)     # [1, 2, 3, 4]

# Verificar:
print(id(original) == id(copia))  # False
print(original is copia)          # False
```

**Métodos equivalentes:**

```python
# Todos fazem cópia superficial:
copia1 = original.copy()
copia2 = original[:]
copia3 = list(original)
```

**Problema com cópia superficial:**

```python
matriz = [[1, 2], [3, 4]]
copia = matriz.copy()

copia[0][0] = 99

print(matriz)  # [[99, 2], [3, 4]] ← modificou!
```

**Por quê?** Copiou a lista externa, mas listas internas ainda são REFERÊNCIAS!

---

### 3. Cópia Profunda (Deep Copy)

**Sintaxe:** `import copy; b = copy.deepcopy(a)`

```python
import copy

matriz = [[1, 2], [3, 4]]
copia_profunda = copy.deepcopy(matriz)

copia_profunda[0][0] = 99

print(matriz)          # [[1, 2], [3, 4]] ← NÃO modificou!
print(copia_profunda)  # [[99, 2], [3, 4]]
```

**Quando usar:**
- Estruturas aninhadas (listas de listas, dicionários de listas, etc)
- Quando precisa isolar completamente

---

## Comparação com C

**Python esconde ponteiros, mas funciona EXATAMENTE como eles!**

### Em C (Explícito)

```c
int lista1[] = {1, 2, 3};
int lista2[] = {4, 5, 6};
int* matriz[] = {lista1, lista2};  // Array de ponteiros!

int* row = matriz[0];  // row aponta para lista1
row[0] = 99;           // Modifica lista1!

printf("%d", lista1[0]);  // 99 ← modificou original!
```

### Em Python (Implícito)

```python
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
matriz = [lista1, lista2]  # Lista de referências!

row = matriz[0]  # row referencia lista1
row[0] = 99      # Modifica lista1!

print(lista1[0])  # 99 ← modificou original!
```

### Tabela Comparativa

| Python | C | Descrição |
|--------|---|-----------|
| `b = a` | `int* b = &a` | Referência/ponteiro |
| `b = a.copy()` | `memcpy(b, a, size)` | Cópia de memória |
| `b = copy.deepcopy(a)` | `memcpy()` recursivo | Cópia profunda |

---

## Armadilhas Clássicas

### Armadilha 1: Lista Default em Função

**PERIGO:**

```python
def adicionar(item, lista=[]):  # Default mutável!
    lista.append(item)
    return lista

print(adicionar(1))  # [1]
print(adicionar(2))  # [1, 2] ← WTF?! Lista "lembra"!
print(adicionar(3))  # [1, 2, 3] ← Todas compartilham MESMA lista!
```

**Por quê?**
- Default é criado UMA vez quando função é definida
- Todas chamadas COMPARTILHAM mesma lista!

**SOLUÇÃO:**

```python
def adicionar(item, lista=None):
    if lista is None:
        lista = []  # Nova lista a cada chamada!
    lista.append(item)
    return lista

print(adicionar(1))  # [1]
print(adicionar(2))  # [2] ← OK!
```

---

### Armadilha 2: Matriz de Referências

**PERIGO:**

```python
linha = [0, 0, 0]
matriz = [linha, linha, linha]  # Todas apontam pra MESMA linha!

matriz[0][0] = 1

print(matriz)  # [[1, 0, 0], [1, 0, 0], [1, 0, 0]] ← WTF?!
```

**SOLUÇÃO:**

```python
matriz = [[0, 0, 0] for _ in range(3)]  # Cria 3 listas DIFERENTES!

matriz[0][0] = 1

print(matriz)  # [[1, 0, 0], [0, 0, 0], [0, 0, 0]] ← OK!
```

---

### Armadilha 3: Loop Modifica Lista Que Itera

**PERIGO:**

```python
numeros = [1, 2, 3, 4, 5, 6]
for num in numeros:
    if num % 2 == 0:
        numeros.remove(num)  # Modifica enquanto itera!

print(numeros)  # [1, 3, 5, 6] ← 6 não foi removido! Bug!
```

**Por quê?** Ao remover elemento, índices mudam, e loop pula elementos!

**SOLUÇÃO:**

```python
# Opção 1: List comprehension (cria nova)
numeros = [1, 2, 3, 4, 5, 6]
numeros = [n for n in numeros if n % 2 != 0]
print(numeros)  # [1, 3, 5] ← OK!

# Opção 2: Iterar sobre cópia
numeros = [1, 2, 3, 4, 5, 6]
for num in numeros[:]:  # Itera sobre CÓPIA!
    if num % 2 == 0:
        numeros.remove(num)
print(numeros)  # [1, 3, 5] ← OK!
```

---

### Armadilha 4: Exemplo do Exercício (row_sums)

**FUNCIONA (porque QUER modificar):**

```python
def row_sums(my_matrix: list):
    for row in my_matrix:  # row é REFERÊNCIA!
        row.append(sum(row))  # Modifica original!

matriz = [[1, 2], [3, 4]]
row_sums(matriz)
print(matriz)  # [[1, 2, 3], [3, 4, 7]] ← Modificou original (OK!)
```

**Por que funciona:**
- Requisito era modificar in-place
- `row` é referência à lista original
- `.append()` modifica a lista original

**Não é bug, é feature!**

---

## Quando Modificar vs Criar Novo

### Modificar Original (In-Place)

**Quando usar:**

✅ Requisito pede explicitamente

```python
# "função NÃO retorna nada, modifica in-place"
def row_sums(matriz):
    for row in matriz:
        row.append(sum(row))
    # Sem return!
```

✅ Economizar memória

```python
# Lista gigante (10 milhões de elementos)
lista_gigante.sort()  # Modifica in-place (economiza memória)
```

**Métodos que modificam in-place:**
- `.append()`, `.extend()`, `.insert()`
- `.remove()`, `.pop()`
- `.sort()`, `.reverse()`
- `lista[i] = valor`

---

### Criar Nova (Retornar)

**Quando usar:**

✅ Preservar original

```python
def row_sums_nova(matriz):
    return [row + [sum(row)] for row in matriz]
    # Original intacto!
```

✅ Programação funcional (imutabilidade)

```python
nova = sorted(original)  # Retorna nova, não modifica!
```

**Métodos que retornam novo:**
- `sorted(lista)` (vs `.sort()`)
- `lista.copy()`
- List comprehensions
- `map()`, `filter()`

---

## Testando Referências

### Usar `id()` para Ver Identidade

```python
lista1 = [1, 2, 3]
lista2 = lista1        # Referência
lista3 = lista1.copy() # Cópia

print(id(lista1))  # 140234567891234
print(id(lista2))  # 140234567891234 ← MESMO!
print(id(lista3))  # 140234567899999 ← DIFERENTE!
```

### Operador `is` vs `==`

```python
lista1 = [1, 2, 3]
lista2 = lista1
lista3 = lista1.copy()

# is: verifica se é o MESMO objeto
print(lista1 is lista2)  # True (mesmo objeto)
print(lista1 is lista3)  # False (objetos diferentes)

# ==: verifica se tem MESMO conteúdo
print(lista1 == lista2)  # True
print(lista1 == lista3)  # True (conteúdo igual!)
```

**Regra:**
- `is` → identidade (mesmo objeto?)
- `==` → igualdade (mesmo valor?)

---

## Visualização Mental

```python
# Referência (duas etiquetas, um objeto):
lista1 = [1, 2, 3]
lista2 = lista1

# Memória:
# [1, 2, 3] ← lista1 e lista2 apontam pra AQUI
```

```python
# Cópia (duas etiquetas, dois objetos):
lista1 = [1, 2, 3]
lista2 = lista1.copy()

# Memória:
# [1, 2, 3] ← lista1 aponta pra aqui
# [1, 2, 3] ← lista2 aponta pra aqui (OUTRO objeto!)
```

---

## Resumo Executivo

### Regras de Ouro

1. **Atribuição simples = referência**
   ```python
   b = a  # b aponta para MESMO objeto
   ```

2. **Métodos mutantes modificam original**
   ```python
   lista.append(4)  # Modifica in-place
   ```

3. **Para copiar, seja EXPLÍCITO**
   ```python
   copia = lista.copy()  # Superficial
   copia = copy.deepcopy(lista)  # Profunda
   ```

4. **Em loops, item é referência**
   ```python
   for row in matriz:
       row.append(...)  # Modifica original!
   ```

5. **Default mutável = perigo**
   ```python
   def func(lista=[]):  # NUNCA!
   def func(lista=None):  # Sempre!
   ```

### Quando Usar Cada

| Situação | Usar |
|----------|------|
| Quer modificar original | Referência (`b = a`) |
| Quer preservar original | Cópia (`.copy()`) |
| Lista de listas | Cópia profunda (`deepcopy`) |
| Passar pra função e modificar | Referência (default) |
| Passar pra função sem modificar | Depende (função deve copiar se precisar) |

---

**Guia criado:** Dezembro 2025  
**Contexto:** Python MOOC - Part 8  
**Fonte:** Discussão sobre exercício row_sums
