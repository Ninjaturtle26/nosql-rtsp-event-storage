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
Camera
 └── Session
      └── Event

## 👥 Integrantes

- Rafael Sansevero Martins Lima
- Marllon Alexander
