# Module metadata schema

Each entry should describe one Eurorack software project.

Required:

- manufacturer
- module
- repository
- type

Recommended:

- description
- platform
- build
- flash
- hardware
- license
- status

Types:

See [`data/tags.yaml`](../data/tags.yaml) for the canonical, CI-validated list
of `type` values — it is the single source of truth `scripts/validate_modules.py`
checks against. Don't duplicate the list here; it will drift.
