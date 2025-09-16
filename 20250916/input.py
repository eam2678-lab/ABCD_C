# -*- coding: utf-8 -*-

# 방법 1: 기본적인 중첩 반복문
def basic_multiplication_table():
    print("=== 기본 구구단 (2단~9단) ===")
    for i in range(2, 10):
        print(f"\n[{i}단]")
        for j in range(1, 10):
            print(f"{i} × {j} = {i * j}")

# 방법 2: 한 줄에 모든 단 출력
def horizontal_multiplication_table():
    print("=== 가로 형태 구구단 ===")
    for j in range(1, 10):
        for i in range(2, 10):
            print(f"{i}×{j}={i*j:2d}", end="  ")
        print()  # 줄바꿈

# 방법 3: 특정 단만 출력
def specific_table(num):
    print(f"=== {num}단 ===")
    for i in range(1, 10):
        print(f"{num} × {i} = {num * i}")

# 방법 4: 사용자 입력받아 구구단 출력
def interactive_table():
    try:
        num = int(input("몇 단을 출력하시겠습니까? (2~9): "))
        if 2 <= num <= 9:
            specific_table(num)
        else:
            print("2~9 사이의 숫자를 입력해주세요.")
    except ValueError:
        print("올바른 숫자를 입력해주세요.")

# 방법 5: 예쁘게 정렬된 구구단
def formatted_table():
    print("=== 정렬된 구구단 ===")
    print("단\\곱", end="")
    for j in range(1, 10):
        print(f"{j:4d}", end="")
    print()
    print("-" * 40)
    
    for i in range(2, 10):
        print(f"{i:2d} ", end="")
        for j in range(1, 10):
            print(f"{i*j:4d}", end="")
        print()

# 방법 6: 리스트 컴프리헨션 사용
def list_comprehension_table():
    print("=== 리스트 컴프리헨션으로 구구단 ===")
    tables = [[f"{i} × {j} = {i*j}" for j in range(1, 10)] for i in range(2, 10)]
    
    for i, table in enumerate(tables, 2):
        print(f"\n[{i}단]")
        for equation in table:
            print(equation)

# 터미널에서 구구단수 입력받기
def input_multiplication_table():
    """터미널에서 구구단수를 입력받아 해당 구구단을 출력하는 함수"""
    print("=== 구구단 프로그램 ===")
    
    while True:
        try:
            # 사용자로부터 구구단수 입력받기
            num = input("출력할 구구단수를 입력하세요 (1~19, 종료는 'q' 또는 'quit'): ")
            
            # 종료 조건 확인
            if num.lower() in ['q', 'quit']:
                print("프로그램을 종료합니다.")
                break
            
            # 숫자로 변환
            num = int(num)
            
            # 유효한 범위 확인 (1~9단까지 허용)
            if 1 <= num <= 9:
                print(f"\n{'='*20}")
                print(f"      {num}단")
                print(f"{'='*20}")
                
                for i in range(1, 10):
                    result = num * i
                    print(f"{num} × {i} = {result}")
                
                print(f"{'='*20}\n")
                
                # 계속 진행할지 묻기
                continue_choice = input("다른 구구단을 보시겠습니까? (y/n): ")
                if continue_choice.lower() not in ['y', 'yes', '']:
                    print("프로그램을 종료합니다.")
                    break
                    
            else:
                print("⚠️  1~9 사이의 숫자를 입력해주세요!\n")
                
        except ValueError:
            print("⚠️  올바른 숫자를 입력해주세요! (종료는 'q')\n")
        except KeyboardInterrupt:
            print("\n\n프로그램을 종료합니다.")
            break

# 여러 구구단을 한 번에 입력받는 함수
def multiple_tables():
    """여러 개의 구구단수를 한 번에 입력받아 출력하는 함수"""
    print("=== 여러 구구단 출력 ===")
    
    try:
        input_str = input("출력할 구구단들을 입력하세요 (예: 2,3,5 또는 2 3 5): ")
        
        # 쉼표나 공백으로 분리
        if ',' in input_str:
            numbers = input_str.split(',')
        else:
            numbers = input_str.split()
        
        # 각 숫자에 대해 구구단 출력
        for num_str in numbers:
            try:
                num = int(num_str.strip())
                if 1 <= num <= 9:
                    print(f"\n{'='*15} {num}단 {'='*15}")
                    for i in range(1, 10):
                        print(f"{num} × {i} = {num * i}")
                else:
                    print(f"⚠️  {num}은(는) 1~9 범위를 벗어났습니다.")
            except ValueError:
                print(f"⚠️  '{num_str.strip()}'은(는) 올바른 숫자가 아닙니다.")
                
    except KeyboardInterrupt:
        print("\n프로그램을 종료합니다.")

# 실행 예시
if __name__ == "__main__":
    print("구구단 프로그램을 선택하세요:")
    print("1. 단일 구구단 (반복 입력)")
    print("2. 여러 구구단 (한 번에 입력)")
    
    choice = input("\n선택 (1 또는 2): ")
    
    if choice == "1":
        input_multiplication_table()
    elif choice == "2":
        multiple_tables()
    else:
        print("기본 단일 구구단으로 실행합니다.")
        input_multiplication_table()