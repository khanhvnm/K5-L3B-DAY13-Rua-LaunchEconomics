# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Nguyễn Tuấn Anh · Người gắn nhãn 2: Đào Hồng Thắng (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Hệ thống | Có | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Hệ thống | Không | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận:** 19 / 20 = 95,0% (ĐẠT yêu cầu ≥ 80%, tức ≥ 16/20 ca)

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- **Ca 18 (`Ngữ cảnh` thay vì `Hệ thống`):** Trợ lý tính đúng số tiền hoàn theo đúng thiết kế và chính sách (30.000 đ × 50% = 15.000 đ cho đơn giao trễ), chỉ có giả định ngầm rằng "khách hàng đã biết quy tắc hoàn 50%" là không khớp hoàn cảnh thực tế khiến khách hiểu lầm và mở lại yêu cầu, nên nguyên nhân gốc là lỗi **Ngữ cảnh**.
- **Ghi chú quy tắc phân biệt bổ sung cho các ca dễ lẫn đã thống nhất:**
  - *Ca 6, 9 (`Do người dùng`):* Nguyên nhân gốc là khách chọn nhầm mục hoặc nhập mã đơn sàn TMĐT thay vì mã vận đơn LogiX-VN (việc trợ lý chưa biết gợi ý nằm ở bước khắc phục).
  - *Ca 8, 15 (`Hệ thống`, không phải `Ngầm`):* Sai sót so với chính sách/thiết kế đã lộ ra và được nhân viên hoặc hệ thống trích dẫn phát hiện ngay trước khi đóng đơn; nhãn `Ngầm` (như *Ca 5, 12, 17*) chỉ dùng khi cả khách lẫn hệ thống đều không nhận ra cho tới khi kiểm tra mẫu hoặc rà soát chi phí định kỳ.
  - *Ca 13 (`Giới hạn hệ thống`):* Yêu cầu nằm ngoài phạm vi hỗ trợ hoặc thiếu công cụ/dữ liệu để xử lý thì gắn nhãn `Giới hạn hệ thống`, kể cả khi cách trợ lý từ chối/chuyển tiếp chưa khéo.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Event `input_validation_failed` (mã đơn không khớp định dạng vận đơn LogiX-VN); theo dõi hằng ngày, cảnh báo khi vượt ngưỡng > 2% tổng số yêu cầu/ngày | Nhận diện mẫu mã đơn sàn TMĐT để tự tra chéo sang mã vận đơn LogiX-VN; nếu không tra được thì hiển thị hướng dẫn kèm ảnh minh hoạ vị trí mã vận đơn trên phiếu gửi | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát tự động mỗi giờ giữa tin nhắn báo "đã hoàn" và event `refund_ledger_write` có `ket_qua = ok` cùng `trace_id`; cảnh báo ngay khi có > 0 ca lệch | Chỉ gửi thông báo "đã hoàn" sau khi dịch vụ sổ cái trả về `refund_ledger_write` thành công (`ok`); nếu lỗi 503 sau 3 lần thử thì báo "đang xử lý" và bắn event `handoff_to_staff` | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Event `ticket_reopened` có `reason` thắc mắc số tiền hoàn nhưng kiểm tra số tiền hoàn đúng chính sách; tổng hợp hằng tuần, cảnh báo khi > 1% số yêu cầu đóng/tuần | Cập nhật mẫu tin nhắn phản hồi luôn ghi rõ công thức và lý do tính tiền (ví dụ: `30.000 đ × 50% theo chính sách giao trễ = 15.000 đ`) | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Event `handoff_to_staff` với `reason = thieu_du_lieu` hoặc `ngoai_pham_vi` thống kê theo từng `loai` yêu cầu mỗi ngày; cảnh báo khi một loại có tỉ lệ chuyển > 20%/ngày | Loại yêu cầu `quoc_te` ra khỏi phạm vi pilot (chuyển thẳng nhân viên từ đầu); với ca thiếu dữ liệu tra cứu được, chuyển nhân viên kèm `tom_tat` thông tin đã thu thập | PM trợ lý hoàn phí |
| 17 | Ngầm | Event `audit_sample_checked` từ việc kế toán kiểm tra mẫu 100 đơn/tuần (`so_tien_da_hoan ≠ so_tien_dung` theo bảng giá hiện hành); cảnh báo khi tỉ lệ lệch ≥ 1%/tuần | Tự động xoá bộ nhớ đệm (cache) bảng giá khi có bảng giá mới được cập nhật và bắt buộc ghi `phien_ban_bang_gia` vào mỗi `trace_id` của lần chạy | Kế toán trưởng |
