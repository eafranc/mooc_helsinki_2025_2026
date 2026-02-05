# Guia Completo: IFs Aninhados vs Simplificação

**Quando Aninhar? Quando Simplificar?**

---

## Índice

1. [[# Regra de Ouro]]
2. [[# Quando IFs Aninhados SÃO Necessários]]
3. [[# Quando IFs Aninhados NÃO São Necessários]]
4. [[# Testes Mentais Para Decidir]]
5. [[# Estatísticas Práticas]]
6. [[# Padrões de Simplificação]]

---

## Regra de Ouro

**IFs aninhados são necessários quando há DEPENDÊNCIA REAL entre condições.**

**Dependência Real** = A segunda condição só pode ser avaliada SE a primeira for verdadeira.

### Teste Rápido

```python
# Se isso funciona SEM erro:
if A and B:
    fazer()

# Então NÃO precisa de aninhamento!

# Se isso dá erro (AttributeError, TypeError, etc):
if A and B:  # ERRO!
    fazer()

# Então aninhamento PODE ser necessário:
if A:
    if B:
        fazer()
```

---

## Quando IFs Aninhados SÃO Necessários

### Caso 1: Acessar Atributo Que Pode Não Existir

**ANINHAMENTO NECESSÁRIO:**

```python
if usuario:
    if usuario.email:  # Só posso verificar SE usuario existe!
        enviar_email(usuario.email)
```

**POR QUÊ NÃO SIMPLIFICAR?**

```python
# ISSO QUEBRARIA:
if usuario and usuario.email:  # AttributeError se usuario = None!
    enviar_email(usuario.email)
```

**Razão:** Python avalia `usuario.email` antes de checar se `usuario` é None.

---

### Caso 2: Segunda Condição Depende de Efeito da Primeira

**ANINHAMENTO NECESSÁRIO:**

```python
arquivo = None
if arquivo_existe("data.txt"):
    arquivo = abrir("data.txt")  # Cria variável
    if arquivo.tamanho > 0:      # Usa variável criada acima
        processar(arquivo)
```

**POR QUÊ NÃO SIMPLIFICAR?**

```python
# ISSO QUEBRARIA:
if arquivo_existe("data.txt") and arquivo.tamanho > 0:  
    # arquivo ainda é None!
```

**Razão:** `arquivo` só existe DENTRO do primeiro if.

---

### Caso 3: Verificação de Tipo Antes de Operação

**ANINHAMENTO NECESSÁRIO:**

```python
if isinstance(valor, dict):
    if "chave" in valor:  # Só posso usar 'in' SE for dict!
        return valor["chave"]
```

---

### Caso 4: Quando Aninhamento É Mais Legível

**ANINHAMENTO MAIS CLARO:**

```python
if modo == "desenvolvimento":
    if debug_habilitado:
        printar_logs_detalhados()
    else:
        printar_logs_basicos()
else:
    # Produção: sem logs
    pass
```

---

## Quando IFs Aninhados NÃO São Necessários

### Caso 1: Condições Independentes

**ANINHAMENTO DESNECESSÁRIO:**

```python
# Ruim:
if x > 0:
    if y > 0:
        return True
```

**SIMPLIFICADO (MELHOR):**

```python
# Bom:
if x > 0 and y > 0:
    return True
```

**Razão:** `y > 0` não depende de `x > 0` - são independentes!

---

### Caso 2: Sequência de Validações (Guard Clauses)

**ANINHAMENTO DESNECESSÁRIO:**

```python
# Ruim:
if valor:
    if isinstance(valor, int):
        if valor > 0:
            processar(valor)
```

**SIMPLIFICADO (MELHOR - Early Return):**

```python
# Bom:
if not valor:
    return
if not isinstance(valor, int):
    return
if valor <= 0:
    return
processar(valor)
```

**Razão:** São guards sequenciais - early return é mais claro!

---

## Testes Mentais Para Decidir

### Teste 1: "Posso Inverter a Ordem?"

```python
# Caso 1:
if x > 0:
    if y > 0:
        fazer()

# Invertendo:
if y > 0:
    if x > 0:
        fazer()

# Funciona igual? SIM → Não há dependência → Use AND!
```

---

### Teste 2: "A Segunda Condição Faz Sentido Sozinha?"

**Pergunte:** "Posso avaliar B sem avaliar A primeiro?"

**Se SIM:** Use AND ou separe

```python
if x > 0 and y > 0:  # Ambas fazem sentido sozinhas
```

**Se NÃO:** Aninhamento necessário

```python
if arquivo:
    if arquivo.tamanho > 0:  # Tamanho só faz sentido SE arquivo existe
```

---

## Estatísticas Práticas

**Em código bem escrito:**

- **90%:** IFs podem ser simplificados
  - 60% → AND simples
  - 20% → Early return
  - 10% → Flags independentes

- **10%:** IFs aninhados são necessários
  - 6% → Acesso a atributos que podem não existir
  - 3% → Dependência de efeitos colaterais
  - 1% → Legibilidade (aninhamento mais claro)

---

## Padrões de Simplificação

### Padrão 1: IF Aninhado → AND

**Antes:**

```python
if A:
    if B:
        fazer()
```

**Depois:**

```python
if A and B:
    fazer()
```

---

### Padrão 2: IF-ELSE Aninhado → Early Return

**Antes:**

```python
if condição1:
    if condição2:
        return A
    else:
        return B
else:
    return C
```

**Depois:**

```python
if not condição1:
    return C
if not condição2:
    return B
return A
```

---

## Checklist de Decisão

Quando encontrar IF aninhado, pergunte:

- [ ] As condições são independentes? → Use AND
- [ ] São validações sequenciais? → Use early return
- [ ] Segunda depende de efeito da primeira? → Aninhamento necessário
- [ ] Segunda acessa atributo da primeira? → Aninhamento necessário
- [ ] Posso inverter ordem sem erro? → Use AND

---

## Resumo Executivo

### Quando ANINHAR:

1. Acessar atributos que podem não existir
2. Segunda condição depende de efeito da primeira
3. Verificações de tipo antes de operações
4. Quando aninhamento é genuinamente mais legível

### Quando SIMPLIFICAR:

1. Condições independentes → AND
2. Sequência de validações → Early return
3. Flags booleanas → Inicialização inteligente
4. Qualquer caso onde simplificação não causa erro

### Regra Final:

**Se pode simplificar sem erro, simplifique!**

**Se simplificar causa erro, aninhamento é necessário.**

---

**Guia criado:** Dezembro 2025  
**Contexto:** Python MOOC - Part 7
