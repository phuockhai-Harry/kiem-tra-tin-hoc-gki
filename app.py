import streamlit as st

st.title("Chào mừng đến với Web App của tôi! 🎉")
st.write("Chương trình đã tự động chạy ngay khi bạn mở link này.")

# Thử một nút bấm
if st.button("Bấm vào đây"):
    st.success("Bạn đã bấm nút thành công!")