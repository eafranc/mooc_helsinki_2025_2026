# Guia Completo: Chamadas de API em Python

## Índice
1. [[# O que é uma API?]]
2. [[# Tipos de APIs]]
3. [[# Como Funcionam as Chamadas de API Web]]
4. [[# Estrutura de uma API REST]]
5. [[# Fazendo Chamadas de API em Python]]
6. [[# JSON - O Formato de Dados das APIs]]
7. [[# Exemplos Práticos Completos]]
8. [[# POST - Enviando Dados para a API]]
9. [[# Headers (Cabeçalhos)]]
10. [[# Autenticação - API Keys]]
11. [[# Boas Práticas]]
12. [[# APIs Públicas para Praticar]]
13. [[# Exemplo Final: Aplicação Completa]]

---

## O que é uma API?

**API** = Application Programming Interface (Interface de Programação de Aplicações)

É um jeito de **um programa conversar com outro programa** através da internet (ou localmente).

### Analogia do Restaurante:

Imagine um restaurante:
- **Você (cliente)** quer comida
- **Cozinha (servidor)** prepara a comida
- **Garçom (API)** é quem faz a comunicação entre você e a cozinha

Você não entra na cozinha, você fala com o garçom:
- Você: "Quero um hambúrguer" (requisição/request)
- Garçom vai na cozinha e traz: "Aqui está seu hambúrguer" (resposta/response)

### No Mundo da Programação:

```
Seu programa (cliente)
↓
Faz uma requisição para a API
↓
API processa no servidor
↓
API retorna dados
↓
Seu programa usa os dados
```

---

## Tipos de APIs

### 1. **APIs Web (REST)** - As mais comuns

Você faz requisições HTTP (como um navegador) e recebe dados (geralmente em JSON).

**Exemplos:**
- API do GitHub (informações sobre repositórios)
- API do Twitter (postar tweets)
- API de clima (temperatura atual)
- API de CEP (buscar endereço)

### 2. **APIs de Bibliotecas** - Código Python

```python
# Você já usa APIs sem saber!
import math

resultado = math.sqrt(16)  # você está usando a API do módulo math
```

Mas vamos focar nas **APIs Web**, que é o mais comum quando falamos de "chamadas de API".

---

## Como Funcionam as Chamadas de API Web

### Protocolo HTTP

APIs Web usam **HTTP** (HyperText Transfer Protocol) - o mesmo protocolo que navegadores usam.

### Métodos HTTP Principais:

| Método | O que faz | Analogia |
|--------|-----------|----------|
| **GET** | Buscar/ler dados | "Me mostre X" |
| **POST** | Criar novos dados | "Crie um novo X" |
| **PUT** | Atualizar dados completos | "Substitua X por Y" |
| **PATCH** | Atualizar dados parciais | "Mude só isso em X" |
| **DELETE** | Deletar dados | "Delete X" |

### Anatomia de uma Requisição HTTP:

```
GET https://api.exemplo.com/users/123
│   │                        │
│   │                        └─ Endpoint (caminho)
│   └─ URL base da API
└─ Método HTTP
```

---

## Estrutura de uma API REST

### URLs seguem um padrão:

```
https://api.github.com/users/octocat/repos
│      │              │     │       │
│      │              │     │       └─ Recurso específico
│      │              │     └─ ID/nome do usuário
│      │              └─ Tipo de recurso
│      └─ Domínio da API
└─ Protocolo
```

### Exemplos Reais:

```
GET https://api.github.com/users/torvalds
    → Busca informações do usuário "torvalds"

GET https://api.github.com/repos/python/cpython
    → Busca informações do repositório CPython

POST https://api.twitter.com/tweets
     → Cria um novo tweet

DELETE https://api.exemplo.com/posts/42
       → Deleta o post com ID 42
```

---

## Fazendo Chamadas de API em Python

### Biblioteca Principal: `requests`

```bash
# Instalar (se não tiver)
pip install requests
```

### Exemplo 1: GET Simples (Buscar Dados)

```python
import requests

# Fazer uma requisição GET
response = requests.get('https://api.github.com/users/torvalds')

# Ver o código de status
print(response.status_code)  # 200 = sucesso

# Ver os dados (JSON)
data = response.json()  # converte JSON para dicionário Python

print(data['name'])       # Linus Torvalds
print(data['location'])   # Portland, OR
print(data['followers'])  # número de seguidores
```

### Códigos de Status HTTP Comuns:

| Código | Significado |
|--------|-------------|
| **200** | OK - Sucesso |
| **201** | Created - Criado com sucesso |
| **400** | Bad Request - Requisição inválida |
| **401** | Unauthorized - Não autenticado |
| **403** | Forbidden - Sem permissão |
| **404** | Not Found - Não encontrado |
| **500** | Internal Server Error - Erro no servidor |

### Exemplo 2: Tratando Erros

```python
import requests

response = requests.get('https://api.github.com/users/usuarioqueNaoExiste123456')

if response.status_code == 200:
    data = response.json()
    print(f"Usuário: {data['name']}")
elif response.status_code == 404:
    print("Usuário não encontrado!")
else:
    print(f"Erro: {response.status_code}")
```

### Exemplo 3: API com Parâmetros (Query String)

```python
import requests

# Buscar repositórios Python no GitHub
url = 'https://api.github.com/search/repositories'
params = {
    'q': 'language:python',  # buscar por linguagem Python
    'sort': 'stars',         # ordenar por estrelas
    'order': 'desc'          # ordem decrescente
}

response = requests.get(url, params=params)
data = response.json()

# Mostrar os 5 primeiros resultados
for repo in data['items'][:5]:
    print(f"{repo['name']}: {repo['stargazers_count']} estrelas")
```

**URL final gerada:**
```
https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc
```

---

## JSON - O Formato de Dados das APIs

**JSON** = JavaScript Object Notation

É como um dicionário Python, mas em texto:

### JSON:
```json
{
  "name": "Eric Alcalai França",
  "age": 30,
  "skills": ["Python", "SAP", "ABAP"],
  "address": {
    "city": "Boituva",
    "state": "SP"
  }
}
```

### Python (após `response.json()`):
```python
{
  'name': 'Eric Alcalai França',
  'age': 30,
  'skills': ['Python', 'SAP', 'ABAP'],
  'address': {
    'city': 'Boituva',
    'state': 'SP'
  }
}
```

### Convertendo:

```python
import json

# JSON (string) → Python (dict)
json_string = '{"name": "Eric", "age": 30}'
python_dict = json.loads(json_string)

# Python (dict) → JSON (string)
python_dict = {'name': 'Eric', 'age': 30}
json_string = json.dumps(python_dict)
```

---

## Exemplos Práticos Completos

### Exemplo 1: API de CEP (ViaCEP)

```python
import requests

def buscar_endereco(cep: str):
    """
    Busca endereço pelo CEP usando a API ViaCEP
    """
    # Limpar formatação do CEP
    cep_limpo = cep.replace("-", "").replace(".", "")
    
    # URL da API
    url = f"https://viacep.com.br/ws/{cep_limpo}/json/"
    
    # Fazer requisição
    response = requests.get(url)
    
    # Verificar se deu certo
    if response.status_code == 200:
        dados = response.json()
        
        # Verificar se o CEP existe
        if 'erro' not in dados:
            return {
                'cep': dados['cep'],
                'logradouro': dados['logradouro'],
                'bairro': dados['bairro'],
                'cidade': dados['localidade'],
                'estado': dados['uf']
            }
        else:
            return None
    else:
        return None

# Usando
endereco = buscar_endereco("01310-100")

if endereco:
    print(f"CEP: {endereco['cep']}")
    print(f"Rua: {endereco['logradouro']}")
    print(f"Bairro: {endereco['bairro']}")
    print(f"Cidade: {endereco['cidade']}")
    print(f"Estado: {endereco['estado']}")
else:
    print("CEP não encontrado!")
```

**Output:**
```
CEP: 01310-100
Rua: Avenida Paulista
Bairro: Bela Vista
Cidade: São Paulo
Estado: SP
```

### Exemplo 2: Classe para API de Clima

```python
import requests
from typing import Optional

class WeatherAPI:
    """Cliente para API de clima"""
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5"
    
    def get_current_weather(self, city: str, units: str = 'metric') -> Optional[dict]:
        """
        Busca clima atual de uma cidade
        
        Args:
            city: Nome da cidade
            units: 'metric' (Celsius) ou 'imperial' (Fahrenheit)
        
        Returns:
            Dicionário com dados do clima ou None se erro
        """
        endpoint = f"{self.base_url}/weather"
        
        params = {
            'q': city,
            'appid': self.api_key,
            'units': units,
            'lang': 'pt_br'
        }
        
        try:
            response = requests.get(endpoint, params=params, timeout=10)
            
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 404:
                print(f"Cidade '{city}' não encontrada")
                return None
            else:
                print(f"Erro na API: {response.status_code}")
                return None
                
        except requests.exceptions.Timeout:
            print("Timeout: API demorou muito para responder")
            return None
        except requests.exceptions.RequestException as e:
            print(f"Erro na requisição: {e}")
            return None
    
    def format_weather_info(self, data: dict) -> str:
        """Formata dados do clima para exibição"""
        if not data:
            return "Sem dados disponíveis"
        
        city = data['name']
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description']
        
        return f"""
Clima em {city}:
  Temperatura: {temp}°C
  Sensação térmica: {feels_like}°C
  Umidade: {humidity}%
  Condição: {description.capitalize()}
        """.strip()

# Usando a classe
api = WeatherAPI(api_key='SUA_CHAVE_AQUI')

# Buscar clima
dados = api.get_current_weather('São Paulo')

if dados:
    print(api.format_weather_info(dados))
```

---

## POST - Enviando Dados para a API

```python
import requests

# Exemplo: criar um post em uma API fictícia
url = 'https://jsonplaceholder.typicode.com/posts'

# Dados a serem enviados
novo_post = {
    'title': 'Meu Primeiro Post',
    'body': 'Este é o conteúdo do post',
    'userId': 1
}

# Fazer requisição POST
response = requests.post(url, json=novo_post)

if response.status_code == 201:  # 201 = Created
    post_criado = response.json()
    print(f"Post criado com ID: {post_criado['id']}")
    print(post_criado)
else:
    print(f"Erro: {response.status_code}")
```

---

## Headers (Cabeçalhos)

APIs frequentemente exigem informações adicionais nos **headers**:

```python
import requests

url = 'https://api.exemplo.com/data'

# Headers comuns
headers = {
    'User-Agent': 'MeuApp/1.0',
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

response = requests.get(url, headers=headers)
```

---

## Autenticação - API Keys

Muitas APIs exigem uma **chave de API** (API Key) para autenticação:

### Exemplo 1: API Key no Header

```python
import requests

# SUA chave de API (geralmente você se registra no site da API)
API_KEY = 'sua_chave_secreta_aqui'

url = 'https://api.openweathermap.org/data/2.5/weather'

headers = {
    'Authorization': f'Bearer {API_KEY}'
}

params = {
    'q': 'São Paulo',
    'units': 'metric'
}

response = requests.get(url, headers=headers, params=params)
data = response.json()
```

### Exemplo 2: API Key como Parâmetro

```python
import requests

API_KEY = 'sua_chave_aqui'

url = 'https://api.openweathermap.org/data/2.5/weather'

params = {
    'q': 'São Paulo',
    'appid': API_KEY,  # API key como parâmetro
    'units': 'metric'
}

response = requests.get(url, params=params)
data = response.json()

if response.status_code == 200:
    print(f"Temperatura em São Paulo: {data['main']['temp']}°C")
```

---

## Boas Práticas

### 1. Sempre Tratar Erros

```python
import requests

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()  # Levanta exceção se status >= 400
    data = response.json()
except requests.exceptions.Timeout:
    print("Timeout!")
except requests.exceptions.HTTPError as e:
    print(f"Erro HTTP: {e}")
except requests.exceptions.RequestException as e:
    print(f"Erro: {e}")
```

### 2. Usar Timeout

```python
# Sempre defina timeout para evitar espera infinita
response = requests.get(url, timeout=10)  # 10 segundos
```

### 3. Não Expor API Keys no Código

```python
# ❌ NÃO faça isso:
API_KEY = 'minha_chave_secreta_123'

# ✅ Use variáveis de ambiente:
import os
API_KEY = os.getenv('WEATHER_API_KEY')
```

### 4. Respeitar Rate Limits

APIs geralmente limitam quantas requisições você pode fazer:

```python
import time

# Fazer múltiplas requisições com intervalo
for city in ['São Paulo', 'Rio de Janeiro', 'Brasília']:
    get_weather(city)
    time.sleep(1)  # espera 1 segundo entre requisições
```

### 5. Validar Dados Recebidos

```python
import requests

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    
    # Validar se campos esperados existem
    if 'name' in data and 'temperature' in data:
        print(f"{data['name']}: {data['temperature']}°C")
    else:
        print("Dados incompletos na resposta")
```

---

## Diferença: urllib vs requests

### urllib (biblioteca padrão do Python):

```python
import urllib.request
import json

url = 'https://api.github.com/users/torvalds'
with urllib.request.urlopen(url) as response:
    data = json.loads(response.read().decode())
    print(data['name'])
```

### requests (mais fácil e popular):

```python
import requests

response = requests.get('https://api.github.com/users/torvalds')
data = response.json()
print(data['name'])
```

**Recomendação:** Use `requests` - é muito mais simples e poderoso!

---

## APIs Públicas para Praticar

Aqui estão algumas APIs **gratuitas** e **sem autenticação** para você testar:

### 1. **ViaCEP** (Buscar endereço por CEP)
```python
import requests

cep = "01310100"
response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
print(response.json())
```

### 2. **JSONPlaceholder** (API fake para testes)
```python
import requests

# GET - buscar posts
response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
print(response.json())

# POST - criar post (fake)
novo_post = {'title': 'Teste', 'body': 'Conteúdo', 'userId': 1}
response = requests.post('https://jsonplaceholder.typicode.com/posts', json=novo_post)
print(response.json())
```

### 3. **GitHub API** (Informações públicas)
```python
import requests

user = 'torvalds'
response = requests.get(f'https://api.github.com/users/{user}')
data = response.json()
print(f"Nome: {data['name']}")
print(f"Repositórios públicos: {data['public_repos']}")
```

### 4. **IBGE API** (Dados do Brasil)
```python
import requests

# Buscar estados
response = requests.get('https://servicodados.ibge.gov.br/api/v1/localidades/estados')
estados = response.json()

for estado in estados[:5]:
    print(f"{estado['sigla']}: {estado['nome']}")
```

### 5. **Random User API** (Gerar usuários fictícios)
```python
import requests

response = requests.get('https://randomuser.me/api/')
user = response.json()['results'][0]

print(f"Nome: {user['name']['first']} {user['name']['last']}")
print(f"Email: {user['email']}")
print(f"Cidade: {user['location']['city']}")
```

### 6. **Dog CEO API** (Imagens aleatórias de cachorros)
```python
import requests

response = requests.get('https://dog.ceo/api/breeds/image/random')
data = response.json()
print(f"Imagem de cachorro: {data['message']}")
```

### 7. **Advice Slip API** (Conselhos aleatórios)
```python
import requests

response = requests.get('https://api.adviceslip.com/advice')
data = response.json()
print(f"Conselho: {data['slip']['advice']}")
```

---

## Exemplo Final: Aplicação Completa

```python
import requests
from datetime import datetime

class GitHubStats:
    """Busca estatísticas de um usuário do GitHub"""
    
    BASE_URL = "https://api.github.com"
    
    def __init__(self, username: str):
        self.username = username
    
    def get_user_info(self):
        """Busca informações básicas do usuário"""
        url = f"{self.BASE_URL}/users/{self.username}"
        response = requests.get(url)
        
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            raise ValueError(f"Usuário '{self.username}' não encontrado")
        else:
            raise Exception(f"Erro na API: {response.status_code}")
    
    def get_repositories(self):
        """Busca repositórios do usuário"""
        url = f"{self.BASE_URL}/users/{self.username}/repos"
        response = requests.get(url)
        
        if response.status_code == 200:
            return response.json()
        return []
    
    def generate_report(self):
        """Gera relatório completo"""
        try:
            user = self.get_user_info()
            repos = self.get_repositories()
            
            # Calcular estatísticas
            total_stars = sum(repo['stargazers_count'] for repo in repos)
            total_forks = sum(repo['forks_count'] for repo in repos)
            languages = set(repo['language'] for repo in repos if repo['language'])
            
            # Repositório mais popular
            most_popular = max(repos, key=lambda r: r['stargazers_count']) if repos else None
            
            # Gerar relatório
            report = f"""
╔════════════════════════════════════════════╗
║  RELATÓRIO GITHUB - {user['login'].upper().center(24)} ║
╚════════════════════════════════════════════╝

👤 Nome: {user.get('name', 'N/A')}
📍 Localização: {user.get('location', 'N/A')}
🏢 Empresa: {user.get('company', 'N/A')}
📝 Bio: {user.get('bio', 'N/A')}

📊 ESTATÍSTICAS:
  • Repositórios públicos: {user['public_repos']}
  • Seguidores: {user['followers']}
  • Seguindo: {user['following']}
  • Total de estrelas: {total_stars}
  • Total de forks: {total_forks}
  • Linguagens: {', '.join(sorted(languages)) if languages else 'N/A'}

🏆 REPOSITÓRIO MAIS POPULAR:
  • Nome: {most_popular['name'] if most_popular else 'N/A'}
  • Estrelas: {most_popular['stargazers_count'] if most_popular else 0}
  • Descrição: {most_popular.get('description', 'Sem descrição') if most_popular else 'N/A'}

🔗 Perfil: {user['html_url']}
            """.strip()
            
            return report
            
        except ValueError as e:
            return f"❌ Erro: {e}"
        except Exception as e:
            return f"❌ Erro inesperado: {e}"

# Usando
stats = GitHubStats('torvalds')
print(stats.generate_report())
```

**Exemplo de Output:**
```
╔════════════════════════════════════════════╗
║  RELATÓRIO GITHUB -       TORVALDS         ║
╚════════════════════════════════════════════╝

👤 Nome: Linus Torvalds
📍 Localização: Portland, OR
🏢 Empresa: Linux Foundation
📝 Bio: N/A

📊 ESTATÍSTICAS:
  • Repositórios públicos: 6
  • Seguidores: 200000
  • Seguindo: 0
  • Total de estrelas: 180000
  • Total de forks: 45000
  • Linguagens: C, Shell

🏆 REPOSITÓRIO MAIS POPULAR:
  • Nome: linux
  • Estrelas: 150000
  • Descrição: Linux kernel source tree

🔗 Perfil: https://github.com/torvalds
```

---

## Exemplo Prático: Consultor de CEPs

```python
import requests
from typing import Optional, List

class ConsultorCEP:
    """Classe para consultar CEPs brasileiros"""
    
    BASE_URL = "https://viacep.com.br/ws"
    
    def buscar_por_cep(self, cep: str) -> Optional[dict]:
        """
        Busca endereço pelo CEP
        
        Args:
            cep: CEP com ou sem formatação
            
        Returns:
            Dicionário com dados do endereço ou None
        """
        # Limpar CEP
        cep_limpo = self._limpar_cep(cep)
        
        # Validar
        if not self._validar_cep(cep_limpo):
            print("CEP inválido!")
            return None
        
        # Fazer requisição
        url = f"{self.BASE_URL}/{cep_limpo}/json/"
        
        try:
            response = requests.get(url, timeout=5)
            
            if response.status_code == 200:
                dados = response.json()
                
                if 'erro' not in dados:
                    return self._formatar_endereco(dados)
                else:
                    print("CEP não encontrado!")
                    return None
            else:
                print(f"Erro na API: {response.status_code}")
                return None
                
        except requests.exceptions.Timeout:
            print("Timeout na consulta")
            return None
        except Exception as e:
            print(f"Erro: {e}")
            return None
    
    def buscar_por_endereco(self, uf: str, cidade: str, logradouro: str) -> List[dict]:
        """
        Busca CEPs por endereço
        
        Args:
            uf: Sigla do estado (ex: SP)
            cidade: Nome da cidade
            logradouro: Nome da rua/avenida (mínimo 3 caracteres)
            
        Returns:
            Lista de endereços encontrados
        """
        if len(logradouro) < 3:
            print("Logradouro deve ter no mínimo 3 caracteres")
            return []
        
        url = f"{self.BASE_URL}/{uf}/{cidade}/{logradouro}/json/"
        
        try:
            response = requests.get(url, timeout=5)
            
            if response.status_code == 200:
                dados = response.json()
                
                if isinstance(dados, list) and len(dados) > 0:
                    return [self._formatar_endereco(end) for end in dados]
                else:
                    print("Nenhum endereço encontrado")
                    return []
            else:
                print(f"Erro na API: {response.status_code}")
                return []
                
        except Exception as e:
            print(f"Erro: {e}")
            return []
    
    def _limpar_cep(self, cep: str) -> str:
        """Remove caracteres não numéricos do CEP"""
        return ''.join(filter(str.isdigit, cep))
    
    def _validar_cep(self, cep: str) -> bool:
        """Valida se CEP tem 8 dígitos"""
        return len(cep) == 8 and cep.isdigit()
    
    def _formatar_endereco(self, dados: dict) -> dict:
        """Formata dados do endereço"""
        return {
            'cep': dados.get('cep', ''),
            'logradouro': dados.get('logradouro', ''),
            'complemento': dados.get('complemento', ''),
            'bairro': dados.get('bairro', ''),
            'cidade': dados.get('localidade', ''),
            'uf': dados.get('uf', ''),
            'ddd': dados.get('ddd', '')
        }
    
    def exibir_endereco(self, endereco: dict):
        """Exibe endereço formatado"""
        if endereco:
            print(f"\n{'='*50}")
            print(f"CEP: {endereco['cep']}")
            print(f"Logradouro: {endereco['logradouro']}")
            if endereco['complemento']:
                print(f"Complemento: {endereco['complemento']}")
            print(f"Bairro: {endereco['bairro']}")
            print(f"Cidade: {endereco['cidade']} - {endereco['uf']}")
            print(f"DDD: {endereco['ddd']}")
            print(f"{'='*50}\n")

# Exemplo de uso
consultor = ConsultorCEP()

# Buscar por CEP
print("=== BUSCA POR CEP ===")
endereco = consultor.buscar_por_cep("01310-100")
if endereco:
    consultor.exibir_endereco(endereco)

# Buscar por endereço
print("\n=== BUSCA POR ENDEREÇO ===")
enderecos = consultor.buscar_por_endereco("SP", "São Paulo", "Paulista")
for end in enderecos[:3]:  # Mostra apenas os 3 primeiros
    consultor.exibir_endereco(end)
```

---

## Resumo dos Conceitos Principais

| Conceito | Descrição |
|----------|-----------|
| **API** | Jeito de programas conversarem |
| **HTTP** | Protocolo usado (GET, POST, PUT, DELETE) |
| **Endpoint** | URL específica da API |
| **JSON** | Formato de dados (como dicionário Python) |
| **Status Code** | Indica se deu certo (200) ou erro (404, 500, etc) |
| **Headers** | Informações extras (autenticação, tipo de conteúdo) |
| **Query Parameters** | Filtros/opções na URL (?q=python&sort=stars) |
| **Authentication** | API Key, tokens para identificar quem está chamando |
| **requests** | Biblioteca Python mais popular para APIs |

---

## Métodos HTTP - Referência Rápida

```python
import requests

# GET - Buscar dados
response = requests.get(url)

# POST - Criar novo recurso
response = requests.post(url, json=dados)

# PUT - Atualizar recurso completo
response = requests.put(url, json=dados)

# PATCH - Atualizar recurso parcialmente
response = requests.patch(url, json=dados)

# DELETE - Deletar recurso
response = requests.delete(url)
```

---

## Checklist de Boas Práticas

- ✅ Sempre use `timeout` nas requisições
- ✅ Trate exceções (Timeout, HTTPError, etc)
- ✅ Valide dados recebidos antes de usar
- ✅ Não exponha API keys no código (use variáveis de ambiente)
- ✅ Respeite rate limits da API
- ✅ Use HTTPS (não HTTP) para segurança
- ✅ Log de erros para debugging
- ✅ Cache de resultados quando apropriado
- ✅ Documente as APIs que você usa
- ✅ Teste com dados diversos (incluindo casos de erro)

---

## Próximos Passos para Estudar

1. **Pratique com APIs públicas gratuitas**
   - ViaCEP, GitHub, JSONPlaceholder, IBGE

2. **Aprenda sobre autenticação OAuth**
   - Twitter, Google, Facebook APIs

3. **Estude sobre GraphQL**
   - Alternativa moderna ao REST

4. **Aprenda a criar suas próprias APIs**
   - Flask, FastAPI, Django REST Framework

5. **Entenda sobre rate limiting e caching**
   - Como otimizar uso de APIs

6. **Websockets e APIs em tempo real**
   - Para dados que atualizam constantemente

7. **Testes de APIs**
   - pytest, unittest, mocking

---

## Recursos Adicionais

### Documentação Oficial:
- **requests**: https://requests.readthedocs.io/
- **JSON**: https://www.json.org/

### APIs para Praticar:
- **Public APIs**: https://github.com/public-apis/public-apis
- **JSONPlaceholder**: https://jsonplaceholder.typicode.com/
- **ViaCEP**: https://viacep.com.br/
- **IBGE**: https://servicodados.ibge.gov.br/api/docs

### Ferramentas Úteis:
- **Postman**: Testar APIs manualmente
- **HTTPie**: Cliente HTTP para linha de comando
- **curl**: Ferramenta clássica para requisições HTTP

---

**Criado por:** Claude (Anthropic)  
**Baseado em:** Conversa com Eric Alcalai França  
**Data:** Dezembro 2024  
**Contexto:** Estudo de Python - Chamadas de API
