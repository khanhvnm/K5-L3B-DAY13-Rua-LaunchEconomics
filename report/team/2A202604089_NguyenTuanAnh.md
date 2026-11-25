# Báo cáo cá nhân — NguyenTuanAnh-2A202604089

## 1. Thông tin thành viên

- Họ tên: Nguyễn Tuấn Anh
- MSSV: 2A202604089
- Email: 26ai.anhnt14@vinuni.edu.vn
- GitHub: `TuanAnhNg131`
- Vai trong nhóm: Người gắn nhãn 1 (CP3 · Nhiệm vụ C), Phụ trách đặc tả chỉ số & thiết kế event (CP1, CP2, CP4 · Nhiệm vụ E1), Tổng hợp báo cáo nhóm (CP5)

## 2. Phần việc phụ trách

- **CP1 (`cp1/e1-chi-so`):** Tính thử 3 chỉ số (chính, mức độ sử dụng, an toàn) và tỉ lệ mở lại trong 7 ngày (`mo_lai_trong_7_ngay`) trên mẫu 1.200 yêu cầu và trong phạm vi pilot (`noi_dia` + `hang_nang`) từ `src/logix_requests.csv`; điền bảng E1 trong `report/team/chi_so.md` và cập nhật thông tin thành viên trong `TEAM.md`.
- **CP2 (`cp2/e1-events`):** Thiết kế danh sách sự kiện (event) có `trace_id` để nối với trace của agent và thực hiện kiểm tra chéo (cross-check) giữa từng chỉ số ở bảng E1 với các event dùng để đo trong `report/team/chi_so.md`.
- **CP3 (`cp3/tuananh-c-bang-loi`):** Đọc và gắn nhãn độc lập 20 ca lỗi theo 5 phân loại của Google PAIR (vai trò Người gắn nhãn 1); ghép và đối chiếu với bộ nhãn độc lập của Người gắn nhãn 2 (Đào Hồng Thắng), tính tỉ lệ đồng thuận, viết quy tắc phân biệt cho ca không trùng và hoàn thiện bảng khắc phục cho 5 ca đại diện trong `report/team/bang_loi.md`.
- **CP4 (Hoàn thiện E1 trong `chi_so.md`):** Hoàn thiện đặc tả 2 chỉ số tự đề xuất (1 chỉ số dùng, 1 chỉ số an toàn) và đồng bộ danh sách 11 event có `trace_id` (bổ sung `input_validation_failed`) để mọi chỉ số ở E1 và mọi cách phát hiện lỗi ở CP3 đều đo được bằng dữ liệu.
- **CP5 (`group_report.md` & `report/tuananh-ca-nhan`):** Tổng hợp kết quả các nhiệm vụ A–E vào `report/team/group_report.md`, rà soát điều kiện "Xong khi" của các checkpoint và hoàn thiện báo cáo cá nhân `report/team/2A202604089_NguyenTuanAnh.md`.

## 3. Đóng góp cụ thể

1. **Tính thử 3 chỉ số và tỉ lệ mở lại nền trên `src/logix_requests.csv` (CP1 · Nhiệm vụ E1):**
   - **Chỉ số chính (`% yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày`):** Đếm các dòng thỏa mãn `dong_trong_24h == 1` và `mo_lai_trong_7_ngay == 0` được `994 / 1.200` yêu cầu $= \mathbf{82,83\%}$.
   - **Chỉ số dùng (`Tỉ lệ bỏ qua gợi ý`):** Trên `177` yêu cầu được xem lại (`duoc_xem_lai == 1`), đếm số yêu cầu có `quyet_dinh_xem_lai` là `sua` hoặc `bo` được `48 / 177` yêu cầu $= \mathbf{27,12\%}$.
   - **Chỉ số an toàn (`Tỉ lệ lỗi lọt đến khách — mở lại trong 7 ngày`):** Đếm các dòng có `mo_lai_trong_7_ngay == 1` được `51 / 1.200` yêu cầu $= \mathbf{4,25\%}$ trên toàn mẫu; tính riêng trong phạm vi pilot `noi_dia` + `hang_nang` (`982` yêu cầu) là `39 / 982` $= \mathbf{3,97\%}$ (cung cấp mốc nền để nhóm đặt luật dừng an toàn ở nhiệm vụ D, tránh đặt ngưỡng tuyệt đối 3% làm dừng pilot ngay tuần đầu).
   - Viết nhận xét tuân thủ đúng quy tắc nhân quả: ghi nhận *"chỉ số trong đợt chạy thử là..."*, không kết luận trợ lý đã nâng chỉ số vì đợt chạy thử không có nhóm đối chứng.
2. **Thiết kế hệ thống event có `trace_id`, đề xuất chỉ số mới và kiểm tra chéo (CP2 & CP4 · Nhiệm vụ E1):**
   - Đề xuất thêm **1 chỉ số dùng** (`% yêu cầu của nhóm trợ lý được nhân viên mở gợi ý`: nối `refund_request_created` có `arm = tro_ly` với `agent_suggestion_shown` qua `trace_id`) và **1 chỉ số an toàn** (`% đơn hoàn sai tiền qua kiểm tra mẫu hằng tuần`: lấy từ `audit_sample_checked` với mẫu 100 đơn/tuần để bắt lỗi ngầm).
   - Đặc tả đầy đủ **11 event** có `trace_id` bao phủ toàn bộ vòng đời xử lý yêu cầu: `refund_request_created`, `input_validation_failed`, `agent_run_completed`, `agent_suggestion_shown`, `staff_review_decision`, `staff_rework_completed`, `handoff_to_staff`, `refund_ledger_write`, `ticket_closed`, `ticket_reopened`, `audit_sample_checked`.
   - Thực hiện kiểm tra chéo (cross-check) chứng minh cả 5 chỉ số bảng E1, các cơ chế phát hiện lỗi ở CP3 và bài toán tính chi phí thực tế (thay số phút `simulated` bằng `phut_xem_lai` và `phut_lam_lai` đo thật trong pilot) đều tính được trực tiếp từ danh sách event.
3. **Gắn nhãn độc lập 20 ca lỗi Google PAIR và thiết kế bảng khắc phục 5 ca (CP3 · Nhiệm vụ C):**
   - Thực hiện gắn nhãn độc lập 20 ca lỗi theo nguyên nhân gốc vào 5 nhóm: **Do người dùng** (ca 1, 6, 9, 14), **Hệ thống** (ca 2, 7, 8, 15, 20), **Ngữ cảnh** (ca 3, 10, 16, 18), **Giới hạn hệ thống** (ca 4, 11, 13, 19) và **Ngầm** (ca 5, 12, 17).
   - Đối chiếu với bộ nhãn độc lập của Đào Hồng Thắng (Người gắn nhãn 2): đạt tỉ lệ đồng thuận **19 / 20 = 95,0%** (vượt ngưỡng yêu cầu $\ge 80\%$).
   - Viết quy tắc phân biệt rõ ràng cho ca không trùng (**Ca 18**: trợ lý tính đúng `30.000 đ × 50% = 15.000 đ` theo chính sách giao trễ nên không phải lỗi `Hệ thống`, gốc lỗi là giả định khách đã biết quy tắc 50% không khớp hoàn cảnh thực tế $\Rightarrow$ thống nhất nhãn **Ngữ cảnh**) cùng các quy tắc cho ca dễ lẫn (ca 6, 9; ca 8, 15 vs. ca 5, 12, 17; ca 13).
   - Xây dựng bảng khắc phục cho 5 ca đại diện đủ 5 loại lỗi (**Ca 9 · Do người dùng**, **Ca 7 · Hệ thống**, **Ca 18 · Ngữ cảnh**, **Ca 4 · Giới hạn hệ thống**, **Ca 17 · Ngầm**), mỗi ca đều chỉ rõ event phát hiện, ngưỡng cảnh báo, tần suất đo và một vai trò phụ trách duy nhất (`PM trợ lý hoàn phí`, `Kỹ sư trưởng agent`, `Trưởng nhóm CSKH`, `Kế toán trưởng`).
4. **Tổng hợp báo cáo nhóm (CP5):**
   - Tham gia tổng hợp kết quả từ 5 nhiệm vụ A–E, các khó khăn kỹ thuật (bổ sung chi phí cả hệ thống `0,49×` [`simulated`], đồng bộ event `input_validation_failed`, xử lý conflict hàm `in_e1`) và hạn chế của đợt chạy thử vào `report/team/group_report.md`.

## 4. Bằng chứng

- Nhánh `cp1/e1-chi-so` (commit `bd2e5ed`, PR `#8`): tính thử 3 chỉ số và tỉ lệ mở lại trong `report/team/chi_so.md`, cập nhật thông tin trong `TEAM.md`.
- Nhánh `cp2/e1-events` (commit `e622866`, PR `#11`): bổ sung danh sách event có `trace_id`, 2 chỉ số tự đề xuất và mục kiểm tra chéo trong `report/team/chi_so.md`.
- Nhánh `cp3/tuananh-c-bang-loi` (commit `4a0ef3d`, PR `#17`, kết hợp PR `#15` và PR `#18`): hoàn thiện bảng 2 bộ nhãn độc lập, tỉ lệ đồng thuận `19/20 = 95,0%`, quy tắc phân biệt ca 18 và bảng khắc phục 5 ca trong `report/team/bang_loi.md`.
- Hồ sơ tổng hợp: `report/team/chi_so.md`, `report/team/bang_loi.md`, `report/team/group_report.md` và `report/team/2A202604089_NguyenTuanAnh.md`.

## 5. Công cụ AI đã dùng

- **Công cụ:** Trợ lý AI Google Antigravity.
- **Mục đích sử dụng:** Hỗ trợ phân tích bảng phân công nhóm theo từng checkpoint, kiểm tra nhanh lệnh Python đọc `src/logix_requests.csv` để đối chiếu số lượng yêu cầu của 3 chỉ số E1, rà soát cấu trúc bảng sự kiện (event) và chuẩn hóa cách diễn đạt quy tắc phân biệt 5 loại lỗi theo khung Google PAIR.
- **Cách tự kiểm tra kết quả:** Tự kiểm tra lại điều kiện lọc trên `src/logix_requests.csv` (lưu ý đọc CSV với `keep_default_na=False` để không làm sai các ô trống của cột `quyet_dinh_xem_lai`; kiểm tra `994/1.200 = 82,83%`, `48/177 = 27,12%`, `51/1.200 = 4,25%`, `39/982 = 3,97%`); tự đọc từng ca trong 20 ca lỗi để xác định nguyên nhân gốc trước khi đối chiếu với Người gắn nhãn 2; kiểm tra chéo từng chỉ số trong `chi_so.md` và từng dòng phát hiện lỗi trong `bang_loi.md` để đảm bảo mọi event đều có `trace_id` và khớp tên.

## 6. Tự đánh giá

- Hoàn thành đầy đủ, chính xác và đúng tiến độ toàn bộ các nhiệm vụ của vai trò Người gắn nhãn 1 xuyên suốt 5 checkpoint (CP1 → CP5), phối hợp nhịp nhàng với Người gắn nhãn 2 (Thắng) và các thành viên viết code/kiểm số (Khánh, Thành) qua từng nhánh Git riêng biệt.
- Bài học chính rút ra từ lab:
  1. Một chỉ số chỉ thật sự có giá trị vận hành khi được ánh xạ (mapping) tường minh sang các sự kiện (event) có `trace_id` — đặc biệt trong pilot phải ghi nhận phút xem lại (`staff_review_decision`) và phút làm lại (`staff_rework_completed`) thật để thay thế hoàn toàn các ước lượng `simulated`.
  2. Khi phân loại lỗi của hệ thống AI theo Google PAIR, phải phân loại theo **nguyên nhân gốc** thay vì theo chỗ cần sửa, đồng thời tách bạch lỗi `Hệ thống` (đã lộ ra) với lỗi `Ngầm` (chỉ bắt được nhờ kiểm tra mẫu định kỳ như `audit_sample_checked`).
  3. Không được kết luận nhân quả (*"trợ lý đã nâng chỉ số"*) từ dữ liệu chạy thử chưa có nhóm đối chứng, và mọi ngưỡng dừng an toàn trong kế hoạch pilot phải được đặt dựa trên mức nền thực tế (`4,25%` toàn mẫu, `3,97%` trong phạm vi) kết hợp so sánh với nhóm đối chứng.
