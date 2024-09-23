import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

data = pd.read_csv("Dashboard/main_data.csv")  

st.title("Bike Sharing Data Analysis")

st.markdown("Analisis data sewa sepeda ini bertujuan untuk mencari insight pada data dan menampilkannya dalam bentuk visualisasi")


if st.checkbox('Tampilkan dataset'):
    st.write(data)


st.markdown("""
**Pertanyaan 1 : Bagaimana tren sewa sepeda pada dari tahun 2011 hingga 2012?**
            
**Pertanyaan 2 : Bagaimana pola sewa sepeda tiap musim?**
            
**Pertanyaan 3 : Bagaimana perbandingan sewa sepeda pada hari libur dan hari kerja?**
""")

# 1. Analisis Tren berdasarkan Tahun
st.subheader("Tren Sewa Sepeda Berdasarkan Tahun")
data['mnth'] = pd.Categorical(data['mnth'], categories=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], ordered=True)
monthly_counts = data.groupby(by=["mnth", "yr"]).agg({"cnt": "sum"}).reset_index()
plt.figure(figsize=(10, 6))
sns.lineplot(data=monthly_counts, x="mnth", y="cnt", hue="yr", legend=False, marker="o")

plt.title("Tren Sewa Sepeda")
plt.xlabel(None)
plt.ylabel(None)
plt.legend(title="Tahun", loc="upper right")
plt.tight_layout()
st.pyplot(plt)

st.markdown ("Grafik menunjukkan tren sewa sepeda bulanan selama 2 tahun terakhir. Terlihat adanya peningkatan sewa sepeda setiap pertengahan tahun dan mengalami penurunan ketika mendekati akhir tahun.")

# 2. Pola Sewa Sepeda Musiman
st.subheader("Sewa Sepeda Berdasarksn Musim")
pola_musim = data.groupby('season')[['registered', 'casual']].sum().reset_index()
urutan_musim = ['spring', 'summer', 'fall', 'winter']
plt.figure(figsize=(12, 6))
plt.bar(pola_musim['season'], pola_musim['registered'], label='Registered', color='tab:pink')
plt.bar(pola_musim['season'], pola_musim['casual'], label='Casual', color='tab:blue')

plt.xlabel(None)
plt.ylabel(None)
plt.title('Jumlah penyewa sepeda berdasarkan musim')
plt.legend()
plt.show()
st.pyplot(plt)

st.markdown("Pada grafik ini terlihat jumlah penyewa sepeda paling banyak ada di musim gugur dan musim panas.")

# Korelasi penyewa sepeda dengan temperatur
st.subheader("Korelasi Jumlah Penyewa dengan Temperatur suhu")
fig, ax = plt.subplots()
sns.scatterplot(x='temp', y='registered', data=data, label='Penyewa dengan Member', color='purple', ax=ax)
sns.scatterplot(x='temp', y='casual', data=data, label='Penyewa tanpa Member', color='red', ax=ax)

ax.set_title('Korelasi Jumlah Penyewa dengan Temperatur suhu')
ax.set_xlabel('Temperatur')
ax.set_ylabel('Jumlah Penyewa')
ax.legend()
st.pyplot(fig)

st.markdown(" Kita juga dapat melihat korelasi antara banyaknya penyewa dengan temperatur suhu yang menunjukkan kesimpulan yang sama yaitu pada musim gugur dan musim panas jumlah penyewa meningkat.")



# 3. Holiday vs Working Day Comparison
st.subheader("Sewa Sepeda: Holiday vs Working Day")
plt.figure(figsize=(10,6))
sns.barplot(x='workingday', y='cnt', data=data, palette=['blue', 'red'])

plt.title('Perbandingan Penyewa Sepeda Workingday Dan Holiday')
plt.xlabel(None)
plt.ylabel('Jumlah Pengguna Sepeda')
plt.show()
st.pyplot(plt)


st.markdown("Pada Chart ini terlihat bahwa pada hari kerja jumlah sewa sepeda meningkat. Hal ini menunjukkan bahwa para penyewa sepeda menggunakan sepeda untuk beraktivitas sehari-hari seperti pergi ke kantor, ke sekolah, serta berbelanja kebutuhan sehari-hari")


st.subheader("Kesimpulan")
st.markdown("""
**Conclution pertanyaan 1 : Bagaimana tren sewa sepeda pada tahun ini?**
Tren sewa sepeda meningkat di tahun 2012. Sewa sepeda meningkat pada bulan Mei dan puncaknya pada bulan September, namun menurun pada Oktober hingga Desember

**Conclution pertanyaan 2 : Bagaimana pola sewa sepeda tiap musim?**
Pola sewa sepeda berdasarkan musim meningkat sedikit demi sedikit setiap musimnya. Dimulai dari musim semi yang menunjukkan jumlah sewa sepeda paling sedikit. Kemudian meningkat pada musim panas dan musim gugur sebagai musim dengan sewa sepeda terbanyak. Kemudian sewa sepeda sedikit menurun di musim dingin.

**Conclution pertanyaan 3 : Bagaimana perbandingan sewa sepeda pada hari libur dan hari kerja?**
Jumlah sewa sepeda paling banyak terjadi pada hari kerja. Hal ini menunjukkan bahwa penyewa menggunakan sepeda untuk kegiatan sehari-hari seperti bekerja, sekolah, membeli bahan makanan dan kegiatan lainnya.
""")

st.caption('Copyright © Marsella Vindriani')
