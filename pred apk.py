
import streamlit as st
import joblib
import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_squared_error

# Load model
model = joblib.load("berlian.sav")

# Judul aplikasi
st.title("Aplikasi Prediksi Harga Berlian")

# Input dari pengguna

# Map input ke numerik (jika diperlukan)
cut_mapping = {"Fair": 0, "Good": 1, "Very Good": 2, "Premium": 3, "Ideal": 4}
color_mapping = {"D": 0, "E": 1, "F": 2, "G": 3, "H": 4, "I": 5, "J": 6}
clarity_mapping = {"I1": 0, "SI2": 1, "SI1": 2, "VS2": 3, "VS1": 4, "VVS2": 5, "VVS1": 6, "IF": 7}

with st.sidebar:
    st.sidebar.header("Masukan Nilai")
    cut = st.selectbox("Pilih Potongan",list(cut_mapping.keys()))
    color = st.selectbox("Pilih Color",list(color_mapping.keys()))
    clarity = st.selectbox("Pilih Clarity",list(clarity_mapping.keys()))
    carat = st.slider("masukan carar")
    depth = st.slider("masukan depty")
    table = st.slider("masukan table")
    x = st.slider("masukan x")
    y = st.slider("masukan y")
    z = st.slider("masukan z")

cut_num = cut_mapping[cut]
color_num = color_mapping[color]
clarity_num = clarity_mapping[clarity]

input_data = np.array([[carat, cut_num, color_num, clarity_num, depth, table,x,y,z]])
prediction = model.predict(input_data)




# Tampilkan hasil prediksi
st.write("### Harga Prediksi Berlian:")
st.write(f"${prediction[0]:,.2f}")