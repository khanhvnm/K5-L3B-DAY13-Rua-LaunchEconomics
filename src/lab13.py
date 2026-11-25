"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# TODO CP1: viết ba hàm dưới đây cho tới khi kiem_tra_dap_an_biet_truoc() in ĐẠT.
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    # Lần chạy thứ i xảy ra khi i-1 lần trước đều sai: tổng (1-p)^(i-1), i = 1..k
    # = (1 - (1-p)^k) / p ; khi k → ∞ thì = 1/p (phân phối hình học).
    if k is None:
        return 1 / p
    return (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    # Thất bại chỉ khi cả k lần đều sai.
    if k is None:
        return 1.0
    return 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    # = số lần chạy kỳ vọng / xác suất thành công = 1/p với mọi k (tử và mẫu cùng chứa 1-(1-p)^k).
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# TODO CP1: viết mo_hinh; CP2 gọi lại hàm này với tham số giá và hệ số đã đổi.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    # Chỉ lấy các lần chạy thuộc các yêu cầu đang xét (để A3 gọi lại với reqs đã lọc theo loai).
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:
        # B1/B3: bỏ các lần chạy vượt giới hạn; yêu cầu cần nhiều lần hơn coi như chuyển nhân viên.
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    # Tử số: MỌI lần chạy, kể cả lần lỗi (lần lỗi vẫn tốn token và tool).
    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    # Phút nhân viên: số GIẢ LẬP (simulated).
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    # Mẫu số: chỉ đếm yêu cầu thành công.
    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())
    return dict(
        token=tien_token.sum(),
        tool=tien_tool.sum(),
        chay_lai=(tien_token + tien_tool)[runs['attempt'] > 1].sum(),  # phần của lần chạy thứ 2, 3
        xem_lai=xem_lai,
        lam_lai=lam_lai,
        tong=tong,
        thanh_cong=thanh_cong,
        cps=tong / thanh_cong,
        hoa_don_moi_yc=(tien_token.sum() + tien_tool.sum()) / len(reqs),
    )


CHI_PHI_CO_DINH = 40_000_000   # đồng / tháng
KHOI_LUONG_THANG = 45_000      # yêu cầu / tháng
PHAM_VI = ['noi_dia', 'hang_nang']


def in_a2(runs, reqs):
    kq = mo_hinh(runs, reqs)
    nhan = {'token': 'đo từ trace', 'tool': 'đo từ trace', 'chay_lai': 'đo từ trace',
            'xem_lai': 'simulated', 'lam_lai': 'simulated', 'tong': 'có phần simulated',
            'thanh_cong': '', 'cps': 'simulated', 'hoa_don_moi_yc': 'đo từ trace'}
    print('\n=== A2 · Mô hình chi phí từ trace ===')
    print(f"(tool: {runs['tool_calls'].sum():,} lần gọi · xem lại: {reqs['phut_xem_lai_simulated'].sum():,} phút"
          f" · làm lại: {reqs['phut_lam_lai_simulated'].sum():,} phút)")
    for ten, gia_tri in kq.items():
        print(f'{ten:15s} {gia_tri:>14,.1f}  {nhan[ten]}')
    print(f"Chi phí mỗi việc thành công gấp {kq['cps'] / kq['hoa_don_moi_yc']:.1f} lần hoá đơn chia số yêu cầu")
    for k in ['token', 'tool', 'xem_lai', 'lam_lai']:
        print(f"  tỉ trọng {k:8s} {kq[k] / kq['tong'] * 100:5.1f}%")
    khong_tc = int((reqs['ket_qua'] != 'thanh_cong').sum())
    he_thong = (kq['tong'] + khong_tc * BASELINE) / len(reqs)
    print(f"Chi phí cả hệ thống mỗi yêu cầu (cộng {khong_tc} ca nhân viên làm thay × 12.000 đ): "
          f"{he_thong:,.0f} đ = {he_thong / BASELINE:.2f}× [simulated]")
    return kq


def in_a3(runs, reqs):
    print('\n=== A3 · Tách theo loại yêu cầu ===')
    print(f"{'loai':10s} {'so_yc':>6s} {'ti_le_tc':>9s} {'chay/yc':>8s} {'cps':>9s} {'so_12k':>7s}")
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        r = reqs[reqs['loai'] == loai]
        kq = mo_hinh(runs, r)
        so_chay = runs['request_id'].isin(r['request_id']).sum()
        print(f"{loai:10s} {len(r):6d} {kq['thanh_cong'] / len(r) * 100:8.1f}% {so_chay / len(r):8.2f}"
              f" {kq['cps']:9,.0f} {kq['cps'] / BASELINE:6.2f}×")
    # Chạy lại có giúp không: tỉ lệ ok theo từng lần thử.
    bang = (runs.merge(reqs[['request_id', 'loai']], on='request_id')
                .assign(ok=lambda d: (d['status'] == 'ok').astype(float))
                .pivot_table(index='loai', columns='attempt', values='ok', aggfunc='mean'))
    print('\nTỉ lệ lần chạy ok theo lần thử (attempt):')
    print((bang * 100).round(1).to_string())


def in_a4(runs, reqs):
    print('\n=== A4 · Chi phí cố định (phạm vi noi_dia + hang_nang) ===')
    r = reqs[reqs['loai'].isin(PHAM_VI)]
    kq = mo_hinh(runs, r)
    print(f"Trong phạm vi: {len(r)} yêu cầu, {kq['thanh_cong']} việc thành công, "
          f"tổng {kq['tong']:,.0f} đ, cps {kq['cps']:,.0f} đ [simulated]")
    for ten, khoi_luong in [('45.000 yc/tháng', KHOI_LUONG_THANG), ('Một nửa khối lượng', KHOI_LUONG_THANG / 2)]:
        # Quy ra số việc thành công mỗi tháng theo tỉ lệ trong mẫu 1.200 yêu cầu.
        tc_thang = khoi_luong * kq['thanh_cong'] / len(reqs)
        co_dinh = CHI_PHI_CO_DINH / tc_thang
        tong_moi_viec = kq['cps'] + co_dinh
        print(f"{ten:20s} việc TC/tháng {tc_thang:>8,.0f} · cố định/việc {co_dinh:>6,.0f} đ"
              f" · cps + cố định {tong_moi_viec:>6,.0f} đ = {tong_moi_viec / BASELINE:.2f}× [simulated]")


# ---------- Nhiệm vụ B · Bảng độ nhạy ----------
KICH_BAN_B1 = {
    'Giá token gấp đôi':          dict(gia_vao=52, gia_ra=260),
    'Giá token giảm một nửa':     dict(gia_vao=13, gia_ra=65),
    'Tỉ lệ xem lại gấp đôi':      dict(he_so_xem_lai=2),
    'Tỉ lệ xem lại giảm một nửa': dict(he_so_xem_lai=0.5),
    'Số ca làm lại gấp đôi':      dict(he_so_lam_lai=2),
    'Số ca làm lại giảm một nửa': dict(he_so_lam_lai=0.5),
    'Lương nhân viên tăng 25%':   dict(luong_phut=2500),
    'Chỉ cho chạy tối đa 2 lần':  dict(max_lan_chay=2),
    'Chỉ cho chạy 1 lần':         dict(max_lan_chay=1),
}
PHUT_XEM_LAI_B4 = 5   # phút xem lại mỗi yêu cầu khi xem lại 100% (đề cho)
PHUT_LAM_LAI_B4 = 9   # phút làm lại mỗi ca (đề cho)


def in_b1_b2(runs, reqs):
    goc = mo_hinh(runs, reqs)['cps']
    print('\n=== B1 · Đổi từng yếu tố (chi phí mỗi việc thành công, simulated) ===')
    print(f"{'Gốc (A2)':28s} {goc:8,.0f}")
    thay_doi = {}
    for ten, kw in KICH_BAN_B1.items():
        cps = mo_hinh(runs, reqs, **kw)['cps']
        thay_doi[ten] = (cps / goc - 1) * 100
        print(f'{ten:28s} {cps:8,.0f} {thay_doi[ten]:+6.1f}%')

    print('\n=== B2 · Đổi một cặp ===')
    cps = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)['cps']
    tong_rieng = thay_doi['Giá token gấp đôi'] + thay_doi['Tỉ lệ xem lại gấp đôi']
    print(f'Giá token × 2 + xem lại × 2: {cps:,.0f} đ ({(cps / goc - 1) * 100:+.1f}%);'
          f' tổng hai tác động riêng {tong_rieng:+.1f}% (mô hình cộng tuyến tính)')
    # Xếp hạng theo mức tăng của kịch bản "gấp đôi"/"tăng" (cùng một cú sốc cho mỗi yếu tố).
    yeu_to = {'Số ca làm lại': thay_doi['Số ca làm lại gấp đôi'],
              'Tỉ lệ xem lại': thay_doi['Tỉ lệ xem lại gấp đôi'],
              'Lương nhân viên (+25%)': thay_doi['Lương nhân viên tăng 25%'],
              'Giá token': thay_doi['Giá token gấp đôi']}
    xep_hang = sorted(yeu_to.items(), key=lambda x: -abs(x[1]))
    print('Xếp hạng: ' + ' · '.join(f'{i}. {ten} ({v:+.1f}%)' for i, (ten, v) in enumerate(xep_hang[:3], 1)))


def in_b3(runs, reqs):
    print('\n=== B3 · Giới hạn chạy lại (simulated) ===')
    print(f"{'gioi_han':>8s} {'tong_tro_ly':>13s} {'khong_tc':>9s} {'ca_he_thong':>13s} {'cps':>7s}")
    for k in [1, 2, 3]:
        kq = mo_hinh(runs, reqs, max_lan_chay=k)
        khong_tc = len(reqs) - kq['thanh_cong']
        # Nhân viên phải làm thay mọi yêu cầu không thành công, mỗi yêu cầu 12.000 đ.
        he_thong = kq['tong'] + khong_tc * BASELINE
        print(f"{k:8d} {kq['tong']:13,.0f} {khong_tc:9d} {he_thong:13,.0f} {kq['cps']:7,.0f}")


def in_b4(runs, reqs):
    print('\n=== B4 · Xem lại 100% (noi_dia + hang_nang, simulated) ===')
    r = reqs[reqs['loai'].isin(PHAM_VI)]
    ru = runs[runs['request_id'].isin(r['request_id'])]
    co_ok = ru.loc[ru['status'] == 'ok', 'request_id'].nunique()   # có gợi ý để nhân viên xem lại
    so_lam_lai = int((r['ket_qua'] == 'lam_lai').sum())
    thanh_cong = int((r['ket_qua'] == 'thanh_cong').sum())
    token_tool = (ru['tokens_in'] / 1000 * GIA_VAO + ru['tokens_out'] / 1000 * GIA_RA
                  + ru['tool_calls'] * GIA_TOOL).sum()
    xem_lai = co_ok * PHUT_XEM_LAI_B4 * LUONG_PHUT
    print(f'{len(r)} yêu cầu · {co_ok} có lần chạy ok · {so_lam_lai} ca làm lại · {thanh_cong} việc thành công')
    print(f'Xem lại {co_ok} × {PHUT_XEM_LAI_B4} phút = {xem_lai:,.0f} đ · token + tool {token_tool:,.0f} đ')

    # Phút làm lại thực tế trung bình trong dữ liệu (trên mọi ca lam_lai).
    phut_tb = reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated']
    for nhan, phut in [(f'{PHUT_LAM_LAI_B4} phút/ca (đề cho)', PHUT_LAM_LAI_B4),
                       (f'{phut_tb.mean():.1f} phút/ca (trung bình dữ liệu, trung vị {phut_tb.median():.1f})',
                        phut_tb.mean())]:
        lam_lai = so_lam_lai * phut * LUONG_PHUT
        tong = xem_lai + lam_lai + token_tool
        cps = tong / thanh_cong
        # Hoà vốn: số phút xem lại mỗi yêu cầu để cps = 12.000 đ.
        hoa_von = (BASELINE * thanh_cong - lam_lai - token_tool) / (co_ok * LUONG_PHUT)
        print(f'Làm lại {nhan}: tổng {tong:,.0f} đ → {cps:,.0f} đ = {cps / BASELINE:.2f}×;'
              f' hoà vốn khi xem lại ≤ {hoa_von:.1f} phút/yêu cầu')
    print(f'Tỉ trọng tiền xem lại trong tổng (9 phút làm lại): '
          f'{xem_lai / (xem_lai + so_lam_lai * PHUT_LAM_LAI_B4 * LUONG_PHUT + token_tool) * 100:.0f}%')


# ---------- Nhiệm vụ E1 · Tính thử ba chỉ số ----------
def in_e1(reqs):
    """Ba chỉ số trên mẫu chạy thử. Không dùng cột _simulated nên không cần nhãn simulated.
    Đợt chạy thử không có nhóm đối chứng: chỉ viết "chỉ số trong đợt chạy thử là ...". """
    print('\n=== E1 · Ba chỉ số trong đợt chạy thử ===')
    chinh = (reqs['dong_trong_24h'] == 1) & (reqs['mo_lai_trong_7_ngay'] == 0)
    xem = reqs[reqs['duoc_xem_lai'] == 1]
    bo_qua = xem['quyet_dinh_xem_lai'].isin(['sua', 'bo'])
    mo_lai = reqs['mo_lai_trong_7_ngay'] == 1
    pv = reqs[reqs['loai'].isin(PHAM_VI)]
    mo_lai_pv = pv['mo_lai_trong_7_ngay'] == 1
    print(f'Chính · đóng 24h và không mở lại 7 ngày: {chinh.mean() * 100:.2f}% ({chinh.sum()}/{len(reqs)})')
    print(f'Dùng  · bỏ qua gợi ý (sua + bo):          {bo_qua.mean() * 100:.2f}% ({bo_qua.sum()}/{len(xem)})')
    print(f'An toàn · mở lại trong 7 ngày:            {mo_lai.mean() * 100:.2f}% ({mo_lai.sum()}/{len(reqs)});'
          f' phạm vi noi_dia + hang_nang {mo_lai_pv.mean() * 100:.2f}% ({mo_lai_pv.sum()}/{len(pv)})')
    # Mức hiện tại trong phạm vi pilot, làm mốc cho dấu hiệu theo dõi ở E2.
    lam_lai_pv = pv['ket_qua'] == 'lam_lai'
    xem_pv = pv['duoc_xem_lai'] == 1
    print(f'Mốc E2 (phạm vi): tỉ lệ làm lại {lam_lai_pv.mean() * 100:.1f}% ({lam_lai_pv.sum()}/{len(pv)});'
          f' tỉ lệ được xem lại {xem_pv.mean() * 100:.1f}% ({xem_pv.sum()}/{len(pv)})')


if __name__ == '__main__':
    import sys
    sys.stdout.reconfigure(encoding='utf-8')  # tránh lỗi in tiếng Việt trên console Windows
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    print('=== A1 ===')
    print(f'so_lan_chay_ky_vong(0.8, 2)            = {so_lan_chay_ky_vong(0.8, 2):.2f}')
    print(f'so_lan_chay_ky_vong(0.8)               = {so_lan_chay_ky_vong(0.8):.2f}')
    print(f'he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) = {he_so_chi_phi_moi_viec_thanh_cong(0.8, 3):.2f}')
    kiem_tra_dap_an_biet_truoc()
    ket_qua = in_a2(runs, reqs)
    in_a3(runs, reqs)
    in_a4(runs, reqs)
    in_b1_b2(runs, reqs)
    in_b3(runs, reqs)
    in_b4(runs, reqs)
    in_e1(reqs)
    # TODO CP4 · Nhiệm vụ D: cỡ mẫu.
    #   from statsmodels.stats.proportion import proportion_effectsize
    #   from statsmodels.stats.power import NormalIndPower
