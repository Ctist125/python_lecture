# 주식과 채권에서 리밸런싱을 거친 값을 계산해 적절한 비율인지를 확인하는 코드

# 안내문
print("해당 프로그램은 주식과 채권의 비율이 적절한지를 확인하는 코드입니다.")
print("-------------------------------------------------------")

# 비율 받아오기
stock_ratio = float(input("주식의 비율을 입력해 주십시오. : "))
stock_ratio_float2 = "{:.2f}".format(stock_ratio)

bond_ratio = 100 - stock_ratio
bond_ratio_float2 = "{:.2f}".format(bond_ratio)
print(f"주식의 비율은 {stock_ratio_float2}% 입니다.")
print(f"채권의 비율은 {bond_ratio_float2}% 입니다.")
print("-------------------------------------------------------")

# 계획 수익률 받아오기
stock = float(input("주식으로 계획하는 최대 수익률(%)을 입력해 주십시오. : "))
bond = float(input("채권으로 계획하는 수익률(%)을 입력해 주십시오. : "))
print("-------------------------------------------------------")

# 설명문
print("손실값은 수익률의 음(-)의 값으로 계산하였습니다.")
print("-------------------------------------------------------")

# 계산 및 경과 출력
# 시작 값
total_money = 100_000
stock_money = total_money * (stock_ratio / 100)
bond_money = total_money * (bond_ratio / 100)

# 1회차
print("1회차")
print("주식 이득")
stock_money = stock_money + (stock_money * (stock / 100))
bond_money = bond_money + (bond_money * (bond / 100))
total_money = stock_money + bond_money

stock_money_float2 = "{:.2f}".format(stock_money)
bond_money_float2 = "{:.2f}".format(bond_money)
total_money_float2 = "{:.2f}".format((total_money))

print(f"주식: {stock_money_float2}원, 채권: {bond_money_float2}원, 총: {total_money_float2}")
print("-------------------------------------------------------")

# 리벨런싱
stock_money = total_money * (stock_ratio / 100)
bond_money = total_money * (bond_ratio / 100)
print("리밸런싱")
print("-------------------------------------------------------")

# 2회차
print("2회차")
print("주식 손실")
stock_money = stock_money - (stock_money * (stock / 100))
bond_money = bond_money + (bond_money * (bond / 100))
total_money = stock_money + bond_money

stock_money_float2 = "{:.2f}".format(stock_money)
bond_money_float2 = "{:.2f}".format(bond_money)
total_money_float2 = "{:.2f}".format((total_money))

print(f"주식: {stock_money_float2}원, 채권: {bond_money_float2}원, 총: {total_money_float2}")
print("-------------------------------------------------------")

# 리벨런싱
stock_money = total_money * (stock_ratio / 100)
bond_money = total_money * (bond_ratio / 100)
print("리밸런싱")
print("-------------------------------------------------------")

# 3회차
print("3회차")
print("주식 손실")
stock_money = stock_money - (stock_money * (stock / 100))
bond_money = bond_money + (bond_money * (bond / 100))
total_money = stock_money + bond_money

stock_money_float2 = "{:.2f}".format(stock_money)
bond_money_float2 = "{:.2f}".format(bond_money)
total_money_float2 = "{:.2f}".format((total_money))

print(f"주식: {stock_money_float2}원, 채권: {bond_money_float2}원, 총: {total_money_float2}")
print("-------------------------------------------------------")

# 리벨런싱
stock_money = total_money * (stock_ratio / 100)
bond_money = total_money * (bond_ratio / 100)
print("리밸런싱")
print("-------------------------------------------------------")

# 4회차
print("4회차")
print("주식 이득")
stock_money = stock_money + (stock_money * (stock / 100))
bond_money = bond_money + (bond_money * (bond / 100))
total_money = stock_money + bond_money

stock_money_float2 = "{:.2f}".format(stock_money)
bond_money_float2 = "{:.2f}".format(bond_money)
total_money_float2 = "{:.2f}".format((total_money))

print(f"주식: {stock_money_float2}원, 채권: {bond_money_float2}원, 총: {total_money_float2}")
print("-------------------------------------------------------")

# 해석법
print("초기 자금보다, 늘었다면 진행하시고, 줄었다면 수정하시면 됩니다.")