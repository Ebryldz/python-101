import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

df = pd.read_csv('/Users/ebruyildiz/Desktop/python 101/housing.csv')

plt.figure(figsize=(10,6))
plt.hist(df['area'], bins=30, color='skyblue', edgecolor='black')
plt.title('Area ile Ev Fiyatları İlişkisi')
plt.xlabel('Alan (metrekare)')
plt.ylabel('Ev Fiyatları')
plt.show()

plt.figure(figsize=(10,6))
plt.hist(df['bedrooms'], bins=30, color='lightgreen', edgecolor='black')
plt.title('Bedrooms ile Ev Fiyatları İlişkisi')
plt.xlabel('Yatak Odası Sayısı')
plt.ylabel('Ev Fiyatları')
plt.show()

plt.figure(figsize=(10,6))
plt.hist(df['stories'], bins=30, color='lightcoral', edgecolor='black')
plt.title('Stories ile Ev Fiyatları İlişkisi')
plt.xlabel('Kat Sayısı')
plt.ylabel('Ev Fiyatları')
plt.show()

bathroom_avg_price = df.groupby('bathrooms')['price'].mean()
bathroom_avg_price.plot(kind='bar', color='lightblue', edgecolor='black', figsize=(10,6))
plt.title('Banyo Sayısına Göre Ortalama Ev Fiyatları')
plt.xlabel('Banyo Sayısı')
plt.ylabel('Ortalama Ev Fiyatları')
plt.show()

furnishing_avg_price = df.groupby('furnishingstatus')['price'].mean()
furnishing_avg_price.plot(kind='bar', color='lightgreen', edgecolor='black', figsize=(10,6))
plt.title('Döşeme Durumuna Göre Ortalama Ev Fiyatları')
plt.xlabel('Döşeme Durumu')
plt.ylabel('Ortalama Ev Fiyatları')
plt.show()

plt.figure(figsize=(12,8))
corr_matrix = df.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Korelasyon Matrisi')
plt.show()