# 🚀 TaskFlow API

API backend do sistema TaskFlow, desenvolvida com Django REST Framework.  
Permite gerenciamento de tarefas com autenticação JWT.

---

## ⚙️ Tecnologias

- Python
- Django
- Django REST Framework
- SimpleJWT
- SQLite

---

## 🔐 Autenticação

A API utiliza JWT (JSON Web Token).

---

### 📌 Gerar token

```bash
curl -X POST http://127.0.0.1:8000/api/token/ \
-H "Content-Type: application/json" \
-d '{
  "username": "seu_usuario",
  "password": "sua_senha"
}'

```

---

### 📌 Resposta

```bash
{
  "access": "seu_token_access",
  "refresh": "seu_token_refresh"
}

```

---

### 🔑 Usando o token

```bash
curl -X GET http://127.0.0.1:8000/api/tasks/ \
-H "Authorization: Bearer SEU_TOKEN"

```
---

### 📌 Endpoints
📋 Listar tarefas
```bash
curl -X GET http://127.0.0.1:8000/api/tasks/ \
-H "Authorization: Bearer SEU_TOKEN"

```

---

### ➕ Criar tarefa

```bash
curl -X POST http://127.0.0.1:8000/api/tasks/ \
-H "Content-Type: application/json" \
-H "Authorization: Bearer SEU_TOKEN" \
-d '{
  "title": "Estudar Django",
  "description": "Aprender DRF",
  "completed": false
}'

```

---

### 📌 Buscar tarefa por ID

```bash
curl -X GET http://127.0.0.1:8000/api/tasks/1/ \
-H "Authorization: Bearer SEU_TOKEN"

```

---

### ✏️ Atualizar tarefa

```bash
curl -X PATCH http://127.0.0.1:8000/api/tasks/1/ \
-H "Content-Type: application/json" \
-H "Authorization: Bearer SEU_TOKEN" \
-d '{
  "title": "Título atualizado",
  "description": "Descrição atualizada",
  "completed": true
}'

```

---

### ❌ Deletar tarefa

```bash
curl -X DELETE http://127.0.0.1:8000/api/tasks/1/ \
-H "Authorization: Bearer SEU_TOKEN"

```

---

### ▶️ Como rodar o projeto

```bash
git clone https://github.com/SEU_USUARIO/taskflow-backend.git
cd taskflow-backend

python -m venv venv
source venv/bin/activate   # Linux/Mac
# venv\Scripts\activate    # Windows

pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser

python manage.py runserver

```

---

### 🌐 Acesso

```bash
http://127.0.0.1:8000/

```




