

## Hierarchical Aggregation Model

```text
Camera
 └── Session
      └── Event
           ├── Spatial Context
           ├── Temporal Context
           ├── Detection Parameters
           ├── Motion Masks
<<<<<<< HEAD
           └── Human Validation
```
=======
           └── Notification Status

Coleções de apoio:

- `cameras`: documento agregado com estado atual da câmera.
- `sessions`: documento da sessão de gravação/processamento.
- `events`: documentos esparsos com apenas eventos relevantes.
- `system_logs`: trilha operacional para auditoria e demonstração.
>>>>>>> 19bbba2 (feat: implementa CRUD e evidencias NoSQL)
