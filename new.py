import streamlit as st

st.title("📱 โปรแกรมคำนวณคนละครึ่ง (40% / 60%)")

# สร้างช่องใส่ตัวเลขบนหน้าเว็บ
total_price = st.number_input("กรอกราคาสินค้าทั้งหมด (บาท):", min_value=0.0, step=10.0)

if total_price > 0:
    my_share = total_price * 0.40
    gov_share = total_price * 0.60
    
    st.write("---")
    st.subheader("📊 ผลการคำนวณ")
    st.info(f"💵 คุณต้องจ่ายเอง (40%): **{my_share:,.2f}** บาท")
    st.success(f"🏛️ รัฐบาลช่วยจ่าย (60%): **{gov_share:,.2f}** บาท")