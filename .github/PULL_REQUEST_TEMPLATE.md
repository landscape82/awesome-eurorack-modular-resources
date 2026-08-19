<!--
Thanks for contributing! If you're adding or fixing a catalogue entry, edit
data/modules.yaml (never README.md directly - it's generated) and run:
  python3 scripts/validate_modules.py
  python3 scripts/generate_readme.py
before committing. See CONTRIBUTING.md for details.
-->

## Summary

<!-- What does this PR change, and why? -->

## Type of change

- [ ] New catalogue entry (`data/modules.yaml`)
- [ ] Fix a broken/dead link
- [ ] Docs / schema / tooling
- [ ] Other

## Broken links

<!--
If this PR fixes link(s) flagged by the Weekly Link Check job summary, list
them here (URL -> what changed): fixed, replaced, removed, or added to
.markdown-link-check.json's ignorePatterns as a known false positive.
-->

## Checklist

- [ ] `python3 scripts/validate_modules.py` passes
- [ ] `python3 scripts/generate_readme.py --check` passes (README matches the data)
- [ ] `npx markdownlint README.md CONTRIBUTING.md docs/*.md --config .markdownlint.json` is clean
- [ ] New/changed repository URLs were verified to actually exist and match the intended project
