# 비율 유효성 검사
def ratio_valid():
    ratio_vaild = False

    while not ratio_vaild:
        # 비율 받아오기
        stock_ratio = float(input("주식의 비율을 입력해 주십시오. : "))

        if stock_ratio > 0 and stock_ratio < 100:
            return stock_ratio
        else:
            print("잘못된 값을 입력하셨습니다.")
            print("-------------------------------------------------------")

# 주식 수익률 유효성 검사
def stock_valid():
    stock_valid = False

    while not stock_valid:
        # 주식 계획 수익률 받아오기
        stock = float(input("주식으로 계획하는 최대 수익률(%)을 입력해 주십시오. : "))

        if stock > 0:
            return stock
        else:
            print("잘못된 값을 입력하셨습니다.")
            print("-------------------------------------------------------")

# 채권 수익률 유효성 검사
def bond_valid():
    bond_vaild = False

    while not bond_vaild:
        # 채권 계획 수익률 받아오기
        bond = float(input("채권으로 계획하는 수익률(%)을 입력해 주십시오. : "))

        if bond > 0:
            return bond
        else:
            print("잘못된 값을 입력하셨습니다.")
            print("-------------------------------------------------------")