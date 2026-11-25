# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/lab13.py`. Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 (ĐẠT) |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 (ĐẠT) |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 (ĐẠT) |

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 | `logix_runs.csv` | đo từ trace |
| Tool | 84.000 | `logix_runs.csv` (5.600 lần gọi) | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 | attempt lớn hơn 1 | đo từ trace |
| Xem lại | 1.780.000 | `phut_xem_lai_simulated` (890 phút) | simulated |
| Làm lại | 2.264.000 | `phut_lam_lai_simulated` (1.132 phút) | simulated |
| Tổng chi phí | 4.373.585 | token + tool + xem lại + làm lại | có phần simulated |
| Số việc thành công | 978 | `ket_qua == 'thanh_cong'` | đo từ dữ liệu |
| Chi phí mỗi việc thành công | 4.472 | 4.373.585 ÷ 978 | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,7 | 329.585 ÷ 1.200 | đo từ trace |

- Chi phí mỗi việc thành công (`4.472 đ` [`simulated`]) gấp **16,3 lần** hoá đơn token + tool chia số yêu cầu (`274,7 đ`). Nếu tính đủ cả hệ thống gồm 222 ca nhân viên làm thay (× 12.000 đ) trên 1.200 yêu cầu thì chi phí là **5.865 đ/yêu cầu = 0,49×** của 12.000 đ (`simulated`).
- Khoản chiếm tỉ trọng lớn nhất là **làm lại với 51,8%** (`2.264.000 đ` [`simulated`]), tiếp theo là **xem lại với 40,7%** (`1.780.000 đ` [`simulated`]). Tổng thời gian nhân viên chiếm **92,5%** tổng chi phí, còn token và tool chỉ chiếm **7,5%**.

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 đ (simulated) | 0,22× (simulated) |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 đ (simulated) | 0,69× (simulated) |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 đ (simulated) | 1,88× (simulated) |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 đ (simulated) | 0,85× (simulated) |

- Loại không đáng để trợ lý xử lý là `quoc_te`: `22.515 đ = 1,88×` của 12.000 đ [`simulated`], thành công chỉ `27,3%`.
- Chạy lại tới 3 lần không giúp `quoc_te`: tỉ lệ `ok` giảm từ `30,0%` (lần 1) xuống `11,4%` (lần 2) và `2,2%` (lần 3), lỗi lặp lại nên chạy thêm chỉ tốn tiền.
- `doi_tac` sát ngưỡng (`10.215 đ = 0,85×` [`simulated`], thành công `54,4%`) và có điều khoản riêng nên cũng loại khỏi phạm vi pilot.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | 4.599 đ (simulated) | 0,38× (simulated) |
| Một nửa khối lượng | 16.875 | 2.370 đ | 5.784 đ (simulated) | 0,48× (simulated) |

- Chi phí cố định 40 triệu đ/tháng không đổi kết luận ở quy mô `45.000` yêu cầu/tháng (`4.599 đ = 0,38×` [`simulated`]) hay một nửa khối lượng (`5.784 đ = 0,48×` [`simulated`]). Tuy nhiên chi phí cố định mỗi việc tăng mạnh khi khối lượng nhỏ và sẽ vượt 12.000 đ nếu tổng lượng yêu cầu tụt dưới khoảng `6.212` yêu cầu/tháng (`4.659` việc thành công/tháng, `simulated`).

## B1 · Đổi từng yếu tố

| Kịch bản | Cách tính | Chi phí mỗi việc thành công | Thay đổi (%) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | 4.723 đ (simulated) | +5,6% |
| Giá token giảm một nửa | 13 đ và 65 đ | 4.346 đ (simulated) | −2,8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 đ (simulated) | +40,7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 đ (simulated) | −20,3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 đ (simulated) | +51,8% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 đ (simulated) | −25,9% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 đ (simulated) | +23,1% |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có attempt > 2; yêu cầu có so_lan_chay > 2 coi là chuyen_nhan_vien | 4.237 đ (simulated) | −5,2% |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | 4.111 đ (simulated) | −8,1% |

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: **6.543 đ (`simulated`)**, tăng `+46,3%` so với gốc `4.472 đ` (`simulated`), đúng bằng tổng hai tác động riêng (`+5,6% + 40,7% = +46,3%`) vì mô hình cộng tuyến tính.
- Xếp hạng ba yếu tố ảnh hưởng mạnh nhất: **1. Số ca làm lại (`+51,8%` [`simulated`]) · 2. Tỉ lệ xem lại (`+40,7%` [`simulated`]) · 3. Lương nhân viên (`+23,1%` khi tăng 25% [`simulated`])**.

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

| Giới hạn | Tổng chi phí trợ lý | Số yêu cầu không thành công | Chi phí cả hệ thống | Chi phí mỗi việc thành công |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 đ (simulated) | 319 | 7.449.781 đ (simulated) | 4.111 đ (simulated) |
| 2 lần | 4.093.220 đ (simulated) | 234 | 6.901.220 đ (simulated) | 4.237 đ (simulated) |
| 3 lần | 4.373.585 đ (simulated) | 222 | 7.037.585 đ (simulated) | 4.472 đ (simulated) |

- Giới hạn **2 lần chạy** rẻ nhất cho công ty (**6.901.220 đ** [`simulated`]), tiết kiệm `136.365 đ` so với 3 lần và `548.561 đ` so với 1 lần. Mức này không trùng với giới hạn cho chi phí mỗi việc thành công thấp nhất (**1 lần**, `4.111 đ` [`simulated`]) vì giới hạn 1 lần đẩy thêm `85` ca sang nhân viên tự làm với giá `12.000 đ/ca`.

## B4 · Nếu phải xem lại tất cả

- Làm lại 9 phút/ca (đề cho): `948` ca có run `ok` × 5 phút + `48` ca làm lại, chia `900` việc thành công = **11.743 đ = 0,98×** của 12.000 đ [`simulated`]; hoà vốn khi xem lại ≤ `5,1 phút`/yêu cầu.
- Làm lại 15,3 phút/ca (trung bình dữ liệu, trung vị 14,5): **12.415 đ = 1,03×** [`simulated`], tức đắt hơn nhân viên tự làm; hoà vốn khi xem lại ≤ `4,8 phút`/yêu cầu.
- Tiền xem lại chiếm **90%** tổng chi phí nên xem lại 100% gần như xoá sạch lợi ích tiết kiệm; pilot phải học được ngưỡng giảm tỉ lệ xem lại an toàn theo bậc và thời gian xem lại có rút xuống dưới `4,8 phút`/yêu cầu được không.
