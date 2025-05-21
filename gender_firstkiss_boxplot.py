# gender_firstkiss_boxplot.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# 讀取資料
df = pd.read_excel("data/DATA_Kiss_count_gender_and_IQ.xlsx")
df['Gender'] = df['Gender'].astype(str)

# 建立輸出資料夾
os.makedirs("plots", exist_ok=True)

# 繪製 Boxplot
plt.figure(figsize=(8, 6))
sns.set(style="whitegrid")

# 使用 palette 區分性別上色
sns.boxplot(x='Gender', y='Age of First Kiss', data=df, palette={'male': 'orange', 'female': 'gold'})

# 加上標題與軸標籤
plt.title("Age of First Kiss by Gender (Boxplot)")
plt.xlabel("Gender")
plt.ylabel("Age of First Kiss")
plt.tight_layout()

# 儲存圖檔
output_path = "plots/age_first_kiss_by_gender_colored.png"
plt.savefig(output_path)
print(f"✅ 圖片已儲存：{output_path}")
