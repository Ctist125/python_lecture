# 주식과 채권에서 리밸런싱을 거친 값을 계산해 적절한 비율인지를 확인하는 코드

# 내부 라이브러리 선언
import random

# 프로젝트 내 파일
import validation
import calculation

# 안내문
print("해당 프로그램은 주식과 채권의 비율이 적절한지를 확인하는 코드입니다.")
print("-------------------------------------------------------")

# 비율 유효성 검사
stock_ratio = validation.ratio_valid()
stock_ratio_float2 = "{:.2f}".format(stock_ratio)

# 채권 비율 계산
bond_ratio = 100 - stock_ratio
bond_ratio_float2 = "{:.2f}".format(bond_ratio)

print(f"주식의 비율은 {stock_ratio_float2}% 입니다.")
print(f"채권의 비율은 {bond_ratio_float2}% 입니다.")
print("-------------------------------------------------------")

# 주식 수익률 유효성 검사
stock = validation.stock_valid()

# 채권 수익률 유효성 검사
bond = validation.bond_valid()

print("-------------------------------------------------------")

# 설명문
print("손실값은 수익률의 음(-)의 값으로 계산하였습니다.")
print("-------------------------------------------------------")

# 계산 및 경과 출력
# 시작 값
print("시작 금액")
start_money = random.randint(100_000, 1_000_000)

stock_money = start_money * (stock_ratio / 100)
stock_monet_float2 = "{:.2f}".format(stock_money)

bond_money = start_money * (bond_ratio / 100)
bond_money_float2 = "{:.2f}".format(bond_money)

print(f"주식: {stock_monet_float2}원, 채권: {bond_money_float2}원, 총: {start_money}원")
print("-------------------------------------------------------")

# 1회차
print("1회차")
print("주식 이득")
result = calculation.stock_gain(stock_money, stock, bond_money, bond)

stock_money = result[0]
bond_money = result[1]
total_money = result[2]

# 리벨런싱
result = calculation.rebalancing(total_money, stock_ratio, bond_ratio)

stock_money = result[0]
bond_money = result[1]

# 2회차
print("2회차")
print("주식 손실")

result = calculation.stock_loss(stock_money, stock, bond_money, bond)

stock_money = result[0]
bond_money = result[1]
total_money = result[2]

# 리벨런싱
result = calculation.rebalancing(total_money, stock_ratio, bond_ratio)

stock_money = result[0]
bond_money = result[1]

# 3회차
print("3회차")
print("주식 손실")

result = calculation.stock_loss(stock_money, stock, bond_money, bond)

stock_money = result[0]
bond_money = result[1]
total_money = result[2]

# 리벨런싱
result = calculation.rebalancing(total_money, stock_ratio, bond_ratio)

stock_money = result[0]
bond_money = result[1]

# 4회차
print("4회차")
print("주식 이득")
result = calculation.stock_gain(stock_money, stock, bond_money, bond)

stock_money = result[0]
bond_money = result[1]
total_money = result[2]

# 해석
total_money_float2 = "{:.2f}".format((total_money))

if total_money > start_money:
    print(f"최종 금액은 {total_money_float2}원으로 좋은 비율입니다.")
elif total_money == start_money:
    print("최종 금액과 시작 금액이 같습니다. 수정을 해보시는 것은 어떻습니까?")
else:
    print(f"최종 금액은 {total_money_float2}원으로 시작 금액보다 적습니다. 비율을 수정해야 합니다.")