# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | 82,83% (994 / 1.200) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | 27,12% (48 / 177) |
| An toàn | Tỉ lệ lỗi lọt đến khách (mở lại trong 7 ngày) | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | 4,25% (51 / 1.200); riêng phạm vi `noi_dia` + `hang_nang`: 3,97% (39 / 982) |
| Dùng | Nhóm tự đề xuất: % yêu cầu của nhóm trợ lý được nhân viên mở gợi ý | Số `refund_request_created` có `arm = tro_ly` và có `agent_suggestion_shown` cùng `trace_id`, chia số `refund_request_created` có `arm = tro_ly` | Không cần tính |
| An toàn | Nhóm tự đề xuất: % đơn hoàn sai tiền qua kiểm tra mẫu hằng tuần (bắt lỗi ngầm mà khách và nhân viên không thấy) | Số `audit_sample_checked` có `so_tien_da_hoan ≠ so_tien_dung`, chia số `audit_sample_checked` trong tuần (mẫu 100 đơn/tuần) | Không cần tính |

- **Nhận xét số liệu chạy thử:** Chỉ số chính trong đợt chạy thử là **82,83%** (994 / 1.200 yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày); tỉ lệ bỏ qua gợi ý trong đợt chạy thử là **27,12%** (48 / 177 yêu cầu được xem lại); tỉ lệ mở lại trong 7 ngày (lỗi lọt đến khách) trong đợt chạy thử là **4,25%** trên toàn mẫu (51 / 1.200) và **3,97%** trong phạm vi pilot `noi_dia` + `hang_nang` (39 / 982). *(Lưu ý: chỉ ghi nhận kết quả trong đợt chạy thử, không kết luận trợ lý đã nâng chỉ số vì đợt chạy thử không có nhóm đối chứng).*

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách | request_id, loai, so_tien, depot, staff_id, arm (tro_ly / doi_chung), created_at, trace_id | Khi khách gửi yêu cầu |
| `input_validation_failed` | Agent | request_id, truong_loi (ma_don / so_tai_khoan / ...), gia_tri_nhap, trace_id | Khi đầu vào của khách không đúng định dạng (ví dụ mã đơn sàn TMĐT thay vì mã vận đơn) |
| `agent_run_completed` | Agent | request_id, attempt, tokens_in, tokens_out, tool_calls, status (ok / loi), trace_id | Sau **mỗi** lần chạy, kể cả lần lỗi |
| `agent_suggestion_shown` | Giao diện nhân viên | request_id, staff_id, so_tien_de_xuat, trace_id | Khi gợi ý hiện ra cho nhân viên |
| `staff_review_decision` | Nhân viên | request_id, staff_id, quyet_dinh (giu / sua / bo), phut_xem_lai (đo thật), trace_id | Khi nhân viên bấm giữ, sửa hoặc bỏ |
| `staff_rework_completed` | Nhân viên | request_id, staff_id, phut_lam_lai (đo thật), ly_do, trace_id | Khi làm lại xong một ca trợ lý trả lời sai |
| `handoff_to_staff` | Agent | request_id, reason (het_lan_chay / thieu_du_lieu / ngoai_pham_vi), tom_tat, trace_id | Khi chuyển yêu cầu cho nhân viên |
| `refund_ledger_write` | Dịch vụ sổ cái | request_id, idempotency_key, so_tien, ket_qua, trace_id | Khi ghi khoản hoàn vào sổ cái |
| `ticket_closed` | Hệ thống ticket | request_id, closed_at, trace_id | Khi yêu cầu được đóng |
| `ticket_reopened` | Khách | request_id, reopened_at, reason, trace_id | Khi khách mở lại yêu cầu |
| `audit_sample_checked` | Kế toán | request_id, so_tien_da_hoan, so_tien_dung, phien_ban_bang_gia, trace_id | Hằng tuần, mẫu 100 đơn |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- **Chính** (đóng trong 24 giờ, không mở lại trong 7 ngày): `refund_request_created.created_at` và `ticket_closed.closed_at` (≤ 24 giờ), không có `ticket_reopened` trong 7 ngày sau `closed_at`. Đo được.
- **Dùng · bỏ qua gợi ý:** `staff_review_decision` có `quyet_dinh` là `sua` hoặc `bo`, chia tổng số `staff_review_decision`. Đo được.
- **An toàn · mở lại trong 7 ngày:** số `ticket_reopened` trong 7 ngày, chia số `refund_request_created`. Đo được.
- **Dùng · tự đề xuất:** `agent_suggestion_shown` nối với `refund_request_created` (lọc `arm = tro_ly`) qua `trace_id`. Đo được.
- **An toàn · tự đề xuất:** `audit_sample_checked`. Đo được.
- **Chi phí mỗi việc thành công (thay số simulated bằng số đo thật):** token và tool từ `agent_run_completed`, phút xem lại từ `staff_review_decision.phut_xem_lai`, phút làm lại từ `staff_rework_completed.phut_lam_lai`, việc thành công từ `ticket_closed` không có `ticket_reopened`. Đo được.

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | +51,8%, chi phí mỗi việc thành công lên 6.787 đ [simulated] (B1) | Tỉ lệ làm lại theo tuần (`staff_rework_completed` ÷ `refund_request_created`, nhóm trợ lý) > 7%; đợt chạy thử: 4,9% (48/982) trong phạm vi | Thu hẹp về `noi_dia`, rà 20 trace làm lại gần nhất trong 3 ngày | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài | 11.743 đ = 0,98× của 12.000 đ; 12.415 đ = 1,03× nếu làm lại 15,3 phút/ca như dữ liệu [simulated] (B4) | % yêu cầu được xem lại (`staff_review_decision` ÷ `agent_suggestion_shown`) còn > 50% ở cuối bước rollout 0.25; phút xem lại trung bình > 4,8 phút | Giảm tỉ lệ xem lại theo bậc khi tỉ lệ sửa + bỏ < 15%; không mở bước 0.50 nếu chưa giảm được | Trưởng nhóm CSKH |
| Khối lượng thấp hơn dự kiến | Cố định 40 triệu/tháng: +1.185 đ/việc ở 45.000 yc/tháng, +2.370 đ/việc (5.784 đ = 0,48×) nếu còn một nửa; vượt 12.000 đ nếu dưới khoảng 6.212 yc/tháng [simulated] (A4) | Số việc thành công theo tuần < 50% kế hoạch | Không mở rộng pilot; xem lại hợp đồng chi phí cố định | PM trợ lý hoàn phí |
