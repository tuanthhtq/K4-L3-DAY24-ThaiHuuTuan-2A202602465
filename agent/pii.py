"""BƯỚC 3a — PII gate TRƯỚC KHI vào context/store (12').

Đọc CHECKPOINTS.md (§3a) trước khi bắt đầu: Presidio không có tiếng Việt
sẵn (AnalyzerEngine() mặc định chỉ hỗ trợ "en"). Đường an toàn cho 2h là
regex recognizer + deny-list cho PERSON — coi spaCy/transformers NER là
stretch goal, KHÔNG bắt buộc.

Interface bắt buộc (tests/test_pii.py gọi trực tiếp 2 hàm này):

    detect(text: str) -> list[dict]
        Mỗi entity: {"type": str, "start": int, "end": int}
        `type` là một trong: "VN_CCCD", "VN_PHONE", "VN_BANK_ACCOUNT", "EMAIL"
        `start`/`end` là offset ký tự trong `text` (offset đầu bao gồm,
        offset cuối KHÔNG bao gồm — giống slice Python text[start:end]).
        Format này khớp với tests/vn_pii_testset.jsonl.

    redact(text: str) -> str
        Trả về `text` sau khi mọi entity từ detect() bị thay bằng
        "[REDACTED_<TYPE>]". Phải xử lý overlap/thứ tự đúng khi có nhiều
        entity (gợi ý: thay từ cuối văn bản về đầu để offset không bị lệch).

Gợi ý định dạng (không bắt buộc đúng regex này, miễn đạt ngưỡng trên test
set ở tests/vn_pii_testset.jsonl):
    VN_CCCD          12 chữ số liên tiếp
    VN_PHONE         0 + 9-10 chữ số, có thể có dấu cách/gạch ngang
    VN_BANK_ACCOUNT  8-16 chữ số liên tiếp, thường đi kèm "STK"/"số tài khoản"
    EMAIL            dạng chuẩn local@domain.tld

Đo bằng: pytest tests/test_pii.py -v -s   (in ra precision/recall)
"""
from __future__ import annotations

import re


_PATTERNS = (
    ("VN_BANK_ACCOUNT", re.compile(r"(?i)(?:STK|số\s+tài\s+khoản)\s*[:#-]?\s*(?P<value>\d{8,16})(?!\d)"), 0),
    ("EMAIL", re.compile(r"(?i)(?<![\w.+-])[\w.+-]+@[a-z0-9-]+(?:\.[a-z0-9-]+)+"), 1),
    ("VN_PHONE", re.compile(r"(?<!\d)0(?:[ -]?\d){9,10}(?!\d)"), 2),
    ("VN_CCCD", re.compile(r"(?<!\d)\d{12}(?!\d)"), 3),
)


def detect(text: str) -> list[dict]:
    candidates = []
    for entity_type, pattern, priority in _PATTERNS:
        for match in pattern.finditer(text):
            start, end = match.span("value") if "value" in pattern.groupindex else match.span()
            candidates.append((priority, start, end, entity_type))

    selected = []
    for _, start, end, entity_type in sorted(candidates):
        if any(start < item["end"] and item["start"] < end for item in selected):
            continue
        selected.append({"type": entity_type, "start": start, "end": end})
    return sorted(selected, key=lambda item: item["start"])


def redact(text: str) -> str:
    for entity in reversed(detect(text)):
        replacement = f"[REDACTED_{entity['type']}]"
        text = text[:entity["start"]] + replacement + text[entity["end"]:]
    return text
