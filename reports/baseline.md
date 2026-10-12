# Baseline - CP1

1. Agent chưa có identity cho từng run. `_naive_loop()` chỉ nhận `message` và `llm`, không có `agent_id`, `run_id` hoặc principal: `agent/loop.py:27`.

2. Không có policy kiểm quyền trước `http_post`. Baseline đọc chỉ thị từ ticket, đọc customer rồi gọi trực tiếp `tools.http_post(...)`: `agent/loop.py:34`, `agent/loop.py:39`, `agent/loop.py:44`. `agent/tools.py:68` chỉ kiểm allowlist host/port của sink, không kiểm quyền hoặc loại dữ liệu.

3. POST body được tạo tại `agent/loop.py:44` và gửi qua `requests.post(...)` tại `agent/tools.py:84`. Sink ghi request vào `reports/sink.log`, đường dẫn log được khai báo tại `sink/sink.py:37`.
