# Parte 13 - Pygame e Desenvolvimento de Jogos

> **Fonte:** University of Helsinki - Python Programming MOOC
> **Resumo criado por:** Claude (Anthropic)
> **Para:** Eric Alcalai França

---

## Índice

- [[#Seção 1 - Introdução ao Pygame]]
- [[#Seção 2 - Animação]]
- [[#Seção 3 - Eventos]]
- [[#Seção 4 - Mais Técnicas Pygame]]
- [[#Conceitos-Chave]]
- [[#Resumo Rápido]]

---

## Seção 1 - Introdução ao Pygame

### O Que É Pygame?

Biblioteca Python para desenvolvimento de jogos:
- Elementos gráficos
- Eventos de teclado e mouse
- Animações e sprites
- Som e música

### Instalação

```bash
# Linux
pip3 install pygame

# Windows (CMD como admin se necessário)
pip3 install pygame

# Mac (Terminal)
pip3 install pygame
```

### Primeiro Programa: Janela Básica

```python
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

window.fill((0, 0, 0))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
```

### Anatomia do Programa

| Comando | Função |
|---------|--------|
| `pygame.init()` | Inicializa os módulos pygame |
| `pygame.display.set_mode((w, h))` | Cria janela com dimensões |
| `window.fill((r, g, b))` | Preenche com cor RGB |
| `pygame.display.flip()` | Atualiza o conteúdo da janela |
| `pygame.event.get()` | Obtém lista de eventos |
| `pygame.QUIT` | Evento de fechar janela |

### Sistema de Coordenadas

```
(0,0) ─────────────────────► X (640)
  │
  │   Origem no canto
  │   superior esquerdo
  │
  │   Y aumenta para BAIXO
  │   (diferente da matemática!)
  │
  ▼
  Y (480)
```

### Carregando e Exibindo Imagens

```python
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

# Carrega imagem do arquivo
robot = pygame.image.load("robot.png")

window.fill((0, 0, 0))
# Desenha imagem na posição (100, 50)
window.blit(robot, (100, 50))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
```

> ⚠️ O arquivo de imagem deve estar no mesmo diretório do código!

### Múltiplas Imagens

```python
# Mesma imagem em diferentes posições
window.blit(robot, (0, 0))
window.blit(robot, (300, 0))
window.blit(robot, (100, 200))
```

### Centralizando Imagem

```python
# Obtém dimensões da imagem
width = robot.get_width()
height = robot.get_height()

# Centro da janela = (320, 240)
# Ajusta para o centro da IMAGEM ficar no centro da janela
window.blit(robot, (320 - width/2, 240 - height/2))
```

### Cores RGB

| Cor | RGB |
|-----|-----|
| Preto | `(0, 0, 0)` |
| Branco | `(255, 255, 255)` |
| Vermelho | `(255, 0, 0)` |
| Verde | `(0, 255, 0)` |
| Azul | `(0, 0, 255)` |
| Amarelo | `(255, 255, 0)` |
| Ciano | `(0, 255, 255)` |
| Magenta | `(255, 0, 255)` |

---

## Seção 2 - Animação

### Princípio da Animação

Ilusão de movimento = desenhar a mesma imagem em posições diferentes, com timing adequado.

### Animação Básica: Movimento Horizontal

```python
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

x = 0
y = 0
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # Limpa a tela
    window.fill((0, 0, 0))
    # Desenha na posição atual
    window.blit(robot, (x, y))
    # Atualiza display
    pygame.display.flip()

    # Move para a direita
    x += 1
    # Controla velocidade: 60 FPS
    clock.tick(60)
```

### O Clock (Relógio)

```python
clock = pygame.time.Clock()

# No final do loop:
clock.tick(60)  # 60 frames por segundo
```

| FPS | Significado |
|-----|-------------|
| 60 | Loop executa 60x por segundo |
| 30 | Loop executa 30x por segundo |

> O clock garante mesma velocidade em computadores diferentes!

### Bouncing (Rebatendo nas Paredes)

```python
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

x = 0
y = 0
velocity = 1  # direção: positivo = direita, negativo = esquerda
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()
    
    x += velocity
    
    # Bateu na parede direita?
    if velocity > 0 and x + robot.get_width() >= 640:
        velocity = -velocity  # inverte direção
    
    # Bateu na parede esquerda?
    if velocity < 0 and x <= 0:
        velocity = -velocity  # inverte direção

    clock.tick(60)
```

### Rotação em Círculo (Trigonometria)

```python
import pygame
import math

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

angle = 0  # ângulo em radianos
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # Calcula posição usando seno e cosseno
    # Centro da janela: (320, 240)
    # Raio do círculo: 100 pixels
    x = 320 + math.cos(angle) * 100 - robot.get_width() / 2
    y = 240 + math.sin(angle) * 100 - robot.get_height() / 2

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()

    angle += 0.01  # incrementa ângulo
    clock.tick(60)
```

### Fórmulas de Movimento Circular

```
x = centro_x + cos(ângulo) * raio
y = centro_y + sin(ângulo) * raio
```

- **Círculo completo:** 2π radianos ≈ 6.28
- **Incremento 0.01:** ~628 iterações para volta completa
- **A 60 FPS:** ~10 segundos por volta

---

## Seção 3 - Eventos

### Tipos de Eventos

| Evento | Descrição |
|--------|-----------|
| `pygame.QUIT` | Fechar janela |
| `pygame.KEYDOWN` | Tecla pressionada |
| `pygame.KEYUP` | Tecla solta |
| `pygame.MOUSEBUTTONDOWN` | Botão do mouse pressionado |
| `pygame.MOUSEBUTTONUP` | Botão do mouse solto |
| `pygame.MOUSEMOTION` | Mouse movido |

### Debug: Imprimindo Todos os Eventos

```python
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

while True:
    for event in pygame.event.get():
        print(event)  # mostra todos os eventos
        if event.type == pygame.QUIT:
            exit()
```

### Eventos de Teclado

```python
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("esquerda")
            if event.key == pygame.K_RIGHT:
                print("direita")
            if event.key == pygame.K_UP:
                print("cima")
            if event.key == pygame.K_DOWN:
                print("baixo")

        if event.type == pygame.QUIT:
            exit()
```

### Constantes de Teclas Comuns

| Constante | Tecla |
|-----------|-------|
| `pygame.K_LEFT` | Seta esquerda |
| `pygame.K_RIGHT` | Seta direita |
| `pygame.K_UP` | Seta cima |
| `pygame.K_DOWN` | Seta baixo |
| `pygame.K_SPACE` | Espaço |
| `pygame.K_RETURN` | Enter |
| `pygame.K_a` ... `pygame.K_z` | Letras |
| `pygame.K_0` ... `pygame.K_9` | Números |

### Movendo Sprite com Teclado (Básico)

```python
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
x = 0
y = 480 - robot.get_height()  # posiciona no chão

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= 10  # move 10 pixels
            if event.key == pygame.K_RIGHT:
                x += 10

        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()
```

### Movimento Contínuo (Enquanto Tecla Pressionada)

```python
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
x = 0
y = 480 - robot.get_height()

# Flags de direção
to_right = False
to_left = False

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        # Tecla pressionada
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left = True
            if event.key == pygame.K_RIGHT:
                to_right = True

        # Tecla solta
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False

        if event.type == pygame.QUIT:
            exit()

    # Movimento contínuo baseado nas flags
    if to_right:
        x += 2
    if to_left:
        x -= 2

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()

    clock.tick(60)
```

### Eventos de Mouse

```python
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(f"Botão {event.button} em {event.pos}")

        if event.type == pygame.QUIT:
            exit()
```

| event.button | Botão |
|--------------|-------|
| 1 | Esquerdo |
| 2 | Meio (scroll) |
| 3 | Direito |

### Desenhando Onde Clica

```python
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Centraliza imagem no clique
            x = event.pos[0] - robot.get_width() / 2
            y = event.pos[1] - robot.get_height() / 2

            window.fill((0, 0, 0))
            window.blit(robot, (x, y))
            pygame.display.flip()

        if event.type == pygame.QUIT:
            exit()
```

### Seguindo o Mouse

```python
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

robot_x = 0
robot_y = 0
target_x = 0
target_y = 0

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            # Atualiza alvo quando mouse move
            target_x = event.pos[0] - robot.get_width() / 2
            target_y = event.pos[1] - robot.get_height() / 2

        if event.type == pygame.QUIT:
            exit()

    # Move gradualmente em direção ao alvo
    if robot_x > target_x:
        robot_x -= 1
    if robot_x < target_x:
        robot_x += 1
    if robot_y > target_y:
        robot_y -= 1
    if robot_y < target_y:
        robot_y += 1

    window.fill((0, 0, 0))
    window.blit(robot, (robot_x, robot_y))
    pygame.display.flip()

    clock.tick(60)
```

---

## Seção 4 - Mais Técnicas Pygame

### Definindo Título da Janela

```python
pygame.display.set_caption("Grande Aventura")
```

### Desenhando Formas Geométricas

```python
import pygame

pygame.init()
display = pygame.display.set_mode((640, 480))
display.fill((0, 0, 0))

# Retângulo: (superfície, cor, (x, y, largura, altura))
pygame.draw.rect(display, (0, 255, 0), (50, 100, 200, 250))

# Círculo: (superfície, cor, (centro_x, centro_y), raio)
pygame.draw.circle(display, (255, 0, 0), (200, 150), 40)

# Linha: (superfície, cor, (x1, y1), (x2, y2), espessura)
pygame.draw.line(display, (0, 0, 255), (80, 120), (300, 160), 2)

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
```

### Funções de Desenho

| Função | Parâmetros | Descrição |
|--------|------------|-----------|
| `pygame.draw.rect` | surface, color, (x, y, w, h) | Retângulo |
| `pygame.draw.circle` | surface, color, (cx, cy), radius | Círculo |
| `pygame.draw.line` | surface, color, (x1, y1), (x2, y2), width | Linha |
| `pygame.draw.ellipse` | surface, color, (x, y, w, h) | Elipse |
| `pygame.draw.polygon` | surface, color, [(x1,y1), (x2,y2), ...] | Polígono |

### Desenhando Texto

```python
import pygame

pygame.init()
display = pygame.display.set_mode((640, 480))
display.fill((0, 0, 0))

# 1. Criar objeto de fonte
game_font = pygame.font.SysFont("Arial", 24)

# 2. Renderizar texto como imagem
#    render(texto, anti-aliasing, cor)
text = game_font.render("Olá Mundo!", True, (255, 0, 0))

# 3. Desenhar imagem do texto
display.blit(text, (100, 50))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
```

### Fontes

```python
# Fonte do sistema
game_font = pygame.font.SysFont("Arial", 24)

# Fonte personalizada (arquivo .ttf)
game_font = pygame.font.Font("minha_fonte.ttf", 24)

# Parâmetros do render
text = game_font.render(
    "Texto",       # string
    True,          # anti-aliasing (suavização)
    (255, 0, 0)    # cor RGB
)
```

### Exibindo Pontuação

```python
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))
font = pygame.font.SysFont("Arial", 24)

score = 0
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                score += 1
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    
    # Renderiza e desenha pontuação
    score_text = font.render(f"Pontos: {score}", True, (255, 255, 255))
    window.blit(score_text, (10, 10))
    
    pygame.display.flip()
    clock.tick(60)
```

---

## Conceitos-Chave

### Estrutura Básica de um Jogo Pygame

```python
import pygame

# 1. INICIALIZAÇÃO
pygame.init()
window = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Meu Jogo")
clock = pygame.time.Clock()

# 2. CARREGAR RECURSOS
imagem = pygame.image.load("sprite.png")
fonte = pygame.font.SysFont("Arial", 24)

# 3. VARIÁVEIS DE ESTADO
x, y = 0, 0
running = True

# 4. GAME LOOP
while running:
    # 4a. PROCESSAR EVENTOS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # outros eventos...
    
    # 4b. ATUALIZAR ESTADO
    # lógica do jogo...
    
    # 4c. RENDERIZAR
    window.fill((0, 0, 0))
    window.blit(imagem, (x, y))
    pygame.display.flip()
    
    # 4d. CONTROLAR FPS
    clock.tick(60)

pygame.quit()
```

### Tabela de Funções Principais

| Função | Descrição |
|--------|-----------|
| `pygame.init()` | Inicializa pygame |
| `pygame.display.set_mode((w, h))` | Cria janela |
| `pygame.display.set_caption(title)` | Define título |
| `pygame.display.flip()` | Atualiza tela |
| `pygame.image.load(path)` | Carrega imagem |
| `surface.blit(image, (x, y))` | Desenha imagem |
| `surface.fill((r, g, b))` | Preenche com cor |
| `pygame.event.get()` | Obtém eventos |
| `pygame.time.Clock()` | Cria relógio |
| `clock.tick(fps)` | Controla velocidade |

### Eventos Comuns

| Tipo | Atributos |
|------|-----------|
| `QUIT` | - |
| `KEYDOWN` | `key`, `unicode`, `mod` |
| `KEYUP` | `key`, `mod` |
| `MOUSEBUTTONDOWN` | `pos`, `button` |
| `MOUSEBUTTONUP` | `pos`, `button` |
| `MOUSEMOTION` | `pos`, `rel`, `buttons` |

---

## Resumo Rápido

### Programa Exemplo: Jogo Simples de Coleta

```python
# =============================================================
# JOGO DE COLETA - Demonstração Parte 13
# =============================================================

import pygame
import random
import math

# ----- INICIALIZAÇÃO -----
pygame.init()
WIDTH, HEIGHT = 640, 480
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Coletor de Estrelas")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 24)
big_font = pygame.font.SysFont("Arial", 48)

# ----- CORES -----
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 100, 255)

# ----- CLASSES -----
class Player:
    def __init__(self):
        self.width = 40
        self.height = 40
        self.x = WIDTH // 2 - self.width // 2
        self.y = HEIGHT - self.height - 10
        self.speed = 5
        self.color = BLUE
    
    def move(self, direction):
        if direction == "left" and self.x > 0:
            self.x -= self.speed
        if direction == "right" and self.x < WIDTH - self.width:
            self.x += self.speed
    
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, 
                        (self.x, self.y, self.width, self.height))
    
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)


class Star:
    def __init__(self):
        self.radius = 15
        self.x = random.randint(self.radius, WIDTH - self.radius)
        self.y = -self.radius
        self.speed = random.randint(2, 5)
        self.color = YELLOW
    
    def update(self):
        self.y += self.speed
    
    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)
    
    def is_off_screen(self):
        return self.y > HEIGHT + self.radius
    
    def collides_with(self, player):
        # Colisão simples: círculo vs retângulo
        player_rect = player.get_rect()
        closest_x = max(player_rect.left, min(self.x, player_rect.right))
        closest_y = max(player_rect.top, min(self.y, player_rect.bottom))
        distance = math.sqrt((self.x - closest_x)**2 + (self.y - closest_y)**2)
        return distance < self.radius


class Obstacle:
    def __init__(self):
        self.width = 30
        self.height = 30
        self.x = random.randint(0, WIDTH - self.width)
        self.y = -self.height
        self.speed = random.randint(3, 6)
        self.color = RED
    
    def update(self):
        self.y += self.speed
    
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, 
                        (self.x, self.y, self.width, self.height))
    
    def is_off_screen(self):
        return self.y > HEIGHT
    
    def collides_with(self, player):
        return player.get_rect().colliderect(
            pygame.Rect(self.x, self.y, self.width, self.height)
        )


# ----- FUNÇÕES DE JOGO -----
def draw_text(surface, text, font, color, x, y, center=False):
    text_surface = font.render(text, True, color)
    if center:
        rect = text_surface.get_rect(center=(x, y))
        surface.blit(text_surface, rect)
    else:
        surface.blit(text_surface, (x, y))


def show_game_over(surface, score):
    surface.fill(BLACK)
    draw_text(surface, "GAME OVER", big_font, RED, WIDTH//2, HEIGHT//2 - 50, True)
    draw_text(surface, f"Pontuação: {score}", font, WHITE, WIDTH//2, HEIGHT//2 + 20, True)
    draw_text(surface, "Pressione ESPAÇO para jogar novamente", font, WHITE, 
              WIDTH//2, HEIGHT//2 + 60, True)
    pygame.display.flip()


def main():
    # Estado do jogo
    player = Player()
    stars = []
    obstacles = []
    score = 0
    lives = 3
    star_timer = 0
    obstacle_timer = 0
    game_over = False
    
    # Flags de movimento
    moving_left = False
    moving_right = False
    
    running = True
    while running:
        # ----- EVENTOS -----
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    moving_left = True
                if event.key == pygame.K_RIGHT:
                    moving_right = True
                if event.key == pygame.K_SPACE and game_over:
                    # Reiniciar jogo
                    player = Player()
                    stars = []
                    obstacles = []
                    score = 0
                    lives = 3
                    game_over = False
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    moving_left = False
                if event.key == pygame.K_RIGHT:
                    moving_right = False
        
        if game_over:
            show_game_over(window, score)
            clock.tick(60)
            continue
        
        # ----- ATUALIZAÇÃO -----
        
        # Movimento do jogador
        if moving_left:
            player.move("left")
        if moving_right:
            player.move("right")
        
        # Spawn de estrelas
        star_timer += 1
        if star_timer >= 60:  # A cada 1 segundo
            stars.append(Star())
            star_timer = 0
        
        # Spawn de obstáculos
        obstacle_timer += 1
        if obstacle_timer >= 90:  # A cada 1.5 segundos
            obstacles.append(Obstacle())
            obstacle_timer = 0
        
        # Atualizar estrelas
        for star in stars[:]:
            star.update()
            if star.collides_with(player):
                score += 10
                stars.remove(star)
            elif star.is_off_screen():
                stars.remove(star)
        
        # Atualizar obstáculos
        for obstacle in obstacles[:]:
            obstacle.update()
            if obstacle.collides_with(player):
                lives -= 1
                obstacles.remove(obstacle)
                if lives <= 0:
                    game_over = True
            elif obstacle.is_off_screen():
                obstacles.remove(obstacle)
        
        # ----- RENDERIZAÇÃO -----
        window.fill(BLACK)
        
        # Desenhar objetos
        player.draw(window)
        for star in stars:
            star.draw(window)
        for obstacle in obstacles:
            obstacle.draw(window)
        
        # HUD
        draw_text(window, f"Pontos: {score}", font, WHITE, 10, 10)
        draw_text(window, f"Vidas: {lives}", font, WHITE, 10, 40)
        
        # Desenhar vidas como corações
        for i in range(lives):
            pygame.draw.circle(window, RED, (WIDTH - 30 - i * 30, 25), 10)
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()


# ----- EXECUÇÃO -----
if __name__ == "__main__":
    main()
```

---

### Checklist de Conceitos

- [ ] Instalar pygame (`pip3 install pygame`)
- [ ] Criar janela com `pygame.display.set_mode()`
- [ ] Definir título com `pygame.display.set_caption()`
- [ ] Carregar imagem com `pygame.image.load()`
- [ ] Desenhar imagem com `surface.blit()`
- [ ] Preencher fundo com `surface.fill()`
- [ ] Atualizar tela com `pygame.display.flip()`
- [ ] Processar eventos com `pygame.event.get()`
- [ ] Controlar FPS com `clock.tick()`
- [ ] Detectar teclas com `KEYDOWN` e `KEYUP`
- [ ] Detectar mouse com `MOUSEBUTTONDOWN` e `MOUSEMOTION`
- [ ] Desenhar formas com `pygame.draw.*`
- [ ] Renderizar texto com `font.render()`
- [ ] Implementar movimento contínuo com flags

---

### Armadilhas Comuns

| Armadilha | Problema | Solução |
|-----------|----------|---------|
| Imagem não encontrada | Arquivo não está no diretório | Colocar no mesmo diretório do .py |
| Movimento "travado" | Usa apenas KEYDOWN | Usar KEYDOWN + KEYUP com flags |
| Velocidade inconsistente | Não usa clock | Sempre usar `clock.tick(fps)` |
| Tela não atualiza | Esqueceu `flip()` | Chamar `pygame.display.flip()` |
| Coordenadas invertidas | Y cresce para baixo | Lembrar que origem é canto superior esquerdo |
| Janela congela | Não processa QUIT | Sempre verificar `pygame.QUIT` |

---

### Padrões de Design

```python
# 1. ESTRUTURA BÁSICA
import pygame
pygame.init()
window = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    # atualização
    # renderização
    pygame.display.flip()
    clock.tick(60)

# 2. MOVIMENTO COM FLAGS
moving_left = False
moving_right = False

# No loop de eventos:
if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_LEFT:
        moving_left = True
if event.type == pygame.KEYUP:
    if event.key == pygame.K_LEFT:
        moving_left = False

# Na atualização:
if moving_left:
    x -= speed

# 3. BOUNCING
if x + width >= screen_width or x <= 0:
    velocity_x = -velocity_x

# 4. MOVIMENTO CIRCULAR
x = center_x + math.cos(angle) * radius
y = center_y + math.sin(angle) * radius
angle += 0.01

# 5. COLISÃO RETÂNGULO-RETÂNGULO
rect1 = pygame.Rect(x1, y1, w1, h1)
rect2 = pygame.Rect(x2, y2, w2, h2)
if rect1.colliderect(rect2):
    # colisão!

# 6. RENDERIZAR TEXTO
font = pygame.font.SysFont("Arial", 24)
text = font.render(f"Score: {score}", True, (255, 255, 255))
window.blit(text, (10, 10))
```

---

## Próximos Passos

A **Parte 14** é um projeto final onde você aplicará todos os conceitos aprendidos para criar um jogo completo!

---

**Fonte:** University of Helsinki MOOC - Python Programming  
**Resumo criado por:** Claude (Anthropic)  
**Para:** Eric Alcalai França
