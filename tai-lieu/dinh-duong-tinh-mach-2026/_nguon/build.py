# -*- coding: utf-8 -*-
# Hướng dẫn chăm sóc điều dưỡng khi truyền SMOFKabiven Peripheral 1206 ml và SMOFlipid 20% 250 ml
# + Bảng kiểm Đạt/Không đạt. PĐD BVĐK Nhật Tân, 14/11/2026.
# Thông số sản phẩm lấy từ SmPC: SmofKabiven Peripheral (HPRA Ireland, PA2059/061/002, sửa đổi 08/2023)
# và SMOFlipid 200 mg/ml (Läkemedelsverket Thụy Điển, sửa đổi 06/03/2020).
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from lib import Doc, Cm, Pt, WD_ALIGN_PARAGRAPH
OUT = sys.argv[1]; os.makedirs(OUT, exist_ok=True)
NGAY = "14/11/2026"
HD = "NhatTan_HD-Cham-soc-truyen-SMOFKabiven-SMOFlipid_v01_20261114"
BK = "NhatTan_BK-Truyen-SMOFKabiven-SMOFlipid_v01_20261114"

CAN_CU = [
    "Luật Khám bệnh, chữa bệnh số 15/2023/QH15 ngày 09/01/2023.",
    "Thông tư 31/2021/TT-BYT ngày 28/12/2021 của Bộ Y tế quy định hoạt động điều dưỡng trong bệnh viện.",
    "Thông tư 18/2020/TT-BYT ngày 12/11/2020 của Bộ Y tế quy định về hoạt động dinh dưỡng trong bệnh viện.",
    "Thông tư 23/2011/TT-BYT ngày 10/6/2011 của Bộ Y tế hướng dẫn sử dụng thuốc trong các cơ sở y tế có giường bệnh.",
    "Thông tư 51/2017/TT-BYT ngày 29/12/2017 của Bộ Y tế hướng dẫn phòng, chẩn đoán và xử trí phản vệ.",
    "Thông tư 43/2018/TT-BYT ngày 26/12/2018 của Bộ Y tế hướng dẫn phòng ngừa sự cố y khoa trong cơ sở khám bệnh, chữa bệnh.",
    "Thông tư 32/2023/TT-BYT ngày 31/12/2023 của Bộ Y tế quy định chi tiết một số điều của Luật Khám bệnh, chữa bệnh (hồ sơ bệnh án, phiếu chăm sóc).",
    "Thông tư 20/2021/TT-BYT ngày 26/11/2021 của Bộ Y tế quy định về quản lý chất thải y tế trong phạm vi khuôn viên cơ sở y tế.",
    "Quyết định 3671/QĐ-BYT ngày 27/9/2012 của Bộ Y tế phê duyệt các hướng dẫn kiểm soát nhiễm khuẩn (trong đó có hướng dẫn phòng ngừa nhiễm khuẩn huyết liên quan đến catheter và tiêm an toàn).",
    "Tờ hướng dẫn sử dụng (SmPC) của Fresenius Kabi: SmofKabiven Peripheral (bản HPRA Ireland, sửa đổi 08/2023) và SMOFlipid 200 mg/ml (bản Läkemedelsverket, sửa đổi 03/2020). Khi tờ hướng dẫn kèm hộp lưu hành tại Việt Nam khác các bản này thì theo tờ kèm hộp. Số đăng ký lưu hành tại Việt Nam: Cần xác minh với Khoa Dược.",
    "Quy trình kỹ thuật truyền dịch tĩnh mạch của Bệnh viện (QT-A48, bộ SOP Nhóm A) cho các bước kỹ thuật đặt và duy trì đường truyền.",
]

# =====================================================================
# 1. HƯỚNG DẪN CHĂM SÓC
# =====================================================================
d = Doc()
d.sop_header("HD-DDTM-01", "Chăm sóc người bệnh truyền SMOFKabiven Peripheral và SMOFlipid 20%",
             lan="01", ngay=NGAY, kind="HƯỚNG DẪN CHĂM SÓC ĐIỀU DƯỠNG")

def H(s): d.h2(s)
def H3(s): d.h3(s)
def P(s): d.para(s)
def B(xs): d.bullets(xs)
def T(rows, w, cc=(), size=11): d.table(rows, w, size=size, center_cols=cc)

H("1. MỤC ĐÍCH")
P("Thống nhất cách điều dưỡng chuẩn bị, thực hiện y lệnh, theo dõi và ghi hồ sơ khi người bệnh được nuôi dưỡng tĩnh mạch bằng SMOFKabiven Peripheral 1206 ml (túi ba ngăn) và SMOFlipid 20% 250 ml (chai), nhằm truyền đúng tốc độ, phát hiện sớm viêm tĩnh mạch, phản ứng dị ứng, rối loạn đường huyết, mỡ máu và quá tải dịch.")

H("2. PHẠM VI ÁP DỤNG")
B([
    "Người bệnh nội trú có y lệnh nuôi dưỡng tĩnh mạch bằng hai sản phẩm trên tại các khoa lâm sàng của Bệnh viện Đa khoa Nhật Tân.",
    "SMOFKabiven Peripheral dùng cho người lớn và trẻ trên 2 tuổi; chống chỉ định cho trẻ dưới 2 tuổi. Trẻ em áp dụng thêm hướng dẫn của Khoa Nhi.",
    "Người thực hiện: điều dưỡng, hộ sinh được phân công, trong phạm vi chuyên môn đã được đánh giá năng lực.",
    "Chỉ định, liều, tốc độ, thời gian truyền và xét nghiệm theo dõi do bác sĩ quyết định (có ý kiến Khoa Dinh dưỡng, Khoa Dược khi cần). Điều dưỡng thực hiện y lệnh, theo dõi, báo cáo, không tự thay đổi.",
])

H("3. CĂN CỨ")
B(CAN_CU)

H("4. THÔNG TIN SẢN PHẨM ĐIỀU DƯỠNG CẦN NẮM")
d.para("Bảng 1. Thông số chính theo tờ hướng dẫn sử dụng của nhà sản xuất", bold=True, indent=False, align="center")
T([
    ["Nội dung", "SMOFKabiven Peripheral 1206 ml", "SMOFlipid 20% 250 ml"],
    ["Dạng", "Túi ba ngăn: glucose 13% 656 ml; acid amin có điện giải 380 ml; nhũ tương lipid 170 ml. Phải phá vách, trộn đều trước khi dùng", "Chai nhũ tương lipid 20% (dầu đậu nành, MCT, dầu ô liu, dầu cá)"],
    ["Thành phần chính", "Acid amin 38 g (nitơ 6,2 g); glucose 85 g; lipid 34 g; Na 30 mmol, K 23 mmol, Mg 3,8 mmol, Ca 1,9 mmol, phosphat 9,9 mmol. Không có vitamin và vi lượng", "Lipid 50 g/chai"],
    ["Năng lượng", "Khoảng 800 kcal (không kể protein khoảng 700 kcal)", "Khoảng 500 kcal/chai (2000 kcal/lít)"],
    ["Áp lực thẩm thấu", "Khoảng 850 mOsm/l (950 mOsm/kg nước): cao, dễ gây viêm tĩnh mạch ngoại vi", "Khoảng 380 mOsm/kg"],
    ["Liều thông thường (người lớn)", "20–40 ml/kg/ngày; tối đa 40 ml/kg/ngày", "1–2 g lipid/kg/ngày = 5–10 ml/kg/ngày"],
    ["Tốc độ tối đa", "Không quá 3,0 ml/kg/giờ", "Khuyến cáo 0,63 ml/kg/giờ (0,125 g/kg/giờ); không quá 0,75 ml/kg/giờ (0,15 g/kg/giờ)"],
    ["Thời gian truyền", "Khuyến cáo 14–24 giờ/túi (trẻ 2–11 tuổi: 12–24 giờ)", "Theo y lệnh; không nhanh hơn tốc độ tối đa"],
    ["Ngưỡng triglycerid khi đang truyền", "Không quá 4 mmol/l", "Không quá 3 mmol/l; vượt thì báo bác sĩ giảm liều hoặc ngừng"],
    ["Bảo quản", "Không quá 25°C, không để đông đá, giữ trong túi ngoài", "Không quá 25°C, không để đông đá"],
    ["Sau khi phá vách/mở", "Vi sinh: dùng ngay. Độ ổn định hóa lý sau trộn ghi 36 giờ ở 25°C hoặc 48 giờ ở 20–25°C tùy bản tờ hướng dẫn (Cần xác minh bản kèm hộp). Có bổ sung thuốc: dùng ngay", "Dùng ngay. Độ ổn định hóa lý 24 giờ ở 25°C. Dùng một lần, bỏ phần thừa"],
], [3.2, 6.8, 6.5], size=10.5)
d.note("SMOFKabiven Peripheral đã chứa 34 g lipid (chính là SMOFlipid). Khi có y lệnh truyền thêm SMOFlipid cùng ngày, điều dưỡng hỏi lại bác sĩ hoặc dược sĩ nếu thấy tổng lipid vượt 2 g/kg/ngày hoặc tổng dịch vượt mức người bệnh chịu được.")

d.para("Bảng 2. Tốc độ tối đa theo cân nặng (tính sẵn để đối chiếu y lệnh)", bold=True, indent=False, align="center")
rows = [["Cân nặng", "SMOFKabiven tối đa (ml/giờ)", "SMOFKabiven tối đa/ngày (ml)", "SMOFlipid khuyến cáo (ml/giờ)", "SMOFlipid tối đa (ml/giờ)"]]
for kg in (30, 40, 50, 60, 70):
    rows.append([f"{kg} kg", f"{kg*3:g}", f"{kg*40:g}", f"{round(kg*0.63)}", f"{round(kg*0.75)}"])
T(rows, [2.4, 3.6, 3.6, 3.5, 3.4], cc=(0, 1, 2, 3, 4))
B([
    "Ví dụ: túi 1206 ml truyền đều trong 24 giờ là khoảng 50 ml/giờ; trong 14 giờ là khoảng 86 ml/giờ.",
    "Đổi sang giọt/phút khi không có máy truyền (dây 20 giọt/ml): số giọt/phút = số ml/giờ chia 3. Ví dụ 50 ml/giờ ≈ 17 giọt/phút. Dây có hệ số khác thì tính theo hệ số ghi trên bao bì dây.",
    "Nhà sản xuất khuyến cáo truyền liên tục, kiểm soát tốt bằng máy truyền dịch khi có thể.",
])

H("5. CHỐNG CHỈ ĐỊNH VÀ THẬN TRỌNG: ĐIỀU DƯỠNG PHÁT HIỆN ĐỂ BÁO BÁC SĨ")
P("Khi nhận định thấy một trong các tình trạng sau, điều dưỡng chưa truyền và báo bác sĩ (không tự quyết định ngừng hay tiếp tục):")
B([
    "Dị ứng với protein cá, trứng, đậu nành, đậu phộng (lạc) hoặc thành phần thuốc.",
    "Rối loạn mỡ máu nặng; suy gan nặng; rối loạn đông máu nặng; suy thận nặng không được lọc máu.",
    "Sốc; tình trạng không ổn định (sau chấn thương nặng, đái tháo đường mất bù, nhồi máu cơ tim cấp, đột quỵ, thuyên tắc, toan chuyển hóa, nhiễm khuẩn huyết nặng).",
    "Phù phổi cấp, thừa dịch, suy tim mất bù.",
    "Riêng SMOFKabiven Peripheral: tăng đường huyết không kiểm soát; điện giải trong máu tăng bệnh lý; rối loạn chuyển hóa acid amin bẩm sinh; hội chứng thực bào máu; trẻ dưới 2 tuổi.",
    "Thận trọng (theo dõi sát hơn): suy thận, đái tháo đường, viêm tụy, suy giáp, nhiễm khuẩn huyết, người bệnh suy kiệt hoặc nhịn ăn lâu ngày (nguy cơ hội chứng nuôi ăn lại).",
])

H("6. NỘI DUNG CHĂM SÓC")
H3("6.1. Nhận định trước truyền")
B([
    "Nhận và đối chiếu y lệnh: tên sản phẩm, thể tích, tốc độ (ml/giờ), thời gian truyền, đường truyền, thuốc bổ sung vào túi (nếu có), xét nghiệm theo dõi.",
    "Định danh người bệnh bằng ít nhất 2 thông tin (họ tên, năm sinh) đối chiếu vòng đeo tay và y lệnh; hỏi lại tiền sử dị ứng.",
    "Cân nặng thực tế (ghi kg) để đối chiếu tốc độ tối đa ở Bảng 2; người béo phì đối chiếu với cân nặng lý tưởng bác sĩ ghi.",
    "Sinh hiệu, tri giác, phù, khó thở, nghe phổi (ran ẩm), lượng nước tiểu; dịch vào – ra 24 giờ trước.",
    "Đường huyết mao mạch nền; kết quả xét nghiệm gần nhất theo y lệnh (điện giải đồ, triglycerid, đường huyết, men gan, chức năng thận).",
    "Tình trạng tĩnh mạch ngoại vi; catheter đang lưu (vị trí, ngày đặt, điểm VIP).",
    "Người bệnh suy kiệt, ăn rất ít hoặc nhịn ăn trên 5 ngày: báo bác sĩ về nguy cơ hội chứng nuôi ăn lại để có y lệnh bắt đầu chậm và theo dõi kali, phospho, magie trong 24–48 giờ đầu.",
    "Giải thích cho người bệnh, người nhà mục đích, thời gian truyền và những dấu hiệu cần báo ngay.",
])

H3("6.2. Chuẩn bị sản phẩm và dụng cụ")
B([
    "Vệ sinh tay; kiểm tra tên, hàm lượng, hạn dùng, số lô; túi ngoài còn nguyên, không rách, không ướt.",
    "SMOFKabiven: các vách ngăn còn nguyên (chưa bị vỡ trước); dung dịch glucose và acid amin trong, không màu hoặc hơi vàng, không có vẩn; nhũ tương lipid trắng đồng nhất. Túi có chỉ thị oxy đổi màu đen thì không dùng (túi đang dùng tại bệnh viện có chỉ thị hay không: Cần xác minh).",
    "SMOFlipid: chai không nứt, nắp kín; nhũ tương trắng đồng nhất, không tách lớp, không có giọt dầu nổi.",
    "Sản phẩm để tủ lạnh thì để về nhiệt độ phòng trước khi truyền; không làm ấm bằng nước nóng hay lò vi sóng.",
    "Dụng cụ: dây truyền dịch (chai thủy tinh SMOFlipid dùng dây có lỗ thông khí); máy truyền dịch nếu có; catheter tĩnh mạch ngoại vi cỡ nhỏ phù hợp (thường 20–22G); dung dịch sát khuẩn; gạc vô khuẩn; băng dán trong suốt; găng; khay; nhãn ghi giờ; máy đo đường huyết; phiếu theo dõi.",
])

H3("6.3. Phá vách ngăn và trộn túi SMOFKabiven")
d.numbered([
    "Xé túi ngoài theo vết xé, bỏ túi ngoài và gói hút oxy.",
    "Đặt túi lên mặt phẳng sạch, cuộn chặt túi từ phía quai treo về phía các cổng, ép đều cho đến khi các vách ngăn dọc mở hoàn toàn.",
    "Lật ngược túi qua lại ít nhất 3 lần để trộn đều. Kiểm tra lại: nhũ tương trắng đồng nhất, không tách lớp, không có hạt dầu. Có tách lớp thì không dùng, báo Khoa Dược.",
    "Ghi ngày, giờ phá vách lên nhãn túi. Truyền ngay sau khi trộn.",
    "Chỉ thêm vitamin, vi lượng, điện giải khi có y lệnh và Khoa Dược xác nhận tương hợp; thêm qua cổng bổ sung bằng kỹ thuật vô khuẩn sau khi đã trộn ba ngăn. Cổng bổ sung và cổng truyền phân biệt theo ký hiệu in trên túi (thường cổng bổ sung màu trắng, cổng truyền màu xanh: Cần xác minh trên túi thực tế).",
])

H3("6.4. Chọn tĩnh mạch và đường truyền")
B([
    "Chọn tĩnh mạch lớn, đoạn thẳng ở cẳng tay để máu chảy quanh catheter tốt, giảm viêm tĩnh mạch do dịch ưu trương.",
    "Tránh nếp khuỷu, cổ tay, mu bàn tay nếu có lựa chọn khác; không đặt ở chi liệt, chi phù, chi có cầu nối động – tĩnh mạch (FAV), tay bên đã nạo vét hạch nách.",
    "Dùng catheter cỡ nhỏ nhất phù hợp; cố định bằng băng trong suốt để quan sát được vị trí; ghi ngày giờ đặt.",
    "Ưu tiên một đường truyền riêng cho dinh dưỡng tĩnh mạch. Không truyền máu, chế phẩm máu cùng dây (nguy cơ giả ngưng kết); không lấy máu xét nghiệm qua đường đang truyền.",
    "SMOFlipid có thể chạy song song với SMOFKabiven hoặc dung dịch acid amin, glucose qua chạc chữ Y khi có y lệnh; nối chạc Y gần vị trí catheter. Không tiêm, không pha thuốc khác vào túi, chai hoặc dây đang truyền nếu Khoa Dược chưa xác nhận tương hợp.",
    "Kỹ thuật đặt và duy trì đường truyền theo QT-A48 của Bệnh viện; sát khuẩn cổng kết nối trước mỗi lần thao tác.",
])

H3("6.5. Thực hiện truyền")
B([
    "Vệ sinh tay, mang găng; đuổi khí; nối dây vô khuẩn; đặt máy truyền đúng ml/giờ theo y lệnh (hoặc đếm giọt).",
    "Truyền chậm trong 15 phút đầu, ở lại giường quan sát dấu hiệu dị ứng (ngứa, nổi mẩn, khó thở, sốt, rét run, đau ngực, đau lưng).",
    "Không tăng tốc để bù khi truyền chậm hơn kế hoạch; báo bác sĩ để điều chỉnh y lệnh.",
    "Thời hạn hoàn tất: túi SMOFKabiven truyền xong trong vòng 24 giờ kể từ khi treo; SMOFlipid truyền riêng hoàn tất trong vòng 12 giờ. Phần còn thừa sau thời hạn hoặc sau khi tháo phải bỏ, không treo lại.",
    "Thay dây truyền dùng cho nhũ tương lipid hoặc hỗn hợp ba thành phần trong vòng 24 giờ kể từ khi bắt đầu truyền (theo hướng dẫn phòng ngừa nhiễm khuẩn huyết liên quan catheter; mốc thời gian cụ thể đối chiếu quy định KSNK của Bệnh viện).",
])

H3("6.6. Theo dõi trong và sau truyền")
d.para("Bảng 3. Nội dung và tần suất theo dõi (tần suất cụ thể theo y lệnh và phân cấp chăm sóc)", bold=True, indent=False, align="center")
T([
    ["Nội dung", "Tần suất gợi ý", "Cần báo bác sĩ khi"],
    ["Dấu hiệu dị ứng, phản vệ", "Liên tục 15 phút đầu, sau đó mỗi lần đi buồng", "Ngứa, mẩn, khó thở, tím, sốt, rét run, tụt huyết áp: NGỪNG TRUYỀN, giữ đường truyền, xử trí phản vệ theo Thông tư 51/2017/TT-BYT"],
    ["Sinh hiệu", "Trước truyền, sau 15–30 phút, sau đó theo phân cấp chăm sóc (ít nhất mỗi ca)", "Sốt, mạch nhanh, huyết áp tăng hoặc tụt, thở nhanh"],
    ["Vị trí truyền (thang VIP, Bảng 4)", "Mỗi ca và mỗi lần thao tác đường truyền", "VIP từ 2 trở lên, sưng, thoát mạch"],
    ["Đường huyết mao mạch", "Theo y lệnh (thường 6 giờ/lần trong 24–48 giờ đầu hoặc khi người bệnh đái tháo đường)", "Vượt ngưỡng bác sĩ ghi; hạ đường huyết khi ngừng truyền đột ngột"],
    ["Dịch vào – ra, cân nặng", "Dịch vào – ra mỗi 24 giờ; cân theo y lệnh", "Phù, khó thở, ran ẩm, tiểu ít, tăng cân nhanh"],
    ["Triglycerid, điện giải, chức năng gan, thận, công thức máu", "Theo y lệnh", "Triglycerid vượt 4 mmol/l (SMOFKabiven) hoặc 3 mmol/l (SMOFlipid); kali, phospho, magie giảm trong 24–48 giờ đầu"],
    ["Tiêu hóa, toàn thân", "Mỗi ca", "Buồn nôn, nôn, vã mồ hôi, rét run (có thể do truyền acid amin quá nhanh); vàng da, gan to, chảy máu, sốt (gợi ý hội chứng quá tải lipid)"],
], [4.0, 5.0, 7.5], size=10.5)
B([
    "Lấy máu xét nghiệm triglycerid, bilirubin, LDH, hemoglobin: lipid trong máu có thể làm sai kết quả; ghi rõ giờ lấy mẫu so với giờ truyền lipid. Lipid thường được đào thải sau 5–6 giờ ngừng truyền; thời điểm lấy mẫu theo y lệnh.",
    "Kết thúc túi: không ngừng đột ngột ở người bệnh đái tháo đường hoặc đang dùng insulin mà không báo bác sĩ; theo dõi đường huyết sau khi ngừng theo y lệnh.",
])

d.para("Bảng 4. Thang điểm viêm tĩnh mạch tại chỗ truyền (VIP, theo Jackson)", bold=True, indent=False, align="center")
T([
    ["Điểm", "Biểu hiện tại vị trí catheter", "Xử trí của điều dưỡng"],
    ["0", "Bình thường", "Tiếp tục theo dõi"],
    ["1", "Có một trong hai: hơi đau hoặc hơi đỏ gần vị trí catheter", "Theo dõi sát, đánh giá lại sau mỗi lần thao tác"],
    ["2", "Có hai trong ba: đau, đỏ, sưng", "Rút catheter, đặt lại ở vị trí khác, báo bác sĩ"],
    ["3", "Đau dọc theo đường catheter, đỏ, sưng cứng", "Rút catheter, báo bác sĩ, ghi hồ sơ"],
    ["4", "Đau, đỏ, cứng, sờ thấy thừng tĩnh mạch", "Rút catheter, báo bác sĩ xử trí, báo cáo sự cố"],
    ["5", "Như mức 4 kèm sốt (viêm tắc tĩnh mạch huyết khối)", "Rút catheter, báo bác sĩ ngay, báo cáo sự cố"],
], [1.6, 7.2, 7.7], cc=(0,), size=10.5)
d.note("Dịch ưu trương (SMOFKabiven Peripheral khoảng 850 mOsm/l) làm tăng nguy cơ viêm tĩnh mạch ngoại vi. Thời hạn lưu và thay catheter ngoại vi theo quy định KSNK của Bệnh viện (Cần xác minh mốc giờ hiện hành); luôn rút khi VIP từ 2 trở lên.")

H3("6.7. Xử trí một số tình huống")
T([
    ["Tình huống", "Việc điều dưỡng làm ngay"],
    ["Nghi phản vệ, dị ứng", "Ngừng truyền, giữ đường truyền bằng dung dịch theo phác đồ, gọi bác sĩ, xử trí theo Thông tư 51/2017/TT-BYT và hộp chống phản vệ; ghi giờ, giữ lại túi/chai và dây."],
    ["Thoát mạch, sưng tại chỗ", "Ngừng truyền, rút catheter, nâng cao chi, báo bác sĩ; đặt đường truyền mới ở chi khác."],
    ["Viêm tĩnh mạch VIP từ 2 trở lên", "Rút catheter, đặt vị trí khác, báo bác sĩ; mức 4–5 báo cáo sự cố."],
    ["Nhũ tương tách lớp, vón, đổi màu", "Không truyền hoặc ngừng ngay; giữ lại sản phẩm, báo Khoa Dược và báo cáo sự cố."],
    ["Truyền nhanh hơn y lệnh", "Đưa về đúng tốc độ, theo dõi đường huyết, dấu quá tải dịch, buồn nôn; báo bác sĩ; báo cáo sự cố."],
    ["Quá thời hạn hoàn tất", "Ngừng, bỏ phần thừa, báo bác sĩ để có y lệnh túi/chai mới; không truyền tiếp túi cũ."],
], [4.6, 11.9], size=10.5)

H3("6.8. Hướng dẫn người bệnh, người nhà")
B([
    "Không tự chỉnh tốc độ, không tự tháo dây; giữ tay có đường truyền nằm yên, tránh gập.",
    "Báo ngay điều dưỡng khi: đau, rát, sưng, đỏ chỗ truyền; ngứa, nổi mẩn, khó thở, lạnh run, sốt; buồn nôn, vã mồ hôi; dịch ngừng chảy hoặc máu trào vào dây.",
    "Ăn uống đường miệng hoặc qua ống thông theo hướng dẫn của bác sĩ, Khoa Dinh dưỡng.",
])

H3("6.9. Kết thúc truyền và xử lý chất thải")
B([
    "Khóa dây, tháo dây vô khuẩn; nếu không còn y lệnh dùng đường truyền thì rút catheter, ấn giữ, dán gạc; đánh giá vị trí.",
    "Túi, chai, dây truyền phân loại theo Thông tư 20/2021/TT-BYT; dây dính máu bỏ vào chất thải lây nhiễm, catheter bỏ vào hộp kháng thủng.",
])

H3("6.10. Ghi hồ sơ")
B([
    "Phiếu chăm sóc, phiếu theo dõi truyền dịch: tên sản phẩm, số lô, hạn dùng, thể tích, giờ phá vách, giờ bắt đầu và kết thúc, tốc độ, thuốc bổ sung (nếu có), vị trí catheter và điểm VIP, sinh hiệu, đường huyết, dịch vào – ra, phản ứng và xử trí, họ tên người thực hiện.",
    "Ghi đúng số đo thực tế, không ghi bình thường khi chưa kiểm tra.",
    "Sự cố (sai tốc độ, sai sản phẩm, phản ứng, thoát mạch, viêm tĩnh mạch mức 4–5) báo cáo theo Thông tư 43/2018/TT-BYT trên phần mềm NT Nursing.",
])

H("7. GIÁM SÁT TUÂN THỦ")
P("Điều dưỡng trưởng khoa giám sát bằng Bảng kiểm BK-DDTM-01 kèm theo, ít nhất 01 lượt/tháng ở khoa có người bệnh nuôi dưỡng tĩnh mạch; Phòng Điều dưỡng giám sát chéo theo kế hoạch. Kết quả nhập vào mục Tuân thủ quy trình của NT Nursing.")

H("8. NỘI DUNG CẦN XÁC MINH TRƯỚC KHI ÁP DỤNG RỘNG")
B([
    "Tờ hướng dẫn sử dụng kèm hộp lưu hành tại Việt Nam và số đăng ký (Khoa Dược đối chiếu với Bảng 1, đặc biệt thời gian ổn định sau phá vách: 36 hay 48 giờ).",
    "Túi đang dùng có chỉ thị oxy hay không; màu cổng bổ sung và cổng truyền.",
    "Mốc thời gian thay catheter ngoại vi và dây truyền theo quy định KSNK hiện hành của Bệnh viện.",
    "Ngưỡng đường huyết cần báo và tần suất xét nghiệm triglycerid do bác sĩ, Khoa Dinh dưỡng thống nhất.",
])

d.para("", indent=False)
d.sop_sign_table()
d.para(f"Tình trạng: Đã duyệt {NGAY} (Phòng Điều dưỡng). Các mục ghi \"Cần xác minh\" hoàn thiện khi có ý kiến Khoa Dược, Khoa KSNK.", italic=True, indent=False, size=11)
d.save(os.path.join(OUT, HD + ".docx"))

# =====================================================================
# 2. BẢNG KIỂM
# =====================================================================
b = Doc()
b.sop_header("BK-DDTM-01", "Bảng kiểm truyền SMOFKabiven Peripheral và SMOFlipid 20%",
             lan="01", ngay=NGAY, kind="BẢNG KIỂM TUÂN THỦ")
b.para("Khoa: ……………………………………   Ngày kiểm tra: …… /…… /20……   Giờ: ……", indent=False, align="left")
b.para("Người được kiểm tra: ………………………………………   Chức danh: ……………………", indent=False, align="left")
b.para("Người kiểm tra: ……………………………………………\nSản phẩm:  □ SMOFKabiven Peripheral 1206 ml   □ SMOFlipid 20% 250 ml", indent=False, align="left")
b.para("Cách chấm: đánh dấu X vào cột Đạt hoặc Không đạt; bước không áp dụng ghi \"KAD\" ở cột Ghi chú và không tính vào tổng. Bước có dấu (*) là bước bắt buộc: một bước (*) không đạt thì kết quả chung là KHÔNG ĐẠT.", italic=True, indent=False, size=11.5)

STEPS = [
    ("A. CHUẨN BỊ", None),
    ("Đối chiếu y lệnh: tên sản phẩm, thể tích, tốc độ ml/giờ, thời gian truyền, thuốc bổ sung", True),
    ("Định danh người bệnh bằng ít nhất 2 thông tin, đối chiếu vòng đeo tay; hỏi dị ứng cá, trứng, đậu nành, đậu phộng", True),
    ("Có cân nặng thực tế; tốc độ y lệnh không vượt tốc độ tối đa (SMOFKabiven ≤ 3,0 ml/kg/giờ; SMOFlipid ≤ 0,75 ml/kg/giờ)", True),
    ("Nhận định sinh hiệu, phù/khó thở, đường huyết nền, tình trạng tĩnh mạch; báo bác sĩ nếu có chống chỉ định hoặc nguy cơ nuôi ăn lại", False),
    ("Giải thích cho người bệnh, người nhà mục đích, thời gian truyền, dấu hiệu cần báo", False),
    ("Vệ sinh tay đúng thời điểm trước khi chuẩn bị", True),
    ("Kiểm tra sản phẩm: hạn dùng, số lô, túi ngoài/chai nguyên vẹn; vách ngăn còn nguyên; dung dịch trong, nhũ tương trắng đồng nhất", True),
    ("Chuẩn bị đủ dụng cụ; chai thủy tinh SMOFlipid dùng dây có lỗ thông khí; máy truyền dịch (nếu có) hoạt động tốt", False),
    ("B. PHÁ VÁCH VÀ PHA (SMOFKabiven)", None),
    ("Bỏ túi ngoài, gói hút oxy; cuộn túi từ quai treo về phía cổng đến khi các vách ngăn mở hết", False),
    ("Lật ngược túi ít nhất 3 lần; kiểm tra không tách lớp; ghi ngày giờ phá vách lên nhãn", True),
    ("Thuốc bổ sung (nếu có) chỉ theo y lệnh, đã được Khoa Dược xác nhận tương hợp, thêm qua cổng bổ sung bằng kỹ thuật vô khuẩn", False),
    ("C. THỰC HIỆN", None),
    ("Chọn tĩnh mạch lớn ở cẳng tay; tránh nếp gấp, chi liệt, chi phù, chi có FAV; catheter cỡ phù hợp, băng trong suốt", False),
    ("Sát khuẩn cổng kết nối, nối dây và đuổi khí đúng kỹ thuật vô khuẩn", True),
    ("Đường truyền riêng; không truyền máu, không tiêm thuốc khác cùng dây; SMOFlipid qua chạc Y chỉ khi có y lệnh", True),
    ("Đặt đúng tốc độ ml/giờ (hoặc giọt/phút tính đúng) theo y lệnh", True),
    ("Ở lại quan sát 15 phút đầu; đo sinh hiệu sau 15–30 phút", True),
    ("D. THEO DÕI", None),
    ("Đánh giá vị trí truyền bằng thang VIP mỗi ca; VIP ≥ 2 đã rút catheter, đặt vị trí khác, báo bác sĩ", True),
    ("Đo đường huyết mao mạch đúng tần suất y lệnh; báo khi vượt ngưỡng", False),
    ("Ghi dịch vào – ra 24 giờ; phát hiện dấu quá tải dịch", False),
    ("Không tăng tốc bù; túi SMOFKabiven hoàn tất trong 24 giờ, SMOFlipid truyền riêng hoàn tất trong 12 giờ; bỏ phần thừa", True),
    ("Người bệnh, người nhà nói lại được ít nhất 2 dấu hiệu cần báo điều dưỡng (hỏi trực tiếp)", False),
    ("E. KẾT THÚC VÀ GHI HỒ SƠ", None),
    ("Tháo dây, xử lý vị trí catheter đúng; phân loại chất thải đúng (dây dính máu là chất thải lây nhiễm, catheter vào hộp kháng thủng)", False),
    ("Ghi phiếu chăm sóc/phiếu truyền dịch đủ: sản phẩm, số lô, giờ phá vách, giờ bắt đầu – kết thúc, tốc độ, VIP, sinh hiệu, đường huyết, phản ứng, người thực hiện", True),
]
rows = [["STT", "Nội dung kiểm tra", "Đạt", "Không đạt", "Ghi chú"]]
n = 0
for txt, key in STEPS:
    if key is None:
        rows.append(["", txt, "", "", ""])
    else:
        n += 1
        rows.append([str(n), txt + (" (*)" if key else ""), "", "", ""])
tb = b.table(rows, [1.1, 10.2, 1.4, 1.6, 2.2], size=10.5, center_cols=(0,))
for i, (txt, key) in enumerate(STEPS, 1):
    if key is None:
        for r in tb.cell(i, 1).paragraphs[0].runs: r.bold = True
NBUOC = n
NBB = sum(1 for _, k in STEPS if k)
b.para(f"Tổng số bước áp dụng: ……/{NBUOC}    Số bước đạt: ……    Tỷ lệ đạt: ……%    Số bước bắt buộc (*) không đạt: ……/{NBB}", bold=True, indent=False)
b.para("Kết quả chung:  □ ĐẠT (tỷ lệ đạt ≥ 90% và không có bước (*) nào không đạt)     □ KHÔNG ĐẠT", bold=True, indent=False)
b.para("Nhận xét – Kiến nghị: ……………………………………………………………………………………………………………", indent=False)
b.para("…………………………………………………………………………………………………………………………………", indent=False)
b.h2("CĂN CỨ PHÁP LÝ")
b.bullets(CAN_CU[:4] + [CAN_CU[4], CAN_CU[5], CAN_CU[8], CAN_CU[9], "Hướng dẫn chăm sóc HD-DDTM-01 của Phòng Điều dưỡng ban hành kèm bảng kiểm này."])
b.para("", indent=False)
tb2 = b.d.add_table(rows=1, cols=3)
for c, t in zip(tb2.rows[0].cells, ["NGƯỜI ĐƯỢC KIỂM TRA", "ĐIỀU DƯỠNG TRƯỞNG KHOA", "NGƯỜI KIỂM TRA"]):
    p = c.paragraphs[0]; p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    b.run(p, t + "\n", bold=True); b.run(p, "(Ký, ghi rõ họ tên)\n\n\n\n", italic=True, size=11)
b.para(f"Mã biểu mẫu BK-DDTM-01, lần ban hành 01, ngày {NGAY}. Đã duyệt {NGAY}.", italic=True, indent=False, size=10.5)
b.save(os.path.join(OUT, BK + ".docx"))
print(NBUOC, NBB)
