# NoSQL RTSP Event Storage

Sistema NoSQL para armazenamento esparso de eventos derivados de streams RTSP, com foco em visão computacional 2D, persistência orientada a eventos e suporte futuro para aprendizado de máquina.

---

# 📌 Tema do Projeto

Este projeto propõe o desenvolvimento de uma arquitetura NoSQL voltada para armazenamento esparso de eventos detectados em streams de vídeo RTSP.

Ao invés de armazenar continuamente vídeos completos, o sistema registra apenas eventos relevantes identificados durante o processamento dos frames, reduzindo significativamente o custo computacional e o volume de armazenamento persistido.

O sistema foi concebido para servir como base de integração futura com pipelines de visão computacional 2D e aprendizado de máquina.

---

# 🎯 Objetivo do Sistema

Desenvolver uma estrutura NoSQL capaz de:

- Receber informações derivadas de streams RTSP;
- Persistir eventos relevantes detectados em tempo real;
- Organizar dados de visão computacional em documentos JSON;
- Permitir escalabilidade para múltiplas câmeras;
- Preparar os dados para futuras análises inteligentes e modelos de Machine Learning.

---

# 🚀 Diferenciais do Sistema

O sistema apresenta os seguintes diferenciais:

- Armazenamento esparso orientado a eventos;
- Redução de armazenamento desnecessário de vídeo bruto;
- Estrutura flexível baseada em documentos JSON;
- Escalabilidade para múltiplos streams RTSP;
- Separação entre metadados e arquivos binários;
- Arquitetura preparada para visão computacional 2D;
- Suporte futuro para integração com modelos de aprendizado de máquina;
- Estrutura modular para análise de eventos, movimentos e objetos detectados.

---

# 🧠 Arquitetura do Sistema

O sistema utiliza uma estratégia híbrida de persistência:

## MongoDB / NoSQL
Responsável pelo armazenamento de:

- Eventos detectados;
- Metadados dos frames;
- Sessões de captura;
- Informações das câmeras;
- Coordenadas e inferências de visão computacional;
- Referências para frames e máscaras.

## Storage Externo
Responsável futuramente pelo armazenamento de:

- Frames (.png / .jpg);
- Motion masks;
- Vídeos;
- Imagens processadas;
- Arquivos derivados da análise computacional.

---

# 🧩 Hierarquia de Informações

A estrutura principal do sistema segue a hierarquia:
```text
Camera
 └── Session
      └── Event
```
## 👥 Integrantes

- Rafael Sansevero Martins Lima
- Marllon Alexander

---

# Demonstração CRUD

O arquivo `crud_demo.py` executa operações de INSERT, FIND, UPDATE e DELETE nas principais coleções do banco `bed_monitoring`:

- `events`
- `sessions`
- `cameras`
- `system_logs`

Para rodar no WSL a partir da raiz do projeto principal:

```bash
docker compose -f infrastructure/mongodb/docker-compose.yaml up -d
python3 -m pip install -r nosql_model/requirements.txt
export MONGO_URI="mongodb://USUARIO:SENHA@localhost:27017"
python3 nosql_model/crud_demo.py all --keep
```

Use `--keep` para manter os documentos no MongoDB e tirar prints no MongoDB Compass.

Depois dos prints, apague somente os documentos da demonstração:

```bash
python3 nosql_model/crud_demo.py delete --demo-run demo_YYYYMMDD_HHMMSS
```

Também é possível abrir uma tela simples no terminal:

```bash
python3 nosql_model/crud_demo.py
```

Mais detalhes estão em `crud_operations.md`.

---

# Relação com o software real

As observações sobre o fluxo do projeto estão corretas:

- INSERT: o `LiveMonitor` cria o documento JSON do evento e chama `EventRepository.insert_event()`, que usa `insert_one()` na coleção `events`.
- FIND: o `WhatsAppWorker` consulta eventos pendentes com `find()` antes de enviar notificações.
- UPDATE: depois do envio pelo WhatsApp, o `WhatsAppWorker` atualiza o mesmo documento em `events`, marcando `notification.status` como `SENT` e preenchendo `notification.sent_at`.
- DELETE: não havia uma necessidade operacional de apagar eventos no fluxo real; por isso o `crud_demo.py` demonstra DELETE de forma controlada, removendo apenas documentos com `demo: true`.

Além disso, o sistema real agora registra/atualiza a coleção `cameras` quando o monitor inicia ou para, e grava eventos operacionais em `system_logs`.
