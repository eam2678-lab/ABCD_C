# -*- coding: utf-8 -*-
import pandas as pd

# Excel 파일 경로
file_path = r'C:\202525004 김준우\20250909\data.xlsx'

# Excel 파일 읽기
df = pd.read_excel(file_path)

# 데이터 확인
print("데이터 크기:", df.shape)
print("\n컬럼명:", df.columns.tolist())
print("\n첫 5행 데이터:")
print(df.head())
print("\n데이터 타입:")
print(df.dtypes)

# 데이터가 올바르게 분리되었는지 확인
if df.shape[1] >= 4:  # 이름, 국어, 영어, 수학 = 4개 컬럼
    print("\n데이터가 올바르게 분리되어 있습니다.")
    
    # 컬럼명 추정 (첫 번째는 이름, 나머지는 점수)
    name_col = df.columns[1]
    korean_col = df.columns[2] 
    english_col = df.columns[3]
    math_col = df.columns[4]
    
    print(f"추정 컬럼: 이름={name_col}, 국어={korean_col}, 영어={english_col}, 수학={math_col}")
    
    try:
        # 숫자 컬럼을 numeric으로 변환
        df[korean_col] = pd.to_numeric(df[korean_col], errors='coerce')
        df[english_col] = pd.to_numeric(df[english_col], errors='coerce')
        df[math_col] = pd.to_numeric(df[math_col], errors='coerce')
        
        # 각 과목별 평균 점수 계산
        korean_avg = df[korean_col].mean()
        english_avg = df[english_col].mean()
        math_avg = df[math_col].mean()
        
        # 결과 출력
        print("\n=== 과목별 평균 점수 ===")
        print(f"국어 평균: {korean_avg:.2f}점")
        print(f"영어 평균: {english_avg:.2f}점") 
        print(f"수학 평균: {math_avg:.2f}점")
        
        # 각 학생별 평균 점수 계산
        df['개인평균'] = (df[korean_col] + df[english_col] + df[math_col]) / 3
        print("\n=== 학생별 평균 점수 ===")
        for i, row in df.iterrows():
            if pd.notna(row['개인평균']):
                print(f"{row[name_col]}: {row['개인평균']:.2f}점")
                
    except Exception as e:
        print(f"평균 계산 중 오류: {e}")
        
else:
    print("\n데이터가 올바르게 분리되지 않았습니다.")
    print("Excel 파일의 데이터 형식을 확인해주세요.")
    print("각 데이터가 별도의 셀에 있어야 합니다.")