# Verification — CP3

- OS / Python: Windows, Python 3.11.15.
- PII: `python -m pytest tests/test_pii.py -v -s` — 2 passed; precision 1.000, recall 1.000.
- Policy + ledger: `python -m pytest tests/test_policy.py tests/test_ledger.py -q` — 7 passed.
- OBO + split + containment: `python -m pytest tests/test_obo.py tests/test_split.py tests/test_injection.py tests/test_scaffold_dispatch.py -q` — 18 passed.
- Full suite: 30 passed; 3 CP4 supply-chain tests fail because `.pre-commit-config.yaml`, `requirements.lock` and completed `reports/secrets-incident.md` are not implemented yet.
- Ledger: `reports/ledger.jsonl` has 23 entries; `verify()` returns `True`; tampered copy returns `False`; includes `http_post` deny with non-empty reason.
- CP3 scope complete. CP4 remains pending.
