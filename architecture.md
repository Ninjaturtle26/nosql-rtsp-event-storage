# Arquitetura NoSQL do Sistema

O sistema utiliza modelagem orientada a eventos para armazenar:

- detecções de movimento
- falsos positivos
- verdadeiros positivos
- parâmetros do detector
- contexto espacial
- contexto temporal

Objetivo:
Construir um dataset evolutivo para melhoria futura do sistema.

## Fluxo real do banco de dados

1. O `LiveMonitor` detecta movimento ou possível saída da cama.
2. O evento é salvo como JSON local e inserido na coleção `events`.
3. O `WhatsAppWorker` busca eventos pendentes na coleção `events`.
4. Depois do processamento, o mesmo documento é atualizado com o status da notificação.
5. A câmera é registrada/atualizada em `cameras`.
6. A criação de sessão, fechamento de sessão e inserção de eventos geram registros em `system_logs`.

O projeto não depende de DELETE no fluxo real, mas a operação é demonstrada no arquivo `crud_demo.py` para cumprir o CRUD completo.
