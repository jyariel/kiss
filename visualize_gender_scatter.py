# visualize_gender_scatter.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from numpy.polynomial.polynomial import polyfit
import numpy as np
import os

# 讀取資料
df = pd.read_excel("data/DATA_Kiss_count_gender_and_IQ.xlsx")
df['Gender'] = df['Gender'].astype(str)

# 建立資料夾
os.makedirs("plots", exist_ok=True)

# 平均值（每個年齡的平均 Kiss Count）
age_kiss_avg = df.groupby('Age of First Kiss')['Kiss Count'].mean()

# 畫圖開始
plt.figure(figsize=(10, 6))
sns.set(style="whitegrid")

# 分別畫出性別資料點
male = df[df['Gender'] == 'male']
female = df[df['Gender'] == 'female']
plt.scatter(male['Age of First Kiss'], male['Kiss Count'], color='orange', alpha=0.6, s=40, label='Male')
plt.scatter(female['Age of First Kiss'], female['Kiss Count'], color='gold', alpha=0.6, s=40, label='Female')

# 畫平均線
sns.lineplot(x=age_kiss_avg.index, y=age_kiss_avg.values, marker='o', label='Average Kiss Count', color='teal')

# 畫趨勢線（回歸）
b, m = polyfit(df['Age of First Kiss'], df['Kiss Count'], 1)
x = np.linspace(df['Age of First Kiss'].min(), df['Age of First Kiss'].max(), 100)
y = m * x + b
plt.plot(x, y, color='red', linestyle='--', label='Trend Line')

# 標題與圖例
plt.title("Kiss Count vs Age of First Kiss\n(Gender Scatter + Average + Trend)")
plt.xlabel("Age of First Kiss")
plt.ylabel("Kiss Count")
plt.legend()
plt.tight_layout()

# 儲存圖檔
plt.savefig("plots/kiss_vs_age_gender_colored.png")
print("✅ 圖片已儲存：plots/kiss_vs_age_gender_colored.png")
