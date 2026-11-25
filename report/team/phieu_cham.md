# Phiếu chấm hội đồng Gate 2a

- Nhóm chấm (hội đồng): Rua (L3B)
- Nhóm được chấm: ABC (L3B)

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | 10 | Go có điều kiện khớp số của nhóm: phạm vi 0,38× của 12.000 đ (0,48× ở nửa khối lượng) [simulated]. Nêu đủ con số bất lợi kèm cách xử lý: xem lại 100% → 11.742,79–12.414,50 đ (0,98–1,03×) → điều kiện 4 hạ xem lại theo bậc; power 0,64 ở mức 5 điểm → điều kiện 3 Giám đốc vận hành ký chấp nhận; thiếu bộ nhãn thứ hai → mục 5 ghi "Chưa" và đưa vào điều kiện 2 |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | 10 | Mọi số có giờ nhân viên ghi `simulated` (4.471,97 đ, 16,28×, bảng độ nhạy, B4, A4); mục 4 không dùng cột giả lập nên ghi "Xong, có bằng chứng". Phạm vi thu hẹp về `noi_dia` (0,22×) + `hang_nang` (0,69×), loại `quoc_te` (1,88×, thành công 27,3%, tỉ lệ ok 30,0% → 11,4% → 2,2%) và `doi_tac` (0,85×) |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | 10 | Đối chứng ngẫu nhiên 20 + 20 nhân viên, phân tầng 12 depot, đủ 20 cụm; loại chia theo depot (trần 300) và theo đơn (tràn tác động). Đủ mẫu cho mức 6 điểm: m ≥ 299, DE 6,96, 859 hiệu dụng. 3 luật dừng đủ 4 vế, có ngưỡng (6%, +2 điểm từ 10 người, 8.000 đ, 40%), thời hạn (2 tuần, 1 tuần) và người dừng (Giám đốc vận hành, rollback 30 phút) |
| **Tổng** | | | | **30 / 30** | |

**Quyết định của hội đồng:** Go có điều kiện

**Lý do:** Hồ sơ khớp bằng chứng ở cả ba tiêu chí: phạm vi pilot rẻ hơn rõ (0,38×, simulated), con số bất lợi được nêu công khai và có điều kiện xử lý, pilot có đối chứng ngẫu nhiên đủ 20 cụm mỗi nhóm. Lịch thời gian (câu hỏi bên dưới) đã được đội trình làm rõ: điều kiện 1 và 3 chốt 28/11/2026, pilot chạy 30/11–31/12/2026, quyết định 05/01/2027. Góp ý không trừ điểm: luật dừng chi phí ghi "không thì cấm mở hang_nang" trong khi `hang_nang` đã nằm trong phạm vi từ đầu; điều kiện 4 nên có ngưỡng đo được (tỉ lệ được xem lại, phút mỗi lần, ví dụ ≤ 4,8 phút) và một luật dừng tương ứng; điều kiện 2 và 4 nên ghi một vai trò phụ trách thay vì hai.

**Một câu hỏi cho đội trình:** Ngày bắt đầu pilot là ngày nào? Điều kiện 1 có hạn "không muộn hơn 05/01/2027", trùng ngày quyết định. Theo hồ sơ, pilot cần 2 tuần rollout + ≥ 10 ngày ở bước 50% + 7 ngày theo dõi, khoảng 5 tuần. Nếu vá lỗi xong ngày 05/01 thì pilot chạy lúc nào?

**Câu trả lời của đội trình (ghi lại tại buổi):** Mốc 05/01/2027 là ngày quyết định toàn đợt pilot; điều kiện 1 (vá ca 7 và ca 20, bật 10 event) bắt buộc xong **trước** ngày bật pilot, không chờ đến 05/01. Tính lùi từ ngày quyết định:

- 28/11/2026: hạn chốt điều kiện 1 và 3 (vá khoá chống trùng, đối soát sổ cái, bật 10 event, Giám đốc vận hành ký duyệt).
- 30/11 → 07/12 (7 ngày): bắt đầu pilot, bước 0.10 (4 nhân viên).
- 07/12 → 14/12 (7 ngày): bước 0.25 (10 nhân viên); hoàn tất điều kiện 2 trước khi lên bước này.
- 14/12 → 24/12 (10 ngày): bước 0.50 (20 nhân viên), gom đủ m ≥ 299 đơn mỗi người trong phạm vi `noi_dia` + `hang_nang`.
- 24/12 → 31/12 (7 ngày): cửa sổ 7 ngày không mở lại của đơn cuối cùng; tổng 31 ngày, còn 5 ngày đệm (01/01–04/01) để tổng hợp số liệu và họp quyết định ngày 05/01/2027.
- Cơ chế chốt cứng: nếu ngày 28/11 chưa qua kiểm tra vá lỗi thì không bật pilot, lùi đồng thời ngày bắt đầu và ngày quyết định theo đúng chu kỳ 31 ngày cộng đệm; không cắt bớt thời gian gom mẫu hay 7 ngày theo dõi.
