import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
# Cấu hình giao diện Web App
st.set_page_config(page_title="Quản lý điểm sinh viên", page_icon="🎓", layout="wide")
# Khởi tạo dữ liệu
data = { 
  'Họ và tên': ['An', 'Bình', 'Chi', 'Dũng', 'Hà', 'Lan', 'Minh', 'Nam', 'Phúc', 'Trang'],
  'Chuyên cần': [9.0, 8.5, 7.0, 9.5, 8.0, 6.0, 9.0, 7.5, 8.0, 9.5],
  'Giữa kỳ': [7.5, 8.0, 6.5, 9.0, 7.0, 5.5, 8.5, 7.0, 7.0, 9.0],
  'Cuối kỳ': [7.5, 8.5, 6.5, 9.0, 7.0, 6.0, 8.5, 7.0, 7.5, 9.5]
}
df = pd.DataFrame(data)
df.index = range(1, len(df) + 1)
df['Tổng kết'] = (0.2 * df['Chuyên cần'] + 0.3 * df['Giữa kỳ'] + 0.5 * df['Cuối kỳ']).round(2) 
def xep_loai(diem):
    if diem >= 8.5: 
        return 'Giỏi' 
    elif diem >= 7.0:
        return 'Khá' 
    elif diem >= 5.0: 
        return 'Trung bình' 
    else: 
        return 'Yếu' 
df['Xếp loại'] = df['Tổng kết'].apply(xep_loai) 
# 1. Hiển thị tiêu đề
st.title("QUẢN LÝ ĐIỂM SINH VIÊN") 
# 2. Hiển thị bảng điểm đầy đủ 10 sinh viên 
st.subheader("📋 Bảng điểm sinh viên") 
st.dataframe(df, use_container_width=True) 
# 3. Hiển thị thông tin thống kê 
st.subheader("📊 Thống kê lớp học") 
dtb_lop = df['Tổng kết'].mean() 
sv_cao = df.loc[df['Tổng kết'].idxmax()] 
sv_thap = df.loc[df['Tổng kết'].idxmin()]
so_sv_dat = (df['Tổng kết'] >= 5.0).sum() 
c1, c2, c3, c4 = st.columns(4) 
c1.metric("Điểm TB lớp", f"{dtb_lop:.2f}") 
c2.metric("Cao điểm nhất", f"{sv_cao['Họ và tên']}", f"{sv_cao['Tổng kết']} đ") 
c3.metric("Thấp điểm nhất", f"{sv_thap['Họ và tên']}", f"{sv_thap['Tổng kết']} đ") 
c4.metric("Số SV đạt (>=5)", f"{so_sv_dat}/{len(df)}") 
st.markdown("---") 
# 4. Danh sách chọn sinh viên và xem chi tiết 
st.subheader("🔍 Tra cứu chi tiết sinh viên") 
selected_student = st.selectbox("Chọn sinh viên:", options=df['Họ và tên'])
sv_info = df[df['Họ và tên'] == selected_student].iloc[0] 
col_a, col_b, col_c, col_d, col_e = st.columns(5) 
col_a.info(f"**Chuyên cần:** {sv_info['Chuyên cần']}") 
col_b.info(f"**Giữa kỳ:** {sv_info['Giữa kỳ']}") 
col_c.info(f"**Cuối kỳ:** {sv_info['Cuối kỳ']}") 
col_d.success(f"**Tổng kết:** {sv_info['Tổng kết']}") 
col_e.warning(f"**Xếp loại:** {sv_info['Xếp loại']}") 
st.markdown("---") 
# 5. Biểu đồ cột điểm tổng kết 
st.subheader("📈 Biểu đồ điểm tổng kết") 
fig, ax = plt.subplots(figsize=(10, 4))
ax.bar(df['Họ và tên'], df['Tổng kết'], color='skyblue',
       edgecolor='black')
ax.set_ylabel("Điểm tổng kết")
ax.set_ylim(0, 10) 
ax.grid(axis='y', linestyle='--', alpha=0.7) 
for i, val in enumerate(df['Tổng kết']): 
  ax.text(i, val + 0.15, str(val), ha='center', va='bottom') 
st.pyplot(fig) 
# 6. Họ tên và MSSV ở chân trang với kích thước chữ nhỏ 
st.markdown("---") 
st.markdown( 
  "<p style=' text-align: center; font-size: 13px; color: gray;'>"
  "Họ và tên: [Đỗ Thị Ngọc Ánh] | MSSV: [027308002842]</p>",
  unsafe_allow_html=True
)
