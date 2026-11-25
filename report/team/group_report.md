# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: Rua
- Lớp: L3B
- Thành viên: xem `TEAM.md`

## 2. Mục tiêu và cách tiếp cận

Dựng hồ sơ launch v0 cho trợ lý hoàn phí LogiX-VN để hội đồng Gate 2a duyệt **kế hoạch pilot**, trả lời bốn câu: có đáng chạy không, nhân viên có dùng không, khi hỏng thì sao, pilot thiết kế thế nào để ra được quyết định.

Cách tiếp cận: mọi con số do `src/lab13.py` tính từ hai file CSV (A, B, E1, D1); người kiểm số tính tay đối chiếu; mỗi checkpoint một nhánh git, merge qua pull request; mọi số từ cột `_simulated` ghi nhãn `simulated`.

## 3. Giải pháp

| Nhiệm vụ | Cách làm | File |
| --- | --- | --- |
| A · Chi phí mỗi việc thành công | Tử số cộng token + tool của mọi lần chạy (kể cả lỗi) + phút xem lại, làm lại; mẫu số chỉ đếm việc thành công; tách theo `loai`; cộng chi phí cố định 40 triệu/tháng | [bang_chi_phi.md](bang_chi_phi.md) |
| B · Độ nhạy | Gọi lại `mo_hinh()` cho 9 kịch bản, 1 cặp, giới hạn 1/2/3 lần chạy (chi phí cả hệ thống), xem lại 100% | [bang_chi_phi.md](bang_chi_phi.md) |
| C · Bảng lỗi | Hai người gắn nhãn độc lập 20 ca theo năm loại Google PAIR, thống nhất ca lệch, bảng khắc phục 5 ca | [bang_loi.md](bang_loi.md) |
| D · Pilot plan | Tính cỡ mẫu theo yêu cầu, nhân viên, depot rồi mới chọn cách chia; luật dừng dựa trên tỉ lệ hiện tại | [pilot_plan.yaml](pilot_plan.yaml) |
| E · Chỉ số, rủi ro, hồ sơ | Tính thử 3 chỉ số, 11 event có `trace_id`, 3 rủi ro lấy số từ bảng độ nhạy, hồ sơ một trang | [chi_so.md](chi_so.md), [ho_so_launch_v0.md](ho_so_launch_v0.md) |

## 4. Kết quả

- Chi phí mỗi việc thành công **4.472 đ** [simulated], gấp 16,3 lần hoá đơn token + tool chia số yêu cầu; giờ nhân viên chiếm 92,5%.
- So với nhân viên tự làm 12.000 đ: toàn mẫu (tính cả 222 ca nhân viên làm thay) 0,49×; phạm vi `noi_dia` + `hang_nang` cộng cố định 0,38× [simulated]. `quoc_te` 1,88× nên loại khỏi pilot.
- Ba yếu tố nhạy nhất: số ca làm lại (+51,8%), tỉ lệ xem lại (+40,7%), lương nhân viên (+23,1%) [simulated]. Xem lại 100% đưa chi phí lên 0,98–1,03× [simulated].
- Chỉ số trong đợt chạy thử: chính 82,83%, bỏ qua gợi ý 27,12%, mở lại 7 ngày 4,25% (không có đối chứng).
- Bảng lỗi: đồng thuận 19/20 = 95%, ca 18 thống nhất là Ngữ cảnh.
- Pilot: chia theo nhân viên 20 + 20, mde 0,06 (859 mỗi nhóm, DE 6,96); power 0,64 nếu tác động thật là 5 điểm.
- **Đề xuất cuối: Go có điều kiện** (4 điều kiện, xem `ho_so_launch_v0.md`).
- Kết quả duyệt chéo nhóm nhận được từ hội đồng: điền sau buổi duyệt chéo (điểm /30, quyết định, câu hỏi và câu trả lời).

## 5. Khó khăn và cách xử lý

- So sánh với 12.000 đ ban đầu ghi 0,37× (4.472 / 12.000), bỏ qua 222 ca nhân viên làm thay; đã sửa thành chi phí cả hệ thống 0,49× (PR #4).
- Khi merge nhánh D1, giải quyết conflict làm mất hàm `in_e1` trong `lab13.py`; phát hiện khi chạy lại toàn bộ file, đã khôi phục (PR #14). Từ đó, sau mỗi merge đều chạy lại `python lab13.py`.
- Bảng khắc phục dùng event `input_validation_failed` chưa có trong danh sách event; đã bổ sung để mọi cách phát hiện đều đo được (PR #18).
- Console Windows lỗi khi in tiếng Việt; thêm `sys.stdout.reconfigure(encoding='utf-8')` để file chạy được trên mọi máy trong nhóm.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md`.

## 7. Hạn chế và hướng cải thiện

- Mọi chi phí có giờ nhân viên dựa trên phút giả lập; pilot phải thay bằng phút đo thật từ `staff_review_decision` và `staff_rework_completed` sau tuần 1.
- Đợt chạy thử không có nhóm đối chứng, nên chưa kết luận được tác động của trợ lý lên chỉ số chính.
- Với 40 nhân viên, pilot chỉ đủ mẫu cho mức chênh 6 điểm; nếu tác động thật là 5 điểm, power chỉ 0,64. Hướng cải thiện: kéo dài bước 0.50 hoặc gộp thêm nhân viên nếu LogiX-VN tuyển thêm.
- ICC 0,02 là giả định của đề; cần ước lượng lại từ dữ liệu pilot.

## 8. Tài liệu tham khảo

- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, arxiv.org/abs/2504.13359
- Google PAIR, *People + AI Guidebook*, chương "Errors + Graceful Failure", pair.withgoogle.com
- Tài liệu statsmodels, `NormalIndPower` (`statsmodels.stats.power`)
- Đề bài và hướng dẫn Lab 13 trong `docs/`
