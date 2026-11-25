# Báo cáo cá nhân — DaoHongThang-2A202604076

## 1. Thông tin thành viên

- Họ tên: Đào Hồng Thắng
- MSSV: 2A202604076
- Email: 26ai.thangdh2@vinuni.edu.vn
- Vai trong nhóm: Người gắn nhãn 2, kiêm giữ hồ sơ (`report/team/ho_so_launch_v0.md`)

## 2. Phần việc phụ trách

- **Giữ hồ sơ launch v0:** điền `ho_so_launch_v0.md` dần theo từng checkpoint, mỗi mục có con số chính, trạng thái và một vai trò phụ trách; chốt dòng đề xuất cuối.
- **CP1:** tên nhóm, lớp; mục 1 (chi phí mỗi việc thành công) và mục 3 (so với nhân viên tự làm).
- **CP2:** nháp mục 7 (rủi ro kinh tế) từ bảng độ nhạy; đánh dấu mục 4–6 là `Chưa` kèm vai trò phụ trách.
- **CP3:** gắn nhãn độc lập 20 ca lỗi (người gắn nhãn 2), gửi bộ nhãn để so với người gắn nhãn 1.
- **CP4:** rà số mục 4, 5, 6 với `chi_so.md`, `bang_loi.md`, `pilot_plan.yaml` và output `src/lab13.py`.
- **CP5:** nháp dòng đề xuất Go có điều kiện (điều kiện, người phụ trách, ngày kiểm tra); điền phiếu chấm khi nhóm làm hội đồng.

## 3. Đóng góp cụ thể

1. **Mục 1 và 3 của hồ sơ (CP1):**
   - Mục 1: `4.472 đ` mỗi việc thành công (4.373.585 đ / 978 việc) [simulated], gấp `16,3` lần hoá đơn token + tool chia số yêu cầu (`274,7 đ`); `92,5%` chi phí là giờ nhân viên (làm lại `51,8%`, xem lại `40,7%`) [simulated].
   - Mục 3: phạm vi `noi_dia` + `hang_nang` cộng cố định 40 triệu/tháng là `4.599 đ = 0,38×` (`0,48×` nếu khối lượng còn một nửa) [simulated]; nêu con số bất lợi `quoc_te` `22.515 đ = 1,88×` làm lý do thu hẹp phạm vi.
2. **Mục 7 và trạng thái mục 4–6 (CP2):** ba rủi ro lấy số từ A4, B1, B4: làm lại gấp đôi `6.787 đ (+51,8%)`; xem lại 100% `11.743 đ = 0,98×` (`1,03×` với 15,3 phút làm lại/ca); khối lượng còn một nửa `2.370 đ/việc`, `5.784 đ = 0,48×` [simulated]. Gửi cùng bộ số cho người viết E2 để `chi_so.md` và hồ sơ không lệch nhau.
3. **Gắn nhãn 20 ca (CP3):** gắn độc lập trong 8 phút, ghi kèm lý do theo nguyên nhân gốc cho từng ca, không xem nhãn tham khảo trong hướng dẫn. Đồng thuận với người gắn nhãn 1 là `19/20 = 95%`. Ca lệch duy nhất là ca 18: tôi gắn `Hệ thống` (tin nhắn thiếu cách tính), nhóm thống nhất `Ngữ cảnh` vì trợ lý tính đúng theo thiết kế và chính sách, chỉ giả định khách đã biết quy tắc hoàn 50%. Bộ nhãn độc lập giữ nguyên sau khi so.
4. **Rà số hồ sơ (CP4):** chạy lại `python lab13.py` và đối chiếu: D1 (`1.251`, `3.103`, `1.000`, `300`, `m ≥ 299`, power `0,64`), tỉ lệ mở lại `4,25%` toàn mẫu và `3,97%` trong phạm vi; ba chỉ số E1 (`82,83%`, `27,12%`, `4,25%`) khớp `chi_so.md`.
5. **Dòng đề xuất (CP5):** nháp **Go có điều kiện** cho pilot `noi_dia` + `hang_nang`, nêu cả con số bất lợi (xem lại 100% `0,98×`, power `0,64`), bốn điều kiện có người phụ trách và ngày kiểm tra (sửa ca 7 và ca 20; ký chấp nhận mức chênh 6 điểm; bật đủ event và thay phút simulated bằng phút đo thật; giảm xem lại theo bậc). Người viết code gộp các ý này vào bản đề xuất cuối (PR #21).

## 4. Bằng chứng

- `b0abca2` (PR #3, nhánh `cp1/ho-so-muc-1-3`): hồ sơ mục 1, 3, tên nhóm và lớp.
- `2ef02c6` (PR #6, nhánh `cp2/ho-so-muc-7`): nháp mục 7, mục 4–6 trạng thái `Chưa`.
- `6ad1797` (nhánh `cp3/c-nhan-nguoi-2`, gộp vào `bang_loi.md` qua PR #15): cột "Nhãn người 2" của 20 ca.
- `0a92aab` (nhánh `cp5/ho-so-final`, gộp vào đề xuất qua PR #21): dòng đề xuất Go có điều kiện.
- Kiểm tra cuối: lệnh `grep` tìm từ cấm (quy tắc 5) trong `report/team` không in gì; hồ sơ đủ bảy mục, mục 1, 2, 3, 7 ghi `Giả lập`.

## 5. Công cụ AI đã dùng

- **Công cụ:** Claude Code (Claude) trong VS Code.
- **Dùng vào việc gì:** đọc đề, `CHECKPOINTS.md`, `SUBMISSION.md` và tóm tắt việc của vai giữ hồ sơ theo từng checkpoint; đề xuất câu chữ cho các mục hồ sơ từ output `src/lab13.py`; tạo nhánh, commit, push theo quy ước nhánh của nhóm; chép bộ nhãn của tôi vào `bang_loi.md`. Ở CP3, AI chỉ chép 20 ca từ file đề thành phiếu trống, không gợi ý hay nhận xét nhãn nào.
- **Tự kiểm tra:** mọi con số trong hồ sơ đối chiếu với output `python lab13.py` chạy trong `src/.venv` và với số tự đối chiếu trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` (ngoài mục Nhiệm vụ C). Nhờ đối chiếu, nhóm phát hiện mục 3 ban đầu ghi `0,37×` chưa cộng 222 ca nhân viên làm thay; bản cuối dùng `0,49×` cho cả hệ thống.

## 6. Tự đánh giá

- Hoàn thành phần giữ hồ sơ: hồ sơ đủ bảy mục trước 17:00, mỗi mục có số, trạng thái và vai trò; bộ nhãn độc lập đạt đồng thuận 95%.
- Chưa tốt: ở CP2 tôi tạo nhánh hồ sơ sửa lại mục 2, 3 trong khi một thành viên khác đã sửa cùng dòng (PR #4), phải xoá nhánh và làm lại từ `main`. Lần sau cần pull `main` và hỏi nhóm trước khi sửa file mình giữ.
- Bài học: chi phí thật nằm ở giờ nhân viên chứ không ở token (`92,5%`); đề xuất được tin khi nêu cả con số bất lợi (`0,98×`, power `0,64`) cùng cách xử lý; gắn nhãn theo nguyên nhân gốc chứ không theo chỗ cần sửa (ca 18).
