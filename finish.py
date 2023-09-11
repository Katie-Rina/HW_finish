import pandas as pd

# Создаем DataFrame
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Получаем уникальные значения столбца
unique_values = data['whoAmI'].unique()

# Создаем новые столбцы 'one_hot_'
for value in unique_values:
    data['one_hot_' + value] = (data['whoAmI'] == value).astype(int)

data.head()