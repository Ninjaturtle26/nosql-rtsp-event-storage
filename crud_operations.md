# Demonstracao CRUD no MongoDB

Este arquivo explica como provar as operacoes NoSQL usadas pelo projeto `bed-monitoring-project`.

## Como rodar no WSL

Suba o MongoDB pelo projeto principal:

```bash
docker compose -f infrastructure/mongodb/docker-compose.yaml up -d
```

Instale a dependencia, se necessario:

```bash
python3 -m pip install -r nosql_model/requirements.txt
```

Se o seu MongoDB exigir usuario e senha, informe a URI somente no terminal local:

```bash
export MONGO_URI="mongodb://USUARIO:SENHA@localhost:27017"
```

Rode o ciclo completo mantendo os documentos no banco para prints no MongoDB Compass:

```bash
python3 nosql_model/crud_demo.py all --keep
```

O comando imprime o `Demo run`. Use esse valor para apagar apenas os documentos de demonstracao depois:

```bash
python3 nosql_model/crud_demo.py delete --demo-run demo_YYYYMMDD_HHMMSS
```

Tambem existe uma tela simples de terminal:

```bash
python3 nosql_model/crud_demo.py
```

## Relacao com o sistema real

- INSERT: `LiveMonitor.save_event_metadata()` chama `EventRepository.insert_event()`, que executa `insert_one()` na colecao `events`.
- FIND: `WhatsAppWorker.run()` procura eventos pendentes com `collection.find({"notification.enabled": True, "notification.status": "PENDING"})`.
- UPDATE: `WhatsAppWorker.process_event()` chama `update_event_document()` para atualizar `notification.status`, `notification.sent_at` e `notification.last_error`.
- DELETE: o fluxo original nao precisava apagar eventos; a demonstracao agora usa `delete_many()` apenas em documentos marcados com `demo: true`.

## Colecoes demonstradas

- `events`: eventos de deteccao, arquivos relacionados e status de notificacao.
- `sessions`: sessoes de captura abertas e fechadas pelo monitor.
- `cameras`: cadastro e estado atual de cada camera.
- `system_logs`: registros operacionais gerados pelo sistema.

## Sugestao de prints

1. Terminal com `python3 nosql_model/crud_demo.py all --keep`.
2. MongoDB Compass mostrando `events` com `notification.status: "SENT"`.
3. MongoDB Compass mostrando `cameras` com `status: "maintenance"` na demo, ou `active/inactive` quando o sistema real rodar.
4. MongoDB Compass mostrando `system_logs`.
5. Terminal com `python3 nosql_model/crud_demo.py delete --demo-run <valor>` e `deleted` maior que zero.
