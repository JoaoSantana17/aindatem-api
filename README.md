# Ainda Tem? – API

API desenvolvida com **Flask** para gerenciar recursos essenciais em situações de emergência, permitindo que cidadãos e órgãos oficiais cadastrem e localizem pontos de ajuda próximos.

> **URL Base:** https://aindatem-api.vercel.app

---

##  Usuário

### `POST /usuario`
Cadastra um novo usuário.

**Body (JSON):**
```json
{
  "email": "exemplo@email.com",
  "senha": "1234"
}
```

---

### `POST /usuario/login`
Realiza login do usuário.

**Body (JSON):**
```json
{
  "email": "exemplo@email.com",
  "senha": "1234"
}
```

**Resposta:**
```json
{
  "message": "Login realizado com sucesso!",
  "user": {
    "email": "exemplo@email.com",
    "nome": "João",
    "tipo": "Cidadão"
  }
}
```

---

##  Recursos

### `GET /recursos`
Retorna todos os recursos cadastrados. Aceita filtros por `recurso`, `fonte` e `distancia`.

**Exemplo:**
```
GET /recursos?recurso=Água&fonte=Comunitária&distancia=Até 5Km
```

**Resposta:**
```json
[
  {
    "nome": "Associação de Bairro",
    "recurso": "Água",
    "fonte": "Comunitária",
    "distancia": "Até 1Km",
    "latitude": -23.5378,
    "longitude": -46.6369,
    "endereco": "Praça da Paz, 12",
    "contato": "(11) 8765-4321",
    "horario": "09h às 19h"
  }
]
```

---

### `POST /recursos`
Cadastra um novo ponto de recurso.

**Body (JSON):**
```json
{
  "nome": "Posto de Apoio",
  "recurso": "Alimento",
  "fonte": "Oficial",
  "distancia": "Até 5Km",
  "latitude": -23.55,
  "longitude": -46.63,
  "endereco": "Rua das Árvores, 45",
  "contato": "(11) 98888-0000",
  "horario": "08h às 18h"
}
```

---

##  Fontes

### `GET /fontes`
Retorna as fontes disponíveis:

```json
["Comunitária", "Oficial"]
```

---

##  Distâncias

### `GET /distancias`
Retorna as faixas de distância disponíveis:

```json
["Até 1Km", "Até 5Km", "Até 10Km"]
```

---

