# Secret giả trong lịch sử Git — CP4

- Scanner và phiên bản: Gitleaks `8.30.1`, config `.gitleaks.toml`.
- Commit chứa token giả: `1bdd849`.
- File, rule và kết quả quét lịch sử: `lab-fake-secret.txt`, rule `lab24-synthetic-token`; `gitleaks git --redact` quét 7 commit, thấy 1 finding và trả exit code 1 đúng kỳ vọng.
- Kết quả quét file hiện tại: `gitleaks dir --redact` không thấy leak và trả exit code 0; token giả chỉ còn trong lịch sử Git.
- Nếu đây là credential thật: thu hồi/rotate ngay, kiểm tra nơi đã sử dụng, thay credential ở mọi bản sao và rà soát log/quyền truy cập.
- Vì sao xoá file khỏi HEAD hoặc pin dependency vẫn chưa đủ: lịch sử Git vẫn giữ giá trị đã lộ; dependency pin và pre-commit chỉ ngăn lỗi mới, không thu hồi credential cũ.
