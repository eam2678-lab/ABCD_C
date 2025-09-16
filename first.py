
a = 'pig'
b = 'dad'

print (a)
print (b)
print (a + b)

import pandas as pd

# Excel 파일 읽기 (기본 버전)
df = pd.read_excel(r"C:\claude\ABCD-C\2025.09.09\data.xlsx")
print(df)

# 추가 옵션들:
# 특정 시트 읽기: df = pd.read_excel(file_path, sheet_name='Sheet1')
# 특정 범위 읽기: df = pd.read_excel(file_path, usecols='A:D', nrows=100)
# 첫 번째 행을 헤더로 사용 안함: df = pd.read_excel(file_path, header=None)

# 간단한 데이터 확인
print(f"크기: {df.shape}")
print(df.head())

# Excel 파일 읽기
df = pd.read_excel(r"C:\claude\ABCD-C\2025.09.09\data.xlsx")

# 데이터 확인
print("원본 데이터:")
print(df)
print()

# 각 학생의 평균 점수 계산
df['평균'] = df[['국어', '수학', '영어']].mean(axis=1)

print("평균 점수가 추가된 데이터:")
print(df)
print()

# 과목별 평균
print("과목별 평균:")
print(f"국어 평균: {df['국어'].mean():.2f}점")
print(f"수학 평균: {df['수학'].mean():.2f}점") 
print(f"영어 평균: {df['영어'].mean():.2f}점")
print(f"전체 평균: {df['평균'].mean():.2f}점")
print()

# 학생별 평균 점수만 보기
print("학생별 평균 점수:")
for i, row in df.iterrows():
    print(f"{row['이름']}: {row['평균']:.2f}점")

# 결과를 새 Excel 파일로 저장
df.to_excel(r"C:\claude\ABCD-C\2025.09.09\결과_평균포함.xlsx", index=False)
print("\n결과가 '결과_평균포함.xlsx'로 저장되었습니다.")