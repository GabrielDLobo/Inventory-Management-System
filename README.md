# 📦 Inventory Management System (SGE)

Sistema de Gestão de Estoque desenvolvido com **Django**, **Python** e **Bootstrap 5**, focado em facilitar o controle de entradas, saídas e organização de produtos em ambientes comerciais.

## 🚀 Funcionalidades

- ✅ Autenticação de usuários
- 📥 Registro de entradas e saídas de produtos
- 🗂️ Gerenciamento de categorias, marcas e fornecedores
- 📊 Visualização de histórico de movimentações
- 🛠️ Interface responsiva com Bootstrap 5

## 🧰 Tecnologias utilizadas

- Python 3.7+
- Django
- Bootstrap 5
- Docker
- PostgreSQL
- Amazon Web Services

## 🖥️ Como executar o projeto localmente

<strong>1. Clone o repositório:</strong>
git clone https://github.com/GabrielDLobo/Inventory-Management-System.git

<strong>2. Crie e ative o ambiente virtual:</strong>
python -m venv venv
venv\Scripts\activate

<strong>3. Instale as dependências</strong>
pip install -r requirements.txt

<strong>4. Aplique as migrações e crie o super usuário</strong>
python manage.py migrate
python manage.py createsuperuser

<strong>5. Execute o servidor</strong>
python manage.py runserver

Acesse o sistema em: http://localhost:8000/login


📚 Aprendizados
Durante o desenvolvimento, aprimorei habilidades em:
• 	Modelagem de dados com Django ORM
• 	Criação de interfaces responsivas
• 	Organização de código em apps modulares
• 	Uso de Docker para ambientes isolados
