# Desafio Django - Sistema de Produtos

Este projeto foi desenvolvido como parte de um desafio técnico utilizando **Django**.  
O sistema implementa autenticação de usuários (cadastro, login e logout) e gerenciamento de produtos.

---

## 🔧 Tecnologias utilizadas
- Python 3.x  
- Django 5.x  
- SQLite (banco de dados padrão do Django)  
- HTML (templates)  
- CSS básico (estático)  

---

## 🚀 Funcionalidades
- Cadastro de usuários (`/accounts/signup/`)  
- Login de usuários (`/accounts/login/`)  
- Logout seguro via POST (`/accounts/logout/`)  
- Listagem de produtos cadastrados  
- Integração básica de templates (`base.html`)  

---

## 📂 Estrutura do projeto
desafio/
├── manage.py
├── belzebells/           # Configurações do Django (settings, urls, wsgi)
├── produtos/             # App de produtos
├── templates/            # Templates HTML
│   ├── base.html
│   ├── registration/
│   │   ├── login.html
│   │   ├── logout.html
│   │   └── signup.html
└── static/               # Arquivos estáticos (CSS, imagens)
    └── css/
        └── style.css

⚙️ Como rodar o projeto localmente

1. Clone o repositório:
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio

2. Crie um ambiente virtual:
python -m venv venv

3. Ative o ambiente virtual:
   - Linux/Mac:
     source venv/bin/activate
   - Windows:
     venv\Scripts\activate
4. Instale as dependências:
   pip install -r requirements.txt

5. Execute as migrações do banco:
   python manage.py migrate

6. Crie um superusuário (para acessar o /admin):
   python manage.py createsuperuser

7. Rode o servidor:
   python manage.py runserver

🔑 Funcionalidades

Cadastro de usuários (/accounts/signup/)

Login (/accounts/login/)

Logout (/accounts/logout/)

Página inicial simples com navegação

App de produtos (estrutura criada)

📝 Observações

- O banco de dados (db.sqlite3) e a pasta __pycache__/ não são versionados (estão no .gitignore).
- O projeto já vem com páginas HTML básicas para login, logout e cadastro.
- CSS básico incluído em static/css/style.css.

👩‍💻 Autor
Desenvolvido por Bells Bonzanini ✨



