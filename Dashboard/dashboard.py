import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Judul Dashboard
st.title("E-Commerce Dashboard")

# dataset
data = pd.read_csv('https://raw.githubusercontent.com/luqmanfh/Data-Analysis/main/Dashboard/all_data.csv')

# Sidebar Options
st.sidebar.header("Pilihan Analisis")
analysis_choice = st.sidebar.selectbox(
    "Pilih Analisis:",
    ["Metode Pembayaran Paling Sering Digunakan", "Kategori Produk dengan Pendapatan Tertinggi"]
)

# Analisis 1: Metode Pembayaran Paling Sering Digunakan
if analysis_choice == "Metode Pembayaran Paling Sering Digunakan":
    st.subheader("Metode Pembayaran Paling Sering Digunakan")

    # Hitung metode pembayaran
    payment_counts = data['payment_type'].value_counts()

    # Visualisasi
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.barplot(x=payment_counts.values, y=payment_counts.index, palette="viridis", ax=ax)
    ax.set_title("Metode Pembayaran Paling Sering Digunakan", fontsize=16)
    ax.set_xlabel("Jumlah Penggunaan", fontsize=12)
    ax.set_ylabel("Metode Pembayaran", fontsize=12)
    st.pyplot(fig)

# Analisis 2: Kategori Produk dengan Pendapatan Tertinggi
elif analysis_choice == "Kategori Produk dengan Pendapatan Tertinggi":
    st.subheader("Kategori Produk dengan Pendapatan Tertinggi")

    # Pastikan dataset memiliki kolom 'price' dan 'product_category_name'
    if 'price' in data.columns and 'product_category_name' in data.columns:
        revenue_by_category = data.groupby('product_category_name')['price'].sum().sort_values(ascending=False)

        # Visualisasi
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.barplot(x=revenue_by_category.values[:10], y=revenue_by_category.index[:10], palette="coolwarm", ax=ax)
        ax.set_title("Kategori Produk dengan Pendapatan Tertinggi", fontsize=16)
        ax.set_xlabel("Total Pendapatan", fontsize=12)
        ax.set_ylabel("Kategori Produk", fontsize=12)
        st.pyplot(fig)
    else:
        st.error("Kolom 'price' dan/atau 'product_category_name' tidak ditemukan dalam dataset.")

else:
    st.write("Silakan upload file CSV untuk memulai analisis.")
