# **SGHSS – Sistema de Gestão Hospitalar e de Serviços de Saúde (Back-end)**

Este repositório contém o módulo **Back-end** do projeto **SGHSS**, desenvolvido como requisito parcial da disciplina **Projeto de Diplomação / Projeto Multidisciplinar** do curso de **Análise e Desenvolvimento de Sistemas** da **UNINTER**.

**Aluno(a):** *Sthefanie Ferreira de Souza Dias Otaviano*  
**RU:** *4583758*

---

## 📋 **Sobre o Projeto**

O **SGHSS** é um sistema destinado à gestão centralizada de informações hospitalares.  
Este back-end foi desenvolvido utilizando **Django** e **Django Rest Framework**, com foco em segurança e conformidade com a **LGPD**.

### **Principais Funcionalidades**

- **Autenticação e Autorização:** login seguro e controle de perfis (Paciente, Profissional, Admin).  
- **Gestão de Pacientes:** CRUD completo para dados civis e clínicos.  
- **Gestão de Profissionais:** cadastro e validação de **CRM/COREN**.  
- **API REST:** endpoints padronizados em **JSON**.

---

## 🚀 **Tecnologias Utilizadas**

- **Linguagem:** Python 3.11+  
- **Framework:** Django 5.x  
- **API:** Django Rest Framework (DRF)  
- **Banco de Dados:** SQLite (ambiente de desenvolvimento)

---

## 📦 **Como Rodar o Projeto**

Siga os passos abaixo para executar o servidor da API localmente.

### **Pré-requisitos**

- Python 3 instalado  
- Git instalado

---

### **1. Clonar o repositório**

```bash
git clone https://github.com/Sthefanie-neuro/sghss-backend
cd sghss-backend
```

---

### **2. Criar e ativar o ambiente virtual**

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### **3. Instalar as dependências**

```bash
pip install -r requirements.txt
```

---

### **4. Configurar o banco de dados**

```bash
python manage.py migrate
```

---

### **5. Criar um superusuário (Admin)**

```bash
python manage.py createsuperuser
```

---

### **6. Iniciar o servidor**

```bash
python manage.py runserver
```

A API estará disponível em:  
👉 http://127.0.0.1:8000/

---

## 🔗 **Endpoints da API**

| Método | Endpoint             | Descrição                         | Acesso              |
|--------|----------------------|-----------------------------------|----------------------|
| POST   | `/api/usuarios/`      | Cadastro de usuário (sign-up)     | Público              |
| GET    | `/api/pacientes/`     | Listar pacientes                  | Requer Token/Login  |
| POST   | `/api/pacientes/`     | Cadastrar paciente                | Requer Token/Login  |
| GET    | `/api/profissionais/` | Listar profissionais              | Requer Token/Login  |
| GET    | `/admin/`             | Painel administrativo (Django)    | Apenas superusuário |

---

## 📝 **Licença**

Este projeto foi desenvolvido exclusivamente para fins **acadêmicos**.
