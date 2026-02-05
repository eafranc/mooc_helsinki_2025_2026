# Introdução ao IPython

IPython é um **shell interativo aprimorado** para Python. Ele oferece uma experiência de REPL (Read–Eval–Print Loop) mais rica que o interpretador padrão, com histórico avançado, auto-completar, inspeção de objetos e comandos especiais chamados *magics*.

---

## 1. O que é o IPython

- IPython é um ambiente interativo para executar código Python linha a linha ou em blocos.
- Ele roda sobre o Python "normal" (como o CPython 3.14 que você instalou) e não é uma implementação alternativa da linguagem.
- Os resultados de cada comando ficam numerados como `In [n]:` e `Out[n]:`, e podem ser reutilizados.

### Principais vantagens em relação ao shell padrão

- Histórico navegável com setas ↑ e ↓.
- Autocompletar com Tab para nomes de variáveis, funções, métodos e módulos.
- Inspeção rápida de objetos com `?` e `??`.
- *Magics* para tarefas comuns (medir tempo, rodar scripts, ver histórico etc.).

---

## 2. Relação entre IPython e Jupyter

- Jupyter Notebook e JupyterLab usam o **kernel IPython** quando a linguagem escolhida é Python.
- Em termos simples: 
  - IPython = o motor/interprete interativo.
  - Jupyter = a interface web (notebooks com células de código, texto, gráficos, etc.).
- Quase tudo que funciona no IPython do terminal também funciona em células de um notebook Jupyter (magics, `?`, histórico da sessão, etc.).

---

## 3. Operação básica do IPython

### Iniciar e sair

- Iniciar (no PowerShell ou terminal):
  - `ipython`
  - ou `python -m IPython`
- Sair da sessão:
  - Digite `exit` ou `quit` e pressione Enter; ou
  - Use `Ctrl+Z` seguido de Enter no Windows.

### Executar código

- **Uma linha**: digite a expressão e pressione Enter.
- **Blocos com múltiplas linhas** (`for`, `if`, `while`, `def`, `class`):
  1. Digite a primeira linha, por exemplo: `for i in range(3):` e aperte Enter.
  2. As linhas seguintes aparecem com o prompt `...:`; escreva o corpo indentado.
  3. Quando terminar o bloco, pressione Enter em branco para executar.

Exemplo:

```python
for i in range(3):
    print(i)
```

### Reutilizar resultados

- O último resultado é guardado em `_`.
- Resultados numerados ficam em `_1`, `_2`, `_3`, ... de acordo com o número da entrada.

Exemplo:

```python
In [1]: 2 + 3
Out[1]: 5

In [2]: _1 * 10
Out[2]: 50
```

---

## 4. Inspeção e ajuda (`?` e `??`)

- `obj?` mostra assinatura, docstring e tipo.
- `obj??` tenta mostrar ainda mais detalhes (incluindo o código fonte, quando possível).

Exemplos (parecidos com o que você já fez):

```python
In [1]: len?
In [2]: x = [10, 20, 30]
In [3]: x?
In [4]: x.pop??
```

Esses comandos são excelentes para estudar a biblioteca padrão e entender melhor funções e métodos.

---

## 5. Autocompletar e histórico

### Autocompletar com Tab

- Digite o começo de um nome e pressione Tab:

```python
In [1]: x = [1, 2, 3]
In [2]: x.ap  # pressione Tab aqui
```

- IPython mostrará opções como `append`.

### Histórico de comandos

- Use setas ↑ e ↓ para navegar pelos comandos anteriores.
- Comando mágico `%history` ou `%hist` mostra o histórico da sessão:

```python
In [3]: %history
```

---

## 6. Magics importantes

Magics são comandos especiais do IPython, começando com `%` (linha única) ou `%%` (célula inteira).

### Magics de uso frequente

- `%history` ou `%hist`: mostra o histórico de comandos.
- `%timeit expr`: mede o tempo de execução de uma expressão ou bloco.
- `%run script.py`: executa um arquivo Python como se fosse `python script.py`.
- `%pwd`: mostra o diretório atual.
- `%cd caminho`: troca de diretório.
- `%ls` (ou `%dir` em algumas plataformas): lista arquivos no diretório atual.
- `%quickref`: mostra um resumo rápido de ajuda do IPython.

Exemplos:

```python
In [1]: %pwd
In [2]: %cd C:/Users/erfra/
In [3]: %run meu_script.py
In [4]: %timeit sum(range(1000))
```

---

## 7. Integração com arquivos .py

Você pode usar o IPython como ambiente de testes para scripts:

- Escreva seu código em um arquivo `meu_script.py`.
- No IPython, navegue até a pasta do arquivo com `%cd`.
- Execute o script com:

```python
%run meu_script.py
```

Tudo o que o script definir (funções, classes, variáveis) ficará disponível no namespace interativo após a execução.

---

## 8. Roteiro de prática inicial

Um roteiro simples para consolidar o uso do IPython:

1. **Explorar o shell**
   - Abra o IPython.
   - Rode algumas expressões simples: `2 + 2`, `10 / 3`, `"oi" * 3`.
   - Observe os prompts `In [n]:` e `Out[n]:`.

2. **Trabalhar com listas**
   - Crie uma lista: `x = [10, 20, 30]`.
   - Use `type(x)` e `x?`.
   - Experimente métodos: `x.append(40)`, `x.pop()`, `x.insert(0, 5)`.
   - Use `len(x)` e navegue pelo histórico com ↑.

3. **Praticar laços e condicionais**
   - Faça um `for` imprimindo números, como você já fez.
   - Crie uma função simples com `def` (por exemplo, `def dobro(n): return 2 * n`).
   - Chame a função várias vezes.

4. **Usar magics**
   - Execute `%history` depois de alguns comandos.
   - Rode `%timeit sum(range(100000))`.
   - Use `%pwd` e `%cd` para navegar em diretórios.

5. **Brincar com ajuda e exploração**
   - Use `len?`, `list?`, `dict?`, `str?`.
   - Use `list.append??`, `str.split??` para ver mais detalhes.

6. **Conectar com Jupyter (opcional)**
   - Se instalar Jupyter depois, perceba que tudo o que você aprendeu aqui se transfere quase 1:1 para as células de um notebook.

---

## 9. Dicas finais

- Use IPython como laboratório: teste ideias pequenas antes de colocá-las em arquivos `.py`.
- Combine IPython com o VS Code: você pode abrir o terminal integrado e trabalhar com o mesmo ambiente de pacotes.
- Faça uso pesado de `?` e `??` — eles substituem boa parte de ficar alternando entre o código e a documentação na web.
