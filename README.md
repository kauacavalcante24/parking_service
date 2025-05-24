# Projeto Parking Service
API de Estacionamento com Python e Django

## Requisitos do Sistema

### Funcionais

- Sistema de administração interno
    - Controle de usuários, acessos e permissões
    - Cadastros:
        - Clientes
        - Veículos
        - Vagas
        - Entradas e saídas de veículos
    - Status de vagas automático (ocupado / livre)
    - Autenticação
    - Filtros
    - Possibilidade de acesso dos clientes
        - Ver apenas seus veículos e registros

### Não funcionais

- Dashboard do Jazzmin
- API Restfull
- Linter e pep08 (flake8)
- JWT token para API
- RQL para filtros
- Documentação da API (swagger)

## Como rodar o Parking Service?

- Clone este repositório em sua máquina
  
- Acesse o terminal estando no caminho do projeto e crie o seu Ambiente Virtual:
    <pre> python -m venv venv </pre>
      
- Após criar a venv, ative ela:
  > Windows (cmd):
  <pre> venv\Scripts\activate </pre>

  > Windows (PowerShell):
  <pre> .\venv\Scripts\activate  </pre>
  
  > Linux/macOS:
  <pre> source venv/bin/activate  </pre>

- Com a venv ativada, você poderá instalar todos os pacotes necessários para o projeto rodar:
    <pre> pip install -r requirements.txt </pre>
   
- Suba as tabelas no banco de dados:
    <pre> python manage.py makemigrations </pre>
    <pre> python manage.py migrate </pre>

- Crie um super usuário para acessar o Sistema de Administração:
    <pre> python manage.py createsuperuser </pre>

- Após isso, ligue o servidor:
    <pre> python manage.py runserver </pre>

## Documentação Completa da API

Está disponível na rota:
http://127.0.0.1:8000/api/v1/docs/
