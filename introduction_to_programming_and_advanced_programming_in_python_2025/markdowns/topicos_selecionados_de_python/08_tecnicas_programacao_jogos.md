# Técnicas de Programação para Jogos

**Contexto:** Padrões úteis aprendidos durante o curso de Python da Universidade de Helsinki (Parte 13 - Pygame)

---

## Índice

- [[#1. Clamping (Limitação de Valores)]]
- [[#2. Object Pooling (Reutilização de Objetos)]]
- [[#3. Flag-Based Movement (Movimento com Bandeiras)]]
- [[#4. Delta Time (Tempo Independente de FPS)]]
- [[#5. Separação de Responsabilidades no Game Loop]]
- [[#6. Dicionário de Teclas Pressionadas]]
- [[#7. Data-Driven Design (Design Orientado a Dados)]]
- [[#Resumo Comparativo]]

---

## 1. Clamping (Limitação de Valores)

### O que é

Técnica para **forçar um valor a permanecer dentro de um intervalo válido**. Em vez de verificar antes de modificar, você modifica livremente e depois "clampa" o resultado.

### Problema

Impedir que um personagem saia dos limites da tela.

### Abordagem ingênua (verificar antes)

```python
# Verifica E move na mesma linha
if to_left and x >= 0:
    x -= 2
if to_right and x <= width - robot_w:
    x += 2
```

**Problemas:**
- Mistura duas responsabilidades (movimento + limite)
- Difícil de modificar depois
- Código fica verboso com muitas condições

### Abordagem com Clamping (mover, depois limitar)

```python
# Passo 1: Move livremente
if to_left:
    x -= 2
if to_right:
    x += 2

# Passo 2: Força o valor para dentro dos limites
x = max(x, 0)                    # não deixa ficar < 0
x = min(x, width - robot_w)      # não deixa ficar > limite direito
```

### Versão compacta com função clamp

Python não tem `clamp` nativo, mas você pode criar:

```python
def clamp(valor, minimo, maximo):
    """Força valor para dentro do intervalo [minimo, maximo]."""
    return max(minimo, min(valor, maximo))

# Uso:
x = clamp(x, 0, width - robot_w)
y = clamp(y, 0, height - robot_h)
```

### Por que é melhor

| Aspecto | Verificar antes | Clamping |
|---------|-----------------|----------|
| Responsabilidades | Misturadas | Separadas |
| Legibilidade | Condições longas | Código limpo |
| Manutenção | Difícil modificar | Fácil ajustar limites |
| Reutilização | Repetitivo | Função única |

### Outros usos de Clamping

```python
# Limitar vida do jogador entre 0 e 100
vida = clamp(vida, 0, 100)

# Limitar volume entre 0.0 e 1.0
volume = clamp(volume, 0.0, 1.0)

# Limitar zoom da câmera
zoom = clamp(zoom, 0.5, 3.0)

# Limitar ângulo de rotação
angulo = clamp(angulo, -45, 45)
```

---

## 2. Object Pooling (Reutilização de Objetos)

### O que é

Técnica para **reutilizar objetos em vez de criar e destruir** constantemente. Você mantém um "pool" (piscina) de objetos pré-alocados e recicla eles quando não estão mais em uso.

### Problema

Em um jogo com robôs caindo infinitamente, criar novos objetos e destruir os antigos consome memória e processamento.

### Abordagem ingênua (criar/destruir)

```python
# Pseudo-código problemático
robots = []

while True:
    # Cria novos robôs constantemente
    if random_chance():
        robots.append(create_new_robot())
    
    # Remove robôs que saíram da tela
    robots = [r for r in robots if r.is_visible()]
    
    # Problema: lista cresce e diminui, 
    # garbage collector trabalha muito
```

### Abordagem com Object Pooling

```python
# Passo 1: Pré-aloca todos os objetos no início
number_of_robots = 20
positions = []

for i in range(number_of_robots):
    x = randint(0, width - robot_w)
    y = randint(-1000, -100)  # começa acima da tela
    positions.append([x, y])

# Passo 2: No loop, recicla em vez de destruir
while True:
    for i in range(number_of_robots):
        x = positions[i][0]
        y = positions[i][1]
        
        # Atualiza posição normalmente...
        # (código de movimento)
        
        # Quando sai da tela: RECICLA
        if x < -robot_w or x > width:
            # "Reseta" o robô para uma nova posição inicial
            positions[i][0] = randint(0, width - robot_w)
            positions[i][1] = randint(-1000, -100)
```

### Diagrama do ciclo de vida

```
┌─────────────────────────────────────────────────────┐
│                    OBJECT POOL                       │
│  ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐           │
│  │ R1  │ │ R2  │ │ R3  │ │ ... │ │ R20 │           │
│  └──┬──┘ └──┬──┘ └──┬──┘ └──┬──┘ └──┬──┘           │
└─────┼───────┼───────┼───────┼───────┼───────────────┘
      │       │       │       │       │
      ▼       ▼       ▼       ▼       ▼
   ┌─────────────────────────────────────┐
   │           TELA DO JOGO              │
   │                                     │
   │    Robôs caem, andam, saem...       │
   │                                     │
   └─────────────────────────────────────┘
      │       │       │       │       │
      │       │       │       │       │
      └───────┴───────┴───────┴───────┘
                      │
                      ▼
              Saiu da tela?
                      │
            ┌─────────┴─────────┐
            │ SIM               │ NÃO
            ▼                   ▼
      Recicla (reseta      Continua
      posição para         normalmente
      cima da tela)
```

### Por que é importante

| Sem pooling | Com pooling |
|-------------|-------------|
| Aloca memória constantemente | Memória fixa |
| Garbage collector ativo | GC quase não trabalha |
| Performance degrada com tempo | Performance constante |
| Pode causar "stuttering" | Animação suave |

### Outros usos de Object Pooling

```python
# Pool de projéteis (tiros)
bullets = [Bullet() for _ in range(100)]

# Pool de partículas (explosões, fumaça)
particles = [Particle() for _ in range(500)]

# Pool de inimigos
enemies = [Enemy() for _ in range(50)]

# Pool de sons (para não recarregar do disco)
sounds = {
    'jump': pygame.mixer.Sound('jump.wav'),
    'hit': pygame.mixer.Sound('hit.wav'),
}
```

---

## 3. Flag-Based Movement (Movimento com Bandeiras)

### O que é

Usar variáveis booleanas (flags) para rastrear **estado contínuo** de teclas pressionadas, separando a **detecção de eventos** da **atualização de movimento**.

### Problema

`KEYDOWN` dispara apenas uma vez quando a tecla é pressionada. Para movimento contínuo, você precisa saber se a tecla **ainda está** pressionada.

### Abordagem errada (mover no evento)

```python
# PROBLEMA: só move uma vez por tecla pressionada
for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            x -= 2  # move só uma vez!
```

### Abordagem correta (flags)

```python
# Flags para cada direção
to_left = False
to_right = False
to_up = False
to_down = False

while True:
    # Passo 1: Atualiza flags baseado em eventos
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left = True
            if event.key == pygame.K_RIGHT:
                to_right = True
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False
    
    # Passo 2: Move baseado no estado das flags
    # (executado TODO frame, não só no evento)
    if to_left:
        x -= 2
    if to_right:
        x += 2
```

### Alternativa: pygame.key.get_pressed()

Pygame oferece uma forma mais direta:

```python
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    # Pega estado atual de TODAS as teclas
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        x -= 2
    if keys[pygame.K_RIGHT]:
        x += 2
    if keys[pygame.K_UP]:
        y -= 2
    if keys[pygame.K_DOWN]:
        y += 2
```

### Quando usar cada abordagem

| Flags manuais | get_pressed() |
|---------------|---------------|
| Mais controle | Mais simples |
| Pode detectar "acabou de pressionar" | Só detecta "está pressionado" |
| Bom para ações únicas + contínuas | Bom só para movimento contínuo |

---

## 4. Delta Time (Tempo Independente de FPS)

### O que é

Técnica para fazer o movimento **independente da taxa de frames**. Em vez de mover X pixels por frame, você move X pixels por segundo.

### Problema

Se você move `x += 2` por frame:
- A 60 FPS: move 120 pixels/segundo
- A 30 FPS: move 60 pixels/segundo
- Jogo fica inconsistente em máquinas diferentes

### Solução: multiplicar pelo delta time

```python
clock = pygame.time.Clock()
speed = 200  # pixels por SEGUNDO

while True:
    dt = clock.tick(60) / 1000  # delta time em segundos
    
    if to_right:
        x += speed * dt  # 200 * 0.016 ≈ 3.2 pixels (a 60fps)
```

### Exemplo completo

```python
import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

x = 100
speed = 200  # pixels por segundo

while True:
    # Delta time: tempo desde o último frame (em segundos)
    dt = clock.tick(60) / 1000
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    keys = pygame.key.get_pressed()
    
    # Movimento independente de FPS
    if keys[pygame.K_RIGHT]:
        x += speed * dt
    if keys[pygame.K_LEFT]:
        x -= speed * dt
    
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), (x, 200, 50, 50))
    pygame.display.flip()
```

### Por que isso importa

| Sem delta time | Com delta time |
|----------------|----------------|
| Velocidade varia com FPS | Velocidade constante |
| Jogo mais rápido em PCs melhores | Consistente em qualquer PC |
| Difícil balancear dificuldade | Comportamento previsível |

---

## 5. Separação de Responsabilidades no Game Loop

### O que é

Organizar o game loop em **fases distintas**, cada uma com uma responsabilidade clara.

### Estrutura recomendada

```python
while True:
    # ═══════════════════════════════════════════
    # FASE 1: INPUT (Entrada)
    # ═══════════════════════════════════════════
    # Processa eventos, atualiza flags
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        # ... outros eventos
    
    # ═══════════════════════════════════════════
    # FASE 2: UPDATE (Atualização)
    # ═══════════════════════════════════════════
    # Atualiza posições, física, lógica do jogo
    if to_right:
        x += speed * dt
    x = clamp(x, 0, width - player_w)
    
    # Verifica colisões
    # Atualiza pontuação
    # Recicla objetos (pooling)
    
    # ═══════════════════════════════════════════
    # FASE 3: RENDER (Desenho)
    # ═══════════════════════════════════════════
    # Limpa tela, desenha tudo, atualiza display
    screen.fill((0, 0, 0))
    screen.blit(player, (x, y))
    pygame.display.flip()
    
    # ═══════════════════════════════════════════
    # FASE 4: TIMING (Controle de tempo)
    # ═══════════════════════════════════════════
    clock.tick(60)
```

### Por que separar

1. **Legibilidade** — fácil encontrar onde está cada lógica
2. **Debugging** — problemas isolados em fases específicas
3. **Manutenção** — modificar uma fase não afeta outras
4. **Escalabilidade** — adicionar features fica organizado

---

## 6. Dicionário de Teclas Pressionadas

### O que é

Usar um **dicionário** para rastrear quais teclas estão pressionadas, em vez de criar uma variável booleana para cada tecla.

### Problema

Com muitas teclas (dois jogadores, por exemplo), você acaba com muitas flags:

```python
# 8 variáveis para 2 jogadores!
to_left1 = False
to_right1 = False
to_up1 = False
to_down1 = False
to_left2 = False
to_right2 = False
to_up2 = False
to_down2 = False
```

### Solução: um dicionário

```python
key_pressed = {}  # começa vazio

# No evento KEYDOWN: adiciona a tecla
if event.type == pygame.KEYDOWN:
    key_pressed[event.key] = True

# No evento KEYUP: remove a tecla
if event.type == pygame.KEYUP:
    del key_pressed[event.key]
```

### O que é `event.key`?

É um **número inteiro** que identifica qual tecla foi pressionada:

```python
pygame.K_LEFT  # = 276
pygame.K_RIGHT # = 275
pygame.K_UP    # = 273
pygame.K_DOWN  # = 274
pygame.K_a     # = 97
pygame.K_w     # = 119
pygame.K_s     # = 115
pygame.K_d     # = 100
```

### Como o dicionário evolui

```python
key_pressed = {}  # estado inicial

# Usuário pressiona seta esquerda (código 276)
key_pressed[276] = True
# Agora: {276: True}

# Usuário pressiona W (código 119) 
key_pressed[119] = True
# Agora: {276: True, 119: True}

# Usuário solta seta esquerda
del key_pressed[276]
# Agora: {119: True}

# Usuário solta W
del key_pressed[119]
# Agora: {}
```

### Como verificar se uma tecla está pressionada

```python
# Verifica se a CHAVE existe no dicionário
if pygame.K_LEFT in key_pressed:
    # seta esquerda está pressionada!
    x -= 2
```

### O valor `True` nem importa

O que importa é **se a chave existe**, não o valor:

```python
# Todas estas formas funcionam igual:
key_pressed[event.key] = True
key_pressed[event.key] = 1
key_pressed[event.key] = "qualquer coisa"

# Porque a verificação é:
if event.key in key_pressed:  # só checa se a CHAVE existe
```

### Fluxo visual

```
Tecla pressionada (KEYDOWN)
         │
         ▼
    event.key = 276 (código da tecla)
         │
         ▼
    key_pressed[276] = True
         │
         ▼
    Dicionário: {276: True}
         │
         ▼
    Verificação: "276 in key_pressed?" → SIM → move


Tecla solta (KEYUP)
         │
         ▼
    event.key = 276
         │
         ▼
    del key_pressed[276]
         │
         ▼
    Dicionário: {}
         │
         ▼
    Verificação: "276 in key_pressed?" → NÃO → não move
```

### Comparação

| Flags individuais | Dicionário |
|-------------------|------------|
| 1 variável por tecla | 1 estrutura para todas |
| `if to_left1:` | `if K_LEFT in key_pressed:` |
| Adicionar tecla = nova variável | Adicionar tecla = automático |
| Código cresce linearmente | Código permanece constante |

---

## 7. Data-Driven Design (Design Orientado a Dados)

### O que é

Em vez de escrever **código** para cada caso específico, você descreve os casos como **dados** e usa um loop genérico para processá-los.

### Problema

Dois jogadores, cada um com 4 direções = 8 combinações de tecla/movimento. Com código tradicional:

```python
# 16 ifs só para detectar eventos!
if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_LEFT:
        to_left1 = True
    if event.key == pygame.K_RIGHT:
        to_right1 = True
    if event.key == pygame.K_UP:
        to_up1 = True
    if event.key == pygame.K_DOWN:
        to_down1 = True
    if event.key == pygame.K_a:
        to_left2 = True
    # ... mais 3 ...

# Mais 8 ifs para movimento!
if to_left1:
    x1 -= 2
if to_right1:
    x1 += 2
# ... mais 6 ...
```

### Solução: descrever controles como dados

```python
# Posições como lista indexada
positions = [
    [0, 0],                                          # robô 0
    [width - robot_w, height - robot_h]              # robô 1
]

# Controles como DADOS, não código
# Cada tupla: (tecla, qual_robô, delta_x, delta_y)
controls = [
    (pygame.K_LEFT,  0, -2,  0),  # LEFT  → robô 0, x -= 2
    (pygame.K_RIGHT, 0,  2,  0),  # RIGHT → robô 0, x += 2
    (pygame.K_UP,    0,  0, -2),  # UP    → robô 0, y -= 2
    (pygame.K_DOWN,  0,  0,  2),  # DOWN  → robô 0, y += 2
    (pygame.K_a,     1, -2,  0),  # A     → robô 1, x -= 2
    (pygame.K_d,     1,  2,  0),  # D     → robô 1, x += 2
    (pygame.K_w,     1,  0, -2),  # W     → robô 1, y -= 2
    (pygame.K_s,     1,  0,  2),  # S     → robô 1, y += 2
]
```

### O loop genérico

```python
# Processa TODOS os controles com 4 linhas
for ctrl in controls:
    tecla, robo, dx, dy = ctrl  # desempacota a tupla
    if tecla in key_pressed:
        positions[robo][0] += dx
        positions[robo][1] += dy
```

Ou de forma mais compacta:

```python
for ctrl in controls:
    if ctrl[0] in key_pressed:
        positions[ctrl[1]][0] += ctrl[2]
        positions[ctrl[1]][1] += ctrl[3]
```

### Código completo

```python
import pygame

pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
robot = pygame.image.load("robot.png")
robot_w, robot_h = robot.get_width(), robot.get_height()
clock = pygame.time.Clock()

# DADOS: posições dos robôs
positions = [
    [0, height - robot_h],
    [width - robot_w, height - robot_h]
]

# DADOS: mapeamento de controles
# (tecla, robô, delta_x, delta_y)
controls = [
    (pygame.K_LEFT,  0, -2,  0),
    (pygame.K_RIGHT, 0,  2,  0),
    (pygame.K_UP,    0,  0, -2),
    (pygame.K_DOWN,  0,  0,  2),
    (pygame.K_a,     1, -2,  0),
    (pygame.K_d,     1,  2,  0),
    (pygame.K_w,     1,  0, -2),
    (pygame.K_s,     1,  0,  2),
]

key_pressed = {}

while True:
    # INPUT: eventos genéricos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            key_pressed[event.key] = True
        if event.type == pygame.KEYUP:
            del key_pressed[event.key]
    
    # UPDATE: loop genérico processa todos os controles
    for ctrl in controls:
        if ctrl[0] in key_pressed:
            positions[ctrl[1]][0] += ctrl[2]
            positions[ctrl[1]][1] += ctrl[3]
    
    # RENDER
    screen.fill((0, 0, 0))
    for pos in positions:
        screen.blit(robot, (pos[0], pos[1]))
    pygame.display.flip()
    clock.tick(60)
```

### Adicionar um terceiro jogador

Com código tradicional: duplicar ~30 linhas.

Com data-driven: adicionar 5 linhas de **dados**:

```python
# Adiciona posição inicial
positions.append([width // 2, height // 2])

# Adiciona controles (IJKL)
controls.append((pygame.K_j, 2, -2,  0))
controls.append((pygame.K_l, 2,  2,  0))
controls.append((pygame.K_i, 2,  0, -2))
controls.append((pygame.K_k, 2,  0,  2))
```

**O resto do código não muda!**

### Por que isso é poderoso

| Código tradicional | Data-driven |
|--------------------|-------------|
| Lógica duplicada | Lógica única |
| Mudança = editar código | Mudança = editar dados |
| Difícil de escalar | Escala facilmente |
| Propenso a erros | Menos lugares para errar |

### Outros usos de Data-Driven Design

```python
# Definir tipos de inimigos
enemies_config = [
    {"name": "slime", "hp": 10, "speed": 1, "damage": 5},
    {"name": "goblin", "hp": 25, "speed": 2, "damage": 10},
    {"name": "dragon", "hp": 100, "speed": 3, "damage": 50},
]

# Definir itens do jogo
items = [
    {"name": "poção", "effect": "heal", "value": 20},
    {"name": "espada", "effect": "damage", "value": 15},
]

# Definir níveis/fases
levels = [
    {"enemies": 5, "boss": False, "background": "forest.png"},
    {"enemies": 10, "boss": False, "background": "cave.png"},
    {"enemies": 3, "boss": True, "background": "castle.png"},
]
```

---

## Resumo Comparativo

| Técnica | Problema que resolve | Quando usar |
|---------|---------------------|-------------|
| **Clamping** | Limitar valores a um intervalo | Bordas de tela, vida, volume |
| **Object Pooling** | Performance com muitos objetos | Projéteis, partículas, inimigos |
| **Flag-Based Movement** | Movimento contínuo com teclado | Controle de personagem |
| **Delta Time** | Consistência entre máquinas | Qualquer movimento/animação |
| **Separação de fases** | Organização do código | Todo game loop |
| **Dicionário de teclas** | Muitas teclas para rastrear | Múltiplos jogadores, muitos controles |
| **Data-Driven Design** | Código repetitivo | Configurações, controles, entidades |

---

## Código Exemplo: Tudo Junto

```python
import pygame
from random import randint

def clamp(valor, minimo, maximo):
    return max(minimo, min(valor, maximo))

pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# Jogador
player_img = pygame.image.load("robot.png")
player_w, player_h = player_img.get_width(), player_img.get_height()
player_x = width // 2
player_y = height - player_h
player_speed = 300  # pixels por segundo

# Object Pool de inimigos
num_enemies = 10
enemies = []
for i in range(num_enemies):
    enemies.append([randint(0, width - 50), randint(-500, -50)])

while True:
    # ══════ TIMING ══════
    dt = clock.tick(60) / 1000
    
    # ══════ INPUT ══════
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    keys = pygame.key.get_pressed()
    
    # ══════ UPDATE ══════
    # Movimento do jogador (com delta time)
    if keys[pygame.K_LEFT]:
        player_x -= player_speed * dt
    if keys[pygame.K_RIGHT]:
        player_x += player_speed * dt
    
    # Clamping nas bordas
    player_x = clamp(player_x, 0, width - player_w)
    
    # Atualiza inimigos (com pooling)
    for enemy in enemies:
        enemy[1] += 100 * dt  # cai
        
        # Reciclagem
        if enemy[1] > height:
            enemy[0] = randint(0, width - 50)
            enemy[1] = randint(-500, -50)
    
    # ══════ RENDER ══════
    screen.fill((0, 0, 0))
    screen.blit(player_img, (player_x, player_y))
    
    for enemy in enemies:
        pygame.draw.rect(screen, (255, 0, 0), (enemy[0], enemy[1], 50, 50))
    
    pygame.display.flip()
```

---

**Fonte:** University of Helsinki MOOC - Python Programming (Part 13)  
**Documento criado por:** Claude (Anthropic)  
**Para:** Eric Alcalai França
