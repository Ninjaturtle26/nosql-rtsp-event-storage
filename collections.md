# Coleções do banco `bed_monitoring`

## Coleção: events

Responsável por armazenar:

- eventos detectados
- câmera e sessão relacionadas
- tipo do evento
- frames inicial/final
- arquivos associados
- parâmetros do modelo
- status da notificação via WhatsApp

Operações demonstradas:

- INSERT: novo evento detectado.
- FIND: busca de eventos pendentes.
- UPDATE: alteração de `notification.status` e `notification.sent_at`.
- DELETE: remoção controlada de documentos de demonstração.

## Coleção: sessions

Responsável por armazenar:

- nome da sessão
- câmera associada
- horário de início
- horário de finalização
- status da gravação

## Coleção: cameras

Responsável por armazenar:

- identificador da câmera
- localização
- stream utilizada
- sessão atual
- status operacional
- último horário visto pelo sistema

## Coleção: system_logs

Responsável por armazenar:

- eventos operacionais do sistema
- mensagens de inicialização/finalização
- registros de inserção de eventos
- metadados auxiliares para auditoria
