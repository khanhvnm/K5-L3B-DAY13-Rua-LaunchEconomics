# Team

## Thông tin nhóm

- Tên nhóm: Rua
- Lớp: L3B
- Repo nhóm: `K5-L3B-DAY13-Rua-LaunchEconomics`
- URL repo, nhánh nộp, commit chốt: https://github.com/khanhvnm/K5-L3B-DAY13-Rua-LaunchEconomics · nhánh `main` · commit chốt: `25a48ff`

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Vũ Nam Khánh | 2A202604112 | 26ai.khanhvn@vinuni.edu.vn | khanhvnm | Người viết code |
|   2 | Phạm Duy Thành | 2A202604075 | 26ai.thanhpd2@vinuni.edu.vn | thanhtey1234 | Người kiểm số |
|   3 | Nguyễn Tuấn Anh | 2A202604089 | 26ai.anhnt14@vinuni.edu.vn | TuanAnhNg131 | Người gắn nhãn 1 |
|   4 | Đào Hồng Thắng | 2A202604076 |26ai.thangdh2@vinuni.edu.vn |myblue-ai| Người gắn nhãn 2, kiêm giữ hồ sơ |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.


## VuNamKhanh-2A202604112

### Phần việc phụ trách

- Người viết code: `src/lab13.py` nhiệm vụ A (A1–A4), B (B1–B4), E1; tích hợp D1 của Thành.
- `pilot_plan.yaml` (D2, D3); quản lý repo nhóm (nhánh theo checkpoint, duyệt và merge pull request); rà soát chéo CP1–CP5.

### Đóng góp cụ thể

- A1 qua ba phép thử (1,20 · 1,25 · 1,25); `mo_hinh()` tính chi phí mỗi việc thành công 4.472 đ, gấp 16,3 lần hoá đơn token + tool; `quoc_te` 1,88×; phạm vi `noi_dia` + `hang_nang` cộng cố định 0,38× [simulated].
- B1–B4: xếp hạng làm lại +51,8% > xem lại +40,7% > lương +23,1%; giới hạn 2 lần chạy rẻ nhất; xem lại 100% lên 0,98–1,03×, hoà vốn 5,1 và 4,8 phút [simulated].
- `pilot_plan.yaml`: chia theo nhân viên 20 + 20, mde 0,06 (859 mỗi nhóm, DE 6,96), power 0,64 ở mức 5 điểm, 4 luật dừng, ngày quyết định 2027-01-11.
- Sửa lỗi khi rà soát: so sánh 0,37× → 0,49× cả hệ thống; khôi phục `in_e1` mất khi merge; bổ sung event `input_validation_failed`. Hỗ trợ hồ sơ mục 2, 4, 5, 6, bảng E2, bảng khắc phục, dòng đề xuất và `group_report.md`.

### Bằng chứng

- PR #1 (`29e0109`) A1–A4; PR #2 (`eb0d5d7`) B1–B4; PR #4 (`62d24c9`) sửa 0,49×; PR #10 (`465506d`) E1; PR #14 (`8ee0b0b`, `f9da891`) khôi phục `in_e1`, `pilot_plan.yaml`; PR #20, #21 (`36b3528`, `0deb81a`) đề xuất và `group_report.md`.
- Báo cáo cá nhân: `report/team/2A202604112_VuNamKhanh.md`.

## PhamDuyThanh-2A202604075

### Phần việc phụ trách

- Người kiểm số (CP1–CP2): tính tay đối chiếu và điền `bang_chi_phi.md` phần A1–A4, B1–B4.
- Người viết code sau giải lao (CP3): nhiệm vụ D1 trong `src/lab13.py`.
- CP5: rà nhãn `simulated`, rà từ cấm, chạy lại `lab13.py` trên máy thứ hai.

### Đóng góp cụ thể

- Tính tay A1 (1,20 · 1,25 · 1,25), dòng `run_00001` (187,694 đ token + 75 đ tool = 262,694 đ, khớp `mo_hinh`), ca lỗi `RF-70008` (710,552 đ vào tử số, 0 việc thành công); kiểm tra đối xứng B1.
- Điền đủ bảng A2–A4 và B1–B4 trong `bang_chi_phi.md` (4.472 đ; 0,49×; 0,38×; B3 2 lần chạy 6.901.220 đ; B4 0,98–1,03×) [simulated].
- Viết `co_mau`, `he_so_thiet_ke`, `co_mau_hieu_dung`, `so_yc_moi_cum_toi_thieu`, `in_d1`: 1.251; 3.103 → 42 nhân viên/nhóm; trần 1.000 và 300; m ≥ 299, DE 6,96; power 0,64; nền mở lại 4,25% / 3,97%.

### Bằng chứng

- Nhánh `cp1/a-bang-chi-phi`, `cp2/b-bang-chi-phi` (`bang_chi_phi.md`); `cp3/d1-sample-size` (D1 trong `src/lab13.py`).
- Báo cáo cá nhân: `report/team/2A202604075_PhamDuyThanh.md`.

## NguyenTuanAnh-2A202604089

### Phần việc phụ trách

- Người gắn nhãn 1 (CP3): gắn nhãn độc lập 20 ca lỗi, so với người gắn nhãn 2, hoàn thiện `bang_loi.md`.
- Nhiệm vụ E1 (CP1, CP2, CP4): ba chỉ số, danh sách event có `trace_id`, kiểm tra chéo trong `chi_so.md`.
- CP5: tham gia tổng hợp `group_report.md`.

### Đóng góp cụ thể

- Tính ba chỉ số trong đợt chạy thử: chính 82,83% (994/1.200), bỏ qua gợi ý 27,12% (48/177), mở lại 7 ngày 4,25% (51/1.200), 3,97% (39/982) trong phạm vi; ghi đúng là không có đối chứng.
- Đề xuất 1 chỉ số dùng và 1 chỉ số an toàn (`audit_sample_checked`); 11 event có `trace_id`; kiểm tra chéo mọi chỉ số E1 và cách phát hiện lỗi ở CP3 đều đo được từ event.
- Gắn nhãn 20 ca theo nguyên nhân gốc; đồng thuận 19/20 = 95%; quy tắc phân biệt ca 18 (Ngữ cảnh); bảng khắc phục 5 ca (9, 7, 18, 4, 17).

### Bằng chứng

- PR #8 (`bd2e5ed`, `cp1/e1-chi-so`); PR #11 (`e622866`, `cp2/e1-events`); PR #17 (`4a0ef3d`, `cp3/tuananh-c-bang-loi`, cùng PR #15, #18).
- Báo cáo cá nhân: `report/team/2A202604089_NguyenTuanAnh.md`.

## DaoHongThang-2A202604076

### Phần việc phụ trách

- Người giữ hồ sơ: điền `ho_so_launch_v0.md` theo từng checkpoint, chốt dòng đề xuất.
- Người gắn nhãn 2 (CP3): gắn nhãn độc lập 20 ca lỗi.
- CP4: rà số hồ sơ mục 4, 5, 6 với `chi_so.md`, `bang_loi.md`, `pilot_plan.yaml` và output `lab13.py`.

### Đóng góp cụ thể

- Hồ sơ mục 1 (4.472 đ, 16,3 lần, 92,5% là giờ nhân viên) và mục 3 (0,38×, 0,48×; `quoc_te` 1,88×) [simulated].
- Mục 7: ba rủi ro kinh tế (làm lại gấp đôi +51,8%; xem lại 100% 0,98–1,03×; khối lượng còn nửa 0,48×) [simulated]; đánh dấu mục 4–6 `Chưa` kèm vai trò.
- Gắn nhãn độc lập 20 ca, đồng thuận 19/20 = 95%; ca 18 thống nhất là Ngữ cảnh.
- Nháp đề xuất Go có điều kiện với bốn điều kiện, người phụ trách và ngày kiểm tra (gộp vào PR #21).

### Bằng chứng

- PR #3 (`b0abca2`) mục 1, 3; PR #6 (`2ef02c6`) mục 7; `6ad1797` (`cp3/c-nhan-nguoi-2`, gộp qua PR #15) nhãn người 2; `0a92aab` (`cp5/ho-so-final`, gộp qua PR #21) dòng đề xuất.
- Báo cáo cá nhân: `report/team/2A202604076_DaoHongThang.md`.
