import streamlit as st

st.title("📺 IPTV Player")

# Kullanıcıdan giriş bilgilerini alma
username = st.text_input("Kullanıcı Adı")
password = st.text_input("Şifre", type="password")
iptv_url = st.text_input("IPTV Linki")

if st.button("Yayını Başlat"):
    if username and password and iptv_url:
        st.video(iptv_url)  # IPTV linkini oynat
        st.success("Yayın başlatıldı!")
    else:
        st.error("Lütfen tüm alanları doldurun!")
