import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# 1. ตั้งค่าหัวข้อเว็บ
st.set_page_config(page_title="Conic Section Learner", layout="wide")
st.title("เรียนรู้ภาคตัดกรวยแบบโต้ตอบ 📐")

# 2. ส่วนเมนูข้าง (Sidebar)
st.sidebar.header("การตั้งค่ากราฟ")
mode = st.sidebar.selectbox("เลือกประเภท:", ["วงกลม", "วงรี", "พาราโบลา", "ไฮเพอร์โบลา"])

h = st.sidebar.slider("จุดศูนย์กลาง/จุดยอด h", -10, 10, 0)
k = st.sidebar.slider("จุดศูนย์กลาง/จุดยอด k", -10, 10, 0)

# 3. ตรรกะการคำนวณกราฟ
fig, ax = plt.subplots(figsize=(6, 6))
theta = np.linspace(0, 2*np.pi, 100)

# สร้างตัวแปร x, y เริ่มต้นเพื่อป้องกัน Error
x, y = np.array([]), np.array([]) 

if mode == "วงกลม":
    r = st.sidebar.slider("รัศมี (r)", 1.0, 10.0, 5.0)
    x = h + r * np.cos(theta)
    y = k + r * np.sin(theta)
    st.latex(rf"(x - {h})^2 + (y - {k})^2 = {r}^2")

elif mode == "วงรี":
    a = st.sidebar.slider("แกนเอก (a)", 1.0, 10.0, 5.0)
    b = st.sidebar.slider("แกนโท (b)", 1.0, 10.0, 3.0)
    x = h + a * np.cos(theta)
    y = k + b * np.sin(theta)
    st.latex(rf"\frac{{(x - {h})^2}}{{{a}^2}} + \frac{{(y - {k})^2}}{{{b}^2}} = 1")

elif mode == "พาราโบลา":
    p = st.sidebar.slider("ค่า p (ระยะโฟกัส)", -5.0, 5.0, 2.0)
    if p == 0: p = 0.1 # ป้องกันหารศูนย์
    x = np.linspace(h-10, h+10, 100)
    y = ((x - h)**2 / (4 * p)) + k
    st.latex(rf"(x - {h})^2 = 4({p})(y - {k})")

elif mode == "ไฮเพอร์โบลา":
    a = st.sidebar.slider("ค่า a", 1.0, 10.0, 5.0)
    b = st.sidebar.slider("ค่า b", 1.0, 10.0, 3.0)
    t = np.linspace(-2, 2, 100)
    # วาด 2 กิ่งของไฮเพอร์โบลา
    x1 = h + a * np.cosh(t)
    y1 = k + b * np.sinh(t)
    x2 = h - a * np.cosh(t)
    y2 = k - b * np.sinh(t)
    ax.plot(x1, y1, color='indigo', linewidth=2)
    ax.plot(x2, y2, color='indigo', linewidth=2)
    st.latex(rf"\frac{{(x - {h})^2}}{{{a}^2}} - \frac{{(y - {k})^2}}{{{b}^2}} = 1")

# 4. การแสดงผลกราฟ (เฉพาะโหมดที่ไม่ใช่ไฮเพอร์โบลาที่วาดไปแล้ว)
if mode != "ไฮเพอร์โบลา":
    ax.plot(x, y, color='indigo', linewidth=2)

ax.axhline(0, color='black', lw=1)
ax.axvline(0, color='black', lw=1)
ax.grid(True, linestyle='--')
ax.set_xlim(-15, 15)
ax.set_ylim(-15, 15)
ax.set_aspect('equal')
st.pyplot(fig)
