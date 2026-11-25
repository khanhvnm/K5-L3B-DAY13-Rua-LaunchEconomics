# Báo cáo cá nhân — VuNamKhanh-2A202604112

## 1. Thông tin thành viên

- Họ tên: Vũ Nam Khánh
- MSSV: 2A202604112
- Email: 26ai.khanhvn@vinuni.edu.vn
- Vai trong nhóm: người viết code (kiêm quản lý repo nhóm: tạo nhánh, duyệt và merge pull request)

## 2. Phần việc phụ trách

- `src/lab13.py`: nhiệm vụ A (A1–A4) và B (B1–B4); sau đó thêm E1 và tích hợp D1 của Thành.
- `report/team/pilot_plan.yaml` (nhiệm vụ D: D2, D3).
- Quản lý git của nhóm: quy ước tên nhánh theo checkpoint, merge 21 pull request, rà soát số liệu sau mỗi lần merge.
- Rà soát chéo từng checkpoint (CP1–CP5) của cả nhóm và sửa các chỗ chưa khớp.

## 3. Đóng góp cụ thể

- **A1:** ba hàm số lần chạy kỳ vọng, tỉ lệ thành công, hệ số chi phí; qua ba phép thử 1,20 · 1,25 · 1,25.
- **A2–A4:** hàm `mo_hinh()` tính chi phí mỗi việc thành công **4.472 đ** [simulated] (tử số gồm mọi lần chạy kể cả lỗi, mẫu số 978 việc thành công), gấp 16,3 lần hoá đơn token chia số yêu cầu; tách theo `loai` (`quoc_te` 1,88×); cộng chi phí cố định cho phạm vi `noi_dia` + `hang_nang` (4.599 đ = 0,38×) [simulated].
- **B1–B4:** 9 kịch bản độ nhạy, xếp hạng làm lại (+51,8%) > xem lại (+40,7%) > lương (+23,1%); giới hạn 2 lần chạy rẻ nhất cho công ty (6.901.220 đ); xem lại 100% lên 0,98–1,03× [simulated], kèm mức hoà vốn 5,1 và 4,8 phút.
- **E1 trong code:** in ba chỉ số trong đợt chạy thử (82,83% · 27,12% · 4,25%) để số trong `chi_so.md` có nguồn từ `lab13.py`.
- **D:** `pilot_plan.yaml` chia theo nhân viên 20 + 20, `mde` 0,06 (859 mỗi nhóm, DE 6,96), ghi rõ đánh đổi power 0,64 ở mức 5 điểm, 4 luật dừng NẾU – TRONG – THÌ – KHÔNG THÌ, ngày quyết định 2027-01-11.
- **Sửa lỗi khi rà soát:**
  - Hồ sơ mục 3 so sánh 0,37× (bỏ qua 222 ca nhân viên làm thay) → sửa thành chi phí cả hệ thống 0,49×.
  - Hàm `in_e1` bị mất khi giải quyết conflict lúc merge D1 → phát hiện khi chạy lại toàn bộ file và khôi phục.
  - Bảng khắc phục dùng event `input_validation_failed` chưa có trong danh sách event → bổ sung.
- **Hỗ trợ phần của thành viên khác khi nhóm cần:** danh sách event và chỉ số tự đề xuất (`chi_so.md`, phần của Tuấn Anh ở CP2), hồ sơ mục 2, 4, 5, 6 và dòng đề xuất, bảng E2, bảng khắc phục 5 ca, `group_report.md`. Phần gắn nhãn 20 ca lỗi do hai người gắn nhãn tự làm.

## 4. Bằng chứng

| Commit / PR | Nội dung |
| --- | --- |
| `29e0109` (PR #1) | CP1: A1–A4 trong `lab13.py` |
| `eb0d5d7` (PR #2) | CP2: B1–B4 trong `lab13.py` |
| `62d24c9` (PR #4) | Sửa hồ sơ mục 3 (0,37× → 0,49×), điền mục 2 |
| `465506d` (PR #10) | Thêm E1 vào `lab13.py`, tách câu trả lời A3 |
| `e622866` (PR #11) | `chi_so.md`: event có `trace_id`, 2 chỉ số tự đề xuất |
| `7705741` (PR #12) | Bảng E2, hồ sơ mục 4, tách câu trả lời B4 |
| `8ee0b0b`, `f9da891` (PR #14) | Khôi phục `in_e1`; `pilot_plan.yaml` |
| `3b8b8f0` (PR #15), `3270d50` (PR #16), `30d9b53` (PR #18) | Bảng khắc phục 5 ca; hồ sơ mục 5, 6; event `input_validation_failed` |
| `36b3528` (PR #20), `0deb81a` (PR #21) | Đề xuất Go có điều kiện, `group_report.md` |

Kiểm tra: `cd src && python lab13.py` chạy hết, in `Ba phép thử đáp án biết trước: ĐẠT` và các bảng A, B, E1, D1.

## 5. Công cụ AI đã dùng

- **Công cụ:** Claude Code (Anthropic) trong VS Code.
- **Dùng vào việc gì:** đọc đề và lập kế hoạch chia việc; viết code A1–A4, B1–B4, E1 trong `lab13.py`; soạn `pilot_plan.yaml`, bảng E2, danh sách event, các dòng hồ sơ và `group_report.md`; rà soát từng checkpoint, phát hiện lỗi (0,37×, mất `in_e1` khi merge, thiếu event); tạo nhánh và commit.
- **Không dùng AI để:** gắn nhãn 20 ca lỗi (hai người gắn nhãn tự làm độc lập) và chấm phiếu duyệt chéo.
- **Cách tự kiểm tra:**
  - Chạy `python lab13.py` sau mỗi thay đổi và sau mỗi lần merge; ba phép thử A1 phải ĐẠT.
  - Đối chiếu mọi số A, B, D1, E1 với bảng số tự đối chiếu trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` (lệch ≤ 2%).
  - Người kiểm số (Thành) tính tay độc lập dòng `run_00001` (187,7 đ token, 75 đ tool) và các phép thử A1.
  - Kiểm tra mỗi "giảm một nửa" bằng nửa mức tăng của "gấp đôi" (B1); tính lại tay cặp B2 (5,6% + 40,7% = 46,3%).
  - `yaml.safe_load` đọc được `pilot_plan.yaml`, không còn dấu `?` ngoài chú thích; dùng `grep` kiểm tra thư mục `report/team` không có từ bị cấm theo quy tắc 5.

## 6. Tự đánh giá

- **Làm tốt:** hoàn thành phần code đúng hạn checkpoint, số khớp đáp án; giữ repo có thứ tự (mỗi checkpoint một nhánh, merge qua pull request); rà soát chéo bắt được lỗi so sánh 0,37× và lỗi mất code khi merge trước khi nộp.
- **Chưa tốt:** phụ thuộc nhiều vào AI để viết code và văn bản; một số phần của thành viên khác do tôi làm thay thay vì để họ tự làm. Lỗi mất `in_e1` cho thấy tôi chưa chạy lại toàn bộ file ngay sau khi giải quyết conflict.
- **Rút kinh nghiệm:** tự viết lại được công thức A1 và `mo_hinh()` không cần AI; luôn chạy lại toàn bộ `lab13.py` sau mỗi merge; để từng thành viên tự hoàn thành phần của mình và chỉ hỗ trợ rà soát.
- **Tự giải thích được:** vì sao tử số tính mọi lần chạy còn mẫu số chỉ đếm việc thành công; cách tính cỡ mẫu hiệu dụng khi chia theo cụm (c × m ÷ (1 + (m − 1) × ICC) < c ÷ ICC); lý do đề xuất Go có điều kiện.
