# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: Rua · Lớp: L3B

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | **4.472 đ** mỗi việc thành công (tổng 4.373.585 đ / 978 việc) [simulated], gấp 16,3 lần hoá đơn token + tool chia số yêu cầu (274,7 đ); 92,5% chi phí là xem lại (40,7%) + làm lại (51,8%) [simulated] | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | 1. Số ca làm lại: gấp đôi → 6.787 đ (**+51,8%**) · 2. Tỉ lệ xem lại: gấp đôi → 6.292 đ (**+40,7%**) · 3. Lương nhân viên: +25% → 5.506 đ (**+23,1%**) [simulated]; giá token gấp đôi chỉ +5,6% | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Toàn bộ, tính cả 222 ca nhân viên làm thay: (4.373.585 + 222 × 12.000) / 1.200 = 5.865 đ/yc = **0,49×** [simulated]; phạm vi noi_dia + hang_nang, cộng cố định 40 triệu/tháng: 4.599 đ = **0,38×** (0,48× nếu khối lượng còn một nửa) [simulated]. Bất lợi: quoc_te 22.515 đ = **1,88×** nên loại khỏi pilot; nếu phải xem lại 100% → 11.743 đ = **0,98×** (12.415 đ = 1,03× với 15,3 phút làm lại/ca như dữ liệu) [simulated] | Giả lập | Trưởng nhóm CSKH |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Trong đợt chạy thử (không có đối chứng): chính 82,83% (994/1.200) đóng 24 giờ, không mở lại 7 ngày · dùng: bỏ qua gợi ý 27,12% (48/177) · an toàn: mở lại 7 ngày 4,25% (51/1.200), 3,97% trong phạm vi pilot. 11 event có `trace_id` đo được cả 5 chỉ số (`chi_so.md`) | Xong, có bằng chứng | Trưởng nhóm CSKH |
| 5 · Bảng lỗi và cách khắc phục | Hai bộ nhãn độc lập 20 ca, đồng thuận **19/20 = 95%** (ca 18 thống nhất là Ngữ cảnh); bảng khắc phục 5 ca đủ năm loại (ca 9, 7, 18, 4, 17), mỗi ca có event, ngưỡng, tần suất và một vai trò phụ trách. Ưu tiên sửa trước ngày bắt đầu: ca 7 (báo "đã hoàn" khi sổ cái lỗi 503; đối soát mỗi giờ, ngưỡng 0 ca) và ca 20 (hoàn trùng, thiếu khoá chống trùng) (`bang_loi.md`) | Xong, có bằng chứng | Kỹ sư trưởng agent |
| 6 · Pilot plan | Chia theo nhân viên 20 + 20, ngẫu nhiên phân tầng theo depot, phạm vi noi_dia + hang_nang; mde 0,06 (859/nhóm, DE 6,96, m ≥ 299 yêu cầu/nhân viên) vì 40 nhân viên không đủ cho 5 điểm (tối đa 1.000 < 1.251). Bất lợi: nếu tác động thật là 5 điểm, power chỉ 0,64. 4 luật dừng có ngưỡng, thời hạn, người dừng (mở lại: đối chứng +2 điểm hoặc trần 6%, hiện 3,97%); quyết định 2027-01-11 (`pilot_plan.yaml`) | Xong, có bằng chứng | Giám đốc vận hành |
| 7 · Rủi ro kinh tế | (1) Làm lại gấp đôi → 6.787 đ (+51,8%); (2) xem lại 100% kéo dài → 11.743 đ = 0,98× (1,03× với 15,3 phút làm lại/ca) — gần hết phần tiết kiệm; (3) khối lượng còn một nửa → cố định 2.370 đ/việc, 5.784 đ = 0,48× [simulated]. Chi tiết dấu hiệu theo dõi và hành động: `chi_so.md` mục E2 | Giả lập | PM trợ lý hoàn phí |

**Đề xuất: Go có điều kiện** cho pilot `noi_dia` + `hang_nang`, chia theo nhân viên 20 + 20, bắt đầu 2026-12-07, quyết định 2027-01-11 (theo `pilot_plan.yaml`). Con số bất lợi đã cân nhắc: xem lại 100% đưa chi phí lên 0,98–1,03× của 12.000 đ [simulated]; power chỉ 0,64 nếu tác động thật là 5 điểm; tỉ lệ mở lại hiện tại 3,97% trong phạm vi.

- Sửa khoá chống trùng (ca 20) và chỉ báo "đã hoàn" khi sổ cái trả ok (ca 7); đối soát mỗi giờ chạy thử 3 ngày với 0 ca lệch · Kỹ sư trưởng agent · kiểm tra 2026-12-04.
- Ký chấp nhận mức chênh 6 điểm (mde 0,06, 859 yêu cầu mỗi nhóm) và power 0,64 ở mức 5 điểm; chốt phạm vi bỏ quoc_te (1,88×) và doi_tac (0,85×) [simulated] · Giám đốc vận hành · kiểm tra 2026-12-02.
- Bật đủ 11 event có `trace_id` trong `chi_so.md` trước ngày bắt đầu; thay phút `_simulated` bằng phút xem lại, làm lại đo thật sau tuần 1 · PM trợ lý hoàn phí · kiểm tra 2026-12-04 và 2026-12-14.
- Có kế hoạch giảm tỉ lệ xem lại theo bậc (khi tỉ lệ sửa + bỏ < 15%) và mục tiêu mỗi lần xem lại ≤ 4,8 phút, vì xem lại 100% không tiết kiệm (B4, simulated); chưa đạt thì không mở bước 0.50 · Trưởng nhóm CSKH · kiểm tra 2026-12-04.
