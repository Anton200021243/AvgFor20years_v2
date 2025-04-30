import pandas as pd

file_path = r"C:\Users\user\PycharmProjects\AvgFor20years\Pogoda.xls"

df = pd.read_excel(file_path, skiprows=6, engine="xlrd")

df.columns = [col.strip() for col in df.columns]

df['Местное время в Москве (ВДНХ)'] = pd.to_datetime(df['Местное время в Москве (ВДНХ)'], format="%d.%m.%Y %H:%M")

target_hours = ['09:00', '12:00', '15:00', '18:00']
df_filtered = df[df['Местное время в Москве (ВДНХ)'].dt.strftime('%H:%M').isin(target_hours)]

df_filtered['Дата'] = df_filtered['Местное время в Москве (ВДНХ)'].dt.date
df_filtered['Год'] = df_filtered['Местное время в Москве (ВДНХ)'].dt.year

df_result = df_filtered.groupby(['Год', 'Дата'])['T'].mean().reset_index()
df_result.rename(columns={'T': 'Среднесуточная температура'}, inplace=True)

df_result.to_excel("среднесуточная_температура.xlsx", index=False)

print("Файл успешно сохранён как 'среднесуточная_температура.xlsx'")
