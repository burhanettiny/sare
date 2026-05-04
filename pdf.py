import streamlit as st
import pdfplumber
import pandas as pd
from io import BytesIO

def extract_tables_from_pdf(file):
    all_tables = []
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            table = page.extract_table()
            if table:
                df = pd.DataFrame(table[1:], columns=table[0]) # İlk satırı başlık yapar
                all_tables.append(df)
    return all_tables

st.set_page_config(page_title="PDF'ten Excel'e Dönüştürücü", layout="centered")

st.title("📄 PDF'ten Excel'e Dönüştürücü")
st.write("PDF dosyanızı yükleyin ve tabloları Excel formatında indirin.")

uploaded_file = st.file_uploader("Bir PDF dosyası seçin", type=["pdf"])

if uploaded_file is not None:
    if st.button("Dönüştür"):
        with st.spinner("PDF işleniyor..."):
            try:
                tables = extract_tables_from_pdf(uploaded_file)
                
                if tables:
                    # Tüm tabloları birleştir (veya tek bir Excel dosyasına farklı sayfalar olarak yazabilirsiniz)
                    combined_df = pd.concat(tables, ignore_index=True)
                    
                    # Excel dosyası oluştur
                    output = BytesIO()
                    with pd.ExcelWriter(output, engine='openpyxl') as writer:
                        combined_df.to_excel(writer, index=False)
                    
                    st.success("Dönüştürme başarılı!")
                    
                    st.download_button(
                        label="Excel Dosyasını İndir",
                        data=output.getvalue(),
                        file_name="donusturulen_dosya.xlsx",
                        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                    )
                else:
                    st.warning("PDF içerisinde okunabilir tablo bulunamadı.")
            except Exception as e:
                st.error(f"Bir hata oluştu: {e}")
