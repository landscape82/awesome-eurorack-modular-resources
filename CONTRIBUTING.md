# Contributing

`README.md` is generated — never edit it directly, edit `data/modules.yaml` and
regenerate.

By participating in this project, you agree to abide by the
[Code of Conduct](CODE_OF_CONDUCT.md).

## Add a module

1. Fork the repository.
2. Copy [`templates/module-template.yaml`](templates/module-template.yaml) and
   append it to the `modules:` list in [`data/modules.yaml`](data/modules.yaml).
3. Fill in every field you have accurate information for. Required fields:
   `manufacturer`, `module`, `repository`, `type`. See
   [`docs/schema.md`](docs/schema.md) for the full field list and
   [`data/tags.yaml`](data/tags.yaml) for valid `type` values.
4. If the manufacturer isn't already listed in
   [`data/manufacturers.yaml`](data/manufacturers.yaml), add it.
5. Run the validator and regenerate the README locally:

   ```bash
   pip install -r requirements.txt
   python3 scripts/validate_modules.py
   python3 scripts/generate_readme.py
   ```

6. Commit both the `data/modules.yaml` change and the regenerated `README.md`.
7. Open a Pull Request. A GitHub Action will re-run the validator and check
   that `README.md` matches what `data/modules.yaml` generates. New catalogue
   entries merged to `main` are logged automatically to
   [CHANGELOG.md](CHANGELOG.md).

## Scope

Only include projects where source code or developer resources are actually
available — no binary-only firmware, abandoned download pages, or
marketing-only links.

## Licensing

Only list projects that publish their own license. This repository's `LICENSE`
covers the catalogue metadata itself, not the linked projects.
