# Báo cáo cá nhân — PhamDuyThanh-2A202604075

## 1. Thông tin thành viên

- Họ tên: Phạm Duy Thành
- MSSV: 2A202604075
- Email: 26ai.thanhpd2@vinuni.edu.vn
- Vai trong nhóm: Người kiểm số (CP1–CP2), Người viết code sau giải lao (CP3 · Nhiệm vụ D1), Người rà soát nhãn `simulated` và kiểm chạy độc lập (CP5)

## 2. Phần việc phụ trách

- **Chuẩn bị & CP1:** Cài đặt môi trường `.venv` độc lập trên máy cá nhân, chạy kiểm chứng `src/lab13.py`; tính tay đối chiếu ba phép thử A1 và dòng trace A2; hoàn thiện phần A1–A4 trong `report/team/bang_chi_phi.md` trên nhánh `cp1/a-bang-chi-phi`.
- **CP2:** Kiểm tra tính đối xứng tuyến tính của bảng độ nhạy B1, hoàn thiện phần B1–B4 trong `report/team/bang_chi_phi.md` trên nhánh `cp2/b-bang-chi-phi`.
- **CP3 (đổi người viết code):** Viết code tính cỡ mẫu và thiết kế cụm cho 5 câu D1 (a–e), tính power ở mức chênh 5 điểm và tỉ lệ `mo_lai_trong_7_ngay` nền trong `src/lab13.py` trên nhánh `cp3/d1-sample-size`.
- **CP5:** Rà soát nhãn `simulated` cho các con số tính từ hai cột `_simulated`, rà từ cấm trong thư mục hồ sơ nhóm và chạy lại `src/lab13.py` trên máy thứ hai.

## 3. Đóng góp cụ thể

1. **Tính tay đối chiếu độc lập (vai trò Người kiểm số):**
   - **A1 ($p = 0{,}8 \Rightarrow 1 - p = 0{,}2$):**
     - Tối đa $k = 2$ lần chạy: $(1 - 0{,}2^2) / 0{,}8 = 0{,}96 / 0{,}8 = 1{,}20$ lần chạy.
     - Chạy đến khi đúng ($k = \infty$): $1 / 0{,}8 = 1{,}25$ lần chạy.
     - Hệ số chi phí khi $k = 3$: $((1 - 0{,}2^3) / 0{,}8) / (1 - 0{,}2^3) = 1{,}24 / 0{,}992 = 1{,}25$ ($k$ triệt tiêu).
   - **A2 (dòng `run_00001` của yêu cầu `RF-70000` trong `src/logix_runs.csv`):**
     - `tokens_in = 4.759`, `tokens_out = 492`, `tool_calls = 5` $\Rightarrow$ tiền token $= 4{,}759 \times 26 + 0{,}492 \times 130 = 123{,}734 + 63{,}960 = 187{,}694\text{ đ}$; tiền tool $= 5 \times 15 = 75\text{ đ}$; tổng $= 262{,}694\text{ đ}$ (khớp tuyệt đối với hàm `mo_hinh`).
   - **A2 (ca lỗi 3 lần `RF-70008` gồm `run_00009`..`run_00011`):**
     - Tổng `tokens_in = 13.897` ($361{,}322\text{ đ}$), `tokens_out = 1.071` ($139{,}230\text{ đ}$), `tool_calls = 14` ($210\text{ đ}$) $\Rightarrow$ đóng góp `710,552 đ` vào tử số nhưng đóng góp `0` việc thành công vào mẫu số.
   - **B1 (kiểm tra đối xứng tuyến tính):** Đối chiếu mức giảm của các kịch bản "giảm một nửa" đúng bằng một nửa mức tăng của kịch bản "gấp đôi" (`−2,8%` vs `+5,6%` giá token; `−20,3%` vs `+40,7%` xem lại; `−25,9%` vs `+51,8%` làm lại).
2. **Hoàn thiện `report/team/bang_chi_phi.md` (CP1 & CP2):**
   - Điền đủ 9 dòng bảng A2 (`4.472 đ` mỗi việc thành công [`simulated`], gấp `16,3 lần` hoá đơn token + tool `274,7 đ/yêu cầu`; giờ nhân viên chiếm `92,5%` gồm `51,8%` làm lại và `40,7%` xem lại [`simulated`]; chi phí cả hệ thống cộng `222` ca chuyển nhân viên là `5.865 đ/yêu cầu = 0,49×` của `12.000 đ` [`simulated`]).
   - Điền bảng A3 (`noi_dia` `0,22×`, `hang_nang` `0,69×`, `quoc_te` `1,88×`, `doi_tac` `0,85×` [`simulated`]) và bảng A4 cộng cố định `40 triệu đ/tháng` (`4.599 đ = 0,38×` ở `45.000` yc/tháng và `5.784 đ = 0,48×` ở nửa khối lượng [`simulated`]).
   - Điền bảng B1 (9 kịch bản), B2 (xếp hạng 3 yếu tố nhạy nhất: làm lại `+51,8%`, xem lại `+40,7%`, lương `+23,1%` [`simulated`]), B3 (giới hạn `2 lần` rẻ nhất cho công ty ở mức `6.901.220 đ` [`simulated`] so với `1 lần` có CPS thấp nhất `4.111 đ` [`simulated`]) và B4 (xem lại 100% tốn `11.743 đ = 0,98×` với `9 phút/ca` làm lại và `12.415 đ = 1,03×` với `15,3 phút/ca` trung bình dữ liệu [`simulated`]).
3. **Viết code Nhiệm vụ D1 trong `src/lab13.py` (CP3):**
   - Cài đặt `co_mau()`, `he_so_thiet_ke()`, `co_mau_hieu_dung()`, `so_yc_moi_cum_toi_thieu()` và `in_d1()`, tính đủ 5 câu D1 (`1.251` yêu cầu/nhóm; `3.103` yêu cầu/nhóm $\Rightarrow 42$ NV/nhóm; trần `1.000` với 20 NV/nhóm; trần `300` với 6 depot/nhóm; `m >= 299` yêu cầu/NV với `DE = 6,96` cho mức chênh 6 điểm).
   - Tính power thực tế bằng `statsmodels` (`NormalIndPower`) còn `0,64` (`64,2%`) nếu tác động thật là 5 điểm ở cỡ mẫu `859`, và tính tỉ lệ `mo_lai_trong_7_ngay` nền (`4,25%` toàn mẫu; `3,97%` trong phạm vi `noi_dia + hang_nang`).

## 4. Bằng chứng

- Nhánh `cp1/a-bang-chi-phi`: cập nhật phần A1–A4 trong `report/team/bang_chi_phi.md`.
- Nhánh `cp2/b-bang-chi-phi`: cập nhật phần B1–B4 trong `report/team/bang_chi_phi.md`.
- Nhánh `cp3/d1-sample-size`: bổ sung phần D1 vào `src/lab13.py` (chạy `python lab13.py` trên máy cá nhân in `Ba phép thử đáp án biết trước: ĐẠT` và toàn bộ bảng A1–A4, B1–B4, D1).
- Nhánh `report/thanh-ca-nhan`: hoàn thiện `report/team/2A202604075_PhamDuyThanh.md`.

## 5. Công cụ AI đã dùng

- **Công cụ:** Trợ lý AI Google Antigravity.
- **Mục đích sử dụng:** Hỗ trợ đọc nhanh cấu trúc đề bài/quy tắc phân công nhóm, gợi ý cấu trúc hàm D1 (`co_mau`, `so_yc_moi_cum_toi_thieu`, `in_d1`) trong `src/lab13.py`, và rà soát checklist quy tắc nhãn `simulated` cũng như từ cấm trong hồ sơ.
- **Cách tự kiểm tra kết quả:** Tự giải tay công thức A1, dòng `run_00001`, ca `RF-70008`, tính đối xứng B1 và bất phương trình cỡ mẫu cụm câu D1e; trực tiếp chạy `python lab13.py` trong `src/.venv`, kiểm tra `ruff check` và đối chiếu từng con số với `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`.

## 6. Tự đánh giá

- Hoàn thành đầy đủ, đúng hạn toàn bộ phần việc được giao ở cả vai trò người kiểm số (CP1–CP2) và người viết code D1 (CP3), tuân thủ quy ước nhánh Git và phân quyền file của nhóm để không gây xung đột khi ghép bài.
- Bài học chính rút ra từ lab: chi phí thật mỗi việc thành công (`4.472 đ` [`simulated`]) gấp `16,3 lần` hoá đơn token + tool vì `92,5%` đến từ thời gian nhân viên xem lại và làm lại; tối ưu riêng CPS theo từng lần chạy dễ bỏ quên chi phí đẩy việc về nhân viên (B3); và khi chia thử nghiệm theo cụm nhân viên, trần cỡ mẫu hiệu dụng bị khống chế bởi $c / \text{ICC}$ nên phải đánh đổi mức chênh tối thiểu phát hiện được và công bố minh bạch power thực tế (`0,64`) cho hội đồng Gate 2a.
