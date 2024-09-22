import pandas as pd

# อ่านไฟล์ CSV
df = pd.read_csv('file-test.csv')

df['Column2'] = df['Column1'].apply(lambda x: 'pos' if 'แฮปปี้' in str(x) else 'neg')

# บันทึกผลลัพธ์ลงในไฟล์ CSV ใหม่
df.to_csv('output_file.csv', index=False)
