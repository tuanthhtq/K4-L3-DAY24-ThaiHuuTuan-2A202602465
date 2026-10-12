# Verification — CP3

- OS / Python: Windows, Python 3.11.15.
- PII: `python -m pytest tests/test_pii.py -v -s` — 2 passed; precision 1.000, recall 1.000.
- Policy + ledger: `python -m pytest tests/test_policy.py tests/test_ledger.py -q` — 7 passed.
- OBO + split + containment: `python -m pytest tests/test_obo.py tests/test_split.py tests/test_injection.py tests/test_scaffold_dispatch.py -q` — 18 passed.
- Full suite: `python -m pytest tests -q` — 33 passed.
- Ledger: `reports/ledger.jsonl` has 23 entries; `verify()` returns `True`; tampered copy returns `False`; includes `http_post` deny with non-empty reason.
- Gitleaks: version 8.30.1; history scan found the synthetic token at commit `1bdd849` with rule `lab24-synthetic-token`; current-tree scan clean.
- Dependency lock: `pip install --require-hashes -r requirements.lock` passed.
- Pre-commit: Gitleaks hook pinned to v8.30.1; `pre-commit run --all-files` passed.
- CP3 and CP4 scope complete.
