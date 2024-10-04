# @FileName  :merge.py
# @Time      :2024/7/13 11:32
# @Author    :Papersheep

import pandas as pd


df1 = pd.read_csv('restaurants.csv')
df2 = pd.read_csv('restaurant_reviews.csv')

# 根据共同列合并数据
merged_df = pd.merge(df2, df1, on='Restaurant Name', how='left')

# save
merged_df.to_csv('merged_file.csv', index=False)


if __name__ == "__main__":
    run_code = 0
