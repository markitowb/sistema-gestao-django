# 🗂️ Sistema de Gestão de Informações

Sistema web local desenvolvido em Python/Django para gestão
de pessoas, empresas, organizações, documentos e registros,
com geração de PDF classificado conforme a LAI e LGPD.

## 🚀 Tecnologias utilizadas

- Python 3.12
- Django 4.x
- SQLite
- Bootstrap 5
- ReportLab (geração de PDF)
- Select2

## ✨ Funcionalidades

- Autenticação com controle de acesso por grupos (Admin/Operador)
- CRUD completo de Pessoas, Empresas e Organizações
- CRUD de Fatos, Relatórios e Memórias com vínculos cruzados
- Upload e gestão de documentos (PDF, Word, Excel, imagens)
- Geração de PDF com cabeçalho, rodapé e classificação de sigilo
- Classificação baseada na LAI (Lei nº 12.527/2011) e LGPD (Lei nº 13.709/2018)
- Dashboard com totais e atividade recente
- Sistema 100% offline — sem dependência de internet

## 🔧 Como executar localmente

1. Clone o repositório
```bash
   git clone https://github.com/seu-usuario/sistema-gestao.git
   cd sistema-gestao
```

2. Crie e ative o ambiente virtual
```bash
   python -m venv venv
   venv\Scripts\activate
```

3. Instale as dependências
```bash
   pip install -r requirements.txt
```

4. Configure as variáveis de ambiente
```bash
   copy .env.example .env
   # Edite o .env com seus valores
```

5. Rode as migrações
```bash
   python manage.py migrate
```

6. Crie o superusuário
```bash
   python manage.py createsuperuser
```

7. Inicie o servidor
```bash
   python manage.py runserver
```

8. Acesse http://127.0.0.1:8000

## 📋 Requisitos

Veja o arquivo `requirements.txt`

## 👨‍💻 Autor

M@rkitoWB — [LinkedIn](https://www.linkedin.com/in/marcusviniciuswb/)
