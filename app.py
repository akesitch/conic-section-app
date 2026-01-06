import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# 1. ตั้งค่าหัวข้อเว็บ
st.set_page_config(page_title="Conic Section Learner", layout="wide")
st.title("เรียนรู้ภาคตัดกรวยแบบโต้ตอบ 📐")

# 2. ส่วนเมนูข้าง (Sidebar)
st.sidebar.header("การตั้งค่ากราฟ")
mode = st.sidebar.selectbox("เลือกประเภท:", ["วงกลม", "วงรี", "พาราโบลา"])

h = st.sidebar.slider("จุดศูนย์กลาง h", -10, 10, 0)
k = st.sidebar.slider("จุดศูนย์กลาง k", -10, 10, 0)

# 3. ตรรกะการคำนวณกราฟ
fig, ax = plt.subplots(figsize=(6, 6))
theta = np.linspace(0, 2*np.pi, 100)

if mode == "วงกลม":
    r = st.sidebar.slider("รัศมี (r)", 1, 10, 5)
    x = h + r * np.cos(theta)
    y = k + r * np.sin(theta)
    st.latex(rf"(x - {h})^2 + (y - {k})^2 = {r}^2")

elif mode == "วงรี":
    a = st.sidebar.slider("แกนเอก (a)", 1, 10, 5)
    b = st.sidebar.slider("แกนโท (b)", 1, 10, 3)
    x = h + a * np.cos(theta)
    y = k + b * np.sin(theta)
    st.latex(rf"\frac{{(x - {h})^2}}{{{a}^2}} + \frac{{(y - {k})^2}}{{{b}^2}} = 1")

# 4. การแสดงผลกราฟ
ax.plot(x, y, color='indigo', linewidth=2)
ax.axhline(0, color='black', lw=1)
ax.axvline(0, color='black', lw=1)
ax.grid(True, linestyle='--')
ax.set_xlim(-15, 15)
ax.set_ylim(-15, 15)
ax.set_aspect('equal')

st.pyplot(fig)