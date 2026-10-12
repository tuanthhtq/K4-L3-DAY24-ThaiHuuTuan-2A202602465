# Compliance mapping - CP5

| Nguồn / yêu cầu | Control đã làm | Evidence file:dòng | Giới hạn |
|---|---|---|---|
| Luật 91/2025/QH15 | PII detection/redaction trước bước tóm tắt; policy deny restricted egress | `agent/pii.py:44`, `agent/pii.py:59`, `agent/policy.py:60`, `reports/ledger.jsonl:46` | Mock evidence không tự chứng minh tuân thủ pháp luật; chưa đối chiếu điều khoản gốc |
| NĐ 356/2025/NĐ-CP | Tách Run A/Run B, principal/scope/purpose/TTL, audit ledger | `agent/runner.py:81`, `agent/runner.py:140`, `agent/runner.py:159`, `agent/ledger.py:49` | Chỉ là control kỹ thuật trong lab, không phải đánh giá pháp lý |
| Luật AI 134/2025/QH15 | Chặn instruction không tin cậy khỏi quyết định customer; lưu decision allow/deny | `agent/runner.py:130`, `agent/runner.py:145`, `reports/ledger.jsonl:46` | Mock LLM và dữ liệu synthetic; chưa đánh giá model production |
| OWASP ASI01, ASI03, ASI04 | Prompt-injection containment, least privilege, egress enforcement | `tests/test_split.py:75`, `tests/test_obo.py:51`, `tests/test_injection.py:71`, `agent/policy.py:62` | Phạm vi chỉ localhost; chưa bao phủ toàn bộ threat model |

Chỉ ghi điều khoản cụ thể khi đã đối chiếu văn bản gốc. Mô phỏng kỹ thuật không tự chứng minh tuân thủ pháp luật.
