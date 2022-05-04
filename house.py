import pandas as pd
import numpy as np

df = pd.read_excel('bài 3 thao tác dữ liệu\Thực hành House Đống Đa\house_price_dống-da.xlsx')
print(df.head())

# 1. Đọc bộ dữ liệu, cho biết số dòng, số cột và kiểu dữ liệu của các thuộc tính.

print(df.shape)

print(df.info())


# 2. Lọc ra các bản ghi bán nhà riêng tại phường Trung liệt hoặc phường Khâm Thiên

df1 = df[(df['type_of_land'] == 'Bán nhà riêng') & \
    ((df['ward_name'] == 'Phường Trung Liệt' )| (df['ward_name'] == 'Phường Khâm Thiên'))]\
        [['type_of_land','street_name','ward_name']]

print(df1.head())

# 3. Lọc các thông tin Địa chỉ, Giá, Hướng nhà, Hướng ban công của các bản ghi có giấy chứng nhận sổ đỏ và có 3 phòng ngủ trở lên.

df2 = df[(df['land_certificate'] == 'Sổ đỏ') & (df['bedroom'] >= 3)]\
    [['address','price','house_direction','balcony_direction']].reset_index()
print(df2.head())

# 4. Với mỗi loại nhà đất, tính trung bình cộng giá cũng như giá lớn nhất và giá nhỏ nhất.
df3 = df.groupby('type_of_land').agg(mean_values = ('price', 'mean'), max_values = ('price', 'max'),\
     min_values = ('price', 'min')).reset_index()
print(df3)

# 5. Tính trung bình cộng số phòng ngủ, số phòng vệ sinh, số tầng của mỗi phường.
df4 = df.groupby('ward_name').agg(mean_bedroom = ('bedroom','mean'),\
     mean_badroom = ('toilet','mean'), mean_floor = ('floor','mean')).reset_index()
print(df4)
# mean_bedroom = ('bedroom','mean'), mean_badroom = ('toilet','mean'), mean_floor = ('floor','mean')