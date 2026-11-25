# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Nguyễn Tuấn Anh · Người gắn nhãn 2: Đào Hồng Thắng (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | ... | Do người dùng | ... | ... |
| 2 | ... | Hệ thống | ... | ... |
| 3 | ... | Ngữ cảnh | ... | ... |
| 4 | ... | Giới hạn hệ thống | ... | ... |
| 5 | ... | Ngầm | ... | ... |
| 6 | ... | Do người dùng | ... | ... |
| 7 | ... | Hệ thống | ... | ... |
| 8 | ... | Hệ thống | ... | ... |
| 9 | ... | Do người dùng | ... | ... |
| 10 | ... | Ngữ cảnh | ... | ... |
| 11 | ... | Giới hạn hệ thống | ... | ... |
| 12 | ... | Ngầm | ... | ... |
| 13 | ... | Giới hạn hệ thống | ... | ... |
| 14 | ... | Do người dùng | ... | ... |
| 15 | ... | Hệ thống | ... | ... |
| 16 | ... | Ngữ cảnh | ... | ... |
| 17 | ... | Ngầm | ... | ... |
| 18 | ... | Hệ thống | ... | ... |
| 19 | ... | Giới hạn hệ thống | ... | ... |
| 20 | ... | Hệ thống | ... | ... |

**Tỉ lệ đồng thuận:** ... / 20 = ...%

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- ...

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | `agent_run_completed` có `status = loi` và `error_code = ma_don_khong_hop_le` (thêm thuộc tính `error_code`); đếm hằng ngày, cảnh báo khi > 2% số `refund_request_created` trong ngày | Nhận diện mã đơn của sàn thương mại điện tử và tra sang mã vận đơn; không tra được thì hướng dẫn kèm ảnh chỉ chỗ lấy mã vận đơn, không dừng ở "mã không hợp lệ" | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát mỗi giờ: tin nhắn "đã hoàn" (`ticket_closed`) không có `refund_ledger_write` với `ket_qua = ok` cùng `trace_id`; ngưỡng 0 ca | Chỉ báo "đã hoàn" khi sổ cái trả ok; sổ cái lỗi 503 sau 3 lần thì báo khách "đang xử lý" và gửi `handoff_to_staff` | Kỹ sư trưởng agent |
| 16 | Ngữ cảnh | Tỉ lệ thông báo hoàn tiền gửi trong khung 22:00–07:00 (theo `ticket_closed.closed_at`) và số `ticket_reopened` có `reason = lam_phien`, theo tuần; ngưỡng 0 thông báo ban đêm | Giữ thông báo gửi ban đêm vào hàng đợi, gửi lúc 07:00; tiền vẫn hoàn ngay theo thiết kế | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | `handoff_to_staff` có `reason = thieu_du_lieu`, đếm theo `loai` hằng tuần; cảnh báo khi > 5% yêu cầu trong phạm vi pilot | Giữ cách chuyển nhân viên kèm tóm tắt; chặng do hãng nước ngoài giao thuộc `quoc_te`, đã đưa ra khỏi phạm vi pilot (A3: 1,88×, simulated) | PM trợ lý hoàn phí |
| 17 | Ngầm | `audit_sample_checked`: kiểm tra mẫu 100 đơn mỗi tuần, so `so_tien_da_hoan` với `so_tien_dung` và `phien_ban_bang_gia`; ngưỡng 1% đơn lệch | Xoá bộ nhớ đệm khi có bảng giá mới; ghi phiên bản bảng giá vào trace; tính lại và hoàn bù 212 đơn lệch | Kế toán trưởng |
