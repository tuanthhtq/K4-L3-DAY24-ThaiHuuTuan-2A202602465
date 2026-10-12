# DPIA-lite - CP5

1. Loại dữ liệu và phân loại: ticket text là `internal`; customer record gồm CCCD, phone, bank account, email là `restricted`; toàn bộ dữ liệu là synthetic.
2. Mục đích xử lý và principal: tổng hợp ticket dưới `support_l1`; đọc customer hợp lệ dưới `dpo` cho `support-reply`; mỗi run có `agent_id`, `run_id`, TTL 5 phút.
3. Dữ liệu đi qua những run/tool nào, endpoint nào: Run A gọi `search_docs`; Run B nhận ticket ID từ filename rồi map `related_tickets` và gọi `read_customer`; egress gate kiểm tra `http_post` tới localhost `127.0.0.1:10024`.
4. Bằng chứng deny/allow và giới hạn của mock: CP5 `reports/attack-after.log` là 0 byte; `reports/ledger.jsonl:46` ghi `http_post` deny cho `dpo`; `verify()` True, bản tamper False; mock không đại diện model production, sink chỉ localhost, chưa có external trust anchor cho hash cuối.
